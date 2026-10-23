---
title: "Conway's Law and Socio-Technical Congruence"
tags: [concept, mining-software-repositories, semester-2, socio-technical-congruence]
course: "Mining Software Repositories"
source_count: 1
status: current
last_updated: 2026-10-22
prerequisites: ["[[mining-software-repositories]]"]
---

## One-line Summary

Conway's law says a system's architecture copies the communication structure of the organisation
that built it, and socio-technical congruence turns that claim into a computed number: the ratio
of coordination that was required to the coordination that actually happened.

## Core Intuition

The lecture opens Chapter 5 with the law itself, quoted on the slide:

> "Organizations which design systems are constrained to produce designs which are copies of
> the communication structures of these organizations" – Conway, 1968

(Citation on the slide: Conway, Melvin E. "How do committees invent." *Datamation* 14.4 (1968):
28-31.)

The consequence the lecture draws is that "our system design would mimic team structures, which
we also refer to as socio-technical congruence", and — this is what makes the topic MSR rather
than folklore — "That is something we can model with a social-technical network!".

The block is a measurement design, not a philosophy. Two networks are built: a **technical** one
modelling the architecture of the software, and a **social** one modelling who talks to whom
about it. The law is stated by comparing them. If the two line up, Conway's law holds for that
project; if not, the architecture does not follow the communication structure.

Everything after the quote is bookkeeping for that comparison: how to find communities, which
communication counts as relevant, how to turn files into architectural components, how to derive
which developers *should* have coordinated, how to observe which ones *did*, and how to divide
one by the other.

The framework used for the coordination side is Cataldo, Herbsleb & Carley (2008), *Socio-technical
congruence: a framework for assessing the impact of technical and work dependencies on software
development productivity*, ESEM '08, New York, NY, USA, 2-11,
https://doi.org/10.1145/1414004.1414008 — cited on the slide and repeated on every slide of the
block.

## Formal Definition / Statement

**The law.** A system design produced by an organisation is constrained to copy that
organisation's communication structure.

**Communities as the social unit.** The lecture had already used communities earlier in the
chapter, on the idea that communities are "developers that are working closely together". Based
on Conway's law "there should be a relationship between the communities and the architecture".
The example is Del Rosso, Christian, "Comprehend and analyze knowledge networks to improve
software evolution", *JSME* 21.3 (2009): 189-215 — two communities within Apache web server
development: *code-oriented developers* and *documentation-oriented developers*. "The social
structure represents this work on different project components."

**Coordination requirements.** "Not every communication is relevant for a project" — an informal
chat exchange is not coordination. A coordination requirement "is related to communication that
needs to happen within a project", e.g. two developers working on the same component or feature,
or one reporting a bug to another. "Consequently, communication in issue tracking systems is
suitable to model coordination requirements", each issue representing a task (feature addition,
bug fix, …).

**Modelling architectures (static).** The nodes of an architecture network are usually the files
within a project; this is "usually more fine-grained than actual architecture, we should observe
the same boundaries as within the actual architecture", or packages/folders for a coarser
structure. Edges come from usage relationships at code level: "in practice, we usually rely on
import statements: one file uses another, if it is imported". Imports "can be too coarse (e.g.,
import java.util.*) or unused", so "a cleaner but more difficult to obtain variant would be to use
the call graph".

**Modelling architectures (co-change).** Alternatively, model architectures through co-change:
"components that are changed together should belong to the same architectural components".

**Matrices**, as printed on the slides:

```
Taskassign = t_A ∈ {0,1}^(n_devs × n_tasks)  such that A_ij = 1 is developer i worked on task j
Taskdeps   = t_D ∈ N_0^(n_tasks × n_tasks)   such that D_ij = k means that tasks i, j have an overlap of
                                               k files that are directly or indirectly depend
Coordreq   = Taskassign · Taskdeps · Taskassign^T ∈ N_0^(n_devs × n_devs)
Coordactual = c_A ∈ {0,1}^(n_devs × n_devs) such that A_ij = 1 if there was coordination between developers i, j
```

Task dependencies arise because "tasks depend on software artifacts": adding a feature depends
on all files that need to be touched, and dependencies can be indirect (working in a package is
related to other code in the same package). Tasks can be interdependent — "if two features are
added to the same files, these tasks depend on each other". Coordination requirements follow:
"we can say that developers need to coordinate, if they are assigned to dependent tasks", and
"if there are more dependencies in terms of overlapping files, the requirement to coordinate is
stronger" — which is why `Taskdeps` counts overlapping files rather than a yes/no relation.

**The congruence measure**, as printed:

```
Congruence(Coordreq, Coordactual) = #CoordHappened(Coordreq, Coordactual) / #CoordRequired(Coordreq)

#CoordHappened(Coordreq, Coordactual) = Σ_{i,j ∈ {1,…,n_devs} : c_ij > 0 and A_ij > 0}
#CoordRequired(Coordreq)             = Σ_{i,j ∈ {1,…,n_devs} : c_ij > 0}
```

"Values close to one mean that the project communication matches the requirements. The further
away a value is from one, the greater the lack of internal communication which means that the
architecture does not follow Conway's law."

## Key Properties

- **Congruence is computed, not asserted.** "We know have modeled who should coordinate with each
  other (Coordreq) and who does coordinate with each other (Coordactual). We can measure the
  congruence between both by looking at the ratio of the required coordination that took place."
- **The required side comes from the architecture, not the org chart.** "Social-technical
  congruence is closely related Conway's law. The coordination requirements are derived from the
  architectural dependencies."
