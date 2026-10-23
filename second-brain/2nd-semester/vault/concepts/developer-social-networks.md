---
title: "Developer Social Networks"
tags: [concept, mining-software-repositories, semester-2, social-networks, network-analysis]
course: "Mining Software Repositories"
source_count: 1
status: current
last_updated: 2026-10-22
prerequisites: ["[[mining-software-repositories]]"]
---

## One-line Summary

A developer social network is a graph whose nodes and edges you choose, and every research claim
about how developers work depends on those two choices before it depends on any metric.

## Core Intuition

The lecture defines the object from Merriam-Webster: "a network of individuals (such as friends,
acquaintances, and coworkers) connected by interpersonal relationships", plus the second sense of
the word, "an online service or site through which people create and maintain interpersonal
relationships". "Research is mostly interested in the first part of the definition." The questions
that follow are the course's own: "Who works together?", "Which teams are there?", "What is the
role of a developer?"

The second intuition is that a network is never *given* — it is constructed: the lecture says there
is "not just one way to model a social network in software development, but many of them." Three
families are named: the **social** network (relationships between people), the **technical**
network (relationships between artifacts, which "does not (necessarily) mean dependencies, but
also other aspects like co-change"), and the **socio-technical** network (both together). The
lecture also flags the terminological slippage: "technical networks are also often refered to as
socio-technical because often some human interaction is used to derive the relationships".

The third intuition is the modelling discipline it imposes. Any network definition rests on "two
key aspects: 1) What are the nodes? 2) What are the edges?" — "relationships between which
actors/artifacts are we interested in?" and "how do we define that there is a relationship between
them?". This parallels the measurement distinction from the enrichment chapter: "Sometimes, we can
model the actors/artifacts/relationships directly, sometimes we have to do this indirectly" — "we
often cannot know who talked to whom exactly … But we can indirectly model this based on
observable data".

## Formal Definition / Statement

**Graphs.** "Formally, social networks are defined as graphs", where a graph is "a tuple where V
defines the vertices/nodes of a graph and E ⊆ V × V the edges". Direction is a modelling choice: in
a directed graph "we can describe an edge as an ordered tuple, i.e., e = (u, v)", in an undirected
graph "as a set, i.e., e = {u, v}". The lecture standardises on the directed notation, treating
any undirected graph as one with the two reverse edges added.

**Paths, degree, connectivity.** A path of length m is "a sequence of nodes (v₁, …, v_m) such that
(v_i, v_{i+1}) ∈ E"; the length "d(u, v) between two nodes u, v ∈ V is defined as the number of
edges on that path", and "Two nodes are connected, if a path between them exists". Undirected degree
is "deg v = #{e ∈ E: v ∈ e}"; the directed case has "an out-degree" and "an in-degree". "A graph is
called connected if there exists a path for all pairs of node u, v ∈ V", otherwise "disconnected";
a connected component is "maximal connected subgraph".

**Communities and partitions.** "Communities are clusters of nodes which have many connections
between them". They need not be fully connected and may have edges to other communities, but not
too many, "because then the communities would be merge into one large community". There is no
threshold: "There is no fixed definition of community in terms of how many internal connections are
required and how many external connections are allowed". Formally, a community detection algorithm
"determines subgraphs P = {p₁, …, p_k} of a graph G = (V, E)" where each p_i = (V_i, E_i) with
V_i ⊆ V and E_i the induced edges, the V_i disjoint, and their union equal to V.

**Node and edge types.** A node type sourced from outside the network is "defined by a function over
the nodes": "type_V: V → types where types is a pre-defined set of types" — "such externally
defined types can, e.g., be roles in a project or organization". A type sourced from the node's
position is "defined by a function over the graph": "type_V_social: V × E → types" — "typically
related to how 'important' a node is in a network, e.g., high degree". Edges may also be of
different kinds, "used to preserve complex information", e.g. whether communication happened "via
email, issues, pull requests, code, …". Either "there can only be a single edge between two nodes
and each edge can only have a single type", or "Edges between nodes can have multiple types and/or
we can have multiple edges between nodes". Both are "modeled by a function over the edges",
"type_E: E → types", and "In case edges can have multiple types, this function is not injective".
The recommendation: "When we have multiple types, it is sometimes easier to model this within
different graphs without types" — variant 1 is one graph with multiple edge types, variant 2 is
two graphs without types.

**Centrality.** Degree centrality is the node degree itself: "C_degree(v) = d(v)"; "For a directed
graph, we have two such centrality measures, i.e., one for the in-degree and one for the
out-degree". Graph-level degree centrality normalises to [0,1] by dividing by "the largest possible
value that the nominator could achieve … This is achieved by a star graph". Closeness centrality
formalises the idea "that a location is central, if the length of the paths to other nodes is
short". Betweenness centrality "means that a node is on many shortest paths between nodes", with
σ_st(v) counting the shortest paths between s and t "such that v is in the path". The clustering
coefficient asks "how closely connected neighborhoods are"; with N_v the nodes adjacent to v, it
is "measured in relation to complete subgraphs" (a clique).

## Key Properties

- **The network is a modelling decision and part of the study design.** What the nodes are and what
  an edge is are decided before data is collected, and different answers answer different questions.
