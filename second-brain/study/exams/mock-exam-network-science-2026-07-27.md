---
title: "Mock Exam 2 — Network Science"
tags: [exam-prep, mock-exam, network-science, semester-1]
course: "Network Science"
exam_date: "2026-07-28"
format: "50% Antwort-Wahl-Verfahren + 50% essay"
status: current
last_updated: 2026-07-27
prerequisites: []
---

# Mock Exam 2 — Network Science

> *Second pass. Different questions, different angles. If you aced Mock 1, prove it here too. No notes. 3 hours. Einfachauswahl unless marked **[Mehrfachauswahl]**.*
>
> Scope: Lectures 1–8, Exercise Sheets 1–8. This mock emphasises spectral methods, Erdős–Rényi thresholds, SIS vs SIR, temporal networks, hierarchical clustering, and homophily index r — areas Mock 1 underweighted.

---

# PART A — Antwort-Wahl-Verfahren (50%)

---

## Section 1 — Graph Theory & Connectivity (L01–L02)

### Q1. In a directed graph, the number of edges equals:

a) Σ in-deg(v) + Σ out-deg(v)
b) Σ in-deg(v) = Σ out-deg(v) = |E|
c) 2 × Σ deg(v)
d) |V| × (|V| − 1)

> [!note]- Solution
> **b)** In a directed graph, each edge (u, v) contributes 1 to u's out-degree and 1 to v's in-degree. So Σ in-deg(v) = Σ out-deg(v) = |E|. This is the directed analogue of the handshaking lemma. (a) would give 2|E|. (c) is the undirected handshaking lemma. (d) is the maximum possible edges in a complete directed graph.

---

### Q2. The diameter of a graph is:

a) The average shortest-path distance between all node pairs
b) The maximum eccentricity over all nodes
c) The minimum eccentricity over all nodes
d) The number of edges in the longest path

> [!note]- Solution
> **b)** Diameter = max eccentricity = max_{u,v} d(u,v) — the longest shortest path in the graph. (a) is the average path length d̄. (c) is the *radius*. (d) is wrong — the diameter considers only shortest paths, not arbitrary long paths.

---

### Q3. The centre of a graph consists of:

a) The node(s) with the highest degree
b) The node(s) with eccentricity equal to the radius
c) The node(s) with the highest betweenness centrality
d) The largest connected component

> [!note]- Solution
> **b)** The centre = {v : ecc(v) = radius}. These are the nodes whose maximum distance to any other node is minimised — the most "central" nodes in the graph-theoretic sense (not centrality-measure sense). For a path graph P₅ = 1–2–3–4–5, the centre is {3} with radius 2.

---

### Q4. A graph is bipartite if and only if:

a) It has no cycles
b) It contains no odd-length cycles
c) It has even number of nodes
d) Every node has even degree

> [!note]- Solution
> **b)** A graph is bipartite ⟺ it contains no odd-length cycles. This is König's theorem. Equivalently, a graph is bipartite ⟺ it is 2-colourable. (a) would mean the graph is a forest — too strong. (c) is irrelevant. (d) is the Eulerian condition.

---

### Q5. In an Erdős–Rényi random graph G(n, p), the expected number of edges is:

a) n × p
b) p × n(n − 1)/2
c) n² × p
d) 2pn

> [!note]- Solution
> **b)** There are C(n, 2) = n(n−1)/2 possible edges, each present independently with probability p. So E[|E|] = p × C(n, 2) = p × n(n−1)/2. The average degree ⟨k⟩ = p(n − 1) ≈ pn for large n.

---

### Q6. [Mehrfachauswahl] Which of the following are correct about Erdős–Rényi random graphs?

a) The degree distribution is approximately Poisson for large n
b) A giant component emerges when ⟨k⟩ > 1 (i.e., p > 1/n)
c) The graph is almost surely connected when p > ln(n)/n
d) The clustering coefficient C ≈ p = k/(n−1) ≈ k/n, which is very low for large n
e) Erdős–Rényi graphs produce power-law degree distributions

> [!note]- Solution
> **a), b), c), d).** The degree distribution is Binomial(n−1, p), which converges to Poisson(np) for large n and small p (a). The giant component threshold is ⟨k⟩ = 1 (b). Connectivity threshold: p > ln(n)/n (c). Clustering = p ≈ k/n → 0 for large n (d). (e) is **false** — Erdős–Rényi has a narrow Poisson-like distribution. Power laws require preferential attachment (Barabási–Albert model).

---

### Q7. The adjacency matrix A of an undirected simple graph is:

a) Symmetric with 0s on the diagonal
b) Upper triangular
c) Always positive definite
d) Diagonal with node degrees

> [!note]- Solution
> **a)** Undirected → A_ij = A_ji (symmetric). Simple → no self-loops → A_ii = 0. (d) describes the degree matrix D, not the adjacency matrix. The eigenvalues of A are real (by symmetry) but can be negative, so A is not positive definite.

---

## Section 2 — Centrality Measures (L04)

### Q8. Consider a star graph with n = 7 nodes (one centre connected to 6 leaves). The degree centrality of the centre node is:

a) 6/7
b) 6/6 = 1.0
c) 1/6
d) 7/6

> [!note]- Solution
> **b)** C_D(v) = deg(v)/(n−1). The centre has degree 6, n = 7, so C_D = 6/6 = 1.0. In a star graph, the centre is connected to everyone — maximum degree centrality. Each leaf has C_D = 1/6 ≈ 0.167.

---

### Q9. Eigenvector centrality is computed by:

a) Counting shortest paths through each node
b) Finding the leading eigenvector of the adjacency matrix A (Ax = λx)
c) Summing the reciprocals of distances from each node
d) Computing the fraction of edges within communities

> [!note]- Solution
> **b)** Eigenvector centrality: C_E(v) = (1/λ) Σ_u A_vu C_E(u), or equivalently Ax = λx where x is the centrality vector and λ is the largest eigenvalue. (a) is betweenness. (c) is harmonic centrality. (d) is modularity.

---

### Q10. The power iteration method for eigenvector centrality works by:

a) Repeatedly computing x^(t+1) = Ax^(t) / ||Ax^(t)|| until convergence
b) Solving the linear system Ax = b
c) Computing all eigenvalues via QR decomposition
d) Running BFS from every node

