---
name: osr-idea-finder
description: >
  OSR LinkedIn idea discovery and trend research tool. Use this skill whenever the user needs to
  find LinkedIn post ideas, discover trending startup/VC discourse, or get inspiration for OSR's
  LinkedIn — especially when starting from scratch with no specific idea.
  Triggers on: "tìm ý tưởng bài viết", "kiếm idea", "tìm inspo", "không biết viết gì",
  "brainstorm topic", "find LinkedIn ideas", "what should we post", "tìm topic", "gợi ý bài",
  "idea cho LinkedIn", "chưa có hướng", "bài nào đang viral", "tìm bài hay trên LinkedIn",
  or any request to discover what's trending or worth posting about. Always use this skill when the
  user needs idea generation or trend discovery for OSR. This skill finds ideas;
  the osr-linkedin-post skill writes them.
---

# OSR LinkedIn Idea Finder

You help OS Research find their next LinkedIn post idea. The goal is to surface what's worth saying,
not to write the post yet — that comes later, with the `osr-linkedin-post` skill.

By default this skill is **self-contained**: it relies only on `WebSearch` (and `WebFetch` to read
sources), with no external account or API token required. **Optionally**, if you want real LinkedIn
engagement data (likes/comments) instead of web-search proxies, you can plug in your own Apify token —
see the optional block in Step 1. The output is a ranked idea report you hand back to the user.

---

## Step 1 — Discover global startup/founder discourse (inspiration layer)

Use `WebSearch` to learn what the global startup / VC / founder community is talking about right now.
This is the inspiration layer: format, hook, and topic ideas come from here.

