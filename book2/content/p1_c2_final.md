# The Org Chart Is a Lie

The approval came through on a Thursday afternoon. The engineer had done everything right: drafted the proposal, walked their manager through the technical case, answered questions, incorporated feedback, got the sign-off in writing. The path was clear.

By Monday, the initiative was dead.

The infrastructure team had problems with the deployment model. Security raised a review gap that would take two months to close. The platform team pointed out a conflict with an architectural decision made six months earlier — a decision that was apparently still alive, still binding, and not documented anywhere the engineer had thought to look. Nobody was rude about it. Nobody was obstructing for bad reasons. The work simply wasn't going to happen, and it wasn't going to happen because the person who said yes didn't control most of the terrain between yes and done.

The engineer had permission. What they didn't have was momentum. These are different things.

---

## The Map and the Territory

An org chart captures specific things accurately. It tells you who your manager is. It tells you who has formal authority over what budget, who signs off on headcount, who can make certain categories of commitment on behalf of the organization. These are not trivial — legal accountability lives there, and the escalation path when things go genuinely wrong matters. The org chart is the right map for specific, narrow questions.

It is a bad map for almost everything else.

What the org chart cannot capture: who people actually trust for technical judgment. Whose opinion carries weight before a decision enters a formal process. Which teams have learned to route around each other because of a conflict two years ago that nobody resolved. Where the informal review gates are — the conversations that have to happen before any proposal survives the formal review. Who acts as the translator between groups that don't share vocabulary. Where information moves freely versus where it clots.

Chester Barnard noticed this in 1938. His book on executive management — still worth reading — drew a sharp distinction between formal organization and informal organization. The formal organization is the structure on the chart: defined roles, explicit authority, documented processes. The informal organization is the spontaneous associations, habitual interactions, and relationships that make the formal organization actually function. Barnard's central observation: formal organizations cannot work without informal ones. The informal fills in the gaps, the ambiguities, the situations the formal structure doesn't anticipate, which is to say, most situations.

The informal organization is not a workaround. It is not dysfunction. It is how work actually gets done, and it has been that way in every organization studied at scale. The org chart doesn't show it because the org chart was never designed to show it.

This creates a specific, recurring problem for engineers. Engineers are trained to read specifications carefully. The org chart reads like a specification — clean hierarchy, explicit relationships, clear authority lines. The engineer reads it and believes they understand the system. What they've actually done is read the documentation for a different, simpler system than the one they're operating in.

---

## What Actually Gets Work Done

Consider the sequence of events that actually precede most significant technical decisions in organizations that are functioning reasonably well.