- **Edges are usually indirect proxies.** Communication is "interpreted broadly": "We have the
  obvious direct communication, e.g., via emails on a mailing list or through discussions within
  issues" and "indirect communication via software artifacts".
- **Direction encodes something.** "The directed network allows to identify whether communication
  was uni-directional or bi-directional" and the edge direction "represent knowledge and
  information flow"; the directed issue-tracker example is directed "to indicate order of comments.
  Outgoing edge means commented before." The undirected variant ignores the order of comments.
- **Artifacts as nodes are usually files.** "Dependency graphs can be viewed as a technical
  network", but MSR "also often looks beyond that to process aspects" — "Two files might not
  technically depend on each other, but are often changed together", for example "two classes that
  implement the same interface might be changed together if the assumption on the behavior of
  interface change". The **co-change graph** has "edges denote files where change together in a
  commit" — a relationship the compiler never sees.
- **The socio-technical graph mixes three edge kinds.** "Edges between devs: commented in the same
  issue"; "Edges between files: changed together in a commit"; "Edges between devs and files: dev
  changed file". Its purpose is "to understand which developers work on the same files".
- **Node types come from outside the graph or from inside it.** Outside: core versus peripheral
  developers, committers versus issue reporters, project roles. Inside: "how 'important' a node is
  in a network, e.g., high degree".
- **Basic structural properties are reported first.** "Measures for the size" — number of nodes V
  and number of edges E — and "Number of components". These "help us to understand the size, the
  overall number of relations, and if we actually have a single network or disconnected
  subnetworks".

## Worked Example

Take the deck's file set: `changes.md`, `Foo.java`, `BarFoo.java`, `Bar.java`, `FooBar.java`.

**Artifact nodes (technical network).** Each file is a node. The co-change graph puts an edge
between two files "where change together in a commit". This is not a dependency graph: two
implementations of the same interface may be changed together while depending on nothing of each
other.

**Developer nodes (social network).** Take the issue tracker: "Nodes: actors in an issue tracker",
"Edge: commented in same issue". Two variants exist for the same data — the undirected one, which
ignores the order of comments, and the directed one, where an outgoing edge means the developer
commented before the other, "represent knowledge and information flow".

**Mixed graph (socio-technical network).** Put the developers and the five files in one graph with
the three edge kinds above, answering "which developers work on the same files" without two
separate graphs and a manual join.

**Metrics on the result.** Report the size and the number of components first — a disconnected graph
means the "team" you think you are studying is several teams. Then apply the three centralities.
Degree centrality on the directed communication graph separates those who comment a lot (out-degree)
from those who are commented at (in-degree). Closeness centrality identifies the developers a short
hop from everybody — in a project, the person most likely to be asked. Betweenness centrality finds
the developers on the shortest paths between others: the coordinators, and in the socio-technical
graph the people who link separate parts of the code.

## Common Pitfalls

- **Treating the graph as a property of the project rather than of the study.** The nodes and edges
  are choices; a co-change graph and a dependency graph describe different systems.
- **Conflating communication with co-change.** An artifact-mediated tie is a different kind of
  edge, and conflating it with a direct tie inflates the apparent collaboration.
- **Discarding direction.** A directed communication graph carries ordering and flow that an
  undirected one throws away.
- **Using a technical network when the question is about people.** The socio-technical graph exists
  to link "social aspects … and technical artifacts".
- **Assuming connectivity.** Whether there is "a single network or disconnected subnetworks" is a
  question, and disconnected subnetworks change every downstream count.
- **Encoding multiple edge types in one weighted graph.** The lecture's advice is to split into
  multiple graphs instead of "a joint weight/type function".
- **Assuming the tooling's social features are the subject.** "Sometimes studied as well, but more
  often" the features are "exploit[ed] … as data source to understand relationships".
- **Ignoring the absence of a fixed community definition.** A community count is a parameter, not a
  fact.

## Connections

- [[community-smells]] — the four smells built on the communication and collaboration graphs.
- [[degree-centrality]] — the node-degree measure used for C_degree.
- [[closeness-centrality]] — the distance-based centrality measure.
- [[betweenness-centrality]] — the shortest-path centrality measure.
- [[clustering-coefficient]] — the neighbourhood-density measure and a community-detection input.
- [[community-structure]] — the formal side of the partition definition given here.
- [[temporal-networks]] — the temporal dimension the black-cloud smell needs.
- [[conways-law]] — the socio-technical congruence application of the mixed graph.

## Open Questions

- **The Mozilla example is a link, not a description.** The slide "The rebel alliance network from
  the Mozilla Foundation" points at https://report.mozilla.community/ and the extracted text
  describes neither the network nor its nodes or edges.
- **Two formulas are not fully legible in the extracted text.** For graph-level degree centrality
  the slide's normalisation is described — "it normalizes to the interval [0,1]" — but the printed
  denominator is garbled; for closeness centrality the extraction shows the numerator "(V − 1)" and
  the sum of distances "Σ d(u, v)", but not the fraction structure.
- **No thresholds are given for community detection**, and the lecture says it will not discuss the
  algorithms in detail, so how the partitions used downstream were computed is left to the study.
- **Edge weights are mentioned but never specified**, and **node identity is not discussed at all**
  in this lecture — yet merging accounts for the same person is a prerequisite for degree and
  centrality numbers to mean anything.
