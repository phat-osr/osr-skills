"""
End-to-end push for Phase 2 bài 2: validate business idea.

Same shape as push_phase2_article1.py — parameterized for bài 2.
"""
from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path

import requests

from config_kw import AIRTABLE_API_BASE, AIRTABLE_BASE_ID, AIRTABLE_PAT
from optimize_titles import optimize_title
from osr_template import build_schema_jsonld, finalize_body, slugify, truncate
from image_finder import find_cover_image
from render_paste_ready import clean_markdown

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from table_ids import TABLE_IDS  # noqa: E402

H = {"Authorization": f"Bearer {AIRTABLE_PAT}", "Content-Type": "application/json"}
ARTICLES_TID = TABLE_IDS["Articles"]
BATCHES_TID = TABLE_IDS["Batches"]

PRIMARY_KW = "validate business idea"
PATTERN = "how_to_validate"
BATCH_ID = "OSR-B-2026-05-PHASE2"
ARTICLE_ID = "OSR-2026-05-22-002"
SV = 210
KD = 26
SIGNAL = 47.5

DRAFT_PATH = Path(__file__).parent / "phase2_drafts" / "02-validate-business-idea.md"

TITLE_OVERRIDE = "How to Validate a Business Idea: 2026 Founder Guide"
META_DESCRIPTION = (
    "Most guides give you steps. None tell you when validation is binding. "
    "The staged evidence approach we use at OS Research, with explicit thresholds."
)

PAA = [
    "How many customer interviews do I need to validate a business idea?",
    "How do you test a business idea before launching?",
    "How do you know if a business idea is good?",
    "What is the difference between business idea validation and market research?",
    "How much does it cost to validate a business idea?",
]

CLUSTER = [
    "customer interviews",
    "problem validation",
    "solution validation",
    "pre-sale test",
    "letter of intent",
    "minimum viable product",
    "mvp",
    "lean startup",
    "product market fit",
    "pivot or persevere",
    "problem solution fit",
    "value proposition",
    "target customer",
    "market research",
    "competitive analysis",
    "early adopters",
    "early customer signal",
    "cold email outreach",
    "pre-launch deposit",
    "founder market fit",
    "jobs to be done",
    "customer development",
    "steve blank",
    "eric ries",
    "the lean startup",
    "validated learning",
    "business model canvas",
    "lean canvas",
    "value proposition canvas",
    "problem space exploration",
]

# Verified internal slugs (cross-checked against Airtable)
INTERNAL_ANCHORS = {
    "startup validation studio": ("startup validation studio", "https://www.osresearch.vn/blog/startup-validation-studio"),
    "experiment library": ("experiment library", "https://www.osresearch.vn/blog/experiment-library"),
    "six week testing cycle": ("six week testing cycle", "https://www.osresearch.vn/blog/six-week-testing-cycle"),
    "product-market fit": ("product-market fit", "https://www.osresearch.vn/blog/product-market-fit"),
}

OUTBOUND_ANCHORS = {
    "Eric Ries": "http://www.startuplessonslearned.com/2009/04/validated-learning-about-customers.html",
    "The Lean Startup": "https://theleanstartup.com/principles",
}


def inject_simple_links(body: str) -> str:
    out = body
    used = set()
    for trigger, (anchor_text, href) in INTERNAL_ANCHORS.items():
        if trigger in used:
            continue
        lo = out.lower()
        idx = lo.find(trigger.lower())
        while idx != -1:
            before = out[idx-1] if idx > 0 else ""
            if before not in "[(":
                end = idx + len(trigger)
                replacement = f"[{anchor_text}]({href})"
                out = out[:idx] + replacement + out[end:]
                used.add(trigger)
                break
            idx = lo.find(trigger.lower(), idx + 1)
    for anchor, href in OUTBOUND_ANCHORS.items():
        lo = out.lower()
        idx = lo.find(anchor.lower())
        if idx == -1:
            continue
        before = out[idx-1] if idx > 0 else ""
        if before in "[(":
            continue
        end = idx + len(anchor)
        out = out[:idx] + f"[{anchor}]({href})" + out[end:]
    return out


