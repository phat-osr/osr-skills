"""
Per-article config registry for Phase 3 batch (OSR-B-2026-05-PHASE3).

7 articles continuing from Phase 2. Sequence: bài 1-7.
Article IDs OSR-2026-05-22-011 through 017.
"""
from __future__ import annotations

BATCH_ID = "OSR-B-2026-05-PHASE3"

# Verified internal slugs. Inherits Phase 2 anchors + adds new ones from this batch.
INTERNAL_ANCHORS = {
    # OSR-original / EXISTING
    "startup validation studio": ("startup validation studio", "https://www.osresearch.vn/blog/startup-validation-studio"),
    "experiment library": ("experiment library", "https://www.osresearch.vn/blog/experiment-library"),
    "six week testing cycle": ("six week testing cycle", "https://www.osresearch.vn/blog/six-week-testing-cycle"),
    "business model canvas": ("business model canvas", "https://www.osresearch.vn/blog/business-model-canvas"),
    "value proposition canvas": ("value proposition canvas", "https://www.osresearch.vn/blog/value-proposition-canvas"),
    "blue ocean strategy": ("blue ocean strategy", "https://www.osresearch.vn/blog/blue-ocean-strategy"),
    "one page business pitch": ("one page business pitch", "https://www.osresearch.vn/blog/one-page-business-pitch"),
    # Phase 1
    "venture capital vietnam": ("venture capital in vietnam", "https://www.osresearch.vn/blog/venture-capital-vietnam"),
    "vietnam market": ("vietnam market", "https://www.osresearch.vn/blog/vietnam-market"),
    "product market fit": ("product-market fit", "https://www.osresearch.vn/blog/product-market-fit"),
    "jobs to be done framework": ("jobs to be done framework", "https://www.osresearch.vn/blog/jobs-to-be-done-framework-examples"),
    "lean canvas business model": ("lean canvas business model", "https://www.osresearch.vn/blog/lean-canvas-business-model"),
    "vibe coding tools": ("vibe coding tools", "https://www.osresearch.vn/blog/vibe-coding-tools"),
    "minimum viable product": ("minimum viable product examples", "https://www.osresearch.vn/blog/minimum-viable-product-examples"),
    "ai business ideas": ("ai business ideas in 2026", "https://www.osresearch.vn/blog/ai-business-ideas-2026"),
    # Phase 2
    "validated learning lean startup": ("validated learning lean startup", "https://www.osresearch.vn/blog/validated-learning-lean-startup"),
    "validate business idea": ("how to validate a business idea", "https://www.osresearch.vn/blog/validate-business-idea"),
    "north star metric": ("north star metric", "https://www.osresearch.vn/blog/north-star-metric"),
    "vietnam unicorns": ("vietnam unicorns", "https://www.osresearch.vn/blog/vietnam-unicorns"),
    "vietnam economy": ("vietnam economy", "https://www.osresearch.vn/blog/vietnam-economy"),
    "why vietnam economy is booming": ("why vietnam economy is booming", "https://www.osresearch.vn/blog/why-vietnam-economy-is-booming"),
    "fdi in vietnam": ("fdi in vietnam", "https://www.osresearch.vn/blog/fdi-in-vietnam"),
    "starting a business in vietnam as a foreigner": ("starting a business in vietnam as a foreigner", "https://www.osresearch.vn/blog/starting-a-business-in-vietnam-as-a-foreigner"),
    "vietnam fintech": ("vietnam fintech", "https://www.osresearch.vn/blog/vietnam-fintech"),
    "vietnam investment opportunities": ("vietnam investment opportunities", "https://www.osresearch.vn/blog/vietnam-investment-opportunities"),
}

OUTBOUND_DEFAULT = {
    "Eric Ries": "http://www.startuplessonslearned.com/2009/04/validated-learning-about-customers.html",
    "Y Combinator seed guide": "https://www.ycombinator.com/library/4A-a-guide-to-seed-fundraising",
    "Harvard Business School GTM": "https://online.hbs.edu/blog/post/go-to-market-strategy-framework",
}


def _serp(top_sources, format_notes, gap, angle, opportunity, paa_qs):
    return {
        "method": "WebSearch (Claude built-in) + summary synthesis",
        "top_5_sources": top_sources,
        "competitor_format_notes": format_notes,
        "identified_gap": gap,
        "unique_angle": angle,
        "paa": paa_qs,
        "gap_opportunity": opportunity,
    }


