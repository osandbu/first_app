# Influence Without Authority Is a Skill

---

There is an engineer at most organizations who is almost always right. His proposals are technically rigorous. His documentation is thorough. His analysis anticipates objections. And year after year, the decisions go another way.

He is not failing because his ideas are bad. He is failing because he is operating on a theory of organizational persuasion that does not match how organizations actually work. The theory is simple: if you present a correct analysis clearly, the correct decision will follow. It is a reasonable theory. It is wrong.

This chapter is about what replaces it.

Influence without formal authority is not a personality trait. It is not something you either have or don't have. It is a set of learnable skills grounded in how human beings actually process information, how organizations actually make decisions, and how social capital actually accumulates. The engineers who consistently get important things done — migrations approved, architectural changes adopted, cross-team alignment achieved — have learned these skills, usually through expensive trial and error. This chapter tries to shortcut some of that expense.

---

## Section 1 — Why Technical Correctness Is Necessary But Not Sufficient

The engineer presenting conclusions to a room full of people who haven't participated in the reasoning that generated those conclusions is asking those people to do something psychologically difficult: accept, on trust, the output of a process they didn't witness. That is a large ask, and it gets larger as the stakes increase.

This is not because people are irrational. It is because, from a stakeholder's perspective, accepting a conclusion without understanding the reasoning is genuinely risky. If the reasoning is wrong, they don't know it. If the proposal has costs that weren't surfaced, they can't see them. If there are alternatives that weren't considered, they have no way to raise them. The correct response to being handed a conclusion without access to the reasoning is skepticism. This is not organizational dysfunction. It is sound epistemic practice.

The failure mode is predictable: the technically correct engineer responds to rejection by making the analysis more thorough. The next presentation has more data, more detail, more rigor. The proposals keep losing. The engineer concludes that the organization is irrational, politically captured, or simply not smart enough to understand the work. This is almost never the correct diagnosis.

Many engineers feel genuine discomfort with the idea of "organizational politics" — the maneuvering, the positioning, the cultivation of relationships before they're needed. The discomfort is worth examining rather than dismissing. It points at something real: there is a difference between making good ideas accessible and obscuring bad ones. There is a difference between understanding what a stakeholder actually cares about and exploiting their biases. These distinctions matter. The engineer who is worried about becoming political is, in part, worried about the right thing.

But the worry often leads to a false binary: either pure technical argument on its merits, or manipulation. The binary doesn't hold. Making your reasoning visible so others can engage with it is not manipulation — it is the opposite of manipulation. Understanding what a colleague cares about so you can address their actual concerns is not lobbying — it is responsive design applied to proposals. The discomfort with politics is worth keeping; the refusal to develop influence as a skill is not.

---

## Section 2 — Read the Room Before You Walk Into It

Before any significant proposal, most engineers know roughly who the decision-maker is and spend most of their preparation time optimizing for that person. This is a mistake, not because the decision-maker doesn't matter, but because it ignores everyone else who affects the outcome.

Stakeholder mapping is a simple tool with significant practical returns. Map the people who affect the decision on two axes: power (their ability to influence or block the outcome) and interest (how much they actually care about this particular decision). The resulting quadrants suggest different strategies:

High power, high interest: these are the people you know about. Engage them directly. Address their concerns substantively. They will participate in the decision whether you engage them or not; the question is whether they participate informed or uninformed.

Low power, high interest: often overlooked, frequently useful. These are people who care deeply and can become coalition members. They may not have formal authority, but they know things and they talk to people.

Low power, low interest: minimal investment. Keep them informed, don't overload them.

High power, low interest: this is where most proposals die quietly. The high-power, low-interest stakeholder is not thinking hard about your proposal. They have their own priorities. They will form an opinion based on a brief summary, a first impression, or — most often — what someone they trust told them. If that someone they trust has concerns about your proposal, you have a problem you don't know about until it's too late.

