# What Staff Engineers Actually Do

You get the title. The promotion email goes out. People congratulate you. Monday arrives, and you do what you have always done: you write good code, you design careful systems, you review pull requests thoroughly, you make solid architectural decisions within your team's scope. Six months later, a year later, you are still excellent at all of it. And something is wrong.

The work feels the same, but the feedback doesn't quite fit. You're not failing, exactly, but you're not being used the way the title implied. You sit in meetings where the conversation seems to expect something from you that you can't quite identify. You write code that everyone agrees is good and you notice no one seems to care about it the way they used to. The promotion feels like a title change with nothing behind it.

Here is what nobody told you: staff engineering is not senior engineering, amplified. It is a different job. Different scope. Different product. Different success criteria. The engineer who treats the staff title as a reward for continuing to do senior engineering is operating in the wrong role, without knowing it — and most of them never get a clear correction.

This chapter makes the implicit explicit.

---

## The Job Changed When You Weren't Looking

The product of senior engineering is working code and sound local architecture. When a senior engineer has a great quarter, a team ships something that works, the codebase is a little cleaner, a few decisions are better-reasoned than they would have been otherwise. That is a legitimate and valuable output. It is also completely wrong as a measure of staff engineering.

The product of staff engineering is direction, synthesis, and organizational clarity. These are different things entirely. Direction means that multiple teams are moving toward a coherent technical future rather than optimizing locally and diverging quietly. Synthesis means that information trapped in silos gets connected — the security assumption embedded in three separate design documents gets noticed because someone read all three. Organizational clarity means that recurring debates stop recurring because someone wrote down what was decided and why.

None of these outputs show up in a commit log. Only one of them looks like engineering at all to a manager tracking velocity.

The scope model is the cleanest lens here. Ask yourself: what is the largest unit whose success is materially affected by my work? For a strong senior engineer, the honest answer is usually your team. Your architecture choices shape what your team builds. Your code review shapes how your team's engineers develop. Your presence or absence in a critical debugging session shapes whether your team ships on time. This is real leverage. It is also bounded — it stops at the team's edge.

For staff engineering, the honest answer should be multiple teams. The cross-team architectural decision you shaped determines whether three teams can compose their systems cleanly or spend two years fighting seams. The technical strategy document you wrote determines whether five teams make consistent choices about a category of infrastructure problem or make five locally rational decisions that create collective incoherence. The pre-alignment conversation you had with the right person eliminated a month-long debate before it started.

For principal engineering, the honest answer is the organization's technical trajectory — sometimes the company's. The impact horizon lengthens. The scope widens further.

If you hold a staff title and the honest answer to the scope question is still your team, you are doing senior engineering at a staff level. This is not a character flaw. It is almost always a failure of transition — of nobody clearly defining what changed, and of the newly-promoted engineer naturally gravitating toward the thing they know they're good at.

The transition requires a deliberate shift in what you optimize for. You are no longer optimizing your own output. You are the conditions under which other engineers' output gets better or worse.

If you want to grow toward this role before you hold the title, stop waiting for the promotion to start the work. The thinking is what produces the credibility that eventually justifies the title. When you are in a design review, ask: what does this decision imply for teams adjacent to ours? Is there an assumption embedded here that will become someone else's problem in eighteen months? Practice written synthesis of technical context — not code, but documents that capture decisions, connect threads, and eliminate recurring debates. The staff engineer's primary medium is writing. If you have never written an architectural decision record that stood for longer than a quarter, or a technical strategy document that shaped work outside your team, start there. Write something that attempts to synthesize technical context for an audience larger than your team. See how hard it is to do clearly. Ask to be included in cross-team design reviews. Notice what the experienced staff engineers in the room are tracking that the team engineers are not. The skill is not instinct — it is pattern recognition developed through exposure.

---

## What the Role Actually Is

Surveys of how staff engineers actually spend their time consistently find something that surprises people who haven't done the role: a majority of time goes to communication, review, and coordination. Not code. The gap between this reality and the average engineer's mental model of a staff engineer — someone who writes impressive code — is large.

There is a useful framework here, not as a taxonomy but as a diagnostic. Four archetypes describe the range of ways staff engineering manifests in practice, and the most useful question is not "which one am I?" but "which description of the week sounds like the work my organization actually needs from me?"

