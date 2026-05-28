"""
Per-article config registry for Phase 2 batch (OSR-B-2026-05-PHASE2).

Each entry is keyed by bài number (3-10). Drives push_phase2_article.py.
Bài 1 + 2 already shipped via their own scripts; structure copied here for reference.
"""
from __future__ import annotations

BATCH_ID = "OSR-B-2026-05-PHASE2"

# Verified internal slugs (cross-checked against Airtable). Shared across all bài.
INTERNAL_ANCHORS = {
    "startup validation studio": ("startup validation studio", "https://www.osresearch.vn/blog/startup-validation-studio"),
    "vietnam unicorns": ("vietnam unicorns", "https://www.osresearch.vn/blog/vietnam-unicorns"),
    "vietnam economy": ("vietnam economy", "https://www.osresearch.vn/blog/vietnam-economy"),
    "why vietnam economy is booming": ("why vietnam economy is booming", "https://www.osresearch.vn/blog/why-vietnam-economy-is-booming"),
    "experiment library": ("experiment library", "https://www.osresearch.vn/blog/experiment-library"),
    "six week testing cycle": ("six week testing cycle", "https://www.osresearch.vn/blog/six-week-testing-cycle"),
    "product-market fit": ("product-market fit", "https://www.osresearch.vn/blog/product-market-fit"),
    "validated learning lean startup": ("validated learning lean startup", "https://www.osresearch.vn/blog/validated-learning-lean-startup"),
    "validate business idea": ("how to validate a business idea", "https://www.osresearch.vn/blog/validate-business-idea"),
    "venture capital vietnam": ("venture capital in vietnam", "https://www.osresearch.vn/blog/venture-capital-vietnam"),
    "vietnam market": ("vietnam market", "https://www.osresearch.vn/blog/vietnam-market"),
    "blue ocean strategy": ("blue ocean strategy", "https://www.osresearch.vn/blog/blue-ocean-strategy"),
}

OUTBOUND_DEFAULT = {
    "Eric Ries": "http://www.startuplessonslearned.com/2009/04/validated-learning-about-customers.html",
    "The Lean Startup": "https://theleanstartup.com/principles",
}

