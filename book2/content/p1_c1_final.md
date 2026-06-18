# Nobody Told You This Was the Job

You spent three weeks on the architectural proposal. Database schema, migration path, scaling analysis, a section on failure modes, an appendix on rollback strategy. You were thorough in the way you'd learned to be thorough — covering your bases technically, anticipating objections, modeling the edge cases. The proposal was, by any reasonable measure, correct.

The decision went a different direction.

Not because someone had a better technical argument. Not because you made an error in the analysis. It went a different direction because the VP sponsoring the alternative had more organizational capital than you understood. Because the migration timeline conflicted with a sales commitment nobody had told you about. Because two of the people who said LGTM in the design doc had significant reservations they didn't feel safe raising. Because the conversation that mattered happened in a room you weren't in, before the meeting you were in.

You walked out thinking the decision was wrong. Maybe it was. But you also didn't fully understand what game was being played. That's what this chapter is about.

The skills that got you to this level — clean architecture, fast debugging, reliable delivery, the ability to reason about systems under pressure — are still necessary. They're just not sufficient anymore. The problems that multiply on your desk past a certain point are organizational: misaligned incentives, communication structures that distort signal, decisions made for reasons that have nothing to do with technical merit. Nobody explains this transition. Most engineers discover it by running into it hard.

---

## What the Promotion Was Actually For

There's a structural dishonesty built into how engineering organizations promote people, and most engineers don't notice it until they've been on the wrong side of it.

When you're promoted to senior engineer or tech lead, the criteria are necessarily backward-looking. They reflect what you did well as a junior or mid-level engineer. You shipped reliably. Your code was clean. Your estimates were accurate enough. You debugged hairy problems and didn't create new ones. The evidence for promotion accumulated over months or years, and it was technical evidence.

The job that comes after the promotion is measuring something else entirely.

The performance review that lands eighteen months in — the first one at the new level — will have feedback you didn't expect. "Needs to develop stronger cross-team relationships." "Could do more to raise visibility of the team's work." "Decisions sometimes bypass stakeholders." None of these were in the criteria you were promoted against. Nobody told you the criteria had changed. Your first interpretation is probably that the organization is being inconsistent.

It is, in a narrow sense. But the inconsistency has a structure, and it's predictable once you see it. The skills that make someone promotable from mid-level to senior are almost entirely about individual technical output. The skills that make someone effective at the senior level are increasingly about organizational influence — shaping which problems get solved, how they get framed, how a team functions, how technical work connects to the priorities of the people who fund it. The input-output relationship changes completely.

Laurence Peter observed in 1969 that people tend to be promoted until they reach the level of their incompetence. In engineering, this has a specific and non-comedic form: engineers are promoted for technical output, then placed in roles that primarily require organizational navigation. The incompetence, when it arrives, isn't personal. It's the absence of training in a different set of skills. Nobody told them the job had changed.

Consider the excellent individual contributor who gets promoted to tech lead. For the first six months, they do exactly what they'd always done, but with a new title. They produce most of the significant code. They take pride in this — it's evidence they can "still do the job." Meanwhile, the things the team actually needs from a tech lead are not getting done. Nobody is managing the cross-team dependency that's creating schedule risk. The roadmap document is out of date. The two junior engineers on the team are floundering without guidance. The product manager doesn't know what's shipping next quarter. The tech lead is performing their old job excellently and their new job poorly — without knowing the new job exists.

This isn't a failure of character. It's a failure of legibility. The compiler tells you when you're wrong. Nothing tells you that the cross-team dependency is becoming a risk until it becomes a crisis. The tech lead keeps measuring themselves by the metric that got them promoted, because no one has given them a different metric.

There's also a subtler dimension to this discontinuity: the feedback loop changes completely. As an individual contributor, feedback is fast and relatively unambiguous. You write a function and the tests pass or they don't. You fix a bug and the system works or it doesn't. The gap between action and signal is hours or days. At the senior and tech lead level, the feedback loop stretches to months. You set a technical direction and you won't know for two quarters whether it was the right one. You mentor a junior engineer and the results may not be visible for a year. You make a call to defer a refactor and the downstream costs won't be legible until much later.

Engineers who were excellent at processing fast feedback often struggle with this shift. Not because they're less capable, but because the skill they honed — rapid iteration based on clear signal — becomes less applicable. The competence that made them exceptional at one level doesn't transfer automatically to the next. This isn't Dunning-Kruger exactly, but it rhymes: the experience of being excellent at one thing and suddenly discovering you're a beginner at an adjacent thing, with a feedback loop too long to tell you where you're going wrong in real time.

---

## The New Problems Don't Look Like Problems

The organizational problems that land on a senior engineer's desk don't arrive labeled. They don't announce themselves the way technical problems do. A failing test is clearly a problem. A compiler error is clearly a problem. An ambiguous stakeholder relationship, a misaligned roadmap, a cross-team dependency that nobody has explicitly acknowledged — these look like friction, like overhead before the real work, like problems that will resolve themselves or that someone else is handling.

