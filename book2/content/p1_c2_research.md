# Research Notes: p1_c2 — "The Org Chart Is a Lie"

## Core Tension

The org chart is a useful fiction. It accurately describes legal accountability (who signs off on your raise) but poorly describes operational reality (who you actually need to persuade to ship anything). Engineers who treat the hierarchy as the ground truth of influence keep experiencing the same confusion: they got permission from their manager, so why is nothing moving? Because permission and momentum are different resources, and they come from different places.

---

## 1. Historical Parallels

### 1.1 The Hawthorne Studies and the Informal Group (1920s–1930s)
Elton Mayo's research at Western Electric's Hawthorne plant is the founding document of informal organization theory. Researchers expected output to track formal incentives (pay, lighting, breaks). Instead, they found that workers had formed tight informal groups with their own norms, and those norms governed output more than management policy did. Workers who exceeded the group's informal production ceiling were ostracized — the social penalty outweighed the financial reward. The formal incentive structure was largely irrelevant. This is the original "the org chart is a lie" finding, predating the phrase by decades.

Implication for engineers: your team's informal norms around code review, on-call, and technical debt are often more binding than anything in a documented process. Violating them has consequences the org chart cannot explain.

### 1.2 Wartime Production and the "Fixing" Networks
In WWII manufacturing, official production processes described how work was supposed to flow. What actually kept production lines moving was an informal network of "fixers" — experienced workers who knew where to get parts, who could barter across departments, and how to route around bureaucratic blockages. Sociologist Donald Roy documented this in steel mills: formal channels were too slow and rigid; the informal network was the actual production system. Management often didn't know this network existed until they accidentally dismantled it through a reorganization.

Implication: when an organization reorgs, informal networks don't automatically transfer. A reorg that looks clean on paper can destroy the actual load-bearing structure without anyone in leadership realizing it for months.

### 1.3 Open Source and Governance Without Authority
The governance of large open source projects is an extreme case of influence-without-authority. A project maintainer cannot order anyone to do anything. Contribution happens through reputation, credibility, and relationships — pure informal network. What's interesting is that formal structures (benevolent dictators for life, steering committees, foundation governance) were often grafted onto projects that were already working through informal means. The formal structure often follows influence that already exists; it doesn't create it.

Implication: senior engineers often operate in a similar mode inside companies. The title gives them standing; the actual influence comes from trust and track record built through relationships that don't show up on a chart.

---

## 2. Key Frameworks

### 2.1 Informal Organization (Chester Barnard, 1938)
Barnard's "The Functions of the Executive" distinguished formal organization (defined roles, authority) from informal organization (the spontaneous associations, habits, and relationships that make formal organizations actually work). His key insight: formal organizations cannot function without informal ones. They are not competitors; the informal fills gaps the formal cannot. Barnard argued that executives succeed not by commanding but by securing willing cooperation — which comes from informal legitimacy, not formal authority.

### 2.2 Sociograms and Network Mapping (Jacob Moreno, 1930s)
Moreno developed sociometry — the mapping of who actually interacts with whom in a group. A sociogram visualizes the informal network: who are the connectors (high betweenness centrality), who are the stars (high in-degree, many people seek them out), who are the isolates. What's consistent across decades of research: the sociogram and the org chart look dramatically different. The formal leaders and the informal connectors are often not the same people.

In organizations, "betweenness centrality" is particularly powerful — people who sit between groups, translating and brokering, often have disproportionate influence even when they have no formal authority. The staff engineer who translates between the platform team and three product teams is a high-betweenness node whether or not any title acknowledges it.

### 2.3 Dunbar's Number and Cognitive Limits on Networks
Robin Dunbar's research on primate neocortex size and group cohesion suggests humans can maintain stable social relationships with roughly 150 people. Within that number, there are tighter layers: ~5 (intimate), ~15 (close friends/trusted colleagues), ~50 (active network). This matters for organizational influence because trust-based influence requires relationship maintenance, and there are cognitive limits on how many relationships you can genuinely maintain.

For engineers, this creates a practical constraint: you cannot build informal influence with everyone. The implication is that where you invest relationship-building attention is a strategic choice, not just a social one.

### 2.4 Communities of Practice (Lave & Wenger, 1991)
Wenger's work on communities of practice describes how informal groups of practitioners develop shared knowledge, norms, and identity that cut across formal organizational lines. A community of practice around reliability engineering, or database architecture, or API design operates largely outside the org chart. Decisions that look like they were made by individuals are often actually negotiated within these communities first.

The practical implication: joining and contributing to informal communities of practice is how technical influence spreads across an organization. The engineer who only works within their team's formal boundaries limits their influence accordingly.

