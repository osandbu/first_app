# Your Mental Model of a Company Is Wrong

You've been in this meeting before. Maybe it was a technical proposal you spent two weeks building — architecture clean, tradeoffs documented, migration path spelled out. Or a refactor you'd been advocating for across five planning cycles. Or the obvious fix to a process that everyone agrees is broken. The decision should have been simple. It wasn't even close. And then it went the wrong way, for reasons that seemed almost unrelated to the merits.

The first instinct, natural and nearly universal: somebody in that room was wrong, or irrational, or playing politics for its own sake. Somebody didn't do the analysis. Somebody is protecting their turf. Somebody is just bad at their job.

Sometimes that's true. But far more often, something else is going on — something that looks like irrational behavior from the outside and makes complete sense from the inside. The gap between those two views is a mental model problem. Specifically, yours.

Engineers carry a particular mental model of how organizations work. It's precise, it's coherent, it's extremely useful for some purposes, and it will lead you badly astray when applied to the wrong thing. This chapter is about naming that model, understanding where it came from, and replacing it with one that actually predicts organizational behavior. Until you do that, the decisions that happen in rooms you weren't in will keep seeming inexplicable.

---

## The Machine Metaphor

There's a specific origin story for how engineers think about organizations, and it starts with engineers.

Frederick Winslow Taylor, a mechanical engineer working in the late nineteenth century, became convinced that industrial labor could be analyzed the same way a machine could — by breaking it into component motions, measuring each one with a stopwatch, standardizing the best method, and specifying it to workers the way you'd specify tolerances on a part. His 1911 book formalized this as "scientific management." The idea swept through industrial enterprises with missionary force. Frank Gilbreth applied it to bricklaying. Henry Ford built it into assembly lines. Management science as a discipline — the whole infrastructure of organizational roles, productivity measurement, standardized processes — was built on top of Taylor's premise: organizations are machines, and engineers are qualified to optimize them.

This is where your mental model comes from. Not abstractly, not just because you studied computer science — but historically, because engineers literally constructed the intellectual framework through which Western industrial society thinks about organizations. The metaphor was built by people whose primary mental model was mechanism. They imported mechanism wholesale.

The machine metaphor is powerful and genuinely useful in narrow conditions. When work is routine, the environment is stable, inputs are well-defined, and the right output can be specified in advance, treating an organization as a machine to be optimized is productive. Early twentieth century factory production met most of these conditions. You can time-motion-study a steel stamping line.

The problem is that the mental model doesn't know its own limits. Engineers are trained on deterministic systems: the same input produces the same output every time. When a system produces bad outputs, there is a faulty component. Find the component, fix the component, restore correct function. Rerun the tests. This is an extraordinarily powerful way to reason about systems that are actually machines. Applied to organizations, it produces systematic confusion.

When a software engineer says "we need to fix the process," "the system is broken," "find the bottleneck," "this is a coordination problem we can solve with better tooling" — these are Taylorist framings. The machine metaphor is so deeply embedded it doesn't feel like a metaphor. It feels like neutral description. That's how mental models work when they're functioning as defaults: they disappear into the background and become the water you're swimming in.

The irony is exact: the engineers most likely to be frustrated by irrational organizational behavior are the engineers most deeply trained in the tradition that built the flawed model for understanding it.

---

## The Organism Reality

In 1986, Gareth Morgan published a book cataloging the different metaphors people use to understand organizations — machine, organism, brain, culture, political system, psychic prison, and others. His central insight was that the metaphor you're using determines what you can see and what you're blind to. The machine metaphor makes certain questions visible and certain questions invisible. Change the metaphor and you can see different things.

The organism metaphor — the second of Morgan's three that matter most here — asks different questions. Not "what component is malfunctioning?" but "what environmental pressure is the organism adapting to?" Not "how do we optimize this process?" but "what survival pressure is this behavior a response to?"

