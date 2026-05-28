"""Populate the Airtable Seed_Keywords table from objective_seeds.py + output/seed_terms.csv.

Combines the two seed sources, dedupes by keyword (case-insensitive), and posts
in batches of 10 (Airtable's per-request limit for create_records).
"""
from __future__ import annotations

import csv
import sys
import time
from datetime import date
from pathlib import Path

import requests

from config_kw import AIRTABLE_API_BASE, AIRTABLE_BASE_ID, AIRTABLE_PAT
import objective_seeds

SEED_TABLE_ID = "tblccnlEdRY2uccmA"
H = {"Authorization": f"Bearer {AIRTABLE_PAT}", "Content-Type": "application/json"}
TODAY = str(date.today())


def collect_seeds() -> list[dict]:
    """Return a deduped list of seed dicts ready for Airtable insert."""
    by_kw: dict[str, dict] = {}

    # Hand-curated seeds from objective_seeds.py
    for kw in objective_seeds.SEEDS_VN_VC:
        k = kw.lower().strip()
        by_kw[k] = {
            "seed_keyword": kw,
            "bucket": "vn_vc",
            "source": "objective_seeds",
            "lang": "en",
            "status": "used",   # already expanded in DFS batch 1
            "created_at": TODAY,
        }
    for kw in objective_seeds.SEEDS_FOUNDER_EDU:
        k = kw.lower().strip()
        if k in by_kw:
            continue
        by_kw[k] = {
            "seed_keyword": kw,
            "bucket": "founder_edu",
            "source": "objective_seeds",
            "lang": "en",
            "status": "used",
            "created_at": TODAY,
        }

    # Expanded seeds from output/seed_terms.csv
    seed_terms_csv = Path(__file__).parent / "output" / "seed_terms.csv"
    if seed_terms_csv.exists():
        with seed_terms_csv.open() as f:
            for row in csv.DictReader(f):
                kw = row["seed"].strip()
                k = kw.lower()
                if k in by_kw:
                    continue
                # Pillar-based bucket assignment
                pillar = row.get("pillar", "")
                bucket = "vn_vc" if pillar == "Vietnam-Market" else "founder_edu"
                by_kw[k] = {
                    "seed_keyword": kw,
                    "bucket": bucket,
                    "source": row.get("source", "sector_x_modifier"),
                    "pillar": pillar if pillar else None,
                    "lang": row.get("lang", "en"),
                    "status": "used",
                    "created_at": TODAY,
                }

    seeds = list(by_kw.values())
    # Clean None values
    for s in seeds:
        for k in list(s.keys()):
            if s[k] is None or s[k] == "":
                del s[k]
    return seeds


def post_batch(records: list[dict], dry: bool):
    payload = {"records": [{"fields": r} for r in records], "typecast": True}
    if dry:
        return None
    r = requests.post(
        f"{AIRTABLE_API_BASE}/{AIRTABLE_BASE_ID}/{SEED_TABLE_ID}",
        headers=H, json=payload, timeout=60,
    )
    if r.status_code >= 400:
        print(f"  ERROR HTTP {r.status_code}: {r.text[:500]}")
        return None
    return r.json()["records"]


def main() -> int:
    dry = "--dry-run" in sys.argv
    seeds = collect_seeds()
    print(f"Collected {len(seeds)} unique seeds")
    from collections import Counter
    print(f"  by source: {dict(Counter(s.get('source') for s in seeds))}")
    print(f"  by bucket: {dict(Counter(s.get('bucket') for s in seeds))}")
    print(f"  by pillar: {dict(Counter(s.get('pillar', '-') for s in seeds))}")

    BATCH = 10  # Airtable create-records limit
    total_inserted = 0
    for i in range(0, len(seeds), BATCH):
        chunk = seeds[i:i+BATCH]
        result = post_batch(chunk, dry)
        if dry:
            print(f"  [DRY] would insert rows {i+1}-{i+len(chunk)}")
        else:
            if result:
                total_inserted += len(result)
                print(f"  inserted {i+1}-{i+len(result)} (total {total_inserted})")
            time.sleep(0.25)  # gentle rate limit

    print(f"\nDone. mode={'DRY' if dry else 'LIVE'}  total_inserted={total_inserted}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
