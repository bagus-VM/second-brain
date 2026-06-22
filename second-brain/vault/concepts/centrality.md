---
title: "Centrality"
tags: [concept, network-science, semester-1, position]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [network-intro, edge-types]
---

## One-line Summary
Centrality measures answer "who is the most important node in a network?" — but "important" has multiple meanings, each captured by a different centrality measure.

## Core Intuition
Not all nodes in a network are equal. Some sit at the crossroads of many paths, some have the most connections, some are closest to everyone else. Each of these intuitions about "importance" corresponds to a different centrality measure. The key insight is that *position in the network structure* determines influence, visibility, and power — independent of any intrinsic properties of the node.

A blogger with few personal posts but many incoming links from diverse communities can be more "important" than one with great content but no connections. A bank with moderate assets but many lending relationships can be the critical point of systemic failure.

## Formal Definition / Statement
Centrality measures assign a score $c(v)$ to each node $v$ capturing some notion of structural importance:

- **==Degree centrality==:** $c(v) = \deg(v)$ — ==number of connections==. Simple, local measure.
- ==**Closeness centrality==:** $c(v) = \frac{1}{\sum_{u} d(v, u)}$ — inverse of average distance to all other nodes. ==Measures how quickly a node can reach the whole network.==
- ==**Betweenness centrality==:** $c(v) = \sum_{s \neq v \neq t} \frac{\sigma_{st}(v)}{\sigma_{st}}$ — fraction of shortest paths passing through $v$. Measures bridge/brokerage role.

For directed networks, degree splits into **in-degree** (edges arriving) and **out-degree** (edges leaving), each with different meanings (popularity vs. activity).

Different measures capture different intuitions — there is no single "correct" centrality. The choice depends on what aspect of importance matters for the question.

## Key Properties
- **Degree centrality** is the simplest and most local — it only looks at immediate neighbors.
- **Closeness centrality** captures global reach — nodes with high closeness can quickly disseminate or gather information.
- **Betweenness centrality** identifies brokers and bridges — nodes that connect otherwise separate communities.
- Centrality rankings can differ dramatically depending on which measure is used.
- In directed networks, high in-degree ≠ high out-degree (a famous person may receive many links but link to few).
- Centrality connects to [[network-diffusion]]: high-centrality nodes are often the most effective spreaders.

## Worked Example
Consider a network where:
- Node A has 20 connections (highest degree) — most "popular"
- Node B has the shortest average distance to all others (highest closeness) — most "reachable"
- Node C sits on the most shortest paths (highest betweenness) — most "central" as a bridge

==These three nodes could all be different! A political blogger who bridges liberal and conservative communities (high betweenness) might have fewer total links (lower degree) than a blogger deeply embedded in one community.==

## Common Pitfalls
- **Assuming there's one "right" centrality.** Different measures answer different questions. The choice depends on the application.
- **Confusing degree with importance.** A node with many connections to the same community is different from one with fewer connections to different communities.
- **Ignoring directedness.** In a directed network, being followed by many (high in-degree) is fundamentally different from following many (high out-degree).
- **Treating centrality as static.** In dynamic networks, central nodes change over time.

## Connections
- [[network-intro]] — centrality is one of the key questions network science asks
- [[edge-types]] — directed edges create in-degree vs. out-degree; weights affect centrality calculations
- [[community-structure]] — high-betweenness nodes often bridge communities
- [[network-diffusion]] — central nodes are critical for spreading dynamics
- [[network-effects]] — centrality connects to visibility, influence, and platform power

## Open Questions
- How do we choose the right centrality measure for a given problem?
- How does centrality change in dynamic (evolving) networks?
- Can we combine multiple centrality measures into a unified ranking?
- How robust are centrality measures to noisy or incomplete network data?
