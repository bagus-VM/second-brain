---
title: "Exercise Sheet 3 — Strong and Weak Ties"
tags:
  - practice
  - network-science
  - semester-1
course: "Network Science"
status: current
last_updated: 2026-06-02
---

# Exercise Sheet 3 — Strong and Weak Ties

## Exercises

### 3.A Triadic Closure

**Exercise 3.A.1: Open Triads and Predicted Closures**

Consider the following friendship network (all edges are strong ties unless stated otherwise):
Edges: A–B, A–C, A–D, B–C, D–E, E–F, D–F.

1. List all open triads in the network.
2. For each open triad, which missing edge is predicted to appear by triadic closure? Rank them by "closure pressure".
3. Which open triad, if closed, would increase the clustering coefficient of node A the most?
4. Node G joins and forms strong ties with A and D. Predict which edge forms next.

---

**Exercise 3.A.2: Computing Clustering Coefficients**

For the graph: A–B, A–C, A–D, B–C, D–E, E–F, D–F:

1. Compute the local clustering coefficient C_v for every node.
2. Compute the average clustering coefficient C̄.
3. Interpret the result: what does it tell us about the network?
4. Visualise the graph with nodes coloured by C_v.

### 3.B Bridges and Brokers

**Exercise 3.B.1: Finding Bridges and Structural Holes**

Three cliques: {1, 2, 3}, {4, 5, 6}, and {7, 8, 9}. Bridges: 3–4 and 6–7.

1. Is 3–4 a bridge? Is 6–7 a bridge?
2. Is 3–4 a local bridge?
3. Node 5 in Clique 2 connects to Cliques 1 and 3. Does it sit in a structural hole?
4. If node 3 forms a direct edge with node 7, what happens to the hole and the bridges?

---

**Exercise 3.B.2: Identifying Bridges with NetworkX**

Build the three-clique graph in NetworkX. Identify bridges and rank edges by edge betweenness.

### 3.C Weak Ties Theorem

**Exercise 3.C.1: Verifying the Weak-Ties Theorem**

Weak-Ties Theorem: Under Strong Triadic Closure (STC), every local bridge is a weak tie.

Check STC and local bridges for:
- **A:** Strong 1–2, 1–3. Weak 2–4. No 2–3.
- **B:** Strong 1–2, 1–3, 2–3. Weak 1–4.
- **C:** Strong 1–2, 2–3, 1–3, 3–4, 2–4.

---

**Exercise 3.C.2: Granovetter's Job Study**

1. Why are rarely-seen acquaintances more useful for job finding than close friends?
2. Apply the weak-ties theorem to redundant vs. novel information.
3. Is "unfriending all close friends" good advice based on the theorem?
4. How does LinkedIn fit this framework?

### 3.D Evidence and Overlap

**Exercise 3.D.1: Neighbourhood Overlap Calculation**

O(u, v) = |N(u) ∩ N(v)| / |N(u) ∪ N(v)| (excluding u and v from N)

For edges: A–B, A–C, A–D, B–C, B–E, C–F:

1. Compute O(A, B), O(A, C), and O(B, E).
2. Rank them. Which is most like a local bridge?

---

**Exercise 3.D.2: Neighbourhood Overlap in NetworkX**

Compute average neighborhood overlap within and across factions in the karate club.

### 3.E Tie Strength in Practice

**Exercise 3.E.1: Tie Strengths in Practice**

1. Facebook (symmetric) vs. Twitter (asymmetric): structural implications for overlap?
2. Why do maintained relationships grow slowly while total count grows quickly?
3. How should you design a recommender for information diversity?

---

**Exercise 3.E.2: Simulating Tie Strength and Overlap**

Assign synthetic strength values to karate-club edges (within-faction strong, across-faction weak) and compute the correlation with neighborhood overlap.

---

## Solutions

### 3.A.1 — Open Triads and Predicted Closures

> [!note]- Solution
> 1. **Open triads:** (B, A, D), (C, A, D), (A, D, E), (A, D, F).
> 2. **Ranking:** Each missing edge is supported by exactly one open triad, so all have equal closure pressure.
> 3. **A's clustering:** B−D or C−D. They tie.
> 4. **Node G:** G, A, and D form a closed triad immediately (since A–D exists). G will likely next close triads with neighbours of A (B, C) or D (E, F).

### 3.A.2 — Computing Clustering Coefficients

