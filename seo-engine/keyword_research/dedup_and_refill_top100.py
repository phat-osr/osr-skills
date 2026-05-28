"""
Dedup + refill top 100 keywords for Phase 1.

Problems found in current top 100:
  - 12 variations of "business model canvas example" (same intent)
  - 6 variations of "fdi vietnam"
  - 5 variations of "powerpoint pitch deck template"
  - 9 variations of "lean canvas + lean startup"
  - 5 variations of "vibe coding tools"
  - Generic/off-topic: "vietnamese store", "poverty in vietnam", "reddit vibe coding"

Fix:
  1. Canonicalize each keyword → sorted unique meaningful tokens (drop stopwords + brand qualifiers)
  2. Group by canonical form, keep highest signal_score per group
  3. Filter off-topic terms (extra negative tokens)
  4. Refill remaining slots from full DFS pool with deduped candidates
  5. Wipe Keywords table + insert clean top 100

Run:
    python dedup_and_refill_top100.py --batch-id OSR-B-20260521 --dry-run
    python dedup_and_refill_top100.py --batch-id OSR-B-20260521
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
import time
from collections import defaultdict
from pathlib import Path

import requests

from airtable_helpers import fetch_all
from config_kw import (
    AIRTABLE_API_BASE, AIRTABLE_BASE_ID, AIRTABLE_PAT, OUTPUT_DIR,
)
from populate_keywords import categorize, signal_score

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from table_ids import TABLE_IDS  # noqa: E402

HEADERS = {"Authorization": f"Bearer {AIRTABLE_PAT}", "Content-Type": "application/json"}
KEYWORDS_TID = TABLE_IDS["Keywords"]
CSV_PATH = OUTPUT_DIR / "dfs_candidates.csv"

# Extra noise (beyond populate_keywords.NEGATIVE_TOKENS)
EXTRA_NEGATIVE = [
    "vietnamese store",   # generic ecommerce, not OSR-relevant
    "poverty",            # sensitive, off-topic
    "reddit",             # forum thread reference, low quality
    " ppt ", "ppt template", "ppt for", "template ppt",  # PPT downloads = thin content
    "powerpoint",         # same — file download intent
    "définition",         # foreign-language artifacts
    "free download", "pdf download",
    ".pdf", "book pdf",   # pure PDF intent
]

# Stopwords + filler to ignore during canonicalization
STOPWORDS = {
    "a", "an", "the", "of", "for", "to", "in", "on", "with", "by", "from",
    "and", "or", "is", "are", "what", "how", "why", "when", "where", "who",
    "example", "examples", "sample", "samples", "template", "templates",
    "model", "models",
    "into",
}


def canonicalize(kw: str) -> str:
    """Return sorted unique-token signature for dedup grouping.

    'business model canvas examples' → 'business canvas'
    'examples of business model canvas' → 'business canvas'
    'pitch deck powerpoint template' → 'deck pitch'
    """
    k = re.sub(r"[^a-z0-9\s]", " ", kw.lower())
    tokens = [t for t in k.split() if t and t not in STOPWORDS]
    # dedup tokens preserving order, then sort for stable signature
    seen = set()
    uniq = []
    for t in tokens:
        if t not in seen:
            seen.add(t)
            uniq.append(t)
    return " ".join(sorted(uniq))


def has_extra_noise(kw: str) -> bool:
    k = kw.lower()
    return any(t in k for t in EXTRA_NEGATIVE)


def load_pool() -> list[dict]:
    if not CSV_PATH.exists():
        raise FileNotFoundError(CSV_PATH)
    with CSV_PATH.open() as fp:
        rows = list(csv.DictReader(fp))
    print(f"Loaded {len(rows)} raw candidates from {CSV_PATH.name}")

    scored = []
    for c in rows:
        kw = (c.get("keyword") or "").strip().lower()
        if not kw or len(kw) < 4:
            continue
        if has_extra_noise(kw):
            continue
        vol = int(c.get("search_volume") or 0)
        kd = int(c.get("keyword_difficulty") or 0)
        cpc = float(c.get("cpc") or 0)
        score = signal_score(kw, vol, kd, cpc)
        if score == 0:
            continue
        scored.append({
            "keyword": kw, "vol": vol, "kd": kd, "cpc": cpc,
            "score": score, "bucket": categorize(kw, c.get("bucket", "")),
            "seed": c.get("seed", ""),
            "canonical": canonicalize(kw),
        })
    print(f"After noise+extra filter: {len(scored)} candidates")
    return scored


def dedup_keep_top(scored: list[dict]) -> list[dict]:
    """Group by canonical form, keep highest-signal per group."""
    groups: dict[str, list[dict]] = defaultdict(list)
    for c in scored:
        groups[c["canonical"]].append(c)
    uniques = []
    merged_count = 0
    for canon, group in groups.items():
        group.sort(key=lambda r: r["score"], reverse=True)
        winner = group[0]
        winner["variants"] = len(group)
        if len(group) > 1:
            merged_count += len(group) - 1
        uniques.append(winner)
    print(f"After dedup: {len(uniques)} unique keywords (merged {merged_count} variants)")
    return uniques


def diversified_top(uniques: list[dict], n: int = 100) -> list[dict]:
    """Pick top n with diversification: cap per bucket to avoid framework-only.

    Target bucket caps (out of 100):
      vn_vc:       30  (main objective per OSR plan)
      framework:   25
      validation:  20  (OSR compete-on)
      ai_build:    15
      fundraising: 10
    """
    caps = {"vn_vc": 30, "framework": 25, "validation": 20,
            "ai_build": 15, "fundraising": 10, "other": 5}
    uniques.sort(key=lambda r: r["score"], reverse=True)
    picked: list[dict] = []
    counts: dict[str, int] = defaultdict(int)
    overflow: list[dict] = []
    for c in uniques:
        b = c["bucket"]
        if counts[b] < caps.get(b, 5):
            picked.append(c)
            counts[b] += 1
            if len(picked) >= n:
                break
        else:
            overflow.append(c)
    # If we didn't fill 100 (some buckets ran out), refill from overflow by raw signal
    if len(picked) < n:
        overflow.sort(key=lambda r: r["score"], reverse=True)
        for c in overflow:
            picked.append(c)
            if len(picked) >= n:
                break
    return picked[:n]


def fetch_existing() -> list[dict]:
    return fetch_all(KEYWORDS_TID, fields=[])


def wipe_all(ids: list[str]) -> int:
    deleted = 0
    for i in range(0, len(ids), 10):
        chunk = ids[i:i + 10]
        params = [("records[]", rid) for rid in chunk]
        r = requests.delete(
            f"{AIRTABLE_API_BASE}/{AIRTABLE_BASE_ID}/{KEYWORDS_TID}",
            headers=HEADERS, params=params, timeout=30,
        )
        if r.status_code >= 400:
            print(f"  delete chunk {i} failed: {r.status_code} {r.text[:200]}")
            raise RuntimeError("wipe failed")
        deleted += len(chunk)
        time.sleep(0.22)
    return deleted


def insert(records: list[dict]) -> int:
    inserted = 0
    for i in range(0, len(records), 10):
        chunk = records[i:i + 10]
        payload = {"records": [{"fields": r} for r in chunk], "typecast": True}
        r = requests.post(
            f"{AIRTABLE_API_BASE}/{AIRTABLE_BASE_ID}/{KEYWORDS_TID}",
            headers=HEADERS, json=payload, timeout=30,
        )
        if r.status_code >= 400:
            print(f"  insert chunk {i} failed: {r.status_code} {r.text[:300]}")
            raise RuntimeError("insert failed")
        inserted += len(chunk)
        time.sleep(0.22)
    return inserted


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch-id", default="OSR-B-20260521")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    pool = load_pool()
    uniques = dedup_keep_top(pool)
    top100 = diversified_top(uniques, 100)

    # Stats
    from collections import Counter
    bucket_dist = Counter(c["bucket"] for c in top100)
    vol_total = sum(c["vol"] for c in top100)
    avg_kd = sum(c["kd"] for c in top100) / max(len(top100), 1)
    avg_score = sum(c["score"] for c in top100) / max(len(top100), 1)
    print()
    print(f"=== Top 100 after dedup + diversification ===")
    print(f"  bucket distribution: {dict(bucket_dist)}")
    print(f"  total search volume: {vol_total:,}")
    print(f"  avg KD: {avg_kd:.1f}")
    print(f"  avg signal: {avg_score:.1f}")
    print()
    print(f"  {'#':<4} {'signal':<7} {'vol':<7} {'kd':<4} {'bucket':<13} {'var':<4} keyword")
    for i, c in enumerate(top100, 1):
        var = f"x{c.get('variants',1)}" if c.get('variants',1) > 1 else ""
        print(f"  {i:<4} {c['score']:<7} {c['vol']:<7} {c['kd']:<4} {c['bucket'][:12]:<13} {var:<4} {c['keyword'][:55]}")

    if args.dry_run:
        print("\n[dry-run]")
        return 0

    print("\n=== Wipe existing Keywords ===")
    existing = fetch_existing()
    print(f"  {len(existing)} rows to delete")
    if existing:
        n = wipe_all([r["id"] for r in existing])
        print(f"  deleted {n}")

    print(f"\n=== Insert {len(top100)} clean keywords ===")
    records = []
    for i, c in enumerate(top100, start=1):
        records.append({
            "keyword_id": f"KW-{args.batch_id}-{i:03d}",
            "keyword": c["keyword"],
            "keyword_lang": "en",
            "seed_parent": c["seed"],
            "discovery_source": ["dataforseo"],
            "volume_global_en": c["vol"],
            "difficulty_proxy": c["kd"],
            "signal_score": c["score"],
            "cpc": c["cpc"],
            "bucket": c["bucket"],
            "batch_id": args.batch_id,
            "status": "enriched",
        })
    n = insert(records)
    print(f"  inserted {n}")

    print("\nDone.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
