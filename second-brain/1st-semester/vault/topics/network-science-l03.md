---
title: "L03 — Strong and Weak Ties"
tags: [topic-overview, network-science, semester-1]
course: "Network Science"
lecture: 3
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: ["[[graph-fundamentals]]"]
---

## One-line Summary
Social ties come in strong and weak varieties; triadic closure shapes how they form, and weak ties serve as critical bridges carrying novel information across communities.

## Core Intuition
Friends-of-friends tend to become friends (triadic closure). When you label ties as strong or weak, Strong Triadic Closure (STC) says: if a node has two strong ties, those endpoints must be connected. This constraint implies that any local bridge — an edge between nodes with no shared neighbors — must be a weak tie. Weak ties are therefore structurally necessary to connect otherwise separate clusters, and they carry non-redundant information. Since recovering the optimal strong/weak labeling is NP-hard, we use polynomial-time proxies (clustering coefficient, neighborhood overlap) and test the weak-tie theorem empirically.

## Lecture Structure

### Part 1: Triadic Closure
- [[triadic-closure]] — open triads tend to close into triangles
- Empirical evidence: Kossinets & Watts (2006) university email study — 30× more likely to connect with shared contacts

### Part 2: Typed Edges and Strong Triadic Closure
- [[strong-triadic-closure]] — constraint on edge labelings: two strong ties force closure
- [[maxstc-complexity]] — recovering the optimal labeling is NP-hard (Sintos & Tsaparas, 2014)

### Part 3: Structural Heuristics
- [[clustering-coefficient]] — node-level measure of neighborhood density
- [[neighborhood-overlap]] — edge-level measure of shared neighbors (Jaccard)

### Part 4: Bridges and the Weak-Tie Theorem
- [[bridges-and-local-bridges]] — edges whose removal disconnects or locally disconnects
- [[weak-ties-hypothesis]] — Granovetter's theorem: local bridges incident to STC-satisfying nodes must be weak

### Part 5: Empirical Validation
- Onnela et al. (2007): cell-phone network — overlap vs. tie strength monotone; knockout experiment
- Facebook maintained friendships plateau at ~150 (Dunbar)
- Twitter active friends plateau despite growing follower counts
- Bakshy et al. (2012): weak ties drive most information diffusion on Facebook

## Key Papers Referenced
| Paper | Key Finding |
|---|---|
| Kossinets & Watts (2006) | 30× closure effect in university email |
| Sintos & Tsaparas (2014) | MaxSTC is NP-hard |
| Onnela et al. (2007) | Overlap correlates with tie strength; weak-tie knockout fragments network |
| Gonçalves et al. (2011) | Maintained friends plateau at ~150 on Facebook |
| Huberman et al. (2008) | Active Twitter friends plateau; followers grow freely |
| Bakshy et al. (2012) | Weak ties generate most total information diffusion |

## Connections
- Builds on: [[graph-fundamentals]] (graph notation, adjacency)
- Related: [[social-capital]] (closure creates trust; bridges create opportunity)
- Related: [[structural-holes]] (Burt's theory: brokerage across structural holes)
- Extends to: [[network-science-l04]] (next lecture, likely network models)

## Open Questions
- How sensitive are empirical results to the choice of tie-strength proxy?
- Can machine learning recover STC labelings tractably on restricted graph classes?
- How do directed/weighted edges change the weak-tie theorem?