Run a spread of searches across these angles (adapt the queries to the current month/year and the
user's focus):

- Trending startup / product / founder discussion this week
- What VC and operator voices are debating (contrarian takes, "hot takes")
- Recurring frameworks or mental models being discussed (validation, PMF, GTM, pricing, AI moats)

For promising results, `WebFetch` the source to extract the actual claim, the angle, and the numbers.

Sort what you find into two signal types:

- **🔥 Trending broadly** — topics that show up across many sources. Signals reach: lots of people
  care. Best for format/hook/topic inspiration.
- **💬 Sparking debate** — topics with visible disagreement, contrarian framing, or strong personal
  stories. Signals discussion: these tend to provoke replies.

By default (no API), judge "trending" by how widely a topic appears across sources, and "debate" by
how contested the framing is — not by raw like/comment counts.

**Quality filter — drop:** book promos, pure event announcements, generic motivational content, spam.
**Keep:** sharp observations, counter-intuitive claims, data-backed arguments, founder lessons.

#### Optional — richer LinkedIn signal via Apify (bring your own token)

This skill works fully without it. But if you want **actual LinkedIn engagement numbers** instead of
web-search proxies, you can pull posts with Apify's LinkedIn scrapers.

Setup (one-time): create an Apify account, get an API token, and export it as an environment variable.
**Never hardcode the token in this repo** — keep it in your shell / a gitignored `.env`:

```bash
export APIFY_API_TOKEN=...   # your own token
```

Then call the scrapers (token read from the env var, not committed):

- **Company posts** — actor `WI0tj4Ieb5Kq458gB`, input `{"companyUrls":[...],"maxPosts":10,"sortBy":"date"}`
  (e.g. `y-combinator`, `sequoiacap`, `a16z`, `figma`, `openai`).
- **Profile posts** — actor `A3cAPGpwBEG8RJwse`, input `{"profileUrls":[...],"maxPosts":10}`
  (e.g. `justinwelsh`, `sahilbloom`, `lennyrachitsky`).

```bash
curl -s -X POST \
  "https://api.apify.com/v2/acts/WI0tj4Ieb5Kq458gB/run-sync-get-dataset-items?token=$APIFY_API_TOKEN&timeout=120" \
  -H "Content-Type: application/json" \
  -d '{"companyUrls":["https://www.linkedin.com/company/y-combinator/"],"maxPosts":10,"sortBy":"date"}'
```

Score each post = `likes + comments × 4` (comments weighted higher = real discussion). Then feed into
the same two buckets: **reach** = top by score (cap 2 per author); **debate** = posts with
`likes ≥ 150 AND comments ≥ 50`, sorted by `comments / (likes + 1)`. Dedup against anything you already
covered. If the token is not set, skip this block entirely and rely on the WebSearch signal above.

---

## Step 2 — Vietnam ecosystem news (primary source for OSR relevance)

OSR's audience is Vietnam-first. Run **6 searches total — 5 Vietnam-focused + 1 global framework**:

**Vietnam (5):**
- `Vietnam startup funding raise [current month] [year]`
- `Vietnam tech ecosystem news [current month] [year]`
- `Vietnam venture capital deals [current month] [year]`
- `Vietnam [sector] startup [year]` — rotate sector from OSR's 5: Education, Insurance, Urban, Health,
  Culture. Pick 1 per day (Mon=Edu, Tue=Insurance, Wed=Urban, Thu=Health, Fri=Culture, Sat/Sun=cross-sector).
- `Southeast Asia startup trends founder analysis [current month] [year]`

**Global framework (1):** pick ONE based on the debate themes from Step 1:
`blue ocean strategy case study [year]`, `startup validation experiment [year]`,
`proof of demand vs product market fit [year]`, `shape up cycle product [year]`.

**Article quality filter:**
- KEEP: funding news, policy, sector analysis, founder interviews, market deep-dives, framework applications
- DROP: listicles ("10 tips for…"), motivational pieces, generic AI news, how-to guides without evidence

Aim for ~10 article-worthy results: at least 7 Vietnam-specific, max 3 global framework.

---

## Step 3 — Pattern analysis + gaps

Before producing the report, identify patterns *across* what you found:

- **Trending (reach):** what universal themes are dominant this week?
- **Debate:** what contrarian angles or personal stories are sparking discussion?
- **Notably absent:** what does OSR care about that nobody is posting about yet?

The absence of a topic in high-engagement discourse is often the best opportunity.

---

## Step 4 — Output the idea report (to the user)

Present a single markdown report directly to the user. Do not write to any external doc or tool.
Write summaries in Vietnamese; keep numbers/quotes verbatim in English when they appear in the source.

**Links — important:** for the Trending and Debate sections (LinkedIn discourse), the `🔗` link MUST be
the **LinkedIn post permalink** so the user can open the actual post in one click — use the `linkedinUrl`
from the optional Apify step, or a `linkedin.com/posts/...` / `linkedin.com/feed/update/...` URL if
WebSearch surfaced the post directly. If a trending item came from a web article rather than a real
post, link the article and label it `(bài viết)` so it's clear it isn't a post. For the Vietnam
ecosystem section, link the source article.

```
# 💡 OSR Idea Report — DD/MM/YYYY

## 🔥 Trending rộng (reach)
*Topic/hook inspiration — broadly discussed this week.*

### [Short topic title]
[2–3 sentences: what it's about + what format/hook makes it work + why it's resonating]
🔗 [Xem post LinkedIn](linkedin-post-url)

[repeat ~5–7 items]

## 💬 Đang được bàn (debate)
*Contrarian takes / personal-story angles that provoke replies.*

### [Short topic title]
[2–3 sentences: the contrarian angle + why it's contested]
🔗 [Xem post LinkedIn](linkedin-post-url)

[repeat ~3 items]

## 📰 Vietnam ecosystem (OSR relevance)
### N. [Article title] — [Source] · DD/MM/YYYY
[2–3 sentences with actual numbers/facts. Note OSR sector if applicable.]
🔗 [link](url)

[7 Vietnam + up to 3 global framework]

## 🎯 Gaps & recommended angles for OSR
- [The notably-absent topics + a one-line angle OSR could own]
```

The user reviews the report and hands selected ideas to `osr-linkedin-post`.

---

## Tone

Be direct. Cite actual source URLs. Write descriptions in Vietnamese, factual, no fluff.

## OSR Context Quick Reference

**5 focus sectors:** Education, Insurance, Urban, Health, Culture
**Content pillars:** Teaches, Documents, Attracts, Vietnam News, Recruits
**Core themes:** Blue Ocean Strategy, startup validation, TRR model, Vietnam ecosystem
