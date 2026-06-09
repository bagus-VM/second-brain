---
title: "Balanced Triads"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: ["[[signed-graphs]]"]
---

## One-line Summary
In a signed graph, a triangle is balanced if it has an even number of negative edges (0 or 2); the (+, +, −) triangle with exactly one negative edge is the forbidden, psychologically unstable pattern.

## Core Intuition
There are exactly four possible sign patterns on a triangle. Two are "stable" (balanced), one is "unstable" (the forbidden type), and one is ambiguous. The intuition comes from Heider's psychology: if two people are friends and they both dislike a third, that feels coherent. If two people are friends but disagree about a third, that creates tension — one relationship must change. The (+, +, −) triangle is the only pattern with this direct contradiction.

## Formal Definition / Statement
Given a signed graph (G, σ), a triangle on nodes {u, v, w} with edge signs s₁, s₂, s₃ is:

| Triangle type | Signs | # negative | Balanced? |
|---|---|---|---|
| All positive | +, +, + | 0 | ✓ balanced |
| Two positive, one negative | +, +, − | 1 | ✗ **unbalanced** |
| One positive, two negative | +, −, − | 2 | ✓ balanced |
| All negative | −, −, − | 3 | ✗ under strong balance; ✓ under [[weak-structural-balance]] |

**Balance condition:** A triangle is balanced ⟺ it has an **even** number of negative edges.

Equivalently: the product of the three edge signs is +.

## Key Properties
- On a complete signed graph, triangle balance is necessary and sufficient for graph balance (Cartwright & Harary)
- On incomplete graphs, triangle balance alone is insufficient — must check all cycles (see [[frustration-index]])
- The (+, +, −) type is the *only* strongly-forbidden pattern — both strong and weak balance exclude it
- In random sign assignment, each type would appear ~25% of the time (or 12.5%/37.5%/37.5%/12.5% accounting for combinatorics)
- Empirically, (+, +, −) is massively underrepresented (~8% vs ~37.5% expected in Epinions)

## Worked Example
**Epinions data (Leskovec et al. 2010):**

| Triangle type | Expected (random) | Observed |
|---|---|---|
| +, +, + | ~12.5% | ~47% |
| +, +, − | ~37.5% | ~8% |
| +, −, − | ~37.5% | ~37% |
| −, −, − | ~12.5% | ~8% |

The forbidden (+, +, −) type occurs at ~1/5 of its expected rate. The all-positive type is ~4× overrepresented. This is strong evidence that triangle-level balance operates in real signed social networks, even though the global two-camp prediction cannot be directly tested on sparse data.

## Common Pitfalls
- Thinking balanced means "all positive" — a triangle with two negative edges is also balanced
- Confusing triangle balance with graph balance — on sparse graphs, all triangles can be balanced while longer cycles are not
- Forgetting the (−, −, −) ambiguity — it's forbidden under strong balance but allowed under weak balance
- Counting unbalanced triangles instead of computing the [[frustration-index]] — multiple unbalanced triangles may share an edge, so one flip can fix several

## Connections
- Local constraint in: [[structural-balance-theory]]
- Determines: [[balance-theorem]] (strong balance → 2 camps)
- Relaxed by: [[weak-structural-balance]] (permits −, −, −)
- Building block of: [[signed-graphs]]
- Measured empirically by: Leskovec et al. (2010) triangle census
- Connects to: [[clustering-coefficient]] — both examine triangle structure, but balance adds sign

## Open Questions
- Does the suppression of (+, +, −) vary across cultures or platforms?
- How does triangle balance interact with edge weight or relationship strength?
- Can triangle-level balance predict sign changes over time?
