---
title: "Graph Fundamentals"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
A graph G = (V, E) is the formal mathematical structure for modeling networks, consisting of vertices (nodes) and edges (links).

## Core Intuition
Every network — social, technical, economic — can be abstracted as a graph. The key step is choosing what counts as a node and what counts as an edge. This modeling choice is never neutral; it determines what you can see and what you miss.

## Formal Definition / Statement
A **graph** G = (V, E) consists of:
- A set of **vertices** (nodes) V
- A set of **edges** (links) E ⊆ V × V

The modeling process goes: **Reality → Choose nodes → Choose edges → Graph model → Analysis**.

## Key Properties
- Nodes represent entities (people, pages, cities, institutions)
- Edges represent relationships (friendship, hyperlinks, roads, transactions)
- Edges can be [[directed-and-undirected-graphs|directed or undirected]]
- Edges can be [[weighted-graphs|weighted or unweighted]]
- Graphs can be [[sparse-dense-and-random-graphs|sparse, dense, or random]]
- The graph formalism is flexible — the "right" graph depends on the research question

## Worked Example
A university course enrollment system:
1. Nodes: Students and courses (two types → [[bipartite-graphs|bipartite]])
2. Edges: "Student X is enrolled in course Y"
3. Direction: Directed (enrollment from student to course)
4. Weights: Credit hours or grade achieved
5. Time: Students enroll/drop each semester → temporal dynamics

## Common Pitfalls
- Assuming the graph model is "the reality" — it's always an abstraction with information loss
- Choosing nodes/edges without thinking about what question you want to answer
- Forgetting that the same real-world system can yield very different graph models depending on the question

## Connections
- [[directed-and-undirected-graphs]] — directionality of edges
- [[weighted-graphs]] — edges carrying numerical values
- [[bipartite-graphs]] — two disjoint node sets
- [[sparse-dense-and-random-graphs]] — quantitative graph differences
- [[graph-representations]] — how to store graphs computationally
- [[neighbourhood-and-degree]] — local node properties

## Open Questions
- When is a graph model "good enough"? What criteria determine the right abstraction?
- How do we handle the epistemic choice of modeling when multiple valid graph representations exist for the same system?
