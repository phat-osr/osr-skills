"""
OS Research article template — JSON-LD generator, section decision rules,
brand-naming rule, body finalizer.

Per plan Section 3 + Section 4.
"""
from __future__ import annotations

import json
import re
from datetime import date
from typing import Any


SITE = "https://www.osresearch.vn"
ORG_NAME = "OS Research"
# Example placeholder author — replace with the real author before publishing.
AUTHOR_NAME = "Author Name"
AUTHOR_LINKEDIN = "https://www.linkedin.com/in/your-handle/"
AUTHOR_JOBTITLE = "Content Lead"
AUTHOR_BIO = "Author at OS Research, a startup validation studio in Vietnam."
ORG_SAMEAS = [
    "https://www.linkedin.com/company/osresearch-vn/",
    "https://www.instagram.com/osresearch.vn/",
]
ORG_ADDRESS = {
    "@type": "PostalAddress",
    "streetAddress": "28 Thảo Điền",
    "addressLocality": "Phường An Khánh",
    "addressRegion": "Thành phố Hồ Chí Minh",
    "addressCountry": "VN",
}

# Map content pattern → articleSection for Schema.org
SECTION_MAP = {
    "framework_example": "Startup Frameworks",
    "how_to_validate": "Founder Playbook",
    "case_study": "Case Studies",
    "sector_ideas": "Vietnam Market",
    "general": "General",
}


# ----------------------------- Section decision rules (Plan Section 3) -----------------------------

SECTION_RULES = {
    "framework_example": {"what_osr_thinks": False, "common_mistakes": True},
    "how_to_validate":   {"what_osr_thinks": False, "common_mistakes": True},
    "case_study":        {"what_osr_thinks": False, "common_mistakes": False},
    "sector_ideas":      {"what_osr_thinks": False, "common_mistakes": False},
    "general":           {"what_osr_thinks": False, "common_mistakes": False},
}


def should_include(section: str, pattern: str) -> bool:
    rules = SECTION_RULES.get(pattern, SECTION_RULES["general"])
    return rules.get(section, False)


# ----------------------------- Brand naming rule (Plan Section 3) -----------------------------

def apply_brand_naming(text: str) -> str:
    """
    In published content, always use 'OS Research' (full form).
    Rule: replace standalone 'OSR' word boundary → 'OS Research', except when:
      - inside a URL or code block
      - already part of 'OS Research'
    """
    # Skip code blocks (```...```)
    parts = re.split(r"(```.*?```)", text, flags=re.DOTALL)
    out = []
    for part in parts:
        if part.startswith("```"):
            out.append(part)
            continue
        # Replace word-boundary OSR → OS Research (but not OS Research itself, not OSR-A-xxx)
        part = re.sub(r"\bOSR\b(?!-A-)", "OS Research", part)
        out.append(part)
    return "".join(out)


def remove_em_dashes(text: str) -> str:
    """Brand voice rule (plan Section 3.4): no em-dashes. Replace with comma/period.

    Logic: skip inside URLs (markdown links/images) and code blocks. For the rest:
      - ` — ` (space–emdash–space): replace with `, ` (most common mid-sentence use)
      - ` –- ` and ` -- `: same
      - Em-dash at end of segment: replace with period
    """
    def replace_outside_links(s: str) -> str:
        # Walk char by char, skip markdown link parens [text](url) and ![alt](url)
        out = []
        i = 0
        while i < len(s):
            # Skip URLs in parentheses after ]
            if s[i] == "(" and i > 0 and s[i-1] == "]":
                close = s.find(")", i)
                if close != -1:
                    out.append(s[i:close+1])
                    i = close + 1
                    continue
            ch = s[i]
            if ch in "—–":
                # space–dash–space → comma–space
                before = out[-1] if out else ""
                after = s[i+1] if i+1 < len(s) else ""
                if before == " " and after == " ":
                    out[-1] = ","  # replace trailing space with comma
                    out.append(" ")  # keep the space after
                    i += 2  # skip dash + following space
                    continue
                # otherwise just strip the dash
                i += 1
                continue
            out.append(ch)
            i += 1
        return "".join(out)

    # Process per non-code-block segment
    parts = re.split(r"(```.*?```)", text, flags=re.DOTALL)
    out = []
    for part in parts:
        if part.startswith("```"):
            out.append(part)
        else:
            out.append(replace_outside_links(part))
    return "".join(out)