The practical error is optimizing entirely for the formal decision-maker while ignoring the director three levels up who can say "this doesn't feel right" in passing and effectively end the discussion. That director may have five minutes of attention available for your migration proposal. If those five minutes happen after an objection has been planted, and before you've had a chance to explain, you've lost a decision you didn't know was being made.

This is not exotic political maneuvering. It is basic situation awareness applied to the organizational environment. You wouldn't deploy a system without understanding the dependencies. Don't propose a change without understanding the human network it will travel through.

Mapping stakeholders explicitly does something else: it forces you to think about what each person actually cares about, not what you assume they care about. The manager who appears resistant to your database migration may be resistant to the performance regression window, which is a different problem than being resistant to the migration. The team lead who isn't engaged may have a Q3 deadline that makes any three-month commitment impossible right now. These are solvable problems, if you know they're the problems.

---

## Section 3 — The Pre-Alignment Conversation

The single most effective technique for getting complex proposals approved is also the one most engineers skip: the private one-on-one conversation with key stakeholders before the formal meeting.

This is not about lobbying. The distinction matters. Lobbying, in the pejorative sense, means using influence to advance a fixed position regardless of its merits. Pre-alignment means having conversations that let you understand concerns before they become public objections — and then modifying your proposal to address what you learn. The proposal that emerges from a round of pre-alignment conversations is, in most cases, a better proposal. Not just a better-received proposal. A better one.

Here is what this looks like in practice. A staff engineer needs approval for a cross-team database migration affecting four teams. The migration requires a three-month engineering commitment from two of them and will generate temporary performance regressions during the transition. She does not schedule a "migration proposal meeting." Instead, over three weeks, she has six individual conversations: with each team lead, with the principal engineer who built the current system, with the director who controls headcount for two of the teams.

In each conversation, she explains what she's considering and asks what concerns would need to be addressed for this to work. Team A worries about the regression window affecting a customer SLA. Team B has a Q3 deadline that makes any large commitment impossible before October. The engineer who built the current system has a personal investment in the existing design that needs to be acknowledged, not steamrolled.

She modifies the proposal: a monitoring plan with rollback criteria for team A, a phased schedule that begins after team B's Q3 deadline, explicit acknowledgment of the prior design's value and how the new system builds on it for the engineer who built it.

When the formal meeting happens, it runs twenty minutes. The concerns that might have derailed it have already been addressed. The formal meeting is ratification, not deliberation.

This is not unusual. It is how most significant organizational decisions actually get made by people who are good at making them. The formal meeting is often the last step, not the main event. The work happened before anyone walked into the room.

Two things make the pre-alignment conversation different from its corrupted version. First: the goal is to understand concerns and modify the proposal accordingly, not to secure commitment to an unchanged proposal. If someone raises a concern you can't address, you need to know that before the meeting, not during it. Second: the conversations are transparent about what's happening. You're not gathering intelligence to neutralize opposition. You're doing the work of making a proposal responsive to the organization it has to work within.

The pre-alignment conversation also reduces the social cost of disagreement. A stakeholder who raises a concern in a private conversation can be accommodated without losing face. The same person raising the same concern in a meeting of ten people is in a different social dynamic — now their objection is public, positions harden, and resolution requires someone to be visibly wrong. Pre-alignment avoids that dynamic by design.

Cialdini's research on commitment and consistency explains part of why this works: once a person has agreed that a problem is real and that a certain approach to solving it is reasonable, they are more likely to maintain consistency with that position later. Getting agreement on the problem before proposing the solution is not just courteous — it is mechanically effective. The stakeholder who walks into the formal meeting having already agreed that the current database architecture is a real constraint is a different participant than the one encountering the proposal cold.

---

## Section 4 — Make Your Reasoning Visible

The problem with presenting conclusions is that it puts the receiver in a passive position: accept or reject a package they can't inspect. The alternative is to present reasoning in a form that others can actually engage with — follow the logic, identify where they disagree, raise concerns about specific steps rather than the whole proposal.

