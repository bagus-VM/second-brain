---
title: "Min-Cut Max-Flow"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
Min-cut / Max-flow finds the smallest set of edges whose removal disconnects two specified groups — exact in polynomial time, but minimizes raw cut size, not normalized density.

## Core Intuition
The min-cut problem asks: what is the smallest set of edges we can remove to disconnect the graph into two components? The max-flow problem asks: what is the maximum flow we can send from a source to a sink? These are dual problems — the min-cut equals the max-flow (Ford-Fulkerson theorem).

## Formal Definition / Statement
**Min-cut:**
Given a graph G = (V, E) and two nodes s and t, find the smallest set of edges whose removal disconnects s from t.

**Max-flow:**
Given a graph G = (V, E) with edge capacities, find the maximum flow from s to t.

**Ford-Fulkerson theorem:**
The maximum flow from s to t equals the minimum cut separating s and t.

**Time complexity:** O(m × max_flow) for the basic Ford-Fulkerson algorithm; O(nm) for more efficient variants.

**Limitation:** minimizes raw cut size, not normalized density. This means the min-cut may be trivially small (cutting off a single node).

## Key Properties
1. **Exact**: finds the true minimum cut
2. **Polynomial time**: efficient algorithms exist
3. **Raw cut size**: doesn't account for cluster size
4. **Trivial solutions**: may cut off a single node (not a meaningful community)
5. **Foundation for other methods**: [[normalized-cut]] and [[conductance]] fix the raw-cut limitation

## Worked Example
Graph with two dense clusters connected by a few edges:

**Min-cut:** removes the 3 edges connecting the clusters → disconnects the graph
**Problem:** if one cluster is much larger than the other, the min-cut may cut off a single node (trivial solution)

**Normalized cut:** divides the cut size by cluster volumes → prevents trivial solutions.

## Common Pitfalls
1. **Confusing min-cut with community detection**: min-cut finds the smallest cut, not the best communities
2. **Ignoring that min-cut favors small clusters**: the raw cut size doesn't account for cluster size
3. **Assuming min-cut is always meaningful**: a single node can be a trivial min-cut
4. **Forgetting that min-cut requires specifying s and t**: it's not a global community-detection method

## Connections
- [[normalized-cut]] — fixes the raw-cut limitation
- [[conductance]] — related normalized measure
- [[spectral-partitioning]] — alternative partitioning method
- [[community-detection]] — the overarching problem
- [[network-science-l04]] — lecture overview

## Open Questions
- How does min-cut perform on directed or weighted graphs?
- Can we use min-cut for community detection without specifying s and t?
- How does min-cut relate to network robustness?
