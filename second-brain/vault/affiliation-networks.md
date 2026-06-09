---
title: "Affiliation Networks"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [homophily]
---

## One-line Summary
Affiliation networks are bipartite graphs connecting persons to foci (classes, clubs, workplaces) — making social context explicit and enabling three distinct closure mechanisms that can produce homophily-like patterns without any personal preference for similarity.

## Core Intuition
Where do people meet? Through shared classes, clubs, workplaces, neighborhoods — social settings called *foci*. An affiliation network models these as a bipartite graph: person nodes on one side, focus nodes on the other, with edges encoding participation. This separates "people are similar" from "people share the same places." The bipartite structure also reveals three closure processes: triadic (friend-of-friend becomes friend), focal (strangers in the same context become friends), and membership (friend introduces you to a new context). Focal closure is particularly important: it can create ties among strangers through repeated exposure alone, producing homophily-like patterns even without any preference for similarity.

## Formal Definition / Statement
**Bipartite affiliation graph** G = (P ∪ F, E):
- P: actor nodes (persons)
- F: focus nodes (groups, locations, classes, organizations)
- E: edges only between P and F — "person p participates in focus f"

**Person-by-focus membership matrix** B:
- B_pf = 1 if person p participates in focus f

**Co-occurrence projections**:
- Person co-occurrence: BB^T (edge weight = shared foci count)
- Focus co-occurrence: B^TB (edge weight = shared participants count)

**Three closure processes**:
| Type | Open path | What closes | Example |
|------|-----------|-------------|---------|
| Triadic | person → friend → person | New friendship | "My lab partner introduces me to their friend" |
| Focal | person → focus → person | New friendship | "We sit in the same elective and start talking" |
| Membership | person → friend → focus | New membership | "My friend invites me to the robotics club" |

## Key Properties
1. **Bipartite structure**: edges only between P and F, never within P or within F
2. **Projection creates dense cliques**: a focus with s members adds C(s,2) edges in projection
3. **Co-occurrence ≠ relationship**: shared context is opportunity, not confirmed tie
4. **Keep weights**: sharing five foci is stronger evidence than sharing one
5. **Focal closure needs no shared friend**: strangers in the same context can form ties
6. **Membership closure is the reverse direction**: friends pull you into contexts they inhabit

## Worked Example
**Corporate board interlocks**:
- Board members (P) connect to company boards (F)
- Member-member projection: two board members share ≥1 company → peer exposure, governance norms
- Company-company projection: two firms share ≥1 board member → strategic interlocks, diffusion

**Classroom example**:
- Students (P) connect to classes, labs, clubs (F)
- Focal closure: two students in the same statistics elective become friends
- Membership closure: a friend invites you to join the robotics club
- Triadic closure: your lab partner introduces you to their other friend

**Kossinets & Watts (2006)**: University email data (~43,000 people, ~14M messages). Measured:
- Triadic closure: P(new tie | k shared contacts) follows saturating curve
- Focal closure: P(new tie | k shared classes) — one class already informative, additional classes add less than independent model predicts

## Common Pitfalls
1. **Confusing co-occurrence with friendship**: shared context is opportunity, not confirmed relationship
2. **Ignoring projection density**: a focus with many members creates many edges — weight matters
3. **Assuming focal closure requires preference**: strangers in the same context form ties through exposure alone
4. **Forgetting membership closure**: the reverse direction (friends → foci) also shapes the network
5. **Treating all closure as triadic**: focal and membership closure are distinct mechanisms

## Connections
- [[homophily]] — affiliation networks can produce homophily-like patterns without preference
- [[selection-vs-socialization]] — contextual correlation operates through shared foci
- [[network-autocorrelation]] — shared foci produce attribute autocorrelation without direct peer influence
- [[schelling-segregation-model]] — foci create the opportunity structure for segregation
- [[network-science-l03]] — triadic closure from Lecture 03
- [[network-science-l05]] — lecture overview

## Open Questions
- How do we model overlapping, hierarchical foci (e.g., a department within a university)?
- Can we quantify the relative contribution of triadic vs focal vs membership closure?
- How do affiliation networks evolve over time?
- What is the right granularity for defining foci?
