---
title: "Reverse Engineering"
tags: [concept, reverse-and-reengineering, semester-2, reverse-engineering, program-analysis]
course: "Reverse- and Reengineering"
source_count: 2
status: current
last_updated: 2026-10-22
prerequisites: ["[[software-aging]]"]
---

## One-line Summary
Reverse engineering is the analysis of a system that supports understanding it — identifying its
components and artifacts, discovering their relationships, and generating abstractions — with the
explicit goal of not altering the system in any way.

## Core Intuition

The definition on slide 3 of lecture 2 is the one to hold on to, because every other slide is
an elaboration of it:

> Reverse engineering supports understanding of a system through identification of the components
> or artifacts of the system, discovering relationships between them, and generating abstractions
> of that information. Goal: no alteration of the system in any way. Abstractions: similar to SE.
> Purpose: maintenance, alteration, or abuse.

(Chikofsky and Cross, "Reverse Engineering and Design Recovery — A Taxonomy", IEEE Software,
Jan 1990, 13–17.)

Two words in that definition carry the concept. The first is **"supports understanding"** — the
output is knowledge, and knowledge is a legitimate end in itself. The second is **"no
alteration"** — reverse engineering stops at understanding. The moment you change the system, you
are no longer reverse engineering; the lecture's process diagram puts alteration in a separate
step called restructuring, under the umbrella of reengineering (see [[reengineering]]).

The third part — "abstractions: similar to SE" — explains why the whole software-engineering
vocabulary (design, architecture, components, requirements) applies to artefacts that have no
source code. Recovery is the same intellectual operation as forward engineering, run in the
opposite direction: where forward engineering goes from an abstract model to a concrete
implementation, reverse engineering goes from a concrete artefact back to an abstract model. The
slide 6 picture, "Reversing forward engineering", shows the Requirement / Architecture design /
System design / Implementation ladder with the analysis arrow pointing back up.

The word "abuse" in "purpose: maintenance, alteration, or abuse" is not a throwaway: the same
technique serves opposite ends, and the lecture opens with a disclaimer that reverse engineering
may be illegal depending on purpose and situation, referring to Directive 2009/24/EC (the
Computer Programs Directive) and national implementation law. Repairing a product you own by
disassembling it and replacing a part is usually legal; copying a competitor's design is not.

## Formal Definition / Statement

Lecture 1 slide 13 gives the older, looser formulation used for the software-engineering
framing:

- Reverse engineering indicates a way to analyze a system.
- Identification of system components and their relationships.
- Presentation of the system in a more understandable form.
- Goals: facilitate understanding of the system; create the basis for future software
  maintenance.

Lecture 1 slide 14 gives the workflow as a ladder, from the concrete to the abstract
(Ludewig 591):

```
Object Code -> Source Code -> Detailed Design -> System design -> Specification
```

Lecture 1 slide 15 gives the process as a table with three inputs feeding every stage — domain
knowledge (component analysis, relationships), documentation, and expert knowledge (requirements
recovery) — and the stages:

```
Source Code --Parsing--> Intermediate Representation
           --Component Analysis--> Design (Architecture)
           --Design Recovery--> Requirements (Model)
           --Design Reconstruction--> Design Model
```

Lecture 2 slide 4 gives the **goals**:

- Discover underlying system features: requirements, specifications, design and implementation.
- System structure: components, their interrelationships (interfaces).
- Functionality: operations performed (on what components).
- Dynamic behaviour: how input is transformed to output.
- Rationale: decision making between a number of alternatives at each design step.
- Construction: modules, documentation, test suites, etc.

Slide 5 gives the **purposes**: understand the semantics of the program; reengineering;
find/fix bugs, quality issues or defects (own software or third-party); security audits (e.g. an
untrusted compiler); management issues (programming standard); forensic analysis of malware (what,
who, countermeasures); protocol/API analysis; learning design decisions and programming
practices; discovering the underlying business model; identification of intellectual property
infringements.

The process itself is given on slides 7–9 of lecture 2 as four steps:

1. **Data acquisition** — identify a system's artifacts and their relationships. Techniques:
   dynamic program analysis and profiling; static program analysis; informal extraction from
   other information sources; potentially domain knowledge (from involved developers etc.);
   documentation; searching other sources (internet, etc.).
2. **Knowledge organization** — create a model of the software (→ SE); efficient storage of
   information; data structures allowing automated analysis; appropriate abstraction level.
3. **Information exploration** — navigate through links in the data structures (mostly manual);
   hierarchies, control flow, data flow, dependences; analysis beyond the basic model (patterns,
   domain knowledge); presentation (visualization, etc.).

with the framing on slide 6 that the whole thing is "reversing forward engineering" and that the
central problem is **lost information**.

## Key Properties

- **Non-invasive by definition.** "No alteration of the system in any way" is a constraint on the
  technique, not a preference.
- **It is upstream of maintenance and reengineering.** Purposes 1 and 2 of the list are
  "understand semantics" and "reengineering"; see [[reengineering-vs-maintenance]].
- **Legality depends on purpose and situation.** The disclaimer is part of the definition's
  context, not a footnote.
- **The abstraction level is a deliberate choice.** Knowledge organization explicitly includes
  "appropriate abstraction level" — the analyst decides how coarse the recovered model is.