There is a discipline worth adopting for any significant proposal: before designing the solution, write the future state. Describe, in concrete terms, what the world looks like after the change is successfully made. What is different about the user's experience, the team's operations, the system's behavior? Force yourself to write this before writing a word about implementation. Then work backwards from that future state to what has to be true to get there.

This discipline does two things. First, it forces you to be precise about what problem you're solving and what success looks like — and often reveals that you haven't been precise enough. Second, it creates a document that anchors the conversation on shared problem definition before anyone can argue about implementation. A reviewer who disagrees with the future-state description is raising a real concern about goals. A reviewer who disagrees with an implementation detail while agreeing on the future state is in a much more tractable conversation.

Framing matters at the level of individual word choice, not just document structure. Kahneman and Tversky's prospect theory established that people evaluate proposals relative to reference points, and they weight losses approximately twice as heavily as equivalent gains. A proposal framed as "here is what we gain by migrating" is processed differently than the same proposal framed as "here is what we're losing by staying on the current system." The content is identical. The psychological effect is not. Using loss frames deliberately — "the current architecture is costing us X per quarter in on-call time, Y weeks per year in migration blockers" — is not manipulation. It is presenting accurate information in a form that matches how humans actually assess it.

Cialdini's pre-suasion research adds a related observation: the moment before a request shapes how the request is received. In documented studies, framing a request with a question about the respondent's helpfulness changed agreement rates from 29% to 77%. The setup conditions the response. In organizational contexts, this means: open with the shared problem before proposing the solution. Ask whether the problem you're describing matches their experience. Secure agreement on the problem definition before you've proposed anything about implementation.

There is a specific technique for one of the most common organizational failure modes — the decision that keeps drifting. Cross-functional decisions often stall not because anyone objects to them but because no one has made deciding a priority. The cost of continuing to defer is diffuse and invisible; the cost of the decision itself is concrete and local. This asymmetry produces indefinite delay.

The response is to make the cost of deferral explicit. One approach: write a brief, specific communication identifying the decision to be made, the options you see, your recommendation with the reasoning behind it, and a date by which you need a response. Not a demand — an honest statement that you cannot proceed without resolution, that you've done the work of narrowing the options, and that delay has a cost you can name. This converts organizational drift into an explicit decision, which is much easier to resolve.

This technique works because it lowers the activation energy for the decision-maker. You're not asking them to do the analysis. You're asking them to react to yours. You've done the hardest part. And you've made clear that "no response" is now a visible choice with a visible cost, not just more drift.

---

## Section 5 — Build the Network Before You Need It

Ronald Burt's empirical work on organizational networks produced a finding that senior engineers should take seriously: the people whose networks bridge disconnected groups — who sit in the gaps, or "structural holes," between clusters — have disproportionate access to diverse information and disproportionate influence. This is not a theory about how networks should work. It is a finding about how they actually do.

Within any cluster — a team, a department, a functional group — information is relatively homogeneous. Members share context, assumptions, vocabulary. The person who bridges two clusters sees both sides. They know what the infrastructure team is worried about and what the product team is trying to ship. They can carry information that neither group has on its own, translate concerns that neither group can quite articulate to the other, and identify where a conflict is based on miscommunication versus genuine disagreement.

Burt's study of managers at a large electronics firm found that this bridging position was independently predictive of compensation, performance evaluations, and promotion rates — independent of technical skill and seniority. The effect was not small. Network position matters.

The practical implication for engineers: the person who understands the concerns of the infrastructure team and the product team is not just a good communicator. They hold a structurally advantaged position. When conflicts arise, they become the natural mediator — not because they have authority, but because they have information and credibility in both groups. They get pulled into decisions earlier than their formal seniority might suggest, because their presence reduces coordination cost.

This position is not created by organizational design. It is created by the engineer who, out of genuine curiosity about what adjacent teams are working on, builds relationships across team boundaries over months and years. The key word is "genuine." The engineer who treats cross-team relationships as a resource to be cultivated instrumentally when a proposal needs support will be recognized as such. The engineer who is actually curious about what the platform team is solving, who shows up to help when it's useful, who shares context without keeping score — that person accumulates a form of social capital that is available when they need it.

