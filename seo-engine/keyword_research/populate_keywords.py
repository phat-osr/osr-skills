"""
Repopulate Keywords table:
  1. Wipe existing 2018 rows
  2. Add new fields: signal_score (number), cpc (number), bucket (text)
  3. Load output/dfs_candidates.csv (1448 keywords)
  4. Compute signal_score per keyword (OSR objective formula)
  5. Sort by signal_score desc + insert into Airtable

Signal formula (from plan Section 2.2):
  base = min(40, log10(volume + 1) * 12)
  + 25 if "vietnam" in keyword             (main objective)
  + 20 if framework canon (BMC, VPC, lean canvas, blue ocean, jtbd, shape up)
  + 20 if validation (validate, mvp, pmf, customer development)
  + 15 if AI-build (vibe coding, claude code, cursor, lovable, v0)
  + 15 if fundraising (raise seed, pitch deck, vc, term sheet)
  + 10 if cpc > $5, +5 if cpc > $2
  - kd * 0.4

Run:
    python populate_keywords.py --dry-run
    python populate_keywords.py
"""
from __future__ import annotations

import argparse
import csv
import math
import sys
import time
from pathlib import Path
from typing import Any

import requests

from airtable_helpers import fetch_all
from config_kw import (
    AIRTABLE_API_BASE, AIRTABLE_BASE_ID, AIRTABLE_META_BASE, AIRTABLE_PAT,
    OUTPUT_DIR,
)

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from table_ids import TABLE_IDS  # noqa: E402

HEADERS = {"Authorization": f"Bearer {AIRTABLE_PAT}", "Content-Type": "application/json"}
KEYWORDS_TID = TABLE_IDS["Keywords"]
CSV_PATH = OUTPUT_DIR / "dfs_candidates.csv"


# ----------------------------- Signal scoring -----------------------------

# Negative tokens — keywords mostly noise (history/culture/food/tourism), not OSR-relevant
NEGATIVE_TOKENS = [
    "war", "movie", "movies", "film", "song", "music", "near me",
    "mythology", "mythical", "dragon", "flag", "army", "soldier", "veteran",
    "food", "pho", "noodle", "restaurant", "recipe", "dish", "rolls",
    "religion", "buddhist", "temple", "tour", "tourism", "travel", "visa",
    "korean", "thailand", "philippines", "indonesia", "malaysia", "japan",
    "north vietnam", "south vietnam", "hanoi", "ho chi minh", "saigon",
    "dong", "currency conversion", "exchange rate", "embassy", "passport",
    "weather", "climate", "wedding", "dress", "shopping", "souvenir",
    "free download", "free pdf", "torrent", "crack", "mod apk",
    "salary", "income tax", "ielts", "duolingo",
]

FRAMEWORK_TOKENS = [
    "business model canvas", "value proposition canvas", "lean canvas",
    "lean startup", "blue ocean", "shape up", "jobs to be done", "jtbd",
    "north star metric", "strategyzer", "strategy canvas", "four actions",
]
VALIDATION_TOKENS = [
    "validate", "validation", "minimum viable product", "mvp ", "mvp",
    "product market fit", "pmf", "customer development", "problem solution",
    "experiment", "hypothesis",
]
AI_BUILD_TOKENS = [
    "vibe coding", "claude code", "cursor ai", "cursor", "lovable",
    "v0 by vercel", "bolt.new", "replit", "windsurf", "no code with ai",
    "build app with ai", "build with ai",
]
FUNDRAISING_TOKENS = [
    "raise seed", "seed round", "pitch deck", "vc due diligence", "term sheet",
    "convertible note", "safe note", "series a", "fundrais", "venture capital",
]


def signal_score(keyword: str, volume: int, kd: int, cpc: float) -> float:
    k = keyword.lower()

    # Hard negative — if matches noise tokens, score = 0
    if any(t in k for t in NEGATIVE_TOKENS):
        return 0.0

    base = min(40, math.log10(volume + 1) * 12) if volume > 0 else 0
    bonus = 0
    if "vietnam" in k or " vn" in k:
        bonus += 25
    if any(t in k for t in FRAMEWORK_TOKENS):
        bonus += 20
    if any(t in k for t in VALIDATION_TOKENS):
        bonus += 20
    if any(t in k for t in AI_BUILD_TOKENS):
        bonus += 15
    if any(t in k for t in FUNDRAISING_TOKENS):
        bonus += 15
    if cpc > 5:
        bonus += 10
    elif cpc > 2:
        bonus += 5
    kd_pen = kd * 0.4
    return round(max(0.0, min(100.0, base + bonus - kd_pen)), 1)


