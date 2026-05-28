# North Star Metric: A Validation Artifact, Not a Tracking One

<aside className="tldr">
**TL;DR.** A north star metric is the single leading indicator that captures customer value and predicts future revenue. Most articles teach you to pick one as a tracking dashboard. We treat it as a validation artifact: the metric you would design an experiment around if you wanted to falsify the company's core thesis. This piece walks through the four-question test, a worked example for an early-stage company, and the failure patterns most teams repeat.
</aside>

## What a north star metric actually is

A north star metric, often shortened to NSM, is the single measure that best captures the value your product delivers to customers and most directly predicts long-term, sustainable growth. The term was popularized by Sean Ellis and Amplitude. Almost every product-led company published since 2018 references it.

The canonical definition has three parts. The metric must reflect customer value. It must be a leading indicator, not a lagging one. It must be company-wide, where every team can draw a line from their daily work to it.

Slack's "weekly messages sent within paid workspaces" is the textbook example. Airbnb's "nights booked." Spotify's "time spent listening." HubSpot's "weekly active teams." These metrics share a structure: a count of a specific value-delivering action by a defined unit, over a defined time window.

The standard sources, Amplitude, Reforge, Userpilot, Mixpanel, CXL, all spend most of their content on this definition and on listing examples. Where they fall short is the part founders actually need: how do you tell whether the NSM you picked is going to work?

## The trap: dashboards that look right and predict nothing

Most teams end up with a north star metric that satisfies the textbook checklist and still does not move with the underlying business. The pattern is reliable.

A founder reads an Amplitude article. They pick a metric that sounds like value delivery: "monthly active users" or "weekly engaged accounts." They build a dashboard. The number goes up for two quarters. They take a Series A on the strength of the curve. The renewal cohort eighteen months later does not behave the way the metric predicted. The company struggles to find product-market fit at a higher price point. Investors ask what happened.

The honest answer is that the metric was a vanity metric in disguise. It looked like a leading indicator because it moved before revenue. It was not actually predictive of revenue. The correlation was a coincidence of growth, not a causal relationship the team could rely on.

Three failure modes drive this:

The metric measures input volume rather than value-delivery. "Number of accounts created" is not "number of accounts that experienced the value moment." The first is easy. The second is the one that predicts retention.

The metric is a lagging indicator wearing a leading-indicator costume. Monthly revenue is the obvious lagging indicator. Less obvious: "monthly active users on plan tier 2 or above." That metric only moves after the user has upgraded, which is downstream of every input you actually want to track.

The metric works for the current stage of the business but breaks at the next one. A weekly engagement metric that predicts trial-to-paid conversion does not predict expansion revenue. A team that uses one NSM across stages will eventually find the metric pointing the wrong direction and not know why.

None of these are exotic mistakes. They are the modal outcome when teams pick a north star from a checklist rather than designing one as a falsifiable claim about how the business works.

## The four-question test we use

At OS Research, we evaluate candidate north star metrics against four questions before adopting one. The questions are simple. They are also strict.

**Question 1: What value moment does this metric count?**

The metric must name a specific action that delivers value to the user. "Users who completed the first project setup." "Customers who closed a deal using the platform." "Patients who finished a guided check-in." If the metric counts an action that does not directly correspond to a moment of realized value, it is a proxy. Proxies sometimes work. They fail more often than they work.

A test: if you described the metric to a customer, would they recognize it as the thing they came to your product for? If not, the metric is internal language for an internal goal, not customer language for customer value.

**Question 2: What user behavior would you have to disprove for this metric to be wrong?**

This question is the falsification step. A real NSM makes a claim about the business: that users who do X also do Y, where Y is durable revenue. Naming the underlying behavior makes the claim testable. If the metric is "weekly active teams," the underlying claim is that teams that stay active weekly retain longer and pay more. That claim can be tested with cohort retention data and ARR-per-cohort analysis.

If you cannot name a behavior whose absence would make you abandon the metric, you do not have an NSM. You have a chart.

**Question 3: At what stage of the company does this metric apply?**