Cohen and Bradford's organizational currencies model gives a useful vocabulary here. Organizations circulate non-monetary currencies: information, organizational access, visibility, recognition, the removal of obstacles, a sense that someone is on your side. These currencies flow through relationships. The engineer who has been consistently helpful — who gave someone useful context before they needed to ask for it, who took time to explain a system she understood to someone who didn't, who flagged a dependency that would have cost another team weeks to discover — has accumulated currency that translates, eventually, to cooperation.

The compounding value of this is easy to underestimate and easy to observe in retrospect. The engineer who asks for something from a colleague she's never engaged with is in a worse position than the one who has been a regular, useful presence in that colleague's professional life. This is not a cynical observation. It is just how trust accumulates among human beings, in and out of organizations.

Consider an engineer on a platform team in persistent tension with several product teams. She makes a practice of understanding what the product teams are actually trying to accomplish, not just what they're asking for. Over time, she becomes the person on the platform team who can describe product team constraints accurately, and the person in product conversations who can describe platform team priorities accurately. When conflicts arise, she is the natural translator. She gets included in decisions before they're finalized because her inclusion reduces friction. Her influence is not the product of organizational maneuvering. It is the product of sustained, genuine attention to what other people are trying to do.

The Linux kernel's governance structure offers a useful limit case. Linus Torvalds has no organizational authority over the thousands of contributors whose work shapes the kernel. He cannot promote anyone, set anyone's compensation, or compel anyone to do anything — everyone can fork. His influence rests on accumulated technical credibility, made visible through decades of detailed code review, and on a governance structure that requires demonstrated implementation rather than formal committee approval. The BDFL model works because the reasoning is always visible. When Torvalds objects to something, the objection carries weight because the track record is public. The lesson for staff engineers is not "be a benevolent dictator." It is that technical credibility is a resource, and its visibility is what makes it useful.

---

## The Skeptic's Turn — Is This Just Politics?

The serious objection deserves a serious answer, not dismissal. The concern: organizations that reward persuasion over substance will systematically misallocate resources. The engineer who is right but navigates poorly loses to the one who is wrong but builds coalitions effectively. In those organizations, influence skills make things worse, not better, because they let bad ideas survive.

This objection is correct about a real failure mode. Some organizations do reward persuasion over substance. When that is consistently true, it produces bad outcomes. The objection is pointing at something real.

The response has two parts.

First: the techniques described in this chapter are not persuasion over substance. They are substance delivered in a form that others can actually engage with. The pre-alignment conversation surfaces concerns so the proposal can be improved. The visible reasoning document lets reviewers engage with the logic rather than being asked to accept a conclusion. The stakeholder map identifies concerns so they can be addressed. These techniques make good proposals more likely to succeed — but they also make bad proposals harder to sustain, because they require exposing the reasoning to scrutiny. A bad idea that survives pre-alignment conversations survived because no one in those conversations could identify what was wrong with it. A bad idea that fails because the reasoning was visible failed for the right reasons.

Second: the "just be right" model does not exist in any organization of real complexity. Decisions in organizations involve multiple stakeholders with different information, different incentives, and different definitions of what the right outcome is. The belief that technical correctness is sufficient is itself a bias — the engineer's version of assuming that the rational actor model describes how human decisions actually get made. In organizations of more than a few dozen people, the ability to build consensus around good ideas is not a corruption of the decision-making process. It is the process.

What to do when the organization actually, consistently rewards persuasion over substance — when bad ideas backed by influential people win reliably over good ideas backed by evidence? That is a real problem. The response depends on how pervasive it is. If it's localized to specific decision-makers or teams, the network-building approach helps: the engineer with relationships across the organization has more paths through which good reasoning can reach the right people. If it's systemic — if the culture reliably selects for persuaders over practitioners — that is an organizational health problem that eventually produces poor outcomes, and it is worth naming clearly. There are organizations where the right response to consistent, systemic misallocation is to decide how long you're willing to stay.