The Tech Lead is embedded in a team or a closely related cluster of teams. They write a meaningful amount of code. They are the default decision-maker on architecture in that domain. They spend significant time with the senior engineers around them — not just reviewing code, but shaping how those engineers think about problems. The scope extends beyond the immediate codebase into team and product strategy. Of the four archetypes, this one looks most like senior engineering in daily texture. But the scope of judgment has expanded, and so has the responsibility for other engineers' growth.

The Architect operates across teams and is responsible for the technical coherence of a domain across all of them. Less embedded in any single team. More time in cross-team design reviews. The job is ensuring that the pieces fit together across an organization that doesn't naturally coordinate itself. An organization with no Architect tends to produce systems that work within each team and fail at the seams between them.

The Solver goes deep into hard, ambiguous technical problems that the organization does not know how to approach. Often works alone or with a small group for sustained periods. The value is the quality of the investigation and the clarity of what comes out of it. Less about amplifying other engineers' judgment, more about going deep where depth is required. The Solver's archetype is the one most likely to write significant amounts of code in service of a focused investigation.

The Right Hand operates in close partnership with an engineering leader — typically a VP or CTO — as a technical force multiplier for that leader's scope. This is the archetype that can look, from the outside, most like a management role. The distinction matters and is worth stating precisely. A senior staff engineer in this role has no direct reports. They sit in on every major organizational decision in an advisory capacity. They write the technical analysis that shapes the final call. The VP makes the decision; this person makes the VP's decision better. An executive who has not had a Right Hand with genuine technical depth tends to make decisions with a different failure mode than one who has — the organizational authority is present, but the technical grounding of the decisions degrades. The Right Hand's leverage is epistemic: they change what conclusions a decision-maker reaches, not who gets to decide.

Involved in organizational design, hiring strategy, and the hardest cross-cutting technical decisions, this archetype is the most management-adjacent without being management itself. A Right Hand at a growing organization might spend their week on something that doesn't look like engineering from the outside at all, but that is shaping the technical trajectory of the whole organization through the decisions they inform.

Consider a canonical staff week. Monday: a two-hour cross-team architectural review where three teams are making decisions about a shared data model. The staff engineer read all three proposals before arriving, synthesizes the conflicts in real time, and helps the three teams converge on an approach that none of them had proposed independently. Tuesday: three design document reviews. One thorough written review of a proposed service decomposition. One quick async comment on a smaller change. One thirty-minute conversation with a senior engineer whose proposal needs substantial rethinking before it goes broader. Wednesday: a half-day investigation into an incident that exposed a latent architectural flaw — not running the incident response, but doing the technical analysis that determines whether the flaw is local or systemic and what class of fix addresses the root cause. Thursday: a product roadmap meeting, where the staff engineer is the technical voice helping the product side understand what is feasible in what timeframe and what dependencies different sequencing choices will create. Friday: writing. Finishing the investigation writeup. Sketching an RFC on the architectural direction the incident suggested. A weekly technical context note to the engineering leadership.

Note what is not in that week: writing production code. Note what is hard to measure: almost all of it.

---

## The Work That Doesn't Show Up in the Commit Log

There is a well-documented observation about the category of work called glue work: the tasks that make teams function — clarifying requirements, writing documentation, running design reviews, onboarding new engineers, managing cross-team dependencies, synthesizing information across silos — that are systematically invisible in standard engineering metrics because they don't ship code. The observation is that this work exists everywhere, is valuable, and goes unrecognized.

For staff engineers, glue work at organizational scale is a significant portion of the job. But it has to be the right glue work, and this distinction matters.

The specific categories of high-leverage staff work that are invisible in engineering metrics include: synthesis across initiatives, which means reading what three teams are working on separately and seeing the conflict or opportunity they can't see because each team is only looking at its own part of the problem. Pre-alignment conversations, the kind that prevent month-long debates — a ten-minute conversation with the right person before a proposal goes to a wider audience eliminates three weeks of back-and-forth in a meeting that a dozen people are now stuck in. Design reviews that catch systemic issues, where someone with cross-team context notices that a local design choice embeds an assumption that will become a systemic problem at scale. And written direction that eliminates a recurring decision — the architectural decision record that means nobody has to relitigate why the authentication system is built the way it is ever again.

Each of these is invisible in the commit log. Each of them has leverage that exceeds almost anything that shows up in the commit log.

Consider the staff engineer who has not made a significant individual technical contribution to the codebase in eight months. In that time, they helped three senior engineers work through a re-architecture of a critical shared library — each produced better work for the sustained engagement. They caught a systemic security assumption embedded in the way five teams were handling a particular class of request — not by auditing code themselves, but by recognizing the pattern across three separate design documents and connecting the dots. They wrote a technical strategy document that clarified the organization's approach to a category of infrastructure decisions, eliminating a class of recurring debates that had been consuming engineering leadership time quarterly. The resulting output is enormous. None of it has their name on the commit.

