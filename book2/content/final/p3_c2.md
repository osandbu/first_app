# The Coordination Tax

You need to ship faster. The solution seems obvious: hire more engineers. Double the team, double the throughput. This is the logic of a construction site — twice the workers, twice the concrete poured. It is also exactly wrong for software development, and it has been wrong in documented, quantified ways since at least 1975.

Fred Brooks made the argument in *The Mythical Man-Month*, drawn from his experience running the OS/360 project at a large computing company in the 1960s. He watched a project fall further behind as managers added people to recover the schedule. He named the mechanism precisely: new members require onboarding from existing members; more members require more communication paths between them; and each new person doesn't arrive delivering a full unit of output — they consume fractional output from everyone who has to bring them up to speed. He called his central observation "Brooks's Law": adding manpower to a late software project makes it later.

This was not a soft observation about morale or culture. It was a structural argument with arithmetic. And the arithmetic is worth sitting with for a moment, because it is the mathematical spine of everything in this chapter.

For n people on a team, the number of potential communication channels between them is n×(n-1)/2. Three people: 3 channels. Five people: 10 channels. Ten people: 45 channels. Twenty people: 190 channels. Fifty people: 1,225 channels.

That growth is O(n²). Every person you add doesn't contribute one additional communication link — they add n-1 links to an already-loaded network. And that network, regardless of how well it is managed, requires maintenance. The coordination tax is not a failure of management. It is an arithmetic fact, and arithmetic does not respond to better facilitation.

---

## What Coordination Actually Costs

Most engineering organizations account for meeting time in calendar hours but not in economic terms. Fix that by running the arithmetic on a specific scenario.

Consider a twenty-person platform team. They run three standing planning meetings per week — sprint planning, backlog refinement, a cross-team sync — each ninety minutes. Three additional ad hoc meetings fill the gaps: a quick alignment session on a changing requirement, a discussion about a blocked dependency, a brief architectural review that expanded from twenty minutes to an hour. By the end of a typical week, every engineer on the team has spent four to five hours in meetings whose primary purpose is maintaining shared context.

Run your own number: multiply your team's fully-loaded hourly cost by the meeting hours per week. Then multiply by fifty-two. The result is uncomfortable. That discomfort is information.

The number becomes more jarring when you observe that the team cannot simply stop. If you skip the meetings, two workstreams diverge for two weeks before anyone notices, and the cost of realigning the diverged work exceeds the cost of the meetings you skipped. The meetings are not inefficiency. They are the team's coordination mechanism. The problem is that the team is too large to coordinate any other way.

Every interaction between two people or two groups carries a transaction cost. When two engineers share a desk and a codebase, their transaction cost with each other is low — a chair swivel and a question, a standing conversation in the hallway, shared context built up over weeks of working side by side. When two teams are separated by organizational boundaries, different codebases, different deployment cycles, or different time zones, their transaction cost with each other rises steeply. The coordination tax is transaction cost made visible in the meeting calendar.

Coase's insight about firm boundaries generates a useful decision rule for engineering teams: you should own whatever work is too cognitively dense and interdependent to coordinate via contract, and interface out whatever can be cleanly specified. The boundary between what a team owns and what it interfaces with should follow that line — between work that requires continuous shared context and work that can be handed off at a stable, well-defined interface. This is not just organizational theory. It is the practical reason shared ownership of critical infrastructure is often the highest transaction-cost arrangement possible: every change requires negotiating with a party that also has ownership rights.

Here is what this means in practice. Suppose two teams share a data pipeline that neither fully owns. One team needs to modify the pipeline. The process: schedule a review with the other team, prepare context, negotiate the change, wait for a deployment window that both teams can accommodate, coordinate the rollout. A two-hour engineering task becomes a two-week process. The transaction cost of the shared dependency has swallowed the work itself.

The instinctive response — "just have better meetings" — doesn't address the underlying problem. Better facilitation lowers the transaction cost per meeting; it does not reduce the number of transactions required. If the dependency surface between teams is wide, the transactions are structural. You can make them cheaper. You cannot eliminate them with process alone.

---

## The History Knew This Already

Brooks's Law is fifty years old. The problems it describes are older than software.