- **Coordination *activities* are observed communication.** Nodes are developers, edges are
  communication between them, "e.g., within an issue", represented as an adjacency matrix.
- **Two modelling choices exist for the architecture side** — static import/call structure and
  co-change — offered as alternatives with no criterion for choosing.
- **The technical network is a proxy for the architecture.** Using files instead of components
  is an approximation the lecture acknowledges but does not quantify.
- **Communities are the social abstraction, and the chapter has machinery for them.** The
  smells half of Chapter 5 defines communities via the communication graph and detects silos,
  lone wolfs, black clouds and bottlenecks on it — see [[community-smells]].
- **The social side of Chapter 5 uses a different modelling choice.** The smells slides use two
  undirected graphs, `G_comm` and `G_coll`, with `V_coll ⊆ V_comm`. Congruence replaces the
  collaboration graph with the architectural dependency network — that swap makes the measurement
  possible.
- **The measurement is a ratio bounded above by 1**, and the slides give no treatment of what a
  very small `Coordreq` denominator does to the estimate.
- **The framework's purpose is productivity**, not architectural aesthetics: the cited paper
  frames congruence as "assessing the impact of technical and work dependencies on software
  development productivity".

## Worked Example

The social example is the Apache web server study: two communities, code-oriented and
documentation-oriented developers, whose split "represents this work on different project
components". Read through the congruence model, this is a prediction — if the communities line up
with the component structure, `Coordreq` is block-like and `Coordactual` should mirror it; if
documentation-oriented developers do not talk to code-oriented developers about code files,
`Coordactual` has holes exactly where `Coordreq` is non-zero, and the ratio falls below one.

The chapter's running example is a small file set — `changes.md`, `Foo.java`, `BarFoo.java`,
`Bar.java`, `FooBar.java` — used on the smells slides for communication edges, collaboration
edges and community boundaries, and reused on the "Conway's law and communities" and "Black
clouds" slides with gray areas as communities. Applied to the congruence model, it gives a tiny
instance of the matrices: `Taskassign` has one row per coloured circle and one column per issue;
`Taskdeps` has a 1 wherever two issues touched overlapping files;
`Coordreq = Taskassign · Taskdeps · Taskassign^T` therefore has a non-zero entry exactly for
pairs of developers who jointly worked on dependent tasks — in the example, the orange/grey pair
that collaborated on `FooBar.java` without communicating, identified on the smells slides as both
an organisational silo and a lone wolf.

For that pair: `Coordreq` says they must coordinate (they touched the same file), `Coordactual`
says they did not, so they contribute to `#CoordRequired` but not to `#CoordHappened`. That
single pair is what drags the ratio below one.

## Common Pitfalls

- **Treating the law as a slogan about org charts.** The claim concerns *communication*
  structures, and the measurable object is congruence between required and actual coordination.
- **Using all communication as coordination.** "Not every communication is relevant for a project."
- **Modelling the architecture only from coarse imports.** `import java.util.*` is too coarse,
  unused imports are spurious, and the call graph is the cleaner alternative — at a price.
- **Ignoring indirect dependencies in `Taskdeps`.** Only direct overlap understates the
  coordination requirement.
- **Using the collaboration graph where the architecture network belongs.** Substituting `G_coll`
  makes the measurement circular.
- **Confusing "congruence close to one" with "good architecture".** The slides only interpret the
  ratio as "the project communication matches the requirements".
- **Comparing ratios across projects without the denominator.** A project with almost no
  dependent tasks has a small `Coordreq` and a ratio that is easy to bring near one.
- **Skipping the community step and using raw nodes as the social unit.**

## Connections

- [[mining-software-repositories]] — the pipeline framing this measurement sits inside.
- [[community-smells]] — the other half of Chapter 5; the community machinery reused here.
- [[developer-social-networks]] — the communication graph that supplies `Coordactual`.
- [[community-structure]] — how communities are detected in the social network.
- [[modularity]] — the community-detection lens on the same social structure.
- [[software-metrics]] — file-level metrics feeding the architecture network.
- [[msr-statistical-methods]] — how a congruence value is tested rather than merely reported.
- [[threats-to-validity]] — proxy measures of architecture are a construct-validity concern.
- [[mining-software-repositories-lecture-5]] — the source lecture for this page.

## Open Questions

- **The summation conditions in the congruence formula are ambiguous as printed.** The slide
  text reads `#CoordHappened = Σ_{i,j ∈ {1,…,n_devs} : c_R > 0 and A > 0}` and
  `#CoordRequired = Σ_{i,j ∈ {1,…,n_devs} : c_R > 0}`, where `c_R` is defined nowhere on the
  slide, and the index sets do not state whether the sum runs over ordered or unordered pairs.
  The formulas are quoted as printed; the intended reading is presumably that `c_R` denotes the
  required-coordination matrix and `A` the actual one, but the slides do not say so.
- **The direction of the law is not tested.** No slide says what to conclude if congruence is
  high — whether communication caused the architecture or the two are merely consistent.
- **There is no criterion for choosing between static and co-change architecture modelling**, nor
  any statement of how sensitive the congruence value is to the choice.
- **Indirect dependencies are stated but not operationalised.** No rule gives how many hops count
  as indirect, nor how the `k` overlap is weighted.
- **No community-level statistic is presented.** The slides say the law "can be studied by
  looking at communities", but the ratio is computed over developer pairs, not communities.
