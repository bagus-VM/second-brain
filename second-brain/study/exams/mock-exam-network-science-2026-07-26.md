---
title: "Mock Exam — Network Science"
tags: [exam-prep, mock-exam, network-science, semester-1]
course: "Network Science"
exam_date: "2026-07-28"
format: "50% Antwort-Wahl-Verfahren + 50% essay"
status: current
last_updated: 2026-07-26
prerequisites: []
---

# Mock Exam — Network Science

> *50% Antwort-Wahl-Verfahren (multiple choice), 50% essay. Einfachauswahl (single-best-answer) unless marked **[Mehrfachauswahl]** (zero, one, or more correct). No notes. This is not a half-measure.*
>
> Scope: Lectures 1–8, Exercise Sheets 1–8. Professor confirmed: centrality equations, small-world equation, graph search algorithms.

---

# PART A — Antwort-Wahl-Verfahren (50%)

---

## Section 1 — Network Fundamentals & Graph Theory (L01–L02)

### Q1. In a simple undirected graph G = (V, E), the handshaking lemma states:

a) Σ deg(v) = |E|
b) Σ deg(v) = 2|E|
c) Σ deg(v) = |V|
d) Σ deg(v) = 2|V|

> [!note]- Solution
> **b)** The handshaking lemma: the sum of all vertex degrees equals twice the number of edges, because each edge contributes 1 to the degree of each of its two endpoints. For directed graphs: Σ in-deg(v) = Σ out-deg(v) = |E|.

---

### Q2. The density of a simple undirected graph with n nodes and m edges is:

a) m / (n(n−1))
b) 2m / (n(n−1))
c) 2m / n
d) m / n²

> [!note]- Solution
> **b)** Density = 2|E| / (|V|(|V|−1)). The number of possible edges in a simple undirected graph is C(n,2) = n(n−1)/2, so density = actual edges / possible edges = m / (n(n−1)/2) = 2m / (n(n−1)). Density = 1 means complete graph; density = 0 means no edges.

---

### Q3. In a directed graph, a strongly connected component (SCC) is:

a) A maximal set of nodes where every node can reach every other node by some path, ignoring edge directions
b) A maximal set of nodes where every node can reach every other node following edge directions
c) Any set of nodes with at least one edge between each pair
d) A set of nodes that are all at the same shortest-path distance from a given source

> [!note]- Solution
> **b)** Strongly connected: every node can reach every other following directed paths. (a) describes a *weakly* connected component. The giant SCC in the web bow-tie is the core that search engines crawl — IN pages can reach it but can't be reached from it.

---

### Q4. When is an Eulerian circuit guaranteed to exist in a connected undirected graph?

a) When the graph is complete
b) When every vertex has even degree
c) When exactly two vertices have odd degree
d) When the graph has no bridges

> [!note]- Solution
> **b)** An Eulerian circuit (traversing every edge exactly once and returning to start) exists iff every vertex has even degree. (c) — exactly two odd-degree vertices — guarantees an Eulerian *path* (not a circuit). Königsberg: all four vertices have odd degree → neither path nor circuit exists.

---

### Q5. [Mehrfachauswahl] Which of the following are true about BFS (Breadth-First Search)?

a) BFS finds shortest paths in unweighted graphs
b) BFS finds shortest paths in weighted graphs with non-negative weights
c) BFS explores layer by layer using a FIFO queue
d) The complexity of BFS is O(|V| + |E|)
e) BFS from node s discovers all nodes at distance k before any node at distance k+1

> [!note]- Solution
> **a), c), d), e).** BFS is the correct algorithm for *unweighted* shortest paths (a). It uses a FIFO queue and discovers nodes layer-by-layer (c). It touches each node and edge once → O(|V|+|E|) (d). Layer k = all nodes at distance exactly k, discovered before layer k+1 (e). (b) is false — for weighted graphs, use Dijkstra (non-negative) or Bellman-Ford (negative weights).

---

### Q6. Dijkstra's algorithm is preferred over BFS when:

a) The graph has negative edge weights
b) The graph is unweighted
c) The graph has non-negative edge weights
d) The graph is directed

> [!note]- Solution
> **c)** Dijkstra handles non-negative weighted shortest paths using a min-heap priority queue. For negative weights, use Bellman-Ford. For unweighted graphs, BFS suffices (every edge weight = 1). Dijkstra on an unweighted graph degenerates into BFS.

---

### Q7. Which description best fits a local bridge?

a) An edge whose removal increases the number of connected components
b) An edge (u, v) where N(u) ∩ N(v) = ∅ — the endpoints share no common neighbours
c) An edge between two nodes in different communities
d) The shortest path between two nodes

> [!note]- Solution
> **b)** A local bridge is an edge whose endpoints have no common neighbours, i.e., neighbourhood overlap O(u,v) = 0. (a) describes a *bridge* (strictly: removing it disconnects the graph). A local bridge may not be a true bridge — alternate multi-hop paths may exist — but the endpoints are socially distant (no shared friends).

---

## Section 2 — Centrality Measures (L04)

### Q8. A graph has 6 nodes. Node A has degree 3. What is the degree centrality C_D(A)?

a) 3
b) 3/6 = 0.5
c) 3/5 = 0.6
d) 3/15 = 0.2

> [!note]- Solution
> **c)** C_D(v) = deg(v) / (n − 1). With n = 6, max possible degree is 5. So C_D(A) = 3/5 = 0.6. The normalisation makes C_D range from 0 (isolated) to 1 (connected to everyone).

---

