"""
Convert article_body_text (markdown with JSX leftovers) into:
  1. article_body_text — cleaned markdown (no JSX, no inline image, no caption)
  2. article_body_html — rendered HTML for paste-into-Framer with formatting

Why both?
  - Markdown is the canonical source (small, editable, version-friendly)
  - HTML is the paste-ready format; Pete opens render OR copies HTML view → paste
    into Framer rich text editor which respects HTML formatting (h2, bullets, table, bold).

Run:
    python render_paste_ready.py --dry-run
    python render_paste_ready.py
"""
from __future__ import annotations

import argparse
import re
import sys
import time
from pathlib import Path

import markdown
import requests

from airtable_helpers import fetch_all
from config_kw import (
    AIRTABLE_API_BASE, AIRTABLE_BASE_ID, AIRTABLE_META_BASE, AIRTABLE_PAT,
    OUTPUT_DIR,
)

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from table_ids import TABLE_IDS  # noqa: E402

HEADERS = {"Authorization": f"Bearer {AIRTABLE_PAT}", "Content-Type": "application/json"}
ARTS = TABLE_IDS["Articles"]


def clean_markdown(body_md: str) -> str:
    """Strip only Framer-unfriendly markup; keep image caption for attribution.

    1. <aside className="tldr"> JSX wrapper → strip, keep inner **TL;DR.** content
       as a plain bold paragraph (Framer ignores JSX).
    2. Image caption line `*Photo by [X](url) on [Unsplash](url)*` after image →
       KEEP. Unsplash license requires attribution; better inline than separate
       field for paste workflow.
    """
    s = body_md

    # 1. Strip <aside> wrapper — keep inner content verbatim
    s = re.sub(
        r'<aside\s+className="tldr">\s*\n?(.*?)\n?\s*</aside>',
        lambda m: m.group(1).strip(),
        s,
        flags=re.DOTALL,
    )
    s = re.sub(r'<aside[^>]*>', '', s)
    s = re.sub(r'</aside>', '', s)

    # 2. Collapse triple+ newlines
    s = re.sub(r'\n{3,}', '\n\n', s)
    return s.strip()


def render_html(body_md: str) -> str:
    """Render cleaned markdown to HTML — preserves headings, lists, tables, bold."""
    extensions = ["tables", "fenced_code", "sane_lists"]
    html = markdown.markdown(body_md, extensions=extensions)
    # Wrap in a container with light inline styles so Framer's paste sees structure
    return html


def patch(record_id: str, fields: dict) -> bool:
    target = f"{AIRTABLE_API_BASE}/{AIRTABLE_BASE_ID}/{ARTS}/{record_id}"
    for attempt in range(3):
        try:
            r = requests.patch(target, headers=HEADERS,
                               json={"fields": fields, "typecast": True}, timeout=120)
            if r.status_code < 400:
                return True
            print(f"    PATCH HTTP {r.status_code}: {r.text[:300]}")
            return False
        except requests.exceptions.RequestException as e:
            print(f"    PATCH attempt {attempt+1}: {e.__class__.__name__}")
            time.sleep(3 * (attempt + 1))
    return False


def ensure_html_field() -> None:
    r = requests.get(f"{AIRTABLE_META_BASE}/tables", headers=HEADERS, timeout=30).json()
    table = next(t for t in r["tables"] if t["id"] == ARTS)
    existing = {f["name"] for f in table["fields"]}
    if "article_body_html" in existing:
        print("  [=] article_body_html exists")
        return
    r = requests.post(
        f"{AIRTABLE_META_BASE}/tables/{ARTS}/fields",
        headers=HEADERS,
        json={"name": "article_body_html", "type": "multilineText",
              "description": "Rendered HTML for paste-into-Framer. Copy from Airtable cell or open the local HTML preview, then paste into Framer's rich text editor."},
        timeout=30,
    )
    print(f"  [+] create article_body_html: HTTP {r.status_code}")
    if r.status_code >= 400:
        print(r.text[:200])


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not args.dry_run:
        ensure_html_field()

    # Output dir for local HTML previews
    preview_dir = OUTPUT_DIR / "framer_paste_html"
    preview_dir.mkdir(exist_ok=True)

    arts = fetch_all(ARTS, fields=["article_id", "primary_keyword", "article_body_text"])
    print(f"\nArticles: {len(arts)}\n")

    for art in sorted(arts, key=lambda x: x["fields"].get("article_id", "")):
        f = art["fields"]
        aid = f.get("article_id", "")
        body_old = f.get("article_body_text", "") or ""
        kw = f.get("primary_keyword", "")

        # 1. Clean markdown
        body_clean = clean_markdown(body_old)
        # 2. Render HTML
        body_html = render_html(body_clean)

        # Save preview file (Pete opens in browser → copies rich text → pastes to Framer)
        preview_file = preview_dir / f"{aid}.html"
        preview_file.write_text(
            f"<!DOCTYPE html>\n"
            f"<html><head><meta charset='utf-8'>"
            f"<title>{kw}</title>"
            f"<style>body{{font-family:-apple-system,BlinkMacSystemFont,sans-serif;"
            f"max-width:760px;margin:40px auto;padding:0 20px;color:#222;line-height:1.6}}"
            f"h1{{font-size:2em}}h2{{margin-top:1.6em;font-size:1.4em;border-bottom:1px solid #eee;padding-bottom:6px}}"
            f"h3{{margin-top:1.2em;font-size:1.15em}}"
            f"table{{border-collapse:collapse;margin:16px 0;width:100%}}"
            f"th,td{{border:1px solid #ddd;padding:8px 12px;text-align:left}}"
            f"th{{background:#f7f7f7;font-weight:600}}"
            f"code{{background:#f4f4f4;padding:2px 5px;border-radius:3px;font-size:0.9em}}"
            f"hr{{border:0;border-top:1px solid #eee;margin:2em 0}}"
            f"</style></head><body>\n"
            f"{body_html}\n"
            f"</body></html>"
        )
        print(f"  {aid:<22} md={len(body_clean):>5} html={len(body_html):>5} → {preview_file.name}")

        if args.dry_run:
            continue

        # PATCH both fields
        patch(art["id"], {
            "article_body_text": body_clean[:99000],
            "article_body_html": body_html[:99000],
        })
        time.sleep(0.3)

    print(f"\nLocal HTML previews: {preview_dir}/")
    print("  Workflow A: open *.html in browser → copy all → paste into Framer (preserves format)")
    print("  Workflow B: copy article_body_html cell from Airtable → paste as HTML in Framer")
    return 0


if __name__ == "__main__":
    sys.exit(main())
