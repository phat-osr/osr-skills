---
name: osr-seo
description: Orchestrate the OS Research SEO content pipeline — produces N review-ready Airtable articles per batch with gap-driven SERP research, OSR brand voice, JSON-LD schema, internal/outbound links, supplementary images (direct Unsplash links), optional R2-hosted infographics, and audit. Trigger when the user asks to "create N articles", "run a batch", invokes "/osr-seo", or asks to add posts to the osresearch.vn Articles table.
---

# /osr-seo — OSR SEO content pipeline

## Repo + scope

Working repo: the `phat-osr/osr-skills` repo. The engine code lives in its `seo-engine/` directory; clone osr-skills locally and run the steps below from that `seo-engine/` dir (referred to as `$SEO_ENGINE_DIR`). Each batch produces N review-ready Articles rows in Airtable base `appbeNr9P6EcKhrYB`. The content reviewer paste-publishes to Framer CMS afterwards.

Audit target per article: **30 ✓ 0 ✗ 0 ⚠** out of 30 criteria. Audit script is `keyword_research/audit_batch.py` (filter is hardcoded to a date prefix — patch line 185 or run inline).

## Pre-flight checks

Before any pipeline work, verify in this order:

1. **Working dir**: `cd $SEO_ENGINE_DIR` (the `seo-engine/` dir inside your local clone of `phat-osr/osr-skills`)
2. **.env present** with:
   - `UNSPLASH_ACCESS_KEY` (mandatory)
   - DataForSEO + Google CSE (optional)
   - **R2 vars** (only if generating infographics): `R2_ACCOUNT_ID`, `R2_ACCESS_KEY_ID`, `R2_SECRET_ACCESS_KEY`, `R2_BUCKET`, `R2_PUBLIC_URL`
   - `AIRTABLE_PAT`
3. **Airtable PAT** valid — read from `.env` (`AIRTABLE_PAT`). Do not rely on any token committed in `config.py`; rotate any token that was ever shared.
4. **Python deps**: `python3 -c "import requests, dotenv"` (no error; add `boto3` only when hosting infographics on R2)

**Image hosting policy:** cover + supplementary photos use **direct Unsplash hotlinks** (no rehosting — ToS-compliant and one fewer DNS lookup than a re-hosted copy). Only infographics are hosted on R2. If you generate an infographic and R2 vars are missing, run `python3 keyword_research/setup_r2.py` first (see `R2_SETUP.md`). Never commit `.env`.

## The 8-step flow

(Optional **Step 0 — Keyword discovery** runs before Step 1 only when the keyword pool needs refreshing; the 8 numbered steps below are the per-batch article production flow.)

### Step 0 — Keyword discovery (optional precursor — run only when the top-100 pool is stale)

Skip if the Keywords table already holds an unused top-100 pool for the current objective (Step 1 surfaces how many are unused). Run this when most keywords are already used, or when opening a new topic area. Needs DataForSEO creds in `.env` (`DFS_LOGIN`, `DFS_PASSWORD`); ~$1 + a few minutes per run. Run all commands from the repo root.