### Q9. Closeness centrality C_C(v) is defined as:

a) (n − 1) / Σ_{u≠v} d(v, u)
b) Σ_{u≠v} 1 / d(v, u), with 1/∞ = 0
c) Σ_{s≠v≠t} σ_st(v) / σ_st
d) (n − 1) / Σ_{u≠v} d(v, u)²

> [!note]- Solution
> **a)** Closeness = (n − 1) / (sum of all distances from v). It measures how quickly v can broadcast to the whole network. (b) is *harmonic* centrality — the disconnected-graph variant that handles unreachable nodes (1/∞ = 0). (c) is *betweenness* centrality — the fraction of shortest paths passing through v.

---

### Q10. Why does closeness centrality fail (or need modification) on disconnected graphs?

a) Because nodes in different components have incommensurate degrees
b) Because the shortest-path distance to an unreachable node is ∞, which makes the normalised distance sum infinite or undefined
c) Because BFS does not work on disconnected graphs
d) Because the giant component absorbs all other components

> [!note]- Solution
> **b)** If v cannot reach u, d(v, u) = ∞, so Σ d(v, u) blows up and C_C(v) → 0 for every node — the measure loses discrimination. Harmonic centrality H(v) = Σ 1/d(v, u) with 1/∞ = 0 repairs this: unreachable nodes simply contribute 0.

---

### Q11. The normalization factor for betweenness centrality in an undirected graph with n nodes is:

a) n
b) n(n − 1)
c) n(n − 1)/2
d) (n − 1)(n − 2)/2

> [!note]- Solution
> **d)** For undirected graphs, the number of ordered (unordered) pairs (s, t) with s ≠ v ≠ t is (n − 1)(n − 2)/2; this normalises raw betweenness to [0, 1]. (Beware: for directed graphs, ordered pairs count gives n(n − 1)/2 or n(n−1) depending on convention — check the lecture.)

---

### Q12. [Mehrfachauswahl] Which statements about eigenvector centrality and PageRank are correct?

a) Both assign higher centrality to nodes connected to other central nodes
b) Eigenvector centrality uses a damping factor α
c) PageRank uses a damping factor α (typically 0.85)
d) PageRank handles dangling nodes (no outgoing edges) and directed graphs more naturally than eigenvector centrality
e) PageRank scores sum to 1; they are probabilities

> [!note]- Solution
> **a), c), d), e).** Both reward connections to important neighbours (a). PageRank adds a damping factor α and a teleportation term (c), which makes the random walk ergodic and handles rank-sinks / dangling nodes naturally (d); PageRank scores are probabilities sum to 1 (e). (b) is false: eigenvector centrality uses the leading eigenvector of A directly — no damping. The damping factor and teleportation are what separate PageRank from plain eigenvector centrality.

---

### Q13. The PageRank formula is:

a) PR(v) = α Σ_{u→v} PR(u)/outdeg(u)
b) PR(v) = (1 − α)/n + α Σ_{u→v} PR(u)/outdeg(u)
c) PR(v) = (1 − α) Σ_{u→v} PR(u)/outdeg(u)
d) PR(v) = α/n + (1 − α) Σ_{u→v} PR(u)/outdeg(u)

> [!note]- Solution
> **b)** PR(v) = (1 − α)/n + α Σ_{u→v} PR(u)/outdeg(u). The (1 − α)/n term is the random-jump probability (teleportation with probability 1 − α). The α term is "follow a link with probability α." The damping factor is typically 0.85. (a) omits teleportation and gets stuck in rank-sinks; (c) and (d) invert the α and (1 − α) roles.

---

### Q14. A betweenness broker (high betweenness, low clustering) is best characterised as:

a) A node deeply embedded in a cohesive cluster
b) A node whose removal would not affect information flow
c) A node sitting on many shortest paths between other pairs, spanning a structural hole
d) A node with the highest degree

> [!note]- Solution
> **c)** High betweenness = many shortest paths pass through v = brokerage role. Low clustering = neighbours don't know each other. Together: a broker sitting in a structural hole between two otherwise-separated clusters. (a) describes an *embedded* node (high clustering), typically with lower betweenness. (d) is wrong — degree ≠ betweenness; many brokers have moderate degree but sit on the only paths between clusters.

---

## Section 3 — Strong and Weak Ties (L03)

### Q15. The clustering coefficient C_v of a node with k neighbours and T triangles through v is:

a) T / C(k, 2)
b) 2T / (k(k − 1))
c) T / k
d) k / 2T

> [!note]- Solution
> **b)** Local clustering C_v = 2 × (edges among neighbours of v) / (deg(v) × (deg(v) − 1)) = 2T / (k(k − 1)). For k = 3 with 1 triangle, C_v = 2(1)/(3·2) = 1/3. (a) is equivalent for k ≥ 2 (since C(k,2) = k(k−1)/2, T/C(k,2) = 2T/(k(k−1)) — they're algebraically identical; the canonical form is (b)).

---

### Q16. Neighbourhood overlap O(u, v) is defined as:

a) |N(u) ∩ N(v)| / |N(u) ∪ N(v)|
b) |N(u) ∪ N(v)| / |N(u) ∩ N(v)|
c) deg(u) + deg(v) / 2
d) The number of common neighbours

> [!note]- Solution
> **a)** O(u, v) = |N(u) ∩ N(v)| / |N(u) ∪ N(v)| (excluding u and v from N). High overlap = strong tie (many shared friends). O = 0 means u and v share no common neighbours — a local bridge.

---

