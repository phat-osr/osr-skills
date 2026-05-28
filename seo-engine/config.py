"""Shared config for OSR SEO Engine."""
import os

# Airtable
AIRTABLE_BASE_ID = "appbeNr9P6EcKhrYB"
AIRTABLE_PAT = os.environ.get("AIRTABLE_PAT", "")
if not AIRTABLE_PAT:
    raise RuntimeError("AIRTABLE_PAT not set. Add it to .env (see .env.example).")
AIRTABLE_API_BASE = "https://api.airtable.com/v0"
AIRTABLE_META_BASE = f"{AIRTABLE_API_BASE}/meta/bases/{AIRTABLE_BASE_ID}"

# Site
SITE_DOMAIN = "www.osresearch.vn"
SITE_BASE_URL = f"https://{SITE_DOMAIN}"
BLOG_PATH = "/blog"

# Quotas
TOTAL_ARTICLES = 1000
PATTERN_QUOTAS = {
    "sector_ideas": 400,
    "how_to_validate": 300,
    "case_study": 200,
    "framework_example": 100,
}

# OSR pillars
PILLARS = [
    {"name": "Education", "keyword": "edtech startup vietnam", "persona": "founder"},
    {"name": "Insurance", "keyword": "insurtech vietnam", "persona": "investor"},
    {"name": "Urban", "keyword": "urban tech vietnam", "persona": "investor"},
    {"name": "Health", "keyword": "healthtech vietnam", "persona": "founder"},
    {"name": "Culture", "keyword": "creator economy vietnam", "persona": "founder"},
    {"name": "Methodology", "keyword": "startup validation framework", "persona": "investor"},
    {"name": "Vietnam-Market", "keyword": "vietnam startup ecosystem", "persona": "investor"},
]

# Authors
# Example placeholder author — replace with the real author before publishing.
AUTHORS = [
    {
        "name": "Author Name",
        "bio": "Author at OS Research, a startup validation studio in Vietnam.",
        "linkedin_url": "https://www.linkedin.com/in/your-handle/",
        "photo_url": "https://www.osresearch.vn/assets/images/author.png",
    },
]
