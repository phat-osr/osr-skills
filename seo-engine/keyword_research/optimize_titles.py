"""
Optimize title_tag to match SERP-winning patterns per keyword type.

Patterns observed in real top-10 SERP (2026-05):
  - "what is X"          → "What Is X? Definition + Examples (2026)"
  - "X examples"         → "X Examples: 15 Real Companies (2026)"
  - "best X" / "X tools" → "Best X 2026: Top 10 Compared"
  - "X framework/model"  → "X: Complete Guide + Examples (2026)"
  - "X vietnam" / "vietnam X" → "X in Vietnam: 2026 Market Report"
  - "product market fit" / similar canon → "X: How to Measure It (2026 Guide)"
  - default              → "X: Complete Guide (2026)"

Title cap: 60 chars (Google's SERP cutoff). "| OS Research" suffix dropped —
Framer / Google auto-appends site name from canonical.

Run:
    python optimize_titles.py --dry-run
    python optimize_titles.py
"""
from __future__ import annotations

import argparse
import re
import sys
import time
from pathlib import Path
from typing import Any

import requests

from airtable_helpers import fetch_all
from config_kw import AIRTABLE_API_BASE, AIRTABLE_BASE_ID, AIRTABLE_PAT

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from table_ids import TABLE_IDS  # noqa: E402

HEADERS = {"Authorization": f"Bearer {AIRTABLE_PAT}", "Content-Type": "application/json"}
ARTICLES_TID = TABLE_IDS["Articles"]

YEAR = "2026"
CAP = 60  # Google SERP title cutoff


def title_case(s: str) -> str:
    small = {"a","an","and","as","at","but","by","for","if","in","of",
             "on","or","the","to","vs","with","is"}
    words = s.split()
    cap = []
    for i, w in enumerate(words):
        if i == 0 or w not in small:
            # Preserve all-caps initialisms (BMC, VPC, JTBD, ERRC, MVP, PMF, FDI, AI, VC, SEO)
            if w.upper() in {"BMC", "VPC", "JTBD", "ERRC", "MVP", "PMF", "FDI", "AI", "VC", "SEO", "GDP", "TRR"}:
                cap.append(w.upper())
            else:
                cap.append(w.capitalize())
        else:
            cap.append(w)
    return " ".join(cap)


def cap_at(s: str, max_len: int) -> str:
    if len(s) <= max_len:
        return s
    # Cut at word boundary
    cut = s[:max_len].rstrip()
    if " " in cut:
        cut = cut.rsplit(" ", 1)[0]
    return cut