### Q17. The Strong Triadic Closure (STC) condition states:

a) If A has ties to B and C, then B and C must be connected, regardless of tie strength
b) If A has *strong* ties to B and C, then B and C must be connected (any edge label)
c) Every triangle in the network must be closed
d) Every weak tie must be a local bridge

> [!note]- Solution
> **b)** STC condition: if a node has *strong* ties to two neighbours, those two must be connected (any label, strong or weak). The generalisation without strength is plain *triadic closure*. STC is a constraint on *labelings* — the same graph can have valid and invalid STC labelings.

---

### Q18. Under Strong Triadic Closure, what must every local bridge be?

a) A strong tie
b) A weak tie
c) A bridge (its removal disconnects the graph)
d) A tie with high neighbourhood overlap

> [!note]- Solution
> **b)** The Weak Ties Theorem (Granovetter): under STC, every local bridge must be a weak tie. Proof sketch: if the local bridge (u, v) were strong, then by STC both u and v must connect to each other's strong-tie partners — but that means they share neighbours, contradicting "no common neighbours" (local bridge = zero overlap). Hence the local bridge must be weak.

---

### Q19. Granovetter's job study is best summarised as: people hear about job opportunities mostly from

a) Their closest friends and family
b) Rarely-seen acquaintances, because they bridge to different social circles
c) Their immediate coworkers
d) The strongest ties in their network, because trust matters for job referrals

> [!note]- Solution
> **b)** Granovetter's key finding: the weak ties (acquaintances) carry novel, non-redundant information because they sit in different social circles (low neighbourhood overlap, often local bridges). Strong ties share your social world and know what you already know. This is *the* empirical grounding of the weak-ties hypothesis.

---

### Q20. [Mehrfachauswahl] Which of the following are correct about triadic closure?

a) If A has edges to B and C, the formation of edge B–C is more likely than for two random nodes
b) Triadic closure is driven by opportunity, trust, and social pressure
c) Triadic closure increases the clustering coefficients of the nodes involved
d) Triadic closure always shrinks the diameter of the graph

> [!note]- Solution
> **a), b), c).** Triadic closure: the friend-of-my-friend-is-my-friend tendency (a), driven by opportunity/trust/pressure (b). Closing a triangle raises the clustering coefficients of all three nodes (c). (d) is false in general — triadic closure increases local redundancy (more edges within a neighbourhood), which can *increase* the number of hops needed to escape a dense cluster, even though overall it contributes to shrinking average path lengths over time.

---

## Section 4 — Communities & Modularity (L05)

### Q21. The modularity Q of a partition is defined as:

a) Q = (1/2m) Σ_c [e_c − a_c²/4m], where e_c = edges inside c, a_c = sum of degrees in c, m = total edges
b) Q = m / (n(n − 1))
c) Q = Σ_c e_c²
d) Q = (1/2m) Σ_c [e_c − a_c²], where a_c = sum of degrees in c, m = total edges

> [!note]- Solution
> **a)** Q = (1/2m) Σ_c [e_c − (a_c² / 4m)]. Each community contributes (actual internal edges) minus (expected internal edges under random rewiring with the same degree distribution). Q > 0 means more community structure than random; Q = 0 random; Q = 1 perfect. Real networks typically Q ∈ [0.3, 0.7]. Maximising Q is NP-hard — all practical methods are heuristics.

---

### Q22. Modularity Q typically takes values for real-world networks in:

a) [−1, +1]
b) [0.1, 0.3]
c) [0.3, 0.7]
d) [0.7, 1.0]

> [!note]- Solution
> **c)** Real networks typically have Q ∈ [0.3, 0.7]. Q near 0 means no community structure; Q = 1 means perfect modularity (rare). The resolution limit means very high Q can be artificial from over-merging.

---

### Q23. The Girvan–Newman community detection algorithm:

a) Iteratively removes the lowest-betweenness edges
b) Iteratively removes the highest-betweenness edges
c) Greedily merges communities that maximise ΔQ
d) Uses spectral methods (Fiedler vector)

> [!note]- Solution
> **b)** Girvan–Newman: top-down divisive. Iteratively remove the edge with the highest *edge betweenness* — bridges between communities carry the most shortest paths. Returns an iterator: `next(gn)` gives 2 communities, then 3, etc. (c) describes greedy modularity maximisation; (d) describes spectral partitioning.

---

### Q24. [Mehrfachauswahl] Which are correct about the modularity *resolution limit*?

a) It prevents modularity from detecting communities smaller than approximately √(2m)
b) Small communities embedded in large networks may be merged into larger groups even when they are clearly distinct
c) It applies only to the Louvain algorithm
d) On Zachary's karate club, greedy modularity often finds 3–4 communities instead of the known 2 factions

> [!note]- Solution
> **a), b), d).** The resolution limit: modularity cannot detect communities smaller than a scale that depends on the total number of edges (≈ √(2m)). Small communities in large networks get lumped into larger ones (a, b). On the karate club, greedy modularity frequently over-splits the larger faction (d). (c) is false — the resolution limit is a *modularity* property, not specific to one algorithm; it affects any Q-maximisation method.

---

### Q25. Which algorithm guarantees well-connected communities by including a refinement step after aggregation?

a) Greedy modularity maximisation
b) Girvan–Newman
c) Louvain
d) Leiden

> [!note]- Solution
> **d)** Leiden is an improvement over Louvain. It adds a refinement step *before* aggregation that guarantees communities are internally well-connected (no disconnected pieces inside a community). Louvain can produce internally disconnected communities because it merges greedily without refinement. Both are agglomerative and local.