They are the real work.

Frederick Brooks wrote about this fifty years ago in a context that still applies. The managers in his stories didn't see coordination overhead as the problem — they saw the programming schedule as the problem. They'd add people to address the schedule and be surprised when it slipped further. The overhead was invisible until it was catastrophic, because it didn't look like a problem. It looked like the normal condition of running a large project.

The organizational equivalents are just as invisible, and they accumulate in the same way. The tech lead who isn't doing cross-team dependency management won't notice the problem for weeks. The engineer who interprets "LGTM" comments as genuine consensus will discover the hidden reservations two sprints in. The senior engineer who doesn't understand why a proposal isn't gaining traction will revise the technical argument three times before realizing the obstacle was never technical.

That last case deserves unpacking because it's so common. A tech lead runs what they believe is a consensus-building process. They circulate a design document. They gather async comments. Several people say LGTM or leave no comment at all. The proposal is ratified in a brief review meeting. Two sprints later, they discover that two of the engineers who signed off actually had significant reservations. They didn't raise them because the culture didn't feel safe for that, or because they assumed someone more senior would surface them, or because they were optimistic about working around the problems once development began. The "consensus" was performative. The tech lead never learned how to read the difference.

The telling detail: the tech lead in this scenario did everything "right" by the process model they were using. They circulated a doc. They asked for feedback. They held a review. What they didn't do was create the conditions where honest disagreement could surface. That's an organizational problem, not a technical one. And it's invisible until it becomes a crisis.

Karl Weick's work on organizational behavior offers a useful frame here. Organizations are not rational machines that process inputs into optimal outputs. They're collections of people constructing coherent narratives about ambiguous situations — making sense of complexity in real time, with incomplete information, under competing pressures. When an organization makes a decision that looks irrational from a technical perspective, the engineer's first instinct is: "these people are wrong." The more useful question is: given the information they have, the incentives they're operating under, and the history they're carrying, what are they doing that's locally rational?

That question almost always has an answer. And the answer is almost always more useful than the original verdict of irrationality.

When you encounter something on your desk that doesn't have a spec and can't be fixed with a pull request, ask whether you're looking at an organizational problem wearing a technical disguise. That recognition — catching the moment when the problem has changed type — is the first diagnostic skill this book is trying to build.

---

## The Rule Change Nobody Announced

Here is the specific transition that's hardest to see clearly from the inside.

As an individual contributor, you create value directly through technical output. You write code, design systems, fix bugs. The connection between what you do and what the organization gets is short and relatively legible. You're measured on what you produce.

Past a certain level — different organizations draw this line in different places, but most draw it somewhere around senior engineer or tech lead — you start to create value primarily through organizational influence. You shape which problems get solved. You define how problems get framed. Your architectural decisions influence what's possible for teams you'll never meet. The technical work you do directly matters less than the technical environment you create for others.

Herbert Simon described what he called "satisficing" — the tendency of organizations to seek solutions that are good enough given the constraints of time, information, and cognitive load, rather than optimal solutions. This is disorienting for engineers trained to find optimal solutions. The organization that keeps a known-flawed system because migration cost is too high and the current system "works well enough" is not making a technical error. It's satisficing in a perfectly rational way, given its context.

Consider: a team inherits a system with a well-understood architectural flaw. The correct fix is obvious to anyone who looks at it. The team proposes a rewrite. The proposal is technically unimpeachable. It gets deprioritized — not because anyone disagrees with the diagnosis, but because the business unit that relies on the system is in the middle of a product push, the relevant VP doesn't want to touch working infrastructure during a critical quarter, and the memory of a failed migration two years earlier is still fresh. This is the sensemaking lens in practice: the VP isn't blocking good engineering. They're constructing a coherent story about risk, given the context they're in. The "obviously right" technical decision doesn't get made because the proposal didn't account for that context.

The transition that nobody announces is this: your job is no longer to find the technically correct answer in isolation. Your job is to find the technically sound answer that can actually be implemented given the organizational environment you're operating in. These are often the same thing. When they're not, pretending they are doesn't help.

Proposals that don't account for organizational satisficing keep losing to proposals that do. A technically superior migration plan that ignores the political cost of disrupting a critical-quarter product push will lose to a technically inferior plan that acknowledges the timing constraint. Not because the decision-makers are irrational. Because the constraints are real and the proposal that treats them as real is more useful than one that pretends they aren't.

---

## The Skeptic's Turn: "Just Do the Technical Work"

The strongest objection to everything in this chapter is a reasonable one, and you're probably already formulating it.

"I'm an engineer. My job is engineering. If organizations need someone to navigate internal politics, that's what managers are for. The whole point of having a management layer is so that technical people can focus on technical work. If I spend time on organizational navigation, I'm not doing my job — I'm doing someone else's job."

This is not a stupid argument. It reflects a genuine preference that many excellent engineers have — a preference for work that has clear answers, where rigor pays off directly, where you can be objectively right. And there's a version of it that's just true: you shouldn't be doing your manager's job. The management layer exists for a reason.