> [!note]- Solution
> 1. Local coefficients: C_B, C_C, C_E, C_F = 1 (their neighbours are all connected). C_A = 1/3 (neighbours B, C, D; only B–C connected). C_D = 1/3 (neighbours A, E, F; only E–F connected).
> 2. C̄ = (1 + 1 + 1 + 1 + 1/3 + 1/3)/6 = 14/18 = 7/9 ≈ 0.78.
> 3. C̄ ≈ 0.78 is high, indicating a "cliquey" social structure where friends of friends are likely to be friends.

### 3.B.1 — Finding Bridges and Structural Holes

> [!note]- Solution
> 1. **Bridges:** Yes. Removing either disconnects the graph into separate cliques (components).
> 2. **Local Bridge:** Yes. Nodes 3 and 4 have no common neighbours besides each other.
> 3. **Structural Hole:** Clique 1 and Clique 3 have no direct connection. Node 5 (via 4 and 6) can broker information between these disjoint worlds, gaining an information advantage.
> 4. **Edge 3–7:** The structural hole closes. Edge 6–7 is no longer a bridge because an alternative path (via 3–7) now exists.

### 3.B.2 — Identifying Bridges with NetworkX

> [!note]- Solution
> ```python
> import networkx as nx
> G = nx.Graph()
> G.add_edges_from([(1,2),(1,3),(2,3),(4,5),(4,6),(5,6),(7,8),(7,9),(8,9),(3,4),(6,7)])
> bridges = list(nx.bridges(G))
> # [(3,4), (6,7)]
> ebc = nx.edge_betweenness_centrality(G)
> ```
> **High Betweenness:** Bridges (3,4) and (6,7) carry all traffic between cliques, giving them maximum edge betweenness. **Vulnerability:** Removing these edges fragments the network faster than removing internal clique edges.

### 3.C.1 — Verifying the Weak-Ties Theorem

> [!note]- Solution
> - **A:** STC Violated (1 tied to 2 and 3, but no 2–3 edge). Theorem premise doesn't hold.
> - **B:** STC Satisfied. Edge 1–4 is a local bridge and is weak. Theorem holds.
> - **C:** STC Violated (2 tied to 1 and 4, but no 1–4 edge). Theorem doesn't apply.

### 3.C.2 — Granovetter's Job Study

> [!note]- Solution
> 1. **Novelty:** Friends share your world and information. Acquaintances bridge to different social circles, providing non-redundant job leads.
> 2. **Structure:** Strong ties cluster in dense groups (redundancy). Weak ties are bridges to distant clusters (novelty).
> 3. **No.** Strong ties provide trust and support; weak ties provide reach. You need both.
> 4. **LinkedIn:** Formalises weak ties with low neighbourhood overlap, enabling people to scale their "reach" into structural holes.

### 3.D.1 — Neighbourhood Overlap Calculation

> [!note]- Solution
> O(A,B) = |{C}| / |{C,D,E}| = 1/3
> O(A,C) = |{B}| / |{B,D,F}| = 1/3
> O(B,E) = |∅| / |{A,C}| = 0
>
> **Ranking:** O(B,E) has zero overlap, making it a perfect local bridge. Information entering via E is likely to be completely novel to the A, B, C cluster.

### 3.D.2 — Neighbourhood Overlap in NetworkX

> [!note]- Solution
> **Interpretation:** Cross-faction edges have significantly lower overlap, confirming they behave as structural bridges between communities. Within-faction edges have high overlap, providing structural redundancy. Low-overlap edges are the "glue" holding separate social worlds together.

### 3.E.1 — Tie Strengths in Practice

> [!note]- Solution
> 1. **Symmetry:** Facebook ties are reciprocal, leading to higher local clustering and overlap. Twitter links are closer to structural bridges with near-zero overlap.
> 2. **Cognitive limits:** Maintained ties are bounded by the Dunbar number and social attention. Passive links are structural weak ties with high novelty but low investment.
> 3. **Diversity:** Recommend content from low-overlap connections. These structural bridges provide access to disjoint social bubbles and non-redundant information.

### 3.E.2 — Simulating Tie Strength and Overlap

> [!note]- Solution
> Pearson correlation is typically > 0.6, confirming that tie strength and neighbourhood overlap are linked: close-knit groups share friends, while bridging ties remain socially isolated. High-strength ties with low overlap may indicate bridging relationships that involve significant social effort.


---

## Related Resources

### 📖 L03 — Strong and Weak Ties
- Lecture topic: [[network-science-l03]]

**Key concepts covered:**
- [[graph-fundamentals]]
- [[triadic-closure]]
- [[strong-triadic-closure]]
- [[maxstc-complexity]]
- [[clustering-coefficient]]
- [[neighborhood-overlap]]
- [[bridges-and-local-bridges]]
- [[weak-ties-hypothesis]]
- [[social-capital]]
- [[structural-holes]]
