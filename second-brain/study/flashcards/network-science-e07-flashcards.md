---
title: "Network Science E07 — Structural Balance Flashcards"
tags:
  - flashcards
  - network-science
  - semester-1
course: "Network Science"
status: current
last_updated: 2026-06-14
---

# Flashcards — Exercise Sheet 7 (Structural Balance)

> [!question]- When is a signed triangle balanced?
> [!answer]- A signed triangle is balanced if the product of its edge signs is positive, i.e., it has an even number of negative edges (0 or 2). The four possibilities: (+,+,+) balanced, (+,+,-) unbalanced, (+,-,-) balanced, (-,-,-) unbalanced in strong balance but balanced in weak balance.

> [!question]- What is the "most unstable" signed triangle?
> [!answer]- (+, +, -): the "two friends, one enemy" pattern. This creates cognitive dissonance (Heider 1946) and is massively underrepresented in real signed networks — about 8% of triangles, vs ~37.5% expected from random signing.

> [!question]- What is the Balance Theorem?
> [!answer]- Cartwright & Harary (1956): a complete signed graph is balanced iff its nodes can be partitioned into at most two camps, such that within-camp edges are positive and between-camp edges are negative. The local triangle rule forces this global structure.

> [!question]- What is the difference between strong and weak balance?
> [!answer]- **Strong balance** (Heider, Cartwright-Harary): only (+,+,+) and (+,-,-) are balanced; forces ≤ 2 camps. **Weak balance** (Davis 1967): adds (-,-,-) as balanced; only (+,+,-) is forbidden; permits k ≥ 1 camps. Weak balance models multipolar systems (e.g., post-1969 Cold War).

> [!question]- What is the frustration index of a signed graph?
> [!answer]- The minimum number of edge sign flips needed to make the graph perfectly balanced. F(G, σ) = min over balanced signings σ' of |{edges where σ(e) ≠ σ'(e)}|. NP-hard to compute exactly. Normalized form: f = F / |E|; f ≈ 0 means near-balanced, f ≈ 0.5 means random.

> [!question]- What does the cycle criterion state for balance?
> [!answer]- On a (possibly incomplete) signed graph, balance is equivalent to: *every cycle has an even number of negative edges*. This generalises the triangle test (a triangle is a 3-cycle) to arbitrary graph topology.

> [!question]- How does the signed Laplacian detect balance?
> [!answer]- The signed Laplacian L_σ = D - A_σ (where A_σ has +1 for positive, -1 for negative edges). λ₁(L_σ) = 0 iff the graph is balanced. Polynomial-time computation, in contrast to NP-hard frustration index.

> [!question]- How did balance theory explain the WWI alliance network?
> [!answer]- The WWI alliance network (Allies vs Central Powers) was *perfectly balanced* under the strong balance theorem: two camps, all within-camp positive, all between-camp negative. Italy's 1915 switch from the Central Powers to the Allies is consistent with balance theory: realigning to reduce tension after one camp became more attractive.

> [!question]- How do you measure "approximate balance" in real networks like the karate club?
> [!answer]- Sign edges by faction (within = +, cross = -). Count the fraction of balanced triangles (even number of -). Empirically, this is ~0.7-0.8 for the karate club, far above the 0.5 expected from random signing. Removing the cross-faction edges that participate in the most unbalanced triangles increases the fraction further.

> [!question]- What is the k-balance generalisation?
> [!answer]- A k-balance structure: k mutually hostile camps, positive edges within each camp, negative edges between camps. Strong balance = k ≤ 2; weak balance = arbitrary k ≥ 1. k = 1 is all-positive; k = n is all-negative.

> [!question]- What is the "two-camp" interpretation of structural balance?
> [!answer]- The Balance Theorem says: if every triangle in a complete signed graph is balanced, the nodes can be split into at most two camps (one camp could be empty if the graph is all-positive). The proof: pick any node v, partition into v's friends and v's enemies. Triangle balance forces all friends to be friends with each other and all enemies with each other, and friends/enemies to be opposed.

> [!question]- Why is the frustration index NP-hard?
> [!answer]- Computing the minimum number of edge sign flips to achieve balance is equivalent to finding the maximum cut of a related graph (a classical NP-hard problem). In practice, approximation algorithms and spectral methods (signed Laplacian) are used.
