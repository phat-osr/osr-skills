"""Shared config for keyword research subsystem."""
from __future__ import annotations

import os
import sys
from pathlib import Path

# Make parent seo-engine importable
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

# Re-export parent config
from config import (  # noqa: E402  (after sys.path append)
    AIRTABLE_API_BASE,
    AIRTABLE_BASE_ID,
    AIRTABLE_META_BASE,
    AIRTABLE_PAT,
    PILLARS,
    SITE_BASE_URL,
)

KR_DIR = Path(__file__).parent
OUTPUT_DIR = KR_DIR / "output"
LOGS_DIR = KR_DIR / "logs"
OUTPUT_DIR.mkdir(exist_ok=True)
LOGS_DIR.mkdir(exist_ok=True)

# ----------------------------- Geo configs -----------------------------
# 7 search markets we care about. global_en is the priority for investor reach.

GEO_CONFIGS: dict[str, dict[str, str]] = {
    "global_en": {"gl": "us", "hl": "en", "country_name": "United States"},
    "vn_en":     {"gl": "vn", "hl": "en", "country_name": "Vietnam (English)"},
    "vn_vi":     {"gl": "vn", "hl": "vi", "country_name": "Vietnam (Vietnamese)"},
    "sg":        {"gl": "sg", "hl": "en", "country_name": "Singapore"},
    "id":        {"gl": "id", "hl": "en", "country_name": "Indonesia"},
    "th":        {"gl": "th", "hl": "en", "country_name": "Thailand"},
    "ph":        {"gl": "ph", "hl": "en", "country_name": "Philippines"},
}

# Throttling
AUTOCOMPLETE_SLEEP_SEC = 0.6           # ~100 req/min, safe
FIRECRAWL_SLEEP_SEC = 1.5              # Firecrawl rate limit on Hobby
TRENDS_SLEEP_SEC = 15                  # Google Trends is very rate-limited
REDDIT_SLEEP_SEC = 1.0
CLAUDE_SLEEP_SEC = 0.3

# Discovery limits
MAX_AUTOCOMPLETE_PER_SEED = 30         # cap to avoid combinatorial blowup
SERP_TOP_N = 10                        # top-10 for difficulty proxy + cluster overlap
PAA_MAX = 8                            # PAA usually surfaces 4-8

# Clustering
SERP_OVERLAP_THRESHOLD = 3             # ≥3 shared URLs in top-10 = same cluster
SEMANTIC_SIM_THRESHOLD = 0.78          # Claude embed cosine
MIN_CLUSTER_SIZE = 3                   # HDBSCAN min

# Secrets (env-only, never commit)
FIRECRAWL_API_KEY = os.environ.get("FIRECRAWL_API_KEY", "")
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
REDDIT_USER_AGENT = os.environ.get("REDDIT_USER_AGENT", "OSR-keyword-research/0.1")

# Modifier suffixes to expand each seed with (Google Autocomplete A-Z trick)
EXPAND_MODIFIERS: list[str] = [
    "",                # bare
    " how to",
    " best",
    " example",
    " explained",
    " vs",
    " for founders",
    " for investors",
    " 2026",
    " in vietnam",
    " in southeast asia",
    " case study",
    " step by step",
    " what is",
    " template",
]

# Question modifiers (drives PAA-friendly keywords)
QUESTION_PREFIXES: list[str] = [
    "what is",
    "how to",
    "how do",
    "why is",
    "where to",
    "when to",
    "is",
    "are",
    "should",
    "can",
    "best",
]
