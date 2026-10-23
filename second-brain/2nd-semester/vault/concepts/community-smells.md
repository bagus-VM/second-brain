---
title: "Community Smells"
tags: [concept, mining-software-repositories, semester-2, social-aspects, community-smells]
course: "Mining Software Repositories"
source_count: 1
status: current
last_updated: 2026-10-22
prerequisites: ["[[developer-social-networks]]"]
---

## One-line Summary

Community smells are the social counterparts of code smells: patterns in a community's
communication structure that indicate a deeper problem, detectable as four concrete graph
configurations.

## Core Intuition

The lecture starts from the established meaning of the word. "In software engineering, we use smell
with a negative connotation", and the usage "originates from the Refactoring book, where the term
code smell was coined" (Fowler & Beck, *Refactoring: Improving the Design of Existing Code*). A code
smell "describes a pattern that indicates that the underlying code might have a deeper problem" —
the examples are *feature envy* ("a component relies more on one other component then itself") and
*god class*.

The move from code to community is a deliberate analogy of that structure. "Code smells are not
bugs, but are associated with them" and "Code smells are a type of technical debt". The lecture
adopts the metaphor for the social side: "The notion of technical debt was adopted for the study of
social debt", where "Social debt indicates that there are problems within a community that are not
being addressed". Hence:

> "A code smell is a pattern within source code that indicates some deeper problem within that
> code. A community smell is a pattern in the community structure that indicates some deeper problem
> within that community."

The provenance matters for the method. "The first set of community smells were identified by a
qualitative study in which developers from a company were interviewed", "carried out based on open
and axial coding of the interview responses", which "allowed deep insights into a single process and
to generalize from there to define a set of community smells". What is missing is breadth: "broader
perspectives on the relevance and prevalence of community smells → This is what MSR can provide!"
(Tamburri et al. 2015). The detection engine is a pair of graphs: "developer social networks are a
suitable tool to study them".

## Formal Definition / Statement

**The communication graph** `G_comm = (V_comm, E_comm)`: "The nodes are the developers taking part
inf communication"; "An edge e = {u, v} ∈ E_comm between two developers u, v ∈ V_comm exists iff
the developers communicated with each other in any medium".

**The collaboration graph** `G_coll = (V_coll, E_coll)`: "The nodes are the developers that modify
source code elements"; "An edge e = {u, v} ∈ E_coll between two developers u, v ∈ V_coll exists,
iff the developers worked on the same source code elements (i.e., files)". Both are undirected.
"We assume that V_coll ⊆ V_comm. Otherwise, we would have code contributors that are not
communicating, which is an obvious problem anyways".

**Organizational silos.** "A silo is an independent sub-community. Silos often lead to duplication of
effort", e.g. "because the same problems are solved multiple times, lack of re-use of code between
silos". Silos can also have negative effects when they lead to "egotistical behavior". Formally:

```
Silos = { {u, v} : u, v ∈ V_coll : no path from u to v exists in G_comm }
```

i.e. "pairs of developers working on (not necessarily the same) code, that do not communicate with
each other (not even indirectly via other developers)".

**Lone wolves.** "If developers work on the same code, they should communicate with each other.
Otherwise, there is a big risk that a non-communicating developers makes decision about the code
that are not in line with the architecture or design envisioned by the remainder of the team. We call
developers who act with such unchecked autonomy lone wolfs". Formally:

```
LoneWolfs = { {u, v} ∈ E_coll : no path from u to v exists in G_comm }
```

and "By definition, we have LoneWolfs ⊆ Silos" — the lone-wolf condition additionally requires the
two developers to share a file.

**Black clouds.** "We say that there is a black cloud in the communication, if there is an inability
to exchange knowledge and experiences between different (sub-)projects regularly". The name "stems
from the idea that a black cloud (e.g., due to a personal conflict) inhibits communication for a
longer period of time". The projects are captured as communities of `G_comm`, "based on the idea
that working together as a community defines a project". For p_i, p_j:

```
bridge_ij = { {u, v} ∈ E_comm : u ∈ p_i and v ∈ p_j }
```

"There is a black cloud between communities p_i, p_j if bridge_ij = 1 and these developers did not
communicate for a longer time interval. The literature used 6 months as time interval."

**Bottlenecks (also called Radio Silence).** "Similar to a black cloud, a bottleneck indicates a
problem in the communication between communities. While black clouds look at the temporal component
in information exchanges, bottlenecks consider only if there is a single-point of failure for the
communication." Concretely, "if there is only a single developer in one community, that handles the
communication with another community". Formally, "we have a bottleneck between p_i, p_j if
v ∈ V_i: ∃ u, v ∈ bridge_ij = 1". "By definition, each black cloud is a bottleneck", and "If there is
only one edge between communities, there can also be only developer handling the communication".

**Diversity and the statistical model.** Diversity is "a broad concept" including "Gender
diversity", "Cultural diversity", "Sexual orientation"; in software development "diversity is a
social aspect", the listed aspects "are all not related to competency" and "may all affect
communication and collaboration". The hypothesis, from "prior management literature on gender
diversity": "The presence of women within the team improves communication, co-operation, and
collaboration, thus reducing the number of community smells". The model is a linear regression with
an ANOVA-style test on the coefficients:

- *Independent*: "Number of women in a team", "Blau-Index (1 − (Σ p_i^male)² + (Σ p_i^female)²)".
- *Dependent*: "Number of organizational silos", "Number of lone wolfs", "Number of black clouds",
  "Number of bottlenecks".
