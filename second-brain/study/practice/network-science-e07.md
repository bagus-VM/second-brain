---
title: "Exercise Sheet 7 — Structural Balance"
tags:
  - practice
  - network-science
  - semester-1
course: "Network Science"
status: current
last_updated: 2026-06-14
---

# Exercise Sheet 7 — Structural Balance

## Exercises

### 7.A Triadic Balance Theory

**Exercise 7.A.1: Classifying Signed Triangles**

For each triangle, determine if balanced (B) or unbalanced (U). A triangle is balanced if the product of its edge signs is positive (even number of negative edges).

1. (+, +, +) — **B** (the "all friends" pattern; no tension)
2. (+, +, −) — **U** (the "two friends, one enemy" pattern; classic tension)
3. (+, −, −) — **B** ("enemy of my enemy is my friend" pattern; in the strong-balance sense this is balanced)
4. (−, −, −) — **U** (in strong balance; "three mutual enemies" cannot coexist; in weak balance this is **B**)

**Most stable pattern**: (+, +, +) — mutual friends, no tension.
**Most "socially unstable"**: (+, +, −) — the classic "enemy of my friend is my enemy" tension, which Heider identified as the source of cognitive dissonance.

### 7.B Weak Balance

**Exercise 7.B.1: Strong vs Weak Balance**

For the two triangles (A, B, C all positive; D, E, F all negative) connected by a negative edge C-D:

- **Triangle (A, B, C) with all positive edges**: balanced under both strong and weak balance (4 negative edges is even, so balanced in both). ✓
- **Triangle (D, E, F) with all negative edges**: 
  - **Strong balance**: unbalanced (3 negative edges is odd)
  - **Weak balance**: balanced (weak balance only forbids the (+, +, −) pattern; all-negative is allowed)
- **Global partition under strong balance**: a single partition into two camps: {A, B, C} vs {D, E, F} (with the negative C-D edge separating them). Under strong balance, all 6 nodes must fit into at most 2 camps.
- **Global partition under weak balance**: {A, B, C}, {D, E, F} is one valid partition; alternatively, all 6 nodes could be in separate "enemy" camps (no requirement for positive within). The structure is more flexible.
- **International relations meaning of all-negative triangle**: three countries that all mutually hate each other. Under strong balance, this is impossible (it would violate the two-camp structure); under weak balance, it represents a "tripolar" or "multipolar" world.

**Exercise 7.B.2: Finding Camps in a Signed Network**

Graph: 1, 2, 3 mutually friends (+); 4, 5, 6 mutually friends (+); all cross-group edges are negative.

1. **All triangles balanced?** The within-group triangles (1,2,3) and (4,5,6) are all positive, balanced. The cross-group triangles (e.g., 1, 2, 4 with edges +, -, -) have two negatives, balanced. So yes, all triangles are balanced.

2. **Two-camp partition**: {1, 2, 3} vs {4, 5, 6}. All within-group edges positive, all cross-group edges negative.

3. **Within-group positive, between-group negative**: confirmed.

4. **Adding a "rogue" positive edge 1-4**: triangle (1, 4, 5) now has edges +, +, - (the new 1-4 is +, the existing 4-5 is +, the existing 1-5 is -). This is the (+, +, -) forbidden pattern → unbalanced. Similarly, triangles (1, 4, 6), (2, 4, 5), (2, 4, 6), (3, 4, 5), (3, 4, 6) all become unbalanced. The network is no longer perfectly balanced.

### 7.C Relaxed Balance and Applications

**Exercise 7.C.1: WWI Alliance Network**

Allies: France, Britain, Russia (mutually +); Central Powers: Germany, Austria-Hungary (mutually +); all Allies-Central edges negative.

1. **Is the network perfectly balanced?** Yes, by the two-camp partition {Allies} vs {Central Powers}.
2. **Match the two-camp Balance Theorem?** Yes — exactly two camps, all within-camp edges positive, all between-camp edges negative.
3. **New country joining with positive ties to both camps**: this would create (+, +, -) triangles. E.g., if Italy joins and is friends with both France and Germany, then triangle (Italy, France, Germany) has +, +, - edges → unbalanced. The network becomes frustrated.
4. **Italy switching from Germany to Allies in 1915**: this is *selection* / *realignment* — Italy was a former Central Power ally but switched sides. Under balance theory, this is exactly what you'd predict: an actor with conflicted ties to both camps will eventually align with one to reduce tension. Italy's switch is consistent with balance theory.

**Exercise 7.C.2: Approximate Balance in Real Networks**

Using the karate club graph, sign edges by faction (within = +, cross = -).

1. **Count balanced vs unbalanced triangles**: the original Zachary karate club graph has 78 triangles total. With faction-based signing, you'd count how many are balanced (even number of -) vs unbalanced (odd number of -).
2. **Fraction balanced**: empirically, this is typically ~0.7-0.8 for the karate club — far above the 0.5 expected from random signing.
3. **Removing top-5 cross-faction edges**: the fraction increases further (some cross-faction edges participate in many unbalanced triangles; removing them helps).
4. **Plot fraction-balanced vs edges-removed**: shows a generally increasing trend, possibly with bumps. Used to identify "bridge" edges between factions.

## Wrap-Up

- Triangle sign products give a one-line balance test
- The Balance Theorem turns a local rule into a global two-camp partition
- Weak balance permits more than two camps and is often more realistic
- Real networks are rarely perfectly balanced — approximate balance is the typical regime

## Related Lectures
- [[network-science-l06]]
- [[balance-theorem]]
- [[structural-balance-theory]]
- [[balanced-triads]]
- [[weak-structural-balance]]
- [[signed-networks]]
- [[frustration-index]]
- [[cycle-criterion]]
- [[signed-laplacian]]
