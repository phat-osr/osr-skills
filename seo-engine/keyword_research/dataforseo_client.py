"""
DataForSEO v3 API client wrapper.

Endpoints used:
  - /v3/dataforseo_labs/google/keyword_suggestions/live  ($0.01 / call, returns ≤680 KWs with volume+KD)
  - /v3/dataforseo_labs/google/related_keywords/live     ($0.01 / call, returns ≤4680 KWs, semantic)
  - /v3/keywords_data/google_ads/search_volume/live      ($0.05 / 1000 KWs, just volume+CPC+competition)
  - /v3/dataforseo_labs/google/bulk_keyword_difficulty/live ($0.05 / 1000 KWs, just KD)
  - /v3/serp/google/organic/live/advanced                ($0.0006 / SERP, top 100 + features)
  - /v3/appendix/user_data                               (free balance check)

Loads DFS_LOGIN + DFS_PASSWORD from env or seo-engine/.env file.

Docs: https://docs.dataforseo.com/v3/
"""
from __future__ import annotations

import base64
import os
from pathlib import Path
from typing import Any

import requests

# Auto-load .env from parent seo-engine
ENV_FILE = Path(__file__).resolve().parent.parent / ".env"
if ENV_FILE.exists():
    for line in ENV_FILE.read_text().splitlines():
        if "=" in line and not line.startswith("#"):
            k, _, v = line.partition("=")
            os.environ.setdefault(k.strip(), v.strip())

DFS_LOGIN = os.environ.get("DFS_LOGIN", "")
DFS_PASSWORD = os.environ.get("DFS_PASSWORD", "")
BASE = "https://api.dataforseo.com"

# Location codes (DataForSEO standard)
LOCATIONS = {
    "global_en": 2840,   # United States (proxy for global English)
    "vn":        2704,   # Vietnam
    "sg":        2702,   # Singapore
    "id":        2360,   # Indonesia
    "th":        2764,   # Thailand
    "ph":        2608,   # Philippines
    "uk":        2826,   # United Kingdom
}

LANG_CODES = {"en": "en", "vi": "vi"}


def _auth() -> dict[str, str]:
    if not DFS_LOGIN or not DFS_PASSWORD:
        raise RuntimeError("Set DFS_LOGIN + DFS_PASSWORD in env or .env file")
    token = base64.b64encode(f"{DFS_LOGIN}:{DFS_PASSWORD}".encode()).decode()
    return {"Authorization": f"Basic {token}", "Content-Type": "application/json"}


# ----------------------------- Core API call -----------------------------

def _post(path: str, payload: list[dict[str, Any]], timeout: int = 60) -> dict[str, Any]:
    r = requests.post(f"{BASE}{path}", headers=_auth(), json=payload, timeout=timeout)
    if r.status_code >= 400:
        return {"_http_error": r.status_code, "_body": r.text[:500]}
    try:
        return r.json()
    except Exception:
        return {"_error": "invalid json", "_body": r.text[:500]}


def _get(path: str, timeout: int = 30) -> dict[str, Any]:
    r = requests.get(f"{BASE}{path}", headers=_auth(), timeout=timeout)
    return r.json() if r.status_code < 400 else {"_http_error": r.status_code, "_body": r.text[:500]}


# ----------------------------- High-level helpers -----------------------------

def get_balance() -> float:
    """Return current account balance in USD."""
    data = _get("/v3/appendix/user_data")
    try:
        return float(data["tasks"][0]["result"][0]["money"]["balance"])
    except Exception:
        return 0.0


def keyword_suggestions(
    seed: str,
    *,
    location: str = "global_en",
    language: str = "en",
    limit: int = 200,
    min_volume: int = 30,
    include_seed_in_response: bool = True,
) -> list[dict[str, Any]]:
    """Returns up to `limit` long-tail variants of `seed` with volume + KD + CPC.

    Cost: $0.01 per call regardless of limit (up to 680).
    """
    payload = [{
        "keyword": seed,
        "location_code": LOCATIONS[location],
        "language_code": LANG_CODES[language],
        "include_seed_keyword": include_seed_in_response,
        "include_serp_info": False,
        "limit": min(limit, 680),
        "filters": [
            ["keyword_info.search_volume", ">=", min_volume],
        ],
        "order_by": ["keyword_info.search_volume,desc"],
    }]
    data = _post("/v3/dataforseo_labs/google/keyword_suggestions/live", payload)
    if "_http_error" in data:
        print(f"  HTTP {data['_http_error']}: {data.get('_body','')[:200]}")
        return []
    try:
        items = data["tasks"][0]["result"][0]["items"] or []
    except Exception:
        return []
    return [_extract_kw_item(x) for x in items]


def related_keywords(
    seed: str,
    *,
    location: str = "global_en",
    language: str = "en",
    depth: int = 2,
    limit: int = 300,
) -> list[dict[str, Any]]:
    """Semantic related keywords (broader than suggestions).

    depth=1 returns ~100, depth=2 returns ~700, depth=3 returns ~4680.
    Cost: $0.01 per call regardless of depth.
    """
    payload = [{
        "keyword": seed,
        "location_code": LOCATIONS[location],
        "language_code": LANG_CODES[language],
        "depth": depth,
        "limit": min(limit, 4680),
        "include_seed_keyword": True,
    }]
    data = _post("/v3/dataforseo_labs/google/related_keywords/live", payload)
    if "_http_error" in data:
        print(f"  HTTP {data['_http_error']}: {data.get('_body','')[:200]}")
        return []
    try:
        items = data["tasks"][0]["result"][0]["items"] or []
    except Exception:
        return []
    out = []
    for x in items:
        # Related keywords endpoint nests under keyword_data
        kd = x.get("keyword_data") or x
        out.append(_extract_kw_item(kd))
    return out


