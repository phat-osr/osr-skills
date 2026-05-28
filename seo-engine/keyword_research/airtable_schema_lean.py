"""
Create the lean 2-table schema in OSR SEO Engine base:
  - Batches (lightweight tracking)
  - Articles (active work — 16 fields + 3 attachments)

Idempotent: skips tables/fields that already exist.

Run:
    python airtable_schema_lean.py
"""
from __future__ import annotations

import sys
import time
from typing import Any

import requests

from config_kw import AIRTABLE_META_BASE, AIRTABLE_PAT

HEADERS = {"Authorization": f"Bearer {AIRTABLE_PAT}", "Content-Type": "application/json"}


def _sel(*options: str) -> dict[str, Any]:
    return {"choices": [{"name": o} for o in options]}


TABLES: list[dict[str, Any]] = [
    {
        "name": "Batches",
        "description": "Lightweight tracking — 1 row per batch of 10 articles.",
        "fields": [
            {"name": "batch_id", "type": "singleLineText"},
            {"name": "theme_label", "type": "singleLineText"},
            {"name": "created_date", "type": "date",
             "options": {"dateFormat": {"name": "iso"}}},
            {"name": "status", "type": "singleSelect",
             "options": _sel("research", "drafting", "review", "approved", "published", "archived")},
            {"name": "total_volume", "type": "number", "options": {"precision": 0}},
            {"name": "avg_kd", "type": "number", "options": {"precision": 1}},
            {"name": "article_count", "type": "number", "options": {"precision": 0}},
            {"name": "notes", "type": "multilineText"},
            {"name": "keyword_pool_csv", "type": "multipleAttachments"},
        ],
    },
    {
        "name": "Articles",
        "description": "Lean Articles table — 16 fields + 3 attachments. Each field maps directly to Framer CMS.",
        "fields": [
            {"name": "article_id", "type": "singleLineText"},
            {"name": "batch_id", "type": "singleLineText"},  # plain text link by ID
            {"name": "primary_keyword", "type": "singleLineText"},
            {"name": "search_volume", "type": "number", "options": {"precision": 0}},
            {"name": "keyword_difficulty", "type": "number", "options": {"precision": 0}},
            {"name": "signal_score", "type": "number", "options": {"precision": 1}},
            {"name": "pattern", "type": "singleSelect",
             "options": _sel("sector_ideas", "how_to_validate", "case_study",
                              "framework_example", "general")},
            {"name": "status", "type": "singleSelect",
             "options": _sel("idea", "drafting", "review", "approved", "published")},
            # Framer-paste-ready fields
            {"name": "title_tag", "type": "singleLineText"},
            {"name": "meta_description", "type": "multilineText"},
            {"name": "slug", "type": "singleLineText"},
            {"name": "cover_image_url", "type": "url"},
            {"name": "cover_image_alt", "type": "singleLineText"},
            {"name": "cover_image_credit", "type": "singleLineText"},
            {"name": "schema_jsonld", "type": "multilineText"},
            {"name": "framer_url", "type": "url"},
            # Attachments
            {"name": "keyword_cluster_csv", "type": "multipleAttachments"},
            {"name": "serp_insights_json", "type": "multipleAttachments"},
            {"name": "article_body_md", "type": "multipleAttachments"},
            # Operational
            {"name": "notes", "type": "multilineText"},
        ],
    },
]


def list_tables() -> dict[str, dict[str, Any]]:
    r = requests.get(f"{AIRTABLE_META_BASE}/tables", headers=HEADERS, timeout=30)
    r.raise_for_status()
    return {t["name"]: t for t in r.json().get("tables", [])}


def create_table(spec: dict[str, Any]) -> dict[str, Any]:
    payload = {
        "name": spec["name"],
        "description": spec.get("description", ""),
        "fields": spec["fields"],
    }
    r = requests.post(f"{AIRTABLE_META_BASE}/tables", headers=HEADERS, json=payload, timeout=30)
    if r.status_code >= 400:
        raise RuntimeError(f"Create {spec['name']} failed: {r.status_code} {r.text}")
    return r.json()


def add_field(table_id: str, field: dict[str, Any]) -> None:
    r = requests.post(f"{AIRTABLE_META_BASE}/tables/{table_id}/fields",
                       headers=HEADERS, json=field, timeout=30)
    if r.status_code >= 400:
        print(f"    skip field {field['name']}: {r.status_code} {r.text[:200]}")


def main() -> int:
    existing = list_tables()
    print(f"Existing tables: {sorted(existing)}\n")

    new_ids: dict[str, str] = {}

    for spec in TABLES:
        name = spec["name"]
        if name in existing:
            print(f"[=] {name} exists ({existing[name]['id']})")
            new_ids[name] = existing[name]["id"]
            existing_field_names = {f["name"] for f in existing[name]["fields"]}
            missing = [f for f in spec["fields"] if f["name"] not in existing_field_names]
            if missing:
                print(f"    adding {len(missing)} missing fields")
                for f in missing:
                    add_field(existing[name]["id"], f)
                    time.sleep(0.25)
        else:
            print(f"[+] Creating {name} with {len(spec['fields'])} fields")
            t = create_table(spec)
            new_ids[name] = t["id"]
            print(f"    id = {t['id']}")
            time.sleep(0.5)

    print(f"\nFinal IDs:")
    for name, tid in new_ids.items():
        print(f"  {name:<10s} {tid}")

    # Update table_ids.py
    print("\n--- Update table_ids.py manually with:")
    for name, tid in new_ids.items():
        print(f'    "{name}": "{tid}",')
    return 0


if __name__ == "__main__":
    sys.exit(main())
