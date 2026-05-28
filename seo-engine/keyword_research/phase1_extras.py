"""
Optional sections per article — "What OS Research thinks" + "Common mistakes".

Per plan Section 3.3, these are required for `framework_example` and
`how_to_validate` patterns. The v4 source bodies didn't include them; this
module appends them at render time via refresh_10_bodies.py.

Insertion point: right BEFORE the `## Frequently asked questions` section.

Each entry:
  primary_keyword → {osr_thinks: markdown, common_mistakes: markdown}
"""
from __future__ import annotations


EXTRAS: dict[str, dict[str, str]] = {

    # ============================================================
    # #003 — examples for business model canvas (framework_example)
    # ============================================================
    "examples for business model canvas": {
        "osr_thinks": (
            "Most Business Model Canvas examples online recycle the same five companies "
            "(Uber, Airbnb, Netflix, Spotify, Apple). They are textbook polished, which is "
            "exactly why they teach the wrong lesson.\n\n"
            "OS Research uses the canvas as a validation artifact, not a strategy document. "
            "Every box starts as a hypothesis. Boxes get filled progressively as evidence "
            "comes in: Customer Segments after 30 interviews, Channels after pre-sale tests, "
            "Revenue Streams after the first paying user. A canvas finished in one sitting is "
            "a wishlist, not a model.\n\n"
            "The most instructive examples are the FAILED canvases. The Quibi canvas reads "
            "beautifully on paper, every box neat. The actual failure lived in the "
            "Customer Segments box, where the team confused 'busy commuters with quick "
            "attention spans' (a persona) with a job-to-be-done (people did not need short "
            "premium video, they needed something to fill scroll gaps). A truly useful "
            "example shows you that gap, not the polished version."
        ),
        "common_mistakes": (
            "- Treating the canvas as a strategy plan instead of a hypothesis map\n"
            "- Filling all 9 boxes in one workshop with assumptions, then never updating\n"
            "- Skipping Key Resources and Cost Structure (least sexy boxes, most critical)\n"
            "- Confusing Customer Segments with personas\n"
            "- Drawing one canvas for the whole company when you should draw one per customer segment"
        ),
    },

    # ============================================================
    # #004 — vibe coding application (framework_example)
    # ============================================================
    "vibe coding application": {
        "osr_thinks": (
            "Vibe coding is a validation accelerator that most founders use past its expiry. "
            "It is excellent for landing pages, fake-door tests, and pre-sale flows. It "
            "becomes dangerous when teams ship customer-facing applications built entirely "
            "by AI without understanding the underlying code.\n\n"
            "The trap is that velocity feels like progress. Six weeks of vibe coding produces "
            "an app that runs, looks polished, and seems shippable. What it hides: security "
            "gaps the team cannot debug, architectural choices the AI made on autopilot, and "
            "compliance blind spots that surface only when a real customer triggers them.\n\n"
            "OS Research maps vibe coding to TRR stages. Below Solution Fit (60 percent on "
            "the TRR scale), vibe everything. Above Solution Fit, audit and harden. The "
            "founders who get this backward, hand-coding while still in validation or vibing "
            "production code at PMF, burn time on the wrong end of the curve."
        ),
        "common_mistakes": (
            "- Building production-grade features in vibe mode then 'shipping fast'\n"
            "- Skipping security review on AI-generated auth and payment flows\n"
            "- Letting the AI choose architecture (it defaults to training-data favorites, often wrong for your scale)\n"
            "- No version control discipline, losing your way after 20 prompts\n"
            "- Treating the vibe-built MVP as the production product instead of an experiment artifact"
        ),
    },

    # ============================================================
    # #005 — lean canvas business model (framework_example)
    # ============================================================
    "lean canvas business model": {
        "osr_thinks": (
            "Lean Canvas works as a living validation artifact, filled progressively per "
            "TRR stage with evidence, not as a one-page strategy document that founders "
            "polish quarterly and forget.\n\n"
            "The Unfair Advantage box is where most lean canvases lie. Founders write "
            "aspirational text ('founder experience', 'proprietary algorithm', 'network "
            "effects') when they actually have no moat yet. The right answer for most "
            "early-stage startups is to leave that box empty until the moat is documented "
            "with evidence: a patent filed, a data asset 10x larger than competitors, a "
            "customer contract that locks out alternatives. Empty is honest. Aspirational "
            "is a tell.\n\n"
            "OS Research fills the Lean Canvas last (after the Business Model Canvas for the "
            "broader business shape) and only with evidence. Problem, Solution, and Key "
            "Metrics drive the daily work. The other boxes are scaffolding."
        ),
        "common_mistakes": (
            "- Treating Lean Canvas as a replacement for BMC rather than a complement at early stage\n"
            "- Writing aspirational text in the Unfair Advantage box\n"
            "- Skipping Key Metrics because they are hard to define\n"
            "- Drawing one canvas per company when you should draw one per customer segment\n"
            "- Confusing the canvas with the plan: the canvas is a snapshot, not a roadmap"
        ),
    },

    # ============================================================
    # #006 — value proposition canvas model (framework_example)
    # ============================================================
    "value proposition canvas model": {
        "osr_thinks": (
            "The Value Proposition Canvas fails when teams fill it from imagination instead "
            "of customer interviews. The six boxes only work as a synthesis tool after 30 "
            "or more interviews, not as a whiteboard brainstorm canvas.\n\n"
            "The right sequence: run customer development interviews using JTBD methodology, "
            "transcribe them, tag patterns, then populate Pains and Gains from actual customer "
            "quotes. Pain Relievers and Gain Creators come last, mapped to specific Pains and "
            "Gains. If a Pain Reliever does not trace back to a specific customer quote, it is "
            "speculation.\n\n"
            "OS Research pairs VPC with JTBD interview format. Pains come from the question "
            "'walk me through the last time you tried to solve this problem.' Gains come from "
            "'if this worked perfectly, what would change for you?' Imagined Pains and Gains "
            "produce features no one asked for. Researched ones produce value propositions "
            "that close pre-sales."
        ),
        "common_mistakes": (
            "- Filling VPC from internal assumptions instead of customer evidence\n"
            "- Writing Gains too generically ('they want to save time') instead of specific outcomes\n"
            "- Ignoring negative Pains (what the customer actively avoids, often the strongest signal)\n"
            "- Treating Pain Relievers as features instead of outcomes\n"
            "- Drawing one VPC for an entire customer segment instead of one per persona within it"
        ),
    },

    # ============================================================
    # #007 — jobs to be done framework (framework_example)
    # ============================================================
    "jobs to be done framework": {
        "osr_thinks": (
            "Jobs to Be Done is the most-cited and least-applied framework in startup land. "
            "Founders read Clay Christensen, write three vague Job Statements, then go back "
            "to building features.\n\n"
            "The Ulwick outcome-driven version is more rigorous and harder to fake. Instead "
            "of vague Jobs ('I want to listen to music'), it produces outcomes ('minimize the "
            "time it takes to find a song I will enjoy'). Outcomes are testable, prioritizable, "
            "and tie directly to product decisions.\n\n"
            "OS Research uses JTBD interview format to surface 30 to 50 outcomes per problem "
            "space. We then plot each on an importance-versus-satisfaction matrix. The "
            "outcomes that score high on importance and low on satisfaction are the "
            "opportunity space. Everything else is noise. Without this rigor, JTBD becomes "
            "personas with different labels."
        ),
        "common_mistakes": (
            "- Writing Job Statements without 20 or more customer interviews\n"
            "- Confusing functional, emotional, and social jobs (mixing them up in the same statement)\n"
            "- Skipping the 'current solution and workaround' interview question (the richest signal)\n"
            "- Treating JTBD as user-personas-with-different-labels\n"
            "- Using JTBD only at product launch and never revisiting as the market shifts"
        ),
    },

    # ============================================================
    # #008 — vibe coding tools (framework_example)
    # ============================================================
    "vibe coding tools": {
        "osr_thinks": (
            "The 'best vibe coding tool' question is the wrong one. Tools matter at the "
            "margin. The real differentiator is whether the founder can articulate the "
            "specification clearly enough for any tool to deliver.\n\n"
            "OS Research uses a tool-by-stage matrix. Lovable and v0 by Vercel for landing "
            "pages and pre-sale flows (output is good enough, iteration is fast). Cursor "
            "and Claude Code for working prototypes where the team needs to read and modify "
            "the generated code. Nothing AI-generated touches production until the team "
            "has reached Solution Fit and a senior engineer has audited the codebase.\n\n"
            "Switching tools mid-build rarely solves the problem. If the output is wrong, "
            "the prompt is wrong. Spend an hour rewriting the spec before spending a day "
            "switching from Lovable to v0."
        ),
        "common_mistakes": (
            "- Tool-shopping instead of specification-writing\n"
            "- Switching tools mid-build because output is not perfect (the problem is usually the prompt)\n"
            "- Using app-builders for things they were not designed for (complex backends, real-time systems)\n"
            "- Not version-controlling AI-generated code\n"
            "- Mistaking tool fluency for engineering judgment"
        ),
    },

    # ============================================================
    # #009 — product market fit (how_to_validate)
    # ============================================================
    "product market fit": {
        "osr_thinks": (
            "Product-Market Fit is a continuum, not a moment. The Sean Ellis 40 percent "
            "survey is a leading indicator, not a final verdict. Single-metric PMF "
            "declarations are vanity.\n\n"
            "OS Research measures PMF with three layered signals that have to be present "
            "together: organic referral rate above 15 percent of new signups, retention "
            "curve flattening above 30 percent by month 6, and willingness to pay where "
            "paying users are at least 50 percent of activated users. Missing any one "
            "means the team has product-channel fit or product-investor fit, not "
            "product-market fit.\n\n"
            "The hardest part of PMF is timing pivots. Most teams pivot 3 months past a "
            "clear no-fit signal because the founder cannot accept what the data says. A "
            "smaller cohort pivots too early, before 1,000 distinct users have used the "
            "product end to end. The discipline is to set the PMF threshold before you "
            "ship and stick to it."
        ),
        "common_mistakes": (
            "- Declaring PMF after the first viral month\n"
            "- Confusing product-channel fit (one channel works) with product-market fit (the market wants it)\n"
            "- Relying solely on the Sean Ellis survey (selection bias toward your most loyal users)\n"
            "- Pivoting too late (3 months past clear no-fit signals)\n"
            "- Pivoting too early (before 1,000 distinct users have completed the core flow)"
        ),
    },

    # ============================================================
    # #010 — blue ocean vs red ocean strategy (framework_example)
    # ============================================================
    "blue ocean vs red ocean strategy": {
        "osr_thinks": (
            "Blue Ocean Strategy gets quoted as a 'create new markets' mantra, but the "
            "real mechanic is the ERRC grid: Eliminate, Reduce, Raise, Create. Most "
            "founders skip the ERRC analysis and try to 'go blue ocean' through positioning "
            "copy. They are usually just building in a red ocean with optimistic framing.\n\n"
            "OS Research treats each ERRC decision as a validation hypothesis. Eliminating "
            "factor X is a bet that customers do not actually value X. That bet has to be "
            "tested with customer interviews and pre-sale evidence before it becomes "
            "strategy. Skipping the test means you eliminated the actual value-add and now "
            "the product has no reason to exist.\n\n"
            "The honest read: most 'blue ocean' opportunities are red oceans the founder "
            "has not yet discovered. The Strategy Canvas is the diagnostic. If your canvas "
            "looks like every competitor's canvas with one dimension tweaked, you are in "
            "the red ocean, not creating a new one."
        ),
        "common_mistakes": (
            "- Confusing 'no direct competitors' with 'blue ocean' (often it just means no market)\n"
            "- Skipping the Strategy Canvas (the diagnostic that reveals true ocean color)\n"
            "- Eliminating wrong factors (cutting the actual value-add)\n"
            "- Treating Cirque du Soleil as a template instead of an analogy\n"
            "- Declaring blue ocean before running ERRC analysis with customer evidence"
        ),
    },
}
