---
title: "Power Law Distribution"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
A power-law distribution is a heavy-tailed distribution where a few nodes have very high degree (hubs) and most nodes have low degree — the signature of scale-free networks.

## Core Intuition
In many real-world networks, the degree distribution follows a power law: P(k) ~ k^(-γ). This means a few nodes (hubs) have very high degree, while most nodes have low degree. This creates a "hub-dominated" structure with important implications for robustness, diffusion, and community detection.

## Formal Definition / Statement
**Power-law distribution:**
P(k) ~ k^(-γ)

where:
- k is the degree
- γ is the power-law exponent (typically 2 < γ < 3 for real networks)
- ~ means "proportional to"

**Properties:**
- Heavy tail: P(k) decays slowly, so high-degree nodes are relatively common
- Scale-free: the distribution looks the same at any scale
- No characteristic degree: there is no "typical" degree

**Degree distribution:**
- Homogeneous: most nodes have similar degree (e.g., Erdős–Rényi random graphs)
- Power-law: few hubs, many low-degree nodes (e.g., Barabási–Albert model)

## Key Properties / Complexity
1. **Heavy tail**: high-degree nodes are relatively common
2. **Scale-free**: the distribution looks the same at any scale
3. **No characteristic degree**: there is no "typical" degree
4. **Hub-dominated**: a few nodes have very high degree
5. **Implications for robustness**: power-law networks are robust to random failures but vulnerable to targeted attacks

## Worked Example
Network with power-law degree distribution (γ = 2.5):

**Degree distribution:**
- 1000 nodes with degree 1
- 100 nodes with degree 10
- 10 nodes with degree 100
- 1 node with degree 1000

**Interpretation:** most nodes are peripheral (degree 1), but a few hubs (degree 100-1000) connect the network.

## Common Pitfalls
1. **Confusing power-law with exponential**: exponential decays faster; power-law has a heavier tail
2. **Assuming all heavy-tailed distributions are power laws**: log-normal, stretched exponential, etc. also have heavy tails
3. **Ignoring that power-law fitting is tricky**: many apparent power laws are not true power laws
4. **Over-interpreting the exponent**: small changes in γ can change the distribution's properties dramatically

## Connections
- [[degree-centrality]] — degree distribution reveals network structure
- [[centrality-measures]] — hubs have high degree centrality
- [[network-science-l04]] — lecture overview

## Open Questions
- How do power-law distributions arise in real networks?
- Can we distinguish true power laws from other heavy-tailed distributions?
- How does the power-law exponent affect network properties?
