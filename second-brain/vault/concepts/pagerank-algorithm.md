---
title: "PageRank Algorithm"
tags: [concept, network-science, semester-1, network-science]
course: "Network Science"
source_count: 0
status: current
last_updated: 2026-06-09
prerequisites: ["[[centrality-measures]]"]
---

## One-line Summary
PageRank assigns importance scores to web pages by modelling a random surfer who follows links with probability α and jumps to a random page with probability 1−α, converging to a stationary distribution.

## Core Intuition
Google's founders asked: "Which web pages are important?" Not just "which have the most links" (that's degree centrality) but "which are linked to by other important pages?" This is recursive prestige — the same idea as eigenvector centrality but adapted for directed graphs with a twist: the random surfer sometimes gets bored and jumps to a random page. This damping factor prevents importance from being trapped in dead-end subgraphs.

## Formal Definition / Statement

### The Iterative Formula
$$PR(v) = \frac{1 - \alpha}{n} + \alpha \sum_{u \to v} \frac{PR(u)}{\text{outdeg}(u)}$$

Where:
- PR(v) = PageRank of node v
- α = damping factor (typically 0.85)
- n = total number of nodes
- The sum runs over all nodes u that have a link pointing to v

### Matrix Form
$$\mathbf{PR} = \frac{1-\alpha}{n} \mathbf{1} + \alpha \mathbf{M} \cdot \mathbf{PR}$$

where M is the column-stochastic transition matrix of the web graph.

### Interpretation
- With probability α: follow a random outgoing link from the current page
- With probability (1−α): teleport to a uniformly random page
- The damping factor α = 0.85 means "on average, the surfer follows 1−α ≈ 5.88 links before jumping"

## Key Properties / Complexity

### Convergence
- PageRank is computed by power iteration: start with uniform scores, repeatedly apply the formula
- Guaranteed to converge for any α ∈ (0, 1) because the modified transition matrix is irreducible and aperiodic
- Typical convergence: 50–100 iterations for web-scale graphs

### Damping Factor
- α = 0.85 is the standard choice (original Brin & Page paper)
- α → 1: pure link following, may not converge on disconnected graphs
- α → 0: pure random jumping, all pages get equal rank (1/n)
- Lower α values converge faster but lose network structure information

### Complexity
- Each iteration: O(m) where m = number of edges
- Total: O(k · m) for k iterations until convergence
- Space: O(n) for the score vector

### Properties
- Scores sum to 1 (they form a probability distribution)
- Directed graphs only — a link from A to B means A "endorses" B
- **Cheatable:** Link farms can manufacture endorsements (this is why Google uses hundreds of other signals)

## Worked Example
**Small web graph:** Pages A, B, C with links A→B, B→C, C→A, A→C.

Iteration 0 (uniform): PR = [0.25, 0.25, 0.25] (C omitted for brevity — assume D exists)

More concretely, 3 pages with out-degrees: A has outdeg 2 (→B, →C), B has outdeg 1 (→C), C has outdeg 1 (→A).

With α = 0.85, n = 3:
- PR(A) = 0.15/3 + 0.85 × (PR(C)/1) = 0.05 + 0.85·PR(C)
- PR(B) = 0.15/3 + 0.85 × (PR(A)/2) = 0.05 + 0.425·PR(A)
- PR(C) = 0.15/3 + 0.85 × (PR(B)/1 + PR(A)/2) = 0.05 + 0.85·PR(B) + 0.425·PR(A)

Iterating from uniform [0.333, 0.333, 0.333]:
- Iteration 1: PR(A)≈0.333, PR(B)≈0.192, PR(C)≈0.475
- Iteration 2: PR(A)≈0.454, PR(B)≈0.243, PR(C)≈0.303
- ... converges to stationary distribution

## Common Pitfalls
- Confusing PageRank with degree centrality — a node with many in-links from unimportant pages ranks lower than one with few in-links from important pages
- Forgetting the damping factor — without it, disconnected components get zero rank
- Assuming PageRank is uncheatable — link farms exploit the algorithm; modern search uses hundreds of signals
- Applying PageRank to undirected graphs — the direction matters (A→B means A endorses B, not the reverse)
- Ignoring dangling nodes (nodes with no outgoing links) — they absorb all probability; must be handled by redistributing their score

## Connections
- [[centrality-measures]] — PageRank is a variant of eigenvector centrality for directed graphs
- [[eigenvector-centrality]] — PageRank adds damping to eigenvector centrality's recursive prestige
- [[betweenness-centrality]] — Alternative centrality measure capturing path brokerage
- [[network-science-l04]] — PageRank is introduced alongside other centrality measures in L04
- [[small-world-networks]] — Web graph exhibits small-world properties that affect PageRank convergence
- [[girvan-newman-algorithm]] — Community detection uses different centrality (edge betweenness)

## Open Questions
- How does PageRank perform on dynamic graphs where links change over time?
- Can personalised PageRank (biased teleport to specific pages) replace the uniform version?
- How do modern search engines combine PageRank with other signals?