> [!note]- Solution
> **a)** Power iteration: start with a random vector x^(0), then repeatedly multiply by A and normalise: x^(t+1) = Ax^(t) / ||Ax^(t)||. This converges to the leading eigenvector (the one with the largest eigenvalue) under mild conditions. Each iteration costs O(|E|) for sparse graphs. Convergence rate depends on the ratio λ₁/λ₂.

---

### Q11. In the PageRank formula PR(v) = (1−α)/n + α Σ_{u→v} PR(u)/outdeg(u), the term (1−α)/n represents:

a) The probability of following a link from a random page
b) The probability of teleporting to page v uniformly at random
c) The damping factor
d) The reciprocal of the number of incoming links

> [!note]- Solution
> **b)** (1−α)/n is the random-jump (teleportation) probability: with probability (1−α), the random surfer ignores all links and jumps to a uniformly random page. With n pages, the probability of landing on v is 1/n. Combined: (1−α)/n. This prevents rank-sinks and handles dangling nodes.

---

### Q12. [Mehrfachauswahl] Which centrality measures require computing shortest paths from every node?

a) Degree centrality
b) Closeness centrality
c) Harmonic centrality
d) Betweenness centrality
e) Eigenvector centrality
f) PageRank

> [!note]- Solution
> **b), c), d).** Closeness (b) and harmonic (c) both require Σ_{u≠v} d(v,u) — BFS from every node → O(n(n+m)). Betweenness (d) counts shortest paths through v for all (s,t) pairs — Brandes algorithm runs BFS from every node. Degree (a) is O(n+m) — just count edges. Eigenvector (e) uses power iteration on A — O(k(n+m)). PageRank (f) iterates on the transition matrix — O(k·m).

---

### Q13. For a node v in a disconnected graph, closeness centrality C_C(v) and harmonic centrality H(v) behave as follows:

a) Both return 0
b) C_C(v) → 0 (sum of distances includes ∞); H(v) remains meaningful (1/∞ = 0)
c) Both are undefined
d) H(v) → 0 but C_C(v) remains meaningful

> [!note]- Solution
> **b)** Closeness: C_C(v) = (n−1)/Σ d(v,u). If any u is unreachable, d(v,u) = ∞, so the denominator is ∞ and C_C(v) → 0 — all nodes in all components get 0, losing all discrimination. Harmonic: H(v) = Σ 1/d(v,u) with 1/∞ = 0. Unreachable nodes simply contribute 0 to the sum. The measure retains discrimination among reachable nodes. This is precisely why harmonic centrality was introduced.

---

### Q14. Betweenness centrality for an undirected graph with n nodes is normalised by dividing by:

a) n(n − 1)
b) (n − 1)(n − 2)/2
c) n(n − 1)/2
d) 2m

> [!note]- Solution
> **b)** The number of ordered pairs (s, t) with s ≠ v ≠ t is (n−1)(n−2). For undirected graphs, we count unordered pairs: (n−1)(n−2)/2. This is the maximum possible raw betweenness (achieved by the centre of a star graph). For directed graphs: (n−1)(n−2).

---

### Q15. A node with high eigenvector centrality but low degree centrality is best described as:

a) A popular node connected to many others
b) A node connected to a few but very prestigious (central) nodes
c) A bridge between communities
d) An isolated node

> [!note]- Solution
> **b)** Eigenvector centrality is recursive: C_E(v) ∝ Σ_u A_vu C_E(u). A node connected to just 2–3 very central nodes can have high eigenvector centrality despite low degree. Example: a node connected only to the highest-PageRank pages in a web graph. Degree centrality counts raw connections; eigenvector weights them by the connections' own importance.

---

## Section 3 — Strong/Weak Ties & Clustering (L03)

### Q16. A node v has 5 neighbours. Among those 5 neighbours, there are 4 edges. The local clustering coefficient C_v is:

a) 4/10 = 0.4
b) 4/5 = 0.8
c) 8/20 = 0.4
d) 2 × 4 / (5 × 4) = 0.4

> [!note]- Solution
> **d)** C_v = 2 × (edges among neighbours) / (k(k−1)) = 2 × 4 / (5 × 4) = 8/20 = 0.4. Equivalently: edges among neighbours / C(k,2) = 4/10 = 0.4. Both formulas give the same answer — (a) and (d) are algebraically identical. The answer is 0.4: 40% of possible triangles through v are closed.

---

### Q17. The global clustering coefficient is defined as:

a) The average of all local clustering coefficients
b) 3 × (number of triangles) / (number of connected triples)
c) The density of the graph
d) The modularity of the best partition

> [!note]- Solution
> **b)** Global clustering C = 3 × triangles / connected triples. Each triangle contains 3 connected triples (open or closed triads), hence the factor 3. This is different from the *average* local clustering coefficient (a), which is the mean of C_v over all nodes. Both are used in practice but measure slightly different things — the global version weights high-degree nodes more (they participate in more triples).

---

### Q18. Neighbourhood overlap O(u,v) = 0 means:

a) u and v are in different connected components
b) u and v share no common neighbours — the edge (u,v) is a local bridge
c) u and v have the same degree
d) The edge (u,v) is a strong tie

> [!note]- Solution
> **b)** O(u,v) = |N(u) ∩ N(v)| / |N(u) ∪ N(v)| = 0 ⟹ N(u) ∩ N(v) = ∅ — no shared neighbours. This is the definition of a local bridge. It does NOT mean u and v are disconnected (a) — they may be directly linked. It does NOT imply strong tie (d) — in fact, under STC, local bridges must be weak ties.

---

### Q19. [Mehrfachauswahl] Which of the following correctly describe triadic closure mechanisms in social networks?

a) Opportunity: shared friends create situations where B and C meet
b) Trust: a mutual friend vouches for both parties
c) Social pressure: an open triad creates incentive to close it
d) Triadic closure always decreases the graph's diameter
e) Triadic closure increases local clustering coefficients

> [!note]- Solution
> **a), b), c), e).** The three drivers of triadic closure: opportunity (a), trust (b), social pressure (c). Closing a triad increases the clustering coefficients of all three nodes involved (e). (d) is false — triadic closure adds local edges that increase redundancy within neighbourhoods; it does not necessarily decrease the global diameter. It can even create dense clusters that *trap* shortest paths locally.

