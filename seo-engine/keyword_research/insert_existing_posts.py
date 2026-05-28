"""
Insert 9 existing osresearch.vn/blog/* posts into Articles table.
Also pivot Phase 1 #10 (Blue Ocean) to comparison angle to avoid overlap with
the existing "blue-ocean-strategy" post.

CSV source: ~/Downloads/Blog (1).csv (exported from Framer).

Overlap resolution:
  - #3 (BMC examples)  ↔  existing /business-model-canvas       → keep (different intent)
  - #6 (VPC model)     ↔  existing /value-proposition-canvas    → keep (different angle), tighten meta
  - #10 (Blue Ocean)   ↔  existing /blue-ocean-strategy         → PIVOT to "vs red ocean" comparison

Run:
    python insert_existing_posts.py --dry-run
    python insert_existing_posts.py
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
import time
from pathlib import Path

import requests

from airtable_helpers import fetch_all
from config_kw import AIRTABLE_API_BASE, AIRTABLE_BASE_ID, AIRTABLE_PAT

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from table_ids import TABLE_IDS  # noqa: E402

from osr_template import SITE, build_schema_jsonld, slugify  # noqa: E402

HEADERS = {"Authorization": f"Bearer {AIRTABLE_PAT}", "Content-Type": "application/json"}
ARTS = TABLE_IDS["Articles"]
CSV_PATH = Path.home() / "Downloads" / "Blog (1).csv"
EXISTING_BATCH = "OSR-EXISTING-20260508"

# slug → (primary_keyword, pattern)
EXISTING_META = {
    "startup-validation-studio":    ("startup validation studio",      "case_study"),
    "modern-vietnamese-household":  ("modern vietnamese household",    "sector_ideas"),
    "blue-ocean-strategy":          ("blue ocean strategy",            "framework_example"),
    "value-proposition-canvas":     ("value proposition canvas",       "framework_example"),
    "business-model-canvas":        ("business model canvas",          "framework_example"),
    "first-business-pitch":         ("one page business pitch",        "how_to_validate"),
    "six-week-testing-cycle":       ("six week testing cycle",         "how_to_validate"),
    "experiment-library":           ("startup experiment library",     "how_to_validate"),
    "experiment-sequences":         ("startup experiment sequences",   "how_to_validate"),
}


def post(rec_fields: dict) -> str:
    payload = {"records": [{"fields": rec_fields}], "typecast": True}
    for attempt in range(3):
        try:
            r = requests.post(
                f"{AIRTABLE_API_BASE}/{AIRTABLE_BASE_ID}/{ARTS}",
                headers=HEADERS, json=payload, timeout=120,
            )
            if r.status_code < 400:
                return r.json()["records"][0]["id"]
            print(f"    CREATE HTTP {r.status_code}: {r.text[:300]}")
            return ""
        except requests.exceptions.RequestException as e:
            print(f"    attempt {attempt+1}: {e.__class__.__name__}")
            time.sleep(3 * (attempt + 1))
    return ""


def patch(record_id: str, fields: dict) -> bool:
    for attempt in range(3):
        try:
            r = requests.patch(
                f"{AIRTABLE_API_BASE}/{AIRTABLE_BASE_ID}/{ARTS}/{record_id}",
                headers=HEADERS, json={"fields": fields, "typecast": True}, timeout=120,
            )
            if r.status_code < 400:
                return True
            print(f"    PATCH HTTP {r.status_code}: {r.text[:300]}")
            return False
        except requests.exceptions.RequestException as e:
            print(f"    attempt {attempt+1}: {e.__class__.__name__}")
            time.sleep(3 * (attempt + 1))
    return False


def insert_existing_posts(rows: list[dict], dry: bool) -> None:
    print(f"\n=== Insert {len(rows)} existing posts (status=published) ===")
    for i, r in enumerate(rows, start=1):
        slug = r["Slug"]
        meta = EXISTING_META.get(slug)
        if not meta:
            print(f"  skip {slug}: no mapping")
            continue
        kw, pattern = meta
        title = r["Title"]
        desc = r["Description"]
        cover_url = r.get("Cover Image", "") or r.get("Image", "")
        cover_alt = r.get("Cover Image:alt", "") or r.get("Image:alt", "")
        body = r["Content Block"]
        url = f"{SITE}/blog/{slug}"
        date_pub = r.get("Date", "2026-05-08")[:10]
        article_id = f"OSR-EXISTING-{i:03d}"

        # Schema JSON-LD (best-effort: HTML body so faq extraction skipped)
        schema = build_schema_jsonld(
            primary_keyword=kw,
            h1=title,
            title_tag=title,
            meta_description=desc,
            tldr=desc,
            slug=slug,
            cover_image_url=cover_url,
            published_date=date_pub,
            word_count=len(re.sub(r"<[^>]+>", "", body).split()),
            faq_pairs=None,
            pattern=pattern,
        )

        fields = {
            "article_id": article_id,
            "batch_id": EXISTING_BATCH,
            "primary_keyword": kw,
            "search_volume": 0,
            "keyword_difficulty": 0,
            "signal_score": 50,
            "pattern": pattern,
            "status": "published",
            "title_tag": title[:255],
            "meta_description": desc[:280],
            "slug": slug,
            "cover_image_url": cover_url,
            "cover_image_alt": cover_alt[:255],
            "cover_image_credit": "",
            "schema_jsonld": schema,
            "article_body_text": body[:99000],
            "final_url": url,
            "framer_url": url,
            "keyword_cluster": "(existing playbook series — not from DFS keyword pool)",
        }
        if dry:
            print(f"  [dry] {article_id}: {title[:55]}  ({len(body)} chars)")
            continue
        rid = post(fields)
        if rid:
            print(f"  ✓ {article_id}: {title[:55]}")
        else:
            print(f"  ✗ {article_id}: CREATE failed")
        time.sleep(0.4)


def pivot_blue_ocean(dry: bool) -> None:
    """Pivot Phase 1 #10 from 'what is the blue ocean strategy' to 'blue ocean vs red ocean strategy'."""
    print("\n=== Pivot Phase 1 #10 (Blue Ocean) to comparison angle ===")
    arts = fetch_all(ARTS, fields=["article_id", "primary_keyword", "slug"])
    target = next((a for a in arts if a["fields"].get("article_id") == "OSR-2026-05-21-010"), None)
    if not target:
        print("  ✗ Phase 1 #10 not found")
        return

    new_kw = "blue ocean vs red ocean strategy"
    new_slug = "blue-ocean-vs-red-ocean-strategy"
    new_title = "Blue Ocean vs Red Ocean Strategy: When to Use Each (2026)"
    new_meta = (
        "Compare Blue Ocean and Red Ocean strategy: when to compete vs create new "
        "demand. ERRC framework, real company examples, and how to choose."
    )
    new_url = f"{SITE}/blog/{new_slug}"

    fields = {
        "primary_keyword": new_kw,
        "slug": new_slug,
        "title_tag": new_title,
        "meta_description": new_meta,
        "final_url": new_url,
        "framer_url": new_url,
        # Note: body content still covers comparison (ERRC, red vs blue, examples) — no rewrite needed.
        # Updated KD/signal from top 100 row "blue ocean vs red ocean strategy"
        "search_volume": 1000,
        "keyword_difficulty": 8,
        "signal_score": 52.8,
    }
    if dry:
        print(f"  [dry] PATCH #10 → kw='{new_kw}', slug='{new_slug}'")
        return
    if patch(target["id"], fields):
        print(f"  ✓ #10 pivoted → {new_url}")
    else:
        print(f"  ✗ #10 PATCH failed")


