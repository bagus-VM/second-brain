---
title: "Leiden Algorithm"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: ["[[louvain-algorithm]]", "[[modularity]]"]
---

## One-line Summary
Leiden improves Louvain by adding a refinement phase before aggregation — splitting weakly connected provisional communities so they aren't locked in as single super-nodes.

## Core Intuition
[[louvain-algorithm|Louvain]] can produce internally weak or disconnected communities because it collapses provisional groups into super-nodes without checking their structural integrity. Leiden (Traag et al., 2019) adds a **refinement step**: before aggregation, each provisional community is inspected and potentially split. If a community is held together only by a weak bridge, Leiden keeps its parts separate.

## Formal Definition / Statement
**Algorithm (Traag et al., 2019):**
1. **Local moving**: same as Louvain — improve Q with greedy node moves
2. **Refinement**: inspect each provisional community before aggregation. Start with its nodes as small sub-communities, then merge/move only if the sub-community remains well-connected and improves the quality function
3. **Aggregation**: collapse only the refined communities into super-nodes
4. **Repeat** on the coarser graph until modularity no longer improves

**Split effect**: if a Louvain community is held together only by a weak bridge, Leiden keeps its parts separate instead of collapsing them into one super-node.

## Key Properties / Complexity
- Preserves Louvain's near-linear scalability
- Prevents structurally broken communities from being locked in
- No fixed k — community count emerges from greedy moves + refinement
- Usually preferred in research pipelines over Louvain
- Still a heuristic — doesn't guarantee global modularity optimum

## Worked Example
Consider a provisional community found by Louvain's local moving phase: nodes {A, B, C, D} where A-B-C form a triangle and D is connected only via a single weak edge to C.
- **Louvain**: collapses {A,B,C,D} into one super-node
- **Leiden**: refinement checks connectivity → splits into {A,B,C} and {D}, then aggregates them separately

This prevents D from being permanently merged with the triangle.

## Common Pitfalls
- Leiden is still a modularity heuristic — inherits the resolution limit
- The refinement step adds computational overhead (but typically small)
- "Better than Louvain" doesn't mean "optimal" — the NP-hard barrier remains
- The quality function can be changed from modularity to other objectives (e.g., CPM)

## Connections
- [[louvain-algorithm]] — Leiden is Louvain + refinement
- [[modularity]] — both optimise Q (or variants)
- [[girvan-newman-algorithm]] — the divisive alternative
- [[community-detection-overview]] — Leiden is the recommended agglomerative method
- [[embedding-based-community-detection]] — alternative approach using node embeddings for overlapping communities
- [[modularity-resolution-limit]] — Leiden inherits modularity's resolution limit despite refinement
- [[hierarchical-clustering]] — multi-level aggregation produces an implicit hierarchy
- [[network-science-l04]] — lecture overview

## Open Questions
- How much does refinement improve partition quality empirically across different graph types?
- Can Leiden's refinement idea be applied to other quality functions beyond modularity?