This is recognizably and legitimately staff-level work. The question of whether the performance evaluation system captures it is a separate problem — a real one, but separate.

Here is the corollary, and it is important: if you are doing a lot of glue work without the technical direction-setting, you are not operating at the staff level. You are a highly effective organizational contributor, which is valuable and which many engineers underestimate — but it is different. The distinction is technical substance. The staff engineer who catches the systemic security assumption in five design documents is doing staff-level work because they had the technical depth to see what the five teams missed. A non-technical coordinator reading those same documents would not have seen it. The glue work without the technical judgment is coordination. The technical judgment that guides which glue to apply and where is what makes it staff engineering.

The guild system understood this distinction. The medieval master was not the fastest individual worker. The master's job was standards, training, judgment on novel problems, and external representation. But the master's authority derived from craft depth. A master who lost the craft depth became something else — a guild administrator, sometimes useful, always diminished, but not a master in the substantive sense. The title persisted; the role had changed.

---

## Staying Technical Without Getting Stuck in the Code

There is a version of this conversation that treats technical engagement as optional for staff engineers who are "primarily organizational." This is wrong. The floor is real, and crossing below it breaks the role.

A staff engineer who has lost technical credibility is not doing the job. They are doing something adjacent to the job — something that might still be useful in a coordination or process sense — but they have lost the thing that makes staff engineering distinct from organizational management. They are making technical calls they cannot adequately evaluate. They are reviewing design documents with the appearance of technical authority and the reality of intuitions that are two years out of date. When they hold a strong position in an architectural debate, the engineers who have been living inside the system know something is off, and the trust erodes — slowly, then faster.

Imagine a staff engineer who has spent two years doing primarily coordination and organizational work. When asked to weigh in on a significant architectural decision, their read is two years stale. They make a strong recommendation. The senior engineers who live in the system push back with specifics. The staff engineer holds the position on the basis of historical experience. The decision made is suboptimal — not because experience is worthless, but because the experience being applied was calibrated to a system that no longer exists in the form remembered.

This failure mode is slow and quiet. It doesn't look like a mistake when it happens. It looks like a reasonable person making a reasonable call. The damage accumulates across a dozen decisions before it becomes visible.

The opposite failure mode is faster and more obvious: the staff engineer who codes too much. This person is technically excellent and produces work of individual quality that exceeds most of the engineers around them. They are also starving the organizational work. The cross-team design review doesn't happen. The synthesis across initiatives doesn't happen. The pre-alignment conversations don't happen because there is no one with the right combination of context and authority to have them. The senior engineers around them are not growing because the staff engineer keeps solving problems the team should develop the capacity to solve themselves.

There is no precise answer to how much technical engagement is enough. What the role requires is enough hands-on work and close technical engagement to maintain current, accurate intuitions about the systems the organization is building. Not the exact details of every system. Current, accurate intuitions.

The calibration varies by archetype. The Solver has to stay deeply technical — the job is depth. The Architect can maintain credibility through close, engaged design review rather than writing production code, but the reviews have to be substantive enough to catch what a non-technical reviewer would miss. The Right Hand can operate somewhat further from the technical frontier while still maintaining enough engagement to know when organizational decisions have technical implications that require closer examination.

Knuth's career makes a clean illustration of the principle, even if the scale is unusual. He did not have organizational authority. He did not manage people or sit in roadmap meetings. His influence derived from technical work made so legible, so carefully communicated, that it shaped how a field thinks. The architectural RFC written by a staff engineer that becomes the basis for a thousand decisions over three years is operating on the same logic: the work's leverage comes from other people building on it. But that leverage requires that the work be technically sound. An RFC written by someone who has lost technical calibration produces a different kind of legacy.

The minimum bar is this: a staff engineer should be able to read a design document for a system they have not been working on daily and identify whether the assumptions are current and whether the approach is consistent with the organization's technical direction. If they cannot do that reliably, the technical credibility has slipped below the floor. The way back is deliberate immersion: take the next non-trivial technical investigation yourself rather than delegating it.

---

## The Skeptic's Turn: When "Staff Engineer" Is Just a Senior Engineer With Delusions

