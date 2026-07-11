---
title: "Exercise Sheet 8 — Small-World Networks"
tags:
  - practice
  - network-science
  - semester-1
course: "Network Science"
status: current
last_updated: 2026-07-11
---

# Exercise Sheet 8 — Small-World Networks

## Exercises

### 8.A The Small-World Concept

**Exercise 8.A.1: Degrees of Separation (Estimation)**

A social network has N = 10^9 users and average degree k = 200.

1. Estimate the average path length using d ≈ log(N)/log(k).
2. Compare the result to Milgram's ≈ 6 for the US population (≈ 2 × 10^8).
3. When are real networks shorter or longer than the random baseline?
4. Recompute d if the average degree drops to k = 10.

> [!note]- Solution
> 1. d ≈ log(10^9)/log(200) ≈ 20.7/5.3 ≈ 3.9 hops.
> 2. With N = 2 × 10^8 the formula gives ≈ 3.6. Milgram observed ≈ 5 to 6. Real networks are not random: local clustering creates "dead ends" that lengthen routing chains.
> 3. Real networks are shorter than the random baseline when hubs act as super-shortcuts. They are longer when high clustering traps walks inside communities.
> 4. d ≈ log(10^9)/log(10) = 9. Dropping the degree from 200 to 10 more than doubles the expected path length.

**Exercise 8.A.2: Is Karate Club a Small World?**

Using `nx.karate_club_graph()`:

1. Compute the average clustering C and the average shortest path length L.
2. Generate a random graph with the same n and m. Compute C_rand and L_rand.
3. Compute the small-world index σ = (C/C_rand)/(L/L_rand).
4. Compare to a pure ring lattice. What pattern emerges?

> [!note]- Solution
> ```python
> import networkx as nx
>
> G = nx.karate_club_graph()
> C_real = nx.average_clustering(G)
> L_real = nx.average_shortest_path_length(G)
>
> R = nx.gnm_random_graph(len(G), G.number_of_edges(), seed=42)
> C_rand = nx.average_clustering(R)
> L_rand = nx.average_shortest_path_length(R)
>
> sigma = (C_real / C_rand) / (L_real / L_rand)
> ```
>
> The karate club has C/C_rand ≈ 4 but L/L_rand ≈ 1: much higher clustering than random, with a similar path length. A high σ (typically > 3) is the small-world signature. The graph is locally cliquey like a lattice and globally compact like a random graph.

### 8.B Rewiring and Path Lengths

**Exercise 8.B.1: The Rewiring Intuition**

A 20-node ring lattice with 4 nearest-neighbour connections each. Average path ≈ 5, clustering ≈ 0.5.

1. What is the maximum reduction in path length from rewiring one edge?
2. Why does rewiring destroy clustering more slowly than it shortens paths?
3. Sketch C(p) and L(p) as p goes from 0 to 1. Where is the "sweet spot"?
4. What does this say about real social networks?

> [!note]- Solution
> 1. A single shortcut connecting maximally distant nodes (distance ≈ N/2 = 10) can roughly halve the diameter. One shortcut has a disproportionately large global effect.
> 2. Clustering measures local triangle density. One rewired edge breaks at most a few triangles, leaving most local structure intact. Path length is a global property, and it is highly sensitive to a single bridge.
> 3. L(p) drops steeply around p ∼ 0.01. C(p) stays near C(0) until moderate p. The sweet spot is p ∈ [0.01, 0.1], the small-world regime.
> 4. Real social networks sit in this regime: high local clustering combined with rare long-range weak ties.

**Exercise 8.B.2: Watts-Strogatz Sweep**

Sweep p from 0.001 to 1.0 (log-spaced) for `nx.watts_strogatz_graph(n=100, k=6, p)`:

1. Compute the normalised ratios C(p)/C0 and L(p)/L0.
2. Plot both against log(p).
3. Identify the small-world regime.
4. Is the transition sharp or gradual?

