# Go-to-Market Strategy: The Diagnostic Most Frameworks Skip

<aside className="tldr">
**TL;DR.** Most go-to-market frameworks give founders a 10-step checklist: define your ICP, set pricing, pick channels, build messaging. The checklist is fine. The diagnostic underneath it is missing. The question that determines whether your GTM works is which motion (product-led, sales-led, marketing-led, community-led) fits your specific product shape. Picking the wrong motion can be undone, but not without 12 to 18 months of cost. This piece walks through the three-question diagnostic that determines your motion, the failure modes of each motion-shape mismatch, and a worked example.
</aside>

## What "go-to-market strategy" actually means

Go-to-market strategy is a generic term that has been stretched to cover everything from a tactical launch plan to a complete cross-functional system. Both uses are common, and the confusion they create is one of the reasons founders struggle with GTM.

The narrow definition: GTM is the launch plan for a specific product or feature. Marketing, sales, customer success, and product align on how the launch is delivered. Useful for a specific moment.

The broader definition: GTM is the system by which a company reaches customers, generates demand, converts to revenue, and retains accounts. Channels, sales motion, pricing, messaging, ICP, and metrics are all components. Useful as a strategic frame.

This piece uses the broader definition because it is the one founders actually need before launch. The narrow definition is what you build inside the broader frame.

The most common GTM frameworks online are step-lists: 5 steps, 7 steps, 10 steps, 13 steps. They cover ICP definition, positioning, pricing, channels, sales process, metrics. The lists are reasonable. The problem is they treat GTM as a checklist where every founder runs the same steps in the same order. The reality is that the right GTM differs structurally based on what you are selling and to whom.

## The trap: applying the wrong motion to your product shape

The most common GTM failure mode is shape-motion mismatch. A founder picks a motion based on what is fashionable in the market or what they have seen work for a famous company. The motion is reasonable for that famous company. It is wrong for the founder's product shape. The mismatch produces:

- Burning 12 to 18 months of capital
- Hiring the wrong roles (sales reps for a self-serve product, growth marketers for an enterprise product)
- Building the wrong infrastructure (sales CRM for a product-led business, in-product analytics for an outbound sales business)
- Producing weak unit economics that get blamed on the product rather than the motion

The mismatch is structural. It is not solved by working harder on the same wrong approach. It is solved by switching motions, which costs months.

Four motion shapes matter. Each has a fit pattern. Mismatches produce predictable failures.

**Product-led growth (PLG).** The product itself acquires, converts, and expands customers. Free trial or freemium. Self-serve signup. Usage triggers conversion to paid. Examples: Slack, Notion, Linear, Figma. Fits when the product can deliver clear value within 5 to 15 minutes of first use and the buyer is the user.

**Sales-led growth (SLG).** A sales team identifies, qualifies, and closes accounts. Outbound prospecting, demos, multi-stakeholder consensus building, contracts. Examples: Salesforce, Oracle, Snowflake. Fits when the buyer is not the user (enterprise IT buying for engineering teams), the contract size is meaningful ($25k+ ACV typical lower bound), and the buying process involves multiple stakeholders.

**Marketing-led growth (MLG).** Content, SEO, and paid acquisition drive top-of-funnel; product-qualified leads convert through a sales-assisted process. Examples: HubSpot, Mailchimp, Calendly (early stages). Fits when the buyer searches for category solutions, the contract size justifies marketing investment ($5k+ ACV typical), and there is depth of content the founder can produce.

**Community-led growth (CLG).** Community engagement, developer relations, or user-generated content drives acquisition. Examples: GitHub, Stripe, Postman (early), Notion (in some segments). Fits when the product targets a community with strong internal trust signals and the founder has authentic distribution into that community.

The motions are not exclusive. Most mature companies use multiple. But early-stage companies should commit to one primary motion. Splitting attention across two or more before product-market fit usually produces neither working well.

## The diagnostic: three questions that determine your motion

