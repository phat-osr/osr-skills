# Minimum Viable Product Examples: What Real MVPs Actually Validate

<aside className="tldr">
**TL;DR.** The most cited minimum viable product examples (Dropbox's explainer video, Airbnb's apartment listing, Buffer's landing page, Zappos' photographed-shoes test) share one feature most coverage misses: each tested a specific named assumption with the smallest possible artifact. The textbook definition from Eric Ries is precise — the version of a product that captures the maximum validated learning with the least effort. The practice has drifted. Most teams now build feature-light products and call the build itself the validation. This piece walks through the canonical MVP examples honestly, the four failure modes that waste founder months, and when to skip the MVP entirely and run a validation experiment instead.
</aside>

## What a minimum viable product actually means

Eric Ries defined the minimum viable product in The Lean Startup as the version of a new product that allows a team to collect the maximum amount of validated learning about customers with the least effort. The definition is precise. It names a specific output, validated learning, and a specific constraint, least effort.

The definition matters because almost every modern use of the term has drifted from it. Search results return ten near-identical pages explaining the definition. They list Airbnb, Uber, and Spotify as examples. They name four types (concierge, wizard of oz, single feature, low fidelity). They invoke build-measure-learn. None of them seriously examine what validated learning means in practice, when an MVP is the wrong tool, or what the failure mode looks like when teams build products and call the construction itself the learning.

The implicit assumption in most MVP content is that you should build an MVP. The question worth asking first is whether you should build one at all. For a meaningful share of validation problems, the answer is no.

## Real-world minimum viable product examples

The most cited MVP examples are useful because each one tested a specific named assumption with the smallest possible artifact. Walking through five of them clarifies what an MVP is supposed to do.

**Dropbox (2008): the explainer video.** Drew Houston wanted to know whether enough people had the file-sync pain to justify building the full product. The MVP was a three-minute video demonstrating the not-yet-built product. The video was posted to Hacker News. Beta signups went from 5,000 to 75,000 overnight. The assumption — that demand existed for the proposed solution — was validated without any product being built.

**Airbnb (2007): renting the founders' own apartment.** Brian Chesky and Joe Gebbia wanted to know whether strangers would pay to stay in a stranger's home for short-term rental. The MVP was their own apartment, a minimalist website, and inflatable mattresses for the guests. Three paying guests booked. The assumption — that the marketplace would clear — was validated with one apartment.

**Buffer (2010): the landing page test.** Joel Gascoigne wanted to know whether the social media scheduling product had paying demand before he built it. The MVP was a two-page website: the first page described the product, the second showed pricing. Signups went to the pricing page; the page itself said "we are not ready yet, leave your email." The signup rate validated demand and the pricing rate validated willingness to pay. Both before a line of product code.

**Zappos (1999): photographed shoes from local stores.** Nick Swinmurn wanted to know whether anyone would buy shoes online. The MVP was a website with photos of shoes from his local shoe stores. When someone ordered, he went to the store, bought the shoes, and shipped them. No inventory, no fulfillment system, no warehouse. The MVP tested demand at the cost of his own legwork. When the orders came consistently, the underlying business was validated.

**Spotify (2008): the landing page plus closed beta.** The Spotify founders tested whether music streaming with reliable quality would attract users by launching a closed-beta landing page with a single product promise: instant, free, reliable music. The waitlist grew. The streaming technology was validated separately through internal testing. Both assumptions confirmed before commercial launch.

Each of these MVP examples shares a structural feature most coverage misses: the founders named the assumption first, designed the smallest possible artifact to test it, and accepted the answer the data gave them. The Airbnb founders did not build an app. The Dropbox founders did not build the sync engine. The Zappos founder did not build a fulfillment system. The discipline produced validated learning at minimum cost.

The drift from this discipline is what the rest of this piece walks through.

## The trap: shipping features and calling it validation

The most common MVP failure mode is what we call theatre. A team has a product idea. They scope down the feature list to a minimum set. They build for three to six months. They launch. They count signups. They declare the MVP a success or a failure based on those signups. Then they iterate.

What is missing from this sequence is the validated learning. The team learned that some people will sign up for a product that solves a stated problem. That is not validated learning. That is a signup count. The actual assumptions the business depends on, whether anyone will pay, whether they will keep using it past 90 days, whether the unit economics work, whether the channel scales, remain untested.

The Ries definition is built around the discipline that the MVP must produce a specific learning outcome about a specific assumption. Most teams skip the assumption-naming step. They build a product, ship it, and call the launch itself the validation. The MVP becomes a vehicle for feature shipping, not for assumption testing. Months are spent. Founders are still no closer to knowing whether the business works.

The four common variants of this trap repeat across hundreds of validation conversations:

**MVP theatre.** Build a feature-light product. Launch. Count signups or downloads. Declare validation. No specific assumption was named beforehand.

**Feature-shipping disguised as MVP.** The MVP grows over six months from a planned three-feature scope to ten features. Each feature addition is justified as "needed for validation." The team is no longer running a learning experiment; they are building the full product more slowly.