---

## Section 5 — Social Context (L06)

### Q26. The E-I (External–Internal) index is defined as:

a) (E + I) / (E − I), where E = external edges and I = internal edges
b) (E − I) / (E + I)
c) E / I
d) I / E

> [!note]- Solution
> **b)** E-I index = (E − I) / (E + I), where E = external (cross-group) edges and I = internal (within-group) edges. Range −1 (pure homophily, all ties internal) to +1 (pure heterophily, all ties external). 0 = neutral mixing. Every edge is either external or internal, so E + I = total |E|.

---

### Q27. If a network has E-I index = −0.75, the network shows:

a) Strong heterophily
b) Weak homophily
c) Strong homophily (most ties are within-group)
d) Neutral mixing

> [!note]- Solution
> **c)** E-I = −0.75 is strongly negative → strong homophily. The vast majority of ties are within-group (E = 1, I = 7 gives (1 − 7)/(1 + 7) = −0.75). +0.75 would be the heterophilic mirror.

---

### Q28. An affiliation (bipartite) network G = (U, V, E) has edges only between U and V (e.g., students and courses). When projected onto the student layer:

a) All course information is preserved with full granularity
b) Two students are connected iff they share at least one course; specific courses and tie-strength granularity are lost
c) The projection always produces a tree
d) The projection is identical to the original bipartite graph

> [!note]- Solution
> **b)** Projection connects students who share at least one affiliation (course). This loses: (a) which specific course generated the tie, (b) the course nodes themselves, (c) tie-strength granularity unless edge weights are kept (students sharing 3 courses vs. 1). Projection can manufacture dense cliques from one large course (C(s, 2) = s(s−1)/2 edges for s students in one course).

---

### Q29. [Mehrfachauswahl] Which three mechanisms appear in affiliation networks as analogues of triadic closure?

a) Triadic closure (A–B and A–C predicts B–C)
b) Focal closure (B and C both attend the same course → B–C forms)
c) Membership closure (B is friends with C who is in course X → B joins X)
d) Random rewiring (edges are randomly flipped between cohorts)
e) Preferential attachment (new agents bind to the highest-degree existing node)

> [!note]- Solution
> **a), b), c).** In affiliation networks there are three closure mechanisms: *triadic* closure (open triad closes), *focal* closure (shared affiliation creates the edge), *membership* closure (a friend pulls you into a new affiliation). Kossinets & Watts (2006) empirically found all three operating in a university evolving network.

---

### Q30. Schelling's segregation model shows that:

a) Strong individual preferences are required for segregation
b) Mild individual preferences (e.g., 30–40% same-type neighbours) can produce strong global segregation through cascading dynamics
c) Segregation only occurs when agents are explicitly racist
d) Homophily has nothing to do with segregation

> [!note]- Solution
> **b)** Schelling's profound insight: mild individual preferences (just 30–40% same-type neighbours) amplify through cascading moves — when one agent relocates, neighbourhoods change, triggering further moves. The macro-level segregation is far stronger than any micro-level preference. The corollary: you *cannot* infer individual preferences from aggregate outcomes (an identification problem).

---

## Section 6 — Structural Balance (L07)

### Q31. Under *strong* structural balance (Cartwright & Harary 1956), which triangles are balanced?

a) Only (+,+,+) 
b) (+,+,+) and (+,−,−) — positive product of edge signs (0 or 2 negatives)
c) (+,+,+) and (−,−,−)
d) Only (+,−,−)

> [!note]- Solution
> **b)** A triangle is balanced iff the product of its edges is positive, i.e., an *even* number of negative edges (0 or 2). Balanced: (+,+,+) and (+,−,−). Unbalanced: (+,+,−) and (−,−,−). The (+,+,−) case is the canonical social-tension triad ("my friend hates my friend").

---

### Q32. Under *weak* balance (Davis 1967), which triangle is also allowed (in addition to the strong ones)?

a) (+,+,−)
b) (+,−,−)
c) (−,−,−)
d) None — weak balance forbids the same triangles as strong balance

> [!note]- Solution
> **c)** Weak balance forbids only (+,+,−). It allows (−,−,−). Three mutual enemies are stable under weak balance → multi-polar worlds (3+ camps) become possible. Under strong balance, (−,−,−) is forbidden — forces a coalition to form, resulting in exactly 2 camps.

---

### Q33. The Balance Theorem (Cartwright & Harary 1956) states that if a complete signed graph is balanced, the nodes partition into at most:

a) 1 camp
b) 2 camps — within-camp edges positive, between-camp edges negative
c) k ≥ 3 camps
d) An arbitrary number of camps

> [!note]- Solution
> **b)** Strong balance forces exactly 2 camps (one if all edges positive). All within-camp edges are positive (friends); all between-camp edges are negative (rivals). Weak balance (Davis 1967) generalises to k ≥ 1 camps: (−,−,−) triangles are allowed, so multi-polar worlds persist.

---

### Q34. The frustration index F(G, σ) is defined as:

a) The number of positive edges in the graph
b) The number of negative edges in the graph
c) The minimum number of edge sign flips needed to make the graph balanced
d) The number of unbalanced triangles in the graph

> [!note]- Solution
> **c)** F(G, σ) = minimum number of edge sign flips needed to achieve balance. Computing F is **NP-hard** (Sintos & Tsaparas 2014, equivalent to MAX-CUT). The polynomial-time *test* for balance uses the signed Laplacian L_σ = D − A_σ: λ₁(L_σ) = 0 ⟺ graph is balanced.