Weeks before a formal decision meeting, conversations happen. The people whose opinions carry weight informally have already heard about the proposal. Some of them have already formed views. The person leading the effort has (or hasn't) had conversations with the key skeptics — not to preempt their objections, but to understand them, to incorporate them, or at minimum to know what they are before the formal meeting. By the time the official decision happens, it's often a ratification of alignment that either exists or doesn't. The meeting is the documentation, not the decision.

Executives who are good at getting things done know this. They call it pre-alignment or socialization or working the problem. The vocabulary varies but the practice is consistent: before you ask for formal approval, you do the informal work of building genuine support. Not theater, not coercion — genuine support, which means actually engaging with the concerns and either resolving them or making the tradeoffs explicit.

The engineer who got the manager's sign-off but missed the infrastructure team, the security team, and the platform team hadn't failed to follow process. They had successfully navigated the formal structure and missed the informal one entirely. They found the person who could say yes and failed to find the people who could actually block.

Formal authority gives you permission. Your manager can say yes. A VP can approve a budget. A director can sign off on an approach. These approvals are real and they matter; without them, certain things definitely won't happen. But formal authority is not the same as the organizational will to execute. Execution requires people to actually do things — to deprioritize other work, to allocate time, to change what they're building. That happens through informal influence, not formal command. The manager who "commands" a team to adopt a new practice and has no informal credibility on that practice is going to find the command doesn't actually transfer into changed behavior.

The Hawthorne studies — whose methodology has been revisited since — pointed to something that subsequent research confirmed repeatedly: informal group norms often govern behavior more than formal policy does. Workers who exceeded the group's informal production ceiling were ostracized. The financial incentive structure was largely irrelevant. The informal social structure was the real system.

The implications for engineering teams are direct. Your team's informal norms around code review, around who raises concerns in meetings, around how on-call burden is actually distributed — these are often more binding than anything in a documented process. They cannot be changed by announcing a new policy. They can only be changed by working with the informal network.

This is also where the invisibility problem starts. Informal networks are not just invisible on the org chart — they're invisible to the people with authority to change the structure. Which means the decisions that destroy them are made without anyone intending to. A team was restructured six months ago. Two engineers ended up on different reporting chains, different standups, different communication channels. They drifted out of regular contact. What nobody knew was that they had an informal arrangement: they proactively flagged cross-system risks to each other, filling a gap that no process covered. Reliability degraded over the following months. The root cause — that the reorg had broken a coordination mechanism nobody knew existed — wasn't discoverable from the org chart. It was only visible to the people who had been part of the arrangement.

That's the invisibility problem in its clearest form: informal networks are load-bearing in ways that don't appear in any document, and so the decisions that destroy them are made without anyone intending to. This chapter will return to what to do about it. But the first step is understanding the structure of the networks themselves.

---

## The Architecture of Informal Networks

In the 1930s, Jacob Moreno developed what he called sociometry: the systematic mapping of who actually interacts with whom in groups. Draw a sociogram — who goes to whom for advice, who shares information with whom, who talks to whom regularly — and it looks dramatically different from the org chart. This has been replicated so many times across so many different kinds of organizations that it's essentially settled as a finding. The formal and informal structures are different, and they serve different functions.

Three specific informal networks are worth understanding, because they're distinct from each other and all distinct from the org chart.

The **advice network** is who people actually go to for expertise. This is not necessarily the most senior person in the room. It is the person whose technical judgment people trust based on demonstrated track record. In many engineering organizations there is a person — often a staff engineer, sometimes someone more junior — who has become the go-to for a particular class of problem. Their opinion shapes team decisions even when they're not in the meeting. When they express doubt, proposals slow down. When they express enthusiasm, teams accelerate. Their title may be three levels below the formal decision-maker. The org chart predicts nothing about this.

The **trust network** is different from the advice network. This is who shares sensitive information with whom — who will tell you the actual state of a project before the status report says it, who will flag that the executive sponsor has gone cold on an initiative before that becomes public knowledge. Trust networks are built slowly, through repeated interactions where people demonstrate discretion. They are the substrate through which real information flows in organizations, rather than the filtered, presentation-ready information that moves through formal channels.

The **communication network** is simply who talks to whom regularly. This one sounds mundane until you map it. The surprise is usually how concentrated it is — a small number of people account for a disproportionate share of cross-team communication, and when those people leave or move teams, information flow degrades in ways that aren't visible until symptoms emerge.

Research on these networks, accumulated over decades, produces a consistent finding: somewhere between twenty and forty percent of the value-added collaboration in an organization comes from only three to five percent of the employees. These high-centrality individuals are often not the formal leaders. They are the connectors — the people who sit on the shortest path between other people in the network.

The mid-level engineer who is the only person both the infrastructure team and the product team trust and communicate with regularly is, in a meaningful sense, more influential on cross-team decisions than many people above them on the org chart. People who bridge otherwise disconnected groups get promoted faster, earn more, and generate more ideas that actually get implemented — the causal mechanism is that they see things others don't, because they're connected to groups that aren't connected to each other, and they can facilitate things others can't, because both sides trust them.

The open source world is an extreme case that clarifies the mechanism. A project maintainer has no authority to order contributions. They cannot command anyone to do anything. The governance is entirely informal — reputation, credibility, track record, relationships built through code review and mailing list discussions over years. Formal governance structures — whether a single named maintainer with final authority, a steering committee, or a foundation board — were often grafted onto projects that were already functioning through informal means. The formal structure usually followed influence that already existed; it didn't create it. Senior engineers in companies often operate in a structurally similar way. The title gives standing; the actual influence comes from trust and track record built through relationships that don't appear anywhere on a chart.

---

## Mapping Your Own Network

This is where the analysis has to get concrete, because the informal network in your organization is not published anywhere. You have to map it.

The mapping process is less exotic than it sounds. It is primarily a matter of observing carefully and asking good questions — and doing both deliberately rather than just absorbing ambient organizational information over years.

Start with the advice network. When a consequential technical decision is being made, notice who people look at before forming their own view. Notice who gets pulled into conversations as informal validators before proposals go formal. Notice who, when they express a concern in a meeting, causes other people to reconsider their positions, and who, when they express a concern, gets politely acknowledged and ignored. The latter is more informative than the former. The person whose objection visibly shifts a room is a node in the advice network, regardless of what their badge says.

Then look at the trust network. When a project is in trouble, who tells who first? When there's a political tension between teams, who knows about it before it becomes public? Who do people go to with concerns they wouldn't put in a status report? This network is harder to observe directly — it's built from private conversations — but you can infer it. The people who always seem to have accurate information about what's actually going on are high-trust nodes. The people who are consistently surprised by news that others already knew are probably outside the trust network for that information.

Ask who has informal veto power. In most organizations, some people can effectively kill a proposal without having formal authority to do so. Their technical objection carries enough weight that if they're visibly unhappy with something, the proposal stalls. Identifying these people — and engaging them before proposals go formal — is the difference between the initiative that moves and the one that dies in committee. This isn't manipulation. It's basic due diligence: find the people with genuine concerns, engage those concerns seriously, and either resolve them or make the tradeoffs explicit. The alternative is spending weeks in formal review only to discover objections that could have been addressed earlier.

Look for the bridge people. Who regularly works across team boundaries? Who appears in meetings for teams they're not formally part of? Who do multiple different teams seem to trust simultaneously? These are your high-betweenness nodes, and they're often the most efficient channel for understanding the informal concerns of groups you're trying to work with.

You have roughly fifteen working relationships you can maintain at genuine depth — which means where you invest relationship-building attention is a real constraint, not a platitude. You cannot build informal influence with everyone. Where you invest is a strategic choice, even if it doesn't feel like one.

The most reliable way to build this map is through genuine curiosity about how things work. Ask people how decisions actually get made on a particular initiative. Ask who they'd want to have concerns addressed by before they felt comfortable supporting something. Ask who they think really knows how the system works. People who have been at an organization for a while will tell you remarkable amounts of this if you ask directly and listen carefully.

After a significant cross-team decision, take five minutes to write down: who visibly shifted the room, who seemed to already know the outcome, who bridged the conversation between groups. Three months of this builds a clearer map than years of ambient experience. The practice doesn't need to be elaborate — a note in a running document is sufficient. The discipline of writing it down is what converts observation into pattern.

---

## Building Informal Capital Without Becoming Political

At this point a reasonable engineer raises an objection that deserves a serious answer: this sounds like politics.

The objection is worth separating into its components. One version of "politics" is cynical — networking for personal advancement, building relationships instrumentally to extract favors, performing warmth you don't feel. This is genuinely corrosive, and it doesn't actually work for long because informal networks run on trust and trust is sensitive to inauthenticity. People who sense they're being cultivated for strategic reasons stop sharing honest information, which defeats the purpose of the relationship entirely.

But there's a different version of political skill that isn't cynical at all: understanding how influence works and building influence through genuine usefulness and trustworthiness.

The engineer who helps the platform team debug a problem they're struggling with, with no immediate return expected, is building informal capital. The engineer who shares context that turns out to be useful to someone in a different team is building informal capital. The engineer who gives an honest assessment of a proposal's weaknesses in a private conversation, before the formal review, is building informal capital — because they're demonstrating that their evaluations can be trusted.

A second objection worth naming directly: this might sound like advice for senior engineers who already have standing. It isn't. Informal networks aren't built through positional authority — they're built through demonstrated usefulness. That means earlier investment compounds longer. The engineer who starts building cross-team trust at year three is in a significantly different position at year seven than the one who waits for the staff promotion. Informal capital accumulates slowly; the sooner you start, the more you have when you need it.

One counter-argument worth addressing: if the informal network works so well, why not just formalize it? Make the informal review gates into formal review gates. Make the advice relationships into documented consultation requirements.

The answer is that informal networks work partly because of their informality. They are faster than formal processes, more adaptive to context, and they operate on trust rather than procedure. When organizations formalize the informal — turn working lunches into mandatory cross-team check-ins, convert organic information-sharing into documented consultation requirements — they often destroy the properties that made the informal network effective and add process overhead without the benefit. Engineers will recognize this failure mode in a different domain: turning a subroutine call into a microservice adds formalism, increases overhead, and loses the properties that made the local function effective. The same pattern applies here. Some formalization is valuable — decision records, review processes, architectural decision documents — but the goal is not to replace the informal with the formal. It's to understand the informal well enough to work with it.

---

## When the Org Chart Matters

Formal and informal structures are not alternatives — they're the declared architecture and the actual runtime behavior. Understanding informal networks doesn't mean ignoring formal structure; it means knowing which instrument does what work. Ignoring formal structure is as blind as over-reading it.

Budget and headcount decisions ultimately require formal approval. Even with enormous informal influence, you cannot get someone hired or a budget allocated without the formal chain of command. Organizational commitments — the kind that get made to customers, to boards, to partners — require formal authorization. When genuine conflict arises between teams and informal negotiation fails, the org chart provides the escalation path. These are not edge cases. They happen regularly.

The effective approach is not to choose between formal and informal, but to understand the right instrument for each kind of work. Use informal alignment to build the consensus that makes formal decisions stick. Use formal authority when the decision type genuinely requires it — and not as a shortcut to skip informal alignment, because formal approval without informal alignment predicts implementation failure with remarkable consistency.

The reorg example introduced earlier goes further than it might first appear. The organization restructured to align with product lines — a formally clean decision, made through proper channels, serving real business goals. The two engineers with the informal reliability coordination were not adversarial; they weren't resisting the change. They simply drifted apart as their schedules, standups, and communication channels diverged. Nobody intended to break the reliability mechanism. Nobody knew it existed as a mechanism, as opposed to two colleagues who happened to talk.

This is what the invisibility problem means in practice: it's not that the people making structural decisions are careless. It's that the information required to make those decisions carefully isn't in any document they consult. The knowledge of which informal arrangements are load-bearing lives in the heads of the people involved. If those people don't surface it, it doesn't exist for planning purposes.

For engineers who want to have influence over organizational decisions — including decisions about structure — this suggests a concrete practice: make the informal visible, selectively and deliberately. Document the cross-team dependencies that work because of informal relationships, not just the ones that are formalized. When informal coordination mechanisms are load-bearing, make sure the people with authority over structure know they exist. Not to formalize them — which often destroys the properties that make them work — but to prevent their inadvertent destruction.

---

## What Changes Monday

First, notice what you can't see on the org chart. The next time you're working on something that requires coordination with other teams, spend fifteen minutes before the first formal meeting mapping the informal terrain. Who in each team has standing to raise concerns that will actually slow things down? Who is likely to have already formed a view that will matter more than what happens in the meeting? Who are the bridge people — the connectors who have relationships across the relevant teams? These aren't supplemental questions to ask after you've run the formal process. They're the questions that determine whether the formal process produces an outcome that sticks.

Second, distinguish permission from momentum before you seek approval. Before you bring a proposal to your manager or to a formal decision meeting, ask: do the people who will actually execute this have the information and the context to support it? Have the people whose technical objections could slow implementation been engaged, not to neutralize them, but to understand whether their concerns are resolvable? If the answer is no, delay the formal ask and spend the next week on the informal one: identify the two or three people whose unresolved concerns will cause the proposal to stall, and get those conversations on the calendar.

Third, pick one or two people in adjacent teams and invest in knowing them without an immediate agenda. Not a networking exercise — a genuine attempt to understand their constraints, their priorities, and what problems they're dealing with. The information you get will be useful. The trust you build will be more useful. This is not a fast return, but the engineers who are most effective at cross-team work over a multi-year period are almost all the ones who did this work consistently before they needed it.

The longer-term shift: once a quarter, write down what you know about the informal power structure of the initiatives you're on. Who has whose trust? Who's the bridge between which groups? Where has influence shifted in the past three months? The engineers who are most effective at organizational navigation aren't more perceptive than their peers — they're more deliberate. They treat the informal network the way they treat a system they're responsible for: something with structure, invariants, failure modes, and points of leverage, worth understanding carefully rather than discovered only when it breaks.

The engineer who left the Thursday meeting with sign-off, then watched the initiative die by Monday, had mastered the org chart. What they hadn't yet learned was how to read the territory. That skill is learnable. It starts with accepting that the map is not the territory, and working from there.
