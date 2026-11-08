---
title: "Kernighan-Lin Algorithm"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
Kernighan-Lin is a local-search algorithm for balanced graph partitioning — iteratively swap node pairs to decrease the cut size until convergence to a local optimum.

## Core Intuition
Start with a random balanced 2-partition. At each step, find the pair of nodes whose swap most decreases the cut size. Swap them and repeat until no beneficial swap exists. The algorithm converges to a local optimum.

## Formal Definition / Statement
**Algorithm:**
1. Initialize a balanced 2-partition at random
2. For each pair of nodes (one from each side), compute the gain from swapping them
3. Swap the pair with the highest gain (even if the gain is negative)
4. Repeat until no beneficial swap exists

**Gain computation:**
For node u in partition A and node v in partition B:
- D(u) = external edges of u - internal edges of u
- D(v) = external edges of v - internal edges of v
- Gain(u,v) = D(u) + D(v) - 2 × A(u,v)

**Time complexity:** O(n²) per pass.

**Limitation:** converges to a local optimum; different initial partitions yield different results.

## Key Properties / Complexity
1. **Local search**: iteratively improves a candidate solution
2. **Balanced partition**: maintains equal-sized partitions
3. **Fast in practice**: O(n²) per pass is manageable for moderate graphs
4. **Local optimum**: different initializations yield different results
5. **Fixed k**: requires specifying the number of partitions in advance

## Worked Example
Graph with 6 nodes, initial partition: {A,B,C} vs. {D,E,F}:

**Step 1:** compute gain for all pairs:
- Swap (A,D): gain = 2
- Swap (B,E): gain = 1
- Swap (C,F): gain = 0

**Step 2:** swap (A,D) — highest gain.

**Step 3:** recompute gains. Swap (B,E) — gain = 1.

**Step 4:** no more beneficial swaps — algorithm terminates.

**Result:** partition {D,B,C} vs. {A,E,F} with cut size reduced from 5 to 3.

## Common Pitfalls
1. **Local optimum**: different initializations yield different results
2. **Fixed k**: must specify the number of partitions in advance
3. **Balanced constraint**: may prevent finding the optimal partition
4. **Expensive for large graphs**: O(n²) per pass is too slow for millions of nodes

## Connections
- [[spectral-partitioning]] — alternative partitioning method
- [[normalized-cut]] — alternative partition objective
- [[conductance]] — related community quality measure
- [[community-detection]] — the overarching problem
- [[graph-partitioning]] — Kernighan-Lin is a core method for balanced graph partitioning
- [[network-science-l04]] — lecture overview

## Open Questions
- How does Kernighan-Lin compare to spectral methods on specific graph types?
- Can we extend Kernighan-Lin to k > 2 partitions?
- How does Kernighan-Lin perform on graphs with community structure?
