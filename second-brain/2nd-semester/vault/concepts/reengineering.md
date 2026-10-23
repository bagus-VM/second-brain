---
title: "Reengineering"
tags: [concept, reverse-and-reengineering, semester-2, maintenance]
course: "Reverse- and Reengineering"
source_count: 2
status: current
last_updated: 2026-10-22
prerequisites: []
---

## One-line Summary
Reengineering is the examination and alteration of an existing system in order to reconstitute it
in a new form — the full round trip from bad code back to requirements and forward again.

## Core Intuition

The word that does the work in the definition is **"new form"**. Reengineering is not repair and
it is not extension. It takes a system as it is, works out what it actually does, and builds a
replacement that does the same things in a shape that can be maintained. The output is not a patch
on the old code; it is a fresh implementation whose requirements were *rediscovered* from the old
implementation.

That rediscovered part is what separates reengineering from a rewrite. A rewrite starts from a
specification somebody writes from memory or from a requirements document that has drifted out of
date. A reengineering project starts from the artefact itself and recovers the specification
*out of* it. This is why the lecture's process diagram is a loop rather than a line — reverse
engineering feeds restructuring, restructuring feeds forward engineering, and forward
engineering produces the improved code, which then becomes the input to the next iteration of
understanding.

The course's central claim about why this work exists is the claim about **software aging**: a
system that was good enough on release degrades because requirements change and features are
piled onto an architecture that was never designed for them. Nothing about the program breaks;
the *context* moves away from it. So the answer is not "fix the bugs" but "recover the design and
rebuild on it", which is why the process is presented as a cycle through all three engineering
disciplines rather than as a maintenance activity.

Note what reengineering is explicitly **not**: the slides' own comparison slide draws the
contrast against *maintenance*. Maintenance serves the customer and adapts the software to the
customer's wishes; reengineering serves the developer and reconstitutes the system. A team that
has been asked to "maintain" a legacy system for a decade and has never been given the mandate to
restructure it has been doing the first thing, not the second.

## Formal Definition / Statement

Chikofsky and Cross (1990), quoted verbatim on the slide:

> "Reengineering, also known as both renovation and reclamation, is the examination and
> alteration of a subject system to reconstitute it in a new form and the subsequent
> implementation of the new form."

Three clauses, each of which constrains the activity:

| Clause | What it rules out |
|---|---|
| "examination ... of a subject system" | The starting point is the system itself, not a specification |
| "alteration ... to reconstitute it in a new form" | The output is not a patched old system; it is a new form of the same thing |
| "and the subsequent implementation of the new form" | Understanding alone is not reengineering; the new form must actually be built |

The process, as the slides draw it:

```
Reverse Engineering   ->   Program Code in poor Quality
Restructuring         ->   Rediscovered Requirements and Design
Forward Engineering   ->   Improved Requirements and Design
                     ->   Improved Code
```

And forward engineering itself runs in the opposite direction of the top row:

```
Abstract representation / model of a system
        -- Forward Engineering -->
Concrete, physical implementation
```

Reengineering is therefore the composition of the two: run the forward process backwards to get
the model, restructure the model, then run the forward process forwards to get better code.

## Key Properties

- **It is a loop, not a line.** The improved code is again a subject system that can be examined
  and reconstituted.
- **The subject system may be specified only as code.** The lecture's reverse-engineering
  workflow runs "Program Code → Specification", and the "worst case" input on the abstraction
  ladder is object code, not source.
- **Reverse engineering and restructuring are separate steps with separate failure modes.**
  Restructuring changes the *form*; reverse engineering changes the *understanding*. A project
  that restructures without understanding is rewriting; one that understands without
  restructuring is documentation.
- **Forward engineering is part of it.** Reengineering that stops at recovered design has
  delivered an analysis, not a reengineering. The slides' diagram always ends in "Improved Code".
- **Refactoring is a component of restructuring**, not the whole of it — see
  [[refactoring-and-code-smells]].
- **It serves the developer, not the customer** — see [[reengineering-vs-maintenance]].
- **It starts from legacy-system conditions** in practice: obsolete languages, missing
  documentation, huge code bases and lost knowledge — see [[legacy-systems]].
- **It can be done three ways**, with very different cost and risk profiles: packing, migration,
  or replacement in one fell swoop — see [[legacy-system-renewal]].
- **Legal constraints are real and material.** The reverse-engineering lecture opens with a
  disclaimer: reverse engineering may be illegal depending on purpose and situation, Directive
  2009/24/EC (the Computer Programs Directive) is referenced, and it is the student's
  responsibility to stay legal. Repairing a product you own by disassembling it is usually legal;
  copying a competitor's design is not.
- **The exam is graded on the concepts, not on tools.** The slides name tools — IDA, GCC's CFG
  dumps, the Eclipse Sourcecode Visualizer — but the learning objectives talk about creating
  "prototypical systems", i.e. the analysis techniques, not the products.

## Worked Example

The lecture runs one small program through the whole pipeline, and it is worth following because
it is what the exercises then ask you to reproduce.

Start with a fragment of legacy C:

```c
read (x);
a = 0;
if (x > max) { x=max;  a=1; }
else if (x < min) { x=min; a=1; }
print (x);
print (a);
```

**Reverse engineering.** The analyst splits the fragment into basic blocks — "a chain of
statements that is guaranteed to be executed one after the other for as long as possible" — B1
through B5, and draws the intraprocedural control flow graph: B1 → (x > max ? B2 : B3), B2 → B5,
B3 → (x < min ? B4 : B5), B4 → B5. That is the *control* structure recovered from the text.

