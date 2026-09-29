---
title: "Random Walks"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
A random walk on a graph is a stochastic process where a walker moves from node to node following edges with probabilities proportional to edge weights — the foundation of [[pagerank]] and many centrality measures.

## Core Intuition
Imagine a walker on a graph. At each step, it chooses a random neighbour and moves there. The long-run visit probability of each node reveals its structural importance — nodes that are visited more often are more central.

## Formal Definition / Statement
**Random walk:**
- Start at a random node
- At each step, choose a neighbour uniformly at random (or proportional to edge weight)
- Move to the chosen neighbour
- Repeat indefinitely

**Transition matrix:**
P_ij = A_ij / deg(i)

where A_ij is the adjacency matrix entry and deg(i) is the degree of node i.

**Stationary distribution:**
π_i = deg(i) / 2m

where m is the total number of edges. In the long run, the walker visits node i with probability proportional to its degree.

**PageRank extension:**
PR(v) = (1-α)/n + α Σ_{u→v} PR(u)/outdeg(u)

- With probability α: follow a link
- With probability 1-α: jump to a random page

## Key Properties / Complexity
1. **Stationary distribution**: long-run visit probability is proportional to degree
2. **Foundation of PageRank**: PageRank is the stationary distribution of a modified random walk
3. **Connects to centrality**: nodes visited more often are more central
4. **Mixing time**: how long until the walk converges to the stationary distribution
5. **Applications**: PageRank, network embeddings, community detection

## Worked Example
Graph with 3 nodes: A (degree 2), B (degree 2), C (degree 2), m = 3 edges:

**Transition matrix:**
P(A→B) = 1/2, P(A→C) = 1/2
P(B→A) = 1/2, P(B→C) = 1/2
P(C→A) = 1/2, P(C→B) = 1/2

**Stationary distribution:**
π_A = 2/6 = 1/3, π_B = 2/6 = 1/3, π_C = 2/6 = 1/3

**Interpretation:** in the long run, the walker visits each node equally often (because all have the same degree).

## Common Pitfalls
1. **Confusing random walk with diffusion**: random walk is a stochastic process; diffusion is a deterministic process
2. **Ignoring that the stationary distribution depends on degree**: high-degree nodes are visited more often
3. **Assuming the walk converges immediately**: mixing time can be long for some graphs
4. **Forgetting that PageRank modifies the random walk**: the damping factor changes the stationary distribution

## Connections
- [[pagerank]] — PageRank is the stationary distribution of a modified random walk
- [[centrality-measures]] — random walks connect to centrality
- [[eigenvector-centrality]] — the stationary distribution is related to the leading eigenvector
- [[network-science-l04]] — lecture overview

## Open Questions
- How does the random walk perform on directed or weighted graphs?
- Can we use random walks for community detection?
- How does the mixing time relate to network structure?