---

### Q20. Onnela et al. (2007) studied mobile phone call networks and found that:

a) Strong ties (frequent calls) have high neighbourhood overlap; weak ties (rare calls) have low overlap — confirming Granovetter
b) Weak ties carry more total call time than strong ties
c) Removing weak ties fragments the network faster than removing strong ties
d) Mobile phone networks have no community structure

> [!note]- Solution
> **a)** Onnela et al. confirmed Granovetter at scale: tie strength (measured by call duration/frequency) is positively correlated with neighbourhood overlap. Strong ties sit inside dense clusters (high overlap); weak ties bridge between clusters (low overlap). Removing weak ties actually fragments the network *more* — they are the bridges. This is the large-scale empirical validation of the weak ties hypothesis.

---

## Section 4 — Communities & Spectral Methods (L04–L05)

### Q21. The graph Laplacian L = D − A has the property that:

a) All eigenvalues are negative
b) λ₁ = 0 always, with eigenvector = constant vector 1
c) λ₁ = 0 if and only if the graph is connected
d) L is always positive definite

> [!note]- Solution
> **b)** L is positive semi-definite: all eigenvalues ≥ 0. The smallest eigenvalue λ₁ = 0 always, with eigenvector being the all-ones vector 1 (since L·1 = D·1 − A·1 = deg − deg = 0). (c) is wrong — λ₁ = 0 always; it's λ₂ (the Fiedler value) that is > 0 iff the graph is connected. (d) is wrong — L is positive *semi*-definite, not definite (λ₁ = 0).

---

### Q22. The Fiedler value λ₂ of the graph Laplacian measures:

a) The number of connected components
b) The algebraic connectivity — how difficult it is to disconnect the graph
c) The diameter of the graph
d) The modularity of the best partition

> [!note]- Solution
> **b)** λ₂ = second-smallest eigenvalue of L = D − A. It is called the *algebraic connectivity* or *Fiedler value*. λ₂ > 0 ⟺ graph is connected. Larger λ₂ → harder to bisect the graph → more robust connectivity. λ₂ = 0 ⟺ graph is disconnected (at least 2 components). The corresponding eigenvector (Fiedler vector) provides a natural bipartition.

---

### Q23. Spectral partitioning using the Fiedler vector works by:

a) Assigning nodes with positive Fiedler vector entries to group 1 and negative entries to group 2
b) Removing the edge with highest betweenness
c) Greedily merging communities that maximise ΔQ
d) Running k-means on the raw adjacency matrix

> [!note]- Solution
> **a)** Spectral bisection: compute L = D − A, find the Fiedler vector x₂ (eigenvector of λ₂). Partition: x₂(i) > 0 → group 1, x₂(i) < 0 → group 2. This minimises the normalised cut under a relaxation. For k communities, use the k smallest non-trivial eigenvectors and run k-means on the resulting embeddings — this is spectral clustering.

---

### Q24. Hierarchical clustering produces a dendrogram. Cutting the dendrogram at the largest gap gives:

a) The partition with the most communities
b) The partition that maximises modularity
c) The partition where the largest jump in dissimilarity between merged clusters occurs — the "natural" number of clusters
d) A single community containing all nodes

> [!note]- Solution
> **c)** A dendrogram plots merge height (dissimilarity) against merges. The largest vertical gap between consecutive merges indicates the most natural cut point — below it, clusters are similar; above it, merging combines dissimilar groups. This is the standard heuristic for choosing k in hierarchical clustering. It does NOT guarantee maximum modularity (b) — that would require explicit Q optimisation.

---

### Q25. [Mehrfachauswahl] Which statements about the Louvain and Leiden algorithms are correct?

a) Both are agglomerative (bottom-up) methods that optimise modularity
b) Louvain can produce internally disconnected communities
c) Leiden adds a refinement step that guarantees internally well-connected communities
d) Louvain has complexity O(n log n) and scales to millions of nodes
e) Leiden is strictly slower than Louvain by a factor of n

> [!note]- Solution
> **a), b), c), d).** Both are agglomerative modularity optimisers (a). Louvain's greedy merging can produce communities where some nodes are only reachable through nodes in other communities — internally disconnected (b). Leiden fixes this with a refinement step before aggregation (c). Louvain is fast — effectively O(m) per pass — and scales to millions of nodes (d). (e) is false — Leiden adds only a small constant-factor overhead; it does not scale worse.

---

### Q26. The modularity resolution limit means that communities smaller than approximately ___ edges are invisible to modularity maximisation:

a) √(2m) where m = total edges
b) m/2
c) log(n)
d) n/2

> [!note]- Solution
> **a)** The resolution limit: modularity cannot resolve communities smaller than approximately √(2m) edges. This is because the null-model expected edge count a_c²/4m becomes comparable to the actual internal edges for small communities. In a network with m = 10,000 edges, communities with fewer than ~141 edges may be merged with adjacent ones even if they are structurally distinct.

---

### Q27. Edge betweenness centrality measures:

a) The number of shortest paths between all node pairs that pass through a given edge
b) The degree of each endpoint of the edge
c) The weight of the edge
d) The clustering coefficient of the edge's endpoints

> [!note]- Solution
> **a)** Edge betweenness C_B(e) = Σ_{s≠t} σ_st(e)/σ_st — the fraction of all shortest paths between all node pairs that traverse edge e. Bridges between communities have high edge betweenness because most cross-community shortest paths must pass through them. This is the basis of the Girvan–Newman algorithm: iteratively remove the highest-betweenness edge to reveal community structure.

---

## Section 5 — Homophily & Social Context (L05–L06)

### Q28. The homophily index r = (H_obs − H_base) / (1 − H_base) equals 0 when:

a) All ties are within-group (perfect segregation)
b) Observed within-group ties equal the random-mixing baseline
c) All ties are between groups (perfect heterophily)
d) The network is complete

> [!note]- Solution
> **b)** r = 0 means H_obs = H_base — the observed fraction of within-group ties is exactly what random mixing would predict. No preference beyond chance. r = 1 means H_obs = 1 (perfect segregation). r < 0 means fewer within-group ties than expected (heterophily). The baseline H_base = Σᵢ pᵢ² (sum of squared group shares) accounts for the fact that large groups naturally have more within-group ties even under random mixing.