- **Information is lost irreversibly.** Compilation destroys method and attribute names
  (lecture 1, slide 37), so "interpretation and expert knowledge of the code during the analysis
  becomes necessary".
- **Static analysis cannot prove execution.** Lecture 1, slide 37: static analysis cannot always
  make statements about whether code is actually executed in practice. A recovered control-flow
  graph is a hypothesis.
- **Only partially automatable.** Slide 37: the reverse engineering process can only be partially
  automated, due to the analyst's own high level of effort.
- **The output feeds a loop.** The recovered requirements and design are the input to
  restructuring, and the improved code is again a subject system.

## Worked Example

The lecture's running example (lecture 1, slides 17–19) is a legacy C fragment:

```c
read (x);
a = 0;
if (x > max) { x=max; a=1; }
else if (x < min) { x=min; a=1; }
print (x);
print (a);
```

*Constructed illustration — the fragment is source material; the walk-through below assembles the
lecture's own analyses of it.*

**Reverse engineering.** The analyst splits the fragment into basic blocks — "a chain of
statements that is guaranteed to be executed one after the other for as long as possible" —
B1 through B5, and draws the intraprocedural control flow graph: B1 → (x > max ? B2 : B3),
B2 → B5, B3 → (x < min ? B4 : B5), B4 → B5. That recovers the control structure; see
[[control-flow-graph]] and [[basic-block]].

**Program dependence graph.** The PDG recovers the data structure instead: control dependence
(A determines whether or how many times B executes) and data dependence (B uses a variable
assigned at A, with a path from A to B on which the variable is not reassigned) replace the
CFG's edges. In the PDG the statement order is gone, which is the point — a PDG answers "what
depends on what", not "what runs when"; see [[program-dependence-graph]].

**Slicing.** With `print (x)` as the slicing criterion, backward slicing yields the read, the
comparison against `max`, the clamp and the print — but not the `a=1` assignments, because `a`
never reaches `x`. With `a=0` as criterion, forward slicing yields the `a=1` assignments and
the print of `a` — but not the `x` branch. Slicing is a static-analysis technique used during
reverse engineering to answer "which variables are affected by a particular variable" and
"which variables affect a particular variable"; see [[program-slicing]].

**Post-documentation and architectural rediscovery.** After the code is presented in a clearer
form, an attempt is made to extract higher-level constructs from archaic code (loops,
parameters, abstract data types), and the software architecture is derived from the existing
program code — which requires knowledge of software architectures, of the programming language
used, and of successful post-documentation (lecture 1, slide 36).

## Common Pitfalls

- **Conflating reverse engineering with reengineering.** Reverse engineering produces
  understanding; reengineering additionally alters and reimplements. The distinction is the
  "no alteration" clause.
- **Treating the recovered model as ground truth.** Because static analysis cannot always say
  whether code is executed, the recovered design is a hypothesis to be tested.
- **Expecting names to survive.** Method and attribute names are lost during compilation; a
  recovered API with meaningless identifiers is normal, not a failure of the tool.
- **Assuming automation.** The lecture is explicit that only partial automation is possible
  because of the analyst's effort.
- **Ignoring the call graph.** Lecture 1, slide 19: nodes are method names, and an edge from a
  to b exists if a possibly calls b; after a function is finished it returns to the calling
  function. Interprocedural control flow is a separate analysis from intraprocedural
  control flow (slide 16), and combining them is what yields the full picture.
- **Confusing analysis with alteration.** Changing the artefact while analysing it destroys the
  "no alteration" property and the legal framing with it.
- **Overlooking the non-code inputs.** Domain knowledge, documentation and informal sources are
  listed as first-class techniques, not as fallbacks.

## Connections

- [[reengineering]] — reverse engineering is the first stage of the reengineering loop.
- [[software-aging]] — the reason understanding is needed: quality erodes as requirements move.
- [[binary-reverse-engineering]] — the case where the subject system is available only as object
  code.
- [[x86-assembly-and-abi]] — the concrete ISA the binary case is analysed against.
- [[reengineering-vs-maintenance]] — who consumes the recovered understanding.
- [[control-flow-graph]] — the intraprocedural recovery step.
- [[program-dependence-graph]] — the data-structure recovery step.
- [[program-slicing]] — the technique that cuts the artifact down to one question at a time.
- [[software-analysis]] — the general field the workflow mirrors.
- [[reverse-and-reengineering-lecture-2]] — the lecture that supplies the definition, goals and
  purposes.

## Open Questions

- **How much of the four-step process is automatable in each case?** The slides state that
  reverse engineering is only partially automatable because of the analyst's effort, but give no
  split between the data-acquisition, knowledge-organization and exploration steps.
- **What is the boundary between reverse engineering and the forbidden alteration, and how are
  the "purposes" selected?** The definition says "no alteration in any way" and lists
  "maintenance, alteration, or abuse" as purposes, without saying where documentation or
  instrumentation during analysis crosses the line. Ten purposes are listed with no criterion
  for which one a given project pursues, and no mapping from purpose to technique.
- **The rationale goal is listed but never operationalized.** "Decision making between a number
  of alternatives at each design step" is a recovery goal, yet the source offers no technique for
  recovering it from code.
- **No method is given for validating a recovered specification.** The lecture's
  problems-of-reverse-engineering slide lists information loss, the limits of static analysis and
  partial automation, but no way to check a recovered model against the running system.
