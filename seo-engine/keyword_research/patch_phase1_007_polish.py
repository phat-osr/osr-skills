"""Polish Phase 1 #007 after keyword swap: strip em-dashes + add 2-3 inbound anchors."""
import sys, re
import requests
from config_kw import AIRTABLE_API_BASE, AIRTABLE_BASE_ID, AIRTABLE_PAT
sys.path.insert(0, "/Users/phatnguyen/Downloads/OSR/seo-engine")
from table_ids import TABLE_IDS

H = {"Authorization": f"Bearer {AIRTABLE_PAT}", "Content-Type": "application/json"}
TID = TABLE_IDS["Articles"]
RID = "recq4fAkOAPkfPiAU"


def patch_body(body: str) -> str:
    # 1. Rewrite the 4 em-dash sentences in my new examples section
    body = body.replace(
        'Before building the social media scheduler, Joel Gascoigne tested whether the job — "schedule my social posts so I can focus on creating" — was urgent enough to drive sign-ups and willingness to pay.',
        'Before building the social media scheduler, Joel Gascoigne tested whether the job, "schedule my social posts so I can focus on creating," was urgent enough to drive sign-ups and willingness to pay.',
    )
    body = body.replace(
        'The product design — pay anyone in seconds with a phone number — fit the job better than incumbent banking apps.',
        'The product design, pay anyone in seconds with a phone number, fit the job better than incumbent banking apps.',
    )

    # 2. Add 2-3 inbound anchors naturally where the phrase already appears or can be added.
    # Add a sentence at end of Buffer paragraph linking to validate business idea
    buffer_anchor = "The MVP was the JTBD validation artifact."
    if buffer_anchor in body and "validate business idea" not in body.lower():
        body = body.replace(
            buffer_anchor,
            buffer_anchor + " The pattern of running cheap validation before committing to build is the canonical [validate business idea](https://www.osresearch.vn/blog/validate-business-idea) move.",
        )

    # Add MoMo → vietnam unicorns link in the MoMo paragraph
    momo_marker = "MoMo's JTBD framing emphasized the moment of transfer between people."
    if momo_marker in body and "vietnam unicorns" not in body.lower():
        body = body.replace(
            momo_marker,
            momo_marker + " MoMo is one of the four [vietnam unicorns](https://www.osresearch.vn/blog/vietnam-unicorns) that emerged from the cash-to-digital payment transition.",
        )

    # Add jobs-to-be-done → product market fit link if not present
    if "[product-market fit]" not in body and "product-market fit" not in body.lower():
        # Add to a sensible spot near JTBD-and-VPC section
        marker_pmf = "## What OS Research thinks"
        if marker_pmf in body:
            body = body.replace(
                marker_pmf,
                "When the JTBD framing is right and the customer's job statement is sharp, you are closer to [product-market fit](https://www.osresearch.vn/blog/product-market-fit) than feature-led teams typically realize.\n\n" + marker_pmf,
            )

    # 3. Final em-dash scan & strip any remaining
    body = re.sub(r"\s—\s", ", ", body)
    body = re.sub(r"—", ", ", body)
    return body


def main():
    r = requests.get(
        f"{AIRTABLE_API_BASE}/{AIRTABLE_BASE_ID}/{TID}/{RID}",
        headers={"Authorization": f"Bearer {AIRTABLE_PAT}"},
        timeout=30,
    )
    r.raise_for_status()
    body = r.json()["fields"].get("article_body_text", "")
    new_body = patch_body(body)
    print(f"em-dashes before: {body.count('—')}  after: {new_body.count('—')}")
    inbound_before = len(re.findall(r"\(https://www\.osresearch\.vn/", body))
    inbound_after = len(re.findall(r"\(https://www\.osresearch\.vn/", new_body))
    print(f"inbound before: {inbound_before}  after: {inbound_after}")
    print(f"body len {len(body)} -> {len(new_body)}")

    if "--dry-run" in sys.argv:
        print("[DRY] not sending"); return
    r = requests.patch(
        f"{AIRTABLE_API_BASE}/{AIRTABLE_BASE_ID}/{TID}/{RID}",
        headers=H,
        json={"fields": {"article_body_text": new_body}, "typecast": True},
        timeout=60,
    )
    if r.status_code >= 400:
        print(f"ERROR {r.status_code}: {r.text[:400]}"); return
    print("PATCH ok")


if __name__ == "__main__":
    main()
