"""
Refresh article_body_text for the 10 Phase 1 articles:
  - Include cover image markdown in body (as before)
  - Convert <aside className="tldr"> JSX → markdown blockquote
  - Apply brand naming + strip optional sections
  - Clear article_body_html (no longer used; Pete prefers markdown paste workflow)

Run:
    python refresh_10_bodies.py
"""
from __future__ import annotations

import json
import sys
import time
from datetime import date
from pathlib import Path

import requests

from airtable_helpers import fetch_all
from config_kw import AIRTABLE_API_BASE, AIRTABLE_BASE_ID, AIRTABLE_PAT

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from table_ids import TABLE_IDS  # noqa: E402

from complete_10_articles import PICKS, get_body_source
from osr_template import finalize_body
from render_paste_ready import clean_markdown
from phase1_extras import EXTRAS

HEADERS = {"Authorization": f"Bearer {AIRTABLE_PAT}", "Content-Type": "application/json"}
ARTS = TABLE_IDS["Articles"]


def main() -> int:
    arts = fetch_all(ARTS, fields=[
        "article_id", "primary_keyword", "pattern",
        "cover_image_url", "cover_image_alt", "cover_image_credit",
    ])
    by_kw = {r["fields"].get("primary_keyword"): r for r in arts}
    pub_date = str(date.today())

    for primary_kw, pattern, body_key, module in PICKS:
        art = by_kw.get(primary_kw)
        if not art:
            print(f"  skip {primary_kw}: no row found")
            continue
        src = get_body_source(body_key, module)
        f = art["fields"]
        body = finalize_body(
            body_md=src["article_body_md"],
            pattern=pattern,
            primary_keyword=primary_kw,
            published_date=pub_date,
            cover_image_url=f.get("cover_image_url"),
            cover_image_alt=f.get("cover_image_alt"),
            cover_image_credit=f.get("cover_image_credit"),
            extras=EXTRAS.get(primary_kw),
        )
        body = clean_markdown(body)

        r = requests.patch(
            f"{AIRTABLE_API_BASE}/{AIRTABLE_BASE_ID}/{ARTS}/{art['id']}",
            headers=HEADERS,
            json={"fields": {
                "article_body_text": body[:99000],
            }, "typecast": True},
            timeout=120,
        )
        ok = "✓" if r.status_code < 400 else "✗"
        wc = len(body.split())
        print(f"  {ok} {f.get('article_id'):<22} {len(body):>5} chars / {wc:>4} words | {primary_kw[:40]}")
        if r.status_code >= 400:
            print(f"      {r.text[:200]}")
        time.sleep(0.3)
    return 0


if __name__ == "__main__":
    sys.exit(main())