### 2.5 Social Capital (Burt, Putnam, Coleman)
Robert Putnam's distinction between bonding social capital (within a group) and bridging social capital (across groups) is directly applicable. Engineers often have deep bonding capital within their team and weak bridging capital across teams. Bridging capital is rarer and more valuable for getting cross-team things done.

Ron Burt's "structural holes" research shows that people who bridge disconnected groups capture information advantages and disproportionate influence. The person who knows people in infrastructure, product, and security — when those groups don't know each other well — has significant informal power regardless of title.

---

## 3. Concrete Scenarios

### 3.1 The Permission That Means Nothing
A senior engineer gets explicit approval from their manager to adopt a new architectural pattern. They announce it. Two weeks later, the infrastructure team flags that it doesn't work with their deployment system. Security says it hasn't been reviewed. The platform team points out it conflicts with a decision made six months ago. The engineer had formal permission and zero informal alignment. The org chart said "approved"; the actual network said "blocked." The missing step was mapping who had standing to object before asking the one person who could formally say yes.

### 3.2 The Invisible Principal
A team is technically led by a director. Everyone on the team defers formally to the director. But on every consequential technical question, they wait to hear what a particular staff engineer thinks before forming views. The staff engineer rarely speaks first in meetings — they ask questions and let others talk, then synthesize. When they express doubt, projects slow down. When they express enthusiasm, teams accelerate. Their formal title is three levels below the director. No one has explicitly acknowledged this dynamic. New team members learn it within a month by observation. The org chart predicts nothing here.

### 3.3 The Reorg That Broke Everything
An organization restructures to align teams with product lines rather than functions. The new chart is clean. Four months later, reliability has degraded. The reason: two engineers in different teams had an informal arrangement where they proactively flagged cross-system risks to each other. The reorg put them on different schedules, different standups, different Slack groups. They drifted out of contact. No one intended to break the reliability coordination mechanism because no one knew it existed as an informal arrangement rather than a documented process. The org chart didn't show what it was destroying.

### 3.4 The New Senior Engineer Who Reads Only the Org Chart
An engineer joins at senior level. They read the org chart carefully. They work diligently. They escalate through proper channels. They are puzzled that their well-reasoned proposals keep dying in committee. What they haven't learned: the two engineers with five years of tenure who informally set the technical agenda before any committee meeting; the skip-level relationship pattern where the principal engineer and the VP talk weekly outside formal channels; the informal technical review that happens in a recurring lunch that has no official standing. The org chart described the theater. They were trying to navigate using the map of a different city.

### 3.5 The Bridge Person
A mid-level engineer spends two years building relationships across the infrastructure, mobile, and data teams while nominally working on the API layer. They become fluent in each team's constraints, vocabulary, and frustrations. When a cross-team initiative is needed, they are the natural coordinator — not because anyone appointed them, but because they are the only person all three teams trust and who has the full context. They have formal authority over nothing. They have informal influence over everything that touches those teams. A new manager looking at the org chart cannot explain why this engineer's opinion gets weight in rooms they have no formal standing in.

### 3.6 The Expert Who Lacks the Network
A technically exceptional engineer delivers outstanding individual work but has few relationships outside their immediate team. When their project requires coordinating with three other teams, the project stalls. Their technical proposals are correct but go unimplemented because they have no informal standing with the people who would need to act on them. A less technically sophisticated engineer with broad relationships and high trust might have shipped the same outcome faster. Technical credibility is necessary but not sufficient; the network determines the delivery.

---

## 4. Counter-Arguments

### 4.1 "The org chart exists for a reason — working around it is politics"
This is the strongest objection and contains real truth. Formal hierarchies encode accountability, ensure decisions are made by people with appropriate context and responsibility, and prevent local optimization from overriding legitimate organizational interests. Engineers who become expert at navigating informal networks can use those skills to advance personal agendas or subvert good organizational decisions.

The response: the argument conflates *understanding* informal networks with *circumventing* formal authority. Mapping influence networks helps you know *who to align* before proposals go through formal channels — not to avoid those channels, but to arrive at them with genuine support rather than paper approval. The goal is not to route around the hierarchy but to ensure that when formal approval happens, it reflects real organizational consensus rather than manufacturing a surprise. Executives who later "discover" that a formally approved decision had no buy-in experience this failure mode constantly.

### 4.2 "If the informal network matters so much, just formalize it"
This objection is practically appealing and consistently fails. Informal networks work partly because of their informality — they are faster, more adaptive, and operate on trust rather than process. When organizations attempt to formalize the informal (mandatory cross-team check-ins, documented influence relationships), they often destroy the properties that made the informal network effective while creating process overhead. The Hawthorne studies are instructive: management attention to the informal group often changed its behavior, not always for the better.

