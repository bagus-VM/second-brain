---
title: "Strong Triadic Closure (STC)"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: ["[[triadic-closure]]"]
---

## One-line Summary
If a node has two strong ties, Strong Triadic Closure requires those endpoints to be connected — making it a constraint on edge labelings, not just a graph property.

## Core Intuition
Plain [[triadic-closure]] says open triads tend to close. STC goes further: it introduces a *type system* for edges (strong vs. weak) and says that strong ties impose a stronger closure pressure. If A has strong ties to both B and C, then B–C must exist. The label of B–C doesn't matter — just its existence. This makes STC a constraint on which edge labelings are valid, not a property of the graph itself.

## Formal Definition / Statement
**Edge labeling.** Given a graph G = (V, E), a labeling is a function ℓ: E → {Strong, Weak}. We write S(v) for the set of strong neighbours of node v under ℓ.

**Strong Triadic Closure (STC).** A labeling ℓ satisfies STC if, for every node v and every pair u₁, u₂ ∈ S(v) of strong neighbours of v, the edge (u₁, u₂) exists in E — with any label (Strong or Weak).

Key point: STC constrains which pairs *must be connected*, not how the closing edge is labeled. The question "does the graph satisfy STC?" is ill-posed — the right question is "which labelings of this graph satisfy STC?"

## Key Properties / Complexity
- STC is a property of a *labeling*, not of a graph
- The same graph can admit both valid and invalid STC labelings
- If a node has only one strong tie, STC imposes no constraint
- If a node has ≥ 2 strong ties, all pairs among those strong neighbours must be connected
- The closing edge can be Strong or Weak — STC doesn't care

## Worked Example
**Graph:** Nodes A, B, C, D with edges A–B, A–C, A–D, B–C. No other edges.

**Finding max STC labeling:**
- At node A, making all 3 ties strong forces B–D, C–D, B–C to exist. Only B–C exists, so at most 2 of A's ties can be strong.
- The two strong ties must be A–B and A–C (whose endpoints are connected via B–C).
- Edge B–C can be strong (no further constraint violated).
- **Optimal:** ℓ(A–B) = ℓ(A–C) = ℓ(B–C) = Strong, ℓ(A–D) = Weak → 3 strong edges (maximum).

## Common Pitfalls
- Asking "does this graph satisfy STC?" — STC is about labelings, not graphs
- Assuming the closing edge must be Strong — STC only requires it to *exist*
- Thinking STC is just triadic closure with a label — the label constraint changes what's required
- Forgetting that a node with only 1 strong tie has no STC obligation

## Connections
- Extends: [[triadic-closure]] (adds edge typing)
- Leads to: [[maxstc-complexity]] (finding optimal labeling is NP-hard)
- Enables: [[weak-ties-hypothesis]] (STC → local bridges must be weak)
- Proxied by: [[clustering-coefficient]] and [[neighborhood-overlap]]
- Part of: [[network-science-l03]] lecture

## Open Questions
- Can STC be extended to weighted edges with a threshold for "strong"?
- How robust is STC to measurement noise in tie-strength estimation?
- Are there tractable special cases beyond cographs where MaxSTC is polynomial?
