"""
Fresh Phase 1 articles for keywords without v4 drafts.

Currently: 2 articles
  - venture capital vietnam  (sector_ideas, vn_vc, signal 68.4)
  - vietnam market           (sector_ideas, vn_vc, signal 64.2)

Each entry has the same shape as v4_content.ARTICLES, so the pipeline can
treat them identically.
"""
from __future__ import annotations


FRESH_ARTICLES = [
    # ============================================================
    # F-001 — venture capital vietnam  (vn_vc, sector_ideas)
    # Updated 2026-05 with 2025 actuals from VinVentures + Do Ventures reports
    # ============================================================
    {
        "primary_keyword": "venture capital vietnam",
        "pattern": "sector_ideas",
        "tldr_answer": (
            "Venture capital in Vietnam fell to USD 215 million across 41 deals in 2025, "
            "the fifth consecutive year of decline. The top 10 rounds captured 73 percent of "
            "total capital (USD 154 million), signalling a shift to fewer, larger Series A and "
            "B+ bets. Four homegrown unicorns (VNG, VNLife, MoMo, Sky Mavis), 50 plus active "
            "funds, and fintech, ecommerce, and AI still dominate the deal flow."
        ),
        "identified_gap": (
            "Top SERP (Vietnam Briefing, PitchBook, Tracxn, CB Insights, Wikipedia VC list) "
            "covers funds and headline deals but misses:\n"
            "- Honest read on capital efficiency vs Indonesia/Singapore comparables\n"
            "- What founders actually experience when raising locally vs cross-border\n"
            "- Why 2023-2024 contraction is structural, not cyclical\n"
            "- The validation-stage gap (early-stage capital deeper than growth-stage)"
        ),
        "competitor_format_notes": (
            "Real SERP (2026-05): Vietnam Briefing (overview), PitchBook (deal data), "
            "Tracxn (fund tracker), CB Insights (sector splits), Genesia Ventures blog "
            "(operator POV), Wikipedia (canonical fund list). Format: market overview + "
            "fund roster + sector breakdown. None of them tie data back to what a Vietnamese "
            "founder should do differently. OSR opening: a validation-economics read."
        ),
        "unique_angle": (
            "- Frame Vietnam VC as 'deep early-stage, thin growth-stage' market\n"
            "- Show why the 2024 deal-count holds while ticket sizes fall (correct read)\n"
            "- OS Research methodology: TRR thresholds for pre-seed vs seed in Vietnam"
        ),
        "article_body_md": """<aside className="tldr">
**TL;DR.** Venture capital in Vietnam fell to USD 215 million across 41 deals in 2025, the fifth consecutive year of decline. The top 10 rounds captured 73 percent of total capital (USD 154 million), signalling a shift to fewer, larger Series A and B+ bets. Four homegrown unicorns (VNG, VNLife, MoMo, Sky Mavis), 50 plus active funds, and fintech, ecommerce, and AI still dominate the deal flow.
</aside>

## What is venture capital in Vietnam?

Venture capital in Vietnam is the private equity capital deployed into early- and growth-stage Vietnamese startups by professional investment firms. The market matured rapidly between 2017 and 2022, peaking at USD 2.6 billion in 2021 before correcting alongside global VC compression. Capital comes from a mix of regional funds (500 Global, Antler, Genesia Ventures), corporate venture arms (VNG Ventures, Viettel Ventures, Vingroup Ventures), and local funds (VinaCapital Ventures, Mekong Capital, ESP Capital, Do Ventures, Touchstone Partners).

## Market size and deal flow

The 2025 numbers from the VinVentures "Vietnam Tech and Venture Capital Outlook 2025" plus the Do Ventures and NIC "Vietnam Innovation and Private Capital Report 2025":

- **Total capital deployed:** USD 215 million (down 59 percent from 2024's USD 529 million)
- **Deal count:** 41 transactions (down 55 percent year-on-year from 92)
- **Top 10 deals concentration:** USD 154 million, or 73 percent of total capital
- **Largest disclosed rounds in 2025:** Coolmate (USD 22.34 million, Series B+), Manabie (USD 22.26 million, Series A), Dat Bike (USD 22 million, Series B+)
- **Decline streak:** five consecutive years from the 2021 peak
- **Stage shift:** capital concentrating in Series A and B+ rounds of USD 5 to 10 million plus; pre-seed and seed activity continues but check sizes shrank

For context, 2021 was the peak: USD 2.6 billion across 165 deals, fuelled by the global zero-rate boom. The 2025 floor sits at roughly 8 percent of that peak. The decline is structural (investor risk reset, exit market closed) more than cyclical, though state-fund initiatives announced in early 2026 may shift the picture.

## The four unicorns

- **VNG** (gaming and Zalo messaging, valued at USD 2.2 billion at last reported round)
- **VNLife** / VNPay (payment infrastructure, USD 1 billion valuation, 2021)
- **MoMo** (consumer wallet, USD 2 billion valuation, 2021)
- **Sky Mavis** (Axie Infinity, USD 3 billion valuation at 2021 peak; current valuation undisclosed and likely materially lower)

No new unicorn has been minted since 2021. The pipeline candidates (Tiki, Sendo, Loship, Vntrip) have all either pulled back, been acquired, or remained below USD 500 million valuations.

## Where capital actually goes

Sector breakdown of 2024 deployed capital:

| Sector | Share | Notable rounds |
|---|---|---|
| Fintech | 31% | Finhay, Infina, Timo |
| Ecommerce and retail tech | 22% | Loship, OnPoint, OkXe |
| AI and SaaS | 17% | Trusting Social, FPT.AI, Got It |
| Education | 8% | Marathon Education, Edupia |
| Health | 7% | eDoctor, Med247 |
| Logistics and mobility | 6% | Ahamove, Be Group |
| Other | 9% | — |

The fintech and ecommerce concentration reflects where Vietnam's digital adoption curve is steepest, but it also means narrow exit comparables for new founders outside those categories.

## Active funds founders should know

Local funds (writing seed to Series A in Vietnam-headquartered companies):

- **VinaCapital Ventures** — generalist, USD 100 million fund III
- **Do Ventures** — USD 50 million focus fund, early stage
- **ESP Capital** — seed and Series A, fintech and consumer
- **Touchstone Partners** — seed, deep-tech leaning
- **500 Global Vietnam** — pre-seed and seed accelerator pipeline
- **Genesia Ventures** — regional, with active Vietnam exposure
- **Mekong Capital** — growth stage, consumer brands track record

Regional funds with regular Vietnam check-writing: Sequoia Capital India, East Ventures, Insignia Ventures, Openspace Ventures, Northstar Group, KKR (selective), AC Ventures, Wavemaker Partners.

Corporate venture arms: VNG Ventures, Viettel Ventures, FPT Ventures, Vingroup Ventures (Vinasun, VinFast, VinaPhone), Masan Ventures.

## The capital efficiency picture vs comparables

A USD 1 million seed round in Vietnam typically buys 18 to 24 months of runway for a 6 to 10 person team. The same round in Singapore or Jakarta buys 9 to 14 months. Vietnamese founders also benefit from a deep, technical talent pool at roughly 40 to 60 percent of Singapore engineering salaries.

The flip side: growth-stage capital is materially thinner. Series A rounds above USD 5 million regularly require cross-border investors (Korean, Japanese, US), which adds 4 to 8 weeks of process time and currency, governance, and IP routing complexity. Vietnamese founders raising above USD 10 million almost always need to flip to a Singapore or Cayman holding structure.

## What this means for founders

For founders deciding when to raise in Vietnam:

1. **Pre-seed under USD 500K**: highly fundable from local angels, accelerators (500 Global, Antler, Genesia), and emerging micro-funds. Validation evidence (TRR Problem Fit threshold) matters more than pedigree.
2. **Seed USD 500K to USD 2 million**: still local-fund-friendly. Need clear unit economics or a defensible early-stage commercial signal.
3. **Series A USD 2 to 8 million**: bridge zone. Most local funds participate but rarely lead at this size. Plan for at least one regional or international lead.
4. **Series B and beyond**: cross-border or strategic capital only. Restructure to Singapore parent before starting the process.

## Frequently asked questions

**Q: How big is the venture capital market in Vietnam in 2025?**
A: USD 215 million across 41 deals in 2025, the fifth consecutive year of decline from the 2021 peak of USD 2.6 billion. The top 10 deals captured USD 154 million, or 73 percent of total capital.

**Q: Who are the top VC firms in Vietnam?**
A: Local leaders include VinaCapital Ventures, Do Ventures, ESP Capital, Touchstone Partners, 500 Global Vietnam, and Genesia Ventures. Active regional funds include Sequoia India, East Ventures, Insignia Ventures, and Openspace.

**Q: What were the largest VC deals in Vietnam in 2025?**
A: Coolmate (USD 22.34 million, Series B+) led, followed by Manabie (USD 22.26 million, Series A) and Dat Bike (USD 22 million, Series B+). The concentration in the top 10 reflects investors favouring proven, scalable businesses over early-stage bets.

**Q: How many unicorns does Vietnam have?**
A: Four, VNG, VNLife (VNPay), MoMo, and Sky Mavis. No new unicorn has been minted since 2021.

**Q: What sectors get the most VC funding in Vietnam?**
A: Fintech and ecommerce remain the top categories. AI and SaaS continue to grow as a share of deployed capital. Education, health, and logistics each take 6 to 8 percent.

**Q: Is it easier to raise venture capital in Vietnam compared to Singapore?**
A: For pre-seed and seed often yes, local funds and capital efficiency favour Vietnamese founders. For Series A and above harder, fewer growth-stage cheque-writers, often requiring cross-border investors.

**Q: Has venture capital in Vietnam recovered from the 2022 correction?**
A: No. 2025 deployed capital is roughly 8 percent of the 2021 peak and the fifth straight year of decline. The drop is structural (investor risk reset, closed exit market), though state-fund initiatives announced in early 2026 may shift the trajectory.
""",
        "faq_block_json": """[
{"question": "How big is the venture capital market in Vietnam in 2025?", "answer": "USD 215 million across 41 deals in 2025, the fifth consecutive year of decline from the 2021 peak of USD 2.6 billion. The top 10 deals captured 73 percent of total capital."},
{"question": "Who are the top VC firms in Vietnam?", "answer": "Local leaders include VinaCapital Ventures, Do Ventures, ESP Capital, Touchstone Partners, 500 Global Vietnam, and Genesia Ventures. Active regional funds include Sequoia India, East Ventures, Insignia Ventures, and Openspace."},
{"question": "What were the largest VC deals in Vietnam in 2025?", "answer": "Coolmate (USD 22.34 million, Series B+) led, followed by Manabie (USD 22.26 million, Series A) and Dat Bike (USD 22 million, Series B+)."},
{"question": "How many unicorns does Vietnam have?", "answer": "Four, VNG, VNLife (VNPay), MoMo, and Sky Mavis. No new unicorn has been minted since 2021."},
{"question": "What sectors get the most VC funding in Vietnam?", "answer": "Fintech and ecommerce remain the top categories. AI and SaaS continue to grow as a share of deployed capital. Education, health, and logistics each take 6 to 8 percent."},
{"question": "Is it easier to raise venture capital in Vietnam compared to Singapore?", "answer": "For pre-seed and seed often yes, local funds and capital efficiency favour Vietnamese founders. For Series A and above harder, fewer growth-stage cheque-writers, often requiring cross-border investors."},
{"question": "Has venture capital in Vietnam recovered from the 2022 correction?", "answer": "No. 2025 deployed capital is roughly 8 percent of the 2021 peak and the fifth straight year of decline. State-fund initiatives announced in early 2026 may shift the trajectory."}
]""",
        "source_citations": (
            "- VinVentures: Vietnam Tech and Venture Capital Outlook 2025\n"
            "- Do Ventures + NIC: Vietnam Innovation and Private Capital Report 2025\n"
            "- VnEconomy: Vietnam venture capital investment declines for fifth consecutive year (Mar 2026)\n"
            "- The Investor: 10 top-funded startups in Vietnam in 2025\n"
            "- Vietnam Briefing: Venture capital landscape in Vietnam\n"
            "- PitchBook: Vietnam VC market data\n"
            "- Tracxn: Vietnam startup funding tracker"
        ),
    },

    # ============================================================
    # F-002 — vietnam market  (vn_vc, sector_ideas)
    # Updated 2026-05 with 2025 actuals from GSO + OECD + Vietnam Briefing
    # ============================================================
    {
        "primary_keyword": "vietnam market",
        "pattern": "sector_ideas",
        "tldr_answer": (
            "Vietnam is a USD 514 billion economy with 100 million people, growing 8.02 percent "
            "in 2025, one of the highest rates in nearly three decades and well above the 6.5 "
            "percent forecast. FDI disbursed hit USD 27.6 billion (highest in five years), total "
            "trade crossed USD 930 billion, and manufacturing absorbed 57 percent of new "
            "investment. Ecommerce, fintech, and renewables stay the fastest-growing sectors "
            "heading into 2026."
        ),
        "identified_gap": (
            "Top SERP (World Bank, IMF, Vietnam Briefing, McKinsey, Statista, Investopedia) "
            "covers macro and headline sectors but misses:\n"
            "- An honest operator-level read of consumer buying power vs sticker GDP\n"
            "- Where the 'fastest-growing in Asia' narrative is true vs marketing\n"
            "- The two-speed economy reality: HCMC and Hanoi vs the other 61 provinces\n"
            "- Strategic implications for founders and global VCs entering"
        ),
        "competitor_format_notes": (
            "Real SERP (2026-05): World Bank country profile, IMF Article IV, Vietnam Briefing "
            "(operator focus), Statista (data charts), McKinsey (consumer report), Investopedia "
            "(intro), HSBC and Standard Chartered research notes. Format: macro overview + "
            "sector list + outlook. Lacks: actionable framing for builders and investors."
        ),
        "unique_angle": (
            "- Frame Vietnam as a 'manufacturing + middle-class compounding' story\n"
            "- Highlight the two-speed economy honestly (urban vs rural divergence)\n"
            "- OS Research lens: validation-friendly market for founders, but exit thin"
        ),
        "article_body_md": """<aside className="tldr">
**TL;DR.** Vietnam is a USD 514 billion economy with 100 million people, growing 8.02 percent in 2025, one of the highest rates in nearly three decades and well above the 6.5 percent forecast. FDI disbursed hit USD 27.6 billion (highest in five years), total trade crossed USD 930 billion, and manufacturing absorbed 57 percent of new investment. Ecommerce, fintech, and renewables stay the fastest-growing sectors heading into 2026.
</aside>

## What is the Vietnam market?

The Vietnam market refers to the combined consumer, industrial, and capital opportunity inside a country that, as of 2025, is the 33rd largest economy in the world by nominal GDP (USD 514 billion) and roughly the 24th largest by purchasing power parity (USD 1.6 trillion). It is the third most populous country in Southeast Asia after Indonesia and the Philippines, the fastest-urbanising country in ASEAN, and the largest non-Chinese manufacturing alternative for Western brands diversifying supply chains.

## Headline numbers as of 2025

- **GDP (nominal):** USD 514 billion (General Statistics Office 2025 estimate, up roughly USD 38 billion from 2024)
- **GDP per capita:** about USD 5,100 (low middle-income band)
- **Real GDP growth:** 8.02 percent in 2025 (vs 6.1 percent in 2024), one of the highest rates in nearly three decades
- **Sectoral growth:** industry and construction 8.95 percent, services 7+ percent and 51 percent of GDP
- **Population:** 100.3 million; median age 33; urbanisation 39 percent
- **Trade:** USD 930 billion total goods trade in 2025; trade surplus USD 20 billion (despite new US tariffs)
- **FDI disbursed:** USD 27.6 billion in 2025 (+9 percent year-on-year, highest in five years)
- **FDI newly registered:** USD 38.4 billion in 2025 (+0.5 percent YoY); manufacturing absorbed USD 9.8 billion (57 percent of new capital)
- **Inflation:** 3.31 percent (low, allowing supportive monetary policy)
- **Fiscal deficit:** roughly 3.8 percent of GDP

For context, Vietnam crossed the USD 100 billion GDP threshold in 2007, USD 200 billion in 2015, and USD 400 billion in 2023. The 2025 jump past USD 500 billion came faster than forecasters predicted. Vietnam remains second only to India among Asian economies above USD 200 billion for sustained compounding growth.

## The two-speed economy

The headline GDP number masks a steep urban-rural divergence:

- **Ho Chi Minh City** (population 9.4 million) and **Hanoi** (population 8.6 million) together account for roughly 32 percent of national GDP. Per-capita income in HCMC's central districts crosses USD 9,000 — middle-income consumer behaviour at scale.
- The **other 61 provinces** average USD 3,200 GDP per capita. Behaviour is largely value-tier, cash-based, and informal-economy heavy.

This matters for any business sizing a Vietnam opportunity: the addressable middle-class market is roughly 25 to 30 million people, not 100 million. McKinsey's "Consumer Sentiment Vietnam 2025" identifies 17 million households as "consuming class" by 2030, up from 12 million today — the compounding curve, not the absolute number, is the story.

## Sector breakdown of GDP

| Sector | Share of GDP | 2024 growth | Notes |
|---|---|---|---|
| Services | 42% | 7.4% | Retail, finance, tourism, logistics |
| Industry and construction | 37% | 7.9% | Manufacturing the bulk; electronics 17% of total exports |
| Agriculture, forestry, fisheries | 12% | 3.3% | Coffee no. 2 globally, rice no. 3, seafood no. 4 |
| Mining and other | 9% | 1.1% | Oil and gas declining; renewables rising |

## Key sectors for the next 5 years

**Manufacturing and electronics.** Samsung produces roughly half of its global smartphone output in Vietnam (Bac Ninh and Thai Nguyen plants). Foxconn, Pegatron, Intel, Amkor, and Marvell have all expanded since 2022. The 2023 Comprehensive Strategic Partnership with the US accelerated the chip-packaging investment trajectory.

**Ecommerce.** Total GMV reached USD 22 billion in 2024 (up 25 percent year-on-year), making Vietnam the fastest-growing ecommerce market in Southeast Asia. Shopee (40 percent share), TikTok Shop (29 percent), Lazada (18 percent), and Tiki (8 percent) dominate. The category is no longer "emerging" — it is operationally mature.

**Fintech.** 70 percent of adults now have a bank account (up from 31 percent in 2017). MoMo and VNPay dominate consumer wallets. Buy-now-pay-later (BNPL) and embedded finance are the active 2025-2026 frontiers.

**Renewables and energy transition.** Power Development Plan 8 (PDP8) targets 50 percent renewables in the grid by 2030. Wind, solar, and LNG investments accelerated through 2024 and 2025.

**Logistics and supply chain.** A consequence of the manufacturing build-out, not a separate trend. Bonded warehouses, 3PL platforms, and last-mile delivery are all expanding 18 to 25 percent annually.

## Consumer profile

The Vietnamese consumer of 2025 is young (median age 33), digitally native (78 percent smartphone penetration, 79 percent of population on social media), and price-sensitive but increasingly willing to trade up on quality once a brand earns trust. Mobile-first commerce dominates: 82 percent of ecommerce GMV completes on mobile.

What sells well: skincare and beauty (premiumisation), F&B and quick-service restaurants (urban expansion), education and English-learning apps (status-driven), and home and personal finance services (the new middle class).

What underperforms vs Western expectations: subscription SaaS (B2B procurement cycles are 6 to 12 months), premium luxury (small absolute base), traditional automotive (VinFast and Chinese EV brands disrupting the segment).

## FDI as a barometer

Foreign direct investment is the cleanest single signal for Vietnam-as-market sentiment. The nine-year run above USD 19 billion in disbursed capital, with 2025 hitting USD 27.6 billion (the highest in five years), reflects a stable and intensifying thesis: low-cost, geopolitically advantageous, infrastructure-improving manufacturing base. Korean and Singaporean capital lead by source; the US, Taiwan, and Japan follow.

The 2025 newly registered FDI mix shifted toward manufacturing again (57 percent or USD 9.8 billion, up from 58 percent in 2024) as supply-chain diversification accelerated under US tariff pressure. Real estate and renewable energy continue absorbing capital alongside.

## Risks to the thesis

- **Currency pressure:** the dong weakened 5 percent against the USD in 2024. The SBV manages a narrow band but has limited reserves to defend.
- **Demographic peak:** the working-age population peaks around 2032. The current demographic dividend is a 7 to 8 year tailwind, not permanent.
- **Talent inflation:** engineering salaries in Hanoi and HCMC have risen 35 to 50 percent since 2020, narrowing the cost advantage vs the Philippines and India.
- **Regulatory:** data sovereignty rules tightened in 2024; some cross-border services now require local data residency.

## Frequently asked questions

**Q: How big is the Vietnam economy?**
A: USD 514 billion nominal GDP in 2025 (up from USD 470 billion in 2024), roughly USD 1.6 trillion in purchasing power parity. The 33rd largest economy globally and the third largest in Southeast Asia.

**Q: What is the Vietnam GDP growth rate in 2025?**
A: 8.02 percent in 2025, one of the highest in nearly three decades and well above the 6.5 percent that most forecasters projected. Industry and construction led at 8.95 percent; services held 51 percent of GDP.

**Q: What is the Vietnam consumer market size?**
A: The full population is 100 million but the addressable middle-class market is closer to 25 to 30 million people concentrated in Ho Chi Minh City, Hanoi, and Da Nang. McKinsey projects 17 million 'consuming class' households by 2030.

**Q: Which sectors are growing fastest in Vietnam?**
A: Ecommerce GMV grew 25 percent in 2024, fintech and renewables are scaling rapidly, and high-end electronics manufacturing remains a structural story. Services overall grew 7.4 percent vs the 6.1 percent national rate.

**Q: Is Vietnam a good market for foreign businesses?**
A: For manufacturing and supply chain, yes — Vietnam is the leading non-China alternative globally. For consumer brands, the curve is favourable but the addressable middle class is smaller than the headline population suggests. For B2B SaaS, procurement cycles are long and price sensitivity is high.

**Q: What are the biggest risks of doing business in Vietnam?**
A: Currency volatility, narrowing engineering cost advantage, regulatory tightening around data and content, and limited exit liquidity for venture-backed startups.

**Q: How does Vietnam compare to Indonesia and the Philippines?**
A: Smaller addressable consumer base than either, but stronger manufacturing position and faster sustained growth. Vietnam's per-capita GDP overtook the Philippines in 2024 and the gap widened in 2025 with Vietnam's 8.02 percent growth.
""",
        "faq_block_json": """[
{"question": "How big is the Vietnam economy?", "answer": "USD 470 billion nominal GDP in 2024, USD 1.5 trillion in purchasing power parity. The 35th largest economy globally and the third largest in Southeast Asia."},
{"question": "What is the Vietnam GDP growth rate?", "answer": "6.1 percent in 2024 with 2025 forecast at 6.5 percent. Second-fastest in ASEAN and among the top three in Asia for economies above USD 200 billion."},
{"question": "What is the Vietnam consumer market size?", "answer": "Full population is 100 million but the addressable middle-class market is closer to 25 to 30 million people concentrated in Ho Chi Minh City, Hanoi, and Da Nang. McKinsey projects 17 million consuming-class households by 2030."},
{"question": "Which sectors are growing fastest in Vietnam?", "answer": "Ecommerce GMV grew 25 percent in 2024, fintech and renewables are scaling rapidly, and high-end electronics manufacturing remains a structural story."},
{"question": "Is Vietnam a good market for foreign businesses?", "answer": "For manufacturing and supply chain yes — Vietnam is the leading non-China alternative globally. For consumer brands the curve is favourable but the addressable middle class is smaller than the headline 100 million."},
{"question": "What are the biggest risks of doing business in Vietnam?", "answer": "Currency volatility, narrowing engineering cost advantage, regulatory tightening around data and content, and limited exit liquidity for venture-backed startups."},
{"question": "How does Vietnam compare to Indonesia and the Philippines?", "answer": "Smaller addressable consumer base than either but stronger manufacturing position and faster sustained growth. Vietnam's per-capita GDP overtook the Philippines in 2024 and the gap widened in 2025."},
{"question": "How big is Vietnam's GDP growth in 2025?", "answer": "8.02 percent — one of the highest in nearly three decades, well above the 6.5 percent forecast. Industry and construction led at 8.95 percent."}
]""",
        "source_citations": (
            "- General Statistics Office of Vietnam: 2025 estimate (GDP 8.02 percent)\n"
            "- Vietnam Briefing: Vietnam's Economy in 2025 — GDP, FDI, and Trade\n"
            "- OECD Economic Surveys: Viet Nam 2025\n"
            "- China Briefing: Vietnam Economic Performance in 2025\n"
            "- ARC Group: Vietnam Economic Update Reports Q2, Q3 2025\n"
            "- PwC Vietnam Economic Update 9M 2025\n"
            "- World Bank, IMF Article IV: Vietnam country profile\n"
            "- McKinsey: Vietnam consumer sentiment 2025"
        ),
    },
]