The response: some formalization is valuable (e.g., documented decision rights, RFCs as a forcing function for alignment). But the goal isn't to make the informal formal — it's to understand the informal well enough to work with it effectively. A map is not the territory; the org chart will always be a reduction of organizational reality. Knowing that is the prerequisite to navigating well.

---

## 5. Data Points and Research

- **Cross & Parker (2004), "The Hidden Power of Social Networks"**: Studied informal networks in dozens of organizations. Found that 20–40% of value-added collaborations came from only 3–5% of employees. These high-centrality individuals were often not the formal leaders. Also found that overloaded connectors are a significant organizational risk — single points of failure hidden from the org chart.

- **IBM Institute for Business Value research on influence and informal networks**: Organizations that actively managed informal networks saw measurably faster decision implementation. "Network analytics" as a management practice showed consistent positive effects on cross-team coordination speed.

- **Krackhardt & Hanson (1993), "Informal Networks: The Company Behind the Chart" (Harvard Business Review)**: Identified three critical informal networks: advice networks (who do people go to for expertise), trust networks (who shares sensitive information), and communication networks (who talks to whom regularly). These three maps look different, and all look different from the org chart.

- **Burt's "Structural Holes" (1992)**: Empirical finding that people who bridge otherwise disconnected groups earn higher compensation, get promoted faster, and generate more ideas that get implemented. The mechanism is information advantage combined with brokerage influence. Effect holds controlling for performance ratings.

- **McKinsey research on "informal organization"**: Consistently finds that when transformational change fails, the cause is failure to engage informal networks and opinion leaders, not failure to get formal sign-off. Formal approval without informal alignment predicts implementation failure.

- **Dunbar (1992, 1998)**: The layered structure of human social networks (5 / 15 / 50 / 150) has been replicated in phone call data, online social networks, and organizational studies. The layers represent different levels of emotional closeness and interaction frequency. Influence through trust requires being in someone's ~15 or ~50 layer — which takes time and consistent interaction.

---

## 6. Suggested Section Structure

### Section 1: The Map and the Territory
Introduce the core premise: org charts are maps, not territory. What they accurately capture (legal accountability, escalation paths) vs. what they can't (influence, trust, information flow, informal norms). Frame the chapter's practical question: how do you navigate the terrain, not just the map?

### Section 2: What Actually Gets Work Done
Walk through how consequential decisions actually get made and implemented. Pre-alignment before formal approval. The role of trust networks vs. authority chains. Distinguish between permission (formal) and momentum (informal). This section is where concrete scenarios land hardest.

### Section 3: The Architecture of Informal Networks
Introduce the conceptual tools: advice networks, trust networks, betweenness centrality, structural holes, communities of practice. Not as academic vocabulary but as practical instruments. What does high betweenness centrality actually look like in a team? What does a structural hole look like, and how do you know when you're filling one?

### Section 4: Mapping Your Own Network
Practical methodology for mapping the informal network an engineer actually operates in. Who are the informal opinion leaders? Who bridges disconnected groups? Where are the informal review gates before formal decisions? This section moves from observation to action: how do you actually draw this map?

### Section 5: Building Informal Capital Without Becoming Political
Address the real tension: how do you build influence networks deliberately without it becoming manipulation? The distinction between being useful/trustworthy (sustainable informal capital) vs. performing relationships strategically (fragile and corrosive). Why the long game matters: informal networks run on reputation, which is accumulated slowly and destroyed quickly.

### Section 6: When the Org Chart Matters (And When to Use It)
Avoid swinging to the opposite extreme. Formal authority is real and matters in specific contexts: budget, headcount, organizational commitments, situations requiring accountability. The engineer who only operates through informal networks is also misreading the situation. Org chart authority matters most in resource allocation, external commitments, and conflict resolution. Informal influence matters most in day-to-day execution, technical direction, and building the alignment that makes formal decisions stick.

---

## Tensions and Angles to Develop

- The person who "doesn't play politics" often means "I only navigate formal channels" — which is itself a political choice, usually an ineffective one.
- New employees face an information asymmetry: the informal network is invisible to them but obvious to everyone who's been there three years. This makes the first six months at a new organization disproportionately high-risk for well-intentioned political errors.
- Remote work has changed informal networks significantly. The spontaneous in-person interactions that built informal trust have partially decayed; some engineers have replaced them deliberately (coffee chats, etc.) and some haven't, leading to an uneven distribution of informal capital in distributed organizations.
- Informal networks can calcify and become the status quo resisting change. The same network that gets things done today can be the thing blocking good ideas tomorrow. This complicates the narrative — informal networks are powerful, and power can be used well or badly.
