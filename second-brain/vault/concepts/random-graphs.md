---
title: "Random Graphs (Erdős-Rényi)"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
An Erdős-Rényi random graph $G(n, p)$ connects each pair of $n$ nodes independently with probability $p$; it serves as the null model for network analysis and has well-understood threshold phenomena.

## Core Intuition
The simplest possible network model: flip a coin for every pair of nodes, connect them if heads. Despite this simplicity, $G(n, p)$ exhibits rich structural phenomena:
- A giant component emerges abruptly when average degree crosses 1
- Average path length scales as $\log n / \log k$ (the [[small-world-property]])
- [[clustering-coefficient|Clustering]] is low: $C \approx p = k/n$

This makes random graphs the natural comparison point: they have short paths but lack the high clustering of real social networks. The [[watts-strogatz-model]] bridges this gap.

## Formal Definition / Statement
**Erdős-Rényi model $G(n, p)$:**
- $n$ nodes
- Each pair $(u, v)$ connected independently with probability $p$
- Expected number of edges: $\binom{n}{2} p$
- Average degree: $k = p(n-1) \approx pn$

**Key properties:**
- Average shortest-path distance: $\bar{d} \approx \frac{\log n}{\log k}$
- Clustering coefficient: $C = p = \frac{k}{n-1} \approx \frac{k}{n}$ (very low for large $n$)
- Degree distribution: Binomial (approximately Poisson for large $n$, small $p$)
- Giant component threshold: $k = 1$ (i.e., $p = 1/n$)

## Key Properties
- **Threshold phenomena**: sharp transitions at critical values of $p$ (giant component, connectivity)
- **Small-world**: $\bar{d} \sim \log n / \log k$ — but NOT clustered
- **Homogeneous degree**: all nodes have approximately the same degree $\approx k$
- **No community structure**: edges are uniformly random, no clustering or modularity
- **Analytically tractable**: most properties have closed-form expressions or well-understood asymptotics

## Worked Example
For $n = 1000$, $p = 0.01$ ($k \approx 10$):
- Expected edges: $\binom{1000}{2} \times 0.01 \approx 4995$
- Average path length: $\bar{d} \approx \frac{\log 1000}{\log 10} = 3$
- Clustering: $C = 0.01$ (very low — most neighbor pairs are NOT connected)
- Giant component: YES ($k = 10 \gg 1$)

Compare to a real social network with $k = 10$: $C \approx 0.1\text{–}0.5$ (much higher), $\bar{d} \approx 3\text{–}5$ (similar).

## Common Pitfalls
- **"Random graphs model real networks well"** — They capture short paths but miss clustering, community structure, and degree heterogeneity
- **"Random graphs are connected"** — Only when $p > \ln n / n$ (above the connectivity threshold)
- **"All random graphs have the same properties"** — Properties depend critically on $p$; below the giant component threshold, the graph is mostly isolated nodes

## Connections
- [[sparse-dense-and-random-graphs]] — Density classification of graphs
- [[small-world-property]] — Random graphs have $\bar{d} \approx \log n / \log k$
- [[watts-strogatz-model]] — The $p = 1$ endpoint of the W-S model is a random graph
- [[clustering-coefficient]] — Random graphs have low $C \approx k/n$
- [[connectivity-and-components]] — Giant component emerges at $k = 1$
- [[power-law-distribution]] — Random graphs have Poisson degree, NOT power-law
- [[scale-free-networks]] — Contrasted with random graphs: heavy-tailed vs. Poisson degree
- [[configuration-model]] — Random graph with arbitrary prescribed degree sequence

## Open Questions
- How do random graph results change when edges are not independent (e.g., triadic closure)?
- What is the "right" null model for networks with community structure?
- How do directed random graphs differ in their threshold behavior?
