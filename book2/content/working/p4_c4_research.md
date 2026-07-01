# Research Notes: p4_c4 "Build vs. Buy Is a Strategy Question"

## Core Thesis / Argument Arc

Build vs. buy is treated as a technical question by most engineers — API surface,
integration effort, performance characteristics — and then they watch the decision go
over their heads. That's because it isn't a technical question. It's a strategy
question: what capabilities does your organization own, and what does ownership mean?
The language of the decision is core competency, transaction cost, and strategic risk —
not technical merit. This chapter gives engineers that language so they can participate
in the decision rather than watch it happen to them.

---

## Historical Parallels

### 1. The IBM PC and the Operating System That Got Away (1981)

In 1980, IBM was designing the personal computer on an accelerated timeline — less than
a year from project greenlight to launch. To meet that timeline, IBM made an
unprecedented choice for the era: source key components from outside vendors rather than
build everything in-house, as was IBM's tradition. They licensed the microprocessor from
an external vendor and sourced the operating system from a small company that didn't
actually own the operating system they licensed — it was acquired from another small
vendor days before the deal closed.

The critical clause: IBM did not acquire exclusive rights to the operating system. The
supplier retained the right to license it to others. IBM accepted this because the
decision-makers considered the operating system a commodity — they were focused on the
hardware, which they believed was the source of their competitive advantage. The
operating system was plumbing.

Within five years, IBM had created the dominant computing platform and watched most of
the economic value flow to the operating system vendor, not to IBM. Clones running the
same operating system eroded IBM's hardware margin entirely. The strategic asset IBM
ceded control of became the most profitable franchise in computing history for decades.

The lesson is not "IBM was stupid." The decision made sense at the time under real
constraints. The lesson is: the commodity layer of today can become the differentiator
of tomorrow, and once you cede control of a component, reacquiring it is nearly
impossible. IBM's executives were doing hardware economics; they failed to see that
software economics were different — marginal cost of zero means software value
compounds differently than hardware value.

### 2. The Mainframe-to-PC Transition and the Buy Revolution (1980s–1990s)

Before the PC era, large computing installations were almost entirely custom: custom
hardware, custom operating systems, custom applications. The idea of buying standardized
software off a shelf was largely foreign to enterprise computing. Organizations had
entire departments of programmers maintaining bespoke payroll systems, inventory systems,
and financial ledgers — systems that were deeply integrated with the organization's
specific processes.

The packaged software revolution of the 1980s and 1990s — general-purpose database
management systems, enterprise resource planning suites, accounting packages — offered
a proposition that was genuinely novel: stop building commodity capabilities and buy
them instead. The economic logic was straightforward. A company's finance department
does not differentiate on the accounting software it uses. Why should it build and
maintain that software?

The resistance was equally genuine. Organizations that had invested years in custom
systems pushed back. "Our processes are unique." "The vendor's data model doesn't fit
ours." "We'll lose control." Some of this resistance was correct. Much of it was
institutional inertia dressed as technical objection.

What this transition reveals is the shape of the underlying question: commodity
capabilities — things every organization in your industry needs, that don't differentiate
you from competitors — are candidates for buying. But the definition of "commodity"
shifts over time. When packaged accounting software was new, skeptics called it
unsuitable. Within a decade it was the default. The question is not just what is
commodity today, but what is on the path to becoming commodity.

### 3. Open Source and the Commoditization of Infrastructure (1990s–2000s)

The open source movement introduced a third option that hadn't existed at scale before:
neither build (own it entirely) nor buy (pay a vendor for it) but adopt (use
collaboratively maintained software that belongs to no one). This changed the build vs.
buy calculation in a specific way: the commodity layer became nearly free.

Operating system kernels, web servers, programming language runtimes, cryptographic
libraries — infrastructure that previously cost significant money to license — became
freely available. This shifted the build vs. buy question upward in the stack. You no
longer had to decide whether to build a web server; you adopted an existing one. The
question became what to build on top of that layer.

Open source also introduced a new strategic risk: the project abandonment problem.
When you buy a vendor's product, you have a contract and (theoretically) support. When
you adopt open source, you have a community that may or may not persist. Organizations
that built critical infrastructure on open source projects that subsequently lost
maintainers found themselves in a worse position than if they'd bought: they had
accumulated dependency on code they hadn't written and now had to either take over
maintenance or migrate.