def optimize_title(primary_keyword: str, pattern: str) -> str:
    """Return a SERP-optimized title for the keyword."""
    k = primary_keyword.lower().strip()
    kt = title_case(k)

    # 1. Question form (what is / how to)
    if k.startswith("what is "):
        topic = k[len("what is "):].strip()
        # Remove leading "the" if present
        if topic.startswith("the "):
            topic = topic[4:]
        topic_t = title_case(topic)
        # "What Is X? Definition + Examples (2026)"
        candidates = [
            f"What Is {topic_t}? Definition + Examples ({YEAR})",
            f"What Is {topic_t}? A {YEAR} Guide with Examples",
            f"What Is {topic_t}? Complete Guide ({YEAR})",
        ]
        for c in candidates:
            if len(c) <= CAP:
                return c
        return cap_at(f"What Is {topic_t}? Guide ({YEAR})", CAP)

    # 2. Examples form ("X examples" / "examples of X" / "examples for X")
    examples_match = re.search(r"\bexamples?\b", k)
    if examples_match:
        # Strip the "examples" qualifier, get core topic
        topic = re.sub(r"\b(examples?\s+(of|for|in)?|of\s+a?\s*|for\s+a?\s*)\b", " ", k)
        topic = re.sub(r"\s+", " ", topic).strip()
        topic_t = title_case(topic)
        candidates = [
            f"{topic_t} Examples: 15 Real Companies ({YEAR})",
            f"{topic_t} Examples (Real Cases + Templates)",
            f"15 {topic_t} Examples to Learn From ({YEAR})",
        ]
        for c in candidates:
            if len(c) <= CAP:
                return c
        return cap_at(f"{topic_t} Examples ({YEAR})", CAP)

    # 3. Tools / best X
    if "tools" in k or k.startswith("best "):
        topic = re.sub(r"^best\s+", "", k)
        topic_t = title_case(topic)
        candidates = [
            f"Best {topic_t} {YEAR}: Top 10 Compared",
            f"10 Best {topic_t} for {YEAR} (Compared)",
            f"Best {topic_t} in {YEAR}: Honest Comparison",
        ]
        for c in candidates:
            if len(c) <= CAP:
                return c
        return cap_at(f"Best {topic_t} ({YEAR})", CAP)

    # 4. Vietnam-related (vn_vc)
    if "vietnam" in k or " vn" in k:
        # Move "vietnam" suffix → "in Vietnam" form
        topic = k.replace("vietnam", "").strip()
        topic_t = title_case(topic) if topic else "Market"
        candidates = [
            f"{topic_t} in Vietnam: {YEAR} Market Report",
            f"{topic_t} in Vietnam ({YEAR}): Funds, Deals, Outlook",
            f"Vietnam {topic_t}: {YEAR} Guide for Founders",
            f"Vietnam {topic_t} {YEAR}: Complete Market Guide",
        ]
        # Fall back to keyword + market-report framing
        if not topic_t.strip() or topic_t.lower() == "market":
            candidates = [
                f"The Vietnam Market: {YEAR} Outlook & Key Sectors",
                f"Vietnam Market {YEAR}: Size, Growth & Sectors",
                f"Vietnam Market Guide ({YEAR}): Sectors & Outlook",
            ]
        for c in candidates:
            if len(c) <= CAP:
                return c
        return cap_at(candidates[0], CAP)

    # 5. Canonical concept keywords (BMC, VPC, lean canvas, JTBD, blue ocean, PMF)
    canonical_specials = {
        "product market fit": f"Product-Market Fit: How to Measure It ({YEAR})",
        "product-market fit": f"Product-Market Fit: How to Measure It ({YEAR})",
        "value proposition canvas": f"Value Proposition Canvas: 6 Blocks + Examples",
        "business model canvas": f"Business Model Canvas: 9 Blocks + Examples",
        "lean canvas": f"The Lean Canvas: Complete Guide + Template ({YEAR})",
        "blue ocean strategy": f"Blue Ocean Strategy: Framework, Examples, ERRC",
    }
    for canon, t in canonical_specials.items():
        if canon in k and len(t) <= CAP:
            return t

    # 6. Framework / model / canvas
    if "framework" in k or "model" in k or "canvas" in k or "strategy" in k:
        candidates = [
            f"{kt}: Complete Guide + Examples ({YEAR})",
            f"{kt}: Framework Explained ({YEAR})",
            f"{kt} Explained: Guide + Examples",
        ]
        for c in candidates:
            if len(c) <= CAP:
                return c
        return cap_at(f"{kt} ({YEAR})", CAP)

    # 7. Default
    candidates = [
        f"{kt}: Complete Guide ({YEAR})",
        f"{kt} Explained ({YEAR})",
        f"{kt}: A {YEAR} Guide",
    ]
    for c in candidates:
        if len(c) <= CAP:
            return c
    return cap_at(f"{kt} ({YEAR})", CAP)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    arts = fetch_all(ARTICLES_TID, fields=["article_id", "primary_keyword", "pattern", "title_tag"])
    print(f"Articles: {len(arts)}\n")

    print(f"  {'article_id':<22} {'old length / new length':<22} new_title")
    print(f"  {'-'*22} {'-'*22} {'-'*60}")
    plans = []
    for r in sorted(arts, key=lambda x: x["fields"].get("article_id","")):
        f = r["fields"]
        kw = f.get("primary_keyword", "")
        pat = f.get("pattern", "general")
        old = f.get("title_tag", "")
        new = optimize_title(kw, pat)
        plans.append((r["id"], f["article_id"], kw, old, new))
        print(f"  {f['article_id']:<22} {len(old):>3} → {len(new):<3} ({len(new):>2}/60)  {new}")

    if args.dry_run:
        print("\n[dry-run]")
        return 0

    print("\n=== PATCH titles ===")
    for rid, aid, kw, old, new in plans:
        if old == new:
            print(f"  {aid}: no change")
            continue
        r = requests.patch(
            f"{AIRTABLE_API_BASE}/{AIRTABLE_BASE_ID}/{ARTICLES_TID}/{rid}",
            headers=HEADERS,
            json={"fields": {"title_tag": new}, "typecast": True},
            timeout=60,
        )
        ok = "✓" if r.status_code < 400 else "✗"
        print(f"  {ok} {aid}: HTTP {r.status_code}")
        if r.status_code >= 400:
            print(f"      {r.text[:200]}")
        time.sleep(0.25)
    print("\nDone.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
