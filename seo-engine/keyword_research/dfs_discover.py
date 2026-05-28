"""
Pull keyword variants with real volume + KD via DataForSEO for the 67
curated seeds in objective_seeds.py.

For each seed, calls keyword_suggestions endpoint (~$0.01 per seed) and stores
all returned candidates into output/dfs_candidates.csv with full metadata:

  keyword, bucket (vn_vc / founder_edu), search_volume, kd, cpc, competition,
  seed (source), monthly_searches_trend, location

Two passes:
  - Pass 1: location=global_en for ALL seeds (priority demand signal)
  - Pass 2: location=vn for VN_VC seeds only (Vietnam-specific volume)

Total estimated cost: ~$0.85 of $1 budget.

Run:
    python dfs_discover.py                  # full discovery
    python dfs_discover.py --geo global_en  # one geo only
    python dfs_discover.py --bucket vn_vc   # one bucket only
    python dfs_discover.py --dry-run        # show plan + cost, no API calls
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
import time
from pathlib import Path
from typing import Any

from config_kw import OUTPUT_DIR
from dataforseo_client import (
    get_balance,
    keyword_suggestions,
)
from objective_seeds import SEEDS_FOUNDER_EDU, SEEDS_VN_VC

OUTPUT_FILE = OUTPUT_DIR / "dfs_candidates.csv"
RAW_FILE = OUTPUT_DIR / "dfs_candidates_raw.json"

FIELDS = [
    "keyword", "bucket", "seed", "location",
    "search_volume", "keyword_difficulty", "cpc",
    "competition", "competition_index",
    "trend_yoy_delta",
]


def trend_yoy(monthly: list[dict[str, Any]]) -> int:
    """Compute YoY % delta from monthly_searches array."""
    if not monthly or len(monthly) < 24:
        return 0
    # latest 12 months sum vs prior 12 months sum
    latest = sum(int(m.get("search_volume") or 0) for m in monthly[:12])
    prior = sum(int(m.get("search_volume") or 0) for m in monthly[12:24])
    if not prior:
        return 0
    return int(((latest - prior) / prior) * 100)


def harvest(seed: str, bucket: str, location: str, min_volume: int = 20) -> list[dict[str, Any]]:
    """Call DFS suggestions, return normalized rows."""
    print(f"  [{bucket}] {seed} (loc={location})")
    candidates = keyword_suggestions(
        seed=seed,
        location=location,
        language="en",
        limit=200,
        min_volume=min_volume,
        include_seed_in_response=True,
    )
    rows: list[dict[str, Any]] = []
    for c in candidates:
        kw = c.get("keyword", "").strip().lower()
        if not kw or len(kw) < 4:
            continue
        rows.append({
            "keyword": kw,
            "bucket": bucket,
            "seed": seed,
            "location": location,
            "search_volume": int(c.get("search_volume") or 0),
            "keyword_difficulty": int(c.get("keyword_difficulty") or 0),
            "cpc": round(float(c.get("cpc") or 0), 2),
            "competition": c.get("competition") or "",
            "competition_index": int(c.get("competition_index") or 0),
            "trend_yoy_delta": trend_yoy(c.get("monthly_searches") or []),
        })
    print(f"      → {len(rows)} candidates (vol≥{min_volume})")
    return rows


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--geo", choices=["global_en", "vn"], default=None,
                    help="run only one geo (default: both for vn_vc, only global_en for founder_edu)")
    ap.add_argument("--bucket", choices=["vn_vc", "founder_edu"], default=None)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--min-volume", type=int, default=20)
    ap.add_argument("--extra-seed", action="append", default=[], metavar="TERM[:bucket]",
                    help="ad-hoc seed added on top of objective_seeds.py; bucket = vn_vc|founder_edu "
                         "(default founder_edu). Repeatable, e.g. --extra-seed 'ai sales agent:founder_edu'")
    args = ap.parse_args()

    # Build run plan
    plan: list[tuple[str, str, str]] = []  # (seed, bucket, location)

    for s in SEEDS_VN_VC:
        if args.bucket and args.bucket != "vn_vc":
            continue
        # VN_VC seeds: query both global_en (VC global) and vn (founders in VN reading EN)
        if not args.geo or args.geo == "global_en":
            plan.append((s, "vn_vc", "global_en"))
        if not args.geo or args.geo == "vn":
            plan.append((s, "vn_vc", "vn"))

    for s in SEEDS_FOUNDER_EDU:
        if args.bucket and args.bucket != "founder_edu":
            continue
        # Founder-edu: global_en only (global founder audience)
        if not args.geo or args.geo == "global_en":
            plan.append((s, "founder_edu", "global_en"))

    # Ad-hoc user seeds from --extra-seed, same geo rules as their bucket
    for raw in args.extra_seed:
        term, _, b = raw.partition(":")
        term = term.strip()
        bucket = (b.strip() or "founder_edu")
        if not term:
            continue
        if bucket not in ("vn_vc", "founder_edu"):
            print(f"  skip --extra-seed '{raw}': bad bucket '{bucket}' (use vn_vc|founder_edu)")
            continue
        if args.bucket and args.bucket != bucket:
            continue
        if bucket == "vn_vc":
            if not args.geo or args.geo == "global_en":
                plan.append((term, "vn_vc", "global_en"))
            if not args.geo or args.geo == "vn":
                plan.append((term, "vn_vc", "vn"))
        else:
            if not args.geo or args.geo == "global_en":
                plan.append((term, "founder_edu", "global_en"))

    print(f"Plan: {len(plan)} API calls × $0.01 = ${len(plan) * 0.011:.2f} estimated")
    print(f"Pre-run balance: ${get_balance():.4f}\n")

    if args.dry_run:
        for s, b, loc in plan[:10]:
            print(f"  would call [{b}] {s} loc={loc}")
        print(f"  ... ({len(plan) - 10} more)" if len(plan) > 10 else "")
        return 0

    all_rows: list[dict[str, Any]] = []
    for i, (seed, bucket, loc) in enumerate(plan, start=1):
        print(f"[{i}/{len(plan)}]", end="")
        try:
            rows = harvest(seed, bucket, loc, min_volume=args.min_volume)
            all_rows.extend(rows)
        except Exception as e:
            print(f"      FAILED: {e}")
        time.sleep(0.4)

    # Save raw + dedupe CSV
    print(f"\nTotal raw candidates: {len(all_rows)}")
    RAW_FILE.write_text(json.dumps(all_rows, ensure_ascii=False, indent=2))
    print(f"  raw → {RAW_FILE}")

    # Dedupe: keep highest-volume row per (keyword, location)
    dedup: dict[tuple[str, str], dict[str, Any]] = {}
    for r in all_rows:
        key = (r["keyword"], r["location"])
        if key not in dedup or r["search_volume"] > dedup[key]["search_volume"]:
            dedup[key] = r
    print(f"  deduped: {len(dedup)} unique (keyword, location) pairs")

    with OUTPUT_FILE.open("w", newline="") as fp:
        w = csv.DictWriter(fp, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(dedup.values())
    print(f"  csv → {OUTPUT_FILE}")

    print(f"\nPost-run balance: ${get_balance():.4f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