The TCP/IP history is instructive on the opposite dynamic: what good influence at scale actually looks like. By the mid-1980s, the official answer to computer network interoperability was OSI — backed by government mandates in multiple countries, formal adoption by standards bodies, plans for mandatory procurement. TCP/IP had none of that. What it had was running code, a working internet, and a governance philosophy articulated by MIT's David Clark at the 1992 IETF meeting: "We reject kings, presidents, and voting. We believe in rough consensus and running code." The IETF required two independent working implementations before a protocol could achieve Draft Standard status. The standards had to prove themselves in software before they were certified.

By 1995, OSI implementations had collapsed to marginal status and TCP/IP dominated. No army ordered this. Engineers, universities, and commercial organizations adopted TCP/IP because it ran — because the influence of the IETF community was built on demonstrated utility rather than formal mandate. The formal authority lost to demonstrated value and an engineering community that had built something people actually used.

This is what legitimate technical influence looks like. Not lobbying. Not coalition-building in the service of ideas that can't demonstrate their value. Demonstrated utility, made visible, governed by rough consensus, defended by practitioners willing to show their work.

---

## What Changes Monday

Before your next significant proposal, stop and do something most engineers skip: map the stakeholders explicitly. Not in your head. On paper. Who are the people who affect this decision? For each one: how much power do they have over the outcome, and how much do they currently care?

Look specifically for the high-power, low-interest stakeholder. That person can kill your proposal without engaging with it. If you don't know what they care about, you don't know what might cause them to do that. You need to know before the formal meeting, not during it.

Have the pre-alignment conversations. Set up individual meetings with every high-power stakeholder before you schedule a formal decision meeting. Ask what concerns would need to be addressed for this to make sense. Listen to the answer. If the concerns reveal problems with your proposal, that is useful information — not a setback. Modify the proposal to address what you learn. The proposal that survives a round of honest conversations with the people who have to live with it is, reliably, a better proposal.

Before you propose a solution, secure agreement on the problem. Write the future state first — what the world looks like if this succeeds — and get alignment on that before you present a single implementation detail. This sounds like extra work. It is extra work. It consistently reduces the total time from proposal to decision.

Stop presenting conclusions to rooms full of people who haven't participated in the reasoning that generated them. Make the reasoning visible. Put it in a document people can read before the meeting. Let them engage with the logic, not just the conclusion. Welcome the challenge to specific steps — that challenge is information, and it is much more useful before you've committed to an approach than after.

For the decision that won't get made: write the specific email. Identify the decision, the options, your recommendation, the reasoning, and the date by which you need a response. Name the cost of continued deferral. This is not demanding authority you don't have. It is doing the organizational work of converting drift into an explicit choice.

The longer-term shift: treat relationships across team boundaries as organizational infrastructure worth investing in consistently, not only when you need something. Be genuinely curious about what adjacent teams are working on and why. Help when you can, without keeping score. Over time, this creates the network that makes everything else in this chapter easier — not as a political resource, but as the natural byproduct of being someone who pays attention to what others are trying to do.

The engineer who loses decisions despite being right is usually right about the technical question and wrong about the organizational one. The organizational question is not "is this the best solution?" The organizational question is "can I create the conditions under which this gets decided correctly?" That second question is learnable. It starts Monday.

---

*Sources and further reading: David Clark's "rough consensus and running code" remarks are from the 24th IETF meeting, Cambridge, Massachusetts, July 1992. Ronald Burt's structural holes research is developed in Brokerage and Closure (Oxford University Press, 2005). Cohen and Bradford's organizational currencies framework appears in Influence Without Authority, third edition (Wiley, 2017). Cialdini's pre-suasion research, including the 29%/77% agreement rate study, is from Pre-Suasion (Simon & Schuster, 2016). Kahneman and Tversky's prospect theory, including the asymmetric weighting of losses and gains, was first published in Econometrica in 1979.*