A pre-product-market-fit NSM and a post-product-market-fit NSM are not the same metric. Before PMF, the NSM is a validation hypothesis: "if users do X often enough, the business will work." After PMF, the NSM is an operating compass: "as long as X grows, the business is healthy." Teams that pick a post-PMF NSM at the pre-PMF stage end up tracking a number they cannot move directly. Teams that hold onto their pre-PMF NSM after PMF end up missing expansion signals.

We make stage explicit. The NSM document names which stage it applies to and which alternative metric supersedes it at the next stage.

**Question 4: Can a small team move this metric in a quarter through deliberate work?**

If the answer is no, the metric is too far downstream. North star metrics that only move with quarter-over-quarter compounding of many small actions are useful for boards. They are not useful for product teams who need to feel the result of a sprint.

The classic example is annual recurring revenue. ARR is a real, important number. It is not a north star metric. It is the lagging outcome that the right NSM should predict. A team that tries to "move ARR" inside a six-week cycle will end up either focused on the wrong things or focused on artificial expansion that hurts retention.

A passing NSM clears all four questions before adoption. A failing NSM gets rebuilt or replaced.

## A worked example: picking an NSM for an early-stage vertical SaaS

Take a concrete case. A founder is building scheduling software for independent dental practices in Vietnam. They have eight pre-paid letters of intent from Stage 2 validation. They are about to build the first usable product version. They want an NSM before they ship.

A naive pass at this picks "weekly active accounts." It sounds right. It is wrong for this stage. Dental practices use scheduling software during business hours, daily. The metric will trivially show high numbers from any practice that adopts at all. It tells the team nothing about whether the product is creating durable value.

A second pass picks "monthly recurring revenue." That is the lagging outcome, not the leading indicator. Dental practices renew annually. MRR moves twelve months after the input behaviors change. The team cannot move it within a quarter.

The fit answer for this stage is a metric like "practices with at least 80% of weekly visits scheduled through the platform." Let's run it through the four questions.

Question 1: the value moment is "a visit is scheduled through our software instead of paper or a generic calendar." That is exactly what the practice came to the product for. Pass.

Question 2: the underlying claim is that practices with high scheduling penetration are practices that have integrated the software into their core workflow and will renew. The falsification: if a practice with 80%+ scheduling penetration churns at the same rate as a practice with 30% penetration, the metric is wrong and we need a different signal. That claim can be tested with cohort data once the product is live. Pass.

Question 3: this is a pre-PMF NSM. It applies until the team has clear retention curves and is ready to layer on expansion metrics. The successor metric is likely "average revenue per practice per year" once retention is established. Pass.

Question 4: an eight-person team can move this metric in a quarter. The levers are onboarding flow, default settings, in-product nudges, customer success calls in week one. All are within team control. Pass.

The metric is adopted. The team also writes down what would make them retire it: if practices at 80%+ penetration retain at the same rate as practices at 30%, the metric is replaced within the next quarter.

What this example shows is that the metric the textbook would have suggested, "weekly active accounts," fails three of the four questions for this company at this stage. The framework forces the team to find a sharper claim about value before adopting the dashboard.

## How to apply this week

If you are about to pick a north star metric or you already have one and are unsure whether it works, three concrete moves shift the work.

**Run your current NSM through the four questions in writing.**

Take the metric you currently track or are about to adopt. Write the answer to each of the four questions in two sentences each. If any answer is "not sure" or "kind of," the metric is not yet binding.

**Name the falsification condition explicitly.**

Write down the specific result that would make you abandon the metric. Make it a number, not a feeling. Share it with whoever else is responsible for it. The act of stating the kill condition turns a dashboard into an experiment.

**Distinguish stage explicitly.**

State which stage of the company the metric serves and what metric supersedes it at the next stage. Teams that skip this step end up either retrofitting the metric to a new reality or quietly switching metrics without acknowledging why.

## What OS Research thinks

We do not think north star metrics are tracking tools. We think they are validation artifacts. The right NSM is the single experiment you would run if you wanted to falsify your company's reason to exist.