1. **Seeds = curated file + ad-hoc terms.** Baseline lives in `keyword_research/objective_seeds.py` (`SEEDS_VN_VC` + `SEEDS_FOUNDER_EDU`). Ask the user for any new seed terms for this batch and tag each with a bucket (`vn_vc` or `founder_edu`). Pass them via `--extra-seed` (don't edit the file unless a seed is permanent).

2. **Feed seeds → DataForSEO** (real volume + KD + CPC per long-tail variant):
   ```bash
   python3 keyword_research/dfs_discover.py --dry-run                 # preview plan + cost
   python3 keyword_research/dfs_discover.py \
       --extra-seed "ai sales agent:founder_edu" \
       --extra-seed "vietnam logistics startups:vn_vc"               # live → output/dfs_candidates.csv
   ```

3. **Dedup near-duplicates + off-topic:** `python3 keyword_research/dedup_and_refill_top100.py` — canonicalizes intent (drops stopwords / brand qualifiers), keeps the highest `signal_score` per group.

4. **Score + load top 100 into Keywords:** `python3 keyword_research/keep_top100_per_batch.py --batch-id OSR-B-YYYYMMDD` (`--dry-run` first). Computes the OSR `signal_score` (volume + "vietnam" + framework / validation / AI-build / fundraising boosts), takes the top 100, inserts them tagged with the new `batch_id`; the full pool is attached as a CSV on the Batches row.

The Keywords table now holds a fresh top-100 pool for the new `batch_id` — proceed to Step 1.

### Step 1 — Read current state

Query Airtable to learn what already exists:

```python
from airtable_helpers import fetch_all
from table_ids import TABLE_IDS
articles = fetch_all(TABLE_IDS["Articles"], fields=["primary_keyword","article_id","slug","status","batch_id"])
batches  = fetch_all(TABLE_IDS["Batches"], fields=["batch_id","status"])
keywords = fetch_all(TABLE_IDS["Keywords"], fields=["keyword","volume_global_en","difficulty_proxy","signal_score","bucket"])
```

Capture:
- `used = {a["fields"]["primary_keyword"].lower() for a in articles}` — exclude these
- `existing_slugs = {a["fields"]["slug"]: a["fields"]["primary_keyword"] for a in articles}` — used for internal-link verification later (Step 7)
- Latest `batch_id` so the new one doesn't collide
- Next available `article_id` (format `OSR-YYYY-MM-DD-NNN`)

### Step 2 — Pick N keywords

Filter unused keywords from the top-100 pool, rank by `signal_score` desc, then apply three filters before showing the candidate list to the user:

1. **Semantic overlap with existing articles** — kill near-duplicates
2. **Writability** — can Claude produce a strong OSR-voiced piece on this?
3. **OSR brand fit** — does it match a pillar (Education, Insurance, Urban, Health, Culture, Methodology, Vietnam-Market)?

Also assess **competeability** for OSR's current domain authority. Avoid head terms with KD ≥ 35 unless they're pillar content; prefer KD < 25 long-tail variants. If a head term keyword is picked, document it as "pillar content not SEO bet."

Show the candidate table with score per axis (writability + OSR fit + KD) and let the user approve/swap.

Assign pattern per keyword:
- `framework_example` — concepts/frameworks (BMC, lean canvas, validated learning, north star metric)
- `how_to_validate` — action-oriented validation (validate business idea, customer interview)
- `case_study` — concrete case (vietnam unicorns, momo vietnam)
- `sector_ideas` — Vietnam-market/sector pieces (vietnam economy, fdi in vietnam)

Pattern drives Step 4 section rules, Step 5b infographic-fit assessment, and Step 7 inject_links behavior.

### Step 3 — Per-keyword SERP research (gap-driven)

**This is the most important step. Skipping it produces generic content.**

For each picked keyword, before writing the body:

1. `WebSearch` "<primary_keyword> people also ask" → capture 5 PAA-like questions
2. `WebSearch` "<primary_keyword> <topic adjacent>" → capture top 10 sources
3. **`WebFetch` the top 3 canonical sources in full** — ask each to extract: (a) exact definition, (b) examples given, (c) methodology proposed, (d) what's emphasized, (e) **what's notably absent**
4. Synthesize a `serp_insights` dict:
   - `top_5_sources` — "Site — title" strings
   - `competitor_format_notes` — what archetype dominates the SERP
   - `identified_gap` — bulleted list of what ALL competitors miss
   - `unique_angle` — bulleted list of 3-5 things OSR's article will add
   - `paa` — 5 questions from Step 3.1
   - `gap_opportunity` — one-paragraph thesis on the differentiation

**The article is then designed to fill identified_gap with the unique_angle. No exceptions.**

### Step 4 — Write body

Per article, write markdown to `keyword_research/phase<N>_drafts/NN-<slug>.md`. Target 1,800-2,500 words.

**Structure (in order):**

```markdown
# <H1 — descriptive, not the title_tag>

<aside className="tldr">
**TL;DR.** [3-4 sentences. Names the gap + headline insight. 800-1000 chars.]
</aside>

## What <topic> actually means
[Definition, framing. End with naming the gap competitors leave.]

## The trap / failure mode
[2-3 paragraphs showing the failure pattern.]

## The <OSR framework / N tests / approach>
[Numbered or sub-headed framework — the unique_angle delivered.]

## A worked example
[MANDATORY when competitors lack one. ~250-400 words. Concrete scenario + specific numbers.]

## How this changes what you build / How to apply
[Implications + 3 concrete moves the reader can make this week.]

## Common mistakes
[ONLY for framework_example + how_to_validate. 4-6 bolded failure patterns.]

## Frequently asked questions
[7-10 Q:/A: pairs. First 5 = PAA from Step 3.1. Last 2-5 = depth questions.]
```

**Brand voice rules:**
- **First-person plural in body.** Prefer "we / our / us" for self-reference instead of saying "OS Research [does X]". Passive third-person brand mentions read as self-aggrandizing. Acceptable: 1 brand-intro mention near top ("here at OS Research, we ..."), or formal noun phrases ("OS Research portfolio").
- **Never fabricate OS Research details to fill content.** Do not invent portfolio companies, client engagements, specific outcomes ("we closed $2.1M for a SaaS founder"), or in-house experiments that did not actually happen. If a real-world example is needed for a worked-example section, run a WebSearch to find a verifiable public case (named company, published source) and cite the URL inline. No untraceable "a founder we worked with" stories.
- **No em-dashes.** Use commas, periods, or colons.
- **Never use "OSR" standalone.** Always "OS Research" when the brand name itself appears.
- **No buzzwords**: game-changing, disruptive, synergy, ecosystem (unless ironic), innovative.
- **Short sentences. Active voice. Direct.**
- **Show the work.** Specific numbers > round claims, but only when sourced (your own measured data, cited public data, or a clearly labelled illustrative scenario).
- **No "What OS Research thinks" H2 section.** That voice now lives inside the regular body sections via "we/our" language. Reference the OSR brand-voice doc if uncertain (`skills/osr-linkedin-post/references/brand-voice.md` in this repo, or the seo-engine repo's brand-voice notes).

### Step 5a — Build metadata + schema

Per article, build:

| Field | Source |
|---|---|
| `article_id` | `OSR-YYYY-MM-DD-NNN` |
| `batch_id` | `OSR-B-YYYY-MM-PHASE<N>` |
| `primary_keyword` | from Step 2 pick |
| `search_volume`, `keyword_difficulty`, `signal_score` | from Keywords table |
| `pattern`, `status` | from Step 2; `status="review"` |
| `title_tag` | `optimize_titles.optimize_title()` then sanity-check ≤60 chars |
| `meta_description` | Hand-write, 130-180 chars, name the angle from `unique_angle` |
| `slug` | `osr_template.slugify(primary_keyword)` |
| `schema_jsonld` | `osr_template.build_schema_jsonld(...)` — pass FAQ pairs parsed from body |
| `article_body_text` | `finalize_body()` THEN `clean_markdown()`. **Order matters.** |
| `keyword_cluster` | 30 related concepts from Step 3, 1 per line |
| `people_also_ask` | 5 PAA from Step 3 |
| `serp_insights_json` | Upload dict to catbox.moe, attach URL |
| `framer_url` | `https://www.osresearch.vn/blog/{slug}` |

### Step 5b — Image strategy (mandatory)

**Every article must have 2-3 images** before push:

1. **Cover image (mandatory)** — `image_finder.find_cover_image(primary_keyword)`. Unsplash hit, embedded right after TL;DR. Caption format: `*Photo by [Author](unsplash.com/@handle) on [Unsplash](unsplash.com)*` wrapped in asterisks.

2. **Supplementary Unsplash image (mandatory)** — content-specific query different from cover, inserted at the H2 closest to body midpoint (skip first H2 = intro and last H2 = FAQ). Use `add_supplementary_images.py` pattern; image_query maps per article in the script's `IMAGE_PLAN` dict. After insertion, run `fix_image_caption_format.py` to wrap captions in asterisks.

3. **Infographic (optional but recommended for visual-structure articles)** — generated via `mcp__nano-banana-pro__generate_image` model `gemini-3-pro-image-preview`, `thinkingLevel: HIGH`, 16:9, 2K. Articles that benefit:
   - **framework_example with numbered structure** (BMC 9-block, Lean Canvas, VPC two-circle, pitch deck 10-slide)
   - **comparison articles** (Blue Ocean vs Red Ocean, GTM 2x2 motion matrix)
   - **list/timeline articles** (Asian unicorns by country, MVP examples timeline, seed-round 5 gates staircase)
   - Skip for pure prose articles (Vietnam macro economy, generic methodology guides)

#### Infographic prompt template (brand-compliant, avoids AI-slop)

```
DESIGN BRIEF FOR AN INFOGRAPHIC. Render ONLY the visual content described.
Any text in the image must be ONLY the exact quoted strings shown.
Do NOT render typography meta-instructions, color codes, font names, or weight numbers inside the image.

DIMENSIONS: 16:9 canvas. Background #f9fbff with subtle diagonal hairline texture.

EXACT TEXT TO RENDER (these are the ONLY strings allowed in the image):
1. Top-left title: "<the article topic title — 2-5 words>"
2. Subtitle below title: "<one-line article angle>"
3. Top-right corner: "osresearch.vn"
4. [List ALL other visible text strings explicitly]
5. Bottom callout strip: "<one-sentence key insight>"

VISUAL LAYOUT:
- Title font: display sans-serif with INK TRAPS (small angular cuts at letterform joins, similar to ABC Whyte Inktrap character; reference: PP Editorial Old, Migra)
- Subtitle font: clean modern sans-serif (IBM Plex Sans style)
- "osresearch.vn" mark in same ink-trap display sans-serif, deep blue color
- [Describe the geometric layout — grid, timeline, matrix, etc.]
- [Per-element specs: shape, position, icon, label]

ABSOLUTE RULES:
- VISUAL FIRST. Icons/illustrations carry the story. Text is minimal labels only.
- Flat 2D editorial. NO 3D, NO gradients, NO shadows, NO realism, NO AI-cartoon style, NO neon glow, NO stock-photo illustrations.
- All pictograms in the image: SAME line weight (3px), SAME geometric style, 2-color (#0248F6 + #181818).
- Editorial inspiration: Pentagram, Information is Beautiful, The Economist, Bloomberg Businessweek.

COLORS (only these): #0248F6 (brand blue), #181818 (carbon text), #5e646a (muted grey), #f9fbff (off-white background), #ffffff (card/shape fills), #e5e9f0 (subtle borders).
```

**Critical prompting lessons:**
- **Strict text whitelist.** Always list "EXACT TEXT TO RENDER" with numbered strings. The model otherwise leaks styling notes (e.g., "IBM Plex Sans 700, #181818") into rendered labels.
- **Use `thinkingLevel: HIGH`** for any infographic with 5+ text labels or precise structure (timeline, matrix, multi-block).
- **Specify ink-trap display sans-serif** for headers (proxy for ABC Whyte Inktrap which the model doesn't know by name). Body uses IBM Plex Sans.
- **One accent color rule.** OSR blue `#0248F6` is the ONLY brand accent; carbon and grey carry the rest. Red `#f03e3e` only allowed as semantic "warning/red ocean" accent.
- **Anti-AI-slop directives** must be explicit and forbidden-pattern oriented ("NO 3D shading, NO faux glossy effects, NO neon glow…").

After generation: save PNG to `/tmp/`, then upload **directly to R2** (infographics are the only image type that gets re-hosted — they are AI-generated, brand-owned assets with no stable upstream URL). Use the R2 creds from `setup_r2.py` / `.env` with a boto3 S3 client against `https://{R2_ACCOUNT_ID}.r2.cloudflarestorage.com`:

```python
key = f"articles/{slug}/infographic-{sha1(png_bytes)[:8]}.png"
s3.put_object(Bucket=R2_BUCKET, Key=key, Body=png_bytes,
              ContentType="image/png",
              CacheControl="public, max-age=31536000, immutable")
infographic_url = f"{R2_PUBLIC_URL}/{key}"
```

Insert the resulting `{R2_PUBLIC_URL}/articles/{slug}/infographic-...png` markdown into the draft body at a logical H2 marker (typically right before the structural section the infographic visualizes — `## The 9 building blocks` for BMC, `## Country-by-country breakdown` for unicorns, etc).

### Step 6 — Inject internal + outbound links

**Internal link slugs MUST be verified against Airtable.** Slug ≠ post title.

Build a verified slug map for the current batch:

```python
slug_by_kw = {
    a["fields"]["primary_keyword"].lower(): a["fields"]["slug"]
    for a in articles_in_airtable
    if a["fields"].get("status") in ("published", "review")
}
```

Then inject links to anchors that match phrases naturally appearing in body. Target 3-5 internal + 2-5 outbound per article.

If a phrase doesn't naturally appear but the inbound link is wanted, **add the phrase to the body intentionally**.

### Step 7 — Push to Airtable

Use `push_phase<N>_article.py` (one generic script per batch reading from `phase<N>_picks.PICKS`):

1. `ensure_batch(dry)` — create Batches row if not present
2. `insert_article(record, dry)` — POST new or PATCH existing if article_id matches
3. serp_insights_json attachment via catbox.moe (Airtable mirrors to its own CDN)

PATCH is partial — fields not in payload are preserved.

### Step 8 — Audit + report

Run `audit_batch.py` (patch the article_id filter prefix to match the current batch's date):

```python
# audit_batch.py line 185 — change OSR-2026-05-21- to today's date prefix
```

Target: **30 ✓ 0 ✗ 0 ⚠** per article. Common warnings (acceptable but prefer to fix):
- **Over-target inbound (6+)** — content-rich; OK
- **Over-target FAQ (11+ Q)** — content-rich; OK
- **Body words ≥1500** under by ~100 — borderline, acceptable
- **Internal links 1-2** under — fix by adding anchor phrases to body

Hard failures (must fix):
- **Any ✗ on `serp_insights_json`** — Step 5a attachment failed; re-run push script
- **`TL;DR plain bold` ✗** — Step 5a `clean_markdown` was skipped, re-run push
- **brand: standalone OSR found** — `apply_brand_naming()` was bypassed
- **image count < 2** — Step 5b skipped supplementary; run `add_supplementary_images.py`
- **caption format ✗** — captions missing asterisk wrap; run `fix_image_caption_format.py`

Report to user: per-article pass/fail counts + Airtable record IDs + framer_url predictions.

## Patterns → section rules (from `osr_template.SECTION_RULES`)

| pattern | Common mistakes |
|---|---|
| `framework_example` | ✓ |
| `how_to_validate` | ✓ |
| `case_study` | ✗ |
| `sector_ideas` | ✗ |
| `general` | ✗ |

Note: "What OS Research thinks" section removed from all patterns as of 2026-05-26. OS Research perspective now expressed via first-person "we/our" inline throughout the body.

## Image count per article (target)

| Pattern | Cover | Supplementary | Infographic | Total |
|---|---|---|---|---|
| `framework_example` (numbered/structured) | ✓ | ✓ | ✓ (strongly recommended) | 3 |
| `framework_example` (concept) | ✓ | ✓ | optional | 2-3 |
| `how_to_validate` | ✓ | ✓ | optional (decision tree, gates) | 2-3 |
| `case_study` | ✓ | ✓ | optional (timeline) | 2-3 |
| `sector_ideas` | ✓ | ✓ | optional (geographic / quant chart) | 2-3 |

Minimum 2 images per article (cover + supplementary). Infographic adds depth + dwell time + makes article more shareable on LinkedIn/Twitter.

## Reusable scripts

| Script | Purpose |
|---|---|
| `keyword_research/objective_seeds.py` | Step 0: curated seed list (`SEEDS_VN_VC` + `SEEDS_FOUNDER_EDU`); `all_seeds()` |
| `keyword_research/dfs_discover.py` | Step 0: feed seeds (file + `--extra-seed`) to DataForSEO → `output/dfs_candidates.csv` |
| `keyword_research/dedup_and_refill_top100.py` | Step 0: canonicalize + dedup near-duplicate/off-topic keywords |
| `keyword_research/keep_top100_per_batch.py` | Step 0: signal-score → top 100 into Keywords table tagged with `batch_id` |
| `keyword_research/push_phase<N>_article.py` | End-to-end push: image, schema, link inject, body finalize, Airtable upsert |
| `keyword_research/phase<N>_picks.py` | Per-article config registry: PICKS dict + INTERNAL_ANCHORS + OUTBOUND_DEFAULT |
| `keyword_research/add_supplementary_images.py` | Adds 1 content-specific Unsplash image per article, mid-body |
| `keyword_research/fix_image_caption_format.py` | Wraps Unsplash captions in `*...*` for italic rendering |
| `keyword_research/setup_r2.py` | One-time R2 bucket + S3 token + .env config (infographic hosting only) |
| `keyword_research/optimize_titles.py` | SERP-pattern title generator |
| `keyword_research/image_finder.py` | Unsplash search + quality check |
| `keyword_research/osr_template.py` | finalize_body + build_schema_jsonld + slugify + apply_brand_naming |
| `keyword_research/render_paste_ready.py` | `clean_markdown()` strips JSX |
| `keyword_research/audit_batch.py` | 30-criteria audit |

## Common gotchas

1. **Slug ≠ title.** Always verify internal-link slugs against Airtable.
2. **JSX strip is separate.** `finalize_body` does NOT strip `<aside>`. `clean_markdown` does. Apply last.
3. **DataForSEO is optional.** If creds missing, use WebSearch + WebFetch fallback for PAA/cluster/serp_insights.
4. **`serp_insights_json` is an attachment** — upload to catbox.moe → PATCH `[{"url": ...}]`.
5. **`audit_batch.py` filter is hardcoded** — change line 185 or use inline audit.
6. **Catbox.moe requires User-Agent.** Direct `requests.get(catbox_url)` fails with `RemoteDisconnected`. Use a browser UA string.
7. **R2 token endpoint not API-creatable.** Cloudflare doesn't expose programmatic creation of S3-compatible R2 tokens via the cfut_* token. User must create via dashboard once (Manage R2 API Tokens → Create API Token).
8. **Infographic prompts: typography meta-text leaks.** Mentioning "IBM Plex Sans 700" inside element description causes the model to render that literally. Strict text whitelist + put typography rules in a separate "VISUAL LAYOUT" section.
9. **Infographic icon style consistency.** Spell out "SAME line weight, SAME geometric style, 2-color" — model defaults to varied styles otherwise.
10. **Articles needing inbound link bump:** add natural anchor phrases like "validate business idea", "venture capital vietnam", "vietnam unicorns", "jobs to be done framework" in body. `inject_simple_links()` auto-converts first occurrence.

## When NOT to use this skill

- One-off content edits — just edit + PATCH directly
- Non-blog content (LinkedIn, newsletter) — different formats and tone
- Pure keyword research with no article output — run Step 0 scripts directly (`dfs_discover.py` → `dedup_and_refill_top100.py` → `keep_top100_per_batch.py`)
- Republishing existing posts to new domains — different workflow

## Output to user

```
Batch <batch_id> complete.
  - Articles created/updated: <N>
  - Image refs: <N> cover, <N> supplementary (direct Unsplash links), <N> infographic (R2-hosted)
  - Airtable record IDs: <list>
  - Audit: <pass>✓ <fail>✗ <warn>⚠ out of <30 × N>
  - Framer paste URLs (predicted):
    - https://www.osresearch.vn/blog/<slug-1>
    - ...
  - Next: the reviewer checks status=review articles in Airtable, then paste-publishes to Framer.
```

If any article < 30/30 hard-fail, list the specific failed criteria + suggested fix.