# ----------------------------- JSON-LD schema generator -----------------------------

def build_schema_jsonld(
    *,
    primary_keyword: str,
    h1: str,
    meta_description: str,
    tldr: str,
    slug: str,
    cover_image_url: str,
    title_tag: str | None = None,
    published_date: str | None = None,
    date_modified: str | None = None,
    word_count: int = 0,
    faq_pairs: list[dict[str, str]] | None = None,
    pattern: str = "general",
) -> str:
    """Return a full <script type=\"application/ld+json\">...</script> blob."""
    pub = published_date or str(date.today())
    upd = date_modified or str(date.today())
    canonical = f"{SITE}/blog/{slug}"
    display_title = title_tag or h1  # prefer SEO title_tag for headline + breadcrumb

    organization = {
        "@type": "Organization",
        "@id": f"{SITE}/#organization",
        "name": ORG_NAME,
        "url": SITE,
        "description": "Startup validation studio in Vietnam.",
        "address": ORG_ADDRESS,
        "sameAs": ORG_SAMEAS,
    }

    person = {
        "@type": "Person",
        "name": AUTHOR_NAME,
        "description": AUTHOR_BIO,
        "sameAs": [AUTHOR_LINKEDIN],
        "jobTitle": AUTHOR_JOBTITLE,
        "worksFor": {"@id": f"{SITE}/#organization"},
    }

    breadcrumb = {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": f"{SITE}/blog"},
            {"@type": "ListItem", "position": 3, "name": display_title, "item": canonical},
        ],
    }

    article = {
        "@type": "BlogPosting",
        "@id": f"{canonical}/#article",
        "mainEntityOfPage": {"@id": canonical},
        "headline": display_title,
        "description": meta_description,
        "abstract": tldr,
        "image": {"@type": "ImageObject", "url": cover_image_url},
        "datePublished": pub,
        "dateModified": upd,
        "wordCount": word_count,
        "inLanguage": "en",
        "keywords": primary_keyword,
        "articleSection": SECTION_MAP.get(pattern, "General"),
        "speakable": {
            "@type": "SpeakableSpecification",
            "cssSelector": [".tldr", ".faq"],
        },
        "author": person,
        "publisher": organization,
    }

    graph = [organization, person, breadcrumb, article]

    if faq_pairs:
        graph.append({
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": qa["question"],
                    "acceptedAnswer": {"@type": "Answer", "text": qa["answer"]},
                }
                for qa in faq_pairs
            ],
        })

    payload = {"@context": "https://schema.org", "@graph": graph}
    return (
        '<script type="application/ld+json">\n'
        + json.dumps(payload, ensure_ascii=False, indent=2)
        + "\n</script>"
    )


# ----------------------------- Body finalizer -----------------------------

