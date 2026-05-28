"""Wrap supplementary-image captions in asterisks so they render italicized on Framer.

Pattern: lines starting with `Photo by [...](...)` not preceded by `*`.
"""
import sys, re, time
import requests
from config_kw import AIRTABLE_API_BASE, AIRTABLE_BASE_ID, AIRTABLE_PAT
sys.path.insert(0, "/Users/phatnguyen/Downloads/OSR/seo-engine")
from table_ids import TABLE_IDS
from airtable_helpers import fetch_all

H = {"Authorization": f"Bearer {AIRTABLE_PAT}", "Content-Type": "application/json"}
TID = TABLE_IDS["Articles"]


def fix_body(body: str) -> tuple[str, int]:
    # Find lines that are `Photo by [Author](...) on [Unsplash](...)` not surrounded by asterisks
    # Wrap them in *...*
    pattern = re.compile(r"(?<!\*)(\bPhoto by \[[^\]]+\]\([^)]+\) on \[Unsplash\]\([^)]+\))(?!\*)")
    new_body, n = pattern.subn(r"*\1*", body)
    return new_body, n


def main():
    dry = "--dry-run" in sys.argv
    arts = fetch_all(TID)
    p23 = [a for a in arts if a['fields'].get('batch_id', '') in ('OSR-B-2026-05-PHASE2','OSR-B-2026-05-PHASE3','OSR-B-20260521')]
    ok = skip = fail = 0
    for a in p23:
        body = a['fields'].get('article_body_text', '') or ''
        new_body, n_fixed = fix_body(body)
        aid = a['fields'].get('article_id')
        if n_fixed == 0:
            print(f"  {aid}: SKIP (no unwrapped captions)")
            skip += 1; continue
        print(f"  {aid}: wrapping {n_fixed} caption(s)")
        if dry:
            ok += 1; continue
        r = requests.patch(
            f"{AIRTABLE_API_BASE}/{AIRTABLE_BASE_ID}/{TID}/{a['id']}",
            headers=H, json={"fields": {"article_body_text": new_body}}, timeout=60,
        )
        if r.status_code >= 400:
            print(f"    ERROR {r.status_code}: {r.text[:200]}"); fail += 1
        else:
            ok += 1
        time.sleep(0.25)
    print(f"\nDone ({'DRY' if dry else 'LIVE'}): ok={ok} skip={skip} fail={fail}")


if __name__ == "__main__":
    main()