---

### Q29. In a network with two groups of sizes n₁ = 60 and n₂ = 40 (N = 100), the random-mixing baseline probability of a cross-group edge is:

a) 0.48
b) 0.52
c) 0.24
d) 0.50

> [!note]- Solution
> **a)** P(cross | random) = 1 − [C(n₁, 2) + C(n₂, 2)] / C(N, 2) = 1 − [C(60,2) + C(40,2)] / C(100,2) = 1 − [1770 + 780] / 4950 = 1 − 2550/4950 = 1 − 0.515 = 0.485 ≈ 0.48. Equivalently: 2 × 60 × 40 / (100 × 99) ≈ 0.485. Under random mixing, about 48% of edges would be cross-group.

---

### Q30. An E-I index of +0.6 indicates:

a) Strong homophily — most ties are within-group
b) Moderate heterophily — more cross-group ties than within-group ties
c) Perfect segregation
d) Neutral mixing

> [!note]- Solution
> **b)** E-I = (E − I)/(E + I) = +0.6 means E > I — more external (cross-group) ties than internal (within-group) ties. This is heterophilic mixing. +1 would be pure heterophily (all ties cross-group). −1 would be pure homophily (all ties within-group). 0 is neutral.

---

### Q31. In an affiliation (bipartite) network, *focal closure* means:

a) Two people who share a friend become friends
b) Two people who share an affiliation (e.g., same course) become friends
c) A person joins a new affiliation because a friend is already in it
d) A focus (e.g., course) is dissolved

> [!note]- Solution
> **b)** Focal closure: shared affiliation → tie formation. Two students enrolled in the same course start interacting and become friends. The shared context (focus) creates the opportunity. (a) is *triadic* closure. (c) is *membership* closure. These three mechanisms — triadic, focal, membership — are the closure processes identified by Kossinets & Watts (2006) in evolving affiliation networks.

---

### Q32. [Mehrfachauswahl] Which of the following are correct about selection vs. socialisation in homophily?

a) Selection: similarity causes tie formation (attribute → tie)
b) Socialisation: tie formation causes similarity (tie → attribute)
c) Cross-sectional data can reliably distinguish selection from socialisation
d) Contextual correlation (shared environment) is a confounder that can mimic both
e) Longitudinal data or experiments are needed to disentangle selection from socialisation

> [!note]- Solution
> **a), b), d), e).** Selection (a): similar people become friends. Socialisation (b): friends become similar over time. Contextual correlation (d): a shared environment (e.g., same neighbourhood, same school) causes both similarity and friendship — a confounder. Cross-sectional data (c) CANNOT distinguish these three — you need longitudinal data tracking changes over time, or controlled experiments, to determine causal direction (e).

---

### Q33. Schelling's segregation model demonstrates that:

a) Agents with strong preferences (>80% same-type) are needed for segregation
b) Mild individual preferences (30–40% same-type) cascade into strong global segregation
c) Segregation only occurs in one-dimensional (linear) arrangements
d) The model always converges to a fully integrated state

> [!note]- Solution
> **b)** Schelling's key result: even when each agent only requires 30–40% of neighbours to be the same type, the cascading dynamics of relocation produce sharp global segregation far exceeding any individual's preference. When one agent moves, it changes neighbourhood composition, potentially triggering further moves. The macro outcome (high segregation) vastly exceeds the micro preference (mild tolerance). This is an *identification problem*: you cannot infer individual preferences from aggregate outcomes.

---

## Section 6 — Structural Balance (L07)

### Q34. Under strong structural balance, the (+, +, −) triangle is:

a) Balanced — two friends and one enemy is stable
b) Unbalanced — "the enemy of my friend is my friend" creates tension
c) Weakly balanced but not strongly balanced
d) The most common triangle type in empirical data

> [!note]- Solution
> **b)** (+, +, −) has an odd number of negative edges (1) → product is negative → unbalanced. Social meaning: A and B are friends, A and C are friends, but B and C are enemies. This creates tension — A is pulled in two directions. Under both strong and weak balance, (+, +, −) is forbidden. Empirically, it is massively *underrepresented* (~8% observed vs ~37.5% expected by random signing) — balance theory is confirmed.

---

### Q35. The cycle criterion for balance in incomplete signed graphs states:

a) A signed graph is balanced iff every cycle has an even number of negative edges
b) A signed graph is balanced iff every triangle has an even number of negative edges
c) A signed graph is balanced iff it has no negative edges
d) A signed graph is balanced iff the graph is a tree

> [!note]- Solution
> **a)** For complete graphs, checking all C(n,3) triangles suffices. For *incomplete* graphs, the correct generalisation is the cycle criterion: the graph is balanced iff *every cycle* (not just triangles) contains an even number of negative edges. This can be checked in polynomial time via BFS: 2-colour the nodes such that positive edges connect same-colour nodes and negative edges connect different-colour nodes. If this colouring exists, the graph is balanced.

---

### Q36. The signed Laplacian L_σ = D − A_σ can test balance in polynomial time. A signed graph is balanced if and only if:

a) All eigenvalues of L_σ are positive
b) The smallest eigenvalue λ₁(L_σ) = 0
c) The largest eigenvalue equals n
d) The trace of L_σ equals 0

> [!note]- Solution
> **b)** λ₁(L_σ) = 0 ⟺ the signed graph is balanced. If the graph is balanced, there exists a node signing s ∈ {+1, −1}^n such that A_σ · s = D · s (every positive edge connects same-sign nodes, every negative edge connects opposite-sign nodes), so L_σ · s = 0. If λ₁ > 0, the graph is unbalanced. This is computed via the Lanczos algorithm in O(|E| · d) time.

---

### Q37. [Mehrfachauswahl] Which of the following are correct about the frustration index F(G, σ)?

a) F(G, σ) = minimum number of edge sign flips to achieve balance
b) Computing F is NP-hard (equivalent to MAX-CUT)
c) F = 0 if and only if the graph is already balanced
d) F can be computed in polynomial time using the signed Laplacian
e) F provides a measure of "how far" a graph is from being balanced