The diagnostic before picking the motion is three questions. Founders who skip this step pick the motion that feels familiar and pay for the mismatch later.

### Question 1: Price point and contract size

What does your annual contract value (ACV) look like at the small, median, and large end?

- ACV $0 to $500: PLG or freemium with high-volume conversion. SLG is uneconomical.
- ACV $500 to $5,000: PLG with sales-assist, or MLG with self-serve conversion. SLG is uneconomical.
- ACV $5,000 to $25,000: MLG with sales-assist, or hybrid SLG with marketing fuel. Pure PLG is uncommon.
- ACV $25,000 to $250,000: SLG with marketing support. Pure PLG is uncommon.
- ACV $250,000+: SLG with executive-led selling. PLG is irrelevant.

Price point is the single strongest determinant of motion. A $50/month tool cannot afford outbound sales; a $250,000/year enterprise platform cannot rely on self-serve trial.

### Question 2: Buyer and user identity

Is the person who signs the contract the same person who uses the product?

- Same person (user = buyer): PLG, CLG, or MLG with self-serve. The motion respects that the user decides.
- Different people (user ≠ buyer): SLG or MLG with sales-assist. The motion accommodates that the user influences but the buyer decides.
- Different organizations (user company ≠ buyer company): SLG. Multi-org dynamics require human selling.

Most enterprise software sits in the second category (engineering teams use the tool; IT or finance approves the purchase). Most consumer and SMB tools sit in the first. Misreading this drives the most common motion mismatches.

### Question 3: Distribution-fit and time to value

Can a user experience clear product value within minutes of first interaction?

- Under 15 minutes: PLG-ready. The product can convert through usage.
- 15 minutes to 2 hours: PLG-possible with strong onboarding, or sales-assisted PLG.
- 2 hours to 2 days: Sales-assisted required. Pure PLG produces weak conversion.
- 2+ days: SLG with extensive onboarding. PLG is irrelevant.

Time to value is about whether the user can experience the "aha" within a session. A note-taking app can. A complex revenue-attribution platform cannot. The difference determines whether self-serve works.

Combining the three answers usually points unambiguously to one motion. Mismatch happens when founders ignore the diagnostic and pick the motion they want regardless.

## The four failure modes from motion mismatch

When the motion does not fit the product shape, the failure modes are consistent.

**Enterprise startup running PLG.** The product has $50k+ ACV potential. The user is an engineer; the buyer is IT or finance. Time to value is two days of integration. The founder ships a free trial, optimizes the signup funnel, hires growth marketers. Eighteen months in: thousands of free trials, very few paid conversions, weak revenue. The fix is rebuilding the SLG motion from scratch. The cost is the wasted year of investment.

**SMB startup running SLG.** The product has $500 ACV. The user is the buyer. Time to value is 10 minutes. The founder hires sales reps, builds outbound prospecting, optimizes for demo bookings. Eighteen months in: CAC is too high to justify the ACV, sales reps are burning out on small deals, conversion economics never improve. The fix is rebuilding as PLG with marketing support. The cost is sales team severance plus the lost year.

**Consumer startup running MLG.** The product is a consumer app with monthly subscription. The founder invests heavily in content marketing and SEO. Eighteen months in: content drives traffic, but consumer products with low ACV cannot afford the content production cost, and SEO traffic does not convert at consumer levels because intent is too broad. The fix is rebuilding as paid acquisition or community-led. The cost is the content investment.

**B2B startup running CLG without genuine community.** The founder loves the idea of community-led growth based on Stripe and Notion stories. The product does not target a community with strong internal trust. The founder builds a Discord, runs events, hires a community manager. Eighteen months in: the community has a few hundred people, none of whom buy at scale, and the founder has no other GTM motion. The fix is shifting to SLG or MLG with the community as a supporting channel. The cost is the time spent building community theatre.

The pattern in all four: the motion was the founder's preference, not the product shape's requirement. The cost of fixing motion mismatch is always months. The cost of avoiding motion mismatch is hours of honest diagnosis.

