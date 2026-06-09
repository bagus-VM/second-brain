---
title: "Configuration Model"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
The configuration model generates random graphs with a prescribed degree sequence — the null model underlying [[modularity]].

## Core Intuition
To test whether a graph has community structure, we need a "random" comparison. The configuration model generates random graphs that preserve the degree sequence — the same number of nodes with the same degrees, but with edges rewired randomly. This isolates the effect of degree from the effect of community structure.

## Formal Definition / Statement
**Configuration model:**
1. Assign each node i a "stub count" k_i (its degree)
2. Randomly pair stubs until all stubs are matched
3. The resulting graph has the prescribed degree sequence but random edge placement

**Expected edge probability:**
P(edge between i and j) = k_i k_j / (2m)

where k_i, k_j are node degrees and m is the total number of edges.

**Use in modularity:**
[[modularity]] Q compares observed edges A_ij to expected edges k_i k_j / (2m) under the configuration model. Q is the surplus of within-community edges over this random expectation.

## Key Properties
1. **Preserves degree sequence**: the random graph has the same degrees as the original
2. **Null model**: isolates the effect of degree from community structure
3. **Expected edge probability**: k_i k_j / (2m) — proportional to the product of degrees
4. **Foundation of modularity**: Q compares observed to expected edges
5. **Multi-graph**: may produce self-loops or multi-edges (ignored in practice)

## Worked Example
Graph with 3 nodes: A (degree 2), B (degree 2), C (degree 2), m = 3 edges:

**Configuration model:**
- Assign stubs: A has 2 stubs, B has 2 stubs, C has 2 stubs
- Randomly pair stubs: possible pairings include (A-B, A-B, C-C), (A-B, A-C, B-C), etc.
- Expected edge probability: P(A-B) = 2×2 / 6 = 2/3

**Modularity:**
- Observed: A-B edge exists (A_ij = 1)
- Expected: k_A k_B / 2m = 2×2 / 6 = 2/3
- Surplus: 1 - 2/3 = 1/3

## Common Pitfalls
1. **Confusing with Erdős–Rényi**: Erdős–Rényi fixes edge probability, not degree sequence
2. **Ignoring that the configuration model produces multi-graphs**: self-loops and multi-edges are possible
3. **Assuming the configuration model is the only null model**: other null models exist for different contexts
4. **Over-interpreting the expected edge probability**: it's a random expectation, not a deterministic prediction

## Connections
- [[modularity]] — uses the configuration model as the null model
- [[community-detection]] — the overarching problem
- [[network-science-l04]] — lecture overview

## Open Questions
- How does the configuration model perform on directed or weighted graphs?
- Can we use other null models for modularity?
- How does the configuration model relate to other random graph models?
