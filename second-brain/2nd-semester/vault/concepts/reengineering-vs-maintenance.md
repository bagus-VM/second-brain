---
title: "Reengineering vs. Maintenance"
tags: [concept, reverse-and-reengineering, semester-2, maintenance, reengineering]
course: "Reverse- and Reengineering"
source_count: 1
status: current
last_updated: 2026-10-22
prerequisites: ["[[reengineering]]", "[[software-aging]]"]
---

## One-line Summary
Maintenance adapts the software to the customer's wishes; reengineering reconstitutes the system
so the developer can work on it again — the same activity seen from two different beneficiaries.

## Core Intuition

The lecture gives this comparison its own slide (slide 48) and also lists it in the learning
objectives on slide 6: "Explain the difference between Maintenance and Reengineering". A single
slide, and yet the distinction it draws is the one that determines what a project actually does.

The definitions, as stated on the slide, attributed to *Ludewig 585 Introduction*:

> **Maintenance**: adaptation of the software according to the customer's wishes — enhancement of
> the software, software correction, change of specifications.
>
> **Reengineering**: serves the developer.
> **Maintenance**: serves the customer.

The slide is laid out as a comparison table with "Serves the developer" and "Serves the
customer" as the two cells that carry the distinction. Read carefully, that is not a claim that
maintenance is bad and reengineering good. It is a claim about *whose need is being served*,
and therefore about *which of two different sets of requirements the change is measured
against*.

A maintenance change is successful when the customer gets what they asked for. The question
"but did this make the code worse to work with?" is not part of the acceptance criterion.
A reengineering change is successful when the system's internal form is fit to be maintained
again — and the slide's own comparison table is the criterion: the developer is the beneficiary.
Reengineering as Chikofsky/Cross define it on slide 8 requires reconstituting the system in a
new form, which is a statement about the artefact, not about a customer's request.

The intuition that ties them together is the aging story (see [[software-aging]]). Software ages
because requirements change and because features get added in ways that do not fit the
architecture. Maintenance is the mechanism by which requirements keep changing; reengineering is
the mechanism by which the accumulated damage is paid back. A team that only does maintenance
keeps serving the customer and never repairs the asset; a team that only does reengineering
improves the asset nobody asked to change.

## Formal Definition / Statement

**Maintenance** (lecture 1, slide 48), verbatim structure:

```
Maintenance: Adaptation of the software according to the customer's wishes
  - Enhancement of the software
  - Software correction
  - Change of specifications
```

Note that all three sub-items are phrased from the customer's point of view: the customer wants
more features, the customer reports a defect, the customer changes what the system is supposed
to do. None of the three is phrased in terms of the system's internal structure.

**Reengineering** (lecture 1, slide 8, Chikofsky & Cross 1990), quoted in the exemplar page
[[reengineering]]:

> "Reengineering, also known as both renovation and reclamation, is the examination and
> alteration of a subject system to reconstitute it in a new form and the subsequent
> implementation of the new form."

And the slide's two-column table:

```
                        Serves the developer
Reengineering: VS Maintenance:
                        Serves the customer
```

**The process diagram that separates them in practice** (lecture 1, slides 12, 38, 45) draws
three rows, and the distinction shows up in what each row consumes and produces:

```
Reverse Engineering   ->   Program Code in poor Quality
Restructuring         ->   Rediscovered Requirements and Design
Forward Engineering   ->   Improved Requirements and Design
                     ->   Improved Code
```

Maintenance occupies no row of that diagram. That absence is the point: the reengineering loop
is a different activity with a different output, not a superset of maintenance's output.

## Key Properties

- **The beneficiaries differ, and that is the definitional difference.** Developer versus
  customer.
- **Maintenance is defined by its trigger** — "adaptation ... according to the customer's
  wishes" — so any change that was not requested is, by the slide's definition, not
  maintenance.
- **Maintenance comes in three flavours**: enhancement, software correction, change of
  specifications.
- **Reengineering requires alteration.** It is "the examination and alteration of a subject
  system" plus "the subsequent implementation of the new form" — understanding alone is not
  reengineering.
- **Both are fed by the same aging process.** The lecture's content list puts software aging
  first and the comparison slide sits at the end of the reengineering half of the lecture.
- **Reengineering is a loop, not a one-off project.** Improved code becomes the next subject
  system.
- **The distinction is behavioural, not organisational.** A team can do both; the slide
  classifies the *intent of the change*, not the team or the phase.
- **Restructuring preserves behaviour.** Slide 39: the new form of the system has the same
  semantics and the same external behaviour as the old form. That is what makes reengineering
  safe to attempt on a system whose specification is gone — the spec is replaced by the
  behaviour itself. Refactoring (slide 40) is part of restructuring and maintains external
  behaviour, which is why regression testing is mandatory there; see
  [[refactoring-and-code-smells]].