---

### Q35. A signed graph has triangular composition (−,−,+,+,+,−,−,+). Which of the four triad types is most common in international relations data as the unbalanced tension pattern?

a) (−,−,−)
b) (+,+,−)
c) (−,+,−)
d) (+,+,+)

> [!note]- Solution
> **c)** The (+,+,−) triad is empirically *rare* — about 8% of triangles vs. ~37.5% expected by random signing — but it is the canonical *tension* pattern. (−,−,−) is also unbalanced but represents three mutual enemies, which in practice is also rare. The (+,+,−) pattern is the one balance theory predicts will resolve (by flipping one sign) — e.g., a country choosing a side between two hostile allies. The way the question phrases "(−,+,−)" refers to the same triangle under sign-product parity.

---

## Section 7 — Small-World Networks (L08)

### Q36. The small-world index σ is defined as:

a) σ = (C/C_rand) × (L_rand/L)
b) σ = (C/C_rand) / (L/L_rand)
c) σ = C × L
d) σ = (L/L_rand) / (C/C_rand)

> [!note]- Solution
> **b)** σ = (C/C_rand) / (L/L_rand), where C = average clustering of real graph, C_rand = average clustering of random graph with same n and m, L = average shortest path length, L_rand = correspondingly for random. σ >> 1 (typically > 3) means small-world: high clustering with short paths. σ ≈ 1 means random-like.

---

### Q37. For a network with N = 10^9 users and average degree k = 200, the estimated average path length d ≈ log(N)/log(k) is approximately:

a) ~3.9 hops
b) ~4.6 hops
c) ~6 hops (Milgram)
d) ~20 hops

> [!note]- Solution
> **a)** d ≈ log(10^9)/log(200) ≈ 20.723/5.298 ≈ 3.9. The formula is the random-graph approximation. Real social networks are usually close to this or slightly longer (clustering creates dead ends) — Milgram's ~6 is *longer* than the random-graph prediction, because real graphs have clustering that traps walks.

---

### Q38. The Watts–Strogatz model produces:

a) Scale-free networks with a power-law degree distribution
b) Small-world networks with a Poisson-like (narrow) degree distribution
c) Networks identical to a complete graph
d) Networks with zero clustering

> [!note]- Solution
> **b)** W-S: start with a ring lattice (uniform degree), rewire each edge with probability p. It interpolates between a regular lattice (p = 0) and a random graph (p = 1). The degree distribution stays Poisson-like (narrow) because rewiring doesn't change k much. For a power-law (scale-free) degree distribution, you need the Barabási–Albert preferential-attachment model.

---

### Q39. In a Watts–Strogatz sweep, what happens to C(p)/C(0) and L(p)/L(0) as p increases from 0 to 1?

a) Both drop sharply around p ≈ 0.01
b) L(p) drops sharply around p ≈ 0.01; C(p) stays near C(0) until much larger p
c) C(p) drops sharply around p ≈ 0.01; L(p) stays near L(0) until much larger p
d) Both stay roughly constant until p ≈ 0.5

> [!note]- Solution
> **b)** L drops sharply even at p ≈ 0.01 — a few shortcuts collapse global distances — while C stays near C(0) until much larger p, since clustering is local and only a few triangles are broken per shortcut. The sweet spot p ∈ [0.01, 0.1] gives L ≈ L_rand but C >> C_rand — the small-world regime.

---

### Q40. Web bow-tie structure (Broder et al. 2000). Pages in the IN component:

a) Are mutually reachable with the SCC core
b) Can reach the SCC core but cannot be reached from it
c) Are reachable from the SCC core but cannot reach back
d) Are reachable from tendrils

> [!note]- Solution
> **b)** IN pages *link into* the SCC (can reach it) but receive no links from it (cannot be reached from the SCC). Practical consequence: crawlers starting from the SCC hub cannot discover IN pages — they are invisible to link-following crawls. This is the crawlability gap. (c) describes OUT.

---

### Q41. [Mehrfachauswahl] Which statements about scale-free networks are correct?

a) Degree distribution follows a power law P(k) ~ k^(−γ)
b) For γ ≤ 3, the second moment ⟨k²⟩ diverges as N → ∞
c) Scale-free networks are robust to random failure but vulnerable to targeted attack
d) The epidemic threshold T_c on a scale-free network (γ ≤ 3) is finite and non-zero
e) Hubs act as shortcuts, making distances often shorter than log N / log k

> [!note]- Solution
> **a), b), c), e).** Power-law degree distribution (a); divergent ⟨k²⟩ for γ ≤ 3 (b); robust to random failures (most removals hit peripheral nodes) but fragile under targeted removal of hubs (c); hubs shorten distances below the random-graph prediction (e). (d) is *false* — for γ ≤ 3, the epidemic threshold T_c = ⟨k⟩/⟨k²⟩ → 0. Any non-zero transmission rate can sustain an epidemic; no finite threshold exists.

---

### Q42. Kleinberg's navigability theorem states that on a 2D grid augmented with long-range links drawn from a power-law distribution r^(-α), greedy routing achieves O((log N)²) delivery time iff:

a) α = 0
b) α = 1
c) α = d (the grid dimension)
d) α = 2d

> [!note]- Solution
> **c)** Kleinberg (2000): greedily routing to the target via the neighbour closest in Euclidean distance achieves polylog delivery time iff α = d (the exponent equals the grid dimension). For α ≠ d, no poly-log algorithm exists — the structure is "small-world" but not *navigable*. On a 2D grid, α = 2 is optimal.

