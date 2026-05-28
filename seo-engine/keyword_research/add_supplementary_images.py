"""Add ONE supplementary Unsplash image per Phase 2+3 article body.

Strategy:
- Each article gets a content-specific image query (different from cover image)
- Inserts at mid-body break (just before the H2 closest to the midpoint)
- Format matches existing cover: ![alt](url)\n\n*Photo by [author] on [Unsplash]*
- Idempotent: skips articles that already have 2+ images
"""
from __future__ import annotations

import re
import sys
import time
from pathlib import Path

import requests

from config_kw import AIRTABLE_API_BASE, AIRTABLE_BASE_ID, AIRTABLE_PAT
from image_finder import find_cover_image

sys.path.insert(0, "/Users/phatnguyen/Downloads/OSR/seo-engine")
from table_ids import TABLE_IDS

H = {"Authorization": f"Bearer {AIRTABLE_PAT}", "Content-Type": "application/json"}
ARTICLES_TID = TABLE_IDS["Articles"]


IMAGE_PLAN = {
    # Phase 1
    "OSR-2026-05-21-001": "venture capital investor meeting boardroom",
    "OSR-2026-05-21-002": "vietnam shopping market consumer",
    "OSR-2026-05-21-003": "business strategy whiteboard planning",
    "OSR-2026-05-21-004": "developer ai coding workspace",
    "OSR-2026-05-21-005": "post-it notes wall brainstorm",
    "OSR-2026-05-21-006": "customer research interview notes",
    "OSR-2026-05-21-007": "morning commute coffee cup",
    "OSR-2026-05-21-008": "code editor laptop developer",
    "OSR-2026-05-21-009": "puzzle pieces fitting together",
    "OSR-2026-05-21-010": "ocean horizon calm water",
    # Phase 2
    "OSR-2026-05-22-001": "notebook hypothesis writing",
    "OSR-2026-05-22-002": "customer feedback interview",
    "OSR-2026-05-22-003": "compass direction navigation",
    "OSR-2026-05-22-004": "saigon city skyline",
    "OSR-2026-05-22-005": "vietnam street market",
    "OSR-2026-05-22-006": "shipping port container",
    "OSR-2026-05-22-007": "manufacturing facility industrial",
    "OSR-2026-05-22-008": "hanoi business district office building",
    "OSR-2026-05-22-009": "mobile payment qr code",
    "OSR-2026-05-22-010": "stock chart financial market",
    # Phase 3
    "OSR-2026-05-22-011": "presentation slides laptop business",
    "OSR-2026-05-22-012": "product prototype sketch notebook",
    "OSR-2026-05-22-013": "singapore skyline marina bay",
    "OSR-2026-05-22-014": "artificial intelligence circuit board",
    "OSR-2026-05-22-015": "developer typing code monitor",
    "OSR-2026-05-22-016": "marketing strategy whiteboard team",
    "OSR-2026-05-22-017": "handshake business agreement",
}


def find_midbody_h2_position(body: str) -> int:
    """Return the start-index of the H2 closest to body midpoint.

    Skips the first two H2s and the FAQ H2 — picks an inner-body H2.
    """
    h2_positions = [m.start() for m in re.finditer(r"^## (?!Frequently asked)", body, re.MULTILINE)]
    if len(h2_positions) < 4:
        # Short article: insert before last non-FAQ H2
        return h2_positions[-1] if h2_positions else len(body) // 2
    midpoint = len(body) // 2
    # Skip first H2 (too early — right after intro), skip last (FAQ)
    candidates = h2_positions[1:-1]
    # Pick closest to midpoint
    return min(candidates, key=lambda p: abs(p - midpoint))


def insert_image_block(body: str, image_data: dict) -> str:
    insert_pos = find_midbody_h2_position(body)
    block = (
        f"![{image_data['alt']}]({image_data['url']})\n\n"
        f"{image_data['credit']}\n\n"
    )
    return body[:insert_pos] + block + body[insert_pos:]


def count_images(body: str) -> int:
    return len(re.findall(r"!\[[^\]]*\]\(https?://[^)]+\)", body))


def fetch_article(article_id: str) -> dict | None:
    r = requests.get(
        f"{AIRTABLE_API_BASE}/{AIRTABLE_BASE_ID}/{ARTICLES_TID}",
        headers={"Authorization": f"Bearer {AIRTABLE_PAT}"},
        params=[("filterByFormula", f"{{article_id}}='{article_id}'")],
        timeout=30,
    )
    r.raise_for_status()
    recs = r.json().get("records", [])
    return recs[0] if recs else None


def patch_body(rid: str, new_body: str, dry: bool):
    if dry:
        return True
    r = requests.patch(
        f"{AIRTABLE_API_BASE}/{AIRTABLE_BASE_ID}/{ARTICLES_TID}/{rid}",
        headers=H,
        json={"fields": {"article_body_text": new_body}, "typecast": True},
        timeout=60,
    )
    if r.status_code >= 400:
        print(f"    ERROR HTTP {r.status_code}: {r.text[:300]}")
        return False
    return True


def main() -> int:
    dry = "--dry-run" in sys.argv
    ok = skip = fail = 0
    for aid, query in IMAGE_PLAN.items():
        print(f"\n=== {aid} === query={query!r}")
        rec = fetch_article(aid)
        if not rec:
            print("  ERROR: not found"); fail += 1; continue
        body = rec["fields"].get("article_body_text", "")
        n_imgs = count_images(body)
        if n_imgs >= 2:
            print(f"  SKIP: already has {n_imgs} images"); skip += 1; continue
        img = find_cover_image(query)
        if not img:
            # Retry with broader query
            broader = " ".join(query.split()[:2])
            print(f"  retry broader: {broader!r}")
            img = find_cover_image(broader)
        if not img:
            print("  ERROR: no image found"); fail += 1; continue
        print(f"  alt: {img['alt']}")
        new_body = insert_image_block(body, img)
        new_n = count_images(new_body)
        print(f"  body {len(body)} -> {len(new_body)} chars, imgs {n_imgs} -> {new_n}")
        if patch_body(rec["id"], new_body, dry):
            print(f"  {'[DRY] would PATCH' if dry else 'PATCH ok'}")
            ok += 1
        else:
            fail += 1
        time.sleep(0.3)
    print(f"\n=== Done ({'DRY' if dry else 'LIVE'}): ok={ok} skip={skip} fail={fail} ===")
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
