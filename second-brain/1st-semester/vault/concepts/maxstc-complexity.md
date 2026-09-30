---
title: "MaxSTC Complexity"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: ["[[strong-triadic-closure]]"]
---

## One-line Summary
Finding the edge labeling with the most strong edges that satisfies Strong Triadic Closure is NP-hard, forcing us to use polynomial-time structural proxies instead.

## Core Intuition
We observe the graph G but not the edge labels. We want to recover the labeling that best explains the structure — maximising strong edges subject to STC. This sounds like a clean optimization problem, but it turns out to be computationally intractable on general graphs. This is a fundamental modelling problem: the theoretical object we care about is out of reach, so we need approximations.

## Formal Definition / Statement
**MaxSTC Problem.** Given G = (V, E), find a labeling ℓ: E → {Strong, Weak} satisfying [[strong-triadic-closure|STC]] that maximizes |{e ∈ E : ℓ(e) = Strong}|.

**Decision version:** Given G and integer k, is there an STC-satisfying labeling with at least k strong edges?

**Complexity result (Sintos & Tsaparas, 2014):**
- MaxSTC is **NP-hard** as an optimization problem
- MaxSTC is **NP-complete** as a decision problem on general graphs
- Polynomial-time algorithms exist for restricted graph classes (e.g., cographs, some bipartite-like structures)

## Key Properties / Complexity
- The number of possible labelings is 2^|E| (exponential)
- Optimal labelings may not be unique — exponentially many optima possible
- Even restricted cases (planar, sparse) may not help unless the structure is very specific
- The NP-hardness is about *recovery from unlabeled data*, not about checking a given labeling

## Worked Example
Graph with 4 nodes: A, B, C, D. Edges: A–B, A–C, A–D, B–C.

- Total possible labelings: 2⁴ = 16
- At node A with 3 neighbours: if all 3 strong → forces B–D, C–D, B–C. Only B–C exists.
- Max 2 of A's ties strong, and they must be A–B, A–C (connected via B–C)
- B–C can also be strong → **3 strong edges maximum**
- Optimal labeling: ℓ(A–B) = ℓ(A–C) = ℓ(B–C) = S, ℓ(A–D) = W

## Common Pitfalls
- Confusing "NP-hard" with "impossible" — it means no known polynomial algorithm, not that approximate solutions are bad
- Thinking the graph "has" an STC labeling — the labeling is inferred, not observed
- Assuming MaxSTC intractability means the theory is useless — the *prediction* (weak-tie theorem) is still testable

## Connections
- Problem from: [[strong-triadic-closure]]
- Motivates: [[clustering-coefficient]] and [[neighborhood-overlap]] as tractable proxies
- Theoretical escape: [[weak-ties-hypothesis]] (derives testable prediction without solving MaxSTC)
- Reference: Sintos & Tsaparas, KDD 2014
- Part of: [[network-science-l03]]

## Open Questions
- For which real-world graph families is MaxSTC tractable?
- Can approximation algorithms guarantee a ratio to the optimal?
- Does the structure of social networks (small-world, power-law degree) make MaxSTC easier in practice?