---

## Section 8 — Network Dynamics (L08)

### Q43. The SIR model on a network has states S → I → R. An epidemic spreads (R₀ > 1) when:

a) R₀ = (β/γ) × ⟨k⟩ > 1
b) R₀ = β × ⟨k⟩ > 1
c) R₀ < 1
d) R₀ = γ / β

> [!note]- Solution
> **a)** R₀ = (β/γ) × ⟨k⟩. R₀ > 1 means each infected individual infects more than one susceptible on average before recovery. R₀ < 1 → epidemic dies out. Here β = spreading rate per contact, γ = recovery rate, ⟨k⟩ = average degree. Higher ⟨k⟩ (denser network) makes epidemics more likely.

---

### Q44. The threshold-cascade adoption rule is:

a) Node v adopts if at least one neighbour is active
b) Node v adopts if a *fraction* q of its neighbours are active
c) Node v adopts if its degree exceeds q
d) Node v adopts with probability q per step

> [!note]- Solution
> **b)** In the Watts threshold-cascade model, v adopts when |active neighbours| / |total neighbours| ≥ q — a fraction threshold. For global cascades, q ≤ 1/2 is required; q > 1/2 makes local majority-needed cascades very hard to trigger. Wide bridges (multiple edges across communities) help cascades cross; thin bridges block them.

---

### Q45. The weak tie paradox of contagion states that:

a) Weak ties always accelerate contagion
b) Weak ties hurt *simple* contagion (disease, rumours) but help *complex* contagion (behaviour)
c) Weak ties help *simple* contagion but hurt *complex* contagion
d) Weak ties never affect contagion

> [!note]- Solution
> **c)** The paradox: the same weak ties that *accelerate simple contagion* (one contact suffices to transmit disease/rumours — bridges spread them across communities) actually *block complex contagion* (where adoption requires reinforcement — multiple adopting neighbours). On a thin bridge with one adopter on the other side, the fraction of active neighbours is below threshold q, and the cascade stops.

---

### Q46. Centola's 2010 experiment showed that:

a) A health behaviour spread faster in random networks than in clustered networks
b) A health behaviour spread faster in clustered networks (~54% adoption) than in random networks (~38%), because dense overlapping neighbourhoods provide social reinforcement for complex contagion
c) Network structure does not affect behaviour spread
d) Simple contagion behaves like complex contagion

> [!note]- Solution
> **b)** Centola (2010): same degree, same diameter — only clustering differed. The clustered network reached 54% adoption vs. 38% in random. The clustered network provides *redundant* social reinforcement: in a dense neighbourhood, when one node adopts, multiple of its friends see the adoption simultaneously, each tipping past threshold q. In random networks, adopters are scattered — each neighbour only sees adoption from one source, below threshold for complex contagion.

---

# PART B — Essay Questions (50%)

> *Five open questions, 10 points each. Show your reasoning. Cite formulas. German academic standards apply.*

---

### E1. (10 points) — Centrality Measures in Practice

Consider the following undirected graph with 8 nodes:

```
Edges: 1–2, 1–5, 2–3, 3–4, 3–7, 4–8, 5–6, 6–7, 7–8
```

(a) Compute **degree centrality** C_D for all 8 nodes (normalised). (3 pts)

(b) For **node 3**: compute its **closeness centrality** C_C. Show all pairwise distances. (3 pts)

(c) Identify the node with the highest **betweenness centrality** *by inspection*. Argue structurally why this node sits on many shortest paths — what does this tell you about its network role? (2 pts)

(d) When would you pick harmonic centrality over closeness centrality? Give a concrete example. (2 pts)

> [!note]- Solution
> **(a)** n = 8, divide by 7.
> - Node 1: deg = 2 → 2/7 ≈ 0.286
> - Node 2: deg = 2 → 0.286
> - Node 3: deg = 3 → 3/7 ≈ 0.429  ← highest (tied with 7)
> - Node 4: deg = 2 → 0.286
> - Node 5: deg = 2 → 0.286
> - Node 6: deg = 2 → 0.286
> - Node 7: deg = 3 → 0.429  ← highest (tied with 3)
> - Node 8: deg = 2 → 0.286
>
> Nodes 3 and 7 tie at the top by degree centricity.
>
> **(b)** Distances from node 3 to every other node (by BFS from 3):
> - d(3, 1) = 2 (via 2)
> - d(3, 2) = 1
> - d(3, 4) = 1
> - d(3, 5) = 3 (via 2 → 1 → 5)
> - d(3, 6) = 2 (via 7)
> - d(3, 7) = 1
> - d(3, 8) = 2 (via 4 or via 7 — multiple shortest paths)
>
> Σ = 2 + 1 + 1 + 3 + 2 + 1 + 2 = 12
>
> C_C(3) = (n − 1) / Σ d(3, u) = 7/12 ≈ 0.583
>
> **(c)** Node 3 (or 7) sits at the structural boundary between the left half (1, 2, 5, 6) and the right half (4, 8). Shortest paths from {1, 2, 5} to {4, 8} pass through 3 either directly (via (3, 4)) or via 7. Node 3 acts as a *broker* — sitting on the boundary between two loosely connected clusters, controlling information flow. Removal of node 3 would increase distances between the halves.
>
> **(d)** Pick harmonic centrality on disconnected graphs. Closeness is undefined or trivially 0 when unreachable nodes contribute ∞ to Σ d. Harmonic: H(v) = Σ_{u≠v} 1/d(v, u) with 1/∞ = 0. Unreachable nodes contribute 0 — preserves discrimination. Example: web graphs where the SCC core cannot reach IN-component pages — closeness on the SCC alone is misleading; harmonic remains meaningful.

