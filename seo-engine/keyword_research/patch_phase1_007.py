"""
Swap keyword for Phase 1 #007:
  jobs to be done framework  →  jobs to be done framework examples

Updates primary_keyword, slug, framer_url, search_volume, keyword_difficulty,
title_tag (already has "Examples"), enhances TL;DR to include exact phrase,
and regenerates schema_jsonld to reference the new keyword.
"""
from __future__ import annotations

import re
import sys
from datetime import date

import requests

from config_kw import AIRTABLE_API_BASE, AIRTABLE_BASE_ID, AIRTABLE_PAT

sys.path.insert(0, "/Users/phatnguyen/Downloads/OSR/seo-engine")
from table_ids import TABLE_IDS
from osr_template import build_schema_jsonld

H = {"Authorization": f"Bearer {AIRTABLE_PAT}", "Content-Type": "application/json"}
ARTICLES_TID = TABLE_IDS["Articles"]
RECORD_ID = "recq4fAkOAPkfPiAU"  # OSR-2026-05-21-007

NEW_KW = "jobs to be done framework examples"
NEW_SLUG = "jobs-to-be-done-framework-examples"
NEW_FRAMER = f"https://www.osresearch.vn/blog/{NEW_SLUG}"
NEW_SV = 70
NEW_KD = 13


def fetch_record() -> dict:
    r = requests.get(
        f"{AIRTABLE_API_BASE}/{AIRTABLE_BASE_ID}/{ARTICLES_TID}/{RECORD_ID}",
        headers={"Authorization": f"Bearer {AIRTABLE_PAT}"}, timeout=30,
    )
    r.raise_for_status()
    return r.json()


def enhance_tldr(body: str) -> str:
    # Insert "jobs to be done framework examples" naturally into TL;DR
    # Current TL;DR starts: "Jobs to Be Done (JTBD) is a customer needs framework..."
    # Add a sentence at end of TL;DR that uses the exact phrase
    pat = re.compile(
        r"(\*\*TL;DR\.\*\*[^\n]*?features\.)",  # ends with "...around outcomes rather than features."
        re.DOTALL,
    )
    insert = (
        " This guide walks through real jobs to be done framework examples "
        "(McDonald's milkshake, MoMo) and how to apply the framework in practice."
    )
    return pat.sub(lambda m: m.group(1) + insert, body, count=1)


def add_examples_section(body: str) -> str:
    """Insert a dedicated 'Jobs to be done framework examples' H2 early in body."""
    if "## Jobs to be done framework examples" in body:
        return body
    # Insert after "## The core insight" section ends (next ## is "## The 4 elements")
    marker = "\n## The 4 elements of the JTBD framework"
    if marker not in body:
        return body
    new_section = """

## Jobs to be done framework examples

Three concrete jobs to be done framework examples make the theory tangible.

**McDonald's milkshake (Clayton Christensen's canonical example).** Adults bought milkshakes in the morning to handle a specific commuter job: something to occupy a long, boring drive that was substantial enough to feel like a meal. The job was not "I want a sweet drink." The job was "I need something thick enough to last 30 minutes that I can hold in one hand while driving." McDonald's reframed the product around the actual job and grew the morning shake segment.

**Buffer's two-page validation.** Before building the social media scheduler, Joel Gascoigne tested whether the job — "schedule my social posts so I can focus on creating" — was urgent enough to drive sign-ups and willingness to pay. A two-page landing-page test (product description + pricing) validated demand before any product code was written. The MVP was the JTBD validation artifact.

**MoMo (Vietnam).** Vietnamese e-wallet MoMo grew by repositioning around the job "send money to family across cities without going to the bank." The traditional banking job framing emphasized account features and trust. MoMo's JTBD framing emphasized the moment of transfer between people. The product design — pay anyone in seconds with a phone number — fit the job better than incumbent banking apps.
"""
    return body.replace(marker, new_section + marker)


def main() -> int:
    dry = "--dry-run" in sys.argv
    rec = fetch_record()
    body = rec["fields"].get("article_body_text", "")
    old_kw = rec["fields"].get("primary_keyword", "")
    print(f"Fetched record {RECORD_ID}")
    print(f"  current primary_keyword: {old_kw!r}")
    print(f"  body words: {len(body.split())}")

    new_body = enhance_tldr(body)
    new_body = add_examples_section(new_body)
    print(f"  new body words: {len(new_body.split())}")

    # Parse existing FAQ pairs from body for schema
    faq_pairs = []
    if "## Frequently asked questions" in new_body:
        faq_block = new_body.split("## Frequently asked questions")[-1]
        cur_q, cur_a = None, []
        for ln in faq_block.split("\n"):
            s = ln.strip()
            if s.startswith("**Q:"):
                if cur_q and cur_a:
                    faq_pairs.append({"question": cur_q, "answer": " ".join(cur_a).strip()})
                cur_q = s.lstrip("*").strip().lstrip("Q:").strip().rstrip("*").strip()
                cur_a = []
            elif s.startswith("A:"):
                cur_a.append(s[2:].strip())
            elif cur_q and s and not s.startswith("**"):
                cur_a.append(s)
        if cur_q and cur_a:
            faq_pairs.append({"question": cur_q, "answer": " ".join(cur_a).strip()})
    print(f"  parsed {len(faq_pairs)} FAQ pairs")

    # Rebuild schema_jsonld with new primary_keyword
    new_schema = build_schema_jsonld(
        primary_keyword=NEW_KW,
        h1="Jobs to Be Done Framework Examples: McDonald's, Buffer, MoMo",
        title_tag=rec["fields"].get("title_tag", ""),
        meta_description=rec["fields"].get("meta_description", ""),
        tldr=re.search(r"\*\*TL;DR\.\*\*\s*(.+?)(?=\n\n|\Z)", new_body, re.DOTALL).group(1).strip()[:300],
        slug=NEW_SLUG,
        cover_image_url=rec["fields"].get("cover_image_url", ""),
        published_date=str(date.today()),
        word_count=len(new_body.split()),
        faq_pairs=faq_pairs,
        pattern=rec["fields"].get("pattern", "framework_example"),
    )

    payload_fields = {
        "primary_keyword": NEW_KW,
        "slug": NEW_SLUG,
        "framer_url": NEW_FRAMER,
        "search_volume": NEW_SV,
        "keyword_difficulty": NEW_KD,
        "article_body_text": new_body,
        "schema_jsonld": new_schema,
    }
    print()
    print("Will PATCH fields:")
    for k, v in payload_fields.items():
        if isinstance(v, str) and len(v) > 80:
            print(f"  {k}: <{len(v)} chars>")
        else:
            print(f"  {k}: {v!r}")
    if dry:
        print("\n[DRY] not sending"); return 0
    r = requests.patch(
        f"{AIRTABLE_API_BASE}/{AIRTABLE_BASE_ID}/{ARTICLES_TID}/{RECORD_ID}",
        headers=H,
        json={"fields": payload_fields, "typecast": True},
        timeout=60,
    )
    if r.status_code >= 400:
        print(f"ERROR HTTP {r.status_code}: {r.text[:500]}"); return 1
    print(f"\nPATCH ok: {r.json()['id']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
