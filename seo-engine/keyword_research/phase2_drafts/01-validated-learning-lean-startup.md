# Validated Learning: Why Most Experiments Don't Count

<aside className="tldr">
**TL;DR.** Validated learning is the discipline of running experiments that actually change a decision. Most startup teams collect data and call it validation. The difference is whether the result would have made you stop. Eric Ries introduced the term in The Lean Startup to separate noise from signal in the Build-Measure-Learn loop. We use four tests to qualify any experiment as valid: a stated hypothesis, a falsifiable outcome, a decision-changing result, and cheap reproducibility.
</aside>

## What validated learning actually means

Validated learning is a term from Eric Ries's The Lean Startup. It sits inside the Build-Measure-Learn loop and answers a single question: did the experiment teach you something that earns the next decision?

The original definition is narrow on purpose. Validated learning is not "what we learned from talking to users." It is not "the data we collected." It is the smallest unit of evidence that justifies whether you keep going, pivot, or stop.

Ries built the concept to push back against vanity. Teams burn capital running experiments that confirm what they already believe. They interpret friendly user interviews as demand signals. They watch top-line metrics climb while retention quietly collapses. None of that is learning. It is activity dressed up as progress.

The discipline of validated learning is the discipline of asking, before you start, what result would change your mind, and then designing the experiment so that the result actually can.

Most articles about validated learning stop at the definition. The canon, Eric Ries's original blog post, the Lean Startup principles page, the Wikipedia entry, the Boldare and Shortform write-ups, all repeat the same framing: hypothesis, MVP, Build-Measure-Learn, pivot or persevere. None of them define what counts. None of them name a threshold that, once stated, would make a team admit the idea is dead. That gap is the entire reason this piece exists.

## The trap: confusing activity with learning

Most teams that say they practice lean startup do not. They run experiments. They do not run experiments that count.

A common failure pattern looks like this:

1. The team decides to test a feature, a price, or a positioning angle.
2. They build something. A landing page, a prototype, a survey.
3. They get a result. Some clicks, some sign-ups, some interview quotes.
4. They write up what they learned and move on.

What is missing is the bar. There is no number, no threshold, no decision rule stated in advance. The team agrees the experiment "went well" or "showed signal" after they see the result. This is post-hoc reasoning. The experiment cannot fail because no one defined what failing would look like.

A second pattern is the confirmation interview. The team has an idea. They schedule fifteen calls with friendly users and ask leading questions. The users are polite and intrigued. The team concludes the idea has demand. They build it. It does not work in market.

A third pattern is vanity-metric chasing. Sign-ups go up. Visit counts go up. The team celebrates. Three months later, day-30 retention is two percent and revenue is flat. The metric that moved was never the metric that mattered.

In each case, the team did something that looked like an experiment. None of it was validated learning.

## The four tests we use to qualify an experiment

At OS Research, an experiment qualifies as validated learning only when it passes four tests. We apply this in the experiment design review, before any building begins.

**Test 1: The hypothesis is written down before the test starts.**

If the hypothesis only exists in someone's head, it will silently shift to match the result. The hypothesis goes in the experiment doc. It names a specific belief about the world, not a feature to build.

A weak hypothesis: "Users want a faster onboarding flow."

A strong hypothesis: "Among non-technical founders in Vietnam who tried our tool last month, at least 30% will pay $19 a month for a guided setup option, measured by a paid pre-sale page over five days of traffic."

The second one can be wrong. The first one cannot.

**Test 2: The outcome is falsifiable.**

You can lose. A falsifiable outcome is a specific result that, if observed, makes you stop or change direction. If every possible outcome of your experiment supports continuing, you are not running an experiment. You are running theater.

"We will get useful feedback" is not falsifiable. "We will hit at least 30% pre-sale conversion or we kill this direction" is.

**Test 3: The result changes a decision.**

A passing experiment moves you to the next stage of investment. A failing experiment stops the project or sends it back to be reshaped. If the team would have done the same next step regardless of the outcome, the experiment was not worth running.

