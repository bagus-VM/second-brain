---
title: "Legacy System Renewal"
tags: [concept, reverse-and-reengineering, semester-2, legacy-systems, reengineering]
course: "Reverse- and Reengineering"
source_count: 1
status: current
last_updated: 2026-10-22
prerequisites: ["[[legacy-systems]]", "[[reengineering]]"]
---

## One-line Summary
The lecture names three procedures for renewing a legacy system — packing it behind a modern
shell, migrating it component by component, or replacing it in one fell swoop — and gives no
comparison between them.

## Core Intuition

Renewal is the action half of the legacy-systems story. The previous slide lists what a legacy
system is: obsolete languages, platforms and operating systems; often poorly documented; often a
very large code base; no knowledge among the company's employees about its handling and
architecture; and — the clause that makes renewal a matter of urgency rather than of taste —
legacy systems oftentimes perform critical tasks in a company. The slide that follows is the
answer: "There are three basic procedures for renewing legacy systems".

What unifies the three is that each keeps the legacy system alive while something else is built
around or alongside it. **Packing** designs a new software as a shell that provides a modern
interface to the outside world but communicates internally with the legacy software. **Migration**
renews the software step by step: you divide the system into components and renew one component
after the other. **Replacement in one fell swoop** develops the software completely from scratch
while still using the old software during the development phase. In no case does the old system
stop being used before the new one exists.

That last observation is the conceptual spine of the slide, even though the deck never states it
that way. All three manage the overlap between an old and a new system, and they differ in how:
in packing the overlap is structural and permanent (the shell always talks to the legacy core), in
migration it shrinks step by step as components are swapped, and in replacement it lasts for the
whole development phase and then disappears in one cut.

Renewal is also the process the lecture has been building, applied to a running,
business-critical legacy system. The reengineering diagram runs reverse engineering →
restructuring → forward engineering, ending in improved code; the analysis techniques of the
earlier slides are what make it possible to divide the system into components at all, and the
refactoring material is what renewing a component consists of.

The learning-objectives slide states the topic as a pair: "Explain the challenges of legacy
systems and how they can be renewed". The challenges are on the legacy-systems slide; the "how" is
this slide. The deck's coverage of the "how" is three one-line definitions and nothing more — no
criteria, no comparison, no recommendation.

## Formal Definition / Statement

The slide, verbatim:

> "Renewal of Legacy Systems
> - There are three basic procedures for renewing legacy systems:
>   - Packing: a new software is designed as a shell that provides a modern interface to the
>     outside world, but communicates internally with the legacy software
>   - Migration: it is possible to renew software step by step
>     - To do this, you divide them into components and renew one component after the other
>   - Replacement in one fell swoop: You develop the software completely from scratch while still
>     using the old software during the development phase"

Unpacked:

| Procedure | What the deck says | The shape of the old/new overlap |
|---|---|---|
| Packing | A new software is designed as a shell providing a modern interface to the outside world, communicating internally with the legacy software | Permanent: the shell stays in front of the legacy core |
| Migration | Renewal step by step: divide the system into components and renew one after the other | Shrinking: each migrated component reduces the legacy surface |
| Replacement in one fell swoop | Develop the software completely from scratch while still using the old software during the development phase | Temporary and total: the old system is used for the whole development phase |

The slide says "three basic procedures" with no "for example" and no "among others", so the list is
presented as exhaustive within the lecture's frame. The definitions are behavioural: each says what
is built, what the old system does during the work, and how the two communicate.

The surrounding definitions that give the procedures their setting come from the same deck:
restructuring is a "transformation of a system from one form into another" where "the new form of
the system has the same semantics and the same external behavior as the old form", and refactoring
is the part of restructuring that improves the internal structure of code while accurately
maintaining external behaviour, divided into code refactoring and architecture refactoring.

## Key Properties

- **The list is exhaustive as presented.** Three procedures, stated as the basic ones, with no
  variants and no hybrids.
- **Each keeps the legacy system in use.** Packing keeps it behind the shell permanently;
  migration keeps it until each component has been renewed; replacement keeps it for the whole
  development phase.
- **Packing puts a boundary at the outside.** The new software is a shell with a modern interface
  to the outside world, and the legacy software is reached only through internal communication.
  The outside world is insulated; the internals are not modernised.
- **Migration decomposes.** The stated mechanism is division into components plus renewal of one
  component after the other. The phrase "step by step" is the definition.
- **Replacement in one fell swoop is a from-scratch development.** The new software is developed
  completely from scratch, and the old software is used during the development phase.
- **Renewal is a reengineering activity at system scale.** The analysis techniques of the lecture
  — control-flow recovery, slicing, post-documentation — are what make components identifiable.
- **Renewing a component is a refactoring job.** Once a component is picked out, the work on it
  falls under restructuring and refactoring, including behaviour preservation and regression
  testing.
