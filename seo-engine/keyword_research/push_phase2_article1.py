"""
End-to-end push for Phase 2 bài 1: validated learning lean startup.

Steps:
1. Build title_tag (via optimize_titles)
2. Build meta_description + slug
3. Use cached Unsplash image (already verified)
4. Build PAA + keyword cluster from WebSearch research
5. Build JSON-LD schema
6. Run finalize_body on the markdown
7. Create OSR-B-2026-05-PHASE2 Batches row (if not exists)
8. Insert Articles row

Run:
    python3 push_phase2_article1.py --dry-run
    python3 push_phase2_article1.py
"""
from __future__ import annotations

import argparse
import json
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

# ----------------------------- Bài 1 specifics -----------------------------

PRIMARY_KW = "validated learning lean startup"
PATTERN = "framework_example"
BATCH_ID = "OSR-B-2026-05-PHASE2"
ARTICLE_ID = "OSR-2026-05-22-001"
SV = 20
KD = 8
SIGNAL = 52.7

# From Airtable Keywords pool (already cached)
DRAFT_PATH = Path(__file__).parent / "phase2_drafts" / "01-validated-learning-lean-startup.md"

# Hand-picked title override (optimize_titles default is awkward for this kw)
TITLE_OVERRIDE = "Validated Learning in Lean Startup: 2026 Guide"

META_DESCRIPTION = (
    "Validated learning is the only standard of evidence that qualifies a lean startup "
    "experiment. Four tests, common traps, and how to apply it."
)

# PAA — extracted from WebSearch on the primary keyword
PAA = [
    "What is validated learning in The Lean Startup?",
    "How is validated learning different from regular learning?",
    "What are examples of validated learning experiments?",
    "How do you measure validated learning?",
    "What is the Build-Measure-Learn loop?",
]

# Keyword cluster — top related from WebSearch + adjacent pool keywords
CLUSTER = [
    "the lean startup",
    "eric ries",
    "build measure learn",
    "build-measure-learn loop",
    "minimum viable product",
    "mvp",
    "lean startup methodology",
    "validated learning examples",
    "innovation accounting",
    "pivot or persevere",
    "lean startup principles",
    "hypothesis testing",
    "startup experiments",
    "vanity metrics",
    "actionable metrics",
    "product market fit",
    "lean canvas",
    "business model canvas",
    "customer development",
    "steve blank",
    "continuous deployment",
    "split testing",
    "ab testing",
    "cohort analysis",
    "five whys",
    "pivot strategy",
    "the lean startup book",
    "startup pivots",
    "jobs to be done",
    "problem-solution fit",
]

# Simple internal anchor map — links to existing OSR posts where anchor matches.
# Slugs verified against Airtable: only "startup-validation-studio", "experiment-library",
# "six-week-testing-cycle" exist as published; "product-market-fit" is Phase 1 predicted URL.
INTERNAL_ANCHORS = {
    "startup experiment library": ("startup experiment library", "https://www.osresearch.vn/blog/experiment-library"),
    "six week testing cycle": ("six week testing cycle", "https://www.osresearch.vn/blog/six-week-testing-cycle"),
    "product-market fit": ("product-market fit", "https://www.osresearch.vn/blog/product-market-fit"),
    "startup validation studio": ("startup validation studio", "https://www.osresearch.vn/blog/startup-validation-studio"),
}

# Outbound canonical sources
OUTBOUND_ANCHORS = {
    "Eric Ries": "http://www.startuplessonslearned.com/2009/04/validated-learning-about-customers.html",
    "Build-Measure-Learn": "https://theleanstartup.com/principles",
}


def inject_simple_links(body: str) -> str:
    """Replace first occurrence of each anchor with a markdown link. Idempotent for already-linked text."""
    out = body
    # Internal — match by lowercased anchor
    used = set()
    for trigger, (anchor_text, href) in INTERNAL_ANCHORS.items():
        if trigger in used:
            continue
        # only replace first occurrence outside of an existing link
        lo = out.lower()
        # Find first index where trigger appears not preceded by '[' or '(' (rough heuristic)
        idx = lo.find(trigger.lower())
        while idx != -1:
            # check the surrounding 1 char on each side to avoid existing markdown links
            before = out[idx-1] if idx > 0 else ""
            after_blob = out[idx:idx+30]
            if before not in "[(":
                # Wrap exact-case text from out
                end = idx + len(trigger)
                exact = out[idx:end]
                replacement = f"[{anchor_text}]({href})"
                out = out[:idx] + replacement + out[end:]
                used.add(trigger)
                break
            idx = lo.find(trigger.lower(), idx + 1)
    # Outbound
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
    # TLDR is the first <aside> block — extract for schema.abstract
    tldr_start = body_md.find("**TL;DR.**") + len("**TL;DR.**")
    tldr_end = body_md.find("</aside>")
    tldr = body_md[tldr_start:tldr_end].strip()

    slug = slugify(PRIMARY_KW)
    title = TITLE_OVERRIDE if TITLE_OVERRIDE else optimize_title(PRIMARY_KW, PATTERN)
    meta = truncate(META_DESCRIPTION, 155)

    # Word count for schema
    word_count = len(body_md.split())

    # FAQ pairs for schema — parse Q:/A: pairs from the FAQ section
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
        h1="Validated Learning in Lean Startup",
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

    # Finalize body — apply brand naming, em-dash removal, cover image insertion
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
    # Strip JSX aside wrapper for Framer paste — converts <aside className="tldr">...</aside>
    # into plain bold TLDR markdown (passes audit "TL;DR plain bold" check)
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


