"""
Inject inbound (internal) + outbound (external) contextual links into 10 Phase 1
article bodies. Replaces first meaningful mention of each anchor phrase with a
markdown link. Skips headings, code blocks, and existing links.

Cap per article: 3-5 internal + 2-5 external.

Run:
    python inject_links.py --dry-run
    python inject_links.py
"""
from __future__ import annotations

import argparse
import re
import sys
import time
from pathlib import Path

import requests

from airtable_helpers import fetch_all
from config_kw import AIRTABLE_API_BASE, AIRTABLE_BASE_ID, AIRTABLE_PAT

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from table_ids import TABLE_IDS  # noqa: E402

from osr_template import SITE  # noqa: E402

HEADERS = {"Authorization": f"Bearer {AIRTABLE_PAT}", "Content-Type": "application/json"}
ARTS = TABLE_IDS["Articles"]

# Internal links — point to existing osresearch.vn posts. Anchors derived from
# actual body content (scanned via debug script). Order matters: longer phrases first.
INTERNAL_LINKS = [
    # (anchor, target slug)
    ("Total Risk Reduced",           "startup-validation-studio"),
    ("OS Research methodology",      "startup-validation-studio"),
    ("modern Vietnamese household",  "modern-vietnamese-household"),
    ("Vietnamese household",         "modern-vietnamese-household"),
    ("Vietnamese consumer",          "modern-vietnamese-household"),
    ("Business Model Canvas",        "business-model-canvas"),
    ("Value Proposition Canvas",     "value-proposition-canvas"),
    ("Blue Ocean Strategy",          "blue-ocean-strategy"),
    ("six-week testing cycle",       "six-week-testing-cycle"),
    ("testing cycle",                "six-week-testing-cycle"),
    ("experiment library",           "experiment-library"),
    ("Test Card",                    "experiment-library"),
    ("Learning Card",                "experiment-library"),
    ("pitch deck",                   "first-business-pitch"),
    ("one-page brief",               "first-business-pitch"),
    ("TRR",                          "startup-validation-studio"),
]

