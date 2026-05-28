"""
Build serp_insights_json attachment for Phase 2 bài 2 (validate business idea).
"""
from __future__ import annotations

import json
import sys
from datetime import date

import requests

from config_kw import AIRTABLE_API_BASE, AIRTABLE_BASE_ID, AIRTABLE_PAT
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from table_ids import TABLE_IDS  # noqa: E402

H = {"Authorization": f"Bearer {AIRTABLE_PAT}", "Content-Type": "application/json"}
ARTICLES_TID = TABLE_IDS["Articles"]
ARTICLE_ID = "OSR-2026-05-22-002"

PAYLOAD = {
    "primary_keyword": "validate business idea",
    "fetched_at": str(date.today()),
    "method": "WebSearch + WebFetch (Claude built-in) — First Round Review fetched in full; HBS/Close/LivePlan blocked or unavailable",
    "top_5_sources": [
        "HBS Online — 5 Steps to Validate Your Business Idea",
        "LivePlan — 5 Easy Steps to Validate Your Business Idea",
        "First Round Review — How to Test a Business Idea (5 steps + tools)",
        "Close.com — How to Validate Your Business Idea (4 steps)",
        "HubSpot — Startup Idea Validation Step-by-Step Guide",
    ],
    "competitor_format_notes": (
        "SERP archetype: procedural step lists (4-12 steps). HBS, LivePlan, WeAreBrain, Close all "
        "follow the same template: define goal → target market → research → customer interviews → "
        "small test → refine. First Round Review goes deeper with named founders (Gagan Biyani, "
        "Webb Brown, Michael Grinich, Jessica McKellar) and specific tactics (cold email, 120+ "
        "interviews, 'eyes light up' signal). Most articles light on examples, heavy on tools "
        "recommendations, and uniformly subjective on what counts as 'validated'."
    ),
    "identified_gap": (
        "Across all canonical sources: (1) no quantified sample size — 120 interviews mentioned "
        "as anecdote, not minimum; (2) 'eyes lighting up' is the modal validation signal, fully "
        "subjective; (3) no pivot vs persist threshold specified anywhere; (4) no stage gating — "
        "validation treated as one-shot; (5) no false-positive taxonomy; (6) no cost/time cap "
        "per experiment; (7) no guidance on weighting conflicting feedback; (8) selection bias "
        "addressed shallowly (cold email mentioned by First Round, others silent). Result: founders "
        "follow the steps, interpret favorably, and ship without binding evidence."
    ),
    "unique_angle": (
        "(1) Four-stage approach with explicit thresholds: Problem evidence (≥60% workaround "
        "naming + ≥40% recent fix attempt), Solution evidence (≥8% pre-sale commitment), Channel "
        "evidence (CAC < LTV/3), Retention evidence (cohort decay curve). "
        "(2) Worked B2B vertical SaaS example (dental scheduling) walking through Stages 1-2 with "
        "real numbers (72% / 44% / 10.6%). "
        "(3) Failure-pattern taxonomy: interview enthusiasm trap, sample-of-friends trap, "
        "vague-threshold trap. "
        "(4) Direct contrast with canon: 'canon teaches the steps, not what counts as binding'. "
        "(5) Connects to OSR validation studio + experiment library + companion validated-learning "
        "piece for evidence-standard depth."
    ),
    "paa": [
        "How many customer interviews do I need to validate a business idea?",
        "How do you test a business idea before launching?",
        "How do you know if a business idea is good?",
        "What is the difference between business idea validation and market research?",
        "How much does it cost to validate a business idea?",
    ],
    "gap_opportunity": (
        "Canon teaches a procedural sequence with subjective signals. OS Research's staged "
        "evidence approach with quantified thresholds + worked B2B example + false-positive "
        "taxonomy gives founders a binding evidence standard competitors lack."
    ),
}


def upload_to_catbox(content: bytes, filename: str) -> str:
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

    print(f"=== serp_insights_json for {ARTICLE_ID} ===")
    print(f"  bytes: {len(content)}")
    url = upload_to_catbox(content, filename)
    print(f"  catbox URL: {url}")

    r = requests.get(
        f"{AIRTABLE_API_BASE}/{AIRTABLE_BASE_ID}/{ARTICLES_TID}",
        headers={"Authorization": f"Bearer {AIRTABLE_PAT}"},
        params=[("filterByFormula", f"{{article_id}}='{ARTICLE_ID}'")],
        timeout=30,
    )
    r.raise_for_status()
    rid = r.json().get("records", [])[0]["id"]
    print(f"  Airtable record: {rid}")

    r = requests.patch(
        f"{AIRTABLE_API_BASE}/{AIRTABLE_BASE_ID}/{ARTICLES_TID}/{rid}",
        headers=H,
        json={
            "fields": {"serp_insights_json": [{"url": url, "filename": filename}]},
            "typecast": True,
        },
        timeout=60,
    )
    if r.status_code >= 400:
        print(f"  ERROR: HTTP {r.status_code} {r.text[:500]}")
        return 1
    print(f"  PATCH ok: HTTP {r.status_code}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
