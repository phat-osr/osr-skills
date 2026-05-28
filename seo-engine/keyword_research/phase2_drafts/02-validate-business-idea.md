# How to Validate a Business Idea: A Staged Evidence Approach

<aside className="tldr">
**TL;DR.** Most guides walk you through five steps to validate a business idea but never tell you what evidence is binding. Customer interviews and "eyes lighting up" are not validation. They are inputs. We validate ideas at OS Research through four sequential stages, each with a specific signal threshold and kill criterion. This piece walks through the staged approach, a worked example, and the false-positive patterns that catch most founders.
</aside>

## What it means to validate a business idea

To validate a business idea is to produce evidence that the idea has a real chance of becoming a real business. Not enthusiasm. Not encouragement from your network. Evidence: customers who behave in ways that pay for what you build.

The standard framing splits validation into a sequence: define the goal, study the market, talk to potential customers, run a small test, decide. That sequence is correct. It is also dangerously incomplete. It tells you what to do without telling you what would convince a skeptic that you have done it.

Almost every popular guide on validating a business idea, from HBS Online to LivePlan to Close.com to First Round Review, follows the same structure. They list four to six steps. They name useful tools. They feature founders saying things like "their eyes should light up." Then the guide ends. The reader is left to decide for themselves whether their own experiment produced binding evidence or just a story they want to believe.

That gap is the entire reason this piece exists.

## The procedural trap

Read enough validation guides and a pattern appears. Every guide tells you to talk to customers. None of them tell you what an interview has to show before you stop talking and start building. Every guide tells you to test the idea. None of them tell you what failure looks like in advance.

The result is predictable. Founders run "validation," interpret the results favorably, and proceed. Six months later the product is in market, retention is six percent, and a postmortem reveals the original interviews were friendly conversations with people who would never have paid for anything. The validation step happened. The validation did not.

The procedural trap has three reliable failure patterns.

**The interview enthusiasm trap.** A founder interviews twenty people. Eighteen say the idea is "interesting" or "useful." The founder concludes the idea has demand. None of those eighteen have committed money, time, or a referral. Stated preference is not revealed preference. An interview that ends without a request for commitment is not a validation event. It is data collection.

**The sample-of-friends trap.** The founder's first twenty interviews come from their network. The signal is positive because the cohort is biased. The founder generalizes and ships. The product launches to a cold audience and dies. The validation was real for the friendly cohort. It was never validated for anyone else.

**The vague-threshold trap.** The founder reads "their eyes should light up" and accepts that as the bar. Six interviewees seem excited. The founder calls it validated. There is no number, no rate, no kill criterion. The threshold drifts to match whatever happened.

These are not edge cases. They are the modal outcome when the canon's procedural framing is followed without an evidence standard underneath.

## The four-stage approach we use at OS Research

At OS Research, validation is staged. Each stage has a specific signal, a specific threshold for passing, and a specific reason to stop. An idea has to clear each stage in order. The discipline is in refusing to skip.

**Stage 1: Problem evidence.**

The question for this stage: does the problem exist in the form you think it does, in a population large enough to matter, and intensely enough that someone would pay to make it go away?

Signal: structured problem interviews with at least twenty people who fit the target profile, with two outcomes recorded per call. First, can the interviewee name a current workaround they use today for this problem? Second, has the interviewee tried to fix this problem in the last ninety days? If at least 60 percent name a workaround AND at least 40 percent attempted a fix recently, the problem exists in the wild. If both numbers fall below those thresholds, the problem is theoretical. Stop.

Kill criterion: under 40 percent workaround naming. The problem is not active in this population.

**Stage 2: Solution evidence.**

The question: among people who have the problem, will any of them commit something concrete in exchange for a specific solution shape?

Signal: a pre-sale or letter-of-intent test. You describe the solution in detail. You ask for a binding commitment. A pre-paid deposit, a signed LOI, a calendar slot for a paid pilot. Numbers go on the line. If at least 8 percent of qualified problem-havers commit, the solution shape is real for this population.

Kill criterion: under 4 percent commitment rate. The solution is not what they would buy.

**Stage 3: Channel evidence.**

The question: can you reach the people who would buy at a cost that does not destroy the unit economics?

