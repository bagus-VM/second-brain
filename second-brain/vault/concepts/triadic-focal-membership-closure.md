---
title: "Triadic, Focal, and Membership Closure"
tags: [concept, network-science, semester-1, closure, triadic-closure, affiliation, focal-closure, membership-closure]
course: "Network Science"
source_count: 2
status: current
last_updated: 2026-06-14
prerequisites: ["[[triadic-closure]]", "[[affiliation-networks]]", "[[homophily]]"]
---

## One-line Summary
A bipartite (affiliation) network has three distinct mechanisms that can create ties in its one-mode projection — triadic closure (two nodes share a friend), focal closure (two nodes share an affiliation), and membership closure (a node joins an affiliation because of a friend) — and they can all operate simultaneously, sometimes on the same new edge.

## Core Intuition
Project a bipartite network (people × events/groups) onto its people layer, and ask: *why* is there an edge between two people? The classical "triadic closure" answer (you and I are friends, so we have a friend in common) is only one of three mechanisms. Kossinets & Watts (2006) decompose the projection-edge formation into:

1. **Triadic closure** — a transitive chain in the projected graph: you have a friend, who has a friend, who becomes your friend.
2. **Focal closure** — a shared external event: you and I both attend the same course / workplace / conference, and that co-presence creates the tie.
3. **Membership closure** — a node's *new* affiliation causes it to connect to nodes already at that affiliation (the "join the club to meet its members" mechanism).

All three can be present, and they can co-occur on the same new edge. The distinction matters for prediction and for causal modelling: focal and membership closure are *context-driven* (the affiliation is the cause), triadic closure is *transitivity-driven* (the existing social network is the cause).

## Formal Definition / Statement

Given a bipartite graph B = (U, V, E) where U is the set of people, V is the set of affiliations (events, groups, courses, places), and E ⊆ U × V are the memberships, the projection onto U is the graph G = (U, E') where:

    (u, w) ∈ E'  iff  ∃ v ∈ V : (u, v) ∈ E ∧ (w, v) ∈ E

Now consider a new projected edge (u, w) that appears at time t. It was caused by **one of three mechanisms** (or a combination):

### Triadic closure
There exists a node p ∈ U such that (u, p) and (p, w) were both already in E' at time t − 1. The new edge closes a triangle in the projected graph. *Driver: existing social network.*

### Focal closure
There exists a node v ∈ V such that (u, v) was already in E at time t − 1, and (w, v) was *also* already in E at time t − 1. The new edge arises from shared affiliation that predates the edge. *Driver: shared context.*

### Membership closure
There exists a node v ∈ V such that exactly one of (u, v) or (w, v) was in E at time t − 1, and the other was added at time t (or just before). The new edge is created because one node *joined* an affiliation the other was already in. *Driver: new affiliation joining.*

### The Kossinets-Watts observation
In a longitudinal study of an online social network, the three mechanisms had approximately equal explanatory power — focal and triadic closure were each ~30-40%, membership closure ~20-30%. The relative importance depends on the *affiliation density* of the network.

## Key Properties / Complexity

### Mechanism signatures
- **Triadic closure** is symmetric: both endpoints already knew *some* friend of the other. The new edge has no "context anchor" — both u and w are at the same event *because* of the new edge.
- **Focal closure** is anchored: there is a specific v ∈ V that both u and w attended at time t − 1, and the new edge is best explained by that co-presence. The affiliation predates the tie.
- **Membership closure** has a temporal arrow: exactly one of u, w newly joined v. Without the joining event, the new edge would not exist.

### Information lost in projection
- Which affiliation generated each tie (focal? membership? both?)
- The *order* of joining (for membership closure)
- The *strength* (multiple shared affiliations → stronger tie)
- The *type* of affiliation (work, leisure, family — different closure dynamics)

### Why projection is lossy
A weighted projection that only counts shared affiliations treats focal and membership closure the same. A multi-layer / multi-relational network preserves the information at the cost of complexity.

## Worked Example

The lecture's affiliation network:
- Students: S1, S2, S3, S4
- Courses: C1, C2, C3
- Enrolments: (S1, C1), (S1, C2), (S2, C1), (S3, C2), (S3, C3), (S4, C3)

Projected edges on students:
- S1–S2 (via C1) — focal closure (both at C1)
- S1–S3 (via C2) — focal closure (both at C2)
- S3–S4 (via C3) — focal closure (both at C3)

Now consider the *potential* edge S2–S3:
- Is there a triadic path? S2 – S1 – S3 exists. → Triadic closure predicts S2–S3.
- Is there a shared focal affiliation at time t−1? S2 and S3 share nothing at t−1. → Focal closure does NOT predict (yet).
- If S2 joins C2, then S2 and S3 share C2. → Now focal closure predicts, AND membership closure operates (S2 joined because of the connection? or independent?).

So the "after S2 joins C2" scenario is a case where *multiple mechanisms* predict the same new edge. Disentangling them requires longitudinal data and ideally exogenous shocks to the affiliation structure.

## Common Pitfalls
- **Confusing closure types in static projections**: with only the projected graph, all closures look the same (an undirected edge). You need the bipartite + temporal information to distinguish them.
- **Ignoring focal closure**: the classical "triadic closure" story is over-emphasised in popular treatments. Real networks show that *shared context* is often the dominant driver of new ties.
- **Conflating membership closure with selection**: joining an affiliation because of a friend (membership closure) is a *behavioural* response to social influence — distinct from selection-by-similarity (which the homophily literature studies).
- **Treating closure as instantaneous**: focal and membership closure operate on the time scale of the affiliation. Joining a course takes a semester; meeting a friend at a conference takes days.
- **Over-weighting triadic closure in dense networks**: in a network where everyone shares a focal affiliation (same workplace, same university), triadic closure is trivially satisfied by the focal one. The mechanisms are not independent.

## Connections
- [[triadic-closure]] — the original (non-bipartite) notion
- [[affiliation-networks]] — the bipartite source
- [[homophily]] — the affinity-based alternative
- [[weak-ties-hypothesis]] — Granovetter's framing: triadic closure through strong ties
- [[selection-vs-socialization]] — the causal-inference framing for the same phenomena
- [[kossinets-watts-2006]] — the empirical study that decomposed the three closures

## Open Questions
- How do the three closures interact in a network that has multiple affiliation types (work + family + hobbies)? (Kossinets & Watts studied one network; the generalisation to multiplex is open.)
- Can a generative model be fit to data that recovers the *relative weights* of the three closures? (Latent space models, stochastic block models — partial answers exist.)
- How does the *cost* of an affiliation (free vs. paid, public vs. private) change the closure mix? (Expensive affiliations weight focal closure higher.)
