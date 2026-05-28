"""
Audit Phase 1 (10 articles) against plan criteria.

Checks per article:
  Field completeness  — all 20 fields present
  Title              — ≤60 chars, primary KW in first half
  Meta description   — 130-180 chars
  Slug               — ≤80 chars, kebab-case
  Body word count    — plan target 1500-2500 (Phase 1 lean: 1000+)
  Body structure     — TL;DR + image + ≥4 H2 + FAQ
  TL;DR format       — **TL;DR.** plain bold, no <aside>, no `>` prefix
  Image              — embedded in body + caption + cover_image_url field
  Internal links     — ≥1 osresearch.vn link (target 3-5)
  Outbound links     — ≥2 external authoritative (target 2-5)
  FAQ section        — present + Q&A count
  Schema JSON-LD     — Article + FAQPage + Breadcrumb + Org + Person
  Section rules      — pattern-correct "What OS Research thinks" / "Common mistakes"
  Brand naming       — no standalone "OSR" (except IDs)
  Em-dash check      — no em-dashes (per brand voice)
  PAA field          — populated
  Cluster field      — populated
  SERP insights      — attachment present

Run:
    python audit_batch.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

from airtable_helpers import fetch_all

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from table_ids import TABLE_IDS  # noqa: E402

from osr_template import should_include  # noqa: E402

ARTS = TABLE_IDS["Articles"]
REQUIRED_FIELDS = [
    "article_id", "batch_id", "primary_keyword", "search_volume", "keyword_difficulty",
    "signal_score", "pattern", "status", "title_tag", "meta_description", "slug",
    "cover_image_url", "cover_image_alt", "cover_image_credit", "schema_jsonld",
    "article_body_text", "keyword_cluster", "people_also_ask", "serp_insights_json",
    "framer_url",  # final_url consolidated into framer_url
]
PASS = "✓"
FAIL = "✗"
WARN = "⚠"


def check(label: str, condition: bool, detail: str = "") -> tuple[str, str]:
    return (PASS if condition else FAIL, f"{label}{(': ' + detail) if detail else ''}")


def warn(label: str, condition: bool, detail: str = "") -> tuple[str, str]:
    return (PASS if condition else WARN, f"{label}{(': ' + detail) if detail else ''}")


def audit_article(art: dict) -> list[tuple[str, str]]:
    f = art["fields"]
    body = f.get("article_body_text", "") or ""
    pattern = f.get("pattern", "general")
    primary_kw = f.get("primary_keyword", "").lower()
    results: list[tuple[str, str]] = []

    # 1. Field completeness — must have all 20 fields (KD=0 is valid)
    missing = [k for k in REQUIRED_FIELDS if k not in f and k != "keyword_difficulty"]
    # keyword_difficulty=0 is legit
    results.append(check(f"fields complete ({len(REQUIRED_FIELDS)})",
                          not missing, ", ".join(missing) if missing else ""))

    # 2. Title ≤60 chars
    title = f.get("title_tag", "")
    results.append(check(f"title ≤60 chars", len(title) <= 60, f"{len(title)} chars"))
    # Primary KW in first half of title
    half = title[:len(title)//2 + 5].lower()
    results.append(warn(f"primary KW in first half of title",
                        any(tok in half for tok in primary_kw.split() if len(tok) > 3)))

    # 3. Meta description 130-180
    meta = f.get("meta_description", "")
    ok = 130 <= len(meta) <= 180
    results.append(warn(f"meta description 130-180", ok, f"{len(meta)} chars"))

    # 4. Slug ≤80 + kebab
    slug = f.get("slug", "")
    ok = len(slug) <= 80 and re.fullmatch(r"[a-z0-9-]+", slug) is not None
    results.append(check(f"slug valid + ≤80", ok, slug))

    # 5. Body word count — plan target 1500-2500
    wc = len(body.split())
    ok = wc >= 1000  # Phase 1 lean baseline
    results.append(warn(f"body words ≥1500 (plan target)", wc >= 1500, f"{wc} words"))

    # 6. TL;DR format — `**TL;DR.**` bold paragraph, no <aside>, no `> TL;DR`
    has_tldr = bool(re.search(r"\*\*TL;DR\.?\*\*", body))
    no_jsx = "<aside" not in body and "</aside>" not in body
    no_blockquote = not re.search(r"^>\s*\*\*TL;DR", body, re.MULTILINE)
    results.append(check("TL;DR plain bold (no JSX, no `>`)",
                          has_tldr and no_jsx and no_blockquote))

    # 7. Image embedded + caption + alt
    has_img = bool(re.search(r"!\[[^\]]+\]\(https?://[^)]+\)", body))
    has_caption = bool(re.search(r"\*Photo by[^*\n]+\*", body))
    results.append(check("image embedded in body", has_img))
    results.append(check("image caption (Unsplash attribution)", has_caption))

    # 8. H2 hierarchy + FAQ section
    h2s = re.findall(r"^## (.+)$", body, re.MULTILINE)
    has_faq = any("frequently asked" in h.lower() or "faq" in h.lower() for h in h2s)
    results.append(check(f"≥4 H2 sections", len(h2s) >= 4, f"{len(h2s)} H2"))
    results.append(check("FAQ section present", has_faq))
    # FAQ Q&A count — match **Q: ... **
    q_count = len(re.findall(r"\*\*Q:.*?\*\*", body))
    results.append(warn(f"FAQ 7-10 Q&A (plan target)", 7 <= q_count <= 10, f"{q_count} Q"))

    # 9. Inbound/outbound links (exclude image markdown)
    body_no_img = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", body)
    links = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", body_no_img)
    inbound = [u for t, u in links if "osresearch.vn" in u]
    outbound = [u for t, u in links if u.startswith("http") and "osresearch.vn" not in u]
    results.append(warn(f"internal links 3-5 (plan target)",
                        3 <= len(inbound) <= 5, f"{len(inbound)} inbound"))
    results.append(warn(f"outbound links 2-5 (plan target)",
                        2 <= len(outbound) <= 5, f"{len(outbound)} outbound"))

    # 10. Schema JSON-LD — Article + FAQPage + Breadcrumb + Org + Person
    schema = f.get("schema_jsonld", "")
    for stype in ["Article", "FAQPage", "BreadcrumbList", "Organization", "Person"]:
        results.append(check(f"schema has {stype}", f'"@type": "{stype}"' in schema))

    # 11. Section decision rules per pattern
    has_osr_thinks = bool(re.search(r"^## What OS Research thinks", body, re.MULTILINE))
    has_mistakes = bool(re.search(r"^## Common mistakes", body, re.MULTILINE))
    want_mistakes = should_include("common_mistakes", pattern)
    # "What OS Research thinks" section is removed across the board — no pattern should have it.
    results.append(check("section: 'What OS Research thinks' removed",
                          not has_osr_thinks,
                          "still present — should be removed" if has_osr_thinks else ""))
    if want_mistakes:
        results.append(check(f"section: Common mistakes ({pattern} should include)", has_mistakes))
    else:
        results.append(check(f"section: Common mistakes ({pattern} should skip)", not has_mistakes))

    # 12. Brand naming — no standalone OSR except in OSR-A-/OSR-2026-* IDs
    osr_in_body = re.findall(r"\bOSR\b(?!-[A-Z0-9])", body)
    results.append(check("brand: no standalone 'OSR' in body",
                          len(osr_in_body) == 0,
                          f"found {len(osr_in_body)}" if osr_in_body else ""))

    # 13. Brand voice — no em-dashes
    em_dashes = body.count("—")
    results.append(warn(f"no em-dashes (brand voice)", em_dashes == 0,
                        f"{em_dashes} em-dashes"))

    # 13b. Brand voice — no passive third-person "OS Research [verb]" (prefer we/our)
    osr_passive = re.findall(
        r"\bOS Research (uses|builds|treats|thinks|recommends|believes|sees|saw|ran|runs|"
        r"views|wrote|writes|published|tested|tests|worked|works|rebuilt|shipped|added|redesigned)\b",
        body,
    )
    results.append(check("brand voice: no 'OS Research [verb]' (use we/our)",
                          len(osr_passive) == 0,
                          f"{len(osr_passive)} passive uses: {set(osr_passive)}" if osr_passive else ""))

    # 13c. Brand voice — no buzzwords
    buzz = re.findall(r"\b(game-changing|disruptive|synergy|innovative)\b", body, re.I)
    results.append(check("brand voice: no buzzwords",
                          len(buzz) == 0,
                          f"{len(buzz)} buzzwords: {set(b.lower() for b in buzz)}" if buzz else ""))

    # 13d. No fabricated portfolio/client claims (per content quality rule)
    fab = re.findall(
        r"\bour portfolio compan|\bwe worked with (?:a|an|the) [a-z]+ founder\b",
        body, re.I,
    )
    results.append(check("content: no fabricated OS Research portfolio claims",
                          len(fab) == 0,
                          f"{len(fab)} fabricated claims" if fab else ""))

    # 13e. No corrupted nested links (URL with `[` inside, or [..[..](..)..](..) shape)
    url_with_bracket = bool(re.search(r"\(https?://[^)]*\[", body))
    nested_link = bool(re.search(r"\[[^\[\]]*\[[^\]]+\]\([^)]+\)[^\[\]]*\]\([^)]+\)", body))
    results.append(check("markdown: no corrupted nested links",
                          not (url_with_bracket or nested_link),
                          "URL contains `[` or nested `[..](..)` link" if (url_with_bracket or nested_link) else ""))

    # 14. People Also Ask populated
    paa = f.get("people_also_ask", "")
    results.append(check("people_also_ask populated", bool(paa.strip())))

    # 15. Cluster populated
    cluster = f.get("keyword_cluster", "")
    results.append(check("keyword_cluster populated", bool(cluster.strip())))

    # 16. SERP insights attachment
    serp = f.get("serp_insights_json", [])
    results.append(check("serp_insights_json attachment", bool(serp)))

    # 17. Cover image url + alt + credit
    results.append(check("cover_image_url filled", bool(f.get("cover_image_url"))))
    results.append(check("cover_image_alt filled", bool(f.get("cover_image_alt"))))
    results.append(check("cover_image_credit filled", bool(f.get("cover_image_credit"))))

    # 18. Framer url (final_url consolidated into framer_url)
    results.append(check("framer_url filled", bool(f.get("framer_url"))))

    return results


def main() -> int:
    arts = fetch_all(ARTS)
    phase1 = sorted(
        [a for a in arts if a["fields"].get("article_id", "").startswith("OSR-2026-05-21-")],
        key=lambda x: x["fields"]["article_id"],
    )
    print(f"=== Audit {len(phase1)} Phase 1 articles ===\n")

    total_pass, total_fail, total_warn = 0, 0, 0
    per_article_summary = []

    for art in phase1:
        f = art["fields"]
        aid = f.get("article_id", "")
        kw = f.get("primary_keyword", "")
        print(f"┌─ {aid}: {kw}")
        results = audit_article(art)
        n_pass = sum(1 for s, _ in results if s == PASS)
        n_fail = sum(1 for s, _ in results if s == FAIL)
        n_warn = sum(1 for s, _ in results if s == WARN)
        total_pass += n_pass
        total_fail += n_fail
        total_warn += n_warn
        per_article_summary.append((aid, kw, n_pass, n_fail, n_warn, len(results)))
        for status, msg in results:
            print(f"│ {status}  {msg}")
        print(f"└─ {n_pass}✓  {n_fail}✗  {n_warn}⚠  (out of {len(results)})\n")

    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"  {'article_id':<22} {'pass':>5}  {'fail':>5}  {'warn':>5}  {'total':>6}  keyword")
    for aid, kw, p, f_, w, t in per_article_summary:
        print(f"  {aid:<22} {p:>5}  {f_:>5}  {w:>5}  {t:>6}  {kw[:38]}")
    print()
    print(f"  TOTAL: {total_pass} pass, {total_fail} fail, {total_warn} warn (out of {total_pass+total_fail+total_warn})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