> [!note]- Solution
> ```python
> import networkx as nx
> import numpy as np
>
> n, k = 100, 6
> ps = np.logspace(-3, 0, 20)
> G0 = nx.watts_strogatz_graph(n, k, 0)
> C0 = nx.average_clustering(G0)
> L0 = nx.average_shortest_path_length(G0)
>
> results = []
> for p in ps:
>     G = nx.watts_strogatz_graph(n, k, p, seed=42)
>     results.append((nx.average_clustering(G) / C0,
>                     nx.average_shortest_path_length(G) / L0))
> ```
>
> L(p) collapses sharply even at p ≈ 0.01, while C(p) stays high until much larger p. The sweet spot p ∈ [0.01, 0.1] is where the network is locally dense and globally compact. The transition in L(p) is sharp. The decay of C(p) is gradual.

### 8.D Web Bow-Tie

**Exercise 8.D.1: Web Core and Periphery**

Directed graph with 9 nodes:

- SCC core: A → B → C → A
- IN: D → A, E → B
- OUT: C → F, B → G
- Tendril: D → H
- Isolated: I

1. Identify all strongly connected components.
2. Classify each node (SCC / IN / OUT / tendril / isolated).
3. Which nodes can reach each other?
4. What does IN vs. OUT vs. SCC mean for a web page?

> [!note]- Solution
> 1. One non-trivial SCC: {A, B, C}. Every other node forms a singleton SCC.
> 2. A, B, C: SCC core. D, E: IN. F, G: OUT. H: tendril (reachable only from D). I: isolated.
> 3. D and E reach the SCC. The SCC reaches F and G. D reaches H (a dead end). D and E cannot reach each other. I can neither reach nor be reached.
> 4. Web meaning:
>    - **IN**: new or poorly-linked pages that link to hubs but receive no links back.
>    - **OUT**: pages the SCC links to but which don't link back (dead-end resources).
>    - **SCC core**: the mutually reachable hub of major sites.
>    - **Tendrils**: isolated sub-webs reachable only from the IN component.

**Exercise 8.D.2: Bow-Tie in Python**

1. Find all SCCs with `nx.strongly_connected_components(W)`.
2. Build the condensation graph with `nx.condensation(W)`.
3. Classify each SCC by its position relative to the giant SCC.
4. What does IN-component membership mean for discoverability?

> [!note]- Solution
> ```python
> import networkx as nx
>
> W = nx.DiGraph()
> W.add_edges_from([("A", "B"), ("B", "C"), ("C", "A"),
>                   ("D", "A"), ("E", "B"),
>                   ("C", "F"), ("B", "G"),
>                   ("D", "H")])
> W.add_node("I")
>
> sccs = list(nx.strongly_connected_components(W))
> C = nx.condensation(W, scc=sccs)
> giant = max(range(len(sccs)), key=lambda i: len(sccs[i]))
>
> reachable_from_giant = nx.descendants(C, giant) | {giant}
> can_reach_giant = nx.ancestors(C, giant) | {giant}
> ```
>
> Nodes in `can_reach_giant` but not in the giant SCC form the IN component. Nodes in `reachable_from_giant` but not in the giant SCC form the OUT component. IN-component pages can reach the SCC but cannot be reached from it. Pages in IN components or tendrils are invisible to crawlers that start from the SCC core: link-following crawls leave large parts of the web unmapped.

## Key Takeaways
- d ≈ log(N)/log(k) gives an order-of-magnitude small-world estimate. Clustering and hubs push real networks away from this baseline.
- A tiny rewiring fraction destroys global distance without destroying local clustering. The sweet spot p ∈ [0.01, 0.1] is the small-world regime.
- σ = (C/C_rand)/(L/L_rand) > 3 is the standard small-world signature: lattice-like clustering with random-like path length.
- Directed web structure has fundamentally different reachability than undirected social graphs. IN pages are invisible to crawlers that start in the SCC.

## Related Vault Pages
- [[watts-strogatz-model]] — the model behind the rewiring sweep in 8.B
- [[small-world-property]] — the property tested by σ in 8.A.2
- [[milgrams-experiment-six-degrees]] — the empirical baseline for 8.A.1
- [[web-bow-tie-structure]] — the structure classified in 8.D
- [[random-graphs]] — the C_rand and L_rand baseline for 8.A.2