def build_record(image_data: dict) -> dict:
    body_md = DRAFT_PATH.read_text()
    tldr_start = body_md.find("**TL;DR.**") + len("**TL;DR.**")
    tldr_end = body_md.find("</aside>")
    tldr = body_md[tldr_start:tldr_end].strip()

    slug = slugify(PRIMARY_KW)
    title = TITLE_OVERRIDE if TITLE_OVERRIDE else optimize_title(PRIMARY_KW, PATTERN)
    meta = truncate(META_DESCRIPTION, 155)

    word_count = len(body_md.split())

    faq_pairs = []
    faq_block = body_md.split("## Frequently asked questions")[-1] if "## Frequently asked questions" in body_md else ""
    lines = faq_block.split("\n")
    cur_q, cur_a = None, []
    for ln in lines:
        ln_s = ln.strip()
        if ln_s.startswith("**Q:"):
            if cur_q and cur_a:
                faq_pairs.append({"question": cur_q, "answer": " ".join(cur_a).strip()})
            cur_q = ln_s.lstrip("*").strip().lstrip("Q:").strip().rstrip("*").strip()
            cur_a = []
        elif ln_s.startswith("A:"):
            cur_a.append(ln_s[2:].strip())
        elif cur_q and ln_s and not ln_s.startswith("**"):
            cur_a.append(ln_s)
    if cur_q and cur_a:
        faq_pairs.append({"question": cur_q, "answer": " ".join(cur_a).strip()})

    schema = build_schema_jsonld(
        primary_keyword=PRIMARY_KW,
        h1="How to Validate a Business Idea",
        title_tag=title,
        meta_description=meta,
        tldr=tldr,
        slug=slug,
        cover_image_url=image_data["url"],
        published_date=str(date.today()),
        word_count=word_count,
        faq_pairs=faq_pairs,
        pattern=PATTERN,
    )

    finalized = finalize_body(
        body_md=body_md,
        pattern=PATTERN,
        primary_keyword=PRIMARY_KW,
        published_date=str(date.today()),
        cover_image_url=image_data["url"],
        cover_image_alt=image_data["alt"],
        cover_image_credit=image_data["credit"],
    )
    finalized = inject_simple_links(finalized)
    finalized = clean_markdown(finalized)

    framer_url = f"https://www.osresearch.vn/blog/{slug}"

    return {
        "article_id": ARTICLE_ID,
        "batch_id": BATCH_ID,
        "primary_keyword": PRIMARY_KW,
        "search_volume": SV,
        "keyword_difficulty": KD,
        "signal_score": SIGNAL,
        "pattern": PATTERN,
        "status": "review",
        "title_tag": title,
        "meta_description": meta,
        "slug": slug,
        "cover_image_url": image_data["url"],
        "cover_image_alt": image_data["alt"],
        "cover_image_credit": image_data["credit"],
        "schema_jsonld": schema,
        "article_body_text": finalized,
        "keyword_cluster": "\n".join(CLUSTER),
        "people_also_ask": "\n".join(PAA),
        "framer_url": framer_url,
    }, faq_pairs, word_count


def insert_article(fields: dict, dry: bool):
    r = requests.get(
        f"{AIRTABLE_API_BASE}/{AIRTABLE_BASE_ID}/{ARTICLES_TID}",
        headers={"Authorization": f"Bearer {AIRTABLE_PAT}"},
        params=[("filterByFormula", f"{{article_id}}='{fields['article_id']}'")],
        timeout=30,
    )
    r.raise_for_status()
    existing = r.json().get("records", [])
    if existing:
        rid = existing[0]["id"]
        print(f"  Article {fields['article_id']} exists at {rid} — PATCH")
        if dry:
            return rid
        r = requests.patch(
            f"{AIRTABLE_API_BASE}/{AIRTABLE_BASE_ID}/{ARTICLES_TID}/{rid}",
            headers=H, json={"fields": fields, "typecast": True}, timeout=60,
        )
        if r.status_code >= 400:
            print(f"  ERROR: HTTP {r.status_code}\n  {r.text[:500]}")
            sys.exit(1)
        print(f"  Updated: {rid}")
        return rid
    if dry:
        print(f"  [DRY] Would POST new Articles row with {len(fields)} fields")
        return None
    r = requests.post(
        f"{AIRTABLE_API_BASE}/{AIRTABLE_BASE_ID}/{ARTICLES_TID}",
        headers=H, json={"fields": fields, "typecast": True}, timeout=60,
    )
    if r.status_code >= 400:
        print(f"  ERROR: HTTP {r.status_code}\n  {r.text[:500]}")
        sys.exit(1)
    rid = r.json()["id"]
    print(f"  Created Articles row: {rid}")
    return rid


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    dry = args.dry_run

    print(f"=== Phase 2 bài 2 end-to-end ===")
    print(f"  primary_keyword: {PRIMARY_KW}")
    print(f"  article_id:      {ARTICLE_ID}")
    print()

    if not DRAFT_PATH.exists():
        print(f"ERROR: draft not found at {DRAFT_PATH}")
        return 1

    print("Step 1: fetch cover image (Unsplash)")
    image_data = find_cover_image(PRIMARY_KW)
    if not image_data:
        return 1
    print(f"  alt: {image_data['alt']}")
    print()

    print("Step 2: build record")
    record, faq_pairs, word_count = build_record(image_data)
    print(f"  title_tag       ({len(record['title_tag'])}/60): {record['title_tag']}")
    print(f"  meta_description ({len(record['meta_description'])}/155)")
    print(f"  body length:    {len(record['article_body_text'])} chars / ~{word_count} words")
    print(f"  schema length:  {len(record['schema_jsonld'])} chars")
    print(f"  FAQ pairs:      {len(faq_pairs)}")
    print()

    print("Step 3: insert/update Articles row")
    insert_article(record, dry)
    print()

    print(f"Done. mode={'DRY' if dry else 'LIVE'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
