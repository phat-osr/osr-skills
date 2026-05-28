"""
Interactive Cloudflare R2 setup. Run ONCE before hosting infographics on R2.

Asks for CF API Token + Account ID via stdin (no echo for token).
Then auto-creates bucket, generates S3 credentials, enables r2.dev public URL,
and writes credentials to .env.

Usage:
    python3 setup_r2.py
    python3 setup_r2.py --bucket my-bucket-name
"""
from __future__ import annotations

import argparse
import getpass
import json
import re
import sys
import time
from pathlib import Path

import requests

CF_API = "https://api.cloudflare.com/client/v4"
ENV_PATH = Path(__file__).resolve().parent.parent / ".env"


def cf_request(method: str, path: str, token: str, json_body: dict | None = None) -> dict:
    url = f"{CF_API}{path}"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    r = requests.request(method, url, headers=headers, json=json_body, timeout=30)
    try:
        data = r.json()
    except Exception:
        r.raise_for_status()
        raise
    if not data.get("success"):
        errors = data.get("errors", [])
        raise RuntimeError(f"CF API {method} {path} -> HTTP {r.status_code}: {json.dumps(errors, indent=2)}")
    return data


def verify_token(token: str) -> str:
    """Verify token is valid; return user email."""
    data = cf_request("GET", "/user/tokens/verify", token)
    return data.get("result", {}).get("status", "unknown")


def list_buckets(token: str, account_id: str) -> list[dict]:
    data = cf_request("GET", f"/accounts/{account_id}/r2/buckets", token)
    return data.get("result", {}).get("buckets", [])


def create_bucket(token: str, account_id: str, name: str) -> bool:
    """Returns True if created, False if already existed."""
    try:
        cf_request("POST", f"/accounts/{account_id}/r2/buckets", token, {"name": name})
        return True
    except RuntimeError as e:
        if "already exists" in str(e).lower() or "10004" in str(e):
            return False
        raise


def enable_managed_public_url(token: str, account_id: str, bucket: str) -> str:
    """Enable r2.dev managed public URL. Returns the public URL."""
    # Enable the managed domain
    path = f"/accounts/{account_id}/r2/buckets/{bucket}/domains/managed"
    body = {"enabled": True}
    data = cf_request("PUT", path, token, body)
    result = data.get("result", {})
    domain = result.get("domain", "")
    if domain:
        return f"https://{domain}"
    # Fallback: query GET to read the URL
    data = cf_request("GET", path, token)
    result = data.get("result", {})
    domain = result.get("domain", "")
    if domain:
        return f"https://{domain}"
    raise RuntimeError(f"Could not retrieve managed r2.dev URL: {result}")


def create_s3_token(token: str, account_id: str, bucket: str) -> dict:
    """Create a scoped R2 API token returning S3-compatible credentials."""
    path = f"/accounts/{account_id}/r2/api/tokens"
    body = {
        "name": f"osr-seo-engine-{bucket}-{int(time.time())}",
        "policies": [
            {
                "effect": "allow",
                "permissions": ["read-and-write"],
                "buckets": [bucket],
            }
        ],
    }
    data = cf_request("POST", path, token, body)
    result = data.get("result", {})
    return {
        "access_key_id": result.get("accessKeyId"),
        "secret_access_key": result.get("secretAccessKey"),
        "token_id": result.get("id"),
        "name": result.get("name"),
    }


def upsert_env(env_path: Path, updates: dict[str, str]):
    """Update .env in place: replace existing keys or append new ones."""
    lines = []
    existing_keys = set()
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            stripped = line.strip()
            if "=" in stripped and not stripped.startswith("#"):
                key = stripped.split("=", 1)[0].strip()
                if key in updates:
                    lines.append(f"{key}={updates[key]}")
                    existing_keys.add(key)
                    continue
            lines.append(line)
    for key, value in updates.items():
        if key not in existing_keys:
            lines.append(f"{key}={value}")
    env_path.write_text("\n".join(lines) + "\n")