But the argument rests on an assumption that is rarely true: that someone else is managing the organizational dynamics well, so you don't have to. In most organizations, nobody is doing this particularly well. The manager who's supposed to be your buffer against organizational complexity is themselves managing up, managing across, dealing with their own set of ambiguous constraints. The stack of organizational dysfunction doesn't get handled on your behalf — it accumulates until it becomes a crisis that lands on everyone's desk at once.

The more damaging technical decisions in most organizations are not made by executives ignoring technical input. They're made by engineers who didn't understand the organizational context their technical decisions would be implemented in. The engineer who specifies a migration path without understanding the sales commitment that makes the timeline impossible. The tech lead who designs for scale without knowing the organization would rather ship in three months and refactor later. The architect who produces the theoretically correct answer to a question the organization wasn't actually asking.

The "stay technical" argument also conflates two different things: understanding organizational context and managing people. This book is not an argument for engineers becoming managers. An engineer can stay deeply technical and still understand incentive structures. You can focus on architecture and still know how decisions get made. These aren't opposed.

There's also a more sophisticated version of the objection worth addressing directly: "Fine — but the answer is to fix the broken organizations, not to ask individuals to adapt to dysfunction. If incentive structures are misaligned, that's a systemic problem. Training people to navigate the pathology just enables it."

This is true and this book doesn't disagree with it. Organizations are often structurally broken in exactly the ways described. The goal is not to teach engineers to make peace with dysfunction. The goal is legibility as a precondition for leverage. You cannot change a system you don't understand. The engineer who accurately maps the incentive structure causing a bad pattern is in a position to do something about it. The engineer who attributes the same pattern to stupidity or malice is not. Understanding organizational dynamics doesn't mean accepting them — it means having the diagnosis you need before you prescribe the treatment.

Dijkstra wrote extensively about the separation between what computers do and what the organizations around computers do as the central unsolved problem of computing. He considered organizational dysfunction a first-class technical problem, not a separate concern. The systems you build will outlive the technical decisions that went into them. What kills most systems isn't bad code — it's misaligned organizational incentives that prevent the maintenance the code needs, or communication failures that let known problems accumulate, or decision-making processes that optimize for the wrong horizon. The organizational environment is part of the technical problem.

---

## What This Book Is

To be direct about scope, because both the scope and the limits matter.

This is not a management book. It doesn't argue that you should seek people leadership or develop what's usually called a "softer" skill set. The skills covered here aren't soft — they're harder than most technical skills in the sense that feedback loops are longer, signal is noisier, and the tools for developing expertise are less mature. They happen to involve humans more directly than CPUs.

The topics ahead — incentives, organizational structure, decision-making, communication, the economics of technical work, leadership without formal authority — are not peripheral to the engineering job at senior levels. They are the job. The technical foundation remains necessary. The architectural skill, the debugging instinct, the delivery discipline — none of that goes away. But the problems that determine your effectiveness and your influence, past a certain threshold, are in the organizational domain.

Project failure studies spanning several decades find that technical factors account for a minority of failures. Organizational and communication failures dominate. Research on what happens to high-performing individual contributors after promotion consistently finds that the ones who fail, fail on interpersonal and organizational dimensions — not technical ones. They applied technical-style reasoning to organizational problems. They treated ambiguous situations as optimization problems. They tried to resolve political dynamics with architectural diagrams. The failure mode is remarkably consistent, and the prevention is not a mystery: recognize that a different set of skills is required and develop them deliberately rather than by accident.

The rest of this book is the deliberate version.

---

## What Changes Monday

Stop treating organizational problems as overhead before the real work. The next time you're frustrated by a decision that went a direction you didn't expect, or a proposal that isn't gaining traction, or a piece of work that got deprioritized despite being technically correct — resist the first instinct, which is to double down on the technical argument. That instinct is often wrong, and doubling down rarely helps.

Instead, diagnose before you revise. Start with the person whose buy-in you don't have. What would they lose if this proposal succeeded? What timing constraints are they working with that you might not know about? What organizational memory — a past failure, a prior commitment — is shaping how they're reading your proposal? Those answers are almost always findable before the next meeting, not after. A proposal that accounts for real constraints will outperform a technically superior proposal that ignores them.

Start noticing when the problem in front of you is organizational rather than technical, and treating that recognition as information rather than frustration. Organizational problems are real problems. They have structure and they respond to analysis — just not the same analysis you apply to a system design. When something doesn't have a spec and can't be fixed with a pull request, you're probably looking at a problem in the human system, not the technical one. Name it that way, to yourself first.

The longer-term shift: make it a practice, when a technical initiative stalls, to map the organizational context before revising the technical substance. What are the incentives of the key stakeholders? What are the constraints — budget, timing, risk tolerance — that weren't in the brief? What's the political history that's making people cautious? Engineers who do this consistently stop being surprised by the decisions that happen in rooms they weren't in. They start being in the rooms, or shaping the context before the rooms convene.

Nobody told you this was the job. The rest of the book is about doing it well.
