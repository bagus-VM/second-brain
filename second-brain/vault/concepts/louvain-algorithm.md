---
title: "Louvain Algorithm"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: ["[[modularity]]"]
---

## One-line Summary
Louvain is a fast greedy heuristic for modularity maximization that alternates between local node moves and community aggregation until Q stops improving.

## Core Intuition
Start with each node as its own community. Visit each node and move it to the neighboring community that most increases [[modularity]] ΔQ. Once no more moves help, collapse each community into a super-node and repeat on the coarser graph. The number of communities k is not pre-given — it emerges from the greedy moves.

## Formal Definition / Statement
**Algorithm (Blondel et al., 2008):**
1. **Initialization**: k = n communities (each node alone)
2. **Local moving**: for each node v, test moving v to neighboring communities; accept if ΔQ > 0
3. **Aggregation**: collapse each community into a super-node; edges become weighted edges between super-nodes
4. **Repeat** steps 2–3 on the coarser graph until modularity no longer improves

**Candidate communities** for node v: the current communities of v's neighbors, plus v's current community.

**Complexity**: near-linear in m empirically — much faster than [[girvan-newman-algorithm]]'s O(|V|·|E|²).

## Key Properties
- No pre-given k needed — community count emerges from greedy decisions
- Scalable to graphs with millions of nodes and edges
- Produces a hierarchy of aggregation levels
- Results can depend on node visit order (greedy, non-deterministic)
- Inherits modularity's **resolution limit** — may merge small communities

## Worked Example
On a graph with 3 communities:
- Pass 1: nodes move to form local triangles; each triangle becomes a community
- Pass 2: super-nodes (triangles) are connected; the algorithm checks if merging any pair of super-nodes increases Q
- If merging doesn't help, the algorithm stops with 3 communities

## Common Pitfalls
- Louvain is greedy — different node orderings can yield different partitions
- Can produce internally weak or disconnected communities because it aggregates without refinement
- Resolution limit: small communities in large graphs may be merged into larger ones
- Not guaranteed to find the global modularity optimum (NP-hard)
- The aggregation step can "lock in" bad early decisions — this is what [[leiden-algorithm]] fixes

## Connections
- [[modularity]] — Louvain optimizes Q via greedy local moves
- [[leiden-algorithm]] — Leiden adds a refinement phase to fix Louvain's disconnected-community problem
- [[girvan-newman-algorithm]] — the divisive alternative; much slower but more principled
- [[hierarchical-clustering]] — Louvain produces multi-level aggregation (implicit hierarchy)
- [[community-detection-overview]] — Louvain is the standard agglomerative method in practice
- [[embedding-based-community-detection]] — alternative approach using node embeddings for overlapping communities
- [[modularity-resolution-limit]] — Louvain inherits modularity's inability to detect small communities
- [[configuration-model]] — null model underlying modularity
- [[network-science-l04]] — lecture overview

## Open Questions
- How sensitive are Louvain results to node ordering in practice?
- Can Louvain be adapted for overlapping communities?
- How does the resolution limit affect real-world analyses?