- **The three are not distinguished by the deck.** The slide gives no ranking, no selection rule,
  no cost, effort or risk information.

## Worked Example

The lecture's running fragment is the clamp routine:

```c
read (x);
a = 0;
if (x > max) {
    x=max;
    a=1;
}
else if (x < min) {
    x=min;
    a=1;
}
print (x);
print (a);
```

It is small enough that the three procedures can be applied to it concretely, and the deck's own
definitions are precise enough to make the application unambiguous.

**Packing.** Take the fragment as it is, and write a new component that presents a modern
interface to the outside world — say, a function returning a structured result rather than
printing to a console — while communicating internally with the legacy code. The legacy routine
still does the clamping and still prints, but the outside world no longer talks to it directly.
The legacy behaviour is preserved exactly, because the legacy code is untouched. Packing does not
require knowing what the legacy code does internally, only how to talk to it.

**Migration.** Divide the system into components and renew them one after another. The fragment
is a natural candidate for one component: the clamping behaviour, which the deck's
reverse-engineering slides recover as a basic-block structure with three paths (above `max`,
below `min`, inside the range). Renewing it means reimplementing it — same semantics, same
external behaviour — in a form that returns the clamped value and the flag instead of printing.
Migration is possible only because the analysis steps could isolate the component: this is where
the lecture's slicing and control-flow work pays off, since a slicing criterion on the printing of
`x` shows which statements the component consists of.

**Replacement in one fell swoop.** Develop the software completely from scratch while still using
the old software during the development phase. The new implementation is built alongside the old
one, which serves the business meanwhile, and the switch happens once the new one is ready.

*Constructed illustration, marked as such:* the deck applies none of the three procedures to this
fragment, and it gives no component decomposition, no interface definition and no cut-over
procedure for any system. The applications above are readings of the deck's three one-line
definitions against the lecture's own example, marked as constructed because they contain
material the slides do not state.

## Common Pitfalls

- **Treating the three procedures as ordered by cost or risk.** The slide ranks nothing, so any
  claim that packing is cheaper, migration safer or replacement riskiest is not supported by the
  source.
- **Confusing packing with migration.** Packing renews nothing: the legacy software remains the
  implementation and the new software is only a shell around it. Migration replaces components
  one by one.
- **Assuming packing removes the legacy system.** The shell's modern interface is on the outside;
  internally it still communicates with the legacy software. The deck does not describe an
  end-state for packing.
- **Reading "replacement in one fell swoop" as "replace without the old system".** The deck says
  the old software is still used during the development phase. The "one fell swoop" refers to the
  switchover, not to an absence of overlap.
- **Assuming the components for migration are given.** The deck says you divide the system into
  components and renew one after the other, but gives no criterion for the division, no ordering
  of components, and no statement about what makes a component a safe unit of renewal.
- **Ignoring that renewing a component is still subject to behaviour preservation.** Restructuring
  requires the same semantics and external behaviour, and refactoring requires accurate maintenance
  of external behaviour plus regression testing. A renewal that quietly changes what the legacy
  component does is not a renewal in the lecture's terms.
- **Expecting a fourth procedure.** The slide says "three basic procedures"; other strategies in
  the wider literature are not in this deck.
- **Reading the renewal slide as a plan.** It is a slide of three definitions, with no process, no
  phases and no organisational guidance.

## Connections

- [[legacy-systems]] — the problems these three procedures answer; the renewal slide follows the
  legacy-systems slide directly.
- [[reengineering]] — the process diagram whose restructuring and forward-engineering stages the
  renewal procedures operationalise at system scale.
- [[refactoring-and-code-smells]] — the work that renewing an individual component consists of.
- [[architecture-smell]] — the architecture-level problems that a shell can hide but not remove.
- [[software-aging]] — the degradation whose remediation these three procedures are.
- [[reverse-engineering]] — the analysis that makes component division possible.
- [[program-slicing]] — the technique that isolates the statements belonging to one component.
- [[control-flow-graph]] — the recovered behaviour of a legacy component, which a renewal must
  preserve.
- [[reengineering-vs-maintenance]] — renewal serves the developer by reconstituting the system;
  maintenance serves the customer by adapting it.

## Open Questions

- **The three procedures are not compared.** The slide gives no cost, effort, risk or duration
  figures, and no statement of when each is appropriate.
- **"Components" is undefined for migration, and no selection criteria are given.** The deck says
  to divide the system into components and renew one after another, but gives no criterion for the
  split and no ordering rule; nothing connects the properties of the legacy system to a choice
  among the three procedures.
- **The end states are unspecified.** The deck describes a shell that communicates internally with
  the legacy software but not whether the legacy software is eventually replaced; and for a
  from-scratch replacement it says the old software is used during the development phase, but not
  how the two systems are reconciled when the new one takes over.
- **No worked instance of any procedure is given.** The deck supplies three definitions and no
  example, so nothing in the source shows a legacy system being packed, migrated or replaced.