Robin Dunbar, an anthropologist studying primate cognition in the early 1990s, found that informal social coordination breaks down around groups of roughly 150 people, above which formal institutions become necessary to hold a group together. The mechanism he proposed — the cognitive load of tracking relationships — is the human-scale version of the same channel-count math. At fifteen to twenty people, informal coordination reaches a natural boundary: below it, everyone knows what everyone else is working on, a decision propagates in an afternoon, context travels over lunch. Above it, those informal pathways fail, and the shared mental model that previously lived in everyone's heads simultaneously now has to be reconstructed through meetings. The fifteen-to-twenty threshold from anthropology maps directly onto the quadratic channel-count arithmetic.

The Apollo program illustrates what happens when you take this to its logical conclusion at genuine scale. At peak, Apollo employed roughly 400,000 people to put twelve on the Moon. Coordination overhead — project management, documentation, review processes, interface negotiation between contractors — consumed an estimated thirty to forty percent of total project cost. Not thirty to forty percent of overhead. Thirty to forty percent of everything.

What Apollo got right — and what made it succeed where projects of comparable ambition have failed — was controlling coordination surface area through interface contracts. The lunar module's guidance software was developed by a team of roughly 100 people. The engineers who thrived at that scale didn't celebrate the overhead — they engineered around it. They narrowed their coordination surface area by defining explicit interface contracts, creating a boundary across which work could proceed without continuous synchronization. Here is what we will deliver, here is the spec we commit to, here is the boundary of our responsibility. Within that boundary, they moved fast. Their internal coordination overhead was manageable. The interface to the outside world was explicit and bounded.

This is the model. Not "small teams always win." Not "scale is always wrong." The model is: coordination surface area is the variable you control, and the way you control it is through architectural and organizational boundaries that constrain where coordination is required.

Gene Amdahl made the parallel argument about parallel computing in 1967. His observation, now called Amdahl's Law: the speedup achievable by parallelizing a computation is limited by the fraction that cannot be parallelized. If twenty percent of a program must run sequentially, no amount of parallelism — no matter how many cores — will ever produce more than a fivefold speedup.

Software development has irreducibly sequential components. Decisions that must be made before work can begin. Interfaces that must be agreed upon before parallel teams can proceed independently. Integration work that requires one system's output before the next can begin. These sequential dependencies don't dissolve because you added engineers. The correct response is to identify and shorten the sequential critical path, not to pile more people onto the parallel parts that are already running at reasonable efficiency. More people on the parallel parts increases coordination overhead without improving the bottleneck. Amdahl's Law becomes an organizational law: you cannot parallelize your way out of sequential dependencies, and adding more people to the parallel portions accelerates the rate at which you run into them.

---

## Why Teams Grow Anyway

If the coordination tax is this well-documented, why do organizations keep building large teams?

The answer is incentives, and the incentives are not mysterious once you look at them clearly.

In most engineering organizations, team size is a legible proxy for importance. A manager with eight direct reports has demonstrable organizational weight in a way that a manager with three does not. Headcount signals investment. When a VP wants to show that a product area is a strategic priority, the visible move is to staff it heavily. When an engineering director wants to demonstrate that they are growing their function, the metric that appears on the career ladder is the number of people they develop. Headcount is the currency of organizational status, and everyone spends it.

This dynamic has nothing to do with whether a large team will actually be more effective. It has everything to do with how effectiveness is proxied and how status is conferred. The team lead who proposes splitting a twenty-person team into three focused teams of six is making a technically sound organizational argument. They are also proposing to reduce their own headcount by two-thirds. The incentive structure makes this argument very hard to make, and harder still to have accepted.

There is a second, subtler driver. When a project is late or struggling, adding people feels like taking action. It is visible, immediate, and unambiguous. The manager who responds to a slipping deadline by adding four engineers is clearly doing something. The manager who responds by proposing a team split and architectural refactor is clearly asking for patience. In environments where motion is conflated with progress, the headcount move wins every time — even when it will make things worse.