---

### E2. (10 points) — Small-World Networks

A collaboration network has N = 10⁶ researchers and average degree k = 50.

(a) Estimate the average path length using d ≈ log(N)/log(k). (2 pts)

(b) The measured average path length is L = 3.2, with average clustering C = 0.72. A random graph with the same N and k has C_rand = 5 × 10⁻⁵ and L_rand = 2.8. Compute the **small-world index** σ. Is this a small-world network? (4 pts)

(c) Explain the **Watts–Strogatz model**. Describe what happens to C(p)/C(0) and L(p)/L(0) as p increases from 0 to 1. Why is the range p ∈ [0.01, 0.1] called the small-world regime? (4 pts)

> [!note]- Solution
> **(a)** d ≈ log(10⁶)/log(50) = 6 / 1.699 ≈ 3.53 hops.
>
> **(b)** σ = (C/C_rand) / (L/L_rand)
> = (0.72 / 5 × 10⁻⁵) / (3.2 / 2.8)
> = (14 400) / (1.143)
> ≈ 12 600.
>
> σ ≫ 3 — this is a strong small-world signal. The clustering is enormous relative to random while path length remains near random. The network combines high local cohesion (friend-of-friend triangles abounding) with global compactness (everyone within a few hops).
>
> **(c)** W-S model:
> - Start with a ring of n nodes, each connected to its k nearest neighbours (regular lattice — high C, long L).
> - Rewire each edge with probability p.
> - p = 0: pure lattice, high C, L ~ n/(2k).
> - p = 1: random graph — low C, short L ≈ log n / log k.
>
> As p increases, L(p) drops *sharply* around p ≈ 0.01 — a few rewired shortcuts collapse global distances, because L is a *global* property highly sensitive to bridges. C(p) stays near C(0) until much larger p — clustering is a *local* property, and one shortcut breaks only a few triangles.
>
> The small-world sweet spot p ∈ [0.01, 0.1] is where L(p) ≈ L_rand but C(p) ≈ C(0). The graph is *locally dense* like a lattice and *globally compact* like a random graph. This explains real social networks: most of your friends know each other (high clustering), yet you can reach any random stranger in ≈ 6 steps (short paths).
>
> **Limitation:** W-S preserves a narrow Poisson-like degree distribution — it cannot reproduce the power laws seen in real networks. Barabási–Albert preferential attachment gives P(k) ~ k⁻³ — scalefree networks.

---

### E3. (10 points) — Modularity, Structural Holes, and Community Detection

(a) State the **modularity Q** formula, defining every term. Explain what Q = 0, Q = 1, and Q ∈ [0.3, 0.7] mean. (4 pts)

(b) Compare **Girvan–Newman**, **greedy modularity maximisation**, and the **Louvain algorithm** in terms of strategy, complexity, and one key strength/weakness each. (3 pts)

(c) Explain the **modularity resolution limit** with a concrete example. (3 pts)

> [!note]- Solution
> **(a)** Q = (1/2m) Σ_c [e_c − (a_c² / 4m)]
> - m = total edges
> - e_c = edges inside community c
> - a_c = sum of degrees of nodes in c
>
> Interpretation:
> - Q = 0: community structure is no better than random rewiring with the same degree distribution.
> - Q = 1: perfect modularity — every community is fully internal and disconnected from others.
> - Real networks: Q ∈ [0.3, 0.7] — meaningful but not perfect community structure.
>
> Maximising Q is NP-hard — every practical method is a heuristic.
>
> **(b)** Three algorithms:
>
> | Algorithm | Strategy | Complexity | Strength | Weakness |
> |---|---|---|---|---|
> | Girvan–Newman | Divisive (top-down): iteratively remove highest-edge-betweenness edges | O(n·m²) | Discovers hierarchical structure; interpretable | Slow on large graphs |
> | Greedy Modularity | Agglomerative (bottom-up): merge pairs maximising ΔQ | O(n log² n) | Fast, simple heuristic | Over-merges due to resolution limit |
> | Louvain | Local moves + super-node aggregation, iterative | O(n log n) (effectively O(m)) | Very fast, scales to millions of nodes | Can produce internally disconnected communities; local optima |
>
> Leiden addresses the disconnect issue of Louvain by adding a refinement step that guarantees internally connected communities.
>
> **(c)** Resolution limit: modularity cannot detect communities smaller than approximately √(2m). In a large network, two small but distinct communities may be merged because the expected edge count a² / 4m becomes non-trivial relative to the actual internal edges.
>
> *Example:* Greedy modularity on the 34-node Karate Club (m = 78) frequently returns 3–4 communities instead of the known 2 factions. The smaller faction (~16 nodes) is "too small" against the random baseline for Q-maximisation to prefer it standalone; the larger faction gets split so Q climbs.

---

### E4. (10 points) — Weak Ties, Contagion, and the Counterintuitive Role of Bridges

(a) State the **Strong Triadic Closure** condition and prove the **Weak Ties Theorem** — under STC, every local bridge must be a weak tie. (4 pts)

(b) Explain the **weak tie paradox of contagion**. Why do weak ties *accelerate* simple contagion (disease) but *hinder* complex contagion (behaviour change)? Reference the **Centola (2010) experiment**. (4 pts)