PICKS = {
    10: {
        "article_id": "OSR-2026-05-22-010",
        "primary_keyword": "vietnam investment opportunities",
        "pattern": "sector_ideas",
        "draft_file": "10-vietnam-investment-opportunities.md",
        "h1_for_schema": "Vietnam Investment Opportunities",
        "sv": 30,
        "kd": 4,
        "signal": 46.3,
        "title": "Vietnam Investment Opportunities: 2026 Outlook",
        "meta_description": (
            "Where the real asymmetry sits in 2026: insurtech distribution, embedded finance, "
            "SME banking software, B2B services for foreign-invested manufacturers."
        ),
        "paa": [
            "What are the best investment opportunities in Vietnam right now?",
            "Is Vietnam a good country to invest in?",
            "How can foreigners invest in Vietnam?",
            "What are the risks of investing in Vietnam?",
            "What sectors should investors focus on in Vietnam?",
        ],
        "cluster": [
            "vietnam investment 2026", "vietnam private equity", "vietnam venture capital",
            "vietnam stock market", "vn index", "vietnam adr", "vietnam fdi",
            "vietnam insurtech investment", "vietnam embedded finance", "vietnam sme banking",
            "vietnam b2b saas", "vietnam consumer software", "vietnam fintech investment",
            "vietnam real estate investment", "vietnam industrial property", "vietnam manufacturing investment",
            "vietnam listed companies", "vietnam dividend stocks", "vietnam banking stocks",
            "vietnam consumer staples", "vietnam foreign ownership limit", "vietnam asean exposure",
            "vietnam emerging market", "vietnam growth equity", "vietnam angel investment",
            "vietnam strategic investment", "vietnam unicorn investment", "vietnam regulatory risk",
            "vietnam exit options", "vietnam capital markets",
        ],
        "outbound_extra": {
            "World Bank Vietnam": "https://www.worldbank.org/en/country/vietnam",
            "Vietnam Briefing": "https://www.vietnam-briefing.com/news/vietnam-economy-gdp-fdi-and-trade-2025.html/",
        },
        "image_query_override": "investment chart growth vietnam",
        "serp_insights": {
            "top_5_sources": [
                "Vietnam Briefing — Investment Climate Outlook",
                "Asia-Relocation — Vietnam Economic 2026 Outlook",
                "Mekong Capital — Foreign Direct Investment in Vietnam",
                "ASEAN Briefing — Vietnam investment guides",
                "World Bank Vietnam — country overview",
            ],
            "competitor_format_notes": (
                "Archetype: consultancy outlook reports + regional broker research + government "
                "investment promotion materials. Most are promotional in tone, listing sectors "
                "without ranking them by current asymmetry. Few separate priced-in opportunities "
                "from the still-asymmetric ones. None systematically address access paths (public "
                "vs private vs FDI) and their respective constraints."
            ),
            "identified_gap": (
                "(1) Sectors listed without ranking by current valuation/asymmetry, "
                "(2) Access path (public, private, FDI) not framed as a strategic choice with "
                "tradeoffs, (3) 'Where asymmetry is NOT' (priced-in obvious bets) almost never "
                "named, (4) The 2024-2026 valuation correction not framed as a re-entry "
                "opportunity, (5) Diligence signals (cohort retention, regulatory positioning) "
                "absent — most reports assume institutional reader does this on their own."
            ),
            "unique_angle": (
                "(1) Four asymmetric opportunity areas named explicitly with picks within each "
                "(insurtech distribution, embedded finance infra, SME banking, B2B services for "
                "FDI manufacturers). "
                "(2) 'Where asymmetry is NOT' section: payments, horizontal e-commerce, residential "
                "real estate, Web3 — explicitly priced-in or structurally weak. "
                "(3) Three access paths (public, private, FDI) compared by constraint and best-fit "
                "investor profile. "
                "(4) Three diligence signals named: FDI run-rate, cohort retention, regulatory "
                "direction. "
                "(5) Connects to economy, fintech, FDI, unicorns, foreigner-business pieces for "
                "the full structural read."
            ),
            "gap_opportunity": (
                "Canon is consultancy outlook reports listing sectors as opportunities. OS Research "
                "ranks them by current asymmetry, names where the obvious bets are priced in, and "
                "compares access paths with explicit tradeoffs."
            ),
        },
    },
    9: {
        "article_id": "OSR-2026-05-22-009",
        "primary_keyword": "vietnam fintech",
        "pattern": "sector_ideas",
        "draft_file": "09-vietnam-fintech.md",
        "h1_for_schema": "Vietnam Fintech",
        "sv": 90,
        "kd": 0,
        "signal": 48.5,
        "title": "Vietnam Fintech: 2026 Market Report",
        "meta_description": (
            "Vietnam's fintech market: $3.42B in 2025, $7.78B forecast by 2030. The payments era "
            "is maturing. Insurtech, embedded finance, and what the next unicorn looks like."
        ),
        "paa": [
            "How big is Vietnam's fintech market?",
            "What are the largest fintech companies in Vietnam?",
            "What sectors of Vietnam's fintech are growing fastest?",
            "Why is Vietnam such a strong fintech market?",
            "What is the role of QR code payments in Vietnamese fintech?",
        ],
        "cluster": [
            "vietnam fintech market size", "vietnam fintech 2025", "vietnam fintech 2026",
            "momo vietnam", "vnpay vietnam", "vnlife", "tiki financial services",
            "vietnam digital payments", "vietnam qr payment", "vietnam mobile payment",
            "vietnam insurtech", "vietnam embedded finance", "vietnam lending fintech",
            "vietnam buy now pay later", "vietnam open banking", "vietnam biometric authentication",
            "state bank of vietnam", "vietnam e-wallet", "vietnam digital banking",
            "vietnam neobank", "vietnam alternative credit scoring", "vietnam fintech startups",
            "vietnam wealth tech", "vietnam fintech unicorn", "vietnam fintech investment",
            "vietnam fintech regulation", "vietnam consumer credit", "vietnam sme lending",
            "vietnam digital economy", "vietnam financial inclusion",
        ],
        "outbound_extra": {
            "Mordor Intelligence": "https://www.mordorintelligence.com/industry-reports/vietnam-fintech-market",
            "TechSci Research": "https://www.techsciresearch.com/report/vietnam-fintech-market/8076.html",
        },
        "image_query_override": "mobile payment phone qr code",
        "serp_insights": {
            "top_5_sources": [
                "WorldFIS / Vietnam — Vietnam's Fintech Ecosystem 2026",
                "Mordor Intelligence — Vietnam Fintech Market Size & Share Outlook to 2030",
                "TechSci Research — Vietnam Fintech Market 2029 Forecast",
                "Russin & Vecchi — Vietnam Is Accelerating Its Fintech Landscape",
                "Digital In Asia — Vietnam Digital Market 2026",
            ],
            "competitor_format_notes": (
                "Archetype: market-research firm reports (Mordor, TechSci, IMARC) selling paid "
                "downloads + consultancy summaries. Most cover the headline market size, segment "
                "breakdowns, and growth forecasts. Few connect the four-fintech-unicorn outcome "
                "to the structural payments wedge that is now closing. None systematically frame "
                "what the next unicorn category will look like or what investors should watch."
            ),
            "identified_gap": (
                "(1) The 'payments era is closing' framing absent — most reports treat payments "
                "as the ongoing growth story, (2) Biometric mandate treated as compliance news "
                "rather than barrier-to-entry shift, (3) Three structural opening categories "
                "(insurtech, embedded finance, lending infra) not ranked by likelihood of next "
                "unicorn, (4) Investor diligence signals (cohort retention, adjacent-product "
                "unit economics, regulatory positioning) absent, (5) Connection between fintech "
                "maturation and the broader two-speed economy not made."
            ),
            "unique_angle": (
                "(1) Payments era explicitly framed as closing — and what's opening next. "
                "(2) Three candidate categories for the next unicorn (insurtech distribution, "
                "embedded finance infrastructure, SME banking) ranked with reasoning. "
                "(3) Three investor diligence signals named: cohort retention, adjacent-product "
                "unit economics, regulatory positioning. "
                "(4) Biometric mandate framed as both compliance and consolidation event. "
                "(5) Connects to unicorns piece + economy piece for structural read."
            ),
            "gap_opportunity": (
                "Canon is market-research firm reports + segment breakdowns. OS Research provides "
                "the strategic read on what's closing, what's opening, and what the next unicorn "
                "category will look like, with explicit investor diligence guidance."
            ),
        },
    },
    8: {
        "article_id": "OSR-2026-05-22-008",
        "primary_keyword": "starting a business in vietnam as a foreigner",
        "pattern": "sector_ideas",
        "draft_file": "08-starting-business-vietnam-foreigner.md",
        "h1_for_schema": "Starting a Business in Vietnam as a Foreigner",
        "sv": 20,
        "kd": 0,
        "signal": 50.9,
        "title": "Business in Vietnam: 2026 Guide for Founders",
        "meta_description": (
            "LLC setup, IRC, ERC, 30-45 day timeline, $10K capital benchmark. The strategic "
            "choices most guides skip: 100% foreign vs JV, which province, when to register."
        ),
        "paa": [
            "Can a foreigner start a business in Vietnam?",
            "What is the minimum capital to start a business in Vietnam?",
            "How long does it take to register a business in Vietnam?",
            "Do I need a Vietnamese partner to start a business in Vietnam?",
            "Can I be the legal representative of my own Vietnamese company?",
        ],
        "cluster": [
            "vietnam llc foreigner", "vietnam company registration",
            "vietnam investment registration certificate", "vietnam enterprise registration certificate",
            "irc erc vietnam", "vietnam minimum capital", "vietnam legal representative",
            "vietnam foreign ownership", "vietnam joint venture", "vietnam 100 percent foreign owned",
            "ho chi minh city business registration", "hanoi business registration",
            "vietnam representative office", "vietnam work permit", "vietnam business address",
            "vietnam e-id corporate", "vietnam tax registration", "vietnam vat invoice",
            "vietnam business license", "vietnam fdi", "vietnam business setup",
            "incorporate vietnam", "doing business vietnam", "vietnam expat business",
            "vietnam company formation", "vietnam banking foreign", "vietnam business address requirement",
            "vietnam regulated sectors", "vietnam company structure", "vietnam director residence",
        ],
        "outbound_extra": {
            "Vietnam Briefing": "https://www.vietnam-briefing.com/doing-business-guide/vietnam/company-establishment",
            "Emerhub": "https://emerhub.com/vietnam/how-to-start-a-business-in-vietnam-as-a-foreigner/",
        },
        "image_query_override": "vietnam business handshake meeting",
        "serp_insights": {
            "top_5_sources": [
                "Vietnam Briefing — Doing Business Guide: Company Establishment",
                "Emerhub — How to Start a Business in Vietnam as a Foreigner",
                "Racines Vietnam — Complete 2025 Expat Guide",
                "BBCIncorp — 2026 Update for Foreigners",
                "Acclime — Establishing a Company in Vietnam Quick Guide 2026",
            ],
            "competitor_format_notes": (
                "Archetype: incorporation-agent + law-firm content. All cover the same steps: "
                "LLC structure, IRC then ERC, ~$10K capital benchmark, 30-45 day timeline, legal "
                "representative requirement, business address. They differ in level of detail but "
                "share the assumption that the reader has already decided to incorporate. None "
                "discuss the strategic choices BEFORE registration: whether to incorporate at all, "
                "100% foreign vs JV, which province, when to register."
            ),
            "identified_gap": (
                "(1) Pre-incorporation question (validate first, then incorporate) never raised — "
                "agents have commercial incentive to push registration, (2) 100% foreign vs JV "
                "framed as legal choice not strategic choice, (3) Province selection treated as "
                "default to HCMC, (4) Legal representative requirement understated — actually a "
                "structural dependency, (5) Banking discipline (capital must be paid within 90 "
                "days) not flagged as the hard deadline, (6) Tax/invoice infrastructure treated "
                "as afterthought."
            ),
            "unique_angle": (
                "(1) Pre-incorporation question raised: validate market before committing to LLC. "
                "(2) 100% foreign vs JV framed by what Vietnamese partner brings (regulatory "
                "navigation, market access, labor relations) that foreign founders systematically "
                "undervalue. "
                "(3) Province choice framed by where business operates, not where founder wants "
                "to live. "
                "(4) Three things registration agents don't surface (legal rep dependency, banking "
                "discipline, tax/invoice infrastructure) named explicitly. "
                "(5) Connects to validate-business-idea staged validation as pre-incorporation step."
            ),
            "gap_opportunity": (
                "Canon is agent-incentivized 'how to register' content. OS Research adds the "
                "strategic questions a founder should answer BEFORE engaging an agent, plus the "
                "three structural realities agents don't surface."
            ),
        },
    },
    7: {
        "article_id": "OSR-2026-05-22-007",
        "primary_keyword": "fdi in vietnam",
        "pattern": "sector_ideas",
        "draft_file": "07-fdi-in-vietnam.md",
        "h1_for_schema": "FDI in Vietnam",
        "sv": 110,
        "kd": 0,
        "signal": 59.5,
        "title": "FDI in Vietnam: 2026 Market Report",
        "meta_description": (
            "Vietnam attracted $31.5B FDI in 10 months of 2025, 60% to manufacturing. "
            "The flows, the sources, the electronics concentration, and the semiconductor pivot."
        ),
        "paa": [
            "How much FDI does Vietnam receive each year?",
            "Which countries invest the most in Vietnam?",
            "What sectors get the most FDI in Vietnam?",
            "Why does so much FDI go to Vietnam?",
            "What are the risks to FDI in Vietnam?",
        ],
        "cluster": [
            "vietnam fdi 2025", "vietnam fdi 2026", "vietnam manufacturing fdi",
            "vietnam electronics fdi", "samsung vietnam", "intel vietnam",
            "foxconn vietnam", "lg vietnam", "bac ninh fdi", "hai phong fdi",
            "thai nguyen electronics", "china fdi vietnam", "singapore fdi vietnam",
            "hong kong fdi vietnam", "south korea fdi vietnam", "japan fdi vietnam",
            "vietnam semiconductor fdi", "vietnam industrial park", "vietnam special economic zone",
            "vietnam supply chain", "vietnam china plus one", "vietnam manufacturing exports",
            "vietnam tariff risk", "vietnam concentration risk", "vietnam economy",
            "vietnam industrial policy", "savills vietnam", "mekong capital",
            "vietnam ministry of planning", "vietnam fdi statistics",
        ],
        "outbound_extra": {
            "Vietnam Briefing": "https://www.vietnam-briefing.com/news/vietnam-economy-gdp-fdi-and-trade-2025.html/",
            "Savills": "https://www.savills.com.sg/blog/article/224618/vietnam-eng/new-manufacturing-fdi-breakdown-h1-2025.aspx",
        },
        "image_query_override": "industrial factory vietnam",
        "serp_insights": {
            "top_5_sources": [
                "Vietnam Briefing — Vietnam's Economy 2025 (GDP, FDI, Trade)",
                "VietnamPlus — FDI inflows: Manufacturing remains dominant",
                "Savills Singapore — Vietnam New Manufacturing FDI Breakdown H1/2025",
                "InCorp Vietnam — Top FDI Companies (Singapore, Korea, Taiwan leadership)",
                "RMIT University — Vietnam's electronics FDI: Growth without spillovers",
            ],
            "competitor_format_notes": (
                "Archetype: data-heavy reports from consultancies (Vietnam Briefing, Savills, "
                "InCorp) + government statistics aggregators. Most cover the headline FDI numbers, "
                "list source countries by capital amount, and break down manufacturing subsectors. "
                "RMIT raises the spillover question (foreign-invested firms don't transfer enough "
                "to domestic supply chain). Almost no source frames concentration risk explicitly "
                "or discusses what the semiconductor pivot will require to land."
            ),
            "identified_gap": (
                "(1) Concentration risk (Samsung ~20% of Vietnam exports in peak years) not "
                "discussed, (2) Geographic split (north electronics cluster vs south diversified) "
                "rarely surfaced as strategic detail, (3) China-as-#1-by-project-count framed as "
                "news but not as structural shift, (4) Semiconductor 50K-engineer target treated "
                "as ambition rather than the structural value-add-curve question, (5) Founder/B2B "
                "opportunity from FDI inflow (services to foreign-invested manufacturers) almost "
                "never named."
            ),
            "unique_angle": (
                "(1) FDI as both growth driver AND concentration risk — both framed honestly. "
                "(2) Geographic split: north electronics cluster vs south diversified mix with "
                "different growth dynamics. "
                "(3) Three structural factors for why Vietnam captured the share (adjacency, "
                "capacity, diplomatic positioning) named explicitly. "
                "(4) Semiconductor pivot framed as the value-add-curve question, with honest "
                "early-signs mixed read. "
                "(5) B2B founder opportunity from FDI customer base named — under-served by "
                "Vietnamese companies."
            ),
            "gap_opportunity": (
                "Canon presents FDI as a celebrated number. OS Research provides the structural "
                "read: where the money lands geographically, the concentration risk it produces, "
                "and the founder/investor implications of serving a foreign-invested customer base."
            ),
        },
    },
    6: {
        "article_id": "OSR-2026-05-22-006",
        "primary_keyword": "why vietnam economy is booming",
        "pattern": "sector_ideas",
        "draft_file": "06-why-vietnam-economy-is-booming.md",
        "h1_for_schema": "Why Vietnam Economy Is Booming",
        "sv": 70,
        "kd": 5,
        "signal": 50.2,
        "title": "Why the Vietnam Economy Is Booming (2026)",
        "meta_description": (
            "Vietnam's economy grew 8.02 percent in 2025. The three structural drivers behind "
            "the boom, what is durable, what is cyclical, and the honest counter-read."
        ),
        "paa": [
            "Why is the Vietnamese economy growing so fast?",
            "How long will the Vietnam economy boom continue?",
            "Is Vietnam the next China?",
            "What sectors are driving Vietnam's growth?",
            "What are the risks to Vietnam's continued growth?",
        ],
        "cluster": [
            "vietnam gdp growth", "vietnam gdp 2025", "vietnam economy 2026",
            "vietnam supply chain", "vietnam manufacturing", "vietnam electronics",
            "vietnam middle class", "vietnam upper middle income", "vietnam fdi",
            "vietnam fintech", "samsung vietnam", "intel vietnam", "foxconn vietnam",
            "vietnam tariff", "vietnam us trade", "vietnam consumer market",
            "vietnam exports", "vietnam semiconductor", "vietnam industrial policy",
            "vietnam infrastructure", "north south expressway", "vietnam port investment",
            "vietnam demographic dividend", "vietnam urbanization", "vietnam consumer software",
            "vietnam unicorns", "vietnam venture capital", "vietnam ecommerce",
            "vietnam digital economy", "vietnam two-speed economy",
        ],
        "outbound_extra": {
            "World Bank": "https://www.worldbank.org/en/country/vietnam",
            "Tradingeconomics": "https://tradingeconomics.com/vietnam/gdp-growth-annual",
        },
        "image_query_override": "vietnam factory worker",
        "serp_insights": {
            "top_5_sources": [
                "World Bank Viet Nam — country overview",
                "Trading Economics — Vietnam GDP Annual Growth Rate",
                "VietnamNet — 2025 surge + 2026 double-digit target",
                "Vietnam Briefing — Vietnam's economy in 2025",
                "TheInvestor.vn — WB 6.3% projection for 2026",
            ],
            "competitor_format_notes": (
                "Archetype: news-cycle articles celebrating the 8% number + government targets + "
                "consultancy reports. Most coverage lists drivers (FDI, exports, consumer demand) "
                "without weighting durability. Tariff risk usually mentioned in last paragraph. "
                "Two-speed economy never named. Almost no source separates cyclical from durable "
                "drivers explicitly."
            ),
            "identified_gap": (
                "(1) Drivers listed without durability weighting — readers can't tell which to "
                "underwrite, (2) Supply chain rearrangement framed as Vietnam-specific instead of "
                "structural China rearrangement landing in Vietnam, (3) Middle-class threshold "
                "($5K per capita changing consumer math) almost never named explicitly, "
                "(4) Concentration risk in electronics under-discussed, (5) Semiconductor policy "
                "treated as ambition rather than structural bet, (6) Two-speed economy (urban "
                "upper-middle vs rural lower-middle) absent from most narratives."
            ),
            "unique_angle": (
                "(1) Three named drivers with durability ratings: middle class compound (most "
                "durable), supply chain (cyclical), policy (baseline). "
                "(2) Honest counter-read that 8% is unlikely to repeat at full strength each year. "
                "(3) Explicit founder + investor implications based on driver mix. "
                "(4) Middle-class $5K threshold framed as the consumer math pivot. "
                "(5) Direct quote of forecast spread (WB 6.3% vs gov 10%) as central question."
            ),
            "gap_opportunity": (
                "Canon celebrates the boom without separating durable from cyclical drivers. OS "
                "Research provides the structural read on which forces compound and which fade, "
                "and what each means for builders and investors in 2026."
            ),
        },
    },
    5: {
        "article_id": "OSR-2026-05-22-005",
        "primary_keyword": "vietnam economy",
        "pattern": "sector_ideas",
        "draft_file": "05-vietnam-economy.md",
        "h1_for_schema": "Vietnam Economy",
        "sv": 2900,
        "kd": 17,
        "signal": 63.2,
        "title": "Vietnam Economy: 2026 Market Report",
        "meta_description": (
            "Vietnam's GDP grew 8.02 percent in 2025. The 2026 forecast splits 6.3 vs 10. "
            "The two-speed economy underneath the headline and what it means for operators."
        ),
        "paa": [
            "What is Vietnam's GDP in 2025?",
            "What is Vietnam's GDP growth forecast for 2026?",
            "Is Vietnam still a developing economy?",
            "Why is the Vietnamese economy growing so fast?",
            "What are the biggest risks to Vietnam's economy?",
        ],
        "cluster": [
            "vietnam gdp 2025", "vietnam gdp per capita", "vietnam gdp growth",
            "vietnam economy 2026", "vietnam fdi", "vietnam manufacturing",
            "vietnam electronics exports", "samsung vietnam", "intel vietnam",
            "foxconn vietnam", "vietnam middle class", "vietnam upper middle income",
            "vietnam world bank forecast", "vietnam hsbc forecast", "vietnam uob forecast",
            "vietnam tariff risk", "vietnam supply chain", "bac ninh electronics",
            "vietnam fintech", "vietnam consumer economy", "vietnam services sector",
            "vietnam agriculture", "vietnam semiconductor", "vietnam digital economy",
            "vietnam unicorns", "vietnam venture capital", "vietnam two-speed economy",
            "vietnam rural urban gap", "vietnam ecommerce", "vietnam exports",
        ],
        "outbound_extra": {
            "World Bank": "https://www.worldbank.org/en/news/press-release/2025/03/12/viet-nam-s-economy-forecast-to-grow-6-8-percent-in-2025-wb",
            "UOB": "https://vietnamnet.vn/en/uob-raises-vietnam-s-2026-gdp-growth-forecast-to-7-5-2480609.html",
        },
        "image_query_override": "vietnam skyline hanoi",
        "serp_insights": {
            "top_5_sources": [
                "World Bank — Viet Nam Economic Update (March 2025, 6.8% 2025 forecast)",
                "Trading Economics — Vietnam GDP Annual Growth Rate (8.02% confirmed)",
                "VietnamNet — Government 10% 2026 target + UOB 7.5%",
                "Vietnam Briefing — Vietnam's Economy 2025: GDP, FDI, Trade",
                "TheInvestor.vn — WB projects Vietnam GDP 6.3% in 2026",
            ],
            "competitor_format_notes": (
                "Archetype: news-style updates citing official 2025 figures + forecast roundups. "
                "World Bank and Vietnam Briefing go data-deep. VietnamNet aggregates "
                "government targets and bank forecasts. No source consistently surfaces the "
                "gap between domestic 10% target and international 6.3-7.5% range as the "
                "structural story. Tariff risk and two-speed economy framing under-discussed."
            ),
            "identified_gap": (
                "(1) Forecast spread (6.3 vs 10%) not framed as the central question, "
                "(2) Two-speed economy (urban upper-middle vs rural lower-middle) almost never "
                "named, (3) Electronics concentration risk under-discussed, (4) Connection "
                "between FDI surge + middle-class compounding + fintech maturation rarely "
                "made explicit, (5) Operator/investor implications absent — most pieces are "
                "macro reports with no founder lens, (6) Semiconductor 50K-engineer target "
                "treated as ambition not as structural pivot."
            ),
            "unique_angle": (
                "(1) Forecast spread (6.3% WB vs 10% government) named as the central read. "
                "(2) Two-speed economy framing: urban consumer software works, rural does not. "
                "(3) Honest electronics-concentration risk: GDP increasingly depends on a "
                "handful of foreign-invested firms. "
                "(4) Operator and investor implications stated explicitly: validation discipline "
                "+ stage-gated picks > broad-market exposure. "
                "(5) Specific 2025/2026 actuals (GDP $514B, per capita $5,026, FDI $31.5B 10mo, "
                "fintech $3.42B → $7.78B by 2030) anchor the read."
            ),
            "gap_opportunity": (
                "Canon presents macro numbers without the operator lens. OS Research provides "
                "the founder/investor read on what the two-speed structure means for where to "
                "build and where to allocate."
            ),
        },
    },
    4: {
        "article_id": "OSR-2026-05-22-004",
        "primary_keyword": "vietnam unicorns",
        "pattern": "sector_ideas",
        "draft_file": "04-vietnam-unicorns.md",
        "h1_for_schema": "Vietnam Unicorns",
        "sv": 260,
        "kd": 0,
        "signal": 54.0,
        "title": "Vietnam Unicorns: 2026 Market Report",
        "meta_description": (
            "Vietnam has six unicorns in 2026. The pattern behind them, the four fintech "
            "founders driving the count, and what the next three by 2030 will need."
        ),
        "paa": [
            "How many unicorns does Vietnam have?",
            "Which companies are Vietnam's unicorns?",
            "When did Vietnam get its first unicorn?",
            "What sectors do Vietnam's unicorns operate in?",
            "Will Vietnam have more unicorns by 2030?",
        ],
        "cluster": [
            "vng valuation", "sky mavis axie infinity", "momo fintech vietnam",
            "vnpay valuation", "tiki vietnam", "vnlife", "vietnam tech ecosystem",
            "ho chi minh city startups", "hanoi startups", "southeast asia unicorns",
            "vietnam fintech", "vietnam gaming", "vietnam ecommerce",
            "andreessen horowitz vietnam", "mizuho momo", "tracxn vietnam",
            "vietnam venture capital", "vietnam startup funding", "vietnam digital economy",
            "super app vietnam", "qr payment vietnam", "axie infinity blockchain",
            "blockchain gaming", "vietnam soonicorn", "vietnam startup ecosystem",
            "vietnam middle class", "vietnam consumer economy", "momo super app",
            "vietnam digital payments", "vietnam mobile internet",
        ],
        "outbound_extra": {
            "Tracxn": "https://tracxn.com/d/unicorns/unicorns-in-vietnam",
            "Andreessen Horowitz": "https://a16z.com/",
        },
        "serp_insights": {
            "top_5_sources": [
                "Tracxn — Unicorn startups in Vietnam (May 2026)",
                "AsiaTechDaily — Vietnam's Startup Ecosystem Tops $3.2B, Six Unicorns",
                "Tatler Asia — Inside the minds behind Vietnam's tech unicorns",
                "Vietcetera — MoMo Hits $2 Billion Valuation",
                "Vietnam.vn / VietnamNet — Government 2030 unicorn target",
            ],
            "competitor_format_notes": (
                "Archetype: Tracxn-style lists + biographical/founder profiles + government "
                "target articles. Most sources list the six unicorns with valuations and "
                "Series details, then add 1-2 paragraphs of founder background. Vietcetera "
                "and TatlerAsia go deeper on individuals. Tracxn focuses on numbers. "
                "Almost no source connects the four-fintech ratio to the underlying "
                "payments-infrastructure gap, and none give honest analysis of which "
                "valuations have moved post-2022 correction."
            ),
            "identified_gap": (
                "(1) No source explains WHY four of six are fintech (structural payments gap), "
                "(2) Sky Mavis valuation cycle post-2022 underplayed or omitted, "
                "(3) VNLIFE vs VNPAY treated as distinct unicorns without acknowledging the "
                "parent-subsidiary relationship and counting convention, "
                "(4) No analysis of what the next wave (3-4 by 2030) will actually need, "
                "(5) Tiki's e-commerce position vs Shopee/Lazada under-discussed."
            ),
            "unique_angle": (
                "(1) Each unicorn analyzed as a blue-ocean play in a category that looked "
                "saturated. "
                "(2) Honest read on the fintech concentration as structural (Vietnam's "
                "payment infrastructure gap during 2015-2022) and now closing. "
                "(3) Direct contrast between MoMo (consumer brand first) and VNPAY (rails "
                "first) as two valid plays on the same inefficiency. "
                "(4) Acknowledges Sky Mavis's post-peak valuation correction without "
                "discrediting the demonstration effect. "
                "(5) Names the sectoral candidates for the next 3-4 unicorns (lending, "
                "insurance, healthtech, edtech, agri supply chain) and why the wedge will "
                "differ from the first wave."
            ),
            "gap_opportunity": (
                "Canon is biographical lists + valuation snapshots. OS Research provides "
                "the structural read of WHY Vietnam's unicorn mix is fintech-heavy, what "
                "the next wedge looks like, and honest valuation-cycle commentary."
            ),
        },
    },
    3: {
        "article_id": "OSR-2026-05-22-003",
        "primary_keyword": "north star metric",
        "pattern": "framework_example",
        "draft_file": "03-north-star-metric.md",
        "h1_for_schema": "North Star Metric",
        "sv": 590,
        "kd": 12,
        "signal": 58.5,
        "title": "North Star Metric: Complete Guide (2026)",
        "image_query_override": "compass night sky",
        "meta_description": (
            "A north star metric is the leading indicator that captures customer value. "
            "The four-question test we use at OS Research to pick one that actually predicts revenue."
        ),
        "paa": [
            "What is a north star metric?",
            "How do you choose a north star metric?",
            "What is the difference between a north star metric and a KPI?",
            "Can a company have more than one north star metric?",
            "What are some examples of north star metrics?",
        ],
        "cluster": [
            "north star framework", "leading indicator", "lagging indicator",
            "key performance indicator", "kpi", "amplitude north star",
            "sean ellis north star", "product analytics", "vanity metric",
            "actionable metric", "engagement metric", "retention metric",
            "monthly active users", "weekly active users", "daily active users",
            "mrr", "arr", "customer lifetime value", "aha moment",
            "input metric", "output metric", "north star metric saas",
            "slack north star metric", "airbnb nights booked",
            "spotify time listening", "north star metric examples",
            "north star metric framework", "product market fit",
            "validated learning", "okrs",
        ],
        "outbound_extra": {
            "Amplitude": "https://amplitude.com/blog/product-north-star-metric",
            "Reforge": "https://www.reforge.com/blog/north-star-metrics",
        },
        "serp_insights": {
            "top_5_sources": [
                "Amplitude — Every Product Needs a North Star Metric",
                "Reforge — How to Choose & Measure NSM (Acquisition, Retention, Monetization)",
                "Userpilot — How to Find Yours & Measure Progress + Examples",
                "UserGuiding — Complete Guide to North Star Metrics for SaaS",
                "Sean Ellis / GrowthHackers — origin of the term",
            ],
            "competitor_format_notes": (
                "Archetype: Amplitude's 3-game framework (Attention/Transaction/Productivity) + "
                "list of canonical examples (Slack, Airbnb, Spotify, HubSpot, Netflix). Userpilot, "
                "UserGuiding, CXL repeat the framing with longer example lists. Reforge segments by "
                "Acquisition/Retention/Monetization with deeper analytics but still treats NSM as a "
                "tracking dashboard rather than an experiment artifact."
            ),
            "identified_gap": (
                "Across all canonical sources: (1) no falsifiability framework — how do you "
                "DISPROVE a NSM choice?, (2) no quantitative thresholds — what growth rate counts?, "
                "(3) no A/B testing methodology for competing NSM candidates, (4) no failure case "
                "studies (companies that chose wrong NSM + consequences), (5) vague input "
                "methodology ('breadth, depth, frequency, efficiency' lacks application steps), "
                "(6) 'when to pivot NSM' mentioned but never elaborated, (7) early-stage vs scale-up "
                "treated identically — all assume product analytics + traffic exist."
            ),
            "unique_angle": (
                "(1) Four-question test before adoption: value moment named, falsification "
                "condition stated, stage-explicit, movable in a quarter. "
                "(2) Stage-gated NSM: pre-PMF NSM (hypothesis) vs post-PMF NSM (operating compass) "
                "with explicit successor. "
                "(3) Worked example: picking NSM for early-stage Vietnam vertical SaaS (dental "
                "scheduling) showing why textbook 'WAU' fails the test. "
                "(4) Failure-pattern taxonomy: picking from list, lagging-in-leading-disguise, "
                "stage drift, multiple competing NSMs, skipped falsification. "
                "(5) Direct contrast: 'canon teaches tracking, we treat NSM as a validation "
                "artifact'."
            ),
            "paa_dup": True,  # mirrors PAA above
            "gap_opportunity": (
                "Canon treats NSM as a tracking dashboard. OS Research treats it as a falsifiable "
                "claim about how the business works, with stage gating and a four-question adoption "
                "test the canon lacks."
            ),
        },
    },
}