**Sunk-cost MVP.** The MVP launches. Early data is ambiguous. The team commits to building more features to "see if it works with X added." Twelve months later they have shipped a complete product they cannot afford to walk away from regardless of what the data shows.

**The wrong-tool MVP.** The team builds an MVP to test an assumption that does not require building anything. Whether customers will pay $50/month for a productivity app can be tested with a landing page and a payment form. Building the app first is the wrong tool.

## What an MVP actually validates

A properly scoped MVP tests one assumption that cannot be tested without building. Common examples:

- Whether the technical approach delivers acceptable quality at acceptable cost (a real-time translation app needs to validate that the latency is usable)
- Whether the workflow integration produces the time savings the customer expects (a developer tool needs to validate that the integration is actually faster than the existing alternative)
- Whether a multi-sided market actually clears (a marketplace needs both sides active to validate liquidity)
- Whether the unit economics survive at small scale (does CAC payback actually land within target when real money is spent)

What an MVP does not validate well:

- Whether anyone wants the product (landing page + ad test is faster)
- Whether the price point clears (interview + pre-sale is faster)
- Whether the messaging resonates (copy test is faster)
- Whether the segment is right (customer development is faster)
- Whether the channel works (channel experiment is faster)

The implication is structural. For most of the assumptions a founder starts with, an MVP is not the most efficient tool to test them. Building should be the last validation step, not the first.

## When to skip the MVP entirely

