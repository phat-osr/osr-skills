"""
Build serp_insights_json attachment for Phase 2 bài 1 and PATCH Airtable.

Uses catbox.moe (free public file host) to host the JSON, then attaches via URL.
"""
from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path

import requests

from config_kw import AIRTABLE_API_BASE, AIRTABLE_BASE_ID, AIRTABLE_PAT

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from table_ids import TABLE_IDS  # noqa: E402

H = {"Authorization": f"Bearer {AIRTABLE_PAT}", "Content-Type": "application/json"}
ARTICLES_TID = TABLE_IDS["Articles"]

ARTICLE_ID = "OSR-2026-05-22-001"

PAYLOAD = {
    "primary_keyword": "validated learning lean startup",
    "fetched_at": str(date.today()),
    "method": "WebSearch + WebFetch (Claude built-in) — 3 canonical sources read in full",
    "top_5_sources": [
        "Eric Ries — startuplessonslearned.com (Validated learning about customers, 2009)",
        "The Lean Startup — theleanstartup.com/principles (canonical methodology)",
        "Wikipedia — Validated learning (definition + history)",
        "Boldare — Validated Learning examples (4-step framework + POLCO case)",
        "Shortform — Validated Learning: What Is It? (Lean Startup)",
    ],
    "competitor_format_notes": (
        "SERP archetype: definitional posts repeating Ries's 'unit of progress' framing + "
        "Build-Measure-Learn loop. Ries's original (2009) uses IMVU + two anonymous case studies "
        "($1M unsustainable vs $30K scalable). leanstartup.com/principles gives no examples at all. "
        "Boldare provides POLCO case + a 4-step framework (hypothesize → metric → experiment → "
        "iterate) but no falsifiability rules. None of the 3 sources walks through an experiment "
        "with explicit pass/fail thresholds."
    ),
    "identified_gap": (
        "Across all 3 canonical sources: (1) no pre-stated hypothesis requirement enforced, "
        "(2) no falsifiability/kill criteria specified, (3) no reproducibility standard, "
        "(4) no concrete worked example showing a test's pass/fail bar applied, "
        "(5) vanity-metric warning is shallow (Boldare 1 line, others none), "
        "(6) timeline / cost constraints unspecified, "
        "(7) 'validated enough to scale' threshold undefined. Ries leans qualitative "
        "('hockey stick growth'), Boldare leans procedural without thresholds."
    ),
    "unique_angle": (
        "(1) Four-test gate: pre-stated hypothesis, falsifiable outcome, decision-changing result, "
        "cheap reproducibility — apply BEFORE experiment design review. "
        "(2) Worked B2B pricing example showing same week of traffic producing two different "
        "evidence bodies depending on discipline applied beforehand. "
        "(3) Explicit failure-pattern taxonomy (confirmation interview, vanity-metric chase, "
        "bar drift, tooling-as-methodology, undocumented learning). "
        "(4) Direct positioning against canon: 'canon teaches you the loop, not what counts as "
        "binding evidence'. (5) OSR cycle anchors: 2-week early, 6-week late, signed LOI > "
        "interview enthusiasm."
    ),
    "paa": [
        "What is validated learning in The Lean Startup?",
        "How is validated learning different from regular learning?",
        "What are examples of validated learning experiments?",
        "How do you measure validated learning?",
        "What is the Build-Measure-Learn loop?",
    ],
    "gap_opportunity": (
        "Canon teaches the Build-Measure-Learn loop but not the evidence standard. "
        "OS Research's four-test gate + worked B2B pricing example gives readers an "
        "actionable discipline competitors don't supply."
    ),
}


def upload_to_catbox(content: bytes, filename: str) -> str:
    """Upload to catbox.moe and return the public URL."""
    r = requests.post(
        "https://catbox.moe/user/api.php",
        data={"reqtype": "fileupload"},
        files={"fileToUpload": (filename, content, "application/json")},
        timeout=30,
    )
    r.raise_for_status()
    url = r.text.strip()
    if not url.startswith("https://"):
        raise RuntimeError(f"catbox upload failed: {url}")
    return url


def main() -> int:
    filename = f"{ARTICLE_ID}_serp.json"
    content = json.dumps(PAYLOAD, indent=2, ensure_ascii=False).encode("utf-8")

    print(f"=== Build serp_insights_json for {ARTICLE_ID} ===")
    print(f"  bytes: {len(content)}")
    print(f"  uploading to catbox.moe...")
    url = upload_to_catbox(content, filename)
    print(f"  catbox URL: {url}")

    # Find Airtable record
    r = requests.get(
        f"{AIRTABLE_API_BASE}/{AIRTABLE_BASE_ID}/{ARTICLES_TID}",
        headers={"Authorization": f"Bearer {AIRTABLE_PAT}"},
        params=[("filterByFormula", f"{{article_id}}='{ARTICLE_ID}'")],
        timeout=30,
    )
    r.raise_for_status()
    recs = r.json().get("records", [])
    if not recs:
        print(f"  ERROR: {ARTICLE_ID} not found")
        return 1
    rid = recs[0]["id"]
    print(f"  Airtable record: {rid}")

    # PATCH attachment
    r = requests.patch(
        f"{AIRTABLE_API_BASE}/{AIRTABLE_BASE_ID}/{ARTICLES_TID}/{rid}",
        headers=H,
        json={
            "fields": {
                "serp_insights_json": [{"url": url, "filename": filename}],
            },
            "typecast": True,
        },
        timeout=60,
    )
    if r.status_code >= 400:
        print(f"  ERROR: HTTP {r.status_code} {r.text[:500]}")
        return 1
    print(f"  PATCH ok: HTTP {r.status_code}")
    print(f"  attachment field: {r.json()['fields'].get('serp_insights_json')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