> [!note]- Solution
> **a), b), c), e).** The frustration index (a) counts the minimum flips. It is NP-hard (b) — equivalent to MAX-CUT (Sintos & Tsaparas 2014). F = 0 ⟺ already balanced (c). It measures distance from balance (e). (d) is false — the signed Laplacian gives a polynomial-time *test* for whether F = 0 (balanced or not), but does NOT compute the exact value of F when F > 0.

---

### Q38. Under weak balance (Davis 1967), a complete signed graph partitions into:

a) Exactly 2 camps
b) k ≥ 1 camps, where within-camp edges are positive and between-camp edges are negative
c) A single camp always
d) Camps of equal size

> [!note]- Solution
> **b)** Weak balance permits (−,−,−) triangles (three mutual enemies), so the Balance Theorem generalises: nodes partition into k ≥ 1 camps. k = 1: all positive. k = 2: strong balance case. k ≥ 3: multi-polar world where mutual hostility between 3+ camps is stable. The only forbidden triangle remains (+,+,−) — two friends who share an enemy must resolve the tension.

---

## Section 7 — Small-World & Scale-Free Networks (L08)

### Q39. In the Barabási–Albert preferential attachment model, a new node connects to existing node i with probability:

a) 1/n (uniform)
b) k_i / Σ_j k_j (proportional to i's degree)
c) p (constant, independent of degree)
d) 1/k_i (inversely proportional to degree)

> [!note]- Solution
> **b)** Π(k_i) = k_i / Σ_j k_j — the "rich get richer" mechanism. New nodes preferentially attach to high-degree existing nodes. This produces a power-law degree distribution P(k) ~ k^(-3) with γ = 3. The model captures the empirical observation that in growing networks (web pages, citation networks), popular nodes attract even more connections.

---

### Q40. For scale-free networks with γ ≤ 3, the epidemic threshold T_c:

a) Is a finite positive constant
b) Equals ⟨k⟩ / (⟨k²⟩ − ⟨k⟩)
c) Approaches 0 as N → ∞ — any non-zero transmission rate can sustain an epidemic
d) Equals 1/R₀

> [!note]- Solution
> **c)** For γ ≤ 3, ⟨k²⟩ diverges as N → ∞. Since T_c ≈ ⟨k⟩ / (⟨k²⟩ − ⟨k⟩), the denominator → ∞ and T_c → 0. This means any disease with non-zero transmission rate can become an epidemic on a sufficiently large scale-free network. There is no finite epidemic threshold. Practical consequence: random vaccination cannot achieve herd immunity — you must target hubs.

---

### Q41. The Barabási–Albert model produces average path lengths of approximately:

a) log(N) / log(k) — same as random graphs
b) log(N) / log(log(N)) — ultra-small, shorter than random graphs
c) N / (2k) — same as regular lattices
d) N² / k

> [!note]- Solution
> **b)** Scale-free networks have d̄ ~ log(N) / log(log(N)) — *ultra-small* distances, even shorter than the random-graph prediction log(N)/log(k). Hubs act as super-shortcuts: most shortest paths pass through a few high-degree nodes that connect distant parts of the network in very few hops. For N = 10⁶, log(N)/log(k) ≈ 3.5 but log(N)/log(log(N)) ≈ 5.3 — wait, this is actually *longer* for small N. The ultra-small effect dominates for very large N where log(log(N)) grows extremely slowly.

---

### Q42. In Kleinberg's navigability theorem on a d-dimensional grid with long-range links drawn proportional to r^(−α), greedy routing is efficient (polylog delivery time) if and only if:

a) α = 0 (uniform random long-range links)
b) α = 1
c) α = d (exponent equals grid dimension)
d) α > 2d

> [!note]- Solution
> **c)** Kleinberg (2000): on a d-dimensional grid, greedy routing (always forward to the neighbour closest to the target) achieves O((log N)²) delivery time iff α = d. For α < d, long-range links are too uniformly distributed — not enough local bias. For α > d, long-range links are too clustered — not enough reach. On a 2D grid, α = 2 is optimal. This explains why some small-world networks are navigable by decentralised search while others are not.

---

### Q43. [Mehrfachauswahl] Which properties correctly describe the Watts–Strogatz model?

a) It starts with a ring lattice where each node is connected to its k nearest neighbours
b) Each edge is rewired with probability p
c) It produces a power-law degree distribution
d) For small p, it achieves high clustering with short path lengths
e) The degree distribution remains narrow (Poisson-like) regardless of p

> [!note]- Solution
> **a), b), d), e).** W-S: ring lattice (a), rewire with p (b), sweet spot at small p for small-world property (d), narrow degree distribution (e). (c) is false — W-S does NOT produce power laws. The degree distribution stays approximately Poisson because rewiring preserves the total degree of most nodes. For power-law degree distributions, use the Barabási–Albert preferential attachment model.

---

## Section 8 — Network Dynamics & Temporal Networks (L08)

### Q44. The SIS model differs from the SIR model in that:

a) SIS has no recovery — infected nodes stay infected forever
b) SIS allows recovered nodes to become susceptible again immediately (no immunity)
c) SIS only works on directed graphs
d) SIS has a higher epidemic threshold than SIR

> [!note]- Solution
> **b)** SIS: S → I → S (no immunity — recovered nodes immediately become susceptible again). SIR: S → I → R (permanent immunity after recovery). SIS models diseases like the common cold (no lasting immunity) or computer viruses (re-infection possible). SIR models diseases like measles (lasting immunity). The endemic equilibrium for SIS: I* = 1 − γ/β when β > γ.

---

### Q45. In the SIR model, R₀ = (β/γ) × ⟨k⟩. If β = 0.1, γ = 0.5, and ⟨k⟩ = 10, then R₀ equals:

a) 0.2
b) 2.0
c) 5.0
d) 0.5

> [!note]- Solution
> **b)** R₀ = (β/γ) × ⟨k⟩ = (0.1/0.5) × 10 = 0.2 × 10 = 2.0. Since R₀ = 2.0 > 1, the disease will spread — each infected individual infects 2 others on average before recovering. This is an epidemic. If ⟨k⟩ were 3 instead, R₀ = 0.6 < 1 and the disease would die out.

---

### Q46. In temporal networks, a *time-respecting path* requires:

a) All edges on the path to be active simultaneously
b) Edges on the path to activate in chronological (non-decreasing) order
c) The path to be the shortest in the static aggregated graph
d) All nodes on the path to be in the same connected component of the static graph

