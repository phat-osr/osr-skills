"""Shared Airtable helpers for keyword_research scripts."""
from __future__ import annotations

import time
from typing import Any

import requests

from config_kw import AIRTABLE_API_BASE, AIRTABLE_BASE_ID, AIRTABLE_PAT

HEADERS = {
    "Authorization": f"Bearer {AIRTABLE_PAT}",
    "Content-Type": "application/json",
}


def fetch_all(table_id: str, fields: list[str] | None = None,
              formula: str | None = None) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    url = f"{AIRTABLE_API_BASE}/{AIRTABLE_BASE_ID}/{table_id}"
    offset = None
    while True:
        params: dict[str, Any] = {"pageSize": 100}
        if fields:
            params["fields[]"] = fields
        if formula:
            params["filterByFormula"] = formula
        if offset:
            params["offset"] = offset
        r = requests.get(url, headers=HEADERS, params=params, timeout=30)
        r.raise_for_status()
        data = r.json()
        out.extend(data.get("records", []))
        offset = data.get("offset")
        if not offset:
            break
    return out


def insert_records(table_id: str, records: list[dict[str, Any]],
                   chunk_size: int = 10, sleep_s: float = 0.22) -> int:
    url = f"{AIRTABLE_API_BASE}/{AIRTABLE_BASE_ID}/{table_id}"
    created = 0
    for i in range(0, len(records), chunk_size):
        chunk = records[i:i + chunk_size]
        payload = {"records": [{"fields": r} for r in chunk], "typecast": True}
        r = requests.post(url, headers=HEADERS, json=payload, timeout=30)
        if r.status_code >= 400:
            print(f"  insert failed chunk {i}: {r.status_code} {r.text[:300]}")
            r.raise_for_status()
        created += len(chunk)
        time.sleep(sleep_s)
    return created


def upsert_records(table_id: str, records: list[dict[str, Any]],
                   merge_on: list[str], chunk_size: int = 10, sleep_s: float = 0.22) -> int:
    """Airtable performUpsert by merge keys."""
    url = f"{AIRTABLE_API_BASE}/{AIRTABLE_BASE_ID}/{table_id}"
    n = 0
    for i in range(0, len(records), chunk_size):
        chunk = records[i:i + chunk_size]
        payload = {
            "performUpsert": {"fieldsToMergeOn": merge_on},
            "records": [{"fields": r} for r in chunk],
            "typecast": True,
        }
        r = requests.patch(url, headers=HEADERS, json=payload, timeout=30)
        if r.status_code >= 400:
            print(f"  upsert failed chunk {i}: {r.status_code} {r.text[:300]}")
            r.raise_for_status()
        n += len(chunk)
        time.sleep(sleep_s)
    return n


def update_record(table_id: str, record_id: str, fields: dict[str, Any]) -> None:
    url = f"{AIRTABLE_API_BASE}/{AIRTABLE_BASE_ID}/{table_id}/{record_id}"
    r = requests.patch(url, headers=HEADERS,
                       json={"fields": fields, "typecast": True}, timeout=30)
    if r.status_code >= 400:
        print(f"  update failed: {r.status_code} {r.text[:200]}")
        r.raise_for_status()