def tighten_meta_overlaps(dry: bool) -> None:
    """Tighten #3 and #6 meta to clarify unique angle vs existing posts."""
    print("\n=== Tighten meta for #3 (BMC examples) and #6 (VPC) ===")
    arts = fetch_all(ARTS, fields=["article_id"])
    updates = {
        "OSR-2026-05-21-003": {  # #3 BMC examples
            "meta_description": (
                "15 Business Model Canvas examples from real companies (Uber, Spotify, "
                "Netflix, Vinamilk, MoMo). Filled-out canvases plus what each one reveals about strategy."
            ),
        },
        "OSR-2026-05-21-006": {  # #6 VPC model
            "meta_description": (
                "Value Proposition Canvas walkthrough: 6 blocks explained block-by-block "
                "with 8 real examples, fit tests, and when to pair with the Business Model Canvas."
            ),
        },
    }
    for aid, fields in updates.items():
        rec = next((a for a in arts if a["fields"].get("article_id") == aid), None)
        if not rec:
            print(f"  ✗ {aid} not found")
            continue
        if dry:
            print(f"  [dry] PATCH {aid} meta")
            continue
        if patch(rec["id"], fields):
            print(f"  ✓ {aid} meta updated")
        else:
            print(f"  ✗ {aid} PATCH failed")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not CSV_PATH.exists():
        print(f"ERROR: {CSV_PATH} not found")
        return 2
    with CSV_PATH.open() as fp:
        rows = list(csv.DictReader(fp))
    print(f"Loaded {len(rows)} existing posts from {CSV_PATH.name}")

    insert_existing_posts(rows, args.dry_run)
    pivot_blue_ocean(args.dry_run)
    tighten_meta_overlaps(args.dry_run)

    print("\nDone.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
