---
title: "Six Degrees of Separation"
tags: [concept, network-science, semester-1, network-science]
course: "Network Science"
source_count: 0
status: current
last_updated: 2026-06-09
prerequisites: ["[[small-world-property]]"]
---

## One-line Summary
Stanley Milgram's 1967 experiment showed that any two strangers in the United States are connected by approximately six intermediate acquaintances — revealing the surprisingly short path lengths in social networks.

## Core Intuition
You might think that in a country of hundreds of millions of people, the chain of acquaintances connecting you to a random stranger would be very long. But it's not — it's about six. This happens because social networks have "shortcuts": a few random long-range connections that dramatically reduce path lengths. Your friend from summer camp who lives across the country, your college roommate's cousin in another industry — these bridges shrink the entire network.

## Formal Definition / Statement

### Milgram's Experiment (1967)
- **Setup:** Randomly selected people in Omaha, Nebraska were asked to forward a letter to a target person in Boston, Massachusetts
- **Rule:** Each participant could only forward the letter to someone they knew on a first-name basis
- **Result:** The median number of intermediaries was ~5.5 (commonly rounded to "six degrees")
- **Implication:** The average geodesic distance in the U.S. social network is approximately 6

### Mathematical Framework
For a random graph G(n, p) with n nodes and edge probability p:
- Expected average path length: L ≈ ln(n) / ln(np) = ln(n) / ln(⟨k⟩)
- For n = 300 million and average degree ⟨k⟩ ≈ 1000: L ≈ ln(3×10⁸) / ln(1000) ≈ 19.5 / 6.9 ≈ 2.8

Real social networks have clustering and structure, so the actual distance is higher than the random graph prediction — but still logarithmic in n.

### Small-World Property
A network exhibits the small-world property if:
- The average shortest path length L grows logarithmically with the number of nodes: L ∝ ln(n)
- This holds for random graphs, Watts-Strogatz small-world networks, and many real networks

## Key Properties / Complexity

### Empirical Evidence
| Network | Nodes | Avg. Distance | Study |
|---------|-------|---------------|-------|
| U.S. social | ~300M | ~6 | Milgram 1967 |
| Microsoft Messenger | 240M | 6.6 | Leskovec & Horvitz 2008 |
| Facebook | 1.5B | 4.74 | Backstrom et al. 2012 |
| Twitter | 41.7M | 4.67 | Kwak et al. 2010 |
| Erdős collaboration | ~500K | 4.7 | Batagelj & Mrvar |

### Why Six?
- Social networks have high clustering (friends of friends are often friends)
- But they also have a few random long-range ties (Watts-Strogatz model)
- These "weak ties" (Granovetter) create shortcuts that reduce global path length
- The result: L ∝ ln(n) even with clustering

### Network Navigation
Milgram's experiment wasn't just about shortest paths — it was about *navigation*. Participants had to find the target using only local knowledge (their own acquaintances). Kleinberg (2000) showed that navigability requires a specific distribution of shortcut lengths — not too many long-range ties, not too few.

## Worked Example
**Milgram's original chain (simplified):**
1. Sender (Omaha) → friend who is a merchant
2. Merchant → client in Boston
3. Client → target person's neighbourhood
4. Neighbour → target person
**Modern equivalent (LinkedIn):**
1. You → your former colleague
2. Former colleague → their university classmate
3. Classmate → someone at the target company
4. That person → the hiring manager

Each "hop" is one degree. The path length is 4, well within the six-degree prediction.

## Common Pitfalls
- Confusing "six degrees" with "six hops" — the original experiment measured intermediaries (5.5), so total hops ≈ 6
- Assuming all networks are small-world — some networks (e.g., lattices) have L ∝ n^(1/d), which grows much faster
- Ignoring that Milgram's experiment had massive attrition — only ~30% of chains reached the target
- Equating shortest path distance with navigable distance — finding the short path requires the right information
- Assuming the number "six" is universal — it varies by network size, structure, and density

## Connections
- [[small-world-property]] — The Watts-Strogatz model explains why real networks have short paths
- [[centrality-measures]] — Nodes with high betweenness often serve as shortcuts
- [[homophily]] — People cluster with similar others, creating high clustering coefficient
- [[kleinberg-decentralized-search]] — Lecture material on network navigation
- [[pagerank-algorithm]] — PageRank relies on the web graph being navigable
- [[girvan-newman-algorithm]] — Community detection exploits the gap between clustered and shortcut edges

## Open Questions
- How has social media changed the effective degrees of separation since 1967?
- Does the six-degree property hold for negative relationships (enemies, not just friends)?
- How does navigability degrade when nodes have limited information about the network?
