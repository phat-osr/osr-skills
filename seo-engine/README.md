# OSR SEO Engine

Content pipeline for [osresearch.vn](https://www.osresearch.vn) — produces review-ready SEO articles from a deduped DataForSEO keyword pool, with brand-voiced bodies, SEO-optimized titles, JSON-LD schema, OSR-branded infographics (nano-banana-pro), supplementary photos via **direct Unsplash links**, People Also Ask + cluster keywords, and curated internal + outbound links. Only infographics are re-hosted (on Cloudflare R2); cover + supplementary photos hotlink Unsplash directly. Output lands in Airtable for review, then Pete paste-publishes to Framer CMS.

**Status:** Phase 1+2+3 shipped — 27 articles in Airtable (status=review) + 9 existing osresearch.vn posts imported. Cover + supplementary photos serve from direct Unsplash links; 9 infographics hosted on R2. Skill `/osr-seo` orchestrates the full flow.

## Quick start

```bash
# 1. Setup
cp .env.example .env  # then fill in keys (Airtable PAT, DataForSEO, Unsplash, optional Google CSE)
pip3 install --user requests markdown

# 2. Verify pipeline state
cd keyword_research
python3 audit_batch.py
# expect: TOTAL: 276 pass, 0 fail, 24 warn (out of 300)

# 3. Run the master pipeline (Pete typically invokes via /osr-seo skill in Claude Code)
python3 complete_10_articles.py   # builds 10 article rows
python3 inject_links.py           # injects internal + outbound contextual links
python3 audit_batch.py            # verifies against plan criteria
```

## Architecture

**Airtable — 3 active tables:**
- `Batches` — 1 row per batch (theme, total volume, avg KD)
- `Keywords` — top 100 deduped per batch (signal-scored + bucket-diversified)
- `Articles` — 20 fields per article (all metadata, schema, body, attachments)

**Pipeline (8 steps):** state check → pick N (semantic overlap + writability + OSR fit + competeability) → **per-keyword SERP research (gap-driven, WebSearch+WebFetch top 3)** → write body → build metadata/schema → **image strategy (cover + supplementary as direct Unsplash links + optional OSR-branded infographic uploaded to R2)** → verify internal slugs + inject links → push to Airtable → audit + report. See `~/.claude/skills/osr-seo/SKILL.md`.

Step 3 is the load-bearing step: WebFetch top 3 canonical sources, identify the gap, write `unique_angle` before writing the body. Skipping it produces generic content that competes on definition rather than on differentiation.

**Image strategy (2-3 per article):**
1. **Cover** (Unsplash via `image_finder.find_cover_image`) — mandatory, after TL;DR
2. **Supplementary** (Unsplash via `add_supplementary_images.py`) — mandatory, mid-body
3. **Infographic** (nano-banana-pro via `mcp__nano-banana-pro__generate_image`) — strongly recommended for framework_example with numbered structure, comparison articles, list/timeline articles. ABC Whyte Inktrap-style title, IBM Plex Sans body, OSR color palette (#0248F6 / #181818 / #5e646a / #f9fbff), `osresearch.vn` branding top-right, 16:9 2K, `thinkingLevel: HIGH`. See SKILL.md for the strict-text-whitelist prompt template that avoids AI-slop.

**Image hosting:**
- **Cover + supplementary photos** hotlink **directly to Unsplash** (`images.unsplash.com/...`) — no rehosting. This is ToS-compliant and avoids an extra CDN hop. The attribution caption (`*Photo by [Author](unsplash.com/@handle) on [Unsplash](unsplash.com)*`) is required and kept inline.
- **Infographics only** are re-hosted on Cloudflare R2 (AI-generated, brand-owned, no stable upstream URL). One-time setup: `python3 keyword_research/setup_r2.py` (interactive — needs CF API token + Account ID). Each infographic is uploaded at generation time to `articles/{slug}/infographic-{sha1[:8]}.png` with immutable cache headers. See `R2_SETUP.md`.

## File map

### Root
| File | Purpose |
|---|---|
| `config.py` | Airtable PAT + Base ID, geo configs |
| `table_ids.py` | Hardcoded Airtable table IDs |

### `keyword_research/`

**Data sources:**
| File | Purpose |
|---|---|
| `dataforseo_client.py` | DFS v3 API wrapper (Keywords + SERP + KD endpoints) |
| `dfs_discover.py` | Keyword suggestions + related_keywords pipeline |
| `objective_seeds.py` | Curated 67-seed list per OSR objective |
| `output/dfs_candidates.csv` | 1448-keyword raw pool from DFS ($1 spend) |

**Schema + helpers:**
| File | Purpose |
|---|---|
| `airtable_helpers.py` | Airtable CRUD with chunking + retries |
| `airtable_schema_lean.py` | Create lean schema (idempotent) |
| `config_kw.py` | Geo configs, env loader, output dirs |

**Keyword scoring + selection:**
| File | Purpose |
|---|---|
| `populate_keywords.py` | Signal score formula + Keywords table insert |
| `dedup_and_refill_top100.py` | Canonical dedup (1448→724 unique) + bucket-diverse top 100 |
| `keep_top100_per_batch.py` | Wipe + insert top 100 with batch_id ref |

**Article content (canonical sources):**
| File | Purpose |
|---|---|
| `v4_content.py` | 10 v4 article bodies (reusable Phase 1 source) |
| `phase1_fresh.py` | Fresh bodies for keywords not in v4 (venture capital vietnam, vietnam market — refreshed 2026-05 with 2025 actuals) |
| `phase1_extras.py` | "What OS Research thinks" + "Common mistakes" per primary_keyword |

**Body finalization:**
| File | Purpose |
|---|---|
| `osr_template.py` | Brand naming, JSON-LD generator, section rules, body finalizer (cover image insert + em-dash removal + extras append per pattern) |
| `render_paste_ready.py` | `clean_markdown()` for Framer paste (strips `<aside>` JSX, keeps image caption) |
| `optimize_titles.py` | SERP-pattern title optimizer (number, year, power phrase per keyword type) |
| `inject_links.py` | Inbound + outbound link injection from curated anchor maps |

**Image:**
| File | Purpose |
|---|---|
| `image_finder.py` | Unsplash primary + Google CSE fallback per quality heuristic |

**Master pipeline + utilities:**
| File | Purpose |
|---|---|
| `complete_10_articles.py` | Main pipeline — picks 10 + runs full flow per article |
| `insert_existing_posts.py` | Import existing osresearch.vn posts (CSV) + pivot Phase 1 overlaps |
| `refresh_10_bodies.py` | Re-render bodies after template changes |
| `add_paa_field.py` | Populate `people_also_ask` from SERP data |
| `audit_batch.py` | 30-criteria audit per article — outputs pass/fail/warn |

## Articles table fields (20)

| Field | Type | Source |
|---|---|---|
| article_id, batch_id, primary_keyword | text | identifiers |
| search_volume, keyword_difficulty, signal_score | number | DFS + computed |
| pattern, status | select | template + workflow |
| title_tag, meta_description, slug | text | SERP-optimized |
| cover_image_url, _alt, _credit | url/text | Unsplash |
| schema_jsonld | longtext | auto (Article + FAQPage + Breadcrumb + Org + Person) |
| article_body_text | longtext | finalized markdown |
| keyword_cluster | longtext | top 30 related, 1 per line |
| people_also_ask | longtext | PAA from SERP, 1 question per line |
| serp_insights_json | attachment | catbox.moe URL: top sources + PAA + gap |
| framer_url | url | predicted = `https://www.osresearch.vn/blog/{slug}` |

## Skill: `/osr-seo`

Pete invokes via Claude Code. Located at `~/.claude/skills/osr-seo/SKILL.md`. Orchestrates the 8-step pipeline:

1. State check (existing articles, used keywords, slug map, next batch_id, next article_id)
2. Pick N keywords from top-100 pool — filter by semantic overlap with used, writability, OSR brand fit; assign pattern
3. **Per-keyword SERP research (gap-driven)** — WebSearch PAA + related, WebFetch top 3 canonical sources, write `identified_gap` + `unique_angle` BEFORE the body
4. Write body to `phase2_drafts/NN-<slug>.md` (1,800-2,500 words; structure: TLDR → problem → OSR framework → **worked example** → implications → OSR thinks → common mistakes → FAQ)
5. Build metadata + image + schema + serp_insights_json per article (apply `finalize_body` then `clean_markdown` for JSX strip — order matters)
6. Verify internal-link slugs against Airtable (slug ≠ post title) + inject links naturally; target 3-5 internal + 2-5 outbound
7. Create Batches row, then POST or PATCH Articles row; upload `serp_insights_json` via catbox.moe
8. Audit (`audit_batch.py` — patch filter prefix line 185 for new batches) + report record IDs + framer URLs

**Lessons baked into the skill** (from Phase 2 bài 1):
- Slug ≠ title. Verify against Airtable before linking.
- WebFetch top 3 sources is mandatory. WebSearch alone gives surface-level coverage notes.
- Worked example is required when the canonical SERP lacks one.
- `clean_markdown` runs after `finalize_body`, not before.
- `serp_insights_json` is an attachment, not text. Upload to catbox.moe then PATCH.

## Cost per batch

~$1.05 per batch of 10:
- DataForSEO: ~$1 (keyword + SERP enrichment)
- Google CSE: ~$0.05 (optional image fallback)
- Unsplash + WebSearch + WebFetch + Claude article generation: free

## Plan reference

Full plan: `~/.claude/plans/hi-n-t-i-t-c-n-agile-whistle.md` — covers architecture, pipeline steps, OSR Winning Article Format, brand voice rules, Framer paste workflow, bugs encountered + fixes, and Phase 2 roadmap.