This sounds obvious. It is not what most teams do. Most teams run experiments to feel like they did due diligence, then proceed with the original plan.

**Test 4: The result is reproducible cheaply.**

A one-off result that depended on a launch event, a paid traffic spike, or a personal-network introduction is not yet validated learning. It is an interesting signal. To call it validation, you should be able to imagine running it again, with a different cohort or a different week, and getting a similar outcome.

We treat single-instance results as hypotheses, not conclusions.

## A worked example: a B2B pricing test

Take a concrete case. A small SaaS team thinks the right price for their workflow tool is $49 a month, but they are not sure. They want to run a validated learning experiment.

A loose version of this experiment looks like this. The team launches a pricing page with three tiers. They drive paid traffic for a week. At the end of the week, the founder looks at the numbers, sees twelve trial sign-ups, and concludes the pricing "works." The team builds the full billing system on top of this finding.

A validated learning version looks different. Before launching anything, the team writes the hypothesis: "Among small-business operations leads in the United States, at least 8 percent of pricing-page visitors will start a paid trial when the entry tier is shown at $49 a month, measured over five business days of consistent paid traffic." That is Test 1 done.

The team commits, in writing, to the kill criterion: "If conversion lands under 4 percent, we abandon the $49 anchor and rebuild around a usage-based model." That is Tests 2 and 3 done. The bar is falsifiable, and the outcome would change the next decision.

They run the test. They get 5.3 percent conversion. Twelve trial signups. The headline number is the same as the loose version. But this team's reading is different: the result is between the threshold for "pursue" and "abandon." That is not validated learning. They redesign the experiment with sharper segments and run it again the following week, this time getting 9.1 percent in one cohort and 2.4 percent in another. The result is now reproducible at the segment level. That is Test 4 done. Now they have validated learning, and the actionable decision is to ship to one segment, not both.

The point is not the specific numbers. The point is that the same week of traffic produced two completely different bodies of evidence depending on the discipline applied before the test ran.

## How this changes what you build

When validated learning is the standard, the work itself changes shape.

You build less. The fastest experiment that can answer the question wins. A landing page beats a prototype. A pre-sale beats a free signup. A signed letter of intent from one real buyer beats a hundred enthusiastic survey responses. Inside our own startup experiment library, the cheapest experiment that hits the bar always wins over the more elaborate one.

You spend less. Cheap experiments mean more shots per quarter. A studio that can validate or kill a direction in two weeks for under a thousand dollars beats one that takes three months and twenty thousand to reach the same conclusion.

You kill more. Discipline at the experiment level means many ideas die quickly. This feels uncomfortable. It is also why mature studios produce a higher hit rate at the company-building stage. The ideas that survive an honest validation gate are the ones that pay for the ones that did not.

You write more. The hypothesis doc, the result doc, the decision memo. None of these are bureaucracy. They are how a team avoids relitigating the same questions a quarter later.

## Three moves you can make this week

If you want to start practicing validated learning in your own work, start here.

**Write the hypothesis before the experiment.**

Take whatever you are currently testing. Write the belief it is testing in one sentence. Add the specific result that would make you stop. If you cannot complete that sentence, you are not yet running a real experiment.

**State the kill criterion publicly.**

Tell your team or your investors what failure looks like before you run the test. Public commitment is a forcing function. It makes the post-hoc story harder to construct.

**Audit your last three experiments.**

For each one, ask: was the hypothesis written before? Was the outcome falsifiable? Did the result change a decision? Could we run it again cheaply? Count how many pass all four. If the number is zero, you are not running validated learning yet. You are running activity.

## What OS Research thinks

We are not neutral on this. Validated learning is the only standard of evidence we use to decide whether an idea moves forward. The four tests above are not a recommendation. They are the gate.

Our experience is that almost every team can list the experiments they have run. Very few can name the hypothesis each one was testing. Even fewer can point to a kill criterion that was stated in advance. The discipline of writing the bar before you start is what separates a startup validation studio that compounds knowledge from one that just stays busy.