> [!note]- Solution
> **b)** A time-respecting path is a sequence of edges (e₁, e₂, ..., eₖ) where each edge is traversed at its activation time, and t(e₁) ≤ t(e₂) ≤ ... ≤ t(eₖ). You can only use an edge when it's active, and you must move forward in time. This means the static aggregated graph can show "phantom paths" — paths that exist in the aggregate but are impossible when temporal ordering is enforced. Temporal distance is often *longer* than static distance.

---

### Q47. [Mehrfachauswahl] Which statements about complex contagion (threshold cascades) are correct?

a) A node adopts when a fraction q of its neighbours are active
b) For global cascades, q ≤ 1/2 is generally required
c) Wide bridges (multiple edges between communities) help cascades cross community boundaries
d) Thin bridges (single edges) are sufficient for complex contagion to spread
e) Centola (2010) showed complex contagion spreads faster in clustered networks than in random networks

> [!note]- Solution
> **a), b), c), e).** Threshold model: adopt when fraction q of neighbours active (a). Global cascades need q ≤ 1/2 (b) — above this, local majority is needed, which is hard to trigger. Wide bridges provide multiple adopter neighbours across communities, supplying sufficient reinforcement (c). Centola confirmed clustered > random for complex contagion (e). (d) is false — thin bridges carry only one adopter, giving fraction 1/deg(v) ≪ q, insufficient for complex contagion.

---

### Q48. The six gaps identified across the Network Science course are:

a) Computational, Causal, Structural, Navigational, Process-Structure, Temporal
b) Spatial, Temporal, Social, Economic, Political, Cultural
c) Local, Global, Mesoscale, Microscale, Macroscale, Network-scale
d) Theoretical, Empirical, Computational, Experimental, Observational, Simulation

> [!note]- Solution
> **a)** The six gaps summarise the core tensions of the course:
> - **Computational** (L03–L04): NP-hard ideals (modularity maximisation, frustration index) vs. polynomial heuristics
> - **Causal** (L05): selection vs. socialisation — mechanism unidentifiable from cross-sectional snapshots
> - **Structural** (L06): balance theory assumes complete graphs, but real data is sparse
> - **Navigational** (L07): short paths exist (small-world) but aren't locally findable without the right structure (Kleinberg)
> - **Process-Structure** (L08): same network structure produces different outcomes for different spreading processes
> - **Temporal** (L08): static aggregation hides causal ordering, creating phantom paths

---

# PART B — Essay Questions (50%)

> *Five open questions, 10 points each. Show your reasoning. Cite formulas where applicable. Precision matters.*

---

### E1. (10 points) — Spectral Partitioning and the Graph Laplacian

Consider the following graph:

```
1 — 2 — 3
|   |   |
4 — 5 — 6
```

Edges: (1,2), (2,3), (1,4), (2,5), (3,6), (4,5), (5,6)

(a) Write down the **degree matrix** D and the **adjacency matrix** A. Compute the **Laplacian** L = D − A. (3 pts)

(b) Explain what the **Fiedler value** λ₂ and **Fiedler vector** tell you about this graph. Without computing eigenvalues exactly, predict what the spectral bisection would look like. (3 pts)

(c) Compare **spectral partitioning** with the **Girvan–Newman algorithm**. When would you prefer one over the other? (2 pts)

(d) How does spectral partitioning generalise to k > 2 communities? (2 pts)

> [!note]- Solution
> **(a)**
> Degrees: deg(1)=2, deg(2)=3, deg(3)=2, deg(4)=2, deg(5)=3, deg(6)=2.
>
> ```
>     1  2  3  4  5  6
>   ┌                ┐
> 1 │ 0  1  0  1  0  0 │     D = diag(2, 3, 2, 2, 3, 2)
> 2 │ 1  0  1  0  1  0 │
> 3 │ 0  1  0  0  0  1 │     L = D - A:
> 4 │ 1  0  0  0  1  0 │
> 5 │ 0  1  0  1  0  1 │       2 -1  0 -1  0  0
> 6 │ 0  0  1  0  1  0 │      -1  3 -1  0 -1  0
>   └                ┘       0 -1  2  0  0 -1
>                            -1  0  0  2 -1  0
>                             0 -1  0 -1  3 -1
>                             0  0 -1  0 -1  2
> ```
>
> **(b)** The graph is connected → λ₂ > 0. The Fiedler vector x₂ provides a natural bipartition: nodes with x₂(i) > 0 go to group 1, x₂(i) < 0 to group 2. Looking at the structure, the natural cut is vertical — {1, 4} vs {3, 6} with node 2 and 5 as the bridge. Spectral bisection would likely split left column {1, 4} from right column {3, 6}, with 2 and 5 assigned based on the sign of their Fiedler entries. The magnitude of λ₂ indicates how "easy" this cut is — a small λ₂ means the graph is easy to bisect.
>
> **(c)** Spectral partitioning: computes eigenvectors of L, partitions by sign of Fiedler vector. Complexity: O(n²) for eigendecomposition, or O(|E|·d) with Lanczos for sparse graphs. Best when you want a principled, algebraically motivated cut and know k in advance.
>
> Girvan–Newman: iteratively removes highest-betweenness edges. Complexity: O(n·m²). Best when you want a hierarchical decomposition (dendrogram of communities) and the graph is not too large.
>
> Prefer spectral when: the graph is large and you need a fast flat partition. Prefer Girvan–Newman when: you want to explore hierarchical community structure and interpret the dendrogram.
>
> **(d)** For k communities: compute the k smallest non-trivial eigenvectors of L (x₂, x₃, ..., xₖ). Form an n × (k−1) matrix where each row is a node's coordinates in this eigenspace. Run k-means clustering on these rows. This is **spectral clustering** — it embeds nodes in a low-dimensional space where community structure becomes geometrically separable, then uses standard clustering.

---

### E2. (10 points) — Erdős–Rényi vs. Barabási–Albert: Two Models of Network Formation

(a) Describe the **Erdős–Rényi G(n, p)** model. State its degree distribution, clustering coefficient, and the conditions for the emergence of a giant component and full connectivity. (3 pts)

