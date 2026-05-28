"""
Add `people_also_ask` field to Articles + populate for 10 Phase 1 articles
from the SERP_DATA already fetched in complete_10_articles.py.

Each cell: 1 PAA question per line (3-7 per article).

Run:
    python add_paa_field.py --dry-run
    python add_paa_field.py
"""
from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

import requests

from airtable_helpers import fetch_all
from config_kw import AIRTABLE_API_BASE, AIRTABLE_BASE_ID, AIRTABLE_META_BASE, AIRTABLE_PAT

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from table_ids import TABLE_IDS  # noqa: E402

from complete_10_articles import SERP_DATA, PICKS

HEADERS = {"Authorization": f"Bearer {AIRTABLE_PAT}", "Content-Type": "application/json"}
ARTS = TABLE_IDS["Articles"]


def ensure_field() -> None:
    r = requests.get(f"{AIRTABLE_META_BASE}/tables", headers=HEADERS, timeout=30).json()
    table = next(t for t in r["tables"] if t["id"] == ARTS)
    if any(f["name"] == "people_also_ask" for f in table["fields"]):
        print("  [=] people_also_ask exists")
        return
    r = requests.post(
        f"{AIRTABLE_META_BASE}/tables/{ARTS}/fields",
        headers=HEADERS,
        json={"name": "people_also_ask", "type": "multilineText",
              "description": "PAA questions extracted from SERP. One question per line. Use to seed FAQ section."},
        timeout=30,
    )
    print(f"  [+] create people_also_ask: HTTP {r.status_code}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not args.dry_run:
        ensure_field()

    # Build keyword → PAA from SERP_DATA (uses the new primary_keyword set)
    # Note: PICKS uses NEW primary_keyword but SERP_DATA is keyed by both.
    # Phase 1 #10 was pivoted: keyword changed but SERP_DATA still keyed by old name.
    kw_to_paa = {kw: data.get("paa", []) for kw, data in SERP_DATA.items()}

    # Map pivoted keyword #10 to its SERP_DATA entry
    PIVOT_REMAP = {
        "blue ocean vs red ocean strategy": SERP_DATA["what is the blue ocean strategy"].get("paa", []),
    }
    kw_to_paa.update(PIVOT_REMAP)

    arts = fetch_all(ARTS, fields=["article_id", "primary_keyword", "status"])
    phase1 = [a for a in arts if a["fields"].get("status") == "review"]
    print(f"\nPhase 1 articles: {len(phase1)}")

    for art in sorted(phase1, key=lambda x: x["fields"].get("article_id", "")):
        f = art["fields"]
        kw = f.get("primary_keyword", "")
        paa = kw_to_paa.get(kw, [])
        if not paa:
            print(f"  ✗ {f.get('article_id')}: no PAA for '{kw}'")
            continue
        text = "\n".join(paa)
        if args.dry_run:
            print(f"  [dry] {f.get('article_id'):<22} {len(paa)} questions, {len(text)} chars")
            continue
        r = requests.patch(
            f"{AIRTABLE_API_BASE}/{AIRTABLE_BASE_ID}/{ARTS}/{art['id']}",
            headers=HEADERS,
            json={"fields": {"people_also_ask": text}, "typecast": True},
            timeout=60,
        )
        ok = "✓" if r.status_code < 400 else "✗"
        print(f"  {ok} {f.get('article_id'):<22} {len(paa)} questions  | {kw[:40]}")
        time.sleep(0.25)

    return 0


if __name__ == "__main__":
    sys.exit(main())