Name the failure mode honestly: there are staff engineers who have effectively stopped doing technical work and are primarily producing process and meetings. They are influential in a social sense — they have been around long enough to know everyone. They speak with the authority of experience. But their technical judgment is stale. When you act on their guidance, outcomes are not better, and sometimes they are worse. They produce coordination and committees rather than clarity and direction.

This is a real failure. It is not a description of the role. It is a degraded version of the role, and the engineers making the critique "staff engineer is just politics with a technical title" usually have a specific person in mind. When they are talking about that person, they are often correct.

The diagnostic has three questions. Answer honestly.

Is your technical judgment still current and accurate? Not "do you feel confident in your opinions" — that is not the same thing. Ask: when you weighed in on a technical decision in the last six months, did the outcome validate the judgment, or did the engineers who implemented it find that your model of the system was wrong in important ways? If you don't know whether your recommendation held up, that absence of feedback is itself diagnostic. Engineers whose judgment is current tend to stay close enough to the work to find out. Engineers who have drifted tend to stop hearing the outcome.

Are teams producing better outcomes because of your engagement? Not better outcomes than teams without any staff engineer. Better outcomes than they would have produced from you specifically. Name one decision a team made differently because of your input, and describe the outcome. Without a concrete example, "better outcomes" is an easy rationalization — the staff engineer tells themselves yes and moves on. The question is answerable, and if it isn't, that is an answer.

Is there work that could only have happened with you involved? Something that required the specific combination of context, judgment, and organizational position you have — not something that any competent person with access to the same meetings could have done equally well?

If the honest answer to all three is no, the critique applies to you. This is not comfortable, but it is useful. The path forward is not to conclude that staff engineering is pointless. It is to understand what makes the role valuable — technical synthesis, credible direction-setting, making the engineers around you more effective on problems that exceed any one of them — and to start doing those things, which may mean becoming technically uncomfortable again.

Now the other objection: "staff engineer is a made-up title with no consistent meaning." This is factually correct. The title is wildly inconsistent across organizations. At some companies it is one level above senior and given to a substantial fraction of engineers. At others it is rare and designated for the technically elite. At some places it comes with real organizational authority. At others it is pure peer influence.

None of this matters structurally. Every organization of sufficient scale has a need for people who operate at a scope larger than a single team, maintain technical credibility, set direction across teams, and manage the technical coherence of what is being built. In some places, this person is called a staff engineer. In others they are called a principal engineer, an architect, a senior engineer with unusual scope. The title is not the thing. The thing is the thing.

The role exists because organizations face a structural problem that the Bell Labs research labs understood in the mid-twentieth century: the most technically productive people are often the worst candidates for management, and promoting them into management wastes what they are actually good at while producing mediocre leaders. The dual-track structure — a management ladder and a technical ladder — was invented to solve this problem. The Fellow at a research laboratory was not expected to produce papers at high volume. The question was whether the rest of the laboratory was doing better work because of them.

That is still the question. Title or no title.

---

## What Changes Monday

**If you were just promoted to staff**, there is one thing to stop: treating the title as a reward for continuing to do senior engineering. The title was earned through senior engineering. The role requires something different. You already know how to do excellent senior engineering. The new job is to ask, at the end of each week, whether the scope of your impact extended beyond your team. If the honest answer is no three weeks running, you are still doing senior engineering. The fix is to deliberately take on one piece of cross-team work — a design review for a team you don't normally engage with, a synthesis of two initiatives that aren't talking to each other — and see what it surfaces. This is not a soft suggestion. It is the mechanism by which the transition actually happens. The scope diagnostic question is worth asking explicitly: what is the largest unit whose success is materially affected by my work this week? If the answer is still your team, that is the gap to close.

**If you are an established staff engineer**, run the audit. Over the last month: what work happened only because you existed? What would have happened anyway, maybe just more slowly or less well? What would not have happened at all?

The second category is fine — adding quality to work that would have occurred regardless is a real contribution. But if that is all you can name, the leverage is not where it should be. If the third category is empty, or you cannot name a specific example for it, that is the answer. Staff engineering at its best is work in that third category: things that required you specifically, that no one else in the organization was positioned to do, that left the organization in a measurably better place — and that may not appear anywhere in the metrics that track output.

Then run the three-question diagnostic from the Skeptic's Turn on yourself. Not as a one-time exercise. Quarterly. The failure mode it is designed to catch is gradual and self-concealing — the engineer who has drifted does not usually know they have drifted. The questions are uncomfortable by design. If they are not uncomfortable, either you are doing the job well or you are not taking the questions seriously.

The job is real. The scope is real. The measure is hard. That is why most people who have the title are still figuring out the role.
