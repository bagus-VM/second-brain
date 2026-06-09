---
title: "Network Science E04 — Centrality and Roles Flashcards"
tags:
  - flashcards
  - network-science
  - semester-1
course: "Network Science"
status: current
last_updated: 2026-06-02
---

# Flashcards — Exercise Sheet 4

## Flashcards

> [!question]- What is the difference between degree centrality and betweenness centrality?
> [!answer]- Degree centrality measures how many direct connections a node has (local importance): C_d(v) = deg(v)/(|V|−1). Betweenness centrality measures how many shortest paths pass through a node (global routing importance). A node can have high degree but low betweenness (embedded in a dense cluster) or moderate degree but high betweenness (bridge node).

> [!question]- What structural role does a node with high betweenness but moderate degree play?
> [!answer]- It is a broker or bridge node. It sits on the unique paths connecting different clusters. Removing it would disconnect those groups. High betweenness with moderate degree is the signature of a structural bridge — it controls information flow between communities without being a local hub.

> [!question]- What is the difference between an embedded node and a broker?
> [!answer]- An embedded node sits inside a dense cluster where all neighbours are mutually connected (high clustering coefficient). It has no brokerage opportunity. A broker sits between groups, controlling the flow of information across structural holes. Embedded nodes have trust/redundancy; brokers have information advantage.

> [!question]- Can a node have high clustering coefficient AND high betweenness centrality?
> [!answer]- Yes. Node 7 in the two-triangle example has C_7 = 1 (its two neighbours are connected) yet high betweenness because it provides an alternative path between two large clusters. Clustering measures local density; betweenness measures global routing — they capture different structural dimensions.

> [!question]- What does it mean when centrality measures disagree for the same node?
> [!answer]- It reveals nuanced structural positions. A node with high eigenvector but low betweenness is embedded in a dense core with redundant paths. A node with high betweenness but low eigenvector is a bridge connecting separate groups but without strong local connections. Different measures capture different aspects of "importance."
