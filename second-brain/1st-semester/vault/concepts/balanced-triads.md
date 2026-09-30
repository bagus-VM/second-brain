---
title: "Balanced Triads"
tags: [concept, network-science, semester-1, structural-balance, signed-networks, triangles]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[signed-networks]]", "[[balance-theorem]]", "[[structural-balance-theory]]"]
---

## One-line Summary
A balanced triad is a signed triangle with an even number of negative edges (0 or 2) — the local rule that, when applied to every triangle in a complete signed graph, forces the global [[balance-theorem|balance theorem's]] two-camp partition.

## Core Intuition
There are only four possible signed triangles (counting the number of negative edges): 0, 1, 2, or 3 negatives. Heider's intuition: a triangle with 0 or 2 negatives is "balanced" — no cognitive tension. A triangle with 1 or 3 negatives is "unbalanced" — creates psychological discomfort.

The single-negative pattern (+, +, −) is the classic source of tension: "the friend of my friend is my enemy" — a contradiction. The three-negative pattern (−, −, −) is the "three mutual enemies" — under strong balance, this is unbalanced; under [[weak-structural-balance|weak balance]], it's allowed.

## Formal Definition / Statement

For a signed triangle (three nodes A, B, C with signs σ(A,B), σ(B,C), σ(A,C)):

| Number of negatives | Sign pattern | Strong balance | Weak balance |
|---------------------|--------------|----------------|--------------|
| 0 | (+, +, +) | balanced | balanced |
| 1 | (+, +, −) | unbalanced | unbalanced |
| 2 | (+, −, −) | balanced | balanced |
| 3 | (−, −, −) | unbalanced | balanced |

**Equivalent definition**: a triangle is balanced iff the product of its edge signs is positive: σ(A,B) × σ(B,C) × σ(A,C) > 0.

**Balance test (complete graph)**: scan all C(n, 3) triangles; the graph is balanced iff all are balanced. Time: O(n³).

**Balance test (general graph)**: see [[cycle-criterion]] — every cycle must have an even number of negative edges.

## Key Properties / Complexity

### The four patterns
- **(+ ,+, +) "all friends"**: trivially balanced. No conflict. The "ideal" state.
- **(+ ,+, −) "two friends, one enemy"**: the unstable pattern. Source of cognitive dissonance. The enemy of my friend should be my friend, not my enemy.
- **(+ ,−, −) "enemy of my enemy is my friend"**: balanced. Alice and Bob are friends; both are enemies of Carol. No tension: Alice and Bob share an enemy, which makes them closer.
- **(− ,−, −) "three mutual enemies"**: unbalanced in strong balance; balanced in weak balance. Strong balance forces ≤ 2 camps, so three mutual enemies can't coexist. Weak balance allows this (k ≥ 1 camps).

### Empirical evidence
In real signed networks (Epinions, Slashdot, Wikipedia — Leskovec et al. 2010):
- (+, +, +): ~47% of triangles (vs ~12.5% expected from random) — overrepresented
- (+, +, −): ~8% of triangles (vs ~37.5% expected from random) — massively underrepresented
- (+, −, −): ~32% (vs ~37.5% expected) — slightly underrepresented
- (−, −, −): ~13% (vs ~12.5% expected) — about as expected

The underrepresentation of (+, +, −) is the strongest empirical support for balance theory.

### Why this matters
The local rule "all triangles balanced" is equivalent (via the [[balance-theorem|Balance Theorem]]) to the global structure "≤ 2 camps". This is an example of a *local-to-global* emergence: a simple local rule produces a specific global structure. The same pattern appears in many network phenomena:
- **Schelling segregation**: local preference for same-type neighbours produces global segregation
- **Ising model**: local spin-spin interactions produce global magnetisation
- **Cellular automata**: local rules produce global patterns (Conway's Game of Life)

## Worked Example

A complete signed graph with 4 nodes:
```
A -- B: +    (allies)
A -- C: +    (allies)
A -- D: −    (rivals)
B -- C: +    (allies)
B -- D: −    (rivals)
C -- D: −    (rivals)
```

Triangles:
- {A, B, C}: +, +, + → 0 negatives → **balanced** ✓
- {A, B, D}: +, −, − → 2 negatives → **balanced** ✓
- {A, C, D}: +, −, − → 2 negatives → **balanced** ✓
- {B, C, D}: +, −, − → 2 negatives → **balanced** ✓

All triangles balanced. Two-camp partition: {A, B, C} vs {D}. Within {A, B, C}: all positive. Within {D}: trivially positive (single node). Between camps: all negative. ✓

## Common Pitfalls
- **"Balanced" means an even number of negatives, not "all positive"**. A triangle with two negatives is just as balanced as one with zero.
- **Strong vs weak balance changes the answer for the all-negative triangle**. Davis's 1967 weak balance is the more empirically accurate model.
- **The local rule is easy to check; the global structure is harder to derive**. The Balance Theorem says they're equivalent, but the *proof* is the interesting part.
- **Empirical evidence is at the triangle level, not the global level**. Real networks are too sparse to test the global two-camp partition. We can verify the local rule (no (+, +, −) triangles) but not the global implication (two-camp structure).
- **A triangle with one negative is the *most* unstable pattern**. It's the source of cognitive dissonance. Don't confuse with the all-negative triangle (unstable only in strong balance).

## Connections
- [[signed-networks]] — the general topic
- [[balance-theorem]] — the global consequence
- [[structural-balance-theory]] — Heider's psychological theory
- [[weak-structural-balance]] — Davis's relaxation
- [[k-balance]] — k-camp generalisation
- [[cycle-criterion]] — for non-complete graphs
- [[frustration-index]] — measuring approximate balance
- [[network-science-l06]] — the lecture

## Open Questions
- Why is the (+, +, −) triangle empirically rare? Is it because people actively avoid it, or because the network evolved to exclude it?
- Does the local triangle rule *cause* the global two-camp structure, or does the global structure *cause* the local triangle rule? (Causality direction in real social networks.)
- Are there other local rules (beyond "even number of negatives") that produce interesting global structures?
