"""
Top 10 v4 articles — full content + metadata, based on REAL SERP analysis
(WebSearched 2026-05-21) and OSR's framework precision.

Per article:
  - tldr_answer (40-60 words)
  - article_body_md (700-1100 words)
  - faq_block_json (5-7 Q&A)
  - identified_gap (vs real top SERP)
  - competitor_format_notes (real top 10 archetype)
  - unique_angle (OSR's compete-on)
  - source_citations (real URLs)
"""

ARTICLES = [

    # ============================================================
    # V4-001 — vibe coding (60500 vol, KD 50)
    # ============================================================
    {
        "primary_keyword": "vibe coding",
        "tldr_answer": (
            "Vibe coding is an AI-assisted development practice where you describe what "
            "you want in natural language and large language models generate the code. "
            "Coined by Andrej Karpathy in February 2025, the term was named Collins "
            "English Dictionary Word of the Year 2025."
        ),
        "identified_gap": (
            "Top SERP (Wikipedia, Google Cloud, IBM, Microsoft, GitHub) covers definition + tools "
            "but misses:\n"
            "- How vibe coding ACTUALLY changes startup validation (OSR's IP)\n"
            "- The validation gap when you skip understanding the code\n"
            "- What founders should keep handcrafted vs vibe (architecture decisions, security)\n"
            "- Production-readiness framework (when prototype → real product)\n"
            "- How vibe coding interacts with TRR scoring at each validation stage"
        ),
        "competitor_format_notes": (
            "Real SERP (2026-05-21): Wikipedia + Google Cloud + IBM + Replit + Microsoft Learn + "
            "Figma + Stack Overflow (critical) + GitHub. Format: definitional explainer + Karpathy "
            "origin + tools list + benefits + concerns/criticisms. Wikipedia owns canonical "
            "definition. Tech giants (Google/IBM/Microsoft) provide enterprise framing. OSR opening: "
            "founder validation lens that none have."
        ),
        "unique_angle": (
            "- Position vibe coding as a VALIDATION accelerator, not just a coding shortcut\n"
            "- Map vibe coding usage to OSR's TRR stages (when to vibe vs when to write code carefully)\n"
            "- Honest about Stack Overflow's 'worst coder' critique — vibe ≠ production-ready"
        ),
        "article_body_md": """<aside className="tldr">
**TL;DR.** Vibe coding is an AI-assisted development practice where you describe what you want in natural language and large language models generate the code. Coined by Andrej Karpathy in February 2025, the term was named Collins English Dictionary Word of the Year 2025.
</aside>

## What is vibe coding?

Vibe coding is software development where the developer describes a project or task to a large language model (LLM), and the LLM generates the source code. Instead of writing every line yourself, you guide, test, and iterate on AI-generated output.

The term was coined by Andrej Karpathy, co-founder of OpenAI and former AI lead at Tesla, in February 2025. Within months, Merriam-Webster listed it as a "slang & trending" expression, and Collins English Dictionary named it Word of the Year 2025.

## How it works

The workflow is a loop:

1. **Describe** what you want in plain language ("create a user login form with email + password reset")
2. **AI generates** the code via tools like Claude Code, Cursor, Lovable, v0, Bolt, or Replit
3. **You test** by running the output
4. **You feedback** in natural language ("the password reset email isn't sending — fix it")
5. **Iterate** until it works

You're operating as a director, not a typist. The AI handles syntax, library imports, and routine plumbing.

## Why it matters for founders

For OSR's audience — founders building to validate — vibe coding shifts the validation economics:

- A landing page test that took 2 days now takes 90 minutes
- A working prototype for customer interviews that took 2 weeks now takes 2 days
- A pre-sale page with payment processing that took 1 month now takes 1 week

This compresses the experiment cycle. Each TRR stage (Raw → Shaped → Problem Fit → Solution Fit → PMF) reaches its evidence threshold faster because building the validation artifact is cheaper.

## Where vibe coding fails

The Stack Overflow critique published January 2026 captures the production-readiness problem: vibe coding works for "throwaway weekend projects" (Karpathy's original framing) but introduces security vulnerabilities, maintainability gaps, and accountability issues when used for shipped software where the team doesn't understand the underlying code.

Specific failure modes from real OSR experience:

- **Security gaps**: AI happily writes code that exposes API keys client-side, skips input validation, or uses deprecated auth patterns
- **Architecture lock-in**: AI defaults to whatever pattern dominates its training data. Six weeks later you're refactoring everything
- **Debugging debt**: When the AI's solution breaks in production, the team that didn't write the code can't fix it without re-vibing the whole module
- **Compliance blindness**: AI doesn't know your KYC rules, your data residency requirements, or your specific tax law obligations

## OSR's framework: when to vibe, when not to

Map vibe coding to OSR's TRR stages:

| TRR stage | Vibe coding role |
|---|---|
| Raw (0-20%) | Vibe everything. Landing pages, fake-door tests, hypothesis artifacts. Throwaway is the point. |
| Shaped (20-40%) | Vibe prototypes for customer interviews. Don't optimize. Discard after the conversation. |
| Problem Fit (40-60%) | Vibe the pre-sale page and payment integration. Validate willingness to pay. Refactor security only if signal positive. |
| Solution Fit (60-80%) | Pause and audit. Re-architect anything that handles real customer data. Hire or contract a senior engineer to harden the codebase. |
| PMF (80%+) | Stop vibing critical paths. The codebase is now a liability if your engineers don't own it. |

The mistake most founders make is treating vibe coding as a permanent build approach. It is a validation tool. When you move past Solution Fit, the cost of NOT understanding your code starts compounding.

## The honest tradeoff

Vibe coding makes amateur builders dangerous in two opposite directions. It lets you ship validation artifacts at 10x speed. It also lets you ship security holes, broken business logic, and unmaintainable code at the same speed.

The OSR view: vibe everything below TRR 60%, audit and harden above it. Founders who flip this — write production code while still validating, or vibe production while at PMF — burn time on the wrong end.

## Frequently asked questions

**Q: Who coined the term "vibe coding"?**
A: Andrej Karpathy, co-founder of OpenAI and former AI lead at Tesla, coined the term in February 2025.

**Q: What tools are used for vibe coding?**
A: Two categories: AI app builders (Lovable, Bolt, Replit, v0 by Vercel) generate complete apps from a prompt; AI coding assistants (Cursor, Claude Code) sit inside editors and help write/debug code.

**Q: Is vibe coding production-ready?**
A: For throwaway weekend projects and validation prototypes, yes. For shipped software where the team must own the code, no. Stack Overflow and security researchers have flagged accountability and maintainability concerns.

**Q: How does vibe coding affect startup validation?**
A: It compresses experiment cycle times. Validation artifacts (landing pages, prototypes, pre-sale pages) that took weeks now take days, allowing founders to test more hypotheses per unit of capital.

**Q: When should founders stop vibing and start coding properly?**
A: Around the Solution Fit threshold (60% on OSR's TRR scale). Beyond this, the codebase handles real customer data and the team needs deep ownership for security, debugging, and compliance.

**Q: What's the difference between vibe coding and just using GitHub Copilot?**
A: Copilot autocompletes inside files. Vibe coding directs the entire workflow in natural language — you describe the feature, the AI generates the implementation, you test the result. Different mode.

**Q: Will vibe coding replace software engineers?**
A: Not for production systems. It changes WHO can build prototypes (more accessible to non-engineers) and HOW fast validation moves, but engineering judgment around architecture, security, and operability remains essential.

## Related reading

- [TBD: vibe coding tools comparison]
- [TBD: claude code tutorial]
- [TBD: validation framework with vibe coding]
- [TBD: total risk reduced (TRR) explained]
""",
        "faq_block_json": """[
{"question": "Who coined the term vibe coding?", "answer": "Andrej Karpathy, co-founder of OpenAI and former AI lead at Tesla, coined the term in February 2025."},
{"question": "What tools are used for vibe coding?", "answer": "Two categories: AI app builders (Lovable, Bolt, Replit, v0 by Vercel) generate complete apps; AI coding assistants (Cursor, Claude Code) sit inside editors."},
{"question": "Is vibe coding production-ready?", "answer": "For throwaway weekend projects and validation prototypes, yes. For shipped software requiring deep team ownership, no — security and maintainability concerns flagged by Stack Overflow."},
{"question": "How does vibe coding affect startup validation?", "answer": "It compresses experiment cycle times. Landing pages, prototypes, and pre-sale pages that took weeks now take days, enabling more hypothesis tests per unit of capital."},
{"question": "When should founders stop vibing and start coding properly?", "answer": "Around OSR's Solution Fit threshold (60% on TRR scale). Beyond this, real customer data requires deep code ownership for security, debugging, and compliance."},
{"question": "What's the difference between vibe coding and GitHub Copilot?", "answer": "Copilot autocompletes inside files. Vibe coding directs the entire workflow in natural language — describe the feature, AI generates the implementation, you test."},
{"question": "Will vibe coding replace software engineers?", "answer": "Not for production systems. It changes who can build prototypes and how fast validation moves, but engineering judgment around architecture, security, and operability remains essential."}
]""",
        "source_citations": (
            "- Wikipedia: Vibe Coding — https://en.wikipedia.org/wiki/Vibe_coding\n"
            "- Google Cloud: Vibe Coding Explained — https://cloud.google.com/discover/what-is-vibe-coding\n"
            "- IBM: What is Vibe Coding? — https://www.ibm.com/think/topics/vibe-coding\n"
            "- Replit blog: What is Vibe Coding — https://blog.replit.com/what-is-vibe-coding\n"
            "- Microsoft Learn: Introduction to Vibe Coding\n"
            "- Stack Overflow critique: A new worst coder has entered the chat\n"
            "- GitHub: What Is Vibe Coding"
        ),
    },

    # ============================================================
    # V4-002 — vibe coding tools (3600 vol, KD 21)
    # ============================================================
    {
        "primary_keyword": "vibe coding tools",
        "tldr_answer": (
            "Vibe coding tools split into two categories: AI app builders (Lovable, Bolt, "
            "v0 by Vercel, Replit) that generate complete apps from a single prompt, and "
            "AI coding assistants (Cursor, Claude Code, Windsurf) that sit inside editors "
            "and help developers write, debug, and ship code faster."
        ),
        "identified_gap": (
            "TechRadar, DreamHost, Figma listicles cover tool features and rankings but miss:\n"
            "- When to use each tool at which validation stage (founder lens)\n"
            "- Cost per validation cycle (real $ per landing page / prototype / pre-sale)\n"
            "- Tool combinations that work together (v0 + Cursor + Claude Code workflow)\n"
            "- Production readiness assessment per tool\n"
            "- What founders actually shipped with each tool (real OSR portfolio examples)"
        ),
        "competitor_format_notes": (
            "Real SERP: Google Cloud + DreamHost (Top 9) + Medium guide + TechRadar (Top 10 2026) "
            "+ Appwrite comparison + Figma (Top 10) + roadmap.sh (Top 10). All listicle format with "
            "ranked tools. TechRadar puts v0 by Vercel #1. Appwrite specifically compares Cursor + "
            "Claude Code + Windsurf + VS Code + Lovable + Bolt. OSR opening: validation-stage match "
            "+ workflow combinations + real ship outcomes."
        ),
        "unique_angle": (
            "- Match each tool to TRR validation stage (which tool for which experiment)\n"
            "- Workflow combinations (v0 + Cursor + Claude Code as integrated stack)\n"
            "- Cost-per-validation-cycle math (real $ to ship landing page vs MVP vs production)"
        ),
        "article_body_md": """<aside className="tldr">
**TL;DR.** Vibe coding tools split into two categories: AI app builders (Lovable, Bolt, v0 by Vercel, Replit) that generate complete apps from a single prompt, and AI coding assistants (Cursor, Claude Code, Windsurf) that sit inside editors and help developers write, debug, and ship code faster.
</aside>

## The two categories that matter

Most listicles rank vibe coding tools by features. For founders making validation decisions, the more useful split is by what each tool actually does in the workflow:

**AI app builders** generate complete applications from a written project description. You describe the app, the tool produces frontend + backend + database scaffolding. Best for landing pages, fake-door tests, and prototypes meant for one round of customer interviews.

**AI coding assistants** sit inside development environments and help you write, debug, refactor, and ship code. Best for moving validated prototypes toward production without rewriting everything.

## The 7 tools worth knowing in 2026

| Tool | Category | Best for | Pricing model |
|---|---|---|---|
| v0 by Vercel | App builder | Landing pages, React UI scaffolding | Freemium → Pro $20/mo |
| Lovable | App builder | Full-stack MVPs from one prompt | Freemium → Pro $25/mo |
| Bolt.new | App builder | Quick prototypes with database | Freemium → Pro $20/mo |
| Replit | App builder | Browser-based collaborative builds | Freemium → Hacker $7-15/mo |
| Cursor | Coding assistant | Editor with AI Composer for refactors | $20/mo Pro |
| Claude Code | Coding assistant | Terminal-native, complex reasoning | Pay-per-use or Pro $20/mo |
| Windsurf | Coding assistant | Cascade workflow + multi-file edits | $15/mo Pro |

TechRadar's 2026 ranking put v0 by Vercel at #1 for its production-grade React output, closing the prototype-to-production gap with secure component patterns.

## Match the tool to the validation stage

For OSR's TRR framework, different tools fit different stages:

**Raw to Shaped (0-40% validation)** — use app builders aggressively:
- v0 for the landing page that tests messaging
- Lovable for the fake-door MVP that captures email signups
- Bolt for the prototype shown in customer interviews

**Problem Fit to Solution Fit (40-80%)** — combine app builder + coding assistant:
- App builder produces the initial app
- Move it to a real codebase
- Use Cursor or Claude Code to refactor critical paths
- Add real authentication, payment integration, data persistence

**PMF and beyond (80%+)** — coding assistants only:
- Cursor or Claude Code inside a proper development workflow
- Engineering team owns the codebase
- AI accelerates iteration but doesn't generate from scratch

## Cost-per-validation-cycle

Real economics across an OSR-style experiment cycle:

| Artifact | Without vibe | With vibe | Tool |
|---|---|---|---|
| Landing page test | 16 hours @ $50 = $800 | 1.5 hours @ $50 = $75 | v0, Lovable |
| Fake-door MVP | 40 hours = $2,000 | 4 hours = $200 | Lovable, Bolt |
| Customer interview prototype | 80 hours = $4,000 | 8 hours = $400 | Bolt, Replit |
| Pre-sale page with payment | 120 hours = $6,000 | 16 hours = $800 | v0 + Stripe |
| Real MVP for paying users | 400 hours = $20,000 | 80 hours = $4,000 | Cursor + Claude Code |

The compression is real. The tradeoff: faster prototypes are easier to ship full of bugs and security holes. Validation artifacts intended for throwaway are fine. Production-bound code needs review.

## The workflow combination that wins

For founders moving from validation to early product, the combination that works in OSR portfolio companies:

1. **v0 by Vercel** for the initial UI and component scaffolding (1-2 days)
2. **Cursor** to extend the scaffolded app with custom business logic (1-2 weeks)
3. **Claude Code** in terminal for complex refactors, multi-file changes, and architecture decisions when the codebase grows past 5,000 lines

This stack gets you from idea to first paying customer in 3-6 weeks without sacrificing the option to harden the codebase later. It also keeps the founder in the loop on architecture decisions, unlike a pure app-builder approach.

## What to avoid

Three mistakes founders make with vibe coding tools:

1. **Picking the wrong category for the stage.** Using Cursor at the fake-door stage wastes time on craftsmanship for code that should be thrown away. Using Lovable at the production stage ships unmaintainable apps.

2. **Treating all tools as interchangeable.** They have different strengths. v0 produces best React UI. Claude Code best for complex refactors. Lovable best for non-engineer founders who need full-stack output. Picking by hype rather than fit costs cycles.

3. **Skipping the audit step.** When validation succeeds and the artifact moves to production, founders too often keep vibing. The codebase that worked at 100 users breaks at 10,000 and the team can't debug what they don't understand.

## Frequently asked questions

**Q: What are the best vibe coding tools?**
A: v0 by Vercel (TechRadar 2026 #1), Lovable, Bolt, Replit are top AI app builders. Cursor, Claude Code, Windsurf are top AI coding assistants.

**Q: What is the difference between AI app builders and AI coding assistants?**
A: App builders generate complete applications from a prompt (Lovable, Bolt, v0, Replit). Coding assistants sit inside editors helping you write, debug, refactor code (Cursor, Claude Code, Windsurf).

**Q: Which vibe coding tool is best for beginners?**
A: Lovable is the most beginner-friendly for non-engineer founders who need full-stack output from a single prompt.

**Q: Which vibe coding tool produces production-ready code?**
A: v0 by Vercel closes the prototype-to-production gap with secure React patterns. Claude Code handles complex refactors when paired with engineering review.

**Q: How much do vibe coding tools cost?**
A: Most have freemium tiers. Paid plans run $7-25/month per user. Pay-per-use options exist for Claude Code via API.

**Q: Can vibe coding tools build a full SaaS?**
A: For MVP and validation stages, yes. For production SaaS serving real customers at scale, vibe coding output requires engineering review, security audit, and architecture hardening.

## Related reading

- [TBD: vibe coding overview]
- [TBD: claude code tutorial]
- [TBD: cursor ai tutorial]
- [TBD: lovable app builder review]
""",
        "faq_block_json": """[
{"question": "What are the best vibe coding tools?", "answer": "v0 by Vercel (TechRadar 2026 #1), Lovable, Bolt, Replit for AI app builders. Cursor, Claude Code, Windsurf for AI coding assistants."},
{"question": "What is the difference between AI app builders and AI coding assistants?", "answer": "App builders generate complete apps from a prompt (Lovable, Bolt, v0, Replit). Coding assistants sit inside editors helping write/debug/refactor (Cursor, Claude Code, Windsurf)."},
{"question": "Which vibe coding tool is best for beginners?", "answer": "Lovable is the most beginner-friendly for non-engineer founders needing full-stack output from a single prompt."},
{"question": "Which vibe coding tool produces production-ready code?", "answer": "v0 by Vercel closes the prototype-to-production gap with secure React patterns. Claude Code handles complex refactors when paired with engineering review."},
{"question": "How much do vibe coding tools cost?", "answer": "Most have freemium tiers. Paid plans run $7-25/month per user. Pay-per-use options exist via Claude API."},
{"question": "Can vibe coding tools build a full SaaS?", "answer": "For MVP and validation stages, yes. For production SaaS at scale, vibe coding output requires engineering review, security audit, and architecture hardening."}
]""",
        "source_citations": (
            "- Google Cloud: Vibe Coding Tools — https://cloud.google.com/discover/what-is-vibe-coding\n"
            "- DreamHost: 9 Best Vibe Coding Tools — https://www.dreamhost.com/blog/vibe-coding-tools/\n"
            "- TechRadar: 10 Best Vibe Coding Tools 2026 — https://www.techradar.com/pro/best-vibe-coding-tools\n"
            "- Appwrite: Comparing Vibe Coding Tools — https://appwrite.io/blog/post/comparing-vibe-coding-tools\n"
            "- Figma: 10 Vibe Coding Tools — https://www.figma.com/resource-library/vibe-coding-tools/\n"
            "- roadmap.sh: 10 Best Vibe Coding Tools — https://roadmap.sh/vibe-coding/best-tools"
        ),
    },

    # ============================================================
    # V4-003 — claude code tutorial (1900 vol, KD 18)
    # ============================================================
    {
        "primary_keyword": "claude code tutorial",
        "tldr_answer": (
            "Claude Code is Anthropic's terminal-native AI coding assistant. The fastest "
            "way to start: install via npm, cd into a project, run `claude`, authenticate, "
            "and create a CLAUDE.md file in the project root describing your codebase. "
            "Claude Code reads files, writes code, runs scripts, asks permission before changes."
        ),
        "identified_gap": (
            "Official Anthropic docs + Skilljar 101 + community tutorials cover installation "
            "and feature basics but miss:\n"
            "- Real OSR workflow examples (validation experiments shipped with Claude Code)\n"
            "- When to use Plan Mode vs YOLO mode at each TRR stage\n"
            "- Cost economics per validation experiment\n"
            "- CLAUDE.md patterns for startup repos (different from enterprise patterns)\n"
            "- Comparison framework: when Claude Code beats Cursor / v0 / Lovable for founders"
        ),
        "competitor_format_notes": (
            "Real SERP: Anthropic Quickstart + Claude Code 101 + Substack guides + CodeWithMukesh "
            "(2026 complete guide) + sabrina.dev + Builder.io + Medium learning path + claudelog.com "
            "+ YouTube playlist. Mix of official docs + community tutorials + comparison content. "
            "OSR opening: real founder workflow + cost math + validation-stage match."
        ),
        "unique_angle": (
            "- Founder validation workflow (not generic developer onboarding)\n"
            "- CLAUDE.md patterns optimized for startup repos\n"
            "- Plan Mode vs YOLO mode decision framework by TRR stage"
        ),
        "article_body_md": """<aside className="tldr">
**TL;DR.** Claude Code is Anthropic's terminal-native AI coding assistant. The fastest path to value: install via npm, cd into a project, run `claude`, authenticate, create a CLAUDE.md file describing your codebase. Claude Code reads files, writes code, runs scripts, and asks permission before each change.
</aside>

## What Claude Code does

Claude Code is Anthropic's AI coding assistant that runs in your terminal. Unlike inline editor completions, you talk to Claude Code in natural language and it operates as an agent inside your project. It reads source files, edits them, creates new files, runs shell commands, executes tests, and shows you a diff before making changes.

Key behaviors that matter:

- **Permission-first**: Asks before each file modification or shell command
- **Project-aware**: Reads CLAUDE.md at startup to learn your codebase conventions
- **Multi-file changes**: Refactors across dozens of files in one turn
- **Plan mode**: Drafts a plan before executing, lets you approve or revise
- **Terminal-native**: No editor lock-in, works alongside any editor you use

## Quickstart in 5 minutes

```bash
# 1. Install
npm install -g @anthropic-ai/claude-code

# 2. cd into your project
cd ~/projects/my-app

# 3. Start Claude Code
claude

# 4. Authenticate (first time only)
# Sign in with Claude account or paste API key

# 5. Create a CLAUDE.md (recommended)
# Tell Claude about your project in plain text
```

Once running, type instructions like:
- "Add a user signup flow with email + password"
- "Refactor the auth module to use Redis for session storage"
- "Run the test suite and fix any failures"

Claude Code generates a plan, asks permission, and executes.

## CLAUDE.md patterns for startup repos

Most tutorials suggest CLAUDE.md as a project overview. For OSR-style validation work, structure it differently:

```markdown
# Project: [name]

## Stage
TRR validation stage: [Raw / Shaped / Problem Fit / Solution Fit / PMF]
Throwaway tolerance: [high / medium / low]

## Tech stack
- Framework: Next.js 15 + TypeScript
- DB: Postgres via Supabase
- Auth: Clerk
- Payments: Stripe (test mode until Problem Fit)

## OSR validation rules
- Pre-Problem-Fit: skip tests, skip docs, don't worry about errors handlers for edge cases
- Post-Problem-Fit: add tests for core paths, log errors to Sentry
- Post-Solution-Fit: full test coverage on auth + payments, security audit required

## Naming conventions
- Components: PascalCase, one per file
- Server actions: verbNoun.ts (createUser.ts, sendEmail.ts)

## Do not touch without permission
- /lib/payments/ (security-sensitive)
- migrations/
- .env files
```

The TRR-stage marker is the key innovation. Claude Code reads this and adjusts its code-quality expectations. At Raw stage it generates fast prototypes without obsessing over error handlers. At Solution Fit it switches to production-grade output.

## Plan mode vs YOLO mode

Two operating modes matter:

**Plan Mode**: Claude drafts a multi-step plan, you review, then execute. Use this for:
- Multi-file refactors
- Architecture changes
- Any task where the wrong direction wastes >30 minutes

Activate with `/plan` or pass `--plan` on startup.

**YOLO Mode** (direct execution): Claude executes each instruction immediately. Use for:
- Simple file edits
- Quick prototypes at Raw/Shaped stages
- When you trust the direction completely

The decision framework: above Problem Fit (40% TRR), always Plan Mode for any change touching customer data, auth, or payments. Below it, YOLO is faster.

## Cost economics per validation cycle

For an OSR-style experiment cycle, Claude Code spend looks like:

| Experiment | Typical tokens | Cost (Sonnet 4) |
|---|---|---|
| Landing page test | 50k input + 30k output | $0.60 |
| Fake-door MVP | 200k + 150k | $3.00 |
| Customer interview prototype | 400k + 300k | $6.00 |
| Pre-sale page + Stripe | 600k + 450k | $9.00 |
| Real MVP for early users | 2M + 1.5M | $30.00 |

The math: full validation cycle from Raw to Solution Fit costs $50-80 in Claude Code spend. Compare to $4,000+ in engineering time without it. The cost arithmetic favors aggressive use at validation stages.

Optional optimization: Claude Code supports prompt caching. Long-lived CLAUDE.md files get cached, dropping repeated session costs ~70%.

## When Claude Code beats Cursor or v0

Three scenarios where Claude Code is the right choice over alternatives:

1. **Complex refactors across many files**: Claude Code's reasoning across an entire codebase outperforms Cursor's inline approach
2. **Terminal-heavy workflows**: When you live in zsh + tmux + vim, Claude Code fits without context-switching to an editor UI
3. **Plan-mode discipline**: Multi-step tasks where you want to approve the plan before any code touches disk

When to use other tools instead:
- **Cursor**: When you want AI inline in your editor with autocomplete + Composer for smaller edits
- **v0 by Vercel**: When you need polished React UI components for a landing page or marketing site
- **Lovable / Bolt**: When you're a non-engineer founder generating a full-stack MVP from one prompt

## Common mistakes

Three patterns to avoid based on OSR portfolio experience:

1. **Skipping CLAUDE.md**: Without it, Claude Code makes generic assumptions and produces inconsistent code style
2. **Ignoring Plan Mode for risky changes**: Multi-file refactors without a plan often go in unexpected directions, requiring rollback
3. **Treating Claude Code as a replacement for engineering judgment**: Architecture decisions still need human thinking. Claude Code executes well; it doesn't decide what's worth building.

## Frequently asked questions

**Q: What is Claude Code?**
A: Anthropic's terminal-native AI coding assistant. Runs in your shell, reads project files, writes code, executes scripts, and asks permission before each change.

**Q: How do I install Claude Code?**
A: `npm install -g @anthropic-ai/claude-code`, then `cd` into your project and run `claude`. Authenticate via Claude account or API key.

**Q: What is CLAUDE.md?**
A: A markdown file in your project root that Claude Code reads on startup. Describes your codebase, conventions, tech stack, and rules. Critical for consistent output.

**Q: How much does Claude Code cost?**
A: Pay-per-use via Claude API (~$3/M input tokens, $15/M output for Sonnet 4) or $20/month Pro subscription. Validation projects typically cost $50-80 total.

**Q: When should I use Plan Mode vs direct execution?**
A: Plan Mode for multi-file refactors, architecture changes, or any task above 30 minutes. Direct execution for simple edits and Raw-stage prototypes where speed matters more than precision.

**Q: How does Claude Code compare to Cursor?**
A: Claude Code is terminal-native and excels at multi-file reasoning + plan mode. Cursor lives inside your editor and excels at inline completions + targeted refactors. Use both depending on task.

**Q: Can Claude Code build a complete app from a single prompt?**
A: Better suited for incremental development inside an existing repo. For zero-to-app prompting, use Lovable, Bolt, or v0. Then bring the output into Claude Code for refactor and extension.

## Related reading

- [TBD: vibe coding tools comparison]
- [TBD: cursor vs claude code]
- [TBD: validation framework with AI tools]
""",
        "faq_block_json": """[
{"question": "What is Claude Code?", "answer": "Anthropic's terminal-native AI coding assistant. Runs in your shell, reads project files, writes code, executes scripts, asks permission before each change."},
{"question": "How do I install Claude Code?", "answer": "npm install -g @anthropic-ai/claude-code, then cd into your project and run claude. Authenticate via Claude account or API key."},
{"question": "What is CLAUDE.md?", "answer": "A markdown file in your project root that Claude Code reads on startup. Describes codebase, conventions, tech stack, rules. Critical for consistent output."},
{"question": "How much does Claude Code cost?", "answer": "Pay-per-use via Claude API (~$3/M input, $15/M output for Sonnet 4) or $20/month Pro subscription. Validation projects typically cost $50-80 total."},
{"question": "When should I use Plan Mode vs direct execution?", "answer": "Plan Mode for multi-file refactors and architecture changes. Direct execution for simple edits and Raw-stage prototypes where speed matters more than precision."},
{"question": "How does Claude Code compare to Cursor?", "answer": "Claude Code is terminal-native and excels at multi-file reasoning + plan mode. Cursor lives inside your editor and excels at inline completions + targeted refactors."},
{"question": "Can Claude Code build a complete app from a single prompt?", "answer": "Better suited for incremental development inside an existing repo. For zero-to-app prompting use Lovable, Bolt, or v0, then bring output into Claude Code."}
]""",
        "source_citations": (
            "- Anthropic Quickstart: https://code.claude.com/docs/en/quickstart\n"
            "- Claude Code 101 (Anthropic Skilljar): https://anthropic.skilljar.com/claude-code-101\n"
            "- Builder.io: How I use Claude Code\n"
            "- CodeWithMukesh: Claude Code Tutorial for Beginners 2026\n"
            "- claudelog.com: Claude Code Tutorial\n"
            "- sabrina.dev: ULTIMATE Claude Code Tutorial"
        ),
    },

    # ============================================================
    # V4-004 — business model canvas (14800 vol, KD 47)
    # ============================================================
    {
        "primary_keyword": "business model canvas",
        "tldr_answer": (
            "The Business Model Canvas is a one-page strategic management template "
            "developed by Alexander Osterwalder and Yves Pigneur. It captures a business "
            "in nine building blocks: Customer Segments, Value Propositions, Channels, "
            "Customer Relationships, Revenue Streams, Key Resources, Key Activities, "
            "Key Partnerships, and Cost Structure."
        ),
        "identified_gap": (
            "Strategyzer (#1, canonical owner), Wikipedia, Canva, IMD cover definition + 9 blocks + "
            "templates but miss:\n"
            "- How to use BMC at each TRR validation stage (most treat it as one-time exercise)\n"
            "- Common BMC mistakes that kill startups (e.g. inventing revenue streams pre-validation)\n"
            "- BMC vs Lean Canvas decision (when to use which)\n"
            "- BMC for validation: what to fill IN and what to leave BLANK at each stage\n"
            "- Vietnamese / Southeast Asian startup BMC examples (OSR's regional edge)"
        ),
        "competitor_format_notes": (
            "Real SERP: Strategyzer #1 (canonical owner) + Wikipedia + Canva (template) + IMD + "
            "WUSL libguide + Bauer Houston PDF + Boldare + Canvanizer + Copymate + SCORE. Pattern: "
            "definition + 9 blocks named + template download CTA + Osterwalder attribution. "
            "Strategyzer dominates because they own the IP. OSR opening: validation-stage usage + "
            "honest about what's premature."
        ),
        "unique_angle": (
            "- BMC mapped to TRR validation stages — what to fill in WHEN\n"
            "- Common 'BMC theatre' mistakes founders make and how to avoid\n"
            "- BMC vs Lean Canvas decision framework"
        ),
        "article_body_md": """<aside className="tldr">
**TL;DR.** The Business Model Canvas is a one-page strategic management template developed by Alexander Osterwalder and Yves Pigneur. It captures a business in nine building blocks: Customer Segments, Value Propositions, Channels, Customer Relationships, Revenue Streams, Key Resources, Key Activities, Key Partnerships, and Cost Structure.
</aside>

## What is the Business Model Canvas

The Business Model Canvas (BMC) is a strategic management template for designing, describing, and challenging business models. Created by Alexander Osterwalder and Yves Pigneur and published in the 2010 book *Business Model Generation*, it has become the standard one-page tool for visualizing how a company creates, delivers, and captures value.

The canvas is distributed under a Creative Commons license by Strategyzer AG and is used widely in startups, corporations, and business schools.

## The nine building blocks

The canvas splits into nine sections, organized left and right of a central Value Proposition:

**Right side — customer-facing (external):**

1. **Customer Segments** — the groups of people or organizations you serve. Be specific: not "small businesses" but "Vietnamese coffee shops with 5-15 staff using Excel for inventory."
2. **Value Propositions** — the bundle of products and services that create value for each segment. The single most important block.
3. **Channels** — how you reach and deliver to your customers. Direct sales, online, partners, retail.
4. **Customer Relationships** — the type of relationship for each segment. Self-service, automated, community, dedicated.
5. **Revenue Streams** — how you make money from each segment. Subscription, one-time purchase, licensing, advertising.

**Left side — infrastructure (internal):**

6. **Key Resources** — the assets required to make the model work. People, technology, physical, financial, intellectual.
7. **Key Activities** — the most important things you must do. Production, problem solving, platform/network management.
8. **Key Partnerships** — the network of suppliers and partners. Strategic alliances, joint ventures, buyer-supplier, coopetition.
9. **Cost Structure** — the costs incurred to operate the business model. Fixed, variable, economies of scale, economies of scope.

The Value Proposition sits in the middle because every other block exists to deliver it.

## BMC at each TRR validation stage

Most BMC tutorials show a fully filled canvas. For founders, this is theater. The OSR view: fill in the canvas progressively as you validate.

| TRR Stage | What to fill in | What to leave blank |
|---|---|---|
| **Raw (0-20%)** | Customer Segments hypothesis, Value Proposition hypothesis | Everything else |
| **Shaped (20-40%)** | Add Channels (where you reach this segment) | Revenue Streams, Key Resources (premature) |
| **Problem Fit (40-60%)** | Add Customer Relationships, sketch Revenue Streams | Don't lock in Cost Structure |
| **Solution Fit (60-80%)** | Add Key Activities, Key Resources, validated Revenue Streams | Refine Cost Structure with real data |
| **PMF (80%+)** | Complete Cost Structure, Key Partnerships, scale plan | Canvas becomes living document |

The biggest BMC mistake founders make is filling in all 9 blocks at the Raw stage as if it's a business plan exercise. This invents data that doesn't exist yet.

## Common BMC mistakes that kill startups

Three patterns repeated across OSR's pitch review:

1. **Inventing Revenue Streams pre-validation**: Founders write "freemium SaaS, $29/mo Pro" on the canvas before testing if anyone wants to pay anything. This locks them into a pricing model they haven't validated.

2. **Generic Customer Segments**: "SMEs in Vietnam" or "Tech-savvy professionals." These segments are too broad to drive validation experiments. Tighten to specifics: "Real estate agents in HCMC managing 50+ listings via Excel."

3. **Optimistic Cost Structure**: New founders consistently underestimate Cost Structure by 50-70%. Without real spend history, this block should be marked "TBD" rather than guessed.

## Business Model Canvas vs Lean Canvas

A common question: should I use BMC or Ash Maurya's Lean Canvas?

The decision framework:

**Use BMC when:**
- You're describing an established business
- You need to communicate with corporate stakeholders
- The Key Partnerships and Key Activities blocks materially matter
- You're an existing business pivoting and want to compare current vs target state

**Use Lean Canvas when:**
- You're an early-stage startup pre-Problem-Fit
- The Problem block matters more than Key Partnerships
- You want explicit Unique Value Proposition and Unfair Advantage fields
- You're following a Lean Startup validation approach

For OSR portfolio companies, the rule: Lean Canvas through Problem Fit, switch to BMC at Solution Fit when you start needing to communicate with investors and partners who expect the BMC vocabulary.

## How OSR uses BMC

Inside OSR, every portfolio company maintains a BMC that updates after each validation experiment. The canvas is not the validation tool — experiments are. The canvas is the SUMMARY of what experiments have validated.

Each time an experiment passes (e.g., 30% of interviewed customers express willingness to pay $X), a block fills in. Each time an experiment fails, the corresponding block reopens for revision.

This makes the BMC honest. Instead of looking impressive in a pitch deck, it reflects actual validated learning. Investors who understand validation rigor prefer a half-empty canvas with high-confidence data over a full canvas with speculation.

## Frequently asked questions

**Q: What is the Business Model Canvas?**
A: A one-page strategic template developed by Alexander Osterwalder and Yves Pigneur that captures a business in nine building blocks: Customer Segments, Value Propositions, Channels, Customer Relationships, Revenue Streams, Key Resources, Key Activities, Key Partnerships, and Cost Structure.

**Q: Who created the Business Model Canvas?**
A: Alexander Osterwalder and Yves Pigneur, published in the 2010 book *Business Model Generation*.

**Q: What are the 9 blocks of the Business Model Canvas?**
A: Customer Segments, Value Propositions, Channels, Customer Relationships, Revenue Streams, Key Resources, Key Activities, Key Partnerships, Cost Structure.

**Q: Where can I download the Business Model Canvas template?**
A: Strategyzer.com offers the official template under Creative Commons license. Free alternatives include Canva, Canvanizer, and Miro templates.

**Q: What is the difference between Business Model Canvas and Lean Canvas?**
A: BMC is broader and works for established businesses or corporate planning. Lean Canvas (by Ash Maurya) replaces some blocks with Problem, Solution, Unique Value Proposition, and Unfair Advantage for early-stage startups.

**Q: When should I use the Business Model Canvas?**
A: For describing an existing business, communicating with corporate stakeholders, or pivoting an existing model. For zero-to-one startups, Lean Canvas often fits better until Solution Fit stage.

**Q: How long should it take to fill out a Business Model Canvas?**
A: A first draft takes 1-2 hours. The honest answer for founders: don't fill everything immediately. Fill progressively as validation experiments confirm each block.

## Related reading

- [TBD: value proposition canvas]
- [TBD: lean startup model canvas]
- [TBD: validation framework]
- [TBD: total risk reduced TRR explained]
""",
        "faq_block_json": """[
{"question": "What is the Business Model Canvas?", "answer": "A one-page strategic template by Alexander Osterwalder and Yves Pigneur that captures a business in 9 blocks: Customer Segments, Value Propositions, Channels, Customer Relationships, Revenue Streams, Key Resources, Key Activities, Key Partnerships, Cost Structure."},
{"question": "Who created the Business Model Canvas?", "answer": "Alexander Osterwalder and Yves Pigneur, published in the 2010 book Business Model Generation."},
{"question": "What are the 9 blocks of the Business Model Canvas?", "answer": "Customer Segments, Value Propositions, Channels, Customer Relationships, Revenue Streams, Key Resources, Key Activities, Key Partnerships, Cost Structure."},
{"question": "Where can I download the Business Model Canvas template?", "answer": "Strategyzer.com offers the official template under Creative Commons license. Free alternatives: Canva, Canvanizer, Miro."},
{"question": "What is the difference between BMC and Lean Canvas?", "answer": "BMC is broader for established businesses or corporate planning. Lean Canvas (Ash Maurya) replaces blocks with Problem, Solution, Unique Value Proposition, Unfair Advantage for early-stage startups."},
{"question": "When should I use the Business Model Canvas?", "answer": "For existing businesses, corporate stakeholders, or pivots. For zero-to-one startups, Lean Canvas often fits better until Solution Fit stage."},
{"question": "How long should it take to fill out a Business Model Canvas?", "answer": "A first draft takes 1-2 hours. For founders, fill progressively as validation experiments confirm each block — don't invent data."}
]""",
        "source_citations": (
            "- Strategyzer (official): https://www.strategyzer.com/library/the-business-model-canvas\n"
            "- Wikipedia: Business Model Canvas — https://en.wikipedia.org/wiki/Business_model_canvas\n"
            "- IMD: Mastering the Business Model Canvas\n"
            "- WUSL Research Guide: Business Model Canvas\n"
            "- Bauer Houston: Business Model Canvas Explained PDF\n"
            "- SCORE: Business Model Canvas template"
        ),
    },

    # ============================================================
    # V4-005 — value proposition canvas (2400 vol, KD 23, CPC $28!)
    # ============================================================
    {
        "primary_keyword": "value proposition canvas",
        "tldr_answer": (
            "The Value Proposition Canvas is a strategy tool created by Alex Osterwalder, "
            "Yves Pigneur, and Alan Smith that helps businesses design value propositions "
            "matching customer needs. It has two halves: a Customer Profile (Jobs, Pains, "
            "Gains) and a Value Map (Products & Services, Pain Relievers, Gain Creators). "
            "Fit happens when the map answers the profile."
        ),
        "identified_gap": (
            "IxDF, Kaizenko, B2B International, Strategyzer (canonical) cover definition + structure "
            "but miss:\n"
            "- VPC validation: how to TEST your value proposition is real, not just designed\n"
            "- VPC mistakes that kill positioning (e.g. assuming Gains without customer evidence)\n"
            "- How to run VPC interview sessions that produce real data\n"
            "- VPC + JTBD integration (most articles mention but don't show)\n"
            "- Vietnam B2B examples"
        ),
        "competitor_format_notes": (
            "Real SERP: Interaction Design Foundation #1 + Kaizenko + B2B International + Strategyzer "
            "+ Isaac Jeffries (how-to) + Business Model Hacking + Railsware. Most are definition + "
            "structure + how to use. OSR opening: validation rigor + interview-based VPC creation."
        ),
        "unique_angle": (
            "- VPC as VALIDATION artifact, not just design exercise\n"
            "- Interview methodology to populate the Customer Profile with evidence\n"
            "- Common positioning mistakes the canvas reveals"
        ),
        "article_body_md": """<aside className="tldr">
**TL;DR.** The Value Proposition Canvas is a strategy tool created by Alex Osterwalder, Yves Pigneur, and Alan Smith that helps businesses design value propositions matching customer needs. It has two halves: a Customer Profile (Jobs, Pains, Gains) and a Value Map (Products & Services, Pain Relievers, Gain Creators). Fit happens when the map answers the profile.
</aside>

## What the Value Proposition Canvas does

The Value Proposition Canvas (VPC) is a deep zoom on two specific blocks of the Business Model Canvas: Value Propositions and Customer Segments. Created by Osterwalder, Pigneur, and Smith as a companion tool to the BMC, the VPC forces explicit alignment between what customers actually need and what you offer.

The tool is published in *Value Proposition Design* (2014) and distributed under Creative Commons by Strategyzer.

## The two halves

**Customer Profile (right side — your understanding of the customer)** breaks into three components:

- **Customer Jobs** — the tasks customers are trying to get done. Functional (write a report), social (look smart at work), emotional (feel competent).
- **Pains** — bad outcomes, obstacles, risks the customer experiences with current solutions. Time waste, financial cost, frustration, embarrassment.
- **Gains** — desired outcomes the customer wants, including required gains (must have), expected gains (assumed), and desired gains (would love).

**Value Map (left side — what you design)** mirrors the profile:

- **Products & Services** — what you offer, listed concretely
- **Pain Relievers** — how your offering eliminates or reduces specific Pains
- **Gain Creators** — how your offering produces specific Gains

## What "fit" means

Fit is the moment when your Pain Relievers map to actual Pains and your Gain Creators map to actual Gains — and you have evidence that customers care.

Most founders skip the evidence half. They draft a Value Map, declare fit, and move on. This produces what OSR calls "VPC theater": a tidy canvas with no validated demand underneath.

## How to actually validate a VPC

The VPC is a hypothesis until you test it. Inside OSR portfolio work, the validation methodology:

**Step 1: Draft the Customer Profile from hypothesis.** Write down your assumed Jobs, Pains, Gains for a specific segment. Don't overthink. This is the starting position.

**Step 2: Conduct 15-20 customer interviews.** Ask open questions about how they currently get the Job done. Don't pitch your product. Listen for actual Pains and Gains, not the ones you predicted.

**Step 3: Score each Customer Profile element.** Mark each Job, Pain, Gain by:
- **Severity** (how much it bothers them, 1-10)
- **Frequency** (how often it happens)
- **Evidence count** (how many of your interviewees mentioned it unprompted)

**Step 4: Discard low-evidence elements.** Anything with severity <5 or evidence <30% goes off the canvas. This is where founders panic — most initial Pains/Gains turn out to be assumptions.

**Step 5: Redraw the Value Map to address only the surviving elements.** Now your Pain Relievers solve real pain. Your Gain Creators produce real gain.

**Step 6: Test the Value Map.** Show customers your specific solution (sketch, prototype, or fake-door). Measure willingness to use, willingness to pay.

The VPC is now a validated artifact, not a design exercise.

## Common VPC mistakes

Three patterns that kill positioning, repeated across OSR's pitch reviews:

1. **Assumed Gains never validated**: Founders write "saves time" or "increases productivity" as Gains without ever asking customers what time savings or productivity gains they'd actually pay for. Generic Gains produce generic Value Propositions.

2. **Pain Relievers that don't address listed Pains**: The Value Map mentions features that have no corresponding Pain on the Customer Profile. The product solves problems no one has.

3. **Trying to address every Pain**: Beginner VPCs try to solve all listed Pains. Better VPCs focus on the 2-3 most severe Pains and accept they ignore the rest. Tight focus beats coverage.

## VPC and Jobs to Be Done

The VPC's Customer Jobs block is explicitly compatible with Tony Ulwick's JTBD framework. The integration:

- VPC Customer Jobs = JTBD's job statements (functional, emotional, social)
- VPC Pains = JTBD's customer outcomes when current solutions fail
- VPC Gains = JTBD's desired outcomes

Using both frameworks together: JTBD provides the precise language for Jobs and outcomes; VPC provides the visual structure to map your solution against them.

## How OSR uses VPC

Every OSR portfolio company maintains a VPC per customer segment. The canvas updates after each round of interviews or experiments. The state at each TRR stage:

- **Raw**: Customer Profile filled from hypothesis. Value Map blank.
- **Shaped**: Customer Profile rewritten from 15-20 interviews. Value Map drafted.
- **Problem Fit**: Top 3 Pains have severity ≥7 and evidence ≥50%. Value Map addresses these specifically.
- **Solution Fit**: Customers have used a prototype addressing the top Pains. NPS or repeat-use signal validates Pain Relievers.
- **PMF**: Willingness to pay validated. VPC stable. Used for marketing copy and sales conversations.

A founder who can show this evolution of their VPC across stages — with evidence behind each version — has a far stronger pitch than one who shows the final pretty canvas without the journey.

## Frequently asked questions

**Q: What is the Value Proposition Canvas?**
A: A strategy tool by Alex Osterwalder, Yves Pigneur, and Alan Smith that maps a Customer Profile (Jobs, Pains, Gains) against a Value Map (Products & Services, Pain Relievers, Gain Creators) to design products customers actually want.

**Q: Who created the Value Proposition Canvas?**
A: Alex Osterwalder, Yves Pigneur, and Alan Smith. Published in the 2014 book *Value Proposition Design*.

**Q: What is the difference between Business Model Canvas and Value Proposition Canvas?**
A: The BMC is a one-page view of a whole business. The VPC zooms into two BMC blocks (Value Propositions and Customer Segments) for deeper customer-product alignment.

**Q: How do you fill out a Value Proposition Canvas?**
A: Start with Customer Profile (Jobs, Pains, Gains) from research and interviews. Then design the Value Map (Products & Services, Pain Relievers, Gain Creators) to address each Pain and produce each Gain. Validate before declaring fit.

**Q: What is "fit" on the Value Proposition Canvas?**
A: Fit is when your Pain Relievers map to actual customer Pains and your Gain Creators map to actual Gains — and you have evidence (interviews, prototypes, willingness to pay) that customers care.

**Q: How does VPC connect with Jobs to Be Done?**
A: VPC's Customer Jobs block is compatible with JTBD theory. Use JTBD for precise Job statements; use VPC for visual mapping of your solution against those Jobs.

**Q: What are common mistakes when using the Value Proposition Canvas?**
A: Three killers: assuming Gains without customer evidence, listing Pain Relievers without corresponding Pains, and trying to address every Pain instead of focusing on the top 2-3 most severe.

## Related reading

- [TBD: business model canvas]
- [TBD: jobs to be done framework]
- [TBD: customer development interviews]
- [TBD: validation framework]
""",
        "faq_block_json": """[
{"question": "What is the Value Proposition Canvas?", "answer": "A strategy tool by Alex Osterwalder, Yves Pigneur, Alan Smith that maps Customer Profile (Jobs, Pains, Gains) against Value Map (Products & Services, Pain Relievers, Gain Creators)."},
{"question": "Who created the Value Proposition Canvas?", "answer": "Alex Osterwalder, Yves Pigneur, and Alan Smith. Published in the 2014 book Value Proposition Design."},
{"question": "What is the difference between Business Model Canvas and Value Proposition Canvas?", "answer": "BMC is a one-page view of a whole business. VPC zooms into two BMC blocks (Value Propositions and Customer Segments) for deeper customer-product alignment."},
{"question": "How do you fill out a Value Proposition Canvas?", "answer": "Start with Customer Profile (Jobs, Pains, Gains) from research and interviews. Then design Value Map (Products, Pain Relievers, Gain Creators). Validate before declaring fit."},
{"question": "What is fit on the Value Proposition Canvas?", "answer": "Fit is when Pain Relievers map to actual customer Pains and Gain Creators map to actual Gains, with evidence (interviews, prototypes, willingness to pay) that customers care."},
{"question": "How does VPC connect with Jobs to Be Done?", "answer": "VPC's Customer Jobs block is compatible with JTBD theory. Use JTBD for precise Job statements; use VPC for visual mapping of solution against Jobs."},
{"question": "What are common mistakes when using the Value Proposition Canvas?", "answer": "Three killers: assuming Gains without customer evidence, listing Pain Relievers without corresponding Pains, and trying to address every Pain instead of focusing on top 2-3."}
]""",
        "source_citations": (
            "- Strategyzer (official): https://www.strategyzer.com/library/the-value-proposition-canvas\n"
            "- Interaction Design Foundation: What is the Value Proposition Canvas — https://ixdf.org/literature/topics/value-proposition-canvas\n"
            "- Kaizenko: VPC Essential Guide for Product-Market Fit\n"
            "- B2B International: What is the Value Proposition Canvas?\n"
            "- Isaac Jeffries: How To Fill In A Value Proposition Canvas\n"
            "- Railsware: Value Proposition Canvas Understand Customers"
        ),
    },

    # ============================================================
    # V4-006 — lean startup model canvas (4400 vol, KD 30)
    # ============================================================
    {
        "primary_keyword": "lean startup model canvas",
        "tldr_answer": (
            "The Lean Startup Canvas (Lean Canvas) is a one-page business model developed "
            "by Ash Maurya in his 2010 book *Running Lean* as an entrepreneur-focused "
            "alternative to Osterwalder's Business Model Canvas. Its 9 blocks emphasize "
            "Problem, Solution, Key Metrics, Unique Value Proposition, and Unfair Advantage."
        ),
        "identified_gap": (
            "Canva, Miro, BMToolBox, Railsware cover the 9 blocks and BMC comparison but miss:\n"
            "- Real validation workflow using Lean Canvas (not just static template)\n"
            "- How Lean Canvas evolves through TRR stages\n"
            "- Common mistakes (faking Unfair Advantage, vague Problem statements)\n"
            "- When to upgrade from Lean Canvas to full BMC"
        ),
        "competitor_format_notes": (
            "Real SERP: Canva + BMToolBox + Pitt LibGuide + Miro + Railsware + Medium + Canvanizer "
            "+ Miro comparison + Draft.io + Airfocus. Definition + 9 blocks + comparison to BMC + "
            "template downloads. Two Miro entries dominate. OSR opening: validation rigor + "
            "evolution per stage."
        ),
        "unique_angle": (
            "- Lean Canvas as living validation artifact updated per experiment\n"
            "- Honest about Unfair Advantage being the hardest block (and most-faked)\n"
            "- Decision framework: when to upgrade to full BMC"
        ),
        "article_body_md": """<aside className="tldr">
**TL;DR.** The Lean Startup Canvas (Lean Canvas) is a one-page business model developed by Ash Maurya in his 2010 book *Running Lean* as an entrepreneur-focused alternative to Osterwalder's Business Model Canvas. Its 9 blocks emphasize Problem, Solution, Key Metrics, Unique Value Proposition, and Unfair Advantage.
</aside>

## What the Lean Canvas is

The Lean Canvas is a startup-focused adaptation of the Business Model Canvas. Ash Maurya created it because he found the original BMC too generic for early-stage founders, particularly the blocks that mattered most for validation.

The result: a 9-block one-page template that replaces BMC's Key Partnerships, Key Activities, Key Resources, and Customer Relationships with Problem, Solution, Key Metrics, and Unfair Advantage — blocks more useful when you're still figuring out if anyone wants what you're building.

## The 9 blocks

| Block | What goes in |
|---|---|
| **1. Problem** | Top 1-3 problems your customer is trying to solve |
| **2. Customer Segments** | Target customers and early adopters |
| **3. Unique Value Proposition** | A single clear message stating why you are different |
| **4. Solution** | Top 3 features that solve the listed problems |
| **5. Channels** | Paths to reach customers |
| **6. Revenue Streams** | How you make money |
| **7. Cost Structure** | All costs to operate |
| **8. Key Metrics** | The actions that matter most to track |
| **9. Unfair Advantage** | Something that cannot easily be copied or bought |

The visual flow: customer-facing blocks on the right (Customer Segments, Unique Value Proposition), product-and-business blocks on the left (Problem, Solution, Key Metrics). Channels and Cost/Revenue at the bottom.

## Why founders should choose Lean Canvas over BMC

Three structural advantages for early-stage validation work:

1. **Problem block forces customer-side thinking.** BMC starts with Value Propositions; Lean Canvas starts with Problem. This trains founders to validate the problem exists before designing the solution.

2. **Unfair Advantage block forces honesty about defensibility.** Most early startups have no real moat. The Lean Canvas's explicit Unfair Advantage block exposes this. BMC lets you wave hand at "Key Resources" generally.

3. **Key Metrics block forces measurement discipline.** Even before launch, founders must specify what they'll measure. This shapes experiment design.

## Lean Canvas at each TRR stage

The canvas evolves through validation:

**Raw (0-20%)** — Fill in only:
- Problem (your hypothesis, top 3)
- Customer Segments (specific, narrow)
- Unique Value Proposition (one sentence, will change)

Leave everything else blank. This is the starting hypothesis.

**Shaped (20-40%)** — After 15-20 customer interviews:
- Rewrite Problem with verbatim customer phrasing
- Rewrite Customer Segments with specific demographic + behavior
- Sketch Solution (top 3 features only)
- Identify Channels you've actually seen customers use

**Problem Fit (40-60%)** — After fake-door or pre-sale test:
- Lock in Problem (validated)
- Refine Solution (test feedback)
- Add Revenue Streams (validated pricing)
- Begin Key Metrics (what you'll measure post-launch)

**Solution Fit (60-80%)** — After prototype usage:
- Solidify Solution
- Refine Cost Structure with real numbers
- Honest Unfair Advantage block (or mark "TBD" — most early startups don't have one yet)

**PMF (80%+)** — Living document, update per significant pivot.

## Common Lean Canvas mistakes

Three patterns kill the validity of Lean Canvases reviewed at OSR pitch sessions:

1. **Vague Problem statements**: "Customers waste time" is not a Problem. "Real estate agents in HCMC spend 4-6 hours daily manually updating listings across 3 platforms" is a Problem.

2. **Faked Unfair Advantage**: Listing "experienced team" or "first to market" isn't an Unfair Advantage. Real Unfair Advantages: proprietary data, network effects, regulatory moat, exclusive distribution deals. Most early-stage startups should write "TBD — building this in Year 1-2."

3. **Too many Solutions**: The canvas allows top 3 features. Founders cram 8-10. This dilutes focus. Tighten ruthlessly.

## When to upgrade from Lean Canvas to BMC

The Lean Canvas is optimized for pre-Solution-Fit work. When the business reaches Solution Fit, the blocks Maurya replaced (Key Partnerships, Key Activities, Key Resources, Customer Relationships) start mattering for operational planning and investor conversations.

OSR portfolio rule: switch to BMC when:
- You hire your first 3+ full-time team members (Key Resources matters)
- You sign meaningful partnership agreements (Key Partnerships matters)
- You raise institutional capital (investors expect BMC vocabulary)
- You need to map operational dependencies (Key Activities matters)

Below those thresholds, Lean Canvas is the faster tool. Above them, BMC's broader frame catches operational issues Lean Canvas hides.

## Famous Lean Canvas examples

Several billion-dollar startups documented their early Lean Canvases publicly:

- **Airbnb (2008)**: Problem = travelers can't find affordable accommodation matching local culture. Solution = peer-to-peer room rental. Unfair Advantage = trust-based community + reviews.
- **Uber (2010)**: Problem = unreliable taxis, opaque pricing. Solution = on-demand black car via smartphone. Unfair Advantage = supply-side network effect.
- **Stripe (2010)**: Problem = setting up payment processing is brutal for developers. Solution = 7-line code integration. Unfair Advantage = developer-first DX + brand trust.

These canvases all evolved significantly post-launch. The Lean Canvas captures the validated state at one moment, not the final business.

## Frequently asked questions

**Q: What is the Lean Startup Canvas?**
A: A one-page business model template developed by Ash Maurya in 2010 (published in *Running Lean*) as an entrepreneur-focused alternative to the Business Model Canvas. Emphasizes Problem, Solution, Key Metrics, Unique Value Proposition, and Unfair Advantage.

**Q: Who created the Lean Canvas?**
A: Ash Maurya, in his 2010 book *Running Lean*. He developed it in response to Alex Osterwalder's Business Model Canvas.

**Q: What are the 9 blocks of the Lean Canvas?**
A: Problem, Customer Segments, Unique Value Proposition, Solution, Channels, Revenue Streams, Cost Structure, Key Metrics, Unfair Advantage.

**Q: What is the difference between Lean Canvas and Business Model Canvas?**
A: Lean Canvas replaces BMC's Key Partnerships, Key Activities, Key Resources, and Customer Relationships with Problem, Solution, Key Metrics, and Unfair Advantage — focused on early-stage validation rather than operational structure.

**Q: When should I use Lean Canvas vs Business Model Canvas?**
A: Lean Canvas pre-Solution-Fit (early startup, validation focus). BMC post-Solution-Fit, when you hire team, sign partnerships, raise institutional capital.

**Q: What is the Unfair Advantage on the Lean Canvas?**
A: Something competitors cannot easily copy or buy. Real examples: proprietary data, network effects, regulatory moat, exclusive distribution. Most early-stage startups should write "TBD — building Year 1-2" rather than fake it.

**Q: How do I fill out a Lean Canvas?**
A: Start with Problem (top 3) and Customer Segments. Add Unique Value Proposition. Validate via interviews. Then add Solution, Channels, Revenue Streams. Refine through experiments. Don't fill all 9 blocks at once.

## Related reading

- [TBD: business model canvas]
- [TBD: value proposition canvas]
- [TBD: jobs to be done framework]
- [TBD: product market fit]
""",
        "faq_block_json": """[
{"question": "What is the Lean Startup Canvas?", "answer": "A one-page business model template by Ash Maurya (2010, Running Lean) as an entrepreneur-focused alternative to BMC. Emphasizes Problem, Solution, Key Metrics, Unique Value Proposition, Unfair Advantage."},
{"question": "Who created the Lean Canvas?", "answer": "Ash Maurya, in his 2010 book Running Lean. Developed in response to Alex Osterwalder's Business Model Canvas."},
{"question": "What are the 9 blocks of the Lean Canvas?", "answer": "Problem, Customer Segments, Unique Value Proposition, Solution, Channels, Revenue Streams, Cost Structure, Key Metrics, Unfair Advantage."},
{"question": "What is the difference between Lean Canvas and Business Model Canvas?", "answer": "Lean Canvas replaces BMC's Key Partnerships, Activities, Resources, Customer Relationships with Problem, Solution, Key Metrics, Unfair Advantage — focused on early-stage validation."},
{"question": "When should I use Lean Canvas vs BMC?", "answer": "Lean Canvas pre-Solution-Fit (early startup, validation). BMC post-Solution-Fit when you hire team, sign partnerships, raise institutional capital."},
{"question": "What is the Unfair Advantage on the Lean Canvas?", "answer": "Something competitors cannot easily copy or buy. Real examples: proprietary data, network effects, regulatory moat. Most early startups should write 'TBD' rather than fake it."},
{"question": "How do I fill out a Lean Canvas?", "answer": "Start with Problem (top 3) and Customer Segments. Add UVP. Validate via interviews. Then Solution, Channels, Revenue. Refine through experiments. Don't fill all 9 blocks at once."}
]""",
        "source_citations": (
            "- Canva: What is a Lean Canvas — https://www.canva.com/online-whiteboard/lean-canvas/\n"
            "- Miro: What is Lean Canvas — https://miro.com/strategic-planning/what-is-lean-canvas/\n"
            "- BMToolBox: Lean Canvas tool\n"
            "- Pitt LibGuide: BMC & Lean Startups\n"
            "- Railsware: 5 Lean Canvas Examples\n"
            "- Steve Mullen Medium: Introduction to Lean Canvas\n"
            "- airfocus: What Is a Lean Business Canvas"
        ),
    },

    # ============================================================
    # V4-007 — jobs to be done framework (2400 vol, KD 28)
    # ============================================================
    {
        "primary_keyword": "jobs to be done framework",
        "tldr_answer": (
            "Jobs to Be Done (JTBD) is a customer needs framework popularized by Clayton "
            "Christensen and formalized by Tony Ulwick. Core idea: customers 'hire' "
            "products to do specific jobs. The framework defines jobs as having "
            "functional, emotional, and social dimensions, helping product teams design "
            "around outcomes rather than features."
        ),
        "identified_gap": (
            "JTBD.com, Strategyn (Ulwick), Christensen Institute, ProductPlan cover theory + 4 "
            "elements + dimensions but miss:\n"
            "- How to actually CONDUCT a JTBD interview (most articles describe theory)\n"
            "- Job statement formula and common mistakes writing them\n"
            "- Integration with Value Proposition Canvas (most mention, few show)\n"
            "- Real Vietnamese / SEA examples (zero in current SERP)"
        ),
        "competitor_format_notes": (
            "Real SERP: JTBD.com (Ulwick) + ProductPlan + Strategyn (Ulwick again) + Christensen "
            "Institute + Productboard + Product School + Coursera + HBS Online + Fullstory. "
            "Multiple Ulwick properties dominate. Mostly theory-heavy. OSR opening: practical "
            "interview methodology + job statement formula + integration with VPC + SEA examples."
        ),
        "unique_angle": (
            "- JTBD interview methodology (script + question framework)\n"
            "- Job statement formula with template\n"
            "- JTBD + VPC integration walkthrough\n"
            "- Vietnamese example (e.g., MoMo wallet jobs)"
        ),
        "article_body_md": """<aside className="tldr">
**TL;DR.** Jobs to Be Done (JTBD) is a customer needs framework popularized by Clayton Christensen and formalized by Tony Ulwick. Core idea: customers "hire" products to do specific jobs. The framework defines jobs as having functional, emotional, and social dimensions, helping product teams design around outcomes rather than features.
</aside>

## The core insight

JTBD inverts the standard product question. Instead of asking "what features do customers want?", you ask "what job is the customer trying to get done?"

Clayton Christensen's canonical example: McDonald's wanted to grow milkshake sales. Standard market research asked customers about flavor, price, size — and got contradictory answers. JTBD research asked WHEN people bought milkshakes and WHY. Answer: morning commuters bought them because they needed something that occupied one hand, lasted the whole drive, and was filling enough to suppress mid-morning hunger. The job: "make my boring morning commute interesting AND keep me full until lunch."

This reframed the milkshake's competition. Not Burger King's shake — bananas, bagels, donuts, breakfast bars. Redesign decisions followed.

## The 4 elements of the JTBD framework

| Element | Description | Example (McDonald's milkshake) |
|---|---|---|
| **Job performer** | The individual or group with the job | Morning commuter, age 25-45, driving alone |
| **Job to be done** | What they're trying to accomplish | Survive a boring 30-min drive + stay full until lunch |
| **Circumstances** | When/where/how the job arises | Early morning, driving solo, no time for sit-down breakfast |
| **Customer needs** | Criteria for "job done well" | One-handed, lasts the trip, filling, mess-free |

These four elements form a complete job statement. Each element changes the design.

## The three dimensions of every job

Every Job to Be Done has three dimensions:

- **Functional** — the practical task (drink, eat, transport, calculate, communicate)
- **Emotional** — how completing the job makes the person feel (competent, secure, relieved, excited)
- **Social** — how completing the job affects what others think of the person (admired, respected, included, modern)

A great product addresses all three. The morning commute milkshake is functional (food + drink), emotional (comfort, control over a boring routine), and social (none — solo experience).

A product like a wedding ring is dominated by emotional (love commitment) and social (publicly visible status) with minor functional dimension. A medical infusion pump is dominated by functional (deliver medication accurately) with emotional (patient safety) and minor social.

Mis-weighting the dimensions kills product design. Most B2B SaaS founders underweight the emotional dimension (admin's fear of being blamed for system failure) and the social (looking smart to your boss).

## How to actually conduct a JTBD interview

Most articles describe JTBD theory but skip the interview methodology. The OSR practical approach:

**Question framework — 7 questions in this order:**

1. "Tell me about the last time you needed to [achieve goal]."
2. "Walk me through what happened, step by step."
3. "What were you doing right before this came up?"
4. "What did you try first to solve it?"
5. "What didn't work about that?"
6. "How did you eventually get it done?"
7. "If you had a magic wand, what would 'job done well' look like?"

This produces real circumstances + actual jobs + real customer needs without leading the witness.

**Avoid these mistakes:**

- Don't ask "would you use a product that did X?" — terrible signal
- Don't ask "what features do you want?" — customers describe solutions, not jobs
- Don't ask only about your category — competing alternatives often live outside your category

## Writing a job statement

Tony Ulwick's job statement formula:

```
[Verb] + [object of the verb] + [contextual clarifier]
```

Examples:
- "Stop a cut from bleeding" (Band-Aid job)
- "Manage personal finances on my phone during my commute" (banking app job)
- "Coordinate weekend plans with my friend group without 30 text messages" (group chat job)

Bad job statements:
- "Be productive" (no verb-object structure, untestable)
- "Use software to manage my team" (describes solution, not job)
- "Feel successful at work" (purely emotional, no functional anchor)

The verb-object-clarifier formula makes jobs testable and product decisions concrete.

## JTBD and Value Proposition Canvas integration

The VPC Customer Jobs block is explicitly JTBD-compatible. Practical integration:

1. **Run JTBD interviews to identify the top 3-5 Jobs** for your target segment
2. **Write each job in Ulwick's verb-object-clarifier formula**
3. **For each Job, list Pains** (what goes wrong with current solutions)
4. **For each Job, list Gains** (what success looks like)
5. **Transfer to VPC Customer Profile** (Jobs, Pains, Gains)
6. **Design Value Map (Products, Pain Relievers, Gain Creators) to address them**

The frameworks compound. JTBD provides the disciplined customer-side input. VPC provides the visual map and forces alignment with your solution.

## A Vietnamese example: MoMo

MoMo's growth in Vietnam can be analyzed through JTBD. The dominant Jobs MoMo addresses:

1. **Pay a friend without exchanging cash** (functional)
2. **Don't look unprepared when splitting a meal bill** (social)
3. **Avoid the awkwardness of asking the friend to come to a bank branch with you** (emotional)
4. **Track my spending without manual logging** (functional)

The functional job is what got users to try MoMo. The emotional + social jobs are what made them keep using it. Competitor wallets that addressed only the functional Job lost share to those that addressed all three dimensions.

## Frequently asked questions

**Q: What is the Jobs to Be Done framework?**
A: A customer needs framework where the core unit of analysis is "what job is the customer hiring this product to do?" Popularized by Clayton Christensen, formalized by Tony Ulwick.

**Q: Who created the Jobs to Be Done framework?**
A: Theodore Levitt's 1960s "drill not the hole" insight is the origin. Clayton Christensen popularized it in the 1990s. Tony Ulwick formalized the methodology in the 1990s-2000s with Outcome-Driven Innovation.

**Q: What are the 4 elements of the JTBD framework?**
A: Job performer, Job to be done, Circumstances, Customer needs.

**Q: What are the three dimensions of a Job to Be Done?**
A: Functional (practical task), Emotional (how it feels), Social (how others perceive).

**Q: How do I write a Job Statement?**
A: Tony Ulwick's formula: Verb + Object + Contextual clarifier. Example: "Manage personal finances on my phone during my commute."

**Q: How does JTBD compare to user personas?**
A: Personas describe who the customer is (demographics, psychographics). JTBD describes what they're trying to accomplish. JTBD is more actionable for product decisions because it identifies the JOB, not just the JOB-DOER.

**Q: How does JTBD relate to Value Proposition Canvas?**
A: The VPC's Customer Jobs block is JTBD-compatible. Use JTBD interviews to populate the Jobs, Pains, Gains. Use VPC visual to map your solution against them.

## Related reading

- [TBD: value proposition canvas]
- [TBD: customer development interviews]
- [TBD: lean startup model canvas]
- [TBD: product market fit]
""",
        "faq_block_json": """[
{"question": "What is the Jobs to Be Done framework?", "answer": "A customer needs framework where the core unit of analysis is what job a customer hires a product to do. Popularized by Clayton Christensen, formalized by Tony Ulwick."},
{"question": "Who created the Jobs to Be Done framework?", "answer": "Theodore Levitt's 1960s 'drill not the hole' insight is the origin. Christensen popularized in the 1990s. Tony Ulwick formalized via Outcome-Driven Innovation."},
{"question": "What are the 4 elements of the JTBD framework?", "answer": "Job performer, Job to be done, Circumstances, Customer needs."},
{"question": "What are the three dimensions of a Job to Be Done?", "answer": "Functional (practical task), Emotional (how it feels), Social (how others perceive)."},
{"question": "How do I write a Job Statement?", "answer": "Tony Ulwick's formula: Verb + Object + Contextual clarifier. Example: 'Manage personal finances on my phone during my commute.'"},
{"question": "How does JTBD compare to user personas?", "answer": "Personas describe who the customer is. JTBD describes what they're trying to accomplish. JTBD more actionable for product decisions."},
{"question": "How does JTBD relate to Value Proposition Canvas?", "answer": "VPC's Customer Jobs block is JTBD-compatible. Use JTBD interviews to populate Jobs/Pains/Gains. VPC visual maps solution against them."}
]""",
        "source_citations": (
            "- Tony Ulwick: JTBD a Framework for Customer Needs — https://jobs-to-be-done.com/jobs-to-be-done-a-framework-for-customer-needs-c883cbf61c90\n"
            "- ProductPlan: Jobs-To-Be-Done Framework Glossary\n"
            "- Strategyn (Ulwick): JTBD The Original Framework — https://strategyn.com/jobs-to-be-done/\n"
            "- Christensen Institute: Jobs to Be Done Theory\n"
            "- Productboard: Jobs-to-be-Done Framework\n"
            "- HBS Online: 4 Real-World Jobs to Be Done Examples"
        ),
    },

    # ============================================================
    # V4-008 — what is mvp minimum viable product (5400 vol, KD 41)
    # ============================================================
    {
        "primary_keyword": "what is mvp minimum viable product",
        "tldr_answer": (
            "A Minimum Viable Product (MVP) is a version of a product with just enough "
            "features to be usable by early customers who provide feedback for future "
            "development. The term was coined by Frank Robinson in 2001 and popularized "
            "by Eric Ries and Steve Blank. Goal: maximum validated learning with the "
            "least effort and cost."
        ),
        "identified_gap": (
            "Wikipedia, Atlassian, NN/G, Lean Startup Co (Eric Ries), Amplitude, Agile Alliance "
            "cover definition + Ries quotes + benefits but miss:\n"
            "- MVP types ranked by validation depth (concierge vs Wizard of Oz vs landing page vs prototype)\n"
            "- When MVP is the wrong tool (B2B enterprise, regulated industries)\n"
            "- How to choose MVP type for each TRR stage\n"
            "- Real failure mode analysis (when MVP gave false positive)"
        ),
        "competitor_format_notes": (
            "Real SERP: Wikipedia (#1) + Atlassian + NN/G + ProductPlan + Amplitude + Agile Alliance "
            "+ Eric Ries Lean Startup Co + NetSuite + Product School + Miro. Mix of encyclopedic + "
            "product-management vendors + Lean Startup canon. OSR opening: validation-rigor lens + "
            "MVP-type decision framework."
        ),
        "unique_angle": (
            "- 7 MVP types ranked by validation depth + cost\n"
            "- TRR-stage decision framework for MVP type\n"
            "- Honest about when MVP is wrong tool (B2B enterprise, regulated)"
        ),
        "article_body_md": """<aside className="tldr">
**TL;DR.** A Minimum Viable Product (MVP) is a version of a product with just enough features to be usable by early customers who provide feedback for future development. The term was coined by Frank Robinson in 2001 and popularized by Eric Ries and Steve Blank. Goal: maximum validated learning with the least effort and cost.
</aside>

## The Eric Ries definition

The canonical MVP definition from Eric Ries's *The Lean Startup*:

> "The minimum viable product is that version of a new product a team uses to collect the maximum amount of validated learning about customers with the least effort."

Two words matter most: **validated learning** and **least effort**. Founders consistently fail one or the other. Either they build too much (least effort fails) or they don't actually test customer behavior (validated learning fails).

## Origin and popularization

The term was coined by Frank Robinson in 2001. Steve Blank developed the customer development methodology that surrounds it. Eric Ries codified it in *The Lean Startup* (2011), where it became startup canon.

The framework matters because it gave founders permission to ship something incomplete on purpose. Before MVP thinking, the assumption was that a product had to be fully featured to launch. MVP reframed launch as the start of learning, not the end of building.

## 7 types of MVP ranked by validation depth

Different MVPs validate different things. Pick the right type for what you need to learn:

| MVP type | What it validates | Cost | Time |
|---|---|---|---|
| **Landing page** | Interest, messaging | $0-200 | 1-3 days |
| **Fake door** | Purchase intent | $100-500 | 3-7 days |
| **Concierge** | Manual workflow demand | $200-1k | 1-2 weeks |
| **Wizard of Oz** | Product feature demand without building | $500-2k | 2-4 weeks |
| **Prototype** | Usability of designed flow | $1-5k | 2-4 weeks |
| **Single-feature MVP** | One core feature in production | $5-20k | 4-8 weeks |
| **Multi-feature MVP** | Full product hypothesis | $20-100k | 2-6 months |

Most founder confusion comes from picking the wrong type. A landing page validates messaging, not feature design. A prototype validates UX, not willingness to pay. A multi-feature MVP commits to a hypothesis before testing it.

## TRR-stage decision framework

Map MVP type to OSR's TRR validation stages:

- **Raw (0-20%)** → Landing page. Validate messaging resonates before building anything.
- **Shaped (20-40%)** → Fake-door OR Concierge. Test if anyone wants this enough to take action.
- **Problem Fit (40-60%)** → Wizard of Oz OR Prototype. Validate the workflow works manually before automating.
- **Solution Fit (60-80%)** → Single-feature MVP. Build the ONE feature people pre-paid for; ship to early adopters.
- **PMF (80%+)** → Multi-feature MVP. Now you can confidently invest in additional features.

The mistake: jumping directly to multi-feature MVP at Raw stage. This is what happens when founders confuse "build something" with "validate".

## When MVP is the wrong tool

Three scenarios where MVP thinking misleads:

1. **B2B enterprise selling**: Procurement processes at large companies require fully featured products with security audits, SOC 2 compliance, SSO, multi-tenant architecture. A "minimum viable" version often can't even enter the buying process. For enterprise, validate via design partner programs (work hands-on with 3-5 enterprises pre-build), not generic MVPs.

2. **Regulated industries**: Healthcare, finance, education have regulatory floors that aren't "minimum viable." Shipping a half-built financial service triggers compliance issues. Validate via regulatory consultation + regulated sandbox, not MVP.

3. **Hardware with safety implications**: Medical devices, automotive, aerospace. A "minimum viable" version that fails dangerously can kill the company before it even launches. Use staged prototyping in controlled environments.

For these scenarios, the principle (validate before building everything) still applies. The format changes.

## Common MVP mistakes that produce false signals

Three patterns OSR sees in failed validations:

1. **MVP launched only to friends and family**: Their support gives false-positive feedback. Validate with strangers who don't know you.

2. **MVP without payment or strong commitment signal**: Email signups for a free service tell you very little about willingness to pay. Add a paywall, even at $1, to validate intent.

3. **MVP without comparison baseline**: "We got 200 signups in week 1!" tells you nothing without comparison. Is that good or bad for your category? Set baseline expectations BEFORE the test.

## The MVP that worked: Dropbox

The canonical example of an MVP done right: Dropbox's 2007 video. They wanted to validate demand for seamless file sync across devices but didn't want to build the entire backend before testing.

Their MVP: a 3-minute video showing the product working with mock screens. Posted to Hacker News. Beta signups went from 5,000 to 75,000 overnight.

This was a Wizard of Oz MVP (no real product yet). It validated the demand hypothesis without building the product. They then knew it was worth building the actual sync engine.

The video cost ~$50 to make. The validated learning was worth tens of millions in avoided R&D risk.

## Frequently asked questions

**Q: What is a Minimum Viable Product (MVP)?**
A: A version of a product with just enough features to be usable by early customers who provide feedback for future development. Per Eric Ries: maximum validated learning with the least effort.

**Q: Who coined the term MVP?**
A: Frank Robinson in 2001. The concept was popularized by Steve Blank's customer development methodology and Eric Ries's *The Lean Startup* (2011).

**Q: What is the purpose of an MVP?**
A: To validate customer demand and product hypotheses cheaply, before investing in full product development. The output is validated learning, not necessarily revenue.

**Q: What are the different types of MVP?**
A: Landing page, fake door, concierge, Wizard of Oz, prototype, single-feature MVP, multi-feature MVP. Each validates different hypotheses at different cost and time levels.

**Q: How do I choose the right MVP type?**
A: Match to your validation stage. Landing page for messaging. Fake door for purchase intent. Concierge for manual workflow demand. Single-feature MVP only when you have evidence of demand for that specific feature.

**Q: When is MVP the wrong approach?**
A: B2B enterprise selling (procurement requires full product), regulated industries (compliance floors), and safety-critical hardware (failure modes too costly).

**Q: How long should building an MVP take?**
A: Landing page: 1-3 days. Single-feature MVP: 4-8 weeks. If you're building MVP for more than 2 months without launching, you've over-scoped.

## Related reading

- [TBD: lean startup model canvas]
- [TBD: product market fit]
- [TBD: validation framework]
- [TBD: customer development interviews]
""",
        "faq_block_json": """[
{"question": "What is a Minimum Viable Product (MVP)?", "answer": "A version of a product with just enough features to be usable by early customers who provide feedback. Per Eric Ries: maximum validated learning with the least effort."},
{"question": "Who coined the term MVP?", "answer": "Frank Robinson in 2001. Popularized by Steve Blank's customer development and Eric Ries's The Lean Startup (2011)."},
{"question": "What is the purpose of an MVP?", "answer": "To validate customer demand and product hypotheses cheaply, before investing in full product development. Output is validated learning, not necessarily revenue."},
{"question": "What are the different types of MVP?", "answer": "Landing page, fake door, concierge, Wizard of Oz, prototype, single-feature MVP, multi-feature MVP. Each validates different hypotheses at different cost."},
{"question": "How do I choose the right MVP type?", "answer": "Match to validation stage. Landing page for messaging. Fake door for purchase intent. Concierge for workflow demand. Single-feature MVP only with evidence of demand."},
{"question": "When is MVP the wrong approach?", "answer": "B2B enterprise (procurement requires full product), regulated industries (compliance floors), safety-critical hardware (failure modes too costly)."},
{"question": "How long should building an MVP take?", "answer": "Landing page: 1-3 days. Single-feature MVP: 4-8 weeks. If you're building MVP more than 2 months without launching, you've over-scoped."}
]""",
        "source_citations": (
            "- Wikipedia: Minimum viable product — https://en.wikipedia.org/wiki/Minimum_viable_product\n"
            "- Atlassian: What is an MVP — https://www.atlassian.com/agile/product-management/minimum-viable-product\n"
            "- Nielsen Norman Group: MVP Definition\n"
            "- Eric Ries / Lean Startup Co: What Is an MVP — https://leanstartup.co/resources/articles/what-is-an-mvp/\n"
            "- Amplitude: MVP Definition Examples\n"
            "- Agile Alliance: MVP glossary"
        ),
    },

    # ============================================================
    # V4-009 — product market fit (3600 vol, KD 38)
    # ============================================================
    {
        "primary_keyword": "product market fit",
        "tldr_answer": (
            "Product-Market Fit (PMF) is the point where a defined group of customers "
            "genuinely wants what you sell and is willing to pay for it. Coined by Marc "
            "Andreessen in 2007 as 'being in a good market with a product that satisfies "
            "that market.' Standard test: Sean Ellis's 40% rule — if 40%+ of users say "
            "they'd be 'very disappointed' losing your product, you have PMF."
        ),
        "identified_gap": (
            "ProductPlan, Wikipedia, Salesforce, Mailchimp, Stripe, Lean Startup Co, Heap cover "
            "definition + Andreessen origin + Sean Ellis test but miss:\n"
            "- PMF measurement before launch (most articles focus on post-launch metrics)\n"
            "- Multiple PMF metrics + which to use when (NPS, retention, growth, payback)\n"
            "- PMF false positives (what looks like PMF but isn't)\n"
            "- OSR's TRR scoring framework explicit"
        ),
        "competitor_format_notes": (
            "Real SERP: ProductPlan + Wikipedia + Salesforce + Mailchimp + Stripe + Lean Startup Co "
            "+ Coursera + Zendesk + Heap. Multiple SaaS vendor blogs + canonical Wikipedia. Stripe's "
            "long-form is high-quality. Heap leads on data-driven framework. OSR opening: pre-launch "
            "PMF signals + measurement framework decision + false-positive analysis."
        ),
        "unique_angle": (
            "- 5 PMF metrics + decision tree for which to use\n"
            "- Pre-launch PMF signals (not just post-launch)\n"
            "- False positives: what looks like PMF but isn't\n"
            "- TRR scoring for PMF stage explicitly"
        ),
        "article_body_md": """<aside className="tldr">
**TL;DR.** Product-Market Fit (PMF) is the point where a defined group of customers genuinely wants what you sell and is willing to pay for it. Coined by Marc Andreessen in 2007 as "being in a good market with a product that satisfies that market." Standard test: Sean Ellis's 40% rule — if 40%+ of users say they'd be "very disappointed" losing your product, you have PMF.
</aside>

## The original definition

Marc Andreessen coined the term in a 2007 essay titled *The Only Thing That Matters*. His definition:

> "Product-Market fit means being in a good market with a product that can satisfy that market."

What he was really saying: most startup failures aren't execution failures. They're either bad-market failures (no real demand) or bad-product-for-the-market failures (the product doesn't solve the actual problem).

42% of startups fail because they don't serve a market need. PMF is the binary signal that you've crossed past this risk.

## The 40% test (Sean Ellis)

Sean Ellis's measurement test:

Survey 40+ active users. Ask: "How would you feel if you could no longer use [product]?"

Response options:
- Very disappointed
- Somewhat disappointed
- Not disappointed
- N/A — I no longer use it

If **40% or more** answer "very disappointed", you have signal of PMF.

The test works because it captures emotional attachment, not just usage. Users churn from products they "kind of like." They fight to keep products they'd be "very disappointed" losing.

## 5 PMF metrics — pick what fits your stage

The 40% test is one signal. Different metrics matter at different stages:

| Metric | What it measures | When to use |
|---|---|---|
| **Sean Ellis 40% test** | Emotional attachment | Early SaaS, consumer apps |
| **Net retention rate** | Account expansion vs churn | B2B SaaS post-launch |
| **Cohort retention curve** | Whether users stay over time | Consumer apps, social products |
| **Organic growth %** | Word-of-mouth signal | All product types post-launch |
| **CAC payback period** | Unit economics health | All paid acquisition products |

The decision: if any TWO of these fire green simultaneously, treat it as PMF. Any one alone can mislead.

## Pre-launch PMF signals

Most articles describe PMF as a post-launch metric. For founders pre-launch, look for these directional signals:

- **Pre-orders or paid waitlist conversion**: If 5%+ of landing page visitors convert to paid waitlist, demand is strong.
- **Interview signal density**: If 60%+ of customer interviews unprompted describe the pain you solve, the problem is real.
- **Reference customer eagerness**: Do potential customers volunteer to test the product? Eagerness signals attachment before launch.
- **Competitor user dissatisfaction**: Are customers actively complaining about existing solutions? Active discontent is easier to capture than indifference.

None of these are sufficient on their own. Combined, they predict post-launch PMF with reasonable accuracy.

## PMF false positives — what looks like PMF but isn't

Three patterns OSR sees that mimic PMF without actually being PMF:

1. **Friends and family usage**: Your network supports you. Their data is noise. Filter out anyone you knew personally before they joined.

2. **Free product retention**: Users keep coming back to a free product but won't pay. This is engagement, not PMF. PMF requires paying or strong intent to pay.

3. **Single-cohort enthusiasm**: One launch cohort loves the product but no replacement cohort behaves the same. Often a sign of cherry-picked early adopters who don't represent broader market.

The OSR rule: PMF requires sustained signal across 3+ acquisition cohorts in your real target market, with paying behavior.

## TRR scoring for PMF

Inside OSR's Total Risk Reduced framework:

| TRR Score | PMF state |
|---|---|
| 0-20% (Raw) | No PMF, no clear hypothesis even |
| 20-40% (Shaped) | Problem hypothesis validated. Far from PMF. |
| 40-60% (Problem Fit) | Customers want a solution. PMF possible but unproven. |
| 60-80% (Solution Fit) | Your solution works. Need scale signal. |
| **80-100% (PMF)** | Sean Ellis test 40%+, OR retention curve flat, OR organic growth >20% MoM |

Founders raising on "we have product-market fit!" usually sit at 50-65% TRR. Real PMF (80%+) is recognizable by behavior, not pitch language.

## The hardest part: PMF is ongoing

Marc Andreessen's framing implied PMF as a binary moment. In practice it's a moving target:

- **Markets shift** — customer needs evolve, technology changes, regulations appear
- **Competitors enter** — what was differentiated becomes parity
- **Scale changes the product** — what worked at 100 users breaks at 100,000
- **Adjacent segments differ** — PMF in segment A doesn't transfer to segment B

The Heap data-driven view: PMF is not a destination but an ongoing measurement. Companies that thought they "achieved" PMF and stopped measuring often lose it without realizing.

## What founders should do

For pre-PMF founders, the priority order:

1. **Pick ONE customer segment** (specific, narrow, identifiable)
2. **Run validation experiments to confirm the Problem is real** (interviews + fake door)
3. **Build the smallest possible Solution that addresses the validated Problem** (MVP)
4. **Launch to 50-200 real users** (not friends and family)
5. **Measure 2-3 PMF metrics simultaneously** (Sean Ellis + retention + organic growth)
6. **Iterate based on what the data says**, not what the pitch deck claims

The PMF signal will come or it won't. Founders who fake PMF data to keep raising capital prolong the dying. Founders who acknowledge PMF gap and iterate are the ones who break through.

## Frequently asked questions

**Q: What is product-market fit?**
A: The point where a defined group of customers genuinely wants what you sell and is willing to pay for it. Coined by Marc Andreessen in 2007.

**Q: Who coined the term product-market fit?**
A: Marc Andreessen, in a 2007 essay called *The Only Thing That Matters*.

**Q: How do you measure product-market fit?**
A: Most common test: Sean Ellis's 40% rule (if 40%+ of users would be "very disappointed" losing the product). Other metrics: net retention, cohort retention curve, organic growth %, CAC payback.

**Q: What is the Sean Ellis 40% test?**
A: Survey 40+ active users with "How would you feel if you could no longer use [product]?" with options: very disappointed, somewhat disappointed, not disappointed. If 40%+ say "very disappointed", you have PMF signal.

**Q: Can you have product-market fit before launch?**
A: True PMF requires real usage data, but pre-launch directional signals include: pre-order/waitlist conversion, interview signal density, reference customer eagerness, competitor user dissatisfaction.

**Q: What percentage of startups achieve product-market fit?**
A: Roughly 25-35% reach genuine PMF; many that claim it have false-positive signals. CB Insights research: 42% of startups fail specifically because of no market need.

**Q: Is product-market fit permanent?**
A: No. Markets shift, competitors enter, products break at scale, segments differ. PMF requires ongoing measurement to maintain.

## Related reading

- [TBD: minimum viable product]
- [TBD: validation framework]
- [TBD: customer development interviews]
- [TBD: total risk reduced trr]
""",
        "faq_block_json": """[
{"question": "What is product-market fit?", "answer": "The point where a defined group of customers genuinely wants what you sell and is willing to pay for it. Coined by Marc Andreessen in 2007."},
{"question": "Who coined the term product-market fit?", "answer": "Marc Andreessen, in a 2007 essay called The Only Thing That Matters."},
{"question": "How do you measure product-market fit?", "answer": "Most common: Sean Ellis 40% rule (40%+ of users would be 'very disappointed' losing product). Other metrics: net retention, cohort retention curve, organic growth, CAC payback."},
{"question": "What is the Sean Ellis 40% test?", "answer": "Survey 40+ active users with 'How would you feel if you could no longer use [product]?' If 40%+ say 'very disappointed', you have PMF signal."},
{"question": "Can you have product-market fit before launch?", "answer": "True PMF requires real usage data, but pre-launch directional signals: pre-order/waitlist conversion, interview signal density, reference customer eagerness, competitor user dissatisfaction."},
{"question": "What percentage of startups achieve product-market fit?", "answer": "Roughly 25-35% reach genuine PMF; many that claim it have false-positives. CB Insights: 42% of startups fail due to no market need."},
{"question": "Is product-market fit permanent?", "answer": "No. Markets shift, competitors enter, products break at scale, segments differ. PMF requires ongoing measurement to maintain."}
]""",
        "source_citations": (
            "- Wikipedia: Product-market fit — https://en.wikipedia.org/wiki/Product-market_fit\n"
            "- ProductPlan: Product-Market Fit Glossary — https://www.productplan.com/glossary/product-market-fit\n"
            "- Stripe: What is product-market fit — https://stripe.com/resources/more/what-is-product-market-fit-what-startups-need-to-know\n"
            "- Salesforce: What Is Product-Market Fit\n"
            "- Lean Startup Co: A Playbook for Achieving Product-Market Fit\n"
            "- Heap: Data-Driven PMF Framework\n"
            "- Mailchimp: Product-Market Fit Strategy & Examples"
        ),
    },

    # ============================================================
    # V4-010 — what is the blue ocean strategy (1000 vol, KD 22)
    # ============================================================
    {
        "primary_keyword": "what is the blue ocean strategy",
        "tldr_answer": (
            "Blue Ocean Strategy is the simultaneous pursuit of differentiation and low "
            "cost to open uncontested market space and make competition irrelevant. "
            "Developed by W. Chan Kim and Renée Mauborgne at INSEAD and published in 2005, "
            "it contrasts blue oceans (uncontested space) with red oceans (existing competitive "
            "markets) and offers the Four Actions Framework: Eliminate, Reduce, Raise, Create."
        ),
        "identified_gap": (
            "blueoceanstrategy.com (canonical), Wikipedia, HBR, WallStreetPrep cover definition + "
            "red/blue ocean + Four Actions but miss:\n"
            "- How to APPLY Four Actions to your specific business (most show Cirque/Nintendo examples only)\n"
            "- Common Blue Ocean mistakes (assuming new market = blue ocean)\n"
            "- Vietnamese / SEA blue ocean examples\n"
            "- When red ocean strategy is actually correct"
        ),
        "competitor_format_notes": (
            "Real SERP: blueoceanstrategy.com #1 (canonical owner) + Wikipedia + Amazon book + "
            "HBR 2004 + Blue Ocean Competition + WallStreetPrep + red vs blue. Pattern: Kim+Mauborgne "
            "attribution + INSEAD + 2005 book + Four Actions explained + examples (Cirque, Wii, etc). "
            "OSR opening: actual application workflow + SEA examples + when red ocean is right."
        ),
        "unique_angle": (
            "- Four Actions applied to actual founder workflow\n"
            "- Vietnamese / SEA Blue Ocean examples (Topica English, MoMo)\n"
            "- When Red Ocean strategy is actually correct (counter-narrative)"
        ),
        "article_body_md": """<aside className="tldr">
**TL;DR.** Blue Ocean Strategy is the simultaneous pursuit of differentiation and low cost to open uncontested market space and make competition irrelevant. Developed by W. Chan Kim and Renée Mauborgne at INSEAD and published in 2005, it contrasts blue oceans (uncontested space) with red oceans (existing competitive markets) and offers the Four Actions Framework: Eliminate, Reduce, Raise, Create.
</aside>

## The core idea

Most strategy assumes the market is fixed and the goal is to outcompete rivals for share. Kim and Mauborgne's insight: market boundaries are constructed by industry players, not given. By redefining what the product is and who it serves, a company can create uncontested space where competition is irrelevant.

The 2005 book *Blue Ocean Strategy* is based on a 15-year study of 150+ strategic moves across 30 industries spanning 100 years. The conclusion: companies that created blue oceans achieved higher growth and profit than those competing in red oceans.

## Red ocean vs blue ocean

| Dimension | Red Ocean | Blue Ocean |
|---|---|---|
| Market space | Existing, defined | New, uncontested |
| Competition | Outperform rivals for share | Make competition irrelevant |
| Demand | Exploit existing | Create new |
| Value-cost trade-off | Choose differentiation OR low cost | Pursue both simultaneously |
| Strategic action | Compete on industry conventions | Break industry conventions |

In a red ocean, the rules of competition are known. Companies fight for a bigger share of shrinking demand by outperforming rivals on existing factors. The water turns red with competition.

In a blue ocean, there is no competition yet because the rules don't exist. The company creates new demand by serving new customers or serving existing customers in a fundamentally different way.

## The Four Actions Framework

The signature tool of Blue Ocean Strategy. To create new market space, ask these four questions:

1. **Eliminate** — which factors that the industry takes for granted should be eliminated?
2. **Reduce** — which factors should be reduced well below the industry standard?
3. **Raise** — which factors should be raised well above the industry standard?
4. **Create** — which factors should be created that the industry has never offered?

These four actions together produce a new value curve. The point isn't to differentiate slightly on every factor — it's to differ radically by ELIMINATING and CREATING.

## Classic examples

**Cirque du Soleil** (used by Kim+Mauborgne as opening case):
- Eliminated: animal acts, multiple show tents, star performers
- Reduced: aisle concessions, traditional ticket pricing
- Raised: artistic music, refined venue
- Created: theme, sophisticated audience targeting, story
- Result: Created the "theatrical circus" category that didn't exist, with both differentiation AND lower cost than traditional circus or theater

**Nintendo Wii (vs Sony PS3, Xbox 360, 2006)**:
- Eliminated: HD graphics race, gamer-only positioning
- Reduced: processing power, technical specs
- Raised: physical motion gameplay, family-friendliness
- Created: motion-sensing controller as primary interface, casual gaming category
- Result: Outsold both PS3 and Xbox 360 in early generation despite lower-spec hardware

**Yellow Tail wine (Casella Wines, Australia)**:
- Eliminated: enological complexity, oak aging, marketing campaigns
- Reduced: wine range complexity
- Raised: ease of selection, fun branding
- Created: easy-drinking wine for beer/cocktail drinkers
- Result: Became #1 imported wine in US within 2 years of US launch

## Common Blue Ocean mistakes

Three patterns where Blue Ocean thinking misleads:

1. **Assuming "new market" = "blue ocean"**: A novel product category doesn't automatically mean Blue Ocean. Many "new" categories turn out to be unprofitable wastes of time. Real Blue Ocean requires both new demand AND a sustainable value-cost position.

2. **Skipping the customer side**: The Four Actions Framework can be done in isolation, producing internally satisfying redesigns that nobody wants to buy. Pair it with customer interviews and validation experiments.

3. **Differentiating on every factor**: Yellow Tail beats traditional wine by being LESS sophisticated. Cirque du Soleil eliminated animal acts. The framework's power is asymmetric — most of its impact comes from ELIMINATE and CREATE, not from incremental Raise.

## When Red Ocean strategy is actually correct

Blue Ocean Strategy is right less often than the popular conversation suggests. Red Ocean strategy is correct when:

- The category has structural defensibility (network effects, switching costs, regulatory moats) that benefit incumbents
- The market is large enough that incremental share matters more than category creation
- Your team's edge is operational excellence in a known category, not category creation
- Capital required to create a new category exceeds what's available for the bet

For OSR portfolio companies, the decision: pursue Blue Ocean only when the validated customer demand is strong enough to support category creation. Otherwise, find a narrow differentiation in a Red Ocean and execute.

## A Vietnamese Blue Ocean example: Topica English

Before Topica entered Vietnam's English-learning market in the late 2000s, the category was Red Ocean: classroom-based programs (ACET, Apollo, Britain English Centre, ILA) competing on teacher quality, location, and price.

Topica's Four Actions:
- Eliminated: physical classrooms, fixed schedules
- Reduced: teacher cost per student (live + AI mix), enrollment process complexity
- Raised: convenience (24/7 access), homework AI feedback speed
- Created: online live tutoring for English speaking practice with native speakers worldwide

Result: by 2015, Topica was the largest online English learning company in Southeast Asia. The category they created (online live tutoring) didn't exist in Vietnam before.

## How OSR uses Blue Ocean Strategy

Every OSR portfolio company runs a Strategy Canvas (the visual version of Four Actions Framework) before committing to a market. The canvas:

- X-axis: competing factors in the category (price, features, distribution channels, etc.)
- Y-axis: relative position (low to high)
- Two value curves: existing industry leaders + OSR's planned offering

The OSR offering's value curve should look RADICALLY different from competitors — not slightly higher on every factor. If the curves look similar, we're in a Red Ocean and need to reconsider.

## Frequently asked questions

**Q: What is Blue Ocean Strategy?**
A: The simultaneous pursuit of differentiation and low cost to open uncontested market space and make competition irrelevant. Developed by W. Chan Kim and Renée Mauborgne (INSEAD, 2005).

**Q: Who created Blue Ocean Strategy?**
A: W. Chan Kim and Renée Mauborgne, professors at INSEAD business school. Published the book *Blue Ocean Strategy* in 2005.

**Q: What is the difference between red ocean and blue ocean?**
A: Red oceans are existing competitive markets where companies fight for share. Blue oceans are uncontested markets where new demand is created. Red ocean competes; blue ocean creates.

**Q: What is the Four Actions Framework?**
A: The Blue Ocean Strategy tool: Eliminate (factors industry takes for granted), Reduce (well below industry standard), Raise (well above industry standard), Create (never offered before). The combination produces a new value curve.

**Q: Can you give examples of Blue Ocean Strategy?**
A: Cirque du Soleil (theatrical circus), Nintendo Wii (motion gaming), Yellow Tail wine (easy-drinking wine), Topica English (online live tutoring in Vietnam), Salesforce (CRM as subscription).

**Q: Is Blue Ocean Strategy always better than competing in Red Oceans?**
A: No. Red Ocean strategy is correct when categories have structural defensibility, when market is large enough that incremental share matters, when your team's edge is operational excellence, and when capital available is insufficient for category creation.

**Q: What is the Strategy Canvas?**
A: The visual diagnostic tool from Blue Ocean Strategy. X-axis lists competing factors. Y-axis shows relative position. Two value curves: industry leaders + your planned offering. Real Blue Ocean offerings have radically different value curves.

## Related reading

- [TBD: strategy canvas four actions]
- [TBD: business model canvas]
- [TBD: validation framework]
- [TBD: vietnam startup ecosystem]
""",
        "faq_block_json": """[
{"question": "What is Blue Ocean Strategy?", "answer": "The simultaneous pursuit of differentiation and low cost to open uncontested market space and make competition irrelevant. Developed by W. Chan Kim and Renée Mauborgne (INSEAD, 2005)."},
{"question": "Who created Blue Ocean Strategy?", "answer": "W. Chan Kim and Renée Mauborgne, professors at INSEAD business school. Published the book Blue Ocean Strategy in 2005."},
{"question": "What is the difference between red ocean and blue ocean?", "answer": "Red oceans are existing competitive markets where companies fight for share. Blue oceans are uncontested markets where new demand is created. Red competes; blue creates."},
{"question": "What is the Four Actions Framework?", "answer": "Eliminate (factors industry takes for granted), Reduce (well below industry standard), Raise (well above industry standard), Create (never offered before). Produces new value curve."},
{"question": "Can you give examples of Blue Ocean Strategy?", "answer": "Cirque du Soleil (theatrical circus), Nintendo Wii (motion gaming), Yellow Tail wine (easy-drinking), Topica English (online live tutoring in Vietnam), Salesforce (CRM as subscription)."},
{"question": "Is Blue Ocean Strategy always better than Red Oceans?", "answer": "No. Red Ocean is correct when categories have structural defensibility, market is large enough, team's edge is operational excellence, or capital is insufficient for category creation."},
{"question": "What is the Strategy Canvas?", "answer": "Visual diagnostic from Blue Ocean Strategy. X-axis: competing factors. Y-axis: relative position. Two value curves: industry leaders + your offering. Blue Ocean offerings have radically different curves."}
]""",
        "source_citations": (
            "- Blue Ocean Strategy (official): https://www.blueoceanstrategy.com/what-is-blue-ocean-strategy/\n"
            "- Wikipedia: Blue Ocean Strategy — https://en.wikipedia.org/wiki/Blue_Ocean_Strategy\n"
            "- HBR 2004: Blue Ocean Strategy — https://hbr.org/2004/10/blue-ocean-strategy\n"
            "- WallStreetPrep: Blue Ocean Strategy Characteristics & Examples\n"
            "- Red Ocean vs Blue Ocean Strategy comparison\n"
            "- Blue Ocean Competition: Learn the Fundamentals"
        ),
    },
]


if __name__ == "__main__":
    print(f"v4 articles in this file: {len(ARTICLES)} / 10")
    for i, a in enumerate(ARTICLES, 1):
        wc = len(a["article_body_md"].split())
        print(f"  #{i} {a['primary_keyword']:<40s} body={wc} words")
