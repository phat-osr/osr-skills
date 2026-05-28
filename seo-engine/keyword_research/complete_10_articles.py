"""
Build 10 complete Articles rows for Phase 1.

Each row gets every field populated (except framer_url which fills after publish):
  - article_id, primary_keyword, search_volume, keyword_difficulty, signal_score
  - pattern, status='review'
  - title_tag, meta_description, slug
  - cover_image_url, cover_image_alt, cover_image_credit (via Unsplash + CSE fallback)
  - schema_jsonld (via osr_template.build_schema_jsonld)
  - article_body_text (finalized body via osr_template.finalize_body)
  - serp_insights_json (attachment via catbox.moe)
  - keyword_cluster_csv (attachment via catbox.moe)

Picks: 10 keywords from top 100 with bucket diversification:
  vn_vc:       2 (venture capital vietnam, vietnam market — FRESH bodies)
  framework:   5 (BMC, lean canvas, VPC, JTBD, blue ocean — v4 reuse)
  ai_build:    2 (vibe coding application, vibe coding tools — v4 reuse)
  validation:  1 (product market fit — v4 reuse)

Run:
    python complete_10_articles.py --dry-run
    python complete_10_articles.py
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import re
import subprocess
import sys
import time
from datetime import date
from pathlib import Path
from typing import Any

import requests

from airtable_helpers import fetch_all
from config_kw import AIRTABLE_API_BASE, AIRTABLE_BASE_ID, AIRTABLE_PAT, OUTPUT_DIR

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from table_ids import TABLE_IDS  # noqa: E402

from osr_template import (  # noqa: E402
    SITE, build_schema_jsonld, finalize_body, slugify, truncate,
)
from image_finder import find_cover_image  # noqa: E402
from v4_content import ARTICLES as V4_ARTICLES  # noqa: E402
from phase1_fresh import FRESH_ARTICLES  # noqa: E402
from optimize_titles import optimize_title  # noqa: E402
from render_paste_ready import clean_markdown  # noqa: E402
from phase1_extras import EXTRAS  # noqa: E402


HEADERS = {"Authorization": f"Bearer {AIRTABLE_PAT}", "Content-Type": "application/json"}
ARTICLES_TID = TABLE_IDS["Articles"]
KEYWORDS_TID = TABLE_IDS["Keywords"]
BATCHES_TID = TABLE_IDS["Batches"]

V4_BY_KEYWORD = {a["primary_keyword"]: a for a in V4_ARTICLES}
FRESH_BY_KEYWORD = {a["primary_keyword"]: a for a in FRESH_ARTICLES}


# ----------------------------- Picks -----------------------------
# Each pick maps the NEW primary_keyword (from top 100) to a body source.

PICKS = [
    # (primary_keyword, pattern, body_source_key_in_module, module)
    ("venture capital vietnam",            "sector_ideas",      "venture capital vietnam",       "fresh"),
    ("vietnam market",                     "sector_ideas",      "vietnam market",                "fresh"),
    ("examples for business model canvas", "framework_example", "business model canvas",         "v4"),
    ("vibe coding application",            "framework_example", "vibe coding",                   "v4"),
    ("lean canvas business model",         "framework_example", "lean startup model canvas",     "v4"),
    ("value proposition canvas model",     "framework_example", "value proposition canvas",      "v4"),
    ("jobs to be done framework",          "framework_example", "jobs to be done framework",     "v4"),
    ("vibe coding tools",                  "framework_example", "vibe coding tools",             "v4"),
    ("product market fit",                 "how_to_validate",   "product market fit",            "v4"),
    ("blue ocean vs red ocean strategy",   "framework_example", "what is the blue ocean strategy","v4"),
]


# ----------------------------- Helpers -----------------------------

def get_body_source(body_key: str, module: str) -> dict[str, Any]:
    if module == "fresh":
        return FRESH_BY_KEYWORD[body_key]
    return V4_BY_KEYWORD[body_key]


def build_title_tag(primary_keyword: str, pattern: str) -> str:
    kw = primary_keyword.strip()
    # Title-case but keep "and", "of", "the", "for", "in", "on", "to", "with", "vs"
    small = {"a","an","and","as","at","but","by","for","if","in","of","on",
             "or","the","to","vs","with"}
    parts = kw.split()
    cap = []
    for i, p in enumerate(parts):
        if i == 0 or p not in small:
            cap.append(p.capitalize())
        else:
            cap.append(p)
    base = " ".join(cap)
    suffix = " | OS Research"
    available = 65 - len(suffix)
    if len(base) > available:
        base = base[:available - 1].rstrip()
    return base + suffix


def build_meta_description(primary_keyword: str, tldr: str) -> str:
    # Use first 155 chars of TLDR as description
    tldr_clean = re.sub(r"\s+", " ", tldr).strip()
    if len(tldr_clean) <= 158:
        return tldr_clean
    return tldr_clean[:155].rstrip() + "..."


def upload_to_catbox(file_path: Path) -> str:
    """Upload to catbox.moe via curl. Returns the URL or empty."""
    try:
        r = subprocess.run(
            ["curl", "-s", "--max-time", "60", "-X", "POST",
             "https://catbox.moe/user/api.php",
             "-F", "reqtype=fileupload",
             "-F", f"fileToUpload=@{file_path}"],
            capture_output=True, text=True, timeout=90,
        )
        url = r.stdout.strip()
        if url.startswith("http"):
            return url
        print(f"    catbox upload returned: '{url[:100]}'")
        return ""
    except Exception as e:
        print(f"    catbox upload error: {e}")
        return ""


def patch_record(record_id: str, fields: dict[str, Any]) -> bool:
    """PATCH a single record with retries."""
    target = f"{AIRTABLE_API_BASE}/{AIRTABLE_BASE_ID}/{ARTICLES_TID}/{record_id}"
    payload = {"fields": fields, "typecast": True}
    for attempt in range(3):
        try:
            r = requests.patch(target, headers=HEADERS, json=payload, timeout=120)
            if r.status_code < 400:
                return True
            print(f"    PATCH HTTP {r.status_code}: {r.text[:200]}")
            return False
        except requests.exceptions.RequestException as e:
            print(f"    PATCH attempt {attempt+1}/3: {e.__class__.__name__}")
            time.sleep(3 * (attempt + 1))
    return False


def create_record(fields: dict[str, Any]) -> str:
    """Create a single Articles record, return record_id or ''.

    Strategy: create with non-attachment fields first; then PATCH attachments separately.
    Airtable rejects the combined CREATE+attachments payload silently on this plan.
    """
    slim = {k: v for k, v in fields.items()
            if k not in ("serp_insights_json",)}
    # NOTE: typecast is TOP-LEVEL only, not per-record. Per-record typecast triggers 422.
    payload = {"records": [{"fields": slim}], "typecast": True}
    for attempt in range(3):
        try:
            r = requests.post(
                f"{AIRTABLE_API_BASE}/{AIRTABLE_BASE_ID}/{ARTICLES_TID}",
                headers=HEADERS, json=payload, timeout=120,
            )
            if r.status_code < 400:
                rid = r.json()["records"][0]["id"]
                # Now PATCH attachments separately
                attach = {k: fields[k] for k in ("serp_insights_json",)
                          if k in fields}
                if attach:
                    if patch_record(rid, attach):
                        print(f"    ✓ attachments PATCHed")
                    else:
                        print(f"    ✗ attachments PATCH failed (record exists, run backfill)")
                return rid
            # Dump the failing payload for diagnosis
            dump_path = OUTPUT_DIR / "phase1_complete" / f"failed_{slim.get('article_id','x')}.json"
            dump_path.write_text(json.dumps(payload, indent=2))
            print(f"    CREATE HTTP {r.status_code}: {r.text[:400]}")
            print(f"    payload dumped to {dump_path}")
            return ""
        except requests.exceptions.RequestException as e:
            print(f"    CREATE attempt {attempt+1}/3: {e.__class__.__name__}")
            time.sleep(3 * (attempt + 1))
    return ""


# ----------------------------- Cluster CSV filter -----------------------------

STOPWORDS_FILTER = {
    "a","an","the","of","for","to","in","on","with","by","from","and","or",
    "is","are","what","how","why","when","where","who","best","top","free",
}


def keyword_tokens(s: str) -> set[str]:
    tokens = re.findall(r"[a-z0-9]+", s.lower())
    return {t for t in tokens if t and t not in STOPWORDS_FILTER and len(t) > 2}


def filter_cluster_keywords(primary: str, all_kws: list[dict], max_n: int = 30) -> list[dict]:
    primary_tokens = keyword_tokens(primary)
    if not primary_tokens:
        return []
    scored = []
    for r in all_kws:
        f = r["fields"]
        kw = f.get("keyword", "")
        if kw.lower() == primary.lower():
            continue
        kw_tokens = keyword_tokens(kw)
        if not kw_tokens:
            continue
        overlap = len(primary_tokens & kw_tokens)
        if overlap == 0:
            continue
        signal = f.get("signal_score", 0)
        scored.append({"kw_rec": f, "overlap": overlap, "signal": signal})
    scored.sort(key=lambda x: (x["overlap"], x["signal"]), reverse=True)
    return [s["kw_rec"] for s in scored[:max_n]]


# ----------------------------- SERP insights data -----------------------------
# Real WebSearch results (2026-05-21) inline. Includes top sources + PAA + competitor archetype.

SERP_DATA = {
    "venture capital vietnam": {
        "top_5_sources": [
            "Vietnam Briefing — Venture Capital in Vietnam: Funds, Trends, Deals (2025)",
            "Do Ventures + NIC — Vietnam Innovation & Tech Investment Report 2024",
            "PitchBook — Vietnam VC market profile",
            "Tracxn — Vietnam Startup Funding Tracker",
            "Cento Ventures — Southeast Asia Tech Investment Report H2 2024",
        ],
        "competitor_archetype": "Market-overview + fund roster + sector breakdown. Heavy on macro data, light on founder-level interpretation.",
        "paa": [
            "How big is the venture capital market in Vietnam?",
            "Who are the top VC firms in Vietnam?",
            "How many unicorns does Vietnam have?",
            "What sectors get the most VC funding in Vietnam?",
            "Is it easier to raise VC in Vietnam vs Singapore?",
        ],
        "gap_opportunity": "No top-5 result frames Vietnam as 'deep early stage, thin growth stage' — that's our angle. Add TRR-stage matrix for fundraising readiness.",
    },
    "vietnam market": {
        "top_5_sources": [
            "World Bank — Vietnam country profile 2024",
            "IMF — Vietnam Article IV Consultation 2024",
            "Vietnam Briefing — Vietnam Market Entry Guide 2025",
            "McKinsey — Vietnam Consumer Sentiment 2025",
            "Statista — Vietnam Market Outlook",
        ],
        "competitor_archetype": "Macro overview + sector list + outlook. Lacks operator-level reading on consumer purchasing power vs sticker GDP.",
        "paa": [
            "How big is the Vietnam economy?",
            "What is the Vietnam GDP growth rate?",
            "Which sectors are growing fastest in Vietnam?",
            "Is Vietnam a good market for foreign businesses?",
            "How does Vietnam compare to Indonesia and the Philippines?",
        ],
        "gap_opportunity": "Two-speed economy (HCMC/Hanoi vs other 61 provinces) is missing from top sources. Add honest middle-class addressable-market read.",
    },
    "examples for business model canvas": {
        "top_5_sources": [
            "Strategyzer — Business Model Canvas examples",
            "Creately — 20+ Business Model Canvas templates",
            "Miro — Business Model Canvas with examples",
            "Investopedia — Business Model Canvas Explained",
            "HubSpot — Business Model Canvas Examples",
        ],
        "competitor_archetype": "Examples gallery format. Each shows 3-7 example companies (Uber, Airbnb, Netflix). Strong on visuals, light on critical analysis.",
        "paa": [
            "What is the Business Model Canvas?",
            "What are examples of the Business Model Canvas?",
            "Who created the Business Model Canvas?",
            "What are the 9 blocks of the Business Model Canvas?",
            "How do you fill out a Business Model Canvas?",
        ],
        "gap_opportunity": "Examples mostly recycle the same 5 companies. OSR can add fresh examples from Vietnamese unicorns (VNG, MoMo) and apply validation lens.",
    },
    "vibe coding application": {
        "top_5_sources": [
            "Wikipedia — Vibe coding",
            "Google Cloud — What is vibe coding?",
            "IBM — What is vibe coding?",
            "Lovable.dev — Build apps with AI",
            "Replit blog — Vibe coding applications",
        ],
        "competitor_archetype": "Definitional + tools list + use cases. Karpathy origin story repeated. Stack Overflow critique cited.",
        "paa": [
            "What is a vibe coding application?",
            "What can you build with vibe coding?",
            "Is vibe coding production ready?",
            "What tools are used for vibe coding applications?",
            "How does vibe coding affect software engineering jobs?",
        ],
        "gap_opportunity": "No top source maps vibe coding to startup validation stages. OSR's TRR-stage matrix is unique angle.",
    },
    "lean canvas business model": {
        "top_5_sources": [
            "Ash Maurya / Leanstack — Lean Canvas",
            "Strategyzer — Lean Canvas vs Business Model Canvas",
            "Miro — Lean Canvas template",
            "Investopedia — Lean Canvas explained",
            "Forbes — Why use Lean Canvas",
        ],
        "competitor_archetype": "Side-by-side with BMC. Walkthrough of 9 blocks. Maurya quote frequently used.",
        "paa": [
            "What is the difference between Lean Canvas and Business Model Canvas?",
            "Who created the Lean Canvas?",
            "What are the 9 blocks of the Lean Canvas?",
            "When should you use Lean Canvas?",
            "What is the unfair advantage box in Lean Canvas?",
        ],
        "gap_opportunity": "Lean Canvas as a validation artifact (filled progressively per TRR stage) is not how competitors frame it. OSR angle.",
    },
    "value proposition canvas model": {
        "top_5_sources": [
            "Strategyzer — Value Proposition Canvas",
            "Miro — Value Proposition Canvas template",
            "Mind Tools — VPC explained",
            "Investopedia — Value Proposition Canvas",
            "Smartsheet — VPC template + examples",
        ],
        "competitor_archetype": "Strategyzer-derived. 6 blocks (3 customer, 3 value). Sticky-note examples. Often paired with BMC.",
        "paa": [
            "What is the Value Proposition Canvas?",
            "Who created the Value Proposition Canvas?",
            "How do you fill in the Value Proposition Canvas?",
            "What are the 6 blocks of the Value Proposition Canvas?",
            "What is the difference between BMC and VPC?",
        ],
        "gap_opportunity": "Customer Jobs framing rarely tied to JTBD methodology. OSR can bridge VPC and JTBD explicitly.",
    },
    "jobs to be done framework": {
        "top_5_sources": [
            "Strategyn / Tony Ulwick — JTBD framework",
            "HBR / Clay Christensen — Milkshake article",
            "Intercom — JTBD for product teams",
            "Mind the Product — JTBD explained",
            "Ash Maurya blog — JTBD vs personas",
        ],
        "competitor_archetype": "Ulwick canonical definition + Christensen milkshake. Functional/Emotional/Social split. Persona contrast.",
        "paa": [
            "What is the Jobs to Be Done framework?",
            "Who created Jobs to Be Done?",
            "How do you write a JTBD statement?",
            "What is the difference between JTBD and user stories?",
            "What is the difference between functional and emotional jobs?",
        ],
        "gap_opportunity": "JTBD interview methodology rarely tied to validation evidence thresholds. OSR can show JTBD as Problem Fit evidence.",
    },
    "vibe coding tools": {
        "top_5_sources": [
            "Lovable.dev — AI app builder",
            "v0.dev (Vercel) — UI generator",
            "Cursor — AI coding editor",
            "Claude Code — Anthropic CLI",
            "Replit + Bolt + Windsurf comparisons",
        ],
        "competitor_archetype": "Tool roundup. Comparison tables. Pricing + use case mapping. Heavy on feature lists, light on choosing-criteria.",
        "paa": [
            "What are the best vibe coding tools?",
            "What is the difference between Lovable and v0?",
            "Is Cursor or Claude Code better?",
            "What is Bolt.new used for?",
            "Are vibe coding tools free?",
        ],
        "gap_opportunity": "No top source breaks tools by validation use case (landing page vs prototype vs preorder). OSR matrix is unique.",
    },
    "product market fit": {
        "top_5_sources": [
            "Marc Andreessen — Original PMF essay (2007)",
            "Sean Ellis — PMF survey methodology",
            "Lenny's Newsletter — PMF measurement",
            "First Round Review — PMF stories",
            "Y Combinator — PMF guide",
        ],
        "competitor_archetype": "Andreessen + Ellis canon. PMF survey method (40% very disappointed). Founder anecdotes. Light on systematic measurement.",
        "paa": [
            "What is product market fit?",
            "How do you measure product market fit?",
            "What is the Sean Ellis 40 percent rule?",
            "How do you know you have product market fit?",
            "What comes after product market fit?",
        ],
        "gap_opportunity": "Few sources tie PMF to a validation framework with discrete evidence thresholds. OSR TRR scale provides that.",
    },
    "what is the blue ocean strategy": {
        "top_5_sources": [
            "Blue Ocean — official site (Kim & Mauborgne)",
            "HBR — Blue Ocean Strategy article archive",
            "Investopedia — Blue Ocean Strategy explained",
            "Mind Tools — Blue Ocean Strategy summary",
            "Strategyzer — Strategy Canvas walkthrough",
        ],
        "competitor_archetype": "Kim & Mauborgne canon. ERRC framework. Cirque du Soleil example. Red ocean vs blue ocean contrast.",
        "paa": [
            "What is the blue ocean strategy?",
            "Who created the blue ocean strategy?",
            "What is the ERRC framework?",
            "What is an example of a blue ocean strategy?",
            "What is the difference between blue ocean and red ocean?",
        ],
        "gap_opportunity": "Blue Ocean is presented as a 'find a new market' framework — rarely as a validation discipline. OSR can frame ERRC as a hypothesis system.",
    },
}


# ----------------------------- Main pipeline -----------------------------

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    # 1. Load Keywords (for signal/vol/kd lookup + cluster filter)
    print("=== Loading Keywords + Batches ===")
    all_kws = fetch_all(KEYWORDS_TID, fields=[
        "keyword", "signal_score", "volume_global_en", "difficulty_proxy",
        "cpc", "bucket", "seed_parent",
    ])
    kw_by_keyword = {r["fields"].get("keyword", ""): r["fields"] for r in all_kws}
    print(f"  Keywords: {len(all_kws)}")

    # Batches link
    batches = fetch_all(BATCHES_TID, fields=["batch_id"])
    batch_record_id = batches[0]["id"] if batches else None
    batch_id_str = batches[0]["fields"].get("batch_id", "OSR-B-20260521") if batches else "OSR-B-20260521"
    print(f"  Batch: {batch_id_str}")

    # Tmp dir
    tmp_dir = OUTPUT_DIR / "phase1_complete"
    tmp_dir.mkdir(exist_ok=True)

    # 2. Process each pick
    pub_date = str(date.today())
    print(f"\n=== Processing {len(PICKS)} picks ===")
    for i, (primary_kw, pattern, body_key, module) in enumerate(PICKS, start=1):
        print(f"\n[{i}/{len(PICKS)}] {primary_kw}  ({pattern})")

        # 2a. Get keyword metrics
        kw_meta = kw_by_keyword.get(primary_kw, {})
        vol = kw_meta.get("volume_global_en", 0)
        kd = kw_meta.get("difficulty_proxy", 0)
        signal = kw_meta.get("signal_score", 0)
        bucket = kw_meta.get("bucket", "")
        print(f"  metrics: vol={vol} kd={kd} signal={signal} bucket={bucket}")

        # 2b. Get body source
        src = get_body_source(body_key, module)
        body_md = src["article_body_md"]
        tldr = src["tldr_answer"]
        faq_pairs = json.loads(src["faq_block_json"])

        # 2c. Generate metadata
        article_id = f"OSR-2026-05-21-{i:03d}"
        # SERP-optimized title (number-driven / year-stamped / power phrases per keyword type)
        title_tag = optimize_title(primary_kw, pattern)
        meta_desc = build_meta_description(primary_kw, tldr)
        slug = slugify(primary_kw)
        print(f"  meta: title='{title_tag[:50]}...', slug='{slug}'")

        # 2d. Cover image (Unsplash)
        img = find_cover_image(primary_kw)
        cover_url = img.get("url", "")
        cover_alt = img.get("alt", primary_kw)
        cover_credit = img.get("credit", "")

        # 2e. Finalize body — brand naming + optional sections (per pattern) + cover image + em-dash removal
        final_body = finalize_body(
            body_md=body_md,
            pattern=pattern,
            primary_keyword=primary_kw,
            published_date=pub_date,
            cover_image_url=cover_url,
            cover_image_alt=cover_alt,
            cover_image_credit=cover_credit,
            extras=EXTRAS.get(primary_kw),
        )
        # Convert <aside> JSX TL;DR → blockquote markdown so Framer paste renders distinct
        final_body = clean_markdown(final_body)
        wc = len(final_body.split())
        print(f"  body: {len(final_body)} chars, {wc} words")

        # 2f. Schema JSON-LD
        schema = build_schema_jsonld(
            primary_keyword=primary_kw,
            h1=primary_kw.title(),
            title_tag=title_tag,
            meta_description=meta_desc,
            tldr=tldr,
            slug=slug,
            cover_image_url=cover_url,
            published_date=pub_date,
            word_count=wc,
            faq_pairs=faq_pairs,
            pattern=pattern,
        )
        print(f"  schema: {len(schema)} chars")

        # 2g. SERP insights JSON
        serp_data = SERP_DATA.get(primary_kw, {})
        serp_payload = {
            "primary_keyword": primary_kw,
            "fetched_at": pub_date,
            "method": "WebSearch (Claude built-in)",
            **serp_data,
        }
        serp_file = tmp_dir / f"{article_id}_serp.json"
        serp_file.write_text(json.dumps(serp_payload, ensure_ascii=False, indent=2))
        # 2g.1 People Also Ask — inline text field, one Q per line.
        paa_list = serp_data.get("paa", [])
        paa_text = "\n".join(paa_list) if paa_list else ""

        # 2h. Cluster — plain keyword list, one per line.
        cluster_kws = filter_cluster_keywords(primary_kw, all_kws, max_n=30)
        kws_only = [(ck.get("keyword") or "").strip() for ck in cluster_kws]
        kws_only = [k for k in kws_only if k]
        cluster_text = "\n".join(kws_only) if kws_only else "(no related keywords found)"
        print(f"  cluster: {len(kws_only)} keywords ({len(cluster_text)} chars)")

        if args.dry_run:
            continue

        # 2i. Upload SERP JSON to catbox (still an attachment — JSON structure preserved)
        serp_url = upload_to_catbox(serp_file)
        time.sleep(1)
        print(f"  serp catbox: {serp_url}")

        # 2j. Build the create payload
        fields = {
            "article_id": article_id,
            "primary_keyword": primary_kw,
            "search_volume": vol,
            "keyword_difficulty": kd,
            "signal_score": signal,
            "pattern": pattern,
            "status": "review",
            "title_tag": title_tag,
            "meta_description": meta_desc,
            "slug": slug,
            "cover_image_url": cover_url,
            "cover_image_alt": cover_alt,
            "cover_image_credit": cover_credit,
            "schema_jsonld": schema,
            "article_body_text": final_body[:99000],
        }
        # batch_id is singleLineText (not linked record) — pass as string
        fields["batch_id"] = batch_id_str
        fields["keyword_cluster"] = cluster_text
        predicted_url = f"{SITE}/blog/{slug}"
        fields["final_url"] = predicted_url
        fields["framer_url"] = predicted_url  # pre-fill; Pete updates after publish if different
        if paa_text:
            fields["people_also_ask"] = paa_text
        if serp_url:
            fields["serp_insights_json"] = [{"url": serp_url, "filename": f"{article_id}_serp.json"}]

        rid = create_record(fields)
        if rid:
            print(f"  ✓ created Articles record {rid}")
        else:
            print(f"  ✗ CREATE failed")
        time.sleep(0.5)

    print("\nDone.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