Organisms do things that don't make sense if you're looking for optimizing logic. A tree doesn't grow toward sunlight because it computed the optimal direction — it grows toward sunlight because that's the adaptation that survived. Organizations behave similarly. They do things that look suboptimal from outside, that look like clear errors, that look like dysfunction — and those behaviors are often adaptations to real pressures that aren't visible to the observer.

Take a team at a mid-size software company that keeps shipping features nobody uses. From the outside, this is baffling. The team is full of smart people. They clearly care about quality. Why don't they do user research? Why don't they look at adoption data? Every engineer on the team can articulate the argument for customer discovery. And then they ship another feature nobody uses.

From the inside, the picture is completely different. The team is measured on velocity. Their performance reviews reference features shipped. Their quarterly goals are written in terms of output, not outcomes. User research takes time, produces ambiguous results, and generates information that might require delaying or killing features that are already scoped. Shipping features produces clear, countable, attributable output. Every incentive in the environment is pointing toward shipping. The team isn't malfunctioning — it's adapted to its environment. Change the measurement system and the behavior changes. Tell the team to "be more customer-focused" without changing the measurements, and nothing changes. The adaptation persists because the pressure persists.

This is not a story about bad people or a broken team. It's a story about an organism shaped by its environment. When you encounter behavior that looks obviously wrong, the organism question — "what pressure produced this adaptation?" — will give you a more useful answer than the machine question of "which component is faulty?"

---

## Local Rationality

The organism metaphor explains behavior at the organizational level. But most organizational decisions are made by individual people, and those people have their own incentive structures. This is where the concept of local rationality does the most work.

Local rationality is simple: people optimize for their own position, not for the organization's position. This is not the same thing as bounded rationality, which is about cognitive limits — the constraints of time, information, and attention that prevent even well-intentioned people from computing optimal solutions. Local rationality is about incentive structures. A person can have full information, unlimited time, and still make choices that are locally rational and globally damaging — because the local incentive structure points in a different direction than the global one.

Herbert Simon's bounded rationality (from his 1958 work with James March) is worth layering in here, though. Real decision-making involves incomplete information, time pressure, multiple competing objectives, and the weight of prior commitments. People don't optimize — they satisfice. They gather enough information to find an option that clears an acceptable threshold, and then they stop. They're not being lazy. The computational cost of genuine optimization, under real conditions, is prohibitive. This is how cognition works.

Put bounded rationality and local rationality together, and what you get is: most organizational decisions are made by people who are both working with incomplete information and optimizing for something other than the global organizational good. This is not pathology. It's arithmetic.

The examples are everywhere once you start looking:

A critical legacy system — fragile, poorly documented, the source of half your production incidents — sits untouched for two years. Everyone knows it needs a refactor. Nobody touches it. From outside: obviously irrational. From inside: the engineer who takes on the refactor spends months in a risky project with unclear success criteria. If the refactor succeeds, it's invisible — nothing broke, so nothing changed in the eyes of performance review. If it fails, it's highly visible — things broke, and the engineer owns it. The asymmetry of outcomes is clear to every engineer who looks at the problem. Each person makes the locally rational choice to avoid it. The globally irrational outcome — a fragile system nobody maintains — emerges from individually rational decisions, one at a time.

A team agrees to every request they receive. Their backlog is a graveyard of half-finished projects. From outside: pathological prioritization. From inside: the last time this team said no to a request, the requestor escalated to the VP, who overruled the team. The lesson everyone absorbed: saying no costs more than saying yes. The locally rational response to that history is to say yes to everything and manage the consequences later. The dysfunction traces directly to a single escalation pattern, months back, that rewrote the team's operating logic.

Two teams in conflict over ownership of a shared service are put under the same manager in a reorg. Six months later, the conflict persists — now as a territorial dispute within a single org rather than across org boundaries. The underlying cause was ambiguous ownership, different metrics, and historical mistrust. None of those things changed when the reporting lines changed. The reorg felt like action. It was organizational theater. The real problem wasn't in the structure; it was in the incentive design and the unresolved history between the teams.