The open source case also illustrates the contribution asymmetry: large organizations
often use open source software at significant scale while contributing little back to
maintenance. The free rider problem in open source is well-documented — a small number
of maintainers bear the cost of maintaining software that thousands of organizations
depend on. When those maintainers burn out or move on, the organizations that assumed
the software was permanently maintained discover the assumption was wrong.

### 4. SaaS and the Subscription Economy (2000s–2010s)

Software-as-a-service extended the buy argument further: not only can you avoid
building commodity software, you can avoid running it too. The total cost of ownership
argument shifted: a SaaS product's price includes hosting, maintenance, security
patching, and upgrades that an on-premise solution required internal labor to provide.

For functions clearly outside the engineering core — sales tools, HR platforms, support
ticketing — the SaaS argument was compelling. But SaaS introduced a new version of the
vendor lock-in problem: data lock-in. When a customer relationship management system
accumulates years of customer data structured according to the vendor's schema, migrating
away requires not just replacing the software but extracting and transforming all that
data into whatever schema the next vendor uses. The switching cost is no longer license
fees — it's data migration complexity.

Organizations that chose SaaS for convenience found that the vendor's data model had
quietly become their data model. Customer segments defined in the vendor's taxonomy,
sales pipelines structured around the vendor's workflow, reporting built on the vendor's
fields — these are not easy to untangle. The lock-in had shifted from the software to
the accumulated organizational behavior organized around the software.

---

## Key Frameworks

### Core Competency Theory (Prahalad & Hamel, 1990)

Prahalad and Hamel's 1990 Harvard Business Review article "The Core Competence of the
Corporation" introduced the idea that organizations should focus investment on the
distinctive capabilities that create competitive advantage and source everything else.
A core competency, by their definition, has three properties: it provides access to a
wide variety of markets, it makes a significant contribution to the perceived customer
benefit of the end product, and it is difficult for competitors to imitate.

Applied to build vs. buy: build what is core competency; buy what is not. A company
whose differentiation is search relevance should own its search infrastructure. A
company whose differentiation is supply chain logistics should not spend engineering
cycles building a custom email marketing platform. The mistake engineers often make is
treating technical interest as a proxy for strategic importance. A capability can be
technically interesting and strategically irrelevant.

The challenge in practice: identifying what is actually core competency requires
strategic clarity that many organizations lack. Engineering teams often don't have
visibility into what leadership considers differentiating. And leadership often hasn't
thought about it clearly. The build vs. buy decision surfaces this ambiguity — which
is part of why it's so often contentious.

### Transaction Cost Economics (Make-or-Buy, Williamson, 1975)

Oliver Williamson's transaction cost framework asks: what is the total cost of
transacting with an external supplier versus doing the thing yourself? Transaction costs
include not just the price of the product but: search costs (finding and evaluating
vendors), contracting costs (negotiating, writing, enforcing the agreement), monitoring
costs (verifying vendor performance), and switching costs (the cost of changing vendors
if the relationship fails).

When transactions are simple and the market is competitive, buying is usually cheaper
than building — the transaction costs are low and the vendor has scale advantages.
When transactions involve high specificity (the vendor's product needs to be customized
substantially to your needs), high uncertainty (hard to specify what you need in
advance), or high switching costs (moving is expensive), the calculus shifts toward
building or toward long-term lock-in risk if you still buy.

Williamson's framework predicts: the more idiosyncratic your requirement, the more
likely you should build, because no vendor's standard product will fit and customization
compounds over time.

### Commodity vs. Differentiator Matrix

A practical two-dimensional analysis: place each capability on a matrix with axes of
(1) how much this differentiates you from competitors and (2) how much internal
engineering effort it currently consumes. Capabilities that are low-differentiating and
high-effort are the clearest buy candidates — they absorb engineering capacity that
could be applied to what actually differentiates you. Capabilities that are
high-differentiating should generally be built and owned, regardless of effort, because
they are the source of competitive advantage.

The dangerous quadrant is high-differentiating, low-effort capabilities that attract
buy proposals because they look cheap. If something is genuinely differentiating, ceding
control of it to a vendor — even at low cost today — creates strategic risk. The
vendor's incentives may not align with yours; they may raise prices, change terms, or
be acquired.

### Vendor Lock-In Risk Analysis

Lock-in risk has multiple dimensions that are worth analyzing separately:

- **Switching cost lock-in**: how expensive is it to replace this vendor? (integration
  depth, data migration, retraining)