(b) Describe the **Barabási–Albert preferential attachment** model. State its degree distribution, explain the "rich get richer" mechanism, and describe its robustness properties. (3 pts)

(c) A real-world collaboration network has N = 10,000 nodes, average degree ⟨k⟩ = 8, clustering C = 0.45, and a degree distribution that follows P(k) ~ k^(−2.5). Which model better describes this network, and why? (2 pts)

(d) Explain why **scale-free networks** (γ ≤ 3) have a vanishing epidemic threshold. What are the practical implications for vaccination strategies? (2 pts)

> [!note]- Solution
> **(a)** Erdős–Rényi G(n, p): n nodes, each pair connected independently with probability p.
> - Degree distribution: Binomial(n−1, p) ≈ Poisson(np) for large n — narrow, homogeneous
> - Clustering: C = p = k/(n−1) ≈ k/n → very low for large n
> - Giant component threshold: ⟨k⟩ = 1 (p = 1/n). Below: many small components. Above: one giant component.
> - Connectivity threshold: p > ln(n)/n. Above this, the graph is almost surely connected.
>
> **(b)** Barabási–Albert: start with m₀ nodes. At each step, add a new node with m edges, connecting to existing node i with probability Π(k_i) = k_i / Σ_j k_j.
> - Degree distribution: P(k) ~ 2m² k^(−3) — power law with γ = 3
> - "Rich get richer": high-degree nodes attract more connections because they are more visible/accessible
> - Robustness: robust to random failure (random removal hits peripheral nodes), fragile under targeted attack (removing hubs fragments the network rapidly)
>
> **(c)** The BA model fits better. Evidence:
> - Power-law degree distribution P(k) ~ k^(−2.5) — ER produces Poisson (narrow), BA produces power law
> - High clustering C = 0.45 — ER would give C ≈ k/n = 8/10000 = 0.0008, far below 0.45
> - Neither model perfectly explains the clustering (BA also gives low clustering for large n), but the power-law tail is the decisive signature of preferential attachment
>
> **(d)** For scale-free networks with γ ≤ 3, ⟨k²⟩ → ∞ as N → ∞. The epidemic threshold T_c ≈ ⟨k⟩ / (⟨k²⟩ − ⟨k⟩) → 0. Any non-zero transmission rate can sustain an epidemic — there is no finite threshold.
>
> Practical implication: **random vaccination cannot achieve herd immunity** in scale-free networks — you would need to vaccinate ~100% of the population. Instead, **targeted vaccination of the top 5–10% highest-degree nodes (hubs)** restores a finite epidemic threshold and is dramatically more efficient. Hubs are superspreaders: they are more likely to be infected (many contacts) and infect more others when infected.

---

### E3. (10 points) — Temporal Networks and the Process-Structure Gap

(a) Define a **time-respecting path** in a temporal network. Give a concrete example of a path that exists in the static aggregated graph but is NOT a valid time-respecting path. (3 pts)

(b) Explain the **process-structure gap**: why does the same network structure produce different outcomes for simple contagion (SIR) and complex contagion (threshold cascades)? Reference the **weak tie paradox**. (4 pts)

(c) A public-health agency wants to spread a new vaccination *behaviour* (not just awareness of the vaccine, but actual adoption). Based on what you know about simple vs. complex contagion, should they:
   (i) Seed the behaviour through weak-tie bridges to reach many communities, or
   (ii) Seed it within densely clustered communities?
   Justify your answer. (3 pts)

> [!note]- Solution
> **(a)** A time-respecting path is a sequence of temporal edges ((u₁,u₂,t₁), (u₂,u₃,t₂), ..., (uₖ,uₖ₊₁,tₖ)) where t₁ ≤ t₂ ≤ ... ≤ tₖ — edges must activate in chronological order. You can only traverse an edge at its activation time, and you must move forward in time.
>
> Example: suppose in the static graph, A–B–C is a path. But temporally, edge A–B activates at t = 5 and edge B–C activates at t = 3. In the static aggregate, the path A→B→C exists. Temporally, it is impossible: you arrive at B at t = 5, but B–C already fired at t = 3. This is a **phantom path** — visible in the aggregate, impossible in reality.
>
> **(b)** The process-structure gap: the same structural feature (e.g., a weak-tie bridge) has opposite effects depending on the spreading process.
>
> Simple contagion (SIR): one S–I contact transmits with probability β. Bridges accelerate spread — one exposure suffices. Weak ties carry the contagion to new communities that the disease hasn't reached. This is Granovetter's insight applied to dynamics.
>
> Complex contagion (threshold cascades): a node adopts only when fraction q of its neighbours are active. Bridges block spread — on a thin bridge, the adopter on the other side provides only 1/deg(v) ≪ q fraction of active neighbours. Insufficient reinforcement. The cascade stops at the bridge.
>
> The weak tie paradox: weak ties that are bridges between communities accelerate simple contagion (information, disease) but hinder complex contagion (behaviour change, norm adoption). The same network structure — weak-tie bridges — is simultaneously helpful and harmful depending on the process.
>
> **(c)** **(ii) Seed within densely clustered communities.**
>
> Vaccination *behaviour* is complex contagion — it requires social reinforcement. People don't adopt a new health behaviour after hearing about it once; they need to see multiple trusted peers adopting it. In a clustered community, when one person gets vaccinated, their friends are also friends of each other, so multiple friends see the adoption simultaneously. This pushes them past the threshold q.
>
> Seeding through weak-tie bridges (i) would spread *awareness* (simple contagion — one contact suffices to inform), but not *behaviour*. The bridge carries insufficient reinforcement for adoption. The correct strategy: seed within cohesive clusters, let the dense reinforcement drive adoption, and let wide bridges (multiple ties between communities) carry the behaviour across boundaries.

---

### E4. (10 points) — Homophily, Affiliation Networks, and the E-I Index

A university department has 20 researchers in 3 groups: A (8 members), B (7 members), C (5 members). The collaboration network has 30 edges total: 12 within A, 8 within B, 4 within C, and 6 cross-group edges.

(a) Compute the **E-I index** for this network. Interpret the result. (3 pts)

(b) Compute the **random-mixing baseline** probability of a cross-group edge. Compare the observed cross-group fraction to this baseline. Is the observed homophily stronger or weaker than expected by chance? (4 pts)