PICKS = {
    1: {
        "article_id": "OSR-2026-05-22-011",
        "primary_keyword": "pitch deck template",
        "pattern": "framework_example",
        "draft_file": "01-pitch-deck-template.md",
        "h1_for_schema": "Pitch Deck Template: What Investors Actually Want in 2026",
        "sv": 3600,
        "kd": 12,
        "signal": 65.0,
        "title": "Pitch Deck Template: What Investors Want in 2026",
        "meta_description": (
            "The 2026 pitch deck investors actually fund: unit economics, AI defensibility, "
            "concrete milestones, and the slides most templates still miss. With OSR's worked example."
        ),
        "paa": [
            "What should be on a pitch deck?",
            "What is the 10/20/30 rule for pitch decks?",
            "How long should a pitch deck be?",
            "What do investors look for in a pitch deck?",
            "What are the most important slides in a pitch deck?",
        ],
        "cluster": [
            "pitch deck template", "startup pitch deck", "investor pitch deck", "seed round pitch deck",
            "vc pitch deck examples", "pitch deck slides", "pitch deck structure", "pitch deck design",
            "guy kawasaki 10 slides", "pitch deck unit economics", "pitch deck traction slide",
            "pitch deck problem slide", "pitch deck solution slide", "pitch deck market size",
            "pitch deck team slide", "pitch deck financials", "pitch deck ask slide",
            "pitch deck competition slide", "pitch deck go to market", "pitch deck business model",
            "pitch deck pdf example", "airbnb pitch deck", "uber pitch deck", "facebook pitch deck",
            "pitch deck consultant", "pitch deck redesign", "pitch deck CAC payback", "pitch deck LTV",
            "AI strategy slide", "pitch deck SOM TAM SAM",
        ],
        "serp_insights": _serp(
            top_sources=[
                "DECKO — What Investors Want in a Pitch Deck in 2026 (And What's Changed)",
                "Y Combinator — Pitch deck templates and seed guide",
                "Visible.vc — 23 Pitch Deck Examples",
                "Slidebean — Pitch Deck Examples from 35+ Killer Startups",
                "OGS Capital — Best Pitch Deck Structure in 2026",
            ],
            format_notes=(
                "SERP dominated by template galleries and listicles ('19 best pitch decks'). "
                "Few sources explain WHY 2026 investors changed what they want. None walk through a "
                "worked example of a deck that fails the 2026 bar."
            ),
            gap=[
                "Listicles show decks but don't explain the underlying investor decision criteria",
                "No source frames the 'efficient growth' shift as a structural change in what slides matter",
                "Most templates still lead with TAM bubble charts; none replace with SOM + 18-month plan",
                "Almost no source includes a unit-economics slide template with NDR + CAC Payback",
                "AI Strategy slide is named as required but not shown in any template",
            ],
            angle=[
                "Frame the 2026 shift explicitly: growth-at-all-costs → efficient growth",
                "Walk through a failed pitch deck → fixed pitch deck worked example",
                "Show the unit economics slide investors want (LTV:CAC ≥ 3:1, CAC Payback, NDR)",
                "Replace TAM bubble with SOM + 18-month milestone framing",
                "Show the AI Strategy slide as defensibility, not feature list",
            ],
            opportunity=(
                "Most pitch deck content is template galleries with no diagnosis of why 2026 decks "
                "fail. OSR's deck is the diagnostic: name the new bar, show the slides that meet it, "
                "and walk a concrete deck through the upgrade. This is positioned as the companion to "
                "the one-page business pitch piece for founders moving from validation to raise."
            ),
            paa_qs=[
                "What should be on a pitch deck?",
                "What is the 10/20/30 rule for pitch decks?",
                "How long should a pitch deck be?",
                "What do investors look for in a pitch deck?",
                "What are the most important slides in a pitch deck?",
            ],
        ),
    },
    2: {
        "article_id": "OSR-2026-05-22-012",
        "primary_keyword": "minimum viable product examples",
        "pattern": "framework_example",
        "draft_file": "02-minimum-viable-product.md",
        "h1_for_schema": "Minimum Viable Product Examples: What Real MVPs Actually Validate",
        "sv": 320,
        "kd": 14,
        "signal": 70.0,
        "title": "Minimum Viable Product Examples: What MVPs Really Prove",
        "meta_description": (
            "Real minimum viable product examples (Dropbox, Airbnb, Buffer) plus the failure modes "
            "most MVP articles skip. OS Research on what an MVP actually proves and when to skip building."
        ),
        "paa": [
            "What is a minimum viable product?",
            "What is an example of an MVP?",
            "What is the difference between an MVP and a prototype?",
            "What are the types of MVP?",
            "Why is a minimum viable product important?",
        ],
        "cluster": [
            "minimum viable product", "mvp definition", "mvp meaning", "mvp examples",
            "mvp vs prototype", "mvp development", "mvp software", "mvp agile",
            "concierge mvp", "wizard of oz mvp", "landing page mvp", "single feature mvp",
            "high fidelity mvp", "low fidelity mvp", "mvp validated learning", "eric ries mvp",
            "lean startup mvp", "mvp build measure learn", "mvp pivot", "mvp customer feedback",
            "mvp scope", "mvp roadmap", "mvp pricing", "mvp launch",
            "airbnb mvp", "uber mvp", "spotify mvp", "dropbox mvp video",
            "mvp failure", "mvp success rate", "mvp vs poc",
        ],
        "serp_insights": _serp(
            top_sources=[
                "Wikipedia — Minimum viable product",
                "Nielsen Norman Group — Minimum Viable Product (MVP): Definition",
                "Atlassian — What is a Minimum Viable Product",
                "GeeksforGeeks — Minimum Viable Product (MVP)",
                "Amplitude — What is a Minimum Viable Product",
            ],
            format_notes=(
                "All top results repeat Ries' definition verbatim. Most list 4-5 MVP types and the "
                "Airbnb/Uber/Spotify examples. Almost none challenge the framing or name when an MVP "
                "is the wrong tool."
            ),
            gap=[
                "Every source treats MVP as the right move; none discuss when NOT to build one",
                "No source distinguishes MVP-as-product from MVP-as-validation-experiment",
                "Worked examples skew toward retro success stories (Airbnb 2008); no 2026 examples",
                "Build-measure-learn is invoked but no source shows the learn step failing properly",
                "Validated learning vs feature shipping is conflated everywhere",
            ],
            angle=[
                "Reframe MVP as the answer to a specific assumption, not the default first step",
                "Catalog the MVP failure modes (theatre, feature-shipping, sunk-cost trap)",
                "When to skip the MVP and run a validated learning experiment instead",
                "Connect to OSR's six week testing cycle as the alternative when MVP is wrong tool",
                "Worked example: a SaaS founder picks the wrong MVP, runs out of runway",
            ],
            opportunity=(
                "SV 22,200 with KD 40 is the highest-volume opportunity in the batch. Canon-fight angle: "
                "agree MVPs are useful but reframe them as one tool among several, not the default. "
                "Position the OSR experiment library and six week testing cycle as the alternative when "
                "the assumption being tested doesn't require shipping a product."
            ),
            paa_qs=[
                "What is a minimum viable product?",
                "What is an example of an MVP?",
                "What is the difference between an MVP and a prototype?",
                "What are the types of MVP?",
                "Why is a minimum viable product important?",
            ],
        ),
    },
    3: {
        "article_id": "OSR-2026-05-22-013",
        "primary_keyword": "asian unicorn",
        "pattern": "sector_ideas",
        "draft_file": "03-asian-unicorn.md",
        "h1_for_schema": "Asian Unicorns: The 2026 Reality Check",
        "sv": 2900,
        "kd": 10,
        "signal": 72.0,
        "title": "Asian Unicorns: The 2026 Reality Behind the Numbers",
        "meta_description": (
            "Asia has 475 unicorns and 64 in Southeast Asia, but the 2025-26 reset changed what "
            "qualifies. The countries pulling ahead, the ones losing share, and Vietnam's position."
        ),
        "paa": [
            "How many unicorns are in Asia?",
            "Which country has the most unicorns in Asia?",
            "What are unicorn companies in Southeast Asia?",
            "Why are Asian unicorns slowing down?",
            "Will Vietnam produce more unicorns?",
        ],
        "cluster": [
            "asian unicorn", "southeast asia unicorn", "apac unicorn list", "asia tech unicorn",
            "vietnam unicorn", "indonesia unicorn", "singapore unicorn", "thailand unicorn",
            "philippines unicorn", "malaysia unicorn", "india unicorn count", "china unicorn",
            "grab unicorn", "gojek unicorn", "tokopedia unicorn", "sea group", "shopee parent",
            "traveloka unicorn", "ninja van", "moglix", "thunes unicorn", "carsome unicorn",
            "byju's unicorn india", "zomato unicorn", "asia decacorn",
            "asia tech ecosystem 2026", "asia tech funding slowdown", "asia ipo market",
            "asia growth startups", "asia profitable startups",
        ],
        "serp_insights": _serp(
            top_sources=[
                "StartupBlink — Top Unicorn Startups in South East Asia for 2026",
                "Crunchbase — Southeast Asia Unicorn Startups Hub",
                "Failory — The Full List of 475 APAC Unicorn Startups (2026)",
                "Tech Collective — Southeast Asia's unicorns in 2025 show a new startup reality",
                "Next Unicorn Ventures — Full List of Unicorn Startups in Southeast Asia",
            ],
            format_notes=(
                "SERP is dominated by static lists with company logos and valuation numbers. "
                "Few articles examine the 2025-26 reset. Tech Collective is the rare reflective piece."
            ),
            gap=[
                "Lists are stale snapshots, not analysis of which unicorns are still alive vs zombie",
                "No source distinguishes capital-cycle unicorns from durable unicorns",
                "Country-level comparison is missing; everyone lists by alphabet or valuation",
                "The 2024-25 down-round reset is barely covered in main results",
                "Vietnam's position among Asian unicorns is underrepresented despite four fintech unicorns",
            ],
            angle=[
                "Frame the 2025-26 reset: easy capital cycle ended, profitability era began",
                "Country-by-country breakdown: who is gaining, holding, losing share",
                "Distinguish active operating unicorns from down-rounded/zombie status",
                "Position Vietnam's unicorns in the Asian context (smaller count, sharper concentration)",
                "Name what the next Asian unicorn looks like (B2B + AI + capital efficient)",
            ],
            opportunity=(
                "The market wants reality not lists. The asian unicorn keyword (SV 2,900, KD 10) is "
                "underserved by reflective analysis. OSR's piece becomes the canonical 2026 read on "
                "where Asian unicorns actually stand, with Vietnam contextualized within the broader frame."
            ),
            paa_qs=[
                "How many unicorns are in Asia?",
                "Which country has the most unicorns in Asia?",
                "What are unicorn companies in Southeast Asia?",
                "Why are Asian unicorns slowing down?",
                "Will Vietnam produce more unicorns?",
            ],
        ),
    },
    4: {
        "article_id": "OSR-2026-05-22-014",
        "primary_keyword": "ai business ideas 2026",
        "pattern": "sector_ideas",
        "draft_file": "04-ai-business-ideas.md",
        "h1_for_schema": "AI Business Ideas 2026: Which Ones Have Real Unit Economics",
        "sv": 30,
        "kd": 0,
        "signal": 55.0,
        "title": "AI Business Ideas 2026: Which Ones Actually Work",
        "meta_description": (
            "Every AI listicle promises 22 profitable ideas. The OS Research filter: which AI "
            "businesses have unit economics that work after model costs, and which ones ride the hype."
        ),
        "paa": [
            "What are the best AI business ideas?",
            "How do I start an AI business?",
            "How much does it cost to start an AI business?",
            "Are AI businesses profitable?",
            "Can a non-technical founder start an AI company?",
        ],
        "cluster": [
            "ai business ideas", "ai startup ideas", "profitable ai business", "ai entrepreneur",
            "ai saas ideas", "ai agent business", "ai content business", "ai chatbot business",
            "ai consulting business", "ai automation business", "ai for small business",
            "ai for ecommerce", "ai for healthcare", "ai for finance", "ai for legal",
            "ai for real estate", "ai for marketing", "ai for sales", "ai for hr",
            "ai for education", "ai api wrapper", "ai vertical saas", "ai workflow automation",
            "ai prompt engineer business", "no code ai business", "ai consulting agency",
            "ai voice agent business", "ai video business", "ai image business", "ai newsletter business",
        ],
        "serp_insights": _serp(
            top_sources=[
                "Commerce Pundit — 22 Profitable AI Business Ideas for Entrepreneurs in 2026",
                "Presta — 20 Profitable AI Business Ideas for 2026 (Real Examples)",
                "Shopify — 20 Profitable AI Business Ideas To Make Money in 2026",
                "Squarespace — 10 AI Business Ideas to Explore in 2026",
                "Entrepreneur — As AI Disrupts the Workforce, These Small Businesses Are Still Safe",
            ],
            format_notes=(
                "Almost universal listicle format: '22 AI ideas', '90+ AI business ideas'. "
                "Quantity over filter. Few sources name unit economics or 2026 model-cost reality."
            ),
            gap=[
                "Listicles don't filter for which ideas survive after model costs and CAC",
                "No source addresses the 'AI wrapper' commoditization question",
                "Vertical SaaS vs AI-feature distinction missing in most sources",
                "Defensibility (data flywheel, workflow integration) named rarely",
                "Underserved: founders evaluating, not browsing, which AI ideas have durable economics",
            ],
            angle=[
                "Filter framework: model-cost defensibility, workflow lock-in, distribution match",
                "Three categories: durable AI businesses, hype-cycle bets, commoditized wrappers",
                "Worked example: cost-of-goods math on a typical AI agent business in 2026",
                "Where Vietnamese founders specifically have edge (cost arbitrage + market depth)",
                "Connect to OSR validation toolkit: how to test AI idea before building",
            ],
            opportunity=(
                "All competing AI idea articles are listicles. OSR's filter-and-judge frame becomes "
                "the article that founders actually keep open while evaluating. Connect to validate "
                "business idea and validated learning lean startup pieces for the validation path."
            ),
            paa_qs=[
                "What are the best AI business ideas?",
                "How do I start an AI business?",
                "How much does it cost to start an AI business?",
                "Are AI businesses profitable?",
                "Can a non-technical founder start an AI company?",
            ],
        ),
    },
    5: {
        "article_id": "OSR-2026-05-22-015",
        "primary_keyword": "vietnam tech industry",
        "pattern": "sector_ideas",
        "draft_file": "05-vietnam-tech-industry.md",
        "h1_for_schema": "Vietnam Tech Industry: Where It Actually Sits in 2026",
        "sv": 140,
        "kd": 28,
        "signal": 58.0,
        "title": "Vietnam Tech Industry: The Honest 2026 Read",
        "meta_description": (
            "Vietnam's tech industry hit $148B in revenue and 1.5M workers. The honest read: where "
            "FPT, VNG, and the AI labs actually compete, and where the gap to Singapore still sits."
        ),
        "paa": [
            "How big is Vietnam's tech industry?",
            "What are the largest tech companies in Vietnam?",
            "Is Vietnam good for software development?",
            "What is Vietnam's role in global tech?",
            "What sectors of Vietnam tech are growing fastest?",
        ],
        "cluster": [
            "vietnam tech industry", "vietnam software industry", "vietnam IT industry",
            "fpt software", "vng corporation", "vinai", "viettel", "sky mavis",
            "vietnam saas", "vietnam tech companies", "vietnam outsourcing", "vietnam offshore development",
            "ho chi minh city tech", "hanoi tech", "vietnam semiconductor industry",
            "vietnam ai industry", "vietnam machine learning", "vietnam engineers",
            "vietnam software exports", "vietnam digital economy", "vietnam ICT revenue",
            "vietnam tech salary", "vietnam developer count", "vietnam coding bootcamp",
            "vietnam tech talent", "vietnam tech investment", "vietnam tech ipo",
            "vietnam saas companies", "vietnam fintech industry", "vietnam tech ecosystem",
        ],
        "serp_insights": _serp(
            top_sources=[
                "FPT Software — Pioneering Vietnam's Tech Revolution",
                "TechVify — The Growth Of IT Industry In Vietnam",
                "Vietcetera — How Vietnam Is Redefining Its Place In Global Tech",
                "InCorp — IT Industry in Vietnam: Opportunities and Challenges",
                "KVY Technology — Vietnam's Software Development Industry",
            ],
            format_notes=(
                "Most top results are vendor-PR (FPT promoting itself) or generic country-overview "
                "articles. Honest analysis of competitive positioning vs Singapore/Indonesia is rare."
            ),
            gap=[
                "Most pieces are vendor PR with no honest weakness analysis",
                "Outsourcing-vs-product company split barely covered",
                "AI capability assessment thin; VinAI mentioned without context",
                "Semiconductor pivot ambition vs current reality not honestly addressed",
                "Vietnam-vs-region comparison missing (where does VN actually win and lose)",
            ],
            angle=[
                "Honest segmentation: outsourcing giants, product companies, AI labs, semiconductor bets",
                "Where Vietnam wins: cost-quality balance for outsourcing, engineering talent depth",
                "Where Vietnam loses: product company maturity, design talent, venture density",
                "The semiconductor bet realistically: 50k engineers target vs current pipeline",
                "Worked comparison: Vietnam vs Singapore vs Indonesia on three sector slices",
            ],
            opportunity=(
                "The SERP is vendor PR. A reflective, segmented OSR read on Vietnam tech becomes the "
                "honest reference that investors, founders, and analysts actually link to. Anchors the "
                "Vietnam tech cluster with vietnam fintech, vietnam unicorns, and venture capital "
                "vietnam pieces."
            ),
            paa_qs=[
                "How big is Vietnam's tech industry?",
                "What are the largest tech companies in Vietnam?",
                "Is Vietnam good for software development?",
                "What is Vietnam's role in global tech?",
                "What sectors of Vietnam tech are growing fastest?",
            ],
        ),
    },
    6: {
        "article_id": "OSR-2026-05-22-016",
        "primary_keyword": "go to market strategy",
        "pattern": "framework_example",
        "draft_file": "06-go-to-market-strategy.md",
        "h1_for_schema": "Go-to-Market Strategy: The Diagnostic Most Frameworks Skip",
        "sv": 110,
        "kd": 16,
        "signal": 55.0,
        "title": "Go-to-Market Strategy: Which Motion Fits Your Shape",
        "meta_description": (
            "Most go-to-market frameworks list 10 steps and call it done. The OS Research diagnostic: "
            "which GTM motion fits your product shape, and the failure mode when you pick wrong."
        ),
        "paa": [
            "What is a go-to-market strategy?",
            "What are the steps in a go-to-market strategy?",
            "What is the difference between GTM and marketing strategy?",
            "What are the four go-to-market motions?",
            "How long does it take to develop a GTM strategy?",
        ],
        "cluster": [
            "go to market strategy", "gtm strategy", "go-to-market plan", "startup gtm",
            "product launch strategy", "gtm framework", "gtm motion", "product led growth",
            "sales led growth", "marketing led growth", "community led growth", "gtm icp",
            "ideal customer profile", "gtm pricing", "gtm positioning", "gtm messaging",
            "gtm channels", "gtm playbook", "gtm metrics", "gtm cac payback",
            "gtm sales cycle", "gtm enterprise", "gtm smb", "gtm prosumer",
            "gtm template", "gtm examples", "b2b gtm", "b2c gtm", "saas gtm",
            "gtm execution", "gtm hbs framework",
        ],
        "serp_insights": _serp(
            top_sources=[
                "Harvard Business School — How to Develop a Go-to-Market Strategy for Your Tech Venture",
                "Arise GTM — Go-To-Market Strategy for Startups",
                "Salesmotion — Go-to-Market Strategy Framework: A 90-Day Launch Plan",
                "Stackmatix — Go-to-Market Strategy for Startups: The Complete Framework",
                "Lean Labs — Go-To-Market Strategy for Startups: 10 Key Steps",
            ],
            format_notes=(
                "SERP dominated by N-step frameworks (5, 7, 10, 13 steps). All cover ICP, positioning, "
                "channels, pricing. Few diagnose which motion fits the founder's product shape."
            ),
            gap=[
                "Step-list frameworks don't help founders choose between PLG/SLG/CLG motions",
                "No diagnostic for matching product shape (price, complexity, buyer) to motion",
                "Failure modes from picking wrong motion not catalogued",
                "ICP definition usually generic; rarely tied to channel economics",
                "Most are launch checklists, not strategic frames",
            ],
            angle=[
                "Diagnostic: three questions that determine your motion (price, sales cycle, buyer type)",
                "Four motions decoded: PLG, SLG, MLG, CLG with shape fit",
                "Failure mode catalog: enterprise startup running PLG, consumer app running outbound",
                "Worked example: founder mismatch and the cost of fixing it 18 months in",
                "Connect to validation toolkit: validate motion before scaling",
            ],
            opportunity=(
                "SERP is step-lists. OSR's motion-diagnostic frame becomes the GTM piece founders "
                "actually use. Mid-funnel value for the validation cluster — connects naturally to "
                "validate business idea and product market fit pieces."
            ),
            paa_qs=[
                "What is a go-to-market strategy?",
                "What are the steps in a go-to-market strategy?",
                "What is the difference between GTM and marketing strategy?",
                "What are the four go-to-market motions?",
                "How long does it take to develop a GTM strategy?",
            ],
        ),
    },
    7: {
        "article_id": "OSR-2026-05-22-017",
        "primary_keyword": "how to raise a seed round",
        "pattern": "how_to_validate",
        "draft_file": "07-how-to-raise-a-seed-round.md",
        "h1_for_schema": "How to Raise a Seed Round: The 2026 Founder's Decision Tree",
        "sv": 70,
        "kd": 11,
        "signal": 52.0,
        "title": "How to Raise a Seed Round: 2026 Founder's Playbook",
        "meta_description": (
            "Average seed in 2026 is $4.4M and the bar has risen. OS Research's playbook on whether "
            "to raise, what to prove first, and the SAFE-vs-priced decision most guides skip."
        ),
        "paa": [
            "How much should I raise in a seed round?",
            "When is the right time to raise a seed round?",
            "How long does it take to raise a seed round?",
            "What do investors expect at the seed stage?",
            "Should I use a SAFE or priced round at seed?",
        ],
        "cluster": [
            "how to raise a seed round", "seed funding", "seed round", "seed investors",
            "seed stage startup", "pre-seed funding", "angel investor", "venture capital seed",
            "safe agreement", "convertible note", "priced round", "valuation cap",
            "y combinator seed", "yc safe", "seed deck", "seed pitch deck",
            "seed metrics", "seed traction", "seed product market fit", "warm intro",
            "investor pipeline", "investor update", "investor relations", "fundraising process",
            "fundraising timeline", "fundraising milestone", "fundraising amount",
            "seed term sheet", "post-seed", "seed to series a",
        ],
        "serp_insights": _serp(
            top_sources=[
                "Y Combinator — A guide to seed fundraising",
                "Carta — Pre-Seed Funding: Guide for Early-Stage Startup Founders",
                "CRV — How to Raise Seed Funding: Complete Guide for Founders",
                "Lenny's Newsletter — Raising a seed round 101",
                "Stripe — Seed Funding for Startups: Guide and Best Practices",
            ],
            format_notes=(
                "Major guides are comprehensive but operational (timeline, warm intros, SAFE terms). "
                "Few address the prior question: should you raise at all, and what to prove first."
            ),
            gap=[
                "Most guides assume you should raise, skip the 'should I' decision",
                "12-18 month runway target stated but not tied to validation milestone",
                "SAFE-vs-priced framed as preference, not consequence-aware tradeoff",
                "2026 environment shift (efficient growth bar) not explicit in tactical advice",
                "Decision tree for first-time founders missing in canonical guides",
            ],
            angle=[
                "Decision tree before tactics: should you raise, what does raising commit you to",
                "What to prove BEFORE talking to seed investors (specific milestone gates)",
                "SAFE vs priced round as consequence: dilution, control, signal to next round",
                "2026 specific: efficient growth bar, what seed investors now demand vs 2021",
                "Connect to OSR validation toolkit: validation milestones that justify a raise",
            ],
            opportunity=(
                "Founder-side seed guide complement to OSR's investor-side venture capital vietnam "
                "piece. SV is small but intent is high. Position as the 'should I and how' guide vs "
                "operational checklists everywhere else."
            ),
            paa_qs=[
                "How much should I raise in a seed round?",
                "When is the right time to raise a seed round?",
                "How long does it take to raise a seed round?",
                "What do investors expect at the seed stage?",
                "Should I use a SAFE or priced round at seed?",
            ],
        ),
    },
}