## A worked example: GTM diagnosis for a vertical SaaS

A founder we observed was building a vertical SaaS product for independent insurance brokers. Target ACV $4,800/year. The user (the broker) signs the contract. The product takes about 2 hours of setup to integrate with the broker's existing CRM and policy management.

The founder's initial plan: PLG with free trial. The intuition came from having seen Notion and Linear succeed with PLG. The motion the founder chose was familiar.

Running the diagnostic:

Question 1 — Price point. ACV $4,800 sits in the "MLG with self-serve or sales-assist" zone. PLG is possible but requires very high conversion volume to make sense. SLG is too expensive for $4,800 ACV. The diagnosis: MLG or PLG with sales-assist.

Question 2 — Buyer identity. The broker is both user and buyer. Self-serve is structurally available. The diagnosis: self-serve compatible.

Question 3 — Time to value. The 2-hour integration is the constraint. Pure PLG would lose users during integration. The diagnosis: sales-assisted PLG, or MLG with content driving qualified trials.

The recommended motion: MLG with content marketing into the broker community, sales-assist for trial-to-paid conversion. Hiring profile: a content marketer plus a sales engineer to help with the integration step. Not the free-trial-and-growth-team setup the founder had imagined.

The founder pivoted to the recommended motion. Six months later, CAC was $1,200, payback was 4 months, conversion from trial to paid was 35 percent (above the SaaS benchmark because the sales engineer addressed the integration friction). The motion fit the shape. The founder's first instinct would have produced a free-trial product that no one converted on because the integration friction was too high for pure PLG.

The cost of the diagnostic was thirty minutes of structured conversation. The cost of skipping it would have been twelve months of building the wrong motion.

## What OS Research thinks

Most go-to-market content is checklist-style. The checklist is not wrong. It is incomplete. The most consequential GTM decision a founder makes is not which steps to follow but which motion to commit to. The motion decision precedes all the other steps and shapes them.

Our view is that GTM strategy should start with the shape-motion diagnostic, not with the ICP definition or channel selection. ICP, channels, pricing, and messaging are all downstream of the motion. Running them first produces internally consistent answers within a motion that may itself be wrong.

