"""
Image finder per plan Section 3.5:
  1. Try Unsplash first (free, fast)
  2. Quality check — if generic, fall back to Google CSE Image
  3. Return cover_image_url + alt + credit

Loads UNSPLASH_ACCESS_KEY (required) + GOOGLE_CSE_ID/KEY (optional) from .env.
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path
from typing import Any

import requests

# Auto-load .env from parent
ENV_FILE = Path(__file__).resolve().parent.parent / ".env"
if ENV_FILE.exists():
    for line in ENV_FILE.read_text().splitlines():
        if "=" in line and not line.startswith("#"):
            k, _, v = line.partition("=")
            os.environ.setdefault(k.strip(), v.strip())

UNSPLASH_KEY = os.environ.get("UNSPLASH_ACCESS_KEY", "")
GOOGLE_CSE_ID = os.environ.get("GOOGLE_CSE_ID", "")
GOOGLE_CSE_KEY = os.environ.get("GOOGLE_CSE_KEY", "")


# Known specific entities — if keyword contains these and Unsplash result doesn't,
# trigger Google CSE fallback (likely we need specific brand/product images).
KNOWN_ENTITIES = {
    "vibe coding", "claude code", "lovable", "v0 by vercel", "cursor ai",
    "bolt", "replit", "windsurf",
    "tiki", "vng", "momo", "grab vietnam", "shopee vietnam", "fpt", "vinamilk",
    "vinasun", "topica", "elsa speak",
    "samsung", "foxconn", "apple", "intel", "amkor", "marvell",
    "strategyzer", "andrej karpathy", "ash maurya", "eric ries", "clayton christensen",
    "marc andreessen", "sean ellis", "tony ulwick",
}


# Generic theme keywords — Unsplash should perform well even with generic photos
GENERIC_THEMES = {
    "validation", "framework", "growth", "team", "startup", "business",
    "strategy", "product", "customer", "user", "marketing", "design",
    "meeting", "office", "workspace", "laptop", "data", "analytics",
    "founder", "investor", "venture", "innovation", "research",
}


# ----------------------------- Unsplash -----------------------------

def unsplash_search(query: str, per_page: int = 5) -> list[dict[str, Any]]:
    if not UNSPLASH_KEY:
        return []
    r = requests.get(
        "https://api.unsplash.com/search/photos",
        params={"query": query, "per_page": per_page, "orientation": "landscape"},
        headers={"Authorization": f"Client-ID {UNSPLASH_KEY}"},
        timeout=15,
    )
    if r.status_code != 200:
        return []
    return r.json().get("results", []) or []


def unsplash_format(result: dict[str, Any], query: str) -> dict[str, str]:
    """Return {url, alt, credit} for a Unsplash result."""
    url = result.get("urls", {}).get("regular", "")
    alt = result.get("alt_description") or result.get("description") or query
    photographer = result.get("user", {}).get("name", "Unsplash")
    handle = result.get("user", {}).get("username", "")
    credit = (
        f"Photo by [{photographer}](https://unsplash.com/@{handle}) "
        f"on [Unsplash](https://unsplash.com)"
    )
    return {"url": url, "alt": alt[:200], "credit": credit, "source": "unsplash"}


# ----------------------------- Quality check -----------------------------

def keyword_has_specific_entity(keyword: str) -> tuple[bool, list[str]]:
    """True if keyword contains a specific entity (brand/product/person)."""
    k = keyword.lower()
    matched = [e for e in KNOWN_ENTITIES if e in k]
    return (bool(matched), matched)


def is_generic_theme(keyword: str) -> bool:
    """True if keyword is generic enough that Unsplash will perform well."""
    k = keyword.lower()
    return any(t in k for t in GENERIC_THEMES)


def unsplash_passes_quality(result: dict[str, Any], keyword: str) -> bool:
    """Pass conditions per plan Section 3.5."""
    has_entity, entities = keyword_has_specific_entity(keyword)
    if not has_entity:
        # Generic enough — Unsplash always fine
        return True
    # Has specific entity — check if Unsplash result mentions it
    text = " ".join([
        (result.get("alt_description") or ""),
        (result.get("description") or ""),
        " ".join((result.get("tags") or []) and [t.get("title", "") for t in result.get("tags", [])]),
    ]).lower()
    return any(e.lower() in text for e in entities)


# ----------------------------- Google CSE fallback -----------------------------

def google_cse_image_search(query: str, num: int = 3) -> list[dict[str, Any]]:
    if not GOOGLE_CSE_ID or not GOOGLE_CSE_KEY:
        return []
    r = requests.get(
        "https://www.googleapis.com/customsearch/v1",
        params={
            "key": GOOGLE_CSE_KEY,
            "cx": GOOGLE_CSE_ID,
            "q": query,
            "searchType": "image",
            "num": num,
            "imgSize": "xlarge",
            "rights": "cc_publicdomain,cc_attribute,cc_sharealike",
        },
        timeout=15,
    )
    if r.status_code != 200:
        print(f"  Google CSE error {r.status_code}: {r.text[:200]}")
        return []
    return r.json().get("items", []) or []


def google_cse_format(item: dict[str, Any], query: str) -> dict[str, str]:
    return {
        "url": item.get("link", ""),
        "alt": item.get("title") or query,
        "credit": f"Source: {item.get('displayLink', 'unknown')}",
        "source": "google_cse",
    }


# ----------------------------- Main entry -----------------------------

def find_cover_image(primary_keyword: str) -> dict[str, str]:
    """Per plan Section 3.5 decision tree.

    Returns: {url, alt, credit, source}
    Returns empty dict if no image found.
    """
    print(f"  finding image for: {primary_keyword}")

    # 1. Try Unsplash
    unsplash_results = unsplash_search(primary_keyword)
    if unsplash_results:
        top = unsplash_results[0]
        if unsplash_passes_quality(top, primary_keyword):
            print(f"    → Unsplash hit (quality pass)")
            return unsplash_format(top, primary_keyword)
        print(f"    → Unsplash result too generic, trying Google CSE...")

    # 2. Google CSE fallback
    if GOOGLE_CSE_KEY and GOOGLE_CSE_ID:
        # Smart query enhancement: add hint based on entity type
        has_entity, entities = keyword_has_specific_entity(primary_keyword)
        if has_entity:
            entity = entities[0]
            if entity in {"tiki", "vng", "momo", "grab vietnam", "shopee vietnam",
                          "fpt", "vinamilk", "vinasun", "topica", "elsa speak"}:
                query = f"{primary_keyword} logo"
            elif entity in {"vibe coding", "claude code", "lovable", "v0 by vercel",
                            "cursor ai", "bolt", "replit", "windsurf"}:
                query = f"{primary_keyword} screenshot"
            elif entity in {"andrej karpathy", "ash maurya", "eric ries",
                            "clayton christensen", "marc andreessen", "sean ellis", "tony ulwick"}:
                query = f"{primary_keyword} portrait"
            else:
                query = primary_keyword
        else:
            query = primary_keyword

        cse_results = google_cse_image_search(query)
        if cse_results:
            print(f"    → Google CSE hit")
            return google_cse_format(cse_results[0], primary_keyword)

    # 3. Final fallback — Unsplash result even if generic
    if unsplash_results:
        print(f"    → Falling back to Unsplash (no Google CSE configured)")
        return unsplash_format(unsplash_results[0], primary_keyword)

    print(f"    → NO IMAGE FOUND")
    return {}


# ----------------------------- Smoke test -----------------------------

if __name__ == "__main__":
    test_keywords = [
        "business model canvas",   # generic-ish → Unsplash OK
        "vibe coding",              # specific entity → Unsplash may fail
        "value proposition canvas",
        "claude code tutorial",
        "what is the blue ocean strategy",
    ]
    for kw in test_keywords:
        result = find_cover_image(kw)
        print(f"\n{kw}:")
        for k, v in result.items():
            print(f"  {k}: {str(v)[:80]}")