# Outbound — anchors that ACTUALLY appear in each body, mapped to authoritative URLs.
OUTBOUND_LINKS: dict[str, list[tuple[str, str]]] = {
    "venture capital vietnam": [
        ("Do Ventures", "https://doventures.vc"),
        ("PitchBook", "https://pitchbook.com"),
        ("VNG", "https://vng.com.vn"),
        ("MoMo", "https://www.momo.vn"),
        ("VinaCapital", "https://vinacapital.com"),
        ("Antler", "https://www.antler.co"),
        ("Genesia Ventures", "https://www.genesiaventures.com"),
        ("500 Global", "https://500.co"),
        ("Sky Mavis", "https://skymavis.com"),
        ("Mekong Capital", "https://www.mekongcapital.com"),
    ],
    "vietnam market": [
        ("World Bank", "https://www.worldbank.org/en/country/vietnam"),
        ("IMF", "https://www.imf.org/en/Countries/VNM"),
        ("McKinsey", "https://www.mckinsey.com/featured-insights/asia-pacific/the-new-faces-of-the-vietnamese-consumer"),
        ("Samsung", "https://www.samsung.com"),
        ("Foxconn", "https://www.foxconn.com"),
        ("Shopee", "https://shopee.vn"),
        ("TikTok Shop", "https://shop.tiktok.com"),
        ("MoMo", "https://www.momo.vn"),
        ("VinFast", "https://vinfastauto.com"),
        ("HSBC", "https://www.business.hsbc.com"),
    ],
    "examples for business model canvas": [
        ("Strategyzer", "https://www.strategyzer.com/library/the-business-model-canvas"),
        ("Osterwalder", "https://en.wikipedia.org/wiki/Alex_Osterwalder"),
        ("Ash Maurya", "https://leanstack.com"),
        ("Uber", "https://www.uber.com"),
        ("Spotify", "https://www.spotify.com"),
        ("Netflix", "https://www.netflix.com"),
    ],
    "vibe coding application": [
        ("Karpathy", "https://en.wikipedia.org/wiki/Andrej_Karpathy"),
        ("Wikipedia", "https://en.wikipedia.org/wiki/Vibe_coding"),
        ("Google Cloud", "https://cloud.google.com/discover/what-is-vibe-coding"),
        ("IBM", "https://www.ibm.com/think/topics/vibe-coding"),
        ("Stack Overflow", "https://stackoverflow.blog/2025/01/a-new-worst-coder-has-entered-the-chat"),
        ("Lovable", "https://lovable.dev"),
        ("Cursor", "https://www.cursor.com"),
        ("Claude Code", "https://docs.anthropic.com/en/docs/claude-code"),
    ],
    "lean canvas business model": [
        ("Ash Maurya", "https://leanstack.com/lean-canvas"),
        ("Osterwalder", "https://en.wikipedia.org/wiki/Alex_Osterwalder"),
        ("Eric Ries", "https://theleanstartup.com"),
        ("Strategyzer", "https://www.strategyzer.com"),
    ],
    "value proposition canvas model": [
        ("Strategyzer", "https://www.strategyzer.com/library/the-value-proposition-canvas"),
        ("Osterwalder", "https://en.wikipedia.org/wiki/Alex_Osterwalder"),
        ("Pigneur", "https://en.wikipedia.org/wiki/Yves_Pigneur"),
    ],
    "jobs to be done framework": [
        ("Ulwick", "https://strategyn.com/about-us/our-people/tony-ulwick"),
        ("Strategyn", "https://strategyn.com/jobs-to-be-done"),
        ("Christensen", "https://hbr.org/2016/09/know-your-customers-jobs-to-be-done"),
        ("HBR", "https://hbr.org/2016/09/know-your-customers-jobs-to-be-done"),
        ("Intercom", "https://www.intercom.com/blog/jobs-to-be-done-2"),
    ],
    "vibe coding tools": [
        ("Lovable", "https://lovable.dev"),
        ("Cursor", "https://www.cursor.com"),
        ("Claude Code", "https://docs.anthropic.com/en/docs/claude-code"),
        ("v0", "https://v0.dev"),
        ("Replit", "https://replit.com"),
        ("Bolt", "https://bolt.new"),
        ("Windsurf", "https://codeium.com/windsurf"),
    ],
    "product market fit": [
        ("Marc Andreessen", "https://pmarchive.com/guide_to_startups_part4.html"),
        ("Sean Ellis", "https://review.firstround.com/how-superhuman-built-an-engine-to-find-product-market-fit"),
        ("Y Combinator", "https://www.ycombinator.com/library/5z-the-real-product-market-fit"),
        ("Andreessen", "https://pmarchive.com/guide_to_startups_part4.html"),
    ],
    "blue ocean vs red ocean strategy": [
        ("Kim and Mauborgne", "https://www.blueoceanstrategy.com/authors/kim-mauborgne"),
        ("Mauborgne", "https://www.blueoceanstrategy.com/authors/kim-mauborgne"),
        ("HBR", "https://hbr.org/2004/10/blue-ocean-strategy"),
        ("Cirque du Soleil", "https://www.cirquedusoleil.com"),
        ("INSEAD", "https://www.insead.edu"),
    ],
}

# Cap per article
MAX_INTERNAL = 5
MAX_OUTBOUND = 5


def link_already_present(body: str, anchor_lower: str, url: str) -> bool:
    """Check if an existing markdown link with this anchor or url is already in body."""
    # Existing link with same URL
    if f"]({url})" in body:
        return True
    # Existing link with same anchor text (case-insensitive)
    for m in re.finditer(r"\[([^\]]+)\]\([^)]+\)", body):
        if m.group(1).lower() == anchor_lower:
            return True
    return False


def _forbidden_spans(body: str) -> list[tuple[int, int]]:
    """Return (start, end) spans where anchor injection is not allowed:
    inside existing links, image markdown, or fenced code blocks."""
    spans: list[tuple[int, int]] = []
    # Both links [text](url) and images ![text](url)
    for m in re.finditer(r'!?\[[^\]]*\]\([^)]+\)', body):
        spans.append((m.start(), m.end()))
    for m in re.finditer(r'```.*?```', body, flags=re.DOTALL):
        spans.append((m.start(), m.end()))
    return spans