The OSR [validate business idea](https://www.osresearch.vn/blog/validate-business-idea) framework treats GTM as part of the validation work. Before building the product, validate the GTM motion: can you reach customers, can you convert them, can the economics work in the motion you have picked. Validating motion before scaling is structurally different from optimizing channels within an assumed motion. The first prevents motion mismatch; the second assumes motion fit.

For founders with strong validation discipline, the diagnostic is the natural next step. For founders without it, the motion mismatch failure mode is the most expensive 12 to 18 months they will spend.

## Common mistakes

**Picking the motion based on what you have seen work.** Slack's PLG worked because Slack's product shape fits PLG. Salesforce's SLG worked because Salesforce's shape fits SLG. Copying the famous company's motion without matching the shape produces predictable failure.

**Splitting the motion early.** Trying to run PLG and SLG simultaneously before product-market fit usually produces both working poorly. Pick one motion as primary; treat others as supporting. Splitting attention before fit dilutes both.

**Ignoring the time-to-value question.** Founders default to PLG because it is fashionable. Products that take two days to integrate cannot run pure PLG regardless of how much the founder wants to. The time-to-value question is structural and not negotiable.

**Hiring the wrong roles for the motion.** Sales reps for a PLG product produce churn. Growth marketers for an SLG product produce signups that do not close. Hiring follows from motion, not the reverse. Hiring before motion is decided usually produces expensive mismatches.

**Treating ICP as the starting point.** ICP is a downstream decision that depends on the motion. Different motions can target different ICPs within the same product. The jobs to be done framework helps clarify which customer problems your motion is actually solving for; running ICP discovery before motion diagnosis often produces an ICP optimized for the wrong motion.

**Skipping the diagnostic because it feels obvious.** Founders who have built before often feel they already know their motion. Sometimes they are right. Often they are right about the previous product and wrong about the current one. Running the diagnostic takes 30 minutes and prevents an expensive mistake.

## Frequently asked questions

**Q: What is a go-to-market strategy?**
A: A go-to-market strategy is the system by which a company reaches customers, generates demand, converts to revenue, and retains accounts. The strategic version includes motion, ICP, positioning, pricing, channels, sales process, and metrics. The narrower tactical version is a launch plan for a specific product or feature.

**Q: What are the steps in a go-to-market strategy?**
A: Most GTM frameworks list 7 to 13 steps covering ICP definition, positioning, pricing, channels, sales process, and metrics. The steps are similar across frameworks. What differs is the underlying motion (PLG, SLG, MLG, CLG), and the motion determines how each step is executed. The first decision is motion; the steps follow.

**Q: What is the difference between GTM and marketing strategy?**
A: Marketing strategy is one component of GTM. Marketing covers demand generation, brand, content, and product marketing. GTM is broader and includes sales motion, customer success, pricing, ICP definition, and channel mix. Marketing strategy fits inside GTM; GTM is the cross-functional system.

**Q: What are the four go-to-market motions?**
A: Product-led growth (PLG), sales-led growth (SLG), marketing-led growth (MLG), and community-led growth (CLG). The motions differ in who acquires, converts, and retains customers. Most mature companies use a primary motion supplemented by others; early-stage companies should commit to one primary motion before product-market fit.

**Q: How long does it take to develop a GTM strategy?**
A: The motion diagnosis takes 30 to 60 minutes of structured conversation. The full GTM strategy (ICP, positioning, channels, pricing, metrics, sales process) typically takes two to four weeks for a focused early-stage team. The diagnostic should come first; the detailed planning follows once the motion is decided.

**Q: How do I know which GTM motion fits my product?**
A: Run the three-question diagnostic. Price point and contract size, buyer-user identity, and time to value. Combining the answers usually points unambiguously to one motion. The diagnostic is in the body of this piece.

**Q: Can I change my GTM motion later?**
A: Yes, but the cost is typically 12 to 18 months and substantial team and infrastructure changes. The most common motion changes (from PLG to SLG as enterprise customers appear, or from SLG to PLG as product matures) require hiring different roles, building different infrastructure, and shifting CAC budgets. Easier to get the motion right initially than to pivot later.

**Q: What GTM motion works best for SaaS?**
A: There is no single answer. SaaS companies span all four motions depending on price point, buyer, and time to value. Notion is PLG; Salesforce is SLG; HubSpot is MLG; Postman is CLG (in part). The right SaaS motion depends on the specific product shape, not on the SaaS label.

**Q: How does GTM strategy relate to product-market fit?**
A: GTM strategy assumes product-market fit. Before product-market fit, founders should treat GTM as part of the validation work: testing whether the motion can reach customers and convert them economically. After product-market fit, the motion is scaled and optimized. Trying to scale a motion before product-market fit usually amplifies whatever does not work. See our [product market fit](https://www.osresearch.vn/blog/product-market-fit) piece for the relationship.

**Q: How is GTM strategy different for B2B vs B2C?**
A: B2B GTM is usually SLG or MLG-with-sales-assist because contract sizes justify human selling and buyers are often not users. B2C GTM is usually PLG, CLG, or paid acquisition because contract sizes do not justify SLG and buyers are users. The exception in B2B is the SMB and prosumer segment, where contract sizes are smaller and B2C-style motions can apply. The exception in B2C is high-end consumer (luxury, certain consumer health), where SLG-style consultative selling can apply.

**Q: What metrics should I track for my GTM strategy?**
A: Different motions have different metrics. PLG: signup-to-activated, activated-to-paid, expansion revenue, payback period. SLG: pipeline, conversion by stage, CAC, sales cycle length. MLG: content traffic, lead-to-MQL conversion, MQL-to-SQL conversion. CLG: community engagement, community-to-customer conversion. Tracking metrics for the wrong motion produces noise that misleads the team. Pick the metrics that match your motion.