This is the counterintuitive property of strained systems: interventions that should theoretically help can increase load before they reduce it. Brooks documented exactly this with headcount additions. A struggling team that adds four engineers typically sees velocity drop for the first four to eight weeks after the hires. The existing engineers are now spending thirty percent of their time in onboarding, pairing sessions, and answering context questions. The new engineers are not yet productive. The codebase's shared mental model, previously held informally by the original team, now has to be reconstructed and re-explained explicitly. Brooks's Law plays out exactly as written. The project that was six weeks late is now ten weeks late, with a larger payroll and a team that is now harder to coordinate.

When you are in a room where headcount is being proposed as the solution to a slipping project, you now have the vocabulary to make the structural argument. The question to ask is not "how many people?" but "what is the dependency structure of the remaining work, and will additional engineers reduce or increase the bottleneck?" That question reframes the decision from resource allocation to system design — which is where the answer actually lives.

---

## The Skeptic's Turn

The obvious objection is that large teams have done large things. Apollo employed 400,000 people. Large engineering projects — infrastructure, hardware, systems with genuine parallelism — require scale. Is the argument here that teams should always be small?

No. The argument is more precise: coordination overhead grows faster than headcount, and the question is always whether the capability gain from adding people exceeds the coordination cost of adding them. The answer depends heavily on the nature of the work.

For work that is genuinely parallel — where tasks can be divided cleanly, where dependencies between subtasks are thin, where each unit of work can be delivered and integrated independently — the gains from scale dominate. Construction is like this in many respects. Manufacturing is. Certain data processing and infrastructure operations are. In these domains, coordination cost is manageable and scale produces proportional gains.

Software product development is not like this in most respects. It is cognitively dense, sequentially dependent, and heavily reliant on shared mental models to proceed efficiently. The integration cost between parallel workstreams is high. The decisions that must be made before work can begin are numerous. The sequential critical path is long. In this kind of work, the breakeven between coordination cost and scale gain happens at surprisingly small team sizes.

The better framing of the counter-argument is: large projects succeed at scale by controlling coordination surface area. Not by pretending the coordination tax doesn't exist, but by investing in the mechanisms that contain it. Interface contracts between teams. Explicit ownership boundaries. Documented specs that allow two groups to proceed independently without continuous synchronization. The Apollo guidance software team succeeded not because it was immune to coordination costs, but because its coordination surface area — the boundary between it and the rest of the program — was narrow, explicit, and well-maintained.

The second objection is that the coordination problem is fundamentally a management problem. Better facilitation, more skilled team leads, tighter process — these could bring coordination overhead under control.

Better management helps at the margin. A skilled team lead running tighter meetings saves real hours per week. But no amount of facilitation removes the O(n²) growth in communication channels that comes with a larger team. The channels exist whether or not they are used efficiently. Process is not a substitute for structure. It is a modifier of a structure that is already determined.

The deeper failure mode of the management-problem framing is that it locates the solution in individual skill rather than system design. The team lead who becomes an expert at running meetings is still running meetings because twenty people require meeting-based coordination. The team lead who splits the team into three groups of six has changed the underlying structure. The first approach optimizes within a system. The second changes the system. These are not equivalent.

There is also an upper bound on what process optimization can achieve. A team with too many dependencies will generate more coordination requirement than any facilitation approach can efficiently handle. At some point, the answer is architectural: reduce the dependencies, define the interfaces, split the team. This is not a failure of management skill — it is the management skill.

---

## Reducing Coordination Surface Area

The lever that matters most is not meeting efficiency. It is dependency architecture.

Coordination overhead is a function of dependencies. Every dependency between two people or two teams generates ongoing transaction cost: conversations to align, meetings to prevent divergence, reviews to catch integration failures, delays while waiting for each other's schedules. The total coordination overhead of a system is proportional to its dependency surface area. Reduce the dependencies, reduce the tax.

This is where Conway's Law, covered in the previous chapter, becomes actionable rather than descriptive. If systems mirror their communication structures, then the inverse is also true: communication requirements follow dependency structures. Two teams that share a data pipeline will always need to coordinate around it. The meeting load is the symptom. The shared dependency is the cause.

The practical interventions follow from this directly.

Define ownership explicitly, not in spirit but in practice. "Shared" ownership of critical infrastructure usually means "nobody owns it, and any change requires coordination." The correct resolution is often to clarify: one team owns it, the other consumes it through a defined interface. The cost of this clarity upfront is lower than the ongoing coordination cost of sustained ambiguity. As a decision rule: own whatever work is too cognitively dense and interdependent to hand off via contract; interface out whatever can be cleanly specified.