def safe_replace_first(body: str, anchor: str, url: str) -> tuple[str, bool]:
    """Replace the first occurrence of anchor (word-boundary, case-insensitive)
    with a markdown link. Skips: existing links, image markdown, code blocks,
    heading lines. Returns (new_body, replaced)."""
    if link_already_present(body, anchor.lower(), url):
        return body, False

    forbidden = _forbidden_spans(body)
    pattern = r"\b" + re.escape(anchor) + r"\b"

    for m in re.finditer(pattern, body, flags=re.IGNORECASE):
        start, end = m.start(), m.end()
        # Skip if inside a forbidden span (link, image, code)
        if any(fs <= start < fe for fs, fe in forbidden):
            continue
        # Skip headings (`#` at line start)
        line_start = body.rfind("\n", 0, start) + 1
        line_end = body.find("\n", end)
        if line_end == -1:
            line_end = len(body)
        if body[line_start:line_end].lstrip().startswith("#"):
            continue
        # OK to replace — preserve original casing
        actual_text = body[start:end]
        replacement = f"[{actual_text}]({url})"
        return body[:start] + replacement + body[end:], True
    return body, False


def inject_links_for_article(body: str, primary_keyword: str) -> tuple[str, int, int]:
    """Inject up to MAX_INTERNAL + MAX_OUTBOUND links. Returns (new_body, n_internal, n_outbound)."""
    n_in, n_out = 0, 0
    new_body = body

    # 1. Internal — but skip self-referential (don't link to own slug)
    own_slug_keywords = {
        "blue ocean vs red ocean strategy": "blue-ocean-strategy",  # avoid pointing to existing /blue-ocean-strategy from Phase 1 #10 (pivot article)
    }
    own_target = own_slug_keywords.get(primary_keyword)
    for anchor, slug in INTERNAL_LINKS:
        if n_in >= MAX_INTERNAL:
            break
        if slug == own_target:
            # We're allowed to link to it; pivot is sufficient distinction.
            pass
        url = f"{SITE}/blog/{slug}"
        new_body, replaced = safe_replace_first(new_body, anchor, url)
        if replaced:
            n_in += 1

    # 2. Outbound — keyword-specific
    for anchor, url in OUTBOUND_LINKS.get(primary_keyword, []):
        if n_out >= MAX_OUTBOUND:
            break
        new_body, replaced = safe_replace_first(new_body, anchor, url)
        if replaced:
            n_out += 1

    return new_body, n_in, n_out


def patch(record_id: str, body: str) -> bool:
    for attempt in range(3):
        try:
            r = requests.patch(
                f"{AIRTABLE_API_BASE}/{AIRTABLE_BASE_ID}/{ARTS}/{record_id}",
                headers=HEADERS,
                json={"fields": {"article_body_text": body[:99000]}, "typecast": True},
                timeout=120,
            )
            if r.status_code < 400:
                return True
            print(f"    PATCH HTTP {r.status_code}: {r.text[:300]}")
            return False
        except requests.exceptions.RequestException as e:
            print(f"    attempt {attempt+1}: {e.__class__.__name__}")
            time.sleep(3 * (attempt + 1))
    return False


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    arts = fetch_all(ARTS, fields=["article_id", "primary_keyword", "status", "article_body_text"])
    phase1 = [a for a in arts if a["fields"].get("status") == "review"]
    print(f"Phase 1 (status=review): {len(phase1)} articles\n")

    total_in, total_out = 0, 0
    for art in sorted(phase1, key=lambda x: x["fields"].get("article_id", "")):
        f = art["fields"]
        kw = f.get("primary_keyword", "")
        body = f.get("article_body_text", "") or ""
        new_body, n_in, n_out = inject_links_for_article(body, kw)
        total_in += n_in
        total_out += n_out
        print(f"  {f.get('article_id'):<22} +{n_in} internal, +{n_out} outbound  ({len(new_body)} chars) | {kw[:40]}")
        if args.dry_run:
            continue
        if n_in + n_out == 0:
            continue
        patch(art["id"], new_body)
        time.sleep(0.3)

    print(f"\nTotal injected: {total_in} internal + {total_out} outbound")
    print(f"Avg per article: {total_in/10:.1f} internal, {total_out/10:.1f} outbound")
    return 0


if __name__ == "__main__":
    sys.exit(main())