Signal: paid acquisition tests on the highest-likelihood channel, with a customer acquisition cost target set before launch. CAC under a third of expected lifetime value is the entry threshold. Anything higher means even if the product works, the business cannot scale.

Kill criterion: CAC above LTV in tested channels. Reachable demand is not affordable demand.

**Stage 4: Retention evidence.**

The question: do the people who buy keep using the product after the novelty wears off?

Signal: day-30 retention, cohort-tracked, across at least two acquisition cohorts. Target threshold is industry-dependent but the discipline is the same: write the bar before the cohort starts, and accept the result.

Kill criterion: a measurable decay curve that flattens below the bar across both cohorts.

The reason for four stages is that each tests a different assumption. Problem evidence does not tell you about solution fit. Solution fit does not tell you about channel economics. None of them tell you about retention. Most failed startups passed one of these and skipped the rest.

## A worked example: validating a vertical SaaS idea

Take a concrete case. A founder has an idea for software that helps independent dental practices schedule patients, track no-shows, and run targeted recall campaigns. The founder is not a dentist. The founder believes the existing tools are bad.

**Stage 1.** The founder books interviews with twenty-five independent dental practice owners and office managers in Vietnam. Two questions are scored. Eighteen of twenty-five name a current workaround, usually a paper system or a generic calendar tool. That is 72 percent. Eleven of twenty-five attempted to fix the workaround in the last ninety days, usually by trying a different app or paying a freelancer to build a custom solution. That is 44 percent.

Both thresholds clear. The problem is active. Stage 1 passes.

**Stage 2.** The founder builds a one-page description of a dental scheduling tool with three specific features the interviews surfaced as critical. The page includes a payment button for a pre-launch deposit of one hundred dollars, refundable if the product ships and the practice does not like it. The page is sent to the original twenty-five plus fifty additional qualified prospects sourced through a dental practice management forum.

Of seventy-five qualified prospects, eight pre-paid the deposit. That is 10.6 percent. Above the 8 percent bar. Stage 2 passes.

The founder now has eight paying pre-customers, a validated problem in a specific population, and a solution shape with revealed-preference evidence. The next stage is channel: can the founder reach more dental practices at a cost that works? That stage is not yet attempted. The founder has not yet earned the right to build the full product.

What this example shows is that the same series of interviews and tests, run with explicit thresholds, produces a different decision than the loose version. The loose version would have read 72 percent and 44 percent and ten enthusiastic founders and concluded "validated." That conclusion is correct in this case but incidental: the threshold discipline is what made it binding.

In a different case, the same founder might have found 32 percent workaround naming and 14 percent recent-fix attempts. The loose reading would have called it "encouraging signal." The threshold reading kills the project at Stage 1 and saves the founder six months.

## How to apply this week

If you are validating a business idea right now, three concrete moves shift you from procedural validation to evidence validation.

**Write your kill criteria before the next experiment.**

Take the next test you have scheduled. Before you run it, write down the specific result that would cause you to stop. Make it a number. Tell at least one other person what the number is. The act of writing the bar in advance is what makes the result binding.

**Stop counting interviews. Start counting commitments.**

Trade interview volume for commitment quality. One pre-paid deposit teaches you more than thirty enthusiastic conversations. If you cannot get anyone to commit, the conversations were not validation.

**Score each interview on two falsifiable questions, not on vibe.**

Replace "did they seem excited" with two specific questions whose answers you record numerically. Workaround naming. Recent fix attempt. Specific budget number. Whatever fits your stage. You should be able to look at the spreadsheet a month from now and see numbers, not adjectives.

## What OS Research thinks

We do not believe validation is a one-shot activity. We believe it is a sequence of stages, each with a specific evidence bar, and most failed ideas died because someone skipped a stage and called the skip a shortcut.

The canon is not wrong about the steps. It is wrong about what counts as having taken them. The discipline is not in interviewing more customers, building cleverer prototypes, or running more A/B tests. The discipline is in writing the bar in advance and accepting the result when it comes back.

We are also opinionated about who validation is for. It is not for proving you are right. It is for finding out, as cheaply and as quickly as possible, whether you are wrong. If you cannot describe an experiment whose outcome would make you abandon the idea, you are not yet in validation mode. You are still in advocacy mode, and you are spending capital to confirm what you already believe.