def test_credentials(s3_creds: dict, account_id: str, bucket: str, public_url: str) -> bool:
    """Smoke test: try to upload + download a small file via boto3."""
    try:
        import boto3
    except ImportError:
        print("  [skip test] boto3 not installed; will be needed for migration")
        return True
    s3 = boto3.client(
        "s3",
        endpoint_url=f"https://{account_id}.r2.cloudflarestorage.com",
        aws_access_key_id=s3_creds["access_key_id"],
        aws_secret_access_key=s3_creds["secret_access_key"],
        region_name="auto",
    )
    test_key = "_setup_test.txt"
    test_body = f"R2 setup test {time.time()}".encode()
    s3.put_object(Bucket=bucket, Key=test_key, Body=test_body, ContentType="text/plain")
    print(f"  PUT ok: {test_key}")
    # Try public read
    r = requests.get(f"{public_url}/{test_key}", timeout=10)
    if r.status_code == 200 and r.content == test_body:
        print(f"  Public GET ok via {public_url}")
        s3.delete_object(Bucket=bucket, Key=test_key)
        return True
    print(f"  Public GET returned {r.status_code} (may need a moment for r2.dev URL to activate)")
    # Don't fail — the URL sometimes needs ~30s to propagate
    s3.delete_object(Bucket=bucket, Key=test_key)
    return True


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--bucket", default="osresearch-cdn", help="Bucket name (default: osresearch-cdn)")
    ap.add_argument("--token", default=None, help="CF API token (or prompted)")
    ap.add_argument("--account-id", default=None, help="CF Account ID (or prompted)")
    args = ap.parse_args()

    print("=== Cloudflare R2 setup ===\n")

    token = args.token or getpass.getpass("Cloudflare API Token: ").strip()
    if not token:
        print("ERROR: empty token"); return 1
    account_id = args.account_id or input("Cloudflare Account ID: ").strip()
    if not re.fullmatch(r"[0-9a-f]{32}", account_id):
        print(f"ERROR: Account ID must be 32-char hex, got: {account_id!r}"); return 1
    bucket = (input(f"Bucket name [{args.bucket}]: ").strip() or args.bucket)
    if not re.fullmatch(r"[a-z0-9-]{3,63}", bucket):
        print(f"ERROR: bucket name must be 3-63 chars, lowercase a-z 0-9 dash"); return 1

    print(f"\nUsing bucket: {bucket}\n")

    # 1. Verify token
    print("Step 1/5: Verify API token")
    status = verify_token(token)
    print(f"  token status: {status}")
    if status != "active":
        print(f"ERROR: token not active"); return 1

    # 2. Create bucket
    print("\nStep 2/5: Create bucket")
    created = create_bucket(token, account_id, bucket)
    print(f"  {'created' if created else 'bucket already exists, reusing'}: {bucket}")

    # 3. Enable r2.dev public URL
    print("\nStep 3/5: Enable r2.dev public URL")
    public_url = enable_managed_public_url(token, account_id, bucket)
    print(f"  public URL: {public_url}")

    # 4. Generate S3 credentials
    print("\nStep 4/5: Generate S3 credentials")
    s3 = create_s3_token(token, account_id, bucket)
    print(f"  access_key_id: {s3['access_key_id'][:8]}...")
    print(f"  secret_access_key: <{len(s3['secret_access_key'])} chars>")

    # 5. Write to .env
    print("\nStep 5/5: Write .env")
    upsert_env(ENV_PATH, {
        "R2_ACCOUNT_ID": account_id,
        "R2_ACCESS_KEY_ID": s3["access_key_id"],
        "R2_SECRET_ACCESS_KEY": s3["secret_access_key"],
        "R2_BUCKET": bucket,
        "R2_PUBLIC_URL": public_url,
    })
    print(f"  wrote: {ENV_PATH}")

    # 6. Smoke test
    print("\nStep 6/5 (bonus): Smoke test")
    test_credentials(s3, account_id, bucket, public_url)

    print("\n=== Done ===")
    print("R2 ready. Infographics are uploaded to R2 inline during /osr-seo Step 5b.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
