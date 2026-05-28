# OSR Skills

Claude Code skills for OS Research automation.

## Skills

- **osr-seo** — Orchestrate the OS Research SEO content pipeline: gap-driven SERP research, brand-voiced articles, JSON-LD schema, internal/outbound links, images + infographics (cover/supplementary via direct Unsplash links, infographics hosted on R2), and a 30-criteria audit. Produces N review-ready Airtable articles per batch. The engine code it drives lives in the `seo-engine/` directory of this repo.
- **osr-idea-finder** — Discover LinkedIn post ideas + Vietnam ecosystem trends via WebSearch. Outputs a ranked idea report to the user (self-contained, no external tools).
- **osr-linkedin-post** — Turn research/notes into polished LinkedIn posts.

## Used by

- Local Claude Code sessions (via `.claude/skills/` symlink or copy)
- Scheduled remote agents (Anthropic cloud) — clones this repo, reads `skills/<skill>/SKILL.md`, executes steps.

## Getting started

1. Clone this repo and make the skills visible to Claude Code: symlink (or copy) each directory under `skills/` into `~/.claude/skills/` (e.g. `ln -s "$(pwd)/skills/osr-seo" ~/.claude/skills/osr-seo`).
2. Install the SEO engine's Python deps: `cd seo-engine && pip3 install -r requirements.txt`.
3. Copy `seo-engine/.env.example` to `seo-engine/.env` and fill in keys. Only `AIRTABLE_PAT` + `UNSPLASH_ACCESS_KEY` are required; everything else is optional per feature (comments in the file explain each). `.env` is gitignored — never commit it.
4. Invoke a skill in Claude Code, e.g. `/osr-seo 5` to produce 5 review-ready articles. Each skill's `SKILL.md` documents its full flow.

The `osr-seo` skill drives the Python pipeline in `seo-engine/` (keyword discovery → article generation → Airtable). `osr-idea-finder` and `osr-linkedin-post` are self-contained (no external accounts or tokens).

## Handover notes

- **Where data lives:** Airtable (content database), Cloudflare R2 (infographics only), Framer (published blog). Setup steps in `seo-engine/SETUP.md` and `seo-engine/R2_SETUP.md`; architecture + field reference in `seo-engine/README.md`.
- **Secrets:** none are committed — every key loads from `.env` (gitignored). Before relying on any token that was shared during development, rotate it.
