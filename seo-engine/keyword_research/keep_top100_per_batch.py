"""
Reduce Keywords table to TOP 100 by signal_score (per batch).
Full pool stays as CSV attachment trên Batches row.

Workflow:
  1. Add `batch_id` field to Keywords if missing
  2. Wipe all current Keywords rows
  3. Compute signal_score per CSV candidate
  4. Sort by signal_score desc → take top 100
  5. Insert with batch_id reference

Run per batch — each new batch's keywords get inserted with that batch_id.

Run:
    python keep_top100_per_batch.py --batch-id OSR-B-20260521
    python keep_top100_per_batch.py --dry-run
"""
from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

import requests

from airtable_helpers import fetch_all
from config_kw import (
    AIRTABLE_API_BASE, AIRTABLE_BASE_ID, AIRTABLE_META_BASE, AIRTABLE_PAT,
    OUTPUT_DIR,
)
from populate_keywords import categorize, signal_score

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from table_ids import TABLE_IDS  # noqa: E402

HEADERS = {"Authorization": f"Bearer {AIRTABLE_PAT}", "Content-Type": "application/json"}
KEYWORDS_TID = TABLE_IDS["Keywords"]
BATCHES_TID = TABLE_IDS["Batches"]
CSV_PATH = OUTPUT_DIR / "dfs_candidates.csv"


def ensure_batch_id_field() -> None:
    r = requests.get(f"{AIRTABLE_META_BASE}/tables", headers=HEADERS, timeout=30).json()
    table = next(t for t in r["tables"] if t["id"] == KEYWORDS_TID)
    if any(f["name"] == "batch_id" for f in table["fields"]):
        print("  [=] batch_id field exists")
        return
    r = requests.post(
        f"{AIRTABLE_META_BASE}/tables/{KEYWORDS_TID}/fields",
        headers=HEADERS,
        json={"name": "batch_id", "type": "singleLineText"},
        timeout=30,
    )
    if r.status_code < 400:
        print("  [+] added batch_id field")
    else:
        print(f"  add batch_id failed: {r.status_code} {r.text[:200]}")


def wipe_all() -> int:
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
            print(f"    deleted {deleted}/{len(ids)}")
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


def load_top100() -> list[dict]:
    import csv
    if not CSV_PATH.exists():
        raise FileNotFoundError(CSV_PATH)
    with CSV_PATH.open() as fp:
        rows = list(csv.DictReader(fp))
    scored = []
    for c in rows:
        kw = (c.get("keyword") or "").strip().lower()
        if not kw or len(kw) < 4:
            continue
        vol = int(c.get("search_volume") or 0)
        kd = int(c.get("keyword_difficulty") or 0)
        cpc = float(c.get("cpc") or 0)
        score = signal_score(kw, vol, kd, cpc)
        if score == 0:
            continue  # noise filter
        scored.append({
            "keyword": kw, "vol": vol, "kd": kd, "cpc": cpc,
            "score": score, "bucket": categorize(kw, c.get("bucket", "")),
            "seed": c.get("seed", ""),
        })
    scored.sort(key=lambda r: r["score"], reverse=True)
    return scored[:100]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch-id", default="OSR-B-20260521")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    print(f"Batch ID for these keywords: {args.batch_id}")

    top100 = load_top100()
    print(f"\nTop 100 by signal_score (after noise filter):")
    print(f"  {'#':<4} {'signal':<7} {'vol':<7} {'kd':<4} {'bucket':<13} keyword")
    for i, c in enumerate(top100[:15], 1):
        print(f"  {i:<4} {c['score']:<7} {c['vol']:<7} {c['kd']:<4} {c['bucket'][:12]:<13} {c['keyword'][:55]}")
    print(f"  ... and {len(top100) - 15} more")

    if args.dry_run:
        print("\n[dry-run]")
        return 0

    print("\n=== Step 1: Ensure batch_id field ===")
    ensure_batch_id_field()

    print("\n=== Step 2: Wipe existing Keywords ===")
    n = wipe_all()
    print(f"  deleted {n}")

    print(f"\n=== Step 3: Insert top {len(top100)} ===")
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