(c) Explain the difference between **selection**, **socialisation**, and **contextual correlation** as explanations for observed homophily. Why can't cross-sectional data distinguish them? (3 pts)

> [!note]- Solution
> **(a)** E-I = (E − I) / (E + I)
> - I (internal/within-group edges) = 12 + 8 + 4 = 24
> - E (external/cross-group edges) = 6
> - E + I = 30 ✓
>
> E-I = (6 − 24) / (6 + 24) = −18/30 = **−0.6**
>
> Interpretation: strong homophily. 80% of collaborations are within-group, 20% cross-group. The negative E-I indicates researchers strongly prefer collaborating within their own group.
>
> **(b)** Random-mixing baseline:
> P(cross | random) = 1 − [C(n_A, 2) + C(n_B, 2) + C(n_C, 2)] / C(N, 2)
> = 1 − [C(8,2) + C(7,2) + C(5,2)] / C(20,2)
> = 1 − [28 + 21 + 10] / 190
> = 1 − 59/190
> = 1 − 0.311
> = **0.689 ≈ 69%**
>
> Under random mixing, ~69% of edges would be cross-group. Observed: 6/30 = 20% cross-group.
>
> The observed cross-group fraction (20%) is dramatically lower than the random baseline (69%). The homophily is **much stronger than expected by chance**. The homophily index r = (H_obs − H_base)/(1 − H_base) = (0.80 − 0.311)/(1 − 0.311) = 0.489/0.689 ≈ 0.71 — very strong homophily beyond what group sizes alone predict.
>
> **(c)** Three explanations for observed homophily:
> - **Selection** (attribute → tie): similar people choose to collaborate. Researchers in group A work on similar topics, so they naturally collaborate more. The attribute (research topic) precedes and causes the tie.
> - **Socialisation** (tie → attribute): collaboration causes similarity. Researchers who happen to collaborate start adopting each other's methods and topics over time. The tie precedes and causes the attribute convergence.
> - **Contextual correlation** (confounder → both): a shared environment causes both similarity and collaboration. Researchers in the same office building or funding programme both work on similar topics AND have more opportunity to collaborate. The shared context is a confounder.
>
> Cross-sectional data (a single snapshot) cannot distinguish these because all three produce the same observable pattern: within-group edges are overrepresented. You need **longitudinal data** (tracking ties and attributes over time) to see whether similarity preceded the tie (selection) or the tie preceded similarity (socialisation), or **experiments** that manipulate one variable while holding the other constant.

---

### E5. (10 points) — Structural Balance: Camp Partitioning and the Signed Laplacian

Consider a complete signed graph on 6 nodes {A, B, C, D, E, F}:

```
A—B: +, A—C: +, A—D: −, A—E: −, A—F: −
B—C: +, B—D: −, B—E: −, B—F: −
C—D: −, C—E: −, C—F: −
D—E: +, D—F: +
E—F: +
```

(a) Check all triangles involving nodes A, D, and E. Are they balanced under strong balance? (3 pts)

(b) Determine whether the full graph is balanced. If so, give the camp partition. (3 pts)

(c) Explain why computing the **frustration index** F(G, σ) is NP-hard. What polynomial-time alternative exists to test whether a signed graph is balanced? (2 pts)

(d) How would the analysis change under **weak balance** (Davis 1967)? Would the partition change? (2 pts)

> [!note]- Solution
> **(a)** Triangles involving A, D, E:
> - {A, D, E}: A–D = −, A–E = −, D–E = +. Signs: (−, −, +). Product = (−)(−)(+) = +. Two negative edges → **balanced** ✓ (allies D and E share common enemy A)
>
> Other triangles with A:
> - {A, B, D}: (+, −, −) → balanced ✓
> - {A, B, E}: (+, −, −) → balanced ✓
> - {A, C, D}: (+, −, −) → balanced ✓
> - {A, C, E}: (+, −, −) → balanced ✓
> - {A, D, F}: (−, −, −) → **unbalanced** under strong balance ✗
>
> Wait — let me recheck {A, D, F}: A–D = −, A–F = −, D–F = +. Signs: (−, −, +). Product = +. Two negatives → **balanced** ✓.
>
> **(b)** All cross-group edges (between {A,B,C} and {D,E,F}) are negative. All within-group edges are positive.
>
> Check all 10 triangles within each camp:
> - {A,B,C}: (+,+,+) → balanced ✓
> - {D,E,F}: (+,+,+) → balanced ✓
>
> Cross-camp triangles (one from {A,B,C}, two from {D,E,F} or vice versa):
> - Pattern is always (+,−,−) or (−,−,+): two negatives and one positive → product positive → balanced ✓
>
> All C(6,3) = 20 triangles are balanced → the graph is **perfectly balanced**.
>
> **Camp partition:**
> - Camp 1: {A, B, C} — all within-camp edges positive ✓
> - Camp 2: {D, E, F} — all within-camp edges positive ✓
> - All 9 cross-camp edges are negative ✓
>
> **(c)** The frustration index F(G, σ) = minimum number of edge sign flips to achieve balance. Computing F is NP-hard because it is equivalent to MAX-CUT: finding the minimum set of edges to flip is the same as finding the partition that minimises the number of "frustrated" edges (positive edges between camps or negative edges within camps). This is the MAX-CUT problem, which is NP-hard.
>
> Polynomial-time alternative: the **signed Laplacian** test. Compute L_σ = D − A_σ where (A_σ)_ij = +1 for positive edges and −1 for negative edges. The graph is balanced iff λ₁(L_σ) = 0. This is computed via the Lanczos algorithm in O(|E|·d) time — polynomial. However, it only tells you *whether* the graph is balanced (F = 0 or F > 0), not the exact value of F.
>
> **(d)** Under weak balance (Davis 1967), the only forbidden triangle is (+,+,−). The (−,−,−) triangle is now permitted. Since all triangles in this graph have either 0 or 2 negative edges (no (−,−,−) triangles exist here), the graph is balanced under both strong and weak balance. **The partition does not change** — it remains Camp 1 = {A,B,C}, Camp 2 = {D,E,F}.
>
> The difference would matter if there were (−,−,−) triangles — under weak balance, these would be allowed and the graph could partition into k ≥ 3 camps. Here, with exactly 2 camps and no all-negative triangles, both theories agree.