The **program dependence graph** then recovers the *data* structure, and in doing so drops the
statement order: control dependence edges (A determines whether or how often B executes) and data
dependence edges (B uses a variable assigned at A, with a path from A to B on which the variable
is not reassigned) replace the CFG's edges. In the PDG, the `if` conditions sit between the
assignments and the prints, and the ordering information is gone — which is exactly the point,
because a PDG answers "what depends on what", not "what runs when".

**Slicing.** Choose the printing of `x` as the slicing criterion and ask backwards: which
statements influence it? The answer is the read, the comparison against `max`, the clamp
`x=max` and the print — but *not* the `a=1` assignments, because `a` never reaches `x`. Choose
`a=0` and slice forwards: which statements are influenced by it? The answer is the `a=1`
assignments and the print of `a` — but not the `x` branch, because `a` never influences `x`.
That asymmetry is the whole utility of slicing: it cuts a 15-line program down to the 4 or 5
statements that actually matter for one question.

**Restructuring.** Having established what the code does, the analyst identifies the smells —
here, a long if/else-if chain on the same variable, and duplicated `a=1` — and rewrites it, for
example by clamping `x` into `[min, max]` and setting `a` from the comparison result, with the
same external behaviour.

**Forward engineering.** The recovered design (clamp the input, report whether it was clamped)
becomes the specification for the new form, and the new form is written from that.

**Legacy renewal.** The same fragment, seen as a product, becomes the input to one of the three
renewal strategies: pack it behind a modern interface, migrate it component by component, or
replace it wholesale.

## Common Pitfalls

- **Confusing reengineering with rewriting.** Rewriting starts from a (usually missing or stale)
  specification; reengineering starts from the system and *derives* the specification. The
  difference is where the requirements come from.
- **Confusing reengineering with maintenance.** Maintenance adapts the system to what the
  customer wants now; reengineering reconstitutes it so it can be worked on. See
  [[reengineering-vs-maintenance]].
- **Stopping after reverse engineering.** Recovering the design is half the loop. The slides'
  diagram ends in "Improved Code"; a project that produces a specification document and stops has
  done a documentation project.
- **Treating "new form" as "new code" without preserving behaviour.** Refactoring must keep the
  external behaviour identical, and that is what makes regression testing mandatory rather than
  optional — see [[refactoring-and-code-smells]].
- **Underestimating the loss of information.** Compilation destroys names, structure and types.
  Slide 37 of lecture 1 is blunt: reverse engineering "can only be partially automated due to the
  analyst's own high level of effort". A tool can recover the CFG; nobody can recover the
  developer's intent.
- **Forgetting that static analysis cannot prove execution.** Slide 37 again: static analysis
  cannot always state whether code is actually executed in practice. A recovered control-flow
  graph is a hypothesis about the program, not a transcript of it.
- **Ignoring the legal dimension.** The disclaimer slide is not boilerplate; reverse engineering
  for interoperability and reverse engineering for copying are different acts with different legal
  outcomes.
- **Assuming the legacy system's tests exist.** A large part of why legacy systems are hard is
  that nobody knows what correct behaviour is — which is exactly why the behaviour has to be
  *rediscovered* rather than *read off a spec*.

## Connections

- [[software-aging]] — the reason the work is needed at all: quality erodes as requirements move.
- [[reverse-engineering]] — the first third of the reengineering process.
- [[reengineering-vs-maintenance]] — the distinction the professor puts on its own slide.
- [[refactoring-and-code-smells]] — restructuring is the second third, and refactoring is its
  code-level part.
- [[legacy-systems]] — the input that reengineering is normally applied to.
- [[legacy-system-renewal]] — the three strategies (packing, migration, replacement) that carry
  a reengineering project in practice.
- [[architecture-smell]] — the level above code smell, which needs human judgement to fix.
- [[control-flow-graph]] — the Semester 1 page; the CFG in the lecture is the same graph.
- [[program-dependence-graph]] — the Semester 1 page; the PDG in the lecture is the same graph.
- [[program-slicing]] — the Semester 1 page; forward/backward slicing and the slicing criterion
  come from there.
- [[software-analysis]] — the general field the lecture's reverse-engineering workflow mirrors.

## Open Questions

- **The slides never quantify the effort.** "The reverse engineering process can only be partially
  automated due to the analyst's own high level of effort" is asserted, not sized. Nothing in the
  material gives a ratio of automated to manual work, or a rule of thumb for when a
  reengineering project is worth starting.
- **The boundary between restructuring and reengineering is not defined.** The slide defines
  restructuring (same semantics, same external behaviour) and refactoring (internal structure
  improved, external behaviour maintained) but never says what makes restructuring "part of"
  reengineering rather than a separate activity.
- **"New form" is left unspecified.** Chikofsky/Cross's phrase does not say how much of the
  original system may survive into the new form — is a reimplemented component still the same
  subject system? The lecture does not say.
- **The relationship between the three renewal strategies is not compared.** Packing, migration
  and replacement are listed with one-line descriptions and no cost, risk or effort comparison.
- **No worked example of the full loop is given.** The lecture demonstrates reverse engineering
  and slicing on a fragment, and describes restructuring in the abstract; the "improved code" half
  of the loop is never actually shown for that fragment.
- **The exam's coverage is not stated.** Only "90 points, 90 minutes" is given — how many
  questions, and whether the legal/disclaimer material is examinable, is not said.
