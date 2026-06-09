---
title: "Bipartite Graphs"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [graph-fundamentals]
---

## One-line Summary
A bipartite graph has two disjoint node sets where edges only connect nodes across sets, never within the same set.

## Core Intuition
Many real-world relationships connect two fundamentally different types of entities: students and courses, users and products, authors and papers. A bipartite graph explicitly models this two-set structure, preventing edges within the same entity type.

## Formal Definition / Statement
A **bipartite graph** G = (U, V, E) has two disjoint node sets (U ∩ V = ∅) where all edges connect a node from U to a node from V. Edges never connect two nodes within the same set.

## Key Properties
- All edges go between U and V, never within U or within V
- Useful for modeling relations between two inherently different sets of entities
- Can be **projected** onto one set (e.g., "students who share a course") — but projection loses information
- A graph is bipartite iff it contains no odd-length cycles
- Common in [[sparse-dense-and-random-graphs|real networks]]: affiliation networks, recommendation systems

## Worked Example
University course enrollment:
- Set U = {Student₁, Student₂, Student₃}
- Set V = {Course_A, Course_B, Course_C}
- Edges: (Student₁, Course_A), (Student₁, Course_B), (Student₂, Course_A), ...
- Projection onto students: connect two students if they share a course
- Projection onto courses: connect two courses if a student takes both

## Common Pitfalls
- Projecting a bipartite graph onto one set and treating the projection as the "real" graph — you lose the two-set structure and introduce assumptions
- Forgetting that bipartite graphs cannot have odd cycles — this is both a property and a useful test
- Confusing bipartite graphs with [[directed-and-undirected-graphs|directed graphs]] — bipartiteness is about node types, not edge direction

## Connections
- [[graph-fundamentals]] — bipartite graphs are a special case of general graphs
- [[sparse-dense-and-random-graphs]] — many real affiliation networks are sparse and bipartite
- [[neighbourhood-and-degree]] — degree in bipartite graphs relates to how many cross-set connections a node has
- [[connectivity-and-components]] — bipartite components have a specific structure

## Open Questions
- When is a bipartite projection a useful simplification, and when does it mislead?
- How do bipartite structures affect network dynamics like diffusion or influence?