def bulk_search_volume(
    keywords: list[str],
    *,
    location: str = "global_en",
    language: str = "en",
) -> dict[str, dict[str, Any]]:
    """Pull volume + CPC + competition for many keywords at once.

    Cost: $0.05 per 1000 keywords. Up to 1000 per call.
    """
    out: dict[str, dict[str, Any]] = {}
    for i in range(0, len(keywords), 1000):
        chunk = keywords[i:i + 1000]
        payload = [{
            "keywords": chunk,
            "location_code": LOCATIONS[location],
            "language_code": LANG_CODES[language],
        }]
        data = _post("/v3/keywords_data/google_ads/search_volume/live", payload)
        if "_http_error" in data:
            print(f"  HTTP {data['_http_error']}: {data.get('_body','')[:200]}")
            continue
        try:
            items = data["tasks"][0]["result"] or []
        except Exception:
            continue
        for item in items:
            kw = (item.get("keyword") or "").lower()
            if not kw:
                continue
            out[kw] = {
                "search_volume": item.get("search_volume") or 0,
                "cpc": item.get("cpc") or 0,
                "competition": item.get("competition") or "",
                "competition_index": item.get("competition_index") or 0,
                "monthly_searches": item.get("monthly_searches") or [],
            }
    return out


def bulk_keyword_difficulty(
    keywords: list[str],
    *,
    location: str = "global_en",
    language: str = "en",
) -> dict[str, int]:
    """KD 0-100 for up to 1000 keywords per call.

    Cost: $0.05 per 1000 keywords.
    """
    out: dict[str, int] = {}
    for i in range(0, len(keywords), 1000):
        chunk = keywords[i:i + 1000]
        payload = [{
            "keywords": chunk,
            "location_code": LOCATIONS[location],
            "language_code": LANG_CODES[language],
        }]
        data = _post(
            "/v3/dataforseo_labs/google/bulk_keyword_difficulty/live", payload
        )
        if "_http_error" in data:
            print(f"  HTTP {data['_http_error']}: {data.get('_body','')[:200]}")
            continue
        try:
            items = data["tasks"][0]["result"][0]["items"] or []
        except Exception:
            continue
        for item in items:
            kw = (item.get("keyword") or "").lower()
            kd = item.get("keyword_difficulty")
            if kw and kd is not None:
                out[kw] = int(kd)
    return out


def serp_top10(
    keyword: str,
    *,
    location: str = "global_en",
    language: str = "en",
) -> dict[str, Any]:
    """Live SERP top organic + PAA + AI Overview detection.

    Cost: $0.002 per task (advanced endpoint).
    """
    payload = [{
        "keyword": keyword,
        "location_code": LOCATIONS[location],
        "language_code": LANG_CODES[language],
        "depth": 10,
    }]
    data = _post("/v3/serp/google/organic/live/advanced", payload)
    if "_http_error" in data:
        return {"top": [], "paa": [], "ai_overview": False, "_error": data.get("_body", "")}
    try:
        items = data["tasks"][0]["result"][0]["items"] or []
    except Exception:
        return {"top": [], "paa": [], "ai_overview": False}

    top: list[dict[str, Any]] = []
    paa: list[str] = []
    ai_overview = False
    for it in items:
        t = it.get("type")
        if t == "organic" and len(top) < 10:
            top.append({
                "rank": it.get("rank_absolute"),
                "url": it.get("url"),
                "title": it.get("title", "")[:200],
                "domain": it.get("domain", ""),
                "description": (it.get("description") or "")[:300],
            })
        elif t == "people_also_ask":
            for q in (it.get("items") or [])[:8]:
                qt = q.get("title", "").strip()
                if qt:
                    paa.append(qt)
        elif t in ("ai_overview", "generative_ai"):
            ai_overview = True
    return {"top": top, "paa": paa, "ai_overview": ai_overview}


# ----------------------------- Internal -----------------------------

def _extract_kw_item(x: dict[str, Any]) -> dict[str, Any]:
    """Normalize a DataForSEO Labs keyword item into a flat dict."""
    info = x.get("keyword_info") or {}
    props = x.get("keyword_properties") or {}
    serp_info = x.get("serp_info") or {}
    return {
        "keyword": (x.get("keyword") or "").lower(),
        "search_volume": info.get("search_volume") or 0,
        "cpc": info.get("cpc") or 0,
        "competition": info.get("competition") or "",
        "competition_index": info.get("competition_index") or 0,
        "keyword_difficulty": props.get("keyword_difficulty") or 0,
        "search_intent": props.get("core_keyword") or "",
        "monthly_searches": info.get("monthly_searches") or [],
        "serp_features": [s.get("type") for s in (serp_info.get("se_results") or [])][:10],
    }


if __name__ == "__main__":
    # Smoke test — uses ~$0.01 of credit
    print(f"Balance: ${get_balance():.4f}")
    print("\nSuggestions for 'startup vietnam' (global_en, top 10 by volume):")
    results = keyword_suggestions("startup vietnam", limit=10, min_volume=10)
    for r in results[:10]:
        print(f"  vol={r['search_volume']:>5} kd={r['keyword_difficulty']:>3} cpc=${r['cpc']:.2f}  {r['keyword']}")
    print(f"\nBalance after: ${get_balance():.4f}")
