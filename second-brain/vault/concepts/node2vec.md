---
title: "Node2Vec"
tags: [concept, network-science, semester-1, random-walks, graph-embeddings]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: ["[[deepwalk]]", "[[random-walks]]"]
---

## One-line Summary
Node2Vec extends DeepWalk with biased second-order random walks controlled by return parameter p and in-out parameter q, letting you tune embeddings for community similarity (homophily) or structural role similarity (Grover & Leskovec 2016).

## Core Intuition
Two notions of similarity exist in graphs:
- Homophily (community): nodes in the same densely connected region are similar, even if structurally different (hub vs. leaf). DFS-like walks capture this.
- Structural equivalence (role): nodes playing the same role are similar, even in different communities (both are hubs, both are bridges). BFS-like walks capture this.

DeepWalk's uniform walks give a blur of both. Node2Vec lets you choose via two knobs.

## Formal Definition / Statement
Given previous node t and current node v, the walk transitions to neighbour x with unnormalized probability:

α(t, x) = 1/p  if d(t, x) = 0  (return to t)
α(t, x) = 1    if d(t, x) = 1  (stay at distance 1)
α(t, x) = 1/q  if d(t, x) = 2  (move outward)

P(x | v, t) ∝ α(t, x) · w_{vx}

where d(t, x) is shortest-path distance from t to x.

- Small p → DFS-like: wander far, reveal communities (homophily)
- Small q → BFS-like: stay local, sample neighbourhoods (structural equivalence)

After generating biased walks, apply the same skip-gram objective as DeepWalk.

## Key Properties
1. Second-order transition: walk decisions depend on where we came from (not just current node)
2. Two interpretable knobs: p controls return, q controls exploration depth
3. Still transductive and feature-free (same limitations as DeepWalk)
4. Scalable: runs on billions of edges with sampled walks + SGD
5. No features required: works on raw adjacency — sensible baseline for any graph task
6. p = q = 1 recovers DeepWalk

## Worked Example
At node v, arrived from t. Three classes of neighbours:
- d(t, x) = 0: back to t — probability ∝ 1/p
- d(t, x) = 1: neighbours of v also adjacent to t — probability ∝ 1
- d(t, x) = 2: neighbours of v not adjacent to t — probability ∝ 1/q

Small p → walk frequently returns (explores local community deeply).
Small q → walk jumps to distant neighbours (samples structural roles).

## Common Pitfalls
- Confusing p and q: small p = DFS (community), small q = BFS (structural role) — or think of it as "small p keeps you returning, small q pushes you outward"
- Like DeepWalk, still transductive: new node = new walks + retraining
- Ignores node attributes entirely
- In practice, the difference from DeepWalk is often modest on well-connected graphs

## Connections
- [[deepwalk]] — node2vec generalises DeepWalk with biased walks
- [[node-embeddings]] — second wave of embedding methods
- [[random-walks]] — the walk generation mechanism
- [[adjacency-matrix-factorization]] — implicit factorisation perspective applies
- [[link-prediction-via-embeddings]] — node2vec is a strong baseline for link prediction
- [[embedding-based-community-detection]] — node2vec embeddings can be clustered to detect communities
- [[graph-neural-networks]] — GNNs address node2vec's transductive and feature-free limitations

## Open Questions
- Can we learn p and q from data instead of tuning them?
- How do biased walks relate to graph diffusion operators?
- What is the theoretical effect of p, q on the implicit co-occurrence matrix?