def ensure_batch(dry: bool):
    """Create OSR-B-2026-05-PHASE2 Batches row if not already present."""
    r = requests.get(
        f"{AIRTABLE_API_BASE}/{AIRTABLE_BASE_ID}/{BATCHES_TID}",
        headers=H,
        params=[("filterByFormula", f"{{batch_id}}='{BATCH_ID}'")],
        timeout=30,
    )
    r.raise_for_status()
    recs = r.json().get("records", [])
    if recs:
        print(f"  Batches row exists: {recs[0]['id']}")
        return
    fields = {
        "batch_id": BATCH_ID,
        "created_date": str(date.today()),
        "theme_label": "phase 2: OSR-aligned picks (vn_vc=7, validation=2, framework=1)",
        "article_count": 10,
        "total_volume": 4300,
        "avg_kd": 7.5,
        "status": "review",
        "notes": "Phase 2: 10 articles picked from unused top-100 pool, filtered for OSR brand fit + writability. Bài 1: validated learning lean startup.",
    }
    if dry:
        print(f"  [DRY] Would create Batches row: {fields}")
        return
    r = requests.post(
        f"{AIRTABLE_API_BASE}/{AIRTABLE_BASE_ID}/{BATCHES_TID}",
        headers=H,
        json={"fields": fields, "typecast": True},
        timeout=30,
    )
    if r.status_code >= 400:
        print(f"  ERROR creating batch: HTTP {r.status_code}\n  {r.text[:500]}")
        sys.exit(1)
    print(f"  Created Batches row: {r.json()['id']}")


def insert_article(fields: dict, dry: bool):
    # Verify article_id not already in table
    r = requests.get(
        f"{AIRTABLE_API_BASE}/{AIRTABLE_BASE_ID}/{ARTICLES_TID}",
        headers=H,
        params=[("filterByFormula", f"{{article_id}}='{fields['article_id']}'")],
        timeout=30,
    )
    r.raise_for_status()
    existing = r.json().get("records", [])
    if existing:
        print(f"  Article {fields['article_id']} already exists at {existing[0]['id']} — will UPDATE")
        if dry:
            print(f"  [DRY] Would PATCH {existing[0]['id']} with {len(fields)} fields")
            return existing[0]["id"]
        r = requests.patch(
            f"{AIRTABLE_API_BASE}/{AIRTABLE_BASE_ID}/{ARTICLES_TID}/{existing[0]['id']}",
            headers=H,
            json={"fields": fields, "typecast": True},
            timeout=60,
        )
        if r.status_code >= 400:
            print(f"  ERROR updating: HTTP {r.status_code}\n  {r.text[:500]}")
            sys.exit(1)
        print(f"  Updated article: {existing[0]['id']}")
        return existing[0]["id"]

    if dry:
        print(f"  [DRY] Would POST new Articles row with {len(fields)} fields")
        return None
    r = requests.post(
        f"{AIRTABLE_API_BASE}/{AIRTABLE_BASE_ID}/{ARTICLES_TID}",
        headers=H,
        json={"fields": fields, "typecast": True},
        timeout=60,
    )
    if r.status_code >= 400:
        print(f"  ERROR creating: HTTP {r.status_code}\n  {r.text[:500]}")
        sys.exit(1)
    rid = r.json()["id"]
    print(f"  Created Articles row: {rid}")
    return rid


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    dry = args.dry_run

    print(f"=== Phase 2 bài 1 end-to-end ===")
    print(f"  primary_keyword: {PRIMARY_KW}")
    print(f"  article_id:      {ARTICLE_ID}")
    print(f"  batch_id:        {BATCH_ID}")
    print(f"  pattern:         {PATTERN}")
    print(f"  draft path:      {DRAFT_PATH}")
    print()

    if not DRAFT_PATH.exists():
        print(f"ERROR: draft not found at {DRAFT_PATH}")
        return 1

    print("Step 1: fetch cover image (Unsplash)")
    image_data = find_cover_image(PRIMARY_KW)
    if not image_data:
        print("  ERROR: no cover image found")
        return 1
    print(f"  image: {image_data['url'][:80]}...")
    print(f"  alt:   {image_data['alt']}")
    print(f"  credit: {image_data['credit'][:60]}...")
    print()

    print("Step 2: build record (title, meta, schema, finalize body)")
    record, faq_pairs, word_count = build_record(image_data)
    print(f"  title_tag       ({len(record['title_tag'])}/60): {record['title_tag']}")
    print(f"  meta_description ({len(record['meta_description'])}/155): {record['meta_description']}")
    print(f"  slug:           {record['slug']}")
    print(f"  framer_url:     {record['framer_url']}")
    print(f"  body length:    {len(record['article_body_text'])} chars / ~{word_count} words")
    print(f"  schema length:  {len(record['schema_jsonld'])} chars")
    print(f"  FAQ pairs:      {len(faq_pairs)}")
    print(f"  PAA count:      {len(PAA)}")
    print(f"  cluster count:  {len(CLUSTER)}")
    print()

    print("Step 3: ensure Batches row exists")
    ensure_batch(dry)
    print()

    print("Step 4: insert/update Articles row")
    rid = insert_article(record, dry)
    print()

    print(f"Done. mode={'DRY' if dry else 'LIVE'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
