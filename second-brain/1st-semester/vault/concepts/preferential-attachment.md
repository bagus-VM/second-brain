---
title: "Preferential Attachment (Barabási-Albert Model)"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
The Barabási-Albert model generates [[scale-free-networks|scale-free networks]] through preferential attachment: new nodes connect to existing nodes with probability proportional to their degree ("the rich get richer").

## Core Intuition
Why do some networks have hubs? The [[random-graphs|Erdős-Rényi model]] treats all nodes equally, producing a Poisson degree distribution with no hubs. Real networks grow over time, and new nodes prefer to connect to well-known (high-degree) nodes. This "rich-get-richer" mechanism naturally produces a power-law degree distribution $P(k) \sim k^{-3}$.

The model has two ingredients:
1. **Growth**: the network starts small and nodes are added one at a time
2. **Preferential attachment**: each new node connects to $m$ existing nodes with probability $\propto k_i$ (where $k_i$ is the degree of node $i$)

## Formal Definition / Statement
**Barabási-Albert model (1999):**
1. Start with a small initial network of $m_0$ nodes
2. At each time step, add a new node with $m$ edges ($m \leq m_0$)
3. The new node connects to existing node $i$ with probability:
$$\Pi(k_i) = \frac{k_i}{\sum_j k_j}$$

**Resulting properties:**
- Degree distribution: $P(k) = \frac{2m(m+1)}{k(k+1)(k+2)} \sim 2m^2 k^{-3}$ (power law with $\gamma = 3$)
- Average path length: $\bar{d} \sim \frac{\log n}{\log \log n}$ (even shorter than random graphs!)
- Clustering coefficient: $C \sim \frac{(\log n)^2}{n}$ (decreases with $n$, but higher than random graphs)

## Key Properties / Complexity
- **Power-law degree**: $P(k) \sim k^{-3}$, the hallmark of [[scale-free-networks|scale-free networks]]
- **Ultra-small distances**: $\bar{d} \sim \log n / \log \log n$ — shorter than the $\log n / \log k$ of random graphs, because hubs provide direct shortcuts
- **No community structure**: the model doesn't produce the high clustering seen in real networks
- **Deterministic exponent**: $\gamma = 3$ is fixed by the model; real networks have $\gamma \in [2, 3]$, requiring model extensions
- **Mathematically tractable**: the degree distribution can be derived using rate equations or continuous approximation

## Worked Example
Start with $m_0 = 3$ fully connected nodes. Each new node brings $m = 2$ edges.

- Node 4 arrives: connects to 2 of the 3 existing nodes, preferentially to those with higher degree
- Node 5 arrives: connects to 2 nodes, now including node 4 (which has degree 2+2=4 if it got both connections)
- After many steps: a few nodes accumulate many connections (hubs), most have degree $\approx m = 2$

The degree of the earliest nodes grows as $k_i(t) \approx m \sqrt{t/t_i}$ where $t_i$ is the birth time of node $i$. Earlier nodes become hubs.

## Common Pitfalls
- **"Preferential attachment is the only way to get power laws"** — Other mechanisms (duplication models, fitness models, optimization) can also produce power-law degree
- **"The BA model explains all scale-free networks"** — It produces $\gamma = 3$ exactly; many real networks have $\gamma \neq 3$. Extensions (e.g., varying $m$, adding fitness) are needed.
- **"Preferential attachment = popularity"** — It's a mathematical mechanism, not necessarily conscious choice. It can arise from random processes that happen to be degree-biased.
- **"The BA model produces high clustering"** — It does NOT. $C$ decreases with $n$. The [[watts-strogatz-model]] produces high clustering but NOT scale-free degree.

## Connections
- [[scale-free-networks]] — The BA model is the canonical generator of scale-free networks
- [[power-law-distribution]] — The mathematical framework for the resulting degree distribution
- [[random-graphs]] — Contrasted: homogeneous degree vs. heavy-tailed degree
- [[watts-strogatz-model]] — A different model family: high clustering but narrow degree distribution
- [[configuration-model]] — Random graph with prescribed degree sequence (can also produce power-law degree, but without growth mechanism)
- [[online-link-formation]] — Real-world manifestation of preferential attachment in web links

## Open Questions
- What drives preferential attachment in specific domains (citation, web, social)?
- How does the model change when nodes have intrinsic "fitness" that modifies attachment probability?
- Can we distinguish power-law degree from other heavy-tailed distributions empirically?