def finalize_body(
    *,
    body_md: str,
    pattern: str,
    primary_keyword: str,
    published_date: str | None = None,
    cover_image_url: str | None = None,
    cover_image_alt: str | None = None,
    cover_image_credit: str | None = None,
    extras: dict[str, str] | None = None,
) -> str:
    """
    Apply final transforms to article body before save:
      1. Brand naming (OSR → OS Research)
      2. Strip "Related reading" / "Sources" footer
      3. Strip optional sections per pattern rules (then re-add from `extras` if provided)
      4. Append "What OS Research thinks" + "Common mistakes" before FAQ (if pattern requires + extras supplied)
      5. Insert cover image after first heading
      6. Replace em-dashes per brand voice
      7. Update published date marker

    `extras`: optional dict with keys 'osr_thinks' and/or 'common_mistakes' (markdown content).
    """
    body = apply_brand_naming(body_md)

    # Strip "Related reading" footer (per Pete: paste-to-Framer doesn't need TBD bullets)
    body = re.sub(r"\n## Related reading.*?(?=\n## |\Z)", "", body, flags=re.DOTALL)
    # Strip any standalone source_citations footer that may have leaked into body
    body = re.sub(r"\n## Sources.*?(?=\n## |\Z)", "", body, flags=re.DOTALL)

    # Strip optional sections based on pattern rules
    if not should_include("what_osr_thinks", pattern):
        # Remove "## What OS Research thinks" section (with body until next ##)
        body = re.sub(
            r"\n## What OS Research thinks.*?(?=\n## |\Z)",
            "",
            body,
            flags=re.DOTALL,
        )
    if not should_include("common_mistakes", pattern):
        body = re.sub(
            r"\n## Common mistakes.*?(?=\n## |\Z)",
            "",
            body,
            flags=re.DOTALL,
        )

    # Append extras (What OS Research thinks + Common mistakes) BEFORE the FAQ section
    # — only if pattern includes them and the body doesn't already contain them.
    if extras:
        insertions: list[str] = []
        if should_include("what_osr_thinks", pattern) and extras.get("osr_thinks"):
            if not re.search(r"^## What OS Research thinks", body, re.MULTILINE):
                insertions.append(
                    "## What OS Research thinks\n\n" + extras["osr_thinks"].strip() + "\n"
                )
        if should_include("common_mistakes", pattern) and extras.get("common_mistakes"):
            if not re.search(r"^## Common mistakes", body, re.MULTILINE):
                insertions.append(
                    "## Common mistakes\n\n" + extras["common_mistakes"].strip() + "\n"
                )
        if insertions:
            extras_block = "\n" + "\n".join(insertions) + "\n"
            # Insert immediately above the FAQ heading; fall back to end of body.
            faq_match = re.search(r"^## (?:Frequently asked questions|FAQ)", body, re.MULTILINE)
            if faq_match:
                idx = faq_match.start()
                body = body[:idx] + extras_block + body[idx:]
            else:
                body = body.rstrip() + "\n" + extras_block

    # Update Published date line if exists
    pub = published_date or str(date.today())
    body = re.sub(
        r"<small>Published.*?</small>",
        f"<small>Published {pub} · by {AUTHOR_NAME}, {ORG_NAME}</small>",
        body,
    )

    # Apply brand voice rule LAST so it cleans em-dashes in newly-inserted extras too
    body = remove_em_dashes(body)

    # Insert cover image after H1 if not already present
    if cover_image_url and cover_image_alt:
        if cover_image_url not in body and "![" not in body[:300]:
            credit_line = f"\n*{cover_image_credit}*" if cover_image_credit else ""
            img_block = f"\n\n![{cover_image_alt}]({cover_image_url}){credit_line}\n"
            # Insert after first H1 or after TLDR block
            if "</aside>" in body:
                body = body.replace("</aside>", "</aside>" + img_block, 1)
            else:
                # after first H1
                body = re.sub(r"(\n# .+?\n)", r"\1" + img_block, body, count=1)

    return body


# ----------------------------- Title / meta helpers -----------------------------

def slugify(s: str) -> str:
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:80]


def truncate(s: str, max_len: int) -> str:
    if len(s) <= max_len:
        return s
    return s[:max_len - 3].rstrip() + "..."


# ----------------------------- Smoke test -----------------------------

if __name__ == "__main__":
    # Test brand naming
    sample = "OSR builds 20 companies. OSR-A-0001 is the first. OSR thinks differently."
    print("Brand naming test:")
    print(f"  IN:  {sample}")
    print(f"  OUT: {apply_brand_naming(sample)}")
    print()

    # Test schema generator
    schema = build_schema_jsonld(
        primary_keyword="business model canvas",
        h1="Business Model Canvas",
        meta_description="A one-page strategic template by Osterwalder and Pigneur.",
        tldr="Quick definition + 9 blocks summary.",
        slug="business-model-canvas",
        cover_image_url="https://images.unsplash.com/photo-123",
        word_count=1100,
        faq_pairs=[
            {"question": "What is the Business Model Canvas?", "answer": "A 9-block strategic template."},
        ],
        pattern="framework_example",
    )
    print(f"Schema JSON-LD length: {len(schema)} chars")
    print(f"First 200 chars: {schema[:200]}...")
