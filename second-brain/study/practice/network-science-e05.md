---
title: "Exercise Sheet 5 — Community Detection"
tags:
  - practice
  - network-science
  - semester-1
course: "Network Science"
status: current
last_updated: 2026-06-02
---

## Topic Map

| Exercise | Key Vault Pages |
|----------|----------------|
| 5.A Basic Measures and Modularity | [[modularity]] · [[community-detection-overview]] |
| 5.B Girvan-Newman Algorithm | [[girvan-newman-algorithm]] · [[edge-betweenness]] |
| 5.C Hierarchical Clustering | [[hierarchical-clustering]] |

# Exercise Sheet 5 — Community Detection

## Exercises

### 5.A Basic Measures and Modularity

**Exercise 5.A.1: Community Density by Hand**

Graph: A, B, C, D, E, F, edges A–B, A–C, B–C, B–D, D–E, D–F, E–F.

Two candidate partitions:
- **P1:** {A, B, C, D} and {E, F}
- **P2:** {A, B, C} and {D, E, F}

For each partition:
1. Compute internal edge density: |edges inside| / |possible edges inside|.
2. Compute external edge density: |crossing edges| / |possible crossing edges|.
3. Which partition better separates the network? Justify with numbers.
4. What is the "ground truth" community structure visible from inspection?

---

**Exercise 5.A.2: Modularity — Concept and Computation**

Modularity Q measures whether communities are denser than expected by chance:

Q = (1/2m) Σ_c [e_c − a²_c / 4m]

where e_c = edges inside community c, a_c = sum of degrees in community c, m = total edges.

1. For P2 from Exercise 5.A.1, compute Q by hand (use m = 7).
2. What does Q = 0 mean? What does Q = 1 mean? What range is typical for real networks?
3. If you randomly shuffled community assignments, what would you expect Q to approach?

---

**Exercise 5.A.3: Community Detection in Python**

Using `nx.karate_club_graph()`:

1. Apply greedy modularity maximisation: `nx.community.greedy_modularity_communities(G)`.
2. Compute the modularity score of the result using `nx.community.modularity(G, communities)`.
3. Compare to the known faction labels (`G.nodes[n]["club"]`). What fraction of nodes are assigned to the "correct" faction?
4. Visualise: plot the network with nodes coloured by detected community.

### 5.B Girvan-Newman Algorithm

**Exercise 5.B.1: Girvan-Newman Steps**

Graph: 6 nodes, two triangles {1, 2, 3} and {4, 5, 6} connected by single edge 3–4.

1. Compute edge betweenness for all edges. Which edge has the highest value?
2. Remove that edge. What happens to the graph?
3. Which edges now have the highest betweenness after the removal?
4. Why is edge 3–4 guaranteed to have the highest betweenness in this structure?

---

**Exercise 5.B.2: Girvan-Newman in Practice**

Using `nx.karate_club_graph()`:

1. Apply the Girvan-Newman algorithm: `nx.community.girvan_newman(G)`.
2. Extract the partition at the 2-community level. Does it recover the known factions?
3. Compare faction recovery accuracy to the greedy modularity result from Exercise 5.A.3.
4. Plot the edge betweenness of the top-5 edges at the initial state and after 1 removal step.

### 5.C Hierarchical Clustering

**Exercise 5.C.1: Dendrogram Interpretation**

Consider the 6-node two-triangle graph from the Girvan-Newman exercise.

1. What does the height of a merge step in a dendrogram represent?
2. In the dendrogram for this graph, at what level do the two triangles merge into a single cluster?
3. How would you choose the "right" number of clusters from a dendrogram?
4. What is the difference between using direct-link similarity vs. neighbourhood-overlap similarity as the merge criterion?

---

**Exercise 5.C.2: Hierarchical Clustering in Python**

Using `nx.karate_club_graph()` and scipy:

1. Compute pairwise shortest-path distances between all nodes. Use this as the distance matrix.
2. Apply hierarchical clustering with average linkage: `scipy.cluster.hierarchy.linkage(...)`.
3. Plot the resulting dendrogram.
4. Cut at a height to obtain 2 clusters. What fraction of nodes match the known factions?

---

## Solutions

### 5.A.1 — Community Density by Hand