- *Confounding/control*: "Number of committers", "Number of commits", "Team size", "Turnover of
  developers", "Project age", "Tenure diversity", "Tenure median", "Ratio of collaborations and
  communications (|E_coll| / |E_comm|)", "Truck factor", "Centrality".

## Key Properties

- **The four smells differ in whether time matters.** Silos and lone wolves compare two graphs
  (communication vs collaboration). Black clouds and bottlenecks compare *communities inside* the
  communication graph: black clouds are temporal, bottlenecks structural.
- **The smells are nested, not parallel.** `LoneWolfs ⊆ Silos`; "each black cloud is a bottleneck",
  so one pair can exhibit several smells at once.
- **The detection rules are graph-theoretic, not statistical.** A path-based test for silos and lone
  wolves ("no path from u to v exists in G_comm") means the condition is about reachability
  through any chain of developers, not about direct communication.
- **Community detection is a prerequisite.** Black clouds and bottlenecks need the communities of
  `G_comm`, and "There is no fixed definition of community in terms of how many internal connections
  are required and how many external connections are allowed" — the algorithm is a parameter of the
  analysis. See [[community-structure]].
- **Detection is framed as a precursor for action.** "Detection is often a precursor for corrective
  measures"; "Smells can inform activities that should increase the health of a community".
- **The unit of counting differs.** Silos and lone wolves are counted as *pairs* of developers;
  black clouds and bottlenecks as *pairs of communities*.

## Worked Example

The deck builds the example on the same five artefacts used in the social-networks lecture:
`changes.md`, `Foo.java`, `BarFoo.java`, `Bar.java`, `FooBar.java`. The legend distinguishes an edge
in `G_comm`, an edge in `G_coll`, a "Worked on file" tie, and two node kinds — "Node in collaboration
and communication graph" versus "Node only in communication graph". A grey area marks a community.

**Silos.** Take two developers, one in an orange circle and one in a grey circle, who are connected
in the collaboration graph but between whom "No communication between these circles" exists — the
slide's conclusion: "All pairs of developers between orange and grey are organizational silos".
Because the condition is "no path from u to v exists in G_comm", they must be entirely disconnected
in the communication graph.

**Lone wolves.** The same figure then notes: "Since the collaboration between orange and grey is
even on the same file (FooBar.java), the organizational silos are also lone wolfs." Sharing
`FooBar.java` additionally makes the pair a lone wolf.

**Black clouds.** In the community view, the two grey-shaded regions are communities, and the single
edge between them is the bridge, marked "Only edge between two communities". The condition: "Black
cloud if no communication for longer period of time" — the literature's 6-month interval.

**Bottlenecks.** The next slide makes the temporal/structural distinction visible: "These black
clouds are also bottlenecks", and, crucially, "Would still be a bottleneck if we add the blue line
as additional communication between the communities, but not a black cloud anymore". Adding the
second edge changes the bridge size from 1 to 2, so the single-point-of-failure condition fails
while the temporal condition still holds.

**The model on real data.** "Results for bottlenecks" reports: "Developer turnover is the main driver
behind this smell" and "More women reduce the likelihood of this smell". "Results for lone wolfs"
reports: "Explained by team size and ratio of collaborations/communications" and "No relation to
number of women or Blau-index".

## Common Pitfalls

- **Confusing a silo with a lone wolf.** Both require no communication path; only the lone wolf
  additionally requires a shared file.
- **Counting direct edges instead of reachability.** The rule is "no path … exists", so two
  developers linked through a chain of colleagues do communicate and are not a silo.
- **Treating a black cloud as time-invariant.** Adding a second communication edge removes the
  bottleneck but not the black cloud, because the black cloud is about the *duration* of the silence.
- **Assuming the four smell models are interchangeable.** The regression counts silos and lone
  wolves as developer pairs and black clouds and bottlenecks as community pairs.
- **Ignoring the community algorithm.** Every black cloud and bottleneck number depends on how
  communities were defined, and the lecture gives no default.
- **Over-reading the diversity results.** "More women reduce the likelihood" of bottlenecks is a
  regression result with control variables, and the lone-wolf result finds no relation to number of
  women or the Blau index.
- **Looking for Conway's law here.** The socio-technical congruence material is a separate block of
  the same lecture, covered on [[conways-law]].

## Connections

- [[developer-social-networks]] — the graph machinery the two smell graphs are built from.
- [[conways-law]] — the other half of the lecture's social-aspects chapter.
- [[grounded-theory]] — the open and axial coding study that first identified the smells.
- [[qualitative-coding]] — the coding mechanics behind that original study.
- [[community-structure]] — the communities the black-cloud and bottleneck counts rest on.
- [[temporal-networks]] — the temporal dimension the black-cloud condition needs.
- [[msr-statistical-methods]] — the linear model, ANOVA test and coefficient interpretation.
- [[threats-to-validity]] — where the community-detection choices become validity threats.
- [[msr-data-noise]] — identity resolution and communication data quality behind the edges.

## Open Questions

- **The worked example's figures are pictures.** The extracted text gives the legend and the
  per-slide conclusions but not the number of developers, the exact edges, or which developers are
  the circles; the example above reconstructs only what the text states.
- **No prevalence figures are given.** The lecture says what MSR can add — "broader perspectives on
  the relevance and prevalence of community smells" — but the slides report no rates for how often
  any of the four smells occurs.
- **The regression's coefficients are not in the material.** The results slides state which
  variables matter but give no effect sizes, confidence intervals or model fit.
- **The Blau index construction is not given** beyond the formula fragment, the male/female
  proportions for the studied projects are unexplained, and the community-detection algorithm behind
  the black-cloud counts is never specified.