Some assumptions are best tested without writing code. The OSR [experiment library](https://www.osresearch.vn/blog/experiment-library) catalogs validation tests that produce sharper learning at lower cost than an MVP would. Three patterns worth naming:

The landing page test. Build a clear value proposition page, drive paid traffic to it, measure conversion to email signup or pre-payment. Tests demand existence without building product. Cost: one to two weeks of work, $500 to $2,000 of ad spend.

The concierge or wizard-of-oz test. Deliver the product service manually to the first ten customers. The customer experiences the value. The team experiences the operational reality. No product is built; the team learns whether the value proposition holds with real money attached. Cost: time of the founders, no engineering required.

The customer development sprint. Run twenty structured interviews with potential customers. Validate or invalidate the assumed problem framing, the willingness to pay, and the buying process. The output is sharper than any MVP signup count. Cost: two to three weeks of founder time.

The decision rule we use: only build an MVP after the validation experiments have confirmed that the underlying business is real and the remaining assumption can only be tested by building. If you cannot name the specific assumption your MVP will test, you are not ready to build one. The MVP becomes feature-shipping.

This is the framework underneath the OSR [six week testing cycle](https://www.osresearch.vn/blog/six-week-testing-cycle): a structured sprint of validation experiments that gates the decision to build.

## A worked example: when the wrong MVP burns six months

A founder we observed had an idea for a SaaS product helping freelance accountants manage their client communication. The team scoped an MVP: client portal, basic messaging, invoice tracking, and a notifications system. They estimated three months of build, then launch and iterate.

The build took five months. The launch produced 60 signups in the first two months. About 12 of them actively used the product. Three paid for a subscription. The team interpreted the data as "promising early traction" and committed to four more months of feature additions: integrations with QuickBooks, mobile app, team collaboration. By month twelve, they had spent the entire seed round.

What the team had not done before building: validated that the freelance accountant segment actually felt the problem urgently enough to switch tools. Twenty structured interviews would have revealed in three weeks that the segment was deeply attached to email and spreadsheets, switching cost was high, and willingness to pay was concentrated in the largest accountants who needed enterprise features the team had not built. The MVP was scoped against the wrong assumption.

The team rebuilt the validation approach: interviews with thirty target customers, a landing page targeting the larger-firm segment, a concierge test serving five firms manually. Within eight weeks, they had clearer learning than the twelve months of MVP iteration had produced. The pivot direction was clear. The remaining capital was redeployed.

The cost of the wrong MVP was not the build expense alone. It was the eleven months of validated-learning forgone while the team was busy building.

## How to scope an MVP correctly when you do need one

If you have validated the underlying business and the only remaining assumption requires building, the MVP scope follows from the assumption.

Name the assumption. Write it as a falsifiable statement. "Our real-time translation engine will produce usable latency under 300ms for 90 percent of conversational exchanges."

Define the test. What measurement proves or disproves the assumption. "We will measure end-to-end latency across 1,000 exchanges from 50 users in the target customer segment."

Scope the smallest product that runs the test. Strip anything that does not produce the measurement. If user accounts are not needed to test latency, do not build user accounts. If the UI does not affect the measurement, ship without UI polish.

Set a learning deadline, not a feature deadline. "We will have measured the latency by end of week six." If the measurement is not complete at the deadline, stop adding features and ship what runs.

Pre-commit to the decision rule. "If 90 percent of exchanges are under 300ms, we proceed. If not, we either pivot the technical approach or kill the business." Without the decision rule, every result becomes ambiguous and the team continues building.

The discipline turns the MVP back into what Ries proposed: a vehicle for learning, not for shipping.

## What OS Research thinks

The MVP is one of the most useful frameworks in startup methodology and one of the most abused. The misuse pattern is consistent: founders adopt the term without the assumption-naming discipline that makes it work, and they build products that ship features rather than test hypotheses.

Our view is that an MVP is the right tool for a narrow set of validation problems, specifically those where the assumption can only be tested by building. For most early-stage assumptions, an MVP is the wrong tool. The OSR [validate business idea](https://www.osresearch.vn/blog/validate-business-idea) framework is built around this: pre-MVP validation experiments come first, and the build decision is gated on what they show.

The canonical lean startup texts get the framework right. The drift is in the practice. Most teams have stopped doing the validated learning step that the MVP was designed to enable. The fix is not abandoning the MVP; it is reclaiming the discipline that the term originally implied. Skip the MVP when validation experiments can do the work. Build only when the assumption requires it. Pre-commit to the learning outcome before the first line of code.

## Common mistakes

**Building before naming the assumption.** Teams scope features before naming what they want to learn. The result is a product that ships but produces no validated learning. Always start with the falsifiable assumption.

**Treating launch as validation.** A launch is an event. Validated learning is a measurement of a specific outcome against a specific assumption. Conflating the two produces feature-shipping disguised as validation.

**Extending the MVP indefinitely.** Each feature addition is justified as "needed for validation." Six months in, the scope is the full product. The fix is the pre-committed learning deadline. When the deadline arrives, ship and measure.

**Building when interviews would have answered the question.** Founders default to building when the underlying assumption can be tested in three weeks of customer interviews. Build is the most expensive validation tool. Use it last, not first.

**Ignoring the decision rule.** The MVP produces a result. Without a pre-committed decision rule, every result becomes interpretable as encouraging. The fix is naming the kill criteria before launch.

**Confusing fidelity with validation.** A high-fidelity MVP looks like a real product. The look is irrelevant to whether the assumption is being tested. A low-fidelity test that produces sharper data is more valuable than a polished build that produces signup counts.

## Frequently asked questions

**Q: What is a minimum viable product?**
A: Per Eric Ries' original definition, the version of a new product that allows a team to collect the maximum amount of validated learning about customers with the least effort. In practice, an MVP should test a specific, named assumption that cannot be tested without building. If you cannot name the assumption, you are not yet ready to build one.

**Q: What is an example of an MVP?**
A: Dropbox's original explainer video, which tested demand before any product was built and produced 75,000 signups overnight. Airbnb's founders renting their own apartment to validate the marketplace concept before scaling. The canonical MVPs share a feature: they tested a specific assumption with the smallest possible artifact.

**Q: What is the difference between an MVP and a prototype?**
A: A prototype is a demonstration artifact, often used to show design intent or technical feasibility internally. An MVP is a validation artifact, deployed to real users to test a specific assumption. Prototypes inform design decisions; MVPs inform business decisions.

**Q: What are the types of MVP?**
A: The commonly named types are concierge MVP (delivering the service manually), wizard of oz MVP (the user sees an automated experience but humans operate it behind the scenes), single-feature MVP (one core feature), landing-page MVP (a marketing page to test demand), and high-fidelity prototype MVP (a polished but limited build). The choice between them follows from the assumption being tested, not from default preference.

**Q: Why is a minimum viable product important?**
A: Because building products is expensive and time-consuming. The MVP framework lets founders test critical assumptions before committing to full product development. The importance is in the validation discipline, not in the MVP artifact itself. Teams that ship MVPs without validation discipline often waste more time than teams that test assumptions first and build less.

**Q: How do I know if my MVP succeeded?**
A: You know when you can answer the assumption you set out to test with a falsifiable yes or no. Signup counts and download numbers are not success criteria; they are vanity metrics. Success means: the assumption is either confirmed (proceed) or disconfirmed (pivot or kill). Anything ambiguous means the MVP was not scoped to test a specific enough assumption.

**Q: How long should an MVP take to build?**
A: As short as possible given the assumption. Most well-scoped MVPs should take four to twelve weeks. MVPs that take longer than three months usually indicate the scope has grown beyond the original learning goal, or the assumption requires more than building can validate. Use [validated learning lean startup](https://www.osresearch.vn/blog/validated-learning-lean-startup) practices to compress the timeline.

**Q: Should every startup build an MVP?**
A: No. For many early-stage assumptions, validation experiments produce sharper learning at lower cost than an MVP would. Build an MVP only when the assumption cannot be tested without building. For everything else, see our [experiment library](https://www.osresearch.vn/blog/experiment-library) for non-build validation patterns.

**Q: What is the relationship between MVP and product-market fit?**
A: The MVP is a tool to test specific assumptions. Product-market fit is the state where the market consistently values what you have built. An MVP can help you validate the assumptions that lead toward product-market fit, but the MVP itself does not produce fit. Many MVPs ship without ever leading to fit, which is why the validation discipline matters more than the MVP artifact.

**Q: How is an MVP different from a proof of concept?**
A: A proof of concept demonstrates that something is technically feasible, often used in enterprise sales contexts. An MVP demonstrates that customers actually value the proof of concept enough to use or pay for it. The technical proof comes first; the validation proof comes second. Conflating them produces products that work but no one wants.