In each case, the local rationality of each individual decision is obvious once you look at the incentive structure producing it. In each case, the machine-metaphor diagnosis — "malfunctioning component" — points to the wrong fix.

---

## The Political System

The third of Morgan's metaphors is the most uncomfortable for engineers to accept, because it requires treating a phenomenon most engineers find distasteful as a neutral structural feature of organizations.

Organizations are political systems. Not "political" in the derogatory sense — not as a character flaw, not as evidence of dysfunction. Political in the precise sense: they are coalitions of people with different interests, competing for limited resources, with no perfect mechanism for resolving conflicts. That's what politics is. It's not corruption. It's what happens when rational actors who want different things share finite budgets, headcount, and authority.

James March, building on Simon's foundational work, developed the "garbage can model" of organizational decision-making — an empirically-grounded framework for understanding how decisions actually get made. Problems, solutions, participants, and choice opportunities don't line up neatly. They float around organizations somewhat independently and collide semi-randomly. The solution that gets attached to the problem is often not the best solution. It's the solution that was available when the decision opportunity arose, championed by people with enough organizational capital to get it through. This feels wrong to engineers trained on optimization. It is, empirically, how most significant organizational decisions work.

The technically superior proposal that keeps losing isn't losing because decision-makers are stupid. It's losing because it's competing in a political system, and winning in that system requires more than technical merit.

Consider a VP choosing between two architectural proposals. One is technically superior: better performance, lower long-term operational complexity, more maintainable. The other is more familiar — it reuses patterns the VP's most trusted team leads have deep experience with, and it preserves existing investments. The VP chooses the second one. From the outside: obviously wrong, political. From the inside: the VP is accountable for the outcome. If the technically superior but unfamiliar architecture fails, it's the VP's failure — they bet on an unproven approach. If the familiar architecture underperforms, the blame is diffuse — the approach was known and accepted, the failure is about execution, and multiple people share ownership. The VP is risk-managing their career under a realistic model of how accountability is distributed in their organization. This is not stupidity. This is a rational response to the incentive structure they're operating in.

Understanding the political-system metaphor doesn't mean accepting that technically bad decisions should win. It means being clear-eyed about what you're competing in. "This is the right architecture" is a technical argument. Getting it adopted requires a political argument — one that accounts for whose interests are being served, what risks each stakeholder is carrying, and which coalition you need to build to shift the outcome. The engineers who make technically excellent proposals and lose repeatedly are usually missing the political argument. They keep revising the technical case as if the obstacle is technical. It isn't.

Diane Vaughan's post-mortem analysis of the Challenger disaster documents this dynamic at its most costly. The engineers who understood that the O-rings were at risk of failing at low temperatures were technically correct. They made the technical case. The case was evaluated not purely on its technical merits but through organizational processes that had developed their own logic over years of pressure — schedule pressure, budget pressure, the normalization of small deviations from stated safety standards. What she called "normalization of deviance": the organization had adapted to its environment in exactly the way organisms do, accepting small deviations as acceptable until the deviations accumulated to catastrophic failure. Each step along the way was locally rational. The aggregate was disaster. The political system produced an outcome that none of its individual members intended or desired.

The engineers making the case for delaying the launch weren't wrong. They were playing the technical game in a political system they didn't fully account for.

---

## When It Really Is Just Dumb

The local rationality frame is a diagnostic tool. It is not a universal excuse, and using it as one is its own failure mode.

The argument here is not that organizational dysfunction is always structurally produced. Sometimes a decision is just wrong — not locally rational, not a response to environmental pressure, not a sophisticated political calculation. Just a bad call made by someone who should have known better. Over-applying "everyone has their reasons" can produce learned helplessness: the dysfunction must be systemic, so nothing can be done, and the appropriately sophisticated response is to understand it rather than challenge it.