Set team size by coordination capacity, not by scope. A team of five to eight people can maintain shared context informally. Above that threshold, the coordination machinery must become formal. If the scope of work requires more people than informal coordination can handle, the correct response is not a larger team — it is multiple teams with well-defined interfaces between them. The scope doesn't determine the team size; the coordination ceiling does.

Split before growing. When a team is struggling with coordination overhead, the reflex is to add a program manager, add another tech lead, add process. The structural question is whether the team can be split such that each resulting team has a narrower, more independent charter. A twenty-person team building a platform for two different consumer products might split into three teams: one per consumer product and one owning the shared infrastructure with a stable interface contract. The coordination surface area narrows dramatically. The transaction costs drop because the dependencies are now explicit and bounded rather than diffuse and renegotiated continuously.

Invest in the interface, not the meeting. When two teams must coordinate, the most expensive form of coordination is synchronous meetings held to maintain shared context. The cheapest durable form is an explicit interface contract maintained in writing — here is what we provide, here is how it behaves, here is how you integrate with it, here is the change protocol. One-time investment in a precise interface eliminates the ongoing transaction cost of continuous alignment. This is why the Apollo guidance software team could move fast within its boundary: the interface was clear enough that they didn't need to coordinate with the rest of the program to do their work.

Coordination overhead consumes the most expensive thing your engineers have: focused cognitive capacity. Four hours per week in synchronization meetings is four hours not spent thinking about the problem. For a twenty-person team, that is eighty person-hours per week of your most experienced people's attention spent on maintaining alignment rather than advancing the work. The customer experiences none of it.

Suppose the work itself could be done by three engineers. Now suppose the organization has assembled fifteen to do it — each bringing a legitimate stakeholder requirement, a distinct team's priorities, a different part of the codebase. The coordination surface area has grown, but the scope hasn't grown proportionally. The standup that three people do over coffee is now a sprint planning meeting for fifteen. The decision that three people make in an afternoon now requires two rounds of async comment and a synchronous review. The six-week ship becomes a partial ship at six weeks, with two workstreams blocked and interfaces under-specified.

The fifteen-person team is not full of bad engineers. The structure of the team makes it nearly impossible to operate at the pace of three people who share a mental model. The coordination tax has consumed the throughput gain from scale.

---

## What Changes Monday

Start by naming the coordination overhead in your current team — not as a vague complaint about too many meetings, but as an economic quantity. How many person-hours per week does your team spend in synchronization activities — meetings, alignment conversations, re-explanation sessions, waiting on dependency resolution? Multiply by your loaded hourly cost. The number will be uncomfortable. That discomfort is information. You now have the vocabulary to make a structural argument rather than a cultural one.

The next conversation to have is about splitting rather than growing. When your team is struggling and the instinct is to add engineers, ask the prior question first: does the existing team have too many cross-cutting dependencies? Would adding people make those dependencies more expensive to maintain before the new engineers are productive enough to help? If the answer to either question is yes, adding people will make the problem worse before it makes it better. The correct proposal is to understand the dependency structure, find the seams where a split would reduce coordination surface area, and define the interface between the resulting teams before adding any headcount.

Audit your meeting load and trace it back to dependencies. For each recurring meeting, ask what dependency it exists to maintain. A weekly cross-team sync exists because two teams share something — a codebase, a pipeline, a deployment process, an organizational accountability — that requires continuous coordination. Each of those dependencies is a candidate for architectural clarification. Some will be unavoidable. Some will reveal ownership ambiguities that can be resolved with a decision, creating a clear owner who communicates via interface contract rather than by consensus.

The longer-term shift is learning to think about team size and team structure as system design decisions, not HR decisions. The communication overhead formula is not a curiosity from a fifty-year-old book — it is an arithmetic constraint on every team you will ever be part of or lead.

Brooks knew it in 1975. Dunbar found it in primate neocortices in 1992. The engineers who built the guidance software for a spacecraft that landed on the Moon learned it by necessity. The math has not changed. What changes is whether you apply it.