- **Architecture refactoring needs human expert knowledge** (slide 44): it cannot be automated.
  So the developer-facing half of the work is not a tooling exercise.

## Worked Example

The lecture's running legacy fragment (slide 17) is small enough to run both activities against
it.

```c
read (x);
a = 0;
if (x > max) { x=max; a=1; }
else if (x < min) { x=min; a=1; }
print (x);
print (a);
```

*Constructed illustration — the fragment is source material from lecture 1; the two readings below
apply the slide-48 definitions to it and are my analysis, not a case worked on the slides.*

**As maintenance.** The customer reports that the system should now support a second, wider
range, `[min2, max2]`, and that the report should say which bound was hit. Under slide 48 this
is *enhancement* of the software and possibly a *change of specifications*, performed according
to the customer's wishes. The acceptance test is behavioural: the new range works, the report is
correct, the customer is satisfied. Whether the result is a third nested branch or a cleaner
clamp helper is not part of the maintenance criterion — it is not what the customer measures.

**As reengineering.** The developer observes that the same fragment has an if/else-if chain on
one variable, duplicated `a=1` assignments, and a nesting level that will make the next
enhancement worse. The reengineering activity is: reverse engineer the fragment (recover the
CFG and the PDG), restructure it while preserving semantics and external behaviour, then
forward-engineer the improved form. The acceptance test is a developer-side one — the new form
is easier to change, and the behaviour is provably unchanged, so the "improved code" can
replace the old code without the customer noticing.

**The same change, twice.** A request to add a third bound can be executed as maintenance
(append a branch, ship it) or as reengineering (first restructure into a clamp abstraction,
then add the third bound as a parameter). The deliverable is a different system in the second
case, even though the customer's request is identical. That is the sharpest form of the
distinction: the request is the same, the beneficiary decides the work.

## Common Pitfalls

- **Reading the comparison as "maintenance is the lesser activity".** The slide classifies
  beneficiaries; it does not rank. Maintenance is what the customer pays for, and for a
  business-critical system it is the activity that keeps the business running.
- **Thinking reengineering replaces maintenance.** The reengineering loop ends in improved code,
  and improved code ages and then needs maintenance again.
- **Collapsing "serves the developer" into "serves the company".** The slide's phrasing is
  about the beneficiary of the change: the developer who must work on the system, versus the
  customer who wants a change in behaviour.
- **Confusing reverse engineering with reengineering and thereby losing the distinction.**
  Reverse engineering produces understanding; reengineering additionally alters and reimplements;
  maintenance alters to serve a customer. Three different activities.
- **Assuming maintenance implies no structural discipline.** The slide's definition does not
  forbid clean code; it defines the *purpose*. A maintenance change can be implemented well.
  What it does not do by definition is reconstitute the system in a new form.
- **Reading "serves the developer" as "no customer benefit".** The reengineering loop ends in
  improved code, which the customer then receives as better-maintained behaviour.
- **Expecting reengineering to be automatable.** Architecture refactoring "cannot be automated
  and requires human expert knowledge" (slide 44), which is precisely why the reengineering
  side is the harder half.

## Connections

- [[reengineering]] — the process page; this page is the sharp comparison, and the two are kept
  consistent but non-duplicative.
- [[software-aging]] — the degradation that both activities exist in response to.
- [[reverse-engineering]] — the first step of the reengineering loop, and a service that
  maintenance also draws on.
- [[refactoring-and-code-smells]] — the code-level part of restructuring, and the tooling that
  serves the developer side.
- [[architecture-smell]] — the architecture-level counterpart, which needs the human judgement
  reengineering depends on.
- [[legacy-systems]] — the systems in practice most in need of both activities.
- [[legacy-system-renewal]] — packing, migration and replacement as the three ways to renew an
  aged system once the reengineering decision is taken.
- [[binary-reverse-engineering]] — the case where even the examination step is hard, because the
  subject system is only available as machine code.
- [[reverse-and-reengineering-lecture-1]] — the lecture in which the comparison slide appears.

## Open Questions

- **What decides which activity a given request gets, and is the boundary one of scope,
  authorization, or intent?** The slide states the two definitions and their beneficiaries but
  gives no rule for choosing between them when a customer's request happens to expose an
  architectural problem. A change can be both customer-requested and reconstituting; the source
  does not say which label wins.
- **How is the cost of maintenance compared with the cost of reengineering?** The slide
  contains no cost, effort, or risk data, and no threshold at which reengineering becomes
  cheaper than continued maintenance.
- **Is "change of specifications" always a maintenance activity, and is the two-way
  comparison ever run?** It appears as the third sub-item of maintenance, but a specification
  change is also the point at which a reengineering project's recovered requirements get
  replaced by new ones. And the lecture gives the definitions side by side and the
  reengineering loop separately, but never runs the same change through both.