- **Capability lock-in**: have you atrophied the internal capability to do this yourself?
  (if you've bought authentication for five years, can you still build it?)
- **Data lock-in**: is your data in the vendor's schema, format, or location such that
  extraction is non-trivial?
- **Network lock-in**: does value come from the fact that others are also using this
  vendor (integrations, compatibility)?

Organizations routinely underestimate switching costs at the time of the buy decision.
Vendor sales cycles emphasize integration ease (going in) while downplaying migration
complexity (going out). A useful due diligence exercise: before signing a vendor
contract, spend an hour designing the exit. What would it take to move off this vendor
in three years? If that exercise produces a lengthy migration plan, the switching cost
is real and should factor into the initial decision.

### Wardley Mapping (Value Chain Evolution)

A strategic mapping framework (developed independently in the open strategy community)
that places capabilities on a two-axis map: the vertical axis represents the value
chain (user need at top, underlying components below), the horizontal axis represents
evolutionary stage (genesis → custom-built → product → commodity/utility). 

The framework's core insight: all capabilities evolve toward commoditization over time
through competition and standardization. A capability that requires custom engineering
today may be available as a standard product in three years and as a utility in five.
Strategy involves both predicting where capabilities are heading and recognizing that
investing heavily in building capabilities that are about to become commodities wastes
resources that could be applied elsewhere.

For build vs. buy: if a capability is in the "custom-built" phase and moving toward
"product," a buy decision timed correctly avoids the cost of building something that
will be available cheaper externally in the near future. If a capability is in the
"genesis" phase (no good external options exist), building may be necessary — and the
question becomes whether to try to maintain that position as the capability matures.

---

## Concrete Scenarios

### 1. The Authentication System That Became a Security Liability

A product team, early-stage, decides to build their own authentication system. The
reasoning is reasonable at the time: commodity solutions don't quite fit the UX
requirements, the team has the capability, and the scope seems manageable. The system
ships. Over the next three years, authentication standards evolve (new token formats,
new attack vectors, multi-factor requirements), the original engineers move on, and
the authentication code accumulates the characteristic properties of legacy code:
nobody fully understands it, changes require careful archaeology, and security reviews
reveal gaps that the original team didn't anticipate.

Each new security requirement — FIDO2 support, breached credential detection,
compliance requirements — requires engineering time to retrofit into a bespoke system.
Meanwhile, commodity solutions have evolved to handle all of these. The cost of the
original build decision is now visible: years of maintenance burden and recurring
security risk on a capability that does not differentiate the product at all. The
engineering team's identity is now partially wrapped up in "our custom auth system,"
making the conversation about migrating to a commodity solution politically loaded in
addition to technically costly.

### 2. The CRM Data Model Trap

A mid-size company selects an enterprise CRM platform for their sales organization.
The selection is primarily driven by the sales team — IT and engineering are advisory.
Over five years, the company's customer data accumulates in the vendor's data model:
custom fields mapped to the vendor's schema, integrations built against the vendor's
API, analytics reports built in the vendor's reporting tool, a sales process that
evolved to match the vendor's workflow.

When the company needs to change CRM platforms (the vendor raises prices, or the
vendor is acquired, or the platform simply ages), the migration project surfaces the
real cost: years of organizational behavior and operational data are structured around
the vendor's conventions. The "customer" in the old system doesn't map cleanly to
the "customer" in the new system. The sales pipeline stages don't translate. The
custom fields are idiosyncratic to the old platform's data model. The migration
project, initially estimated at three months, takes eighteen months and requires
significant data transformation work. The total cost of vendor lock-in, never
calculated at selection time, is now on the table.

### 3. The Infrastructure Abstraction That Wasn't

A platform team, responding to the classic build vs. buy tension around cloud
infrastructure, decides to build an internal abstraction layer. The goal is
vendor-independence: the abstraction should allow the company to switch cloud
providers without changing application code. This is an admirable goal in principle.

In practice: the abstraction layer adds development overhead (every new cloud feature
must be wrapped), adds operational complexity (the abstraction must be maintained and
debugged in addition to the underlying infrastructure), and creates a capability gap
(cloud provider features that don't fit cleanly into the abstraction are simply not
exposed, which frustrates application developers). Meanwhile, the probability of
actually switching cloud providers — the risk the abstraction was designed to hedge
against — turns out to be low. The company paid a real and ongoing cost to hedge
against a risk that wasn't worth hedging at that price.

The lesson: build vs. buy must include an honest assessment of risk probability, not
just risk magnitude. A catastrophic but highly unlikely risk may not warrant expensive
architectural mitigation.

### 4. The Open Source Dependency That Lost Its Maintainer

An engineering team builds a data pipeline on top of a well-regarded open source
library. The library is mature, well-documented, and has an active community at the
time of adoption. Over three years, the lead maintainer burns out and steps back. The
community fragments. Security vulnerabilities are discovered and patches are slow. The
library falls behind newer developments in the ecosystem.

The team now has three options: maintain the library themselves (they become maintainers
of a project they didn't author), migrate to a different library (expensive), or stay
on an unmaintained dependency (security risk, technical debt). None of these options
were visible in the original adoption decision. The risk of open source isn't the
licensing — it's the maintenance continuity assumption.

### 5. The Team That Built What It Could Have Bought

A team spends a quarter building a feature flagging system. The system is competent and
well-tested. It ships. Over the following year, the team fields requests for: gradual
rollout controls, targeting rules based on user properties, an audit log, a UI for
non-technical stakeholders, integration with the analytics platform. Each of these is
a reasonable extension. Each requires engineering time. By the end of year two, the
team has something that closely resembles the commodity feature flagging products that
existed before they started building.

The calculation the team originally made — "the commodity products are more than we
need" — was correct at the time. The calculation they didn't make: what will we need
in two years, and what is the cost of building toward it incrementally versus starting
with a platform designed for it? Feature flagging is not a differentiating capability
for most products. The engineering time invested would have generated more value applied
to the features that actually differentiated the product.

### 6. The Platform That Overreached Into Core Product Territory

A large organization's platform team, tasked with providing internal capabilities to
product teams, gradually builds further and further up the stack. What starts as
infrastructure becomes a framework, then an application platform, then — as the platform
team adds business logic to simplify integration — something that encodes product
decisions. Product teams begin to feel that platform choices constrain product
direction. Migrating off the platform is expensive; they're locked in to an internal
vendor.

This is the internal build-vs-buy problem: even internally-built capabilities can
produce lock-in if they accumulate enough coupling. The same risk analysis that applies
to external vendors applies to internal platforms. The platform team's reasonable goal
(reduce duplication, increase leverage) produces the same structural risks as an
external dependency when the platform becomes too deeply embedded in product behavior.

---

## Counter-Arguments

### "Building gives you control and understanding that buying never could"

This is true and deserves a genuine response rather than dismissal. There are
categories of capability where building is the correct answer not despite higher cost
but because of what the building process produces. A company whose differentiation is
real-time data processing needs engineers who deeply understand data processing. Buying
that capability from a vendor produces a black box: it works until it doesn't, and when
it doesn't, the team doesn't have the knowledge to diagnose or fix it.

The nuanced response: build for understanding when understanding is itself the strategic
asset. The question is not just "what does the component cost to build?" but "what does
the team learn by building it, and is that learning valuable?" For commodity
capabilities, the learning is not valuable enough to justify the cost — everyone who
needs a payment processor doesn't need to deeply understand payment processing. For
core competencies, the learning may be the whole point.

Additionally, building enforces clarity of requirements. When you buy, you accept the
vendor's data model, API design, and operational model. When you build, you are forced
to specify exactly what you need — which is sometimes more than buying and sometimes a
clarifying discipline.

### "Vendor solutions are never exactly right; you always end up customizing anyway"

Also true, and the argument for building from this is: if you're going to spend
significant engineering time customizing a vendor product, you might spend it more
productively building something that fits exactly. The buy-and-customize path combines
the costs of both: you pay vendor licensing fees AND spend engineering time, and you
end up with something that is neither a standard product (losing future vendor updates)
nor a clean custom build (losing architectural control).

The nuanced response: the relevant question is where on the customization spectrum
you're likely to land. If customization is genuinely bounded — a few configuration
parameters, a few integrations — the buy calculation holds. If the vendor's core data
model or workflow is fundamentally incompatible with your requirements, the total cost
of customization often exceeds the cost of building to spec. The trap is the gap between
"we'll just customize a few things" (the promise) and "we've spent two years building
on top of a vendor API and now we can't move" (the outcome).

The counter-counter-argument: the discipline of working within a vendor's model is
sometimes valuable precisely because it prevents scope creep. Building from scratch
produces infinite flexibility, which produces infinite scope. Sometimes a vendor's
opinionated model forces the organization to fit their processes to a standard rather
than building an infinitely customized solution that only their organization understands.

---

## Data Points and Studies

- Research on enterprise software projects consistently shows that a majority of
  large-scale custom builds overrun schedule and budget estimates, often by factors of
  two to three. Studies of software project failure from the Standish Group (CHAOS
  reports) show that project success rates correlate inversely with project size and
  duration — longer custom builds fail more.

- Studies of total cost of ownership for enterprise software show that the initial
  licensing or build cost typically represents 20–30% of the total ten-year cost; the
  remainder is maintenance, integration, training, and updates. The build vs. buy
  decision made on initial cost alone systematically underestimates total cost for both
  options.

- The "innovation stack" concept, drawn from research on entrepreneurial competitive
  advantage, identifies that companies which successfully disrupted incumbents did so
  not by optimizing one capability but by building a mutually reinforcing set of novel
  capabilities. When one capability in the stack is bought from a vendor, the
  interlocking advantage is harder to achieve — the vendor's version of the capability
  is available to competitors as well.

- Research on switching costs in enterprise software (academic literature on technology
  lock-in and switching costs) consistently finds that actual switching costs are two
  to five times higher than organizations estimated at adoption time. The primary
  underestimated costs are data migration, process re-engineering, and retraining —
  none of which are visible in the vendor's initial proposal.

- Transaction cost economics research (Williamson's empirical work and subsequent
  scholarship) shows that vertical integration (building) is more common in industries
  with high asset specificity — where the capability is highly specific to the
  organization's context. This predicts that commodity capabilities should be bought
  and idiosyncratic capabilities should be built, which matches observed behavior in
  industries with mature make-or-buy norms (automotive supply chains, aerospace).

- Open source sustainability research (studies of major open source projects) shows
  that a small number of contributors (typically fewer than 5% of users) account for
  the majority of maintenance work. The "tragedy of the commons" dynamic in open source
  is well-documented: organizations free-ride on open source at scale because the
  marginal cost is zero, but the aggregate effect is systematic undermaintenance of
  critical infrastructure. The Log4Shell vulnerability (2021, unnamed here as the
  specific product) exposed how widely critical open source libraries had been adopted
  without corresponding investment in their maintenance.

---

## Suggested Chapter Structure

1. **The Language Mismatch** — Engineers frame build vs. buy as a technical question
   (API quality, integration effort, performance). Decision-makers frame it as a
   strategic question (what capabilities define us, what risks are we taking). The
   chapter opens with the observation that engineers who make the best technical case
   keep losing these decisions — not because they're wrong about the technology, but
   because they're answering a different question than the one being asked.

2. **What "Own" Actually Means** — Core competency theory applied concretely. What does
   it mean to own a capability? Not just that you built it — that you understand it
   deeply, that you can change it, that it reflects your organization's specific
   requirements in ways a vendor can't replicate. The historical parallels: the PC
   operating system story as a case study in what happens when you cede control of
   something that turns out to be strategic.

3. **The Commodity Ladder** — The Wardley-style insight that all capabilities evolve
   toward commoditization. Yesterday's differentiator is today's commodity. The
   mainframe-to-PC transition, the packaged software revolution, the open source
   commoditization of infrastructure. The strategic question is not just "is this
   commodity now?" but "is this on the path to commodity?" If so, building it is
   investment in something that will become available free or cheap — timing matters.

4. **Lock-In Is Not One Thing** — Disaggregating lock-in risk into switching cost,
   capability atrophy, data lock-in, and network lock-in. For each: how to assess it,
   how to hedge against it, and when the risk is worth accepting. The due diligence
   exercise: before signing, design the exit. Scenarios: the CRM data model trap, the
   authentication security liability.

5. **The Skeptic's Case (and Its Limits)** — Genuine engagement with the "build for
   understanding" and "vendors never fit exactly" arguments. When building is the right
   answer and why. The nuance: it depends on whether the learning is the strategic
   asset, and on where on the customization spectrum you're realistically going to land.

6. **Translating for the Room** — Practical advice on how to participate in build vs.
   buy decisions rather than watching them happen. How to frame the conversation in
   strategic terms: what is core competency, what are the real lock-in risks, what is
   the true total cost of ownership. The senior engineer who can make this case in the
   language of strategy — not just technical merit — gets a seat at the table.
