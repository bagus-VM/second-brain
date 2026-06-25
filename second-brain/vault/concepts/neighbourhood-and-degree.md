---
title: "Neighbourhood and Degree"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [graph-fundamentals]
---

## One-line Summary
==The neighbourhood N(v) of a node is the set of its directly connected neighbors==; the degree deg(v) counts how many edges are incident to it.

## Core Intuition
Degree is the simplest measure of a node's local connectivity. ==A person with 500 social connections has degree 500==. A web page linked by 1000 other pages has in-degree 1000. These local properties aggregate into global patterns like degree distribution, which characterizes the entire network.

## Formal Definition / Statement
- **Neighbourhood**: N(v) = {u ∈ V : {u, v} ∈ E} — the set of all nodes connected to v by an edge
- **Degree**: deg(v) = |N(v)| — the number of edges incident to v (in simple graphs)
- For directed graphs:
  - **In-degree**: number of edges pointing to v
  - **Out-degree**: number of edges pointing from v

## Key Properties
- In an undirected graph, every edge contributes to the degree of both endpoints
- **Handshaking lemma**: Σ deg(v) = 2|E| — the sum of all degrees equals twice the number of edges
- Average degree = 2|E| / |V|
- Degree is a local property; the degree distribution is a global property (covered in later lectures)
- In [[bipartite-graphs|bipartite graphs]], degree counts cross-set connections

## Worked Example
For the graph with edges A-B, B-C, C-D, D-A, A-C:
- N(A) = {B, C, D}, deg(A) = 3
- N(B) = {A, C}, deg(B) = 2
- N(C) = {B, D, A}, deg(C) = 3
- N(D) = {C, A}, deg(D) = 2
- Sum of degrees = 3+2+3+2 = 10 = 2 × 5 edges ✓

## Common Pitfalls
- Confusing degree with the number of edges — degree counts edges incident to one node, not total edges
- Forgetting that in directed graphs, in-degree and out-degree are separate concepts
- Assuming high degree means "important" — degree is just one measure of centrality (covered later)

## Connections
- [[graph-fundamentals]] — degree is a fundamental node property
- [[directed-and-undirected-graphs]] — in-degree and out-degree for directed graphs
- [[graph-representations]] — adjacency list directly stores N(v)
- [[sparse-dense-and-random-graphs]] — average degree relates to graph density
- [[bipartite-graphs]] — degree in bipartite graphs counts cross-set connections

## Open Questions
- How does the degree distribution (not just individual degree) characterize a network?
- What happens when we consider higher-order neighborhoods (friends of friends)?