That's not what's being argued. The local rationality frame corrects a specific bias: the engineer's first-instinct diagnosis of "that's just dumb," which ends the analysis and forecloses the more useful questions. The point of asking "what incentive structure produced this behavior?" is not to excuse the behavior. It's to find out where the actual problem is, because if the problem is structural, addressing the symptom doesn't fix it, and more often makes it worse. The team that keeps shipping features nobody uses will keep shipping features nobody uses if you tell them to be more customer-focused without changing what they're measured on. The individual choice to write bad code doesn't recur when the person is counseled; the structural incentive to ship without testing recurs whenever the conditions recur.

The practical heuristic for distinguishing structural dysfunction from individual bad judgment: if the same type of bad decision recurs across different people in different roles — if every person who has held a particular position makes a specific flavor of bad call — it's structural. The pattern is produced by the position, not the person. If it's a one-off, a clear deviation from what most people in similar positions do, it might just be a bad call.

This matters because the fixes are completely different. Structural dysfunction requires changing the incentive structure — the measurement system, the accountability design, the flow of information. Individual bad judgment requires addressing the individual — feedback, coaching, or the harder conversation. Applying the structural fix to an individual problem and the individual fix to a structural problem are both expensive ways to not solve anything.

The Challenger case is again instructive. Vaughan's analysis could have concluded: leadership was under schedule pressure, the organization had normalized risk, therefore no one person is to blame and nothing can be done. That is not what she concluded. She used the structural analysis to identify the specific organizational mechanisms — the launch approval process, the way safety concerns were escalated and evaluated — that allowed locally rational decisions to produce a catastrophic outcome. Understanding the structure gave her the lever for what would need to change. The structural analysis did not excuse anyone; it located the specific failure points that warranted fixing.

The same principle applies to the organizational decisions you'll encounter. Understanding the local rationality of a VP's call to choose the familiar architecture doesn't mean the call was right. It means you now know which specific element of the incentive structure — the asymmetric accountability model, the diffusion of blame for known-approach failures — would need to change for the decision pattern to change. That's actionable. "They chose wrong because they're bad at their jobs" is not.

---

## What Changes Monday

Stop diagnosing organizational decisions the way you'd diagnose a software failure. The machine-metaphor instinct — find the faulty component, fix it, restore correct function — works when you're actually looking at a machine. When you're looking at an organization, it produces analyses that are satisfying to construct and useless to act on. The next time you encounter a decision that seems obviously wrong, before you conclude someone in the room was incompetent, spend five minutes asking what incentive structure would produce that behavior. You will almost always find one.

Start mapping incentives before you walk into cross-functional conversations. Before any significant meeting with stakeholders outside your immediate team, answer these questions: What does success look like for each person in that room, in their current role? What are they being measured on? What risks are they carrying that you might not know about? You don't need complete information to do this — you need thirty minutes and some honest thinking. The proposal that accounts for real constraints in the room will outperform the technically superior proposal that ignores them. This is not about compromising technical quality. It's about making your technical argument in a language the room can actually receive.

When you encounter behavior that looks irrational — the team that won't touch the legacy code, the organization that keeps reorganizing without fixing the underlying problem, the decision process that seems immune to technical argument — ask the organism question before the machine question. What environmental pressure is this behavior adapted to? The answer will often give you the real problem to solve. Fix the measurement system, not the team's attitude. Address the ambiguous ownership, not the reporting structure. Change the accountability design, not the people.

The longer-term shift is more fundamental: update your working model of what an organization is. It is not a machine you can optimize. It is not a computer program you can debug by finding the root cause. It is a coalition of people with different interests, adapting to external pressures, making locally rational decisions under bounded information. This model predicts organizational behavior accurately. The machine model doesn't. Once you've made the switch — and it takes time, and the old model will keep reasserting itself under pressure — the decisions that happen in rooms you weren't in will start making sense. You'll still disagree with many of them. But they'll stop seeming inexplicable. And that's the prerequisite for doing anything useful about them.