> [!note]- Solution
> **Partition P1: {A,B,C,D} and {E,F}**
> - Internal edges in {A,B,C,D}: A–B, A–C, B–C, B–D = 4. Possible: C(4,2) = 6. Density = 4/6 ≈ 0.67.
> - Internal edges in {E,F}: E–F = 1. Possible: C(2,2) = 1. Density = 1/1 = 1.0.
> - Crossing edges: D–E, D–F = 2. Possible crossing: 4×2 = 8. External density = 2/8 = 0.25.
>
> **Partition P2: {A,B,C} and {D,E,F}**
> - Internal edges in {A,B,C}: A–B, A–C, B–C = 3. Possible: C(3,2) = 3. Density = 3/3 = 1.0.
> - Internal edges in {D,E,F}: D–E, D–F, E–F = 3. Possible: C(3,2) = 3. Density = 3/3 = 1.0.
> - Crossing edges: B–D = 1. Possible: 3×3 = 9. External density = 1/9 ≈ 0.11.
>
> **Comparison:** P2 achieves perfect internal density (1.0) in both communities and minimal external density (0.11). P2 is the clearly superior partition.
>
> **Ground truth:** The graph consists of two complete triangles (A–B–C and D–E–F) joined by a single bridge edge B–D. The natural communities are exactly {A, B, C} and {D, E, F}.

### 5.A.2 — Modularity Computation

> [!note]- Solution
> 1. Computing Q for P2 (m = 7):
>    - Community {A,B,C}: e₁ = 3, a₁ = 2+3+2 = 7. Expected = 49/28 ≈ 1.75.
>    - Community {D,E,F}: e₂ = 3, a₂ = 3+2+2 = 7. Expected = 49/28 ≈ 1.75.
>    - Q = (1/14) × [(3−1.75) + (3−1.75)] = (1/14) × 2.5 ≈ 0.18
> 2. **Q = 0:** community structure no better than random. **Q = 1:** perfect modularity. **Typical real networks:** Q ∈ [0.3, 0.7].
> 3. **Random assignment:** Q approaches 0. Any positive Q indicates more internal edges than chance.

### 5.A.3 — Community Detection in Python

> [!note]- Solution
> **Resolution limit:** Greedy modularity typically finds 3–4 communities (Q ≈ 0.4), whereas the known faction split has only 2 groups. The algorithm splits the larger faction into two sub-clusters. **Accuracy:** Despite the extra split, high faction matching (85%+) shows that modularity effectively captures the core social divisions.

### 5.B.1 — Girvan-Newman Steps

> [!note]- Solution
> 1. **Edge 3–4** lies on every path between nodes in {1,2,3} and {4,5,6}: 3×3 = 9 pairs. Betweenness = 9 (unnormalised), far above any intra-triangle edge.
> 2. After removing 3–4: The graph splits into two disconnected triangles.
> 3. Within each isolated triangle, all three edges are equivalent with equal betweenness.
> 4. **Why guaranteed:** Any path from {1,2,3} to {4,5,6} must cross this edge — there is no alternative route. The betweenness of a bridge is always |L| × |R| = 3 × 3 = 9.

### 5.B.2 — Girvan-Newman in Practice

> [!note]- Solution
> **Precision:** Girvan-Newman at 2 communities typically recovers the exact faction split (~97% accuracy). Unlike modularity, it doesn't over-partition the factions. **Top-down logic:** By iteratively removing the highest-betweenness (bridge) edges, the algorithm cleanly isolates the two social hubs (Mr. Hi and the Officer) and their respective followers.

### 5.C.1 — Dendrogram Interpretation

> [!note]- Solution
> 1. **Height** represents the dissimilarity (or distance) between the two clusters being merged. Low height = very similar clusters; high height = dissimilar clusters being forced together.
> 2. Within each triangle, nodes merge at low height first. The two triangles merge at the highest height because they are connected only by a single bridge edge — maximum dissimilarity.
> 3. **Choosing k:** Look for the largest gap in merge heights (longest vertical line before next merge). Cutting just below a large gap gives a natural number of clusters. Here k = 2.
> 4. **Direct-link similarity:** two nodes are similar if they share an edge. **Neighbourhood-overlap similarity:** = |N(u)∩N(v)|/|N(u)∪N(v)|. More robust to missing edges and better captures social equivalence.

### 5.C.2 — Hierarchical Clustering in Python

> [!note]- Solution
> The dendrogram shows two main branches merging at the highest height — these correspond to the two factions. Average linkage with shortest-path distances is robust for capturing social proximity. Some fringe bridge-nodes may be misclassified if they sit equidistant from both centers in terms of hops.


---

## Related Resources

### 📖 Network Science L05: Social Context and Link Formation
- Lecture topic: [[network-science-l05]]

**Key concepts covered:**
- [[homophily]]
- [[echo-chambers]]
- [[network-autocorrelation]]
- [[selection-vs-socialization]]
- [[affiliation-networks]]
- [[schelling-segregation-model]]
- [[modularity]]