We also think the term "lean startup" has been weakened by overuse. Hanging a "lean" label on top of normal product work does not make it lean. The work is lean when an honest skeptic could look at what you ran, agree the bar was set fairly, and accept the result as binding. That is the work.

If you have been reading the canon, Eric Ries's original posts, the Lean Startup principles page, the standard summaries, and feel like something is still missing, the missing thing is usually the bar. The canon teaches you to run the loop. It does not teach you what evidence is binding once the loop produces a result. That is the layer we keep returning to, because that is where most teams quietly give up on rigor.

## Common mistakes

**Designing the experiment around the answer you want.**

You already believe the idea will work. You quietly choose a sample, a metric, and a threshold that makes it likely to pass. The experiment is a performance, not a test.

**Letting the bar drift after the result is in.**

You said 30% would be the threshold. You see 22%. You decide 22% is still a strong signal because of a reason invented after seeing the number. The bar moved. The discipline collapsed.

**Treating user interview enthusiasm as demand.**

People are generous in conversation. The same person who said the idea was "amazing" will not pay $19 for it when the credit card screen appears. Stated preference is not revealed preference. Validated learning is built on revealed preference.

**Confusing tooling for methodology.**

A team installs an experimentation platform. They run A/B tests on button colors. None of the tests are tied to a hypothesis about the business. The team feels scientific. The studio learns nothing about whether the company should exist.

**Skipping the documentation step.**

The result is in. The team moves on. Three months later, a new hire asks why the company pivoted, and no one can find the memo. The learning was real, briefly. Then it evaporated.

## Frequently asked questions

**Q: How is validated learning different from regular A/B testing?**
A: A/B testing is a tool. Validated learning is a standard for what counts as evidence. You can run A/B tests without doing validated learning if the tests are not tied to a falsifiable business hypothesis, and you can do validated learning without A/B testing if a signed letter of intent or a pre-sale conversion answers your question. The same logic applies when teams are searching for product-market fit: hitting the metric is only validated learning if the bar was set before the test.

**Q: Where does validated learning sit in the Build-Measure-Learn loop?**
A: It is the output of one full loop. You build the smallest artifact that can produce evidence, measure the result against the bar you set, and the learning is "validated" only if it meets the four tests. If it does not, you ran the loop but did not produce validated learning.

**Q: How long should one experiment cycle take?**
A: We aim for two weeks at the early stages and a six week testing cycle at the later stages. Faster cycles force smaller, sharper experiments. Longer cycles tend to produce scope creep and ambiguity about what was actually tested.

**Q: What if the result is ambiguous?**
A: That is a failed experiment, not a learning. An ambiguous result means the experiment design was not sharp enough. Redesign it with a tighter hypothesis and a cleaner outcome metric, then run it again. Do not interpret your way out of the ambiguity.

**Q: Can validated learning apply outside of early-stage startups?**
A: Yes. Any team allocating capital to a bet can use the same standard. The bar shifts because large companies have higher fixed costs and longer cycles, but the four tests still hold.

**Q: How is validated learning different from customer development?**
A: Customer development, as defined by Steve Blank, is the parent discipline of getting out of the building and testing assumptions with real customers. Validated learning is the evidence standard inside that work. You can do customer development poorly, by interviewing without falsifiable hypotheses, and end up with no validated learning despite weeks of effort.

**Q: Does every team need to adopt validated learning?**
A: Teams in execution mode, where the business model is proven and the question is "how do we run it better," can rely on more conventional metrics. Teams in search mode, where the business model is still being discovered, will burn capital fast without validated learning as a gate.

**Q: Which experiment types produce validated learning fastest?**
A: Pre-sale pages, signed letters of intent, and concierge tests usually beat surveys, interviews, and free signups for speed and signal quality. The principle is to push the experiment as close to a revealed commitment as possible. The faster a user has to put something on the line, the cleaner the signal.