The reason the canonical articles end up shallow is that they assume the metric is for tracking, so the only quality test is whether it correlates with revenue. We hold a sharper test: the metric must name a falsifiable claim about how the business works, the team must be able to move it in a quarter, and the company must agree in advance on what result would retire the metric.

Most teams reading this will discover their current NSM was picked from a list rather than designed as a claim. That is the moment to rebuild. The work pays back fast. A six week testing cycle pointed at a metric you actually believe in produces more learning than three quarters of dashboard maintenance. Our own experiment library treats every candidate NSM as a hypothesis to be cleared before it is allowed to drive sprint planning.

## Common mistakes

**Picking the metric from a list.**

The Slack example fits Slack. The Airbnb example fits Airbnb. Adopting a metric because a famous company used it skips the entire question of whether the claim applies to your business. The metric is the surface. The claim underneath is the thing that matters.

**Confusing a lagging metric with a leading one.**

Monthly revenue, ARR, customer count, gross margin: all important, none are north star metrics. They are downstream of the behaviors a real NSM tracks. Teams that pick a lagging metric as their NSM end up unable to influence the number within a planning cycle.

**Letting the metric stay constant as the company stages change.**

A pre-PMF NSM and a post-PMF NSM should be different. Teams that fail to upgrade the metric when the business stage changes end up tracking yesterday's problem.

**Mistaking high engagement for retained engagement.**

A metric that counts active users in a week is not the same as a metric that counts active users who will still be active in week ten. The retention curve underneath the surface number is what predicts revenue. The surface number alone is a vanity metric in slow motion.

**Multiple competing north star metrics.**

If three different teams each have their own "north star," the company does not have a north star. It has three priorities, which is the same as having none. The point of the metric is to force alignment. Defeat alignment and the metric loses its function.

**Skipping the falsification step.**

A metric without a stated kill condition cannot fail. A metric that cannot fail is not testable. A metric that is not testable is not an NSM. It is a chart with a marketing name.

## Frequently asked questions

**Q: What is a north star metric?**
A: A single leading indicator that captures the value your product delivers to customers and predicts long-term revenue. The metric is meant to align the company on one shared measure of progress that every team can connect their work to.

**Q: How do you choose a north star metric?**
A: Identify what value your product delivers, name the specific action that represents that value, and write down the claim the metric is making about the business. Then run the candidate metric through four questions: what value moment does it count, what behavior would have to be wrong for the metric to be wrong, which stage of the company does it apply to, and can a small team move it in a quarter.

**Q: What is the difference between a north star metric and a key performance indicator?**
A: A north star metric is the single most important leading indicator for the company. KPIs are the broader set of measurements that support the NSM and the rest of the business. The NSM is the apex of the metric tree. KPIs are the branches.

**Q: Can a company have more than one north star metric?**
A: No. The point of the metric is to force alignment across teams. Having multiple "north stars" defeats the alignment function. Most companies that claim to have several are actually using regular KPIs and calling them north stars to satisfy a meeting.

**Q: What are some examples of north star metrics?**
A: Slack tracks weekly messages sent within paid workspaces. Airbnb tracks nights booked. Spotify tracks time spent listening. Netflix tracks subscriber count. HubSpot tracks weekly active teams. The right metric for your company depends on what value your product delivers and what stage you are at.

**Q: When should I change my north star metric?**
A: When the underlying claim the metric was making turns out to be wrong, or when the company moves to a new stage where the metric no longer connects to the most important growth lever. Stage changes are the more common trigger. Write the successor metric down before retiring the current one so the team does not lose continuity.

**Q: Is revenue a good north star metric?**
A: No. Revenue is the lagging outcome the NSM is meant to predict. Tracking revenue as the NSM teaches the team nothing about what actions move the business, because revenue moves weeks or months after the input behaviors change.

**Q: How does a north star metric relate to product-market fit?**
A: A pre-product-market-fit north star is a validation hypothesis about whether users will do the value-delivering action often enough. A post-product-market-fit north star is an operating compass for how the business stays healthy as it scales. The two are different metrics for different stages. See our companion piece on [product-market fit](https://www.osresearch.vn/blog/product-market-fit) for the framing.