(c) Practical implication: design an intervention to spread a public-health *behaviour* (something requiring reinforcement) versus a *piece of news*. How do the network structures you exploit differ? (2 pts)

> [!note]- Solution
> **(a)** STC condition: if a node A has *strong* ties to both B and C, then B and C must be connected (any label).
>
> Proof sketch (Weak Ties Theorem):
> - Suppose (A, B) is a *local bridge*, meaning N(A) ∩ N(B) = ∅ (no shared friends).
> - Suppose (A, B) is a *strong* tie.
> - Pick any other strong tie of A, say (A, C).
> - By STC, B and C must be connected.
> - But then C ∈ N(A) and C ∈ N(B) (since B–C exist), so N(A) ∩ N(B) ≠ ∅ — contradicting the local-bridge definition.
> - Conclusion: the local bridge (A, B) cannot be strong. It must be weak.
>
> Intuition: weak ties are the only connection to *different* social spheres (low overlap), and STC forbids them from being strong.
>
> **(b)** Simple contagion: one S–I contact transmits. Weak ties (bridges) carry the contagion across communities — Granovetter's insight applied to dynamics. The bridge is *sufficient*: one exposure is enough.
>
> Complex contagion: adoption requires social reinforcement — a *fraction* q of neighbours must be active. On a *thin* bridge with only one adopter on the other side, the fraction of active neighbours is ≈ 1/deg(v) < q. The cascade *stops* — there is insufficient reinforcement across the bridge.
>
> The paradox: the same structural feature (weak-tie bridges) accelerates simple contagion but blocks complex contagion. They are *help* and *harm* simultaneously.
>
> Centola (2010) confirmed empirically: a health behaviour spread *faster in clustered networks* (54%) than random (38%), despite identical degree and diameter. The clustered neighbourhood provides redundant reinforcement — when one node adopts, multiple friends simultaneously cross threshold q. In random networks, adopters are scattered — each neighbour sees adoption from a single source.
>
> **(c)** *Behaviour* (complex contagion): exploit clustering. Recruit through cohesive groups — community leaders, embedded social circles. Dense reinforcement is what compels behaviour change. Avoid relying on weak-tie bridges — they have too few adopters per contact.
>
> *News* (simple contagion): exploit weak ties and bridges. Seed hubs and let the bridges carry the message across communities. One contact is enough; wide bridges accelerate spread.

---

### E5. (10 points) — Structural Balance in a Signed Network

Consider a complete signed graph on 5 nodes {A, B, C, D, E}:

```
A—B: +, A—C: +, A—D: −, A—E: −
B—C: +, B—D: −, B—E: −
C—D: −, C—E: −
D—E: +
```

(a) Determine whether this network is **balanced** under *strong* balance theory by checking every triangle. Show your reasoning. (4 pts)

(b) If balanced, give the **camp partition**. If not, identify a minimum set of edges to flip to achieve balance. (2 pts)

(c) Explain the difference between **strong balance** (Cartwright & Harary 1956) and **weak balance** (Davis 1967). How many camps does each allow, and which triangle does weak balance additionally permit? (2 pts)

(d) Name the **polynomial-time** test that can determine whether a signed graph is balanced without enumerating all triangles. How is it computed? (2 pts)

> [!note]- Solution
> **(a)** There are C(5, 3) = 10 triangles. A triangle is balanced iff its edge-sign product is positive (i.e., 0 or 2 negative edges — even number).
>
> - {A, B, C}: (+, +, +) product +, balanced ✓
> - {A, B, D}: (+, −, −) product +, balanced ✓
> - {A, B, E}: (+, −, −) product +, balanced ✓
> - {A, C, D}: (+, −, −) product +, balanced ✓
> - {A, C, E}: (+, −, −) product +, balanced ✓
> - {A, D, E}: (−, −, +) product +, balanced ✓
> - {B, C, D}: (+, −, −) product +, balanced ✓
> - {B, C, E}: (+, −, −) product +, balanced ✓
> - {B, D, E}: (−, −, +) product +, balanced ✓
> - {C, D, E}: (−, −, +) product +, balanced ✓
>
> All 10 triangles are balanced → the network is perfectly balanced under strong balance.
>
> **(b)** Camp partition (predicted by the Balance Theorem):
> - **Camp 1:** {A, B, C} — all three edges positive (A–B, A–C, B–C).
> - **Camp 2:** {D, E} — D–E positive.
> - All cross-camp edges are negative:
>   - A–D, A–E, B–D, B–E, C–D, C–E all signed negative ✓
>
> Partition is valid.
>
> **(c)** Strong balance (Cartwright & Harary 1956): forbids both (+,+,−) and (−,−,−) triangles. Forces exactly 2 camps (or 1 camp of all-positive). All within-camp edges positive, all between-camp edges negative.
>
> Weak balance (Davis 1967): forbids *only* (+,+,−). Allows (−,−,−) as balanced — three mutual enemies are now stable. This permits k ≥ 1 camps (multi-polar world). E.g., three mutually hostile countries are stable under weak balance; under strong balance, they must resolve into two camps.
>
> **(d)** The **signed Laplacian** test: L_σ = D − A_σ where (A_σ)_ij = +1 for positive edges and −1 for negative edges. The graph is balanced *iff* the smallest eigenvalue of L_σ is λ₁ = 0. Computed with the Lanczos algorithm in O(|E| · d) time, polynomial in the graph size. For general graphs (not complete), the *cycle criterion* gives another polynomial check via BFS: a graph is balanced iff every cycle contains an even number of negative edges.