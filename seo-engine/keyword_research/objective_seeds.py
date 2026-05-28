"""
Curated seed list aligned with OSR's Phase 1 objective:

  Main audience — Global VCs:
    Research about Vietnam economy, startup landscape, deal flow, sector
    opportunities. KEYWORDS CONTAINING "vietnam" WIN.

  Secondary audience — Global founders:
    Learn business frameworks, idea generation (esp. AI-native), techniques to
    build with AI, fundraising techniques, AND startup validation methodology
    (OSR's core IP — can genuinely compete on this).

Two seed buckets, each ~30 terms. Each seed will be expanded via DataForSEO
keyword_suggestions to ~50-680 long-tail variants with real volume + KD.

Run:
    python objective_seeds.py    # prints the list for review
"""

# ============================================================================
# BUCKET A — Vietnam-VC research (main audience)
# Target reader: global VC partner, family office, micro-VC, corporate venture
# researching SEA / Vietnam dealflow. Each keyword contains "vietnam" or
# strongly implies Vietnam-only context.
# ============================================================================

SEEDS_VN_VC = [
    # Vietnam macro / economy
    "vietnam economy 2026",
    "vietnam gdp growth",
    "vietnam tech market",
    "vietnam digital economy",
    "vietnam fdi",
    # Vietnam startup ecosystem (broad)
    "vietnam startup ecosystem",
    "vietnam startup news",
    "vietnam unicorn startups",
    "vietnam startup landscape",
    "vietnam tech startups",
    # Vietnam VC / funding
    "vietnam venture capital",
    "vietnam vc landscape",
    "vietnam seed funding",
    "vietnam startup investment",
    "vietnam dealflow",
    "investing in vietnam startups",
    "vietnam angel investors",
    # Vietnam sector opportunities (the 5 OSR pillars + cross-cutting)
    "fintech vietnam",
    "edtech vietnam",
    "healthtech vietnam",
    "insurtech vietnam",
    "proptech vietnam",
    "agritech vietnam",
    "logistics vietnam",
    "ecommerce vietnam",
    "saas vietnam",
    "creator economy vietnam",
    # Vietnam consumer market
    "gen z vietnam",
    "vietnam middle class",
    "consumer trends vietnam",
    # Vietnam regulatory / business climate
    "starting a business in vietnam",
    "vietnam business regulations",
    "vietnam tax for startups",
]


# ============================================================================
# BUCKET B — Global founder education (secondary audience)
# Target reader: pre-seed/seed founder learning frameworks. AI-native angle
# is the modern wedge. Validation is OSR's compete-on core. Fundraising is
# the high-intent need.
# ============================================================================

SEEDS_FOUNDER_EDU = [
    # Validation (OSR's core IP — highest priority to compete)
    "how to validate startup idea",
    "startup validation framework",
    "validate business idea",
    "customer development interviews",
    "problem solution fit",
    "product market fit",
    "minimum viable product",
    # Idea generation (AI-native angle is the modern wedge)
    "ai startup ideas",
    "saas startup ideas",
    "side project ideas",
    "passive income startup ideas",
    "ai business ideas",
    "ai agent startup ideas",
    # Build with AI (Greg Isenberg territory)
    "vibe coding",
    "build app with ai",
    "no code with ai",
    "cursor ai development",
    "claude code tutorial",
    "lovable app builder",
    "v0 by vercel",
    # Business frameworks (OSR's methodology library)
    "business model canvas",
    "value proposition canvas",
    "blue ocean strategy",
    "lean startup",
    "jobs to be done framework",
    "north star metric",
    # Fundraising
    "how to raise seed round",
    "how to pitch investors",
    "pitch deck template",
    "term sheet explained",
    "convertible note vs safe",
    "vc due diligence checklist",
    # Go-to-market / growth
    "startup go to market strategy",
    "product launch strategy",
]


def all_seeds() -> list[tuple[str, str]]:
    """Return [(seed, bucket), ...] for all seeds."""
    return (
        [(s, "vn_vc") for s in SEEDS_VN_VC]
        + [(s, "founder_edu") for s in SEEDS_FOUNDER_EDU]
    )


if __name__ == "__main__":
    print(f"VN-VC seeds:       {len(SEEDS_VN_VC)}")
    print(f"Founder-edu seeds: {len(SEEDS_FOUNDER_EDU)}")
    print(f"Total seeds:       {len(SEEDS_VN_VC) + len(SEEDS_FOUNDER_EDU)}")
    print(f"\nExpected DFS cost: {(len(SEEDS_VN_VC) + len(SEEDS_FOUNDER_EDU)) * 0.011:.2f} USD")
    print(f"\nBUCKET A — Vietnam-VC ({len(SEEDS_VN_VC)} seeds):")
    for s in SEEDS_VN_VC:
        print(f"  - {s}")
    print(f"\nBUCKET B — Founder-edu ({len(SEEDS_FOUNDER_EDU)} seeds):")
    for s in SEEDS_FOUNDER_EDU:
        print(f"  - {s}")