This is why we run a startup validation studio. We are designed around the bias most founders cannot escape on their own: the bias toward continuing. Our experiment library catalogs the staged tests we use across companies, with the thresholds applied to each.

## Common mistakes

**Treating interviews as validation events.**

Interviews are problem evidence at best. They are never solution evidence by themselves. A founder who has run thirty interviews and zero commitment tests has not yet validated anything that matters.

**Letting the threshold move after the result is in.**

You said you needed 8 percent pre-sale conversion. You got 5 percent. You decide 5 percent is "still encouraging given the small sample." The bar drifted. The discipline collapsed. The same logic that justifies 5 percent will justify 3 percent next quarter.

**Confusing interview enthusiasm with demand.**

People are generous in conversation. The same person who said the idea was "exactly what I need" will not pull out a credit card. Stated preference is not revealed preference. Validation lives in revealed preference.

**Skipping channel and retention stages.**

A product can pass problem and solution validation and still be a bad business. If channel economics do not work or retention decays sharply, you have validated an idea you cannot operate. The first two stages are necessary but never sufficient.

**Validating a different population than you will sell to.**

Friends, mentors, advisors, fellow founders. Their enthusiasm validates an audience that will not buy. The cohort you interview must match the cohort you will eventually sell to. If those are different groups, the validation does not transfer.

**Confusing busy with rigorous.**

Sixty interviews and three prototypes and a beta launch can all happen in a quarter without producing a single binding piece of evidence. Activity and rigor are not the same thing. Rigor is what was written in advance, not what was done.

## Frequently asked questions

**Q: How many customer interviews do I need to validate a business idea?**
A: For Stage 1 problem evidence, twenty to twenty-five structured interviews with people who fit the target profile is a reasonable minimum. The number matters less than the structure: two falsifiable questions scored consistently. Twenty interviews with two binary signals beats one hundred interviews scored on vibe.

**Q: How do you test a business idea before launching?**
A: Use a pre-sale or letter-of-intent test, not a free signup. A free signup measures curiosity. A pre-paid deposit, a signed LOI, or a paid pilot calendar slot measures commitment. The cost difference for the participant is the entire point.

**Q: How do you know if a business idea is good?**
A: An idea is "good" when it passes problem evidence, solution evidence, channel evidence, and retention evidence in sequence, each at a pre-stated threshold. An idea is "interesting" when one or two of those signals look positive but the rest are untested. Most ideas that feel good are interesting, not validated.

**Q: What is the difference between business idea validation and market research?**
A: Market research describes the population, its size, and its current behavior. Validation tests whether a specific solution will produce specific actions from a specific subset of that population. Research is descriptive. Validation is predictive and falsifiable.

**Q: What is the Build-Measure-Learn loop?**
A: A loop introduced by Eric Ries in The Lean Startup. Build a minimum viable artifact, measure how the target population responds, and learn whether the underlying assumption was correct. Validation is the outcome of one full loop only when the result clears a threshold stated before the loop began. See our companion piece on [validated learning lean startup](https://www.osresearch.vn/blog/validated-learning-lean-startup) for the evidence standard.

**Q: How much does it cost to validate a business idea?**
A: Less than most founders spend. Stage 1 problem interviews cost time, not money. Stage 2 pre-sale tests cost the price of a one-page site and one to two weeks of paid traffic. Most ideas can be validated or killed for under two thousand dollars. The point of staged validation is that you do not commit Stage 3 budget until Stage 2 has cleared.

**Q: When should I stop validating and start building?**
A: When Stages 1 and 2 have both cleared their thresholds with the cohort you intend to sell to. Channel and retention validation continue alongside building. The mistake is to delay building forever in the name of "more validation," or to start building before Stage 2 commitment evidence exists.

**Q: Can I validate a business idea without quitting my job?**
A: Yes, and you should. Stages 1 and 2 are designed to run in fifty to one hundred hours over the equivalent of a six week testing cycle of evenings and weekends. The point of the staged approach is to keep the cost of being wrong low. Quitting before Stage 2 clears makes the cost of being wrong much higher than it needs to be.
