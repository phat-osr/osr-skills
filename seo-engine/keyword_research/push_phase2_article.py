"""
Generic end-to-end push for any Phase 2 bài.

Reads config from phase2_picks.PICKS[bai_num]. Builds full Articles row,
PATCHes or POSTs to Airtable, uploads serp_insights_json to catbox.

Usage:
    python3 push_phase2_article.py --bai 3 --dry-run
    python3 push_phase2_article.py --bai 3
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
from phase2_picks import PICKS, BATCH_ID, INTERNAL_ANCHORS, OUTBOUND_DEFAULT

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from table_ids import TABLE_IDS  # noqa: E402

H = {"Authorization": f"Bearer {AIRTABLE_PAT}", "Content-Type": "application/json"}
ARTICLES_TID = TABLE_IDS["Articles"]


def inject_simple_links(body: str, outbound_extra: dict) -> str:
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
                out = out[:idx] + f"[{anchor_text}]({href})" + out[end:]
                used.add(trigger)
                break
            idx = lo.find(trigger.lower(), idx + 1)
    outbound = {**OUTBOUND_DEFAULT, **outbound_extra}
    for anchor, href in outbound.items():
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


def build_record(cfg: dict, image_data: dict) -> tuple[dict, list, int]:
    draft_path = Path(__file__).parent / "phase2_drafts" / cfg["draft_file"]
    body_md = draft_path.read_text()
    tldr_start = body_md.find("**TL;DR.**") + len("**TL;DR.**")
    tldr_end = body_md.find("</aside>")
    tldr = body_md[tldr_start:tldr_end].strip()

    primary_kw = cfg["primary_keyword"]
    slug = slugify(primary_kw)
    title = cfg.get("title") or optimize_title(primary_kw, cfg["pattern"])
    meta = truncate(cfg["meta_description"], 155)
    word_count = len(body_md.split())

    # Parse FAQ pairs
    faq_pairs = []
    faq_block = body_md.split("## Frequently asked questions")[-1] if "## Frequently asked questions" in body_md else ""
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

    schema = build_schema_jsonld(
        primary_keyword=primary_kw,
        h1=cfg["h1_for_schema"],
        title_tag=title,
        meta_description=meta,
        tldr=tldr,
        slug=slug,
        cover_image_url=image_data["url"],
        published_date=str(date.today()),
        word_count=word_count,
        faq_pairs=faq_pairs,
        pattern=cfg["pattern"],
    )

    finalized = finalize_body(
        body_md=body_md,
        pattern=cfg["pattern"],
        primary_keyword=primary_kw,
        published_date=str(date.today()),
        cover_image_url=image_data["url"],
        cover_image_alt=image_data["alt"],
        cover_image_credit=image_data["credit"],
    )
    finalized = inject_simple_links(finalized, cfg.get("outbound_extra", {}))
    finalized = clean_markdown(finalized)

    framer_url = f"https://www.osresearch.vn/blog/{slug}"

    return {
        "article_id": cfg["article_id"],
        "batch_id": BATCH_ID,
        "primary_keyword": primary_kw,
        "search_volume": cfg["sv"],
        "keyword_difficulty": cfg["kd"],
        "signal_score": cfg["signal"],
        "pattern": cfg["pattern"],
        "status": "review",
        "title_tag": title,
        "meta_description": meta,
        "slug": slug,
        "cover_image_url": image_data["url"],
        "cover_image_alt": image_data["alt"],
        "cover_image_credit": image_data["credit"],
        "schema_jsonld": schema,
        "article_body_text": finalized,
        "keyword_cluster": "\n".join(cfg["cluster"]),
        "people_also_ask": "\n".join(cfg["paa"]),
        "framer_url": framer_url,
    }, faq_pairs, word_count


def upload_to_catbox(content: bytes, filename: str) -> str:
    r = requests.post(
        "https://catbox.moe/user/api.php",
        data={"reqtype": "fileupload"},
        files={"fileToUpload": (filename, content, "application/json")},
        timeout=30,
    )
    r.raise_for_status()
    url = r.text.strip()
    if not url.startswith("https://"):
        raise RuntimeError(f"catbox upload failed: {url}")
    return url


def insert_article(fields: dict, dry: bool) -> str | None:
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
            print(f"  ERROR: HTTP {r.status_code}\n  {r.text[:500]}"); sys.exit(1)
        print(f"  Updated: {rid}")
        return rid
    if dry:
        print(f"  [DRY] Would POST new with {len(fields)} fields"); return None
    r = requests.post(
        f"{AIRTABLE_API_BASE}/{AIRTABLE_BASE_ID}/{ARTICLES_TID}",
        headers=H, json={"fields": fields, "typecast": True}, timeout=60,
    )
    if r.status_code >= 400:
        print(f"  ERROR: HTTP {r.status_code}\n  {r.text[:500]}"); sys.exit(1)
    rid = r.json()["id"]
    print(f"  Created Articles row: {rid}")
    return rid


def push_serp_insights(cfg: dict, rid: str, dry: bool):
    si = cfg["serp_insights"]
    payload = {
        "primary_keyword": cfg["primary_keyword"],
        "fetched_at": str(date.today()),
        "method": "WebSearch + WebFetch (Claude built-in)",
        "top_5_sources": si["top_5_sources"],
        "competitor_format_notes": si["competitor_format_notes"],
        "identified_gap": si["identified_gap"],
        "unique_angle": si["unique_angle"],
        "paa": cfg["paa"],
        "gap_opportunity": si["gap_opportunity"],
    }
    content = json.dumps(payload, indent=2, ensure_ascii=False).encode("utf-8")
    filename = f"{cfg['article_id']}_serp.json"
    print(f"  serp_insights: {len(content)} bytes")
    if dry:
        print(f"  [DRY] Would upload + PATCH"); return
    url = upload_to_catbox(content, filename)
    print(f"  catbox URL: {url}")
    r = requests.patch(
        f"{AIRTABLE_API_BASE}/{AIRTABLE_BASE_ID}/{ARTICLES_TID}/{rid}",
        headers=H,
        json={
            "fields": {"serp_insights_json": [{"url": url, "filename": filename}]},
            "typecast": True,
        },
        timeout=60,
    )
    if r.status_code >= 400:
        print(f"  ERROR attaching serp_insights: HTTP {r.status_code} {r.text[:300]}")
        return
    print(f"  attachment PATCH ok")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--bai", type=int, required=True, help="Bài number (3-10)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    dry = args.dry_run

    if args.bai not in PICKS:
        print(f"ERROR: bài {args.bai} not in PICKS registry"); return 1
    cfg = PICKS[args.bai]

    print(f"=== Phase 2 bài {args.bai} end-to-end ===")
    print(f"  article_id: {cfg['article_id']}")
    print(f"  primary_kw: {cfg['primary_keyword']}")
    print(f"  pattern:    {cfg['pattern']}")
    print()

    draft_path = Path(__file__).parent / "phase2_drafts" / cfg["draft_file"]
    if not draft_path.exists():
        print(f"ERROR: draft not found at {draft_path}"); return 1

    print("Step 1: fetch cover image")
    img_query = cfg.get("image_query_override") or cfg["primary_keyword"]
    image_data = find_cover_image(img_query)
    if not image_data:
        print(f"  retry with broader query")
        image_data = find_cover_image("compass direction")
    if not image_data:
        return 1
    print(f"  alt: {image_data['alt']}")
    print()

    print("Step 2: build record")
    record, faq_pairs, word_count = build_record(cfg, image_data)
    print(f"  title  ({len(record['title_tag'])}/60): {record['title_tag']}")
    print(f"  meta   ({len(record['meta_description'])}/155)")
    print(f"  body   {len(record['article_body_text'])} chars / ~{word_count} words")
    print(f"  schema {len(record['schema_jsonld'])} chars")
    print(f"  FAQ:   {len(faq_pairs)}")
    print()

    print("Step 3: insert/update Articles row")
    rid = insert_article(record, dry)
    print()

    if rid:
        print("Step 4: serp_insights attachment")
        push_serp_insights(cfg, rid, dry)
        print()

    print(f"Done. mode={'DRY' if dry else 'LIVE'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