def categorize(keyword: str, bucket_from_csv: str) -> str:
    """Determine bucket label for the keyword."""
    k = keyword.lower()
    if bucket_from_csv == "vn_vc" or "vietnam" in k or " vn" in k:
        return "vn_vc"
    if any(t in k for t in AI_BUILD_TOKENS):
        return "ai_build"
    if any(t in k for t in VALIDATION_TOKENS):
        return "validation"
    if any(t in k for t in FRAMEWORK_TOKENS):
        return "framework"
    if any(t in k for t in FUNDRAISING_TOKENS):
        return "fundraising"
    return "other"


# ----------------------------- Airtable ops -----------------------------

def add_fields() -> None:
    """Add signal_score, cpc, bucket fields if missing."""
    r = requests.get(f"{AIRTABLE_META_BASE}/tables", headers=HEADERS, timeout=30)
    r.raise_for_status()
    table = next(t for t in r.json()["tables"] if t["id"] == KEYWORDS_TID)
    existing = {f["name"] for f in table["fields"]}

    new_fields = [
        {"name": "signal_score", "type": "number", "options": {"precision": 1}},
        {"name": "cpc", "type": "number", "options": {"precision": 2}},
        {"name": "bucket", "type": "singleLineText"},
    ]
    for f in new_fields:
        if f["name"] in existing:
            print(f"  [=] field {f['name']} exists")
            continue
        r = requests.post(
            f"{AIRTABLE_META_BASE}/tables/{KEYWORDS_TID}/fields",
            headers=HEADERS, json=f, timeout=30,
        )
        if r.status_code >= 400:
            print(f"  add field {f['name']} failed: {r.status_code} {r.text[:200]}")
        else:
            print(f"  [+] added field {f['name']}")


def wipe_all() -> int:
    """Delete all rows in Keywords."""
    ids = []
    recs = fetch_all(KEYWORDS_TID, fields=[])
    ids = [r["id"] for r in recs]
    if not ids:
        return 0
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
        if deleted % 200 == 0:
            print(f"  deleted {deleted}/{len(ids)}")
        time.sleep(0.22)
    return deleted


def insert(records: list[dict[str, Any]]) -> int:
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
        if inserted % 200 == 0:
            print(f"  inserted {inserted}/{len(records)}")
        time.sleep(0.22)
    return inserted


# ----------------------------- Main -----------------------------

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--top", type=int, default=0, help="insert top N only (0 = all)")
    args = ap.parse_args()

    # Load CSV
    if not CSV_PATH.exists():
        print(f"ERROR: {CSV_PATH} not found")
        return 2
    with CSV_PATH.open() as fp:
        cands = list(csv.DictReader(fp))
    print(f"Loaded {len(cands)} candidates from {CSV_PATH.name}")

    # Compute signal scores
    scored: list[dict[str, Any]] = []
    for c in cands:
        kw = (c.get("keyword") or "").strip().lower()
        if not kw or len(kw) < 4:
            continue
        vol = int(c.get("search_volume") or 0)
        kd = int(c.get("keyword_difficulty") or 0)
        cpc = float(c.get("cpc") or 0)
        bucket_csv = c.get("bucket", "")
        score = signal_score(kw, vol, kd, cpc)
        bucket = categorize(kw, bucket_csv)
        scored.append({
            "keyword": kw, "volume": vol, "kd": kd, "cpc": cpc,
            "score": score, "bucket": bucket, "seed": c.get("seed", ""),
        })

    # Sort by signal_score desc
    scored.sort(key=lambda r: r["score"], reverse=True)
    if args.top:
        scored = scored[:args.top]
    print(f"After signal scoring + sort: {len(scored)} ready to insert")

    # Top 10 preview
    print("\nTop 10 by signal:")
    for i, c in enumerate(scored[:10], 1):
        print(f"  #{i:>2} score={c['score']:>5} vol={c['volume']:>6} kd={c['kd']:>3} bucket={c['bucket']:<12s} {c['keyword']}")

    # Bucket distribution
    from collections import Counter
    bucket_count = Counter(c["bucket"] for c in scored)
    print(f"\nBucket distribution: {dict(bucket_count)}")

    if args.dry_run:
        print("\n[dry-run] would wipe existing + insert", len(scored), "rows")
        return 0

    # Add fields
    print("\n=== Adding new fields if missing ===")
    add_fields()

    # Wipe
    print("\n=== Wiping existing Keywords ===")
    n = wipe_all()
    print(f"  deleted {n}")

    # Insert
    print(f"\n=== Inserting {len(scored)} new rows ===")
    records = []
    for i, c in enumerate(scored, start=1):
        records.append({
            "keyword_id": f"KW-{i:05d}",
            "keyword": c["keyword"],
            "keyword_lang": "en",
            "seed_parent": c["seed"],
            "discovery_source": ["dataforseo"],
            "volume_global_en": c["volume"],
            "difficulty_proxy": c["kd"],
            "signal_score": c["score"],
            "cpc": c["cpc"],
            "bucket": c["bucket"],
            "status": "enriched",
        })
    n = insert(records)
    print(f"  inserted {n}")

    print("\nDone.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
