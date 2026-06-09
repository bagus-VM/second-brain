---
title: "Real-World Network Examples"
tags: [concept, network-science, semester-1, examples]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [network-intro]
---

## One-line Summary
Networks appear across every domain — social, communication, information, economic, and infrastructure — and the same structural questions apply to all of them.

## Core Intuition
The power of network science lies in its universality. A friendship graph, a web hyperlink structure, an interbank lending system, and a road map are all instances of the same abstraction. Different domains, same math. Studying examples builds intuition for what network structure looks like in practice and what questions it can answer.

## Formal Definition / Statement
Network science identifies several canonical network types by domain:

| Domain | Nodes | Edges | Example |
|---|---|---|---|
| **Social** | People | Friendships, interactions | Zachary's Karate Club |
| **Communication** | People/devices | Email exchanges, calls | Organizational email network |
| **Information** | Documents/pages | Hyperlinks, citations | Political blog network (2004 US election) |
| **Economic** | Institutions/companies | Loans, trade | Interbank loan network |
| **Infrastructure** | Physical locations | Roads, cables | Internet routing topology |

## Key Properties
- **Social networks** reveal communities, influence, and the spread of behaviors. Structure can predict group splits (Karate Club).
- **Communication networks** show actual interaction patterns, which often differ drastically from formal organizational hierarchies.
- **Information networks** reveal clusters and polarization *without reading content* — structure alone exposes political alignment (Adamic & Glance 2005).
- **Economic networks** expose systemic risk: one institution's failure cascades through lending connections.
- **Infrastructure networks** have dense cores and sparse peripheries, reflecting uneven development.

## Worked Example
**Political Blog Network (2004 US Election):** Nodes are political blogs, edges are hyperlinks between them. When visualized, two dense clusters emerge — liberal and conservative. The network structure reveals political alignment without analyzing a single word of content. This demonstrates that structure alone carries semantic information.

## Common Pitfalls
- **Domain ≠ type.** "Social network" and "information network" are not formal graph types (like directed/undirected). They describe the domain, not the mathematical structure.
- **Assuming all networks in a domain look alike.** An email network and a friendship network are both "social" but have very different structural properties.
- **Over-generalizing from one example.** Zachary's Karate Club has 34 nodes — conclusions may not scale.

## Connections
- [[network-intro]] — the basic definition of a network
- [[edge-types]] — the mathematical representation of edges across these examples
- [[community-structure]] — communities appear in social, information, and economic networks
- [[network-diffusion]] — how things spread through these different network types
- [[network-effects]] — why the structure of these networks matters

## Open Questions
- Are there universal structural patterns that appear across all network domains? 
	- yes, and this happens because of the abstraction
- How do we compare networks from different domains quantitatively? by applying the same math that we get from the abstraction and apply it across different domains 
	- By extracting structural properties (density, clustering, diameter, centrality measures) that are domain-agnostic — the same metrics work on any graph regardless of whether nodes are people, pages, or banks.
- What makes some networks more amenable to analysis than others? the complexity of its dynamic, structure, position, and evolution
	- A network is amenable to analysis when its structural patterns (communities, hubs, bridges) are interpretable relative to the domain, and you can validate findings against ground truth (like Zachary's club split).
