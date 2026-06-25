---
title: "PageRank"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
PageRank extends [[eigenvector-centrality]] with a damping factor — a random surfer follows links with probability α and jumps to a random page with probability 1-α.

## Core Intuition
A random surfer on the web follows links with probability α and teleports to a random page with probability 1-α. PageRank is the long-run visit probability of each page — the stationary distribution of this random walk.

## Formal Definition / Statement
**PageRank equation:**
PR(v) = (1-α)/n + α Σ_{u→v} PR(u)/outdeg(u)

where:
- α is the damping factor (typically 0.85)
- n is the number of nodes
- outdeg(u) is the out-degree of node u

**Interpretation:**
- With probability α: follow a link from the current page
- With probability 1-α: jump to a random page

**Range:** PageRank scores are probabilities: each score is in [0, 1] and all scores sum to 1.

**Power iteration:** repeatedly update all scores until they converge. Each iteration is sparse: O(n + m), often written O(m) on connected graphs.

## Key Properties
1. **Probabilistic interpretation**: scores are visit probabilities
2. **Damping factor**: prevents traps in dead-end nodes or cycles
3. **Scales well**: power iteration is efficient for large graphs
4. **Cheatable**: link farms can manufacture endorsements
5. **Harder to game than pure eigenvector centrality**: the damping factor reduces manipulation

## Worked Example
Small web graph with 4 pages (A, B, C, D):

**Links:** A→B, A→C, B→C, C→A, D→C
**Damping factor:** α = 0.85

**Iteration 1:** initialize all scores to 1/4 = 0.25
**Iteration 2:** update each score based on incoming links
**Convergence:** after ~10 iterations, scores stabilize

**Result:** C has highest PageRank (most incoming links from important pages).

## Common Pitfalls
1. **Confusing with eigenvector centrality**: PageRank adds a damping factor; pure eigenvector centrality does not
2. **Assuming PageRank is hard to game**: link farms can still manipulate scores
3. **Ignoring that PageRank is a probability distribution**: scores sum to 1
4. **Forgetting the damping factor**: without it, the random walk may get trapped

## Connections
- [[eigenvector-centrality]] — PageRank is an extension with damping
- [[centrality-measures]] — one of the main centrality measures
- [[random-walks]] — PageRank is the stationary distribution of a random walk
- [[network-science-l04]] — lecture overview

## Open Questions
- How does PageRank perform on directed or weighted graphs?
- Can we detect and prevent link farm manipulation?
- How does PageRank relate to network robustness?
