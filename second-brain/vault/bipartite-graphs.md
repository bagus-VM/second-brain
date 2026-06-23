---
title: "Bipartite Graphs"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-23
prerequisites: [graph-fundamentals]
---

## One-line Summary
A bipartite graph has two disjoint node sets where edges only connect nodes across sets, never within the same set.
![[Pasted image 20260623142244.png|300]]
## Core Intuition
Many real-world relationships connect two fundamentally different types of entities: students and courses, users and products, authors and papers. A bipartite graph explicitly models this two-set structure, preventing edges within the same entity type.

## Formal Definition / Statement
A **bipartite graph** G = (U, V, E) has two disjoint node sets (U ∩ V = ∅) where all edges connect a node from U to a node from V. Edges never connect two nodes within the same set.

## Key Properties
- All edges go between U and V, never within U or within V
- Useful for modeling relations between two inherently different sets of entities
- Can be **projected** onto one set (==e.g., "students who share a course")== — but projection loses information
- A graph is bipartite if it contains no odd-length cycles
- ==Common in [[sparse-dense-and-random-graphs|real networks]]: affiliation networks, recommendation systems==

## Worked Example
University course enrollment:
- Set U = {Student₁, Student₂, Student₃}
- Set V = {Course_A, Course_B, Course_C}
- Edges: (Student₁, Course_A), (Student₁, Course_B), (Student₂, Course_A), ...
- Projection onto students: connect two students if they share a course
- Projection onto courses: connect two courses if a student takes both

## Common Pitfalls
- Projecting a bipartite graph onto one set and treating the projection as the "real" graph — you lose the two-set structure and introduce assumptions
- **Forcing a system into a bipartite mold when within-set edges exist and matter.** The "no edges inside U or V" axiom is a simplification; it misleads when those deleted edges drive the phenomenon. ==Example: modeling a sexual-contact network as bipartite (men↔women) for epidemic threshold — same-sex within-set edges are exactly the bridges that sustain transmission below the bipartite-predicted threshold. The simplification is cleanest where it's most wrong.==
- **Reading a projection's dense cliques as real communities.** A high-degree node on one side injects C(s,2) edges into the projection (see [[affiliation-networks]] pitfall #2). ==One mandatory course with 400 students → a 400-clique that community detection flags as one community. Artifact, not structure. Co-occurrence ≠ relationship.==
- Forgetting that bipartite graphs cannot have odd cycles — this is both a property and a useful test
- Confusing bipartite graphs with [[directed-and-undirected-graphs|directed graphs]] — bipartiteness is about node types, not edge direction

## Connections
- [[graph-fundamentals]] — bipartite graphs are a special case of general graphs
- [[sparse-dense-and-random-graphs]] — many real affiliation networks are sparse and bipartite
- [[neighbourhood-and-degree]] — degree in bipartite graphs relates to how many cross-set connections a node has
- [[connectivity-and-components]] — bipartite components have a specific structure
- [[affiliation-networks]] — focal closure: a shared focus bridges disconnected groups; the focus is the broker
- [[structural-holes]] — a high-degree focus spans structural holes between groups (high betweenness)
- [[weak-tie-paradox-contagion]] — bipartite foci accelerate simple contagion but block complex contagion

## Open Questions
- ~~When is a bipartite projection a useful simplification, and when does it mislead?~~ **Resolved 2026-06-23:** 
	- It misleads in two ways — (1) when the no-within-set-edges axiom is false and those edges drive the phenomenon (e.g., epidemic threshold on a sexual-contact network), and (2) when you collapse it by projection and read the resulting dense cliques as real communities (a single high-degree focus manufactures a clique of C(s,2)). It's a useful simplification when the two-type split is genuine and you analyze the graph *as* bipartite, keeping both partitions visible. See Common Pitfalls above.
- ~~How do bipartite structures affect network dynamics like diffusion or influence?~~ **Resolved 2026-06-23 (student answer + Professor White refinement):**
	- **Student intuition (correct):** University network, students ↔ courses bipartite. A student leaks an exam sheet to a friend. It spreads to the whole class — 300 students, 90 friend groups, even different faculties — even though none of those groups are friends with each other. The 1 common denominator: the single course they all share.
	- **Precise mechanism:** The course node is a BROKER spanning the [[structural-holes]] between 90 disconnected friend groups. It has high betweenness — it sits on the shortest path between every cross-group pair. The leak is SIMPLE contagion (one hearing suffices), so bridges accelerate it ([[weak-tie-paradox-contagion]]).
	- **What's bipartite-specific:** The broker is a CONTEXT (focus), not a person. One course node of degree 300 creates C(300,2) potential bridges simultaneously — no individual has to be a super-spreader. The focus IS the hub. This is what bipartite structure adds: foci, not just actors, can be the high-betweenness bottlenecks (see [[affiliation-networks]] focal closure).
	- **The flip:** For COMPLEX contagion (needs reinforcement, e.g., "should I risk using the leak?"), that same thin bridge through one shared course BLOCKS — one contact can't meet the threshold. Same structure, opposite effect.
	- **Projection contrast:** In the bipartite view, the single point of failure is visible — remove the course, diffusion stops. Project to student-student and you get a 300-clique that hides the mechanism entirely (connects to the first resolved OQ above).
