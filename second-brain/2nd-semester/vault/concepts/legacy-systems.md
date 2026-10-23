---
title: "Legacy Systems"
tags: [concept, reverse-and-reengineering, semester-2, legacy-systems, software-aging]
course: "Reverse- and Reengineering"
source_count: 1
status: current
last_updated: 2026-10-22
prerequisites: ["[[reengineering]]", "[[software-aging]]"]
---

## One-line Summary
A legacy system is an old, poorly documented, often enormous piece of software whose handling and
architecture nobody at the company understands any more — and which nonetheless performs critical
tasks for the business.

## Core Intuition

The lecture gives legacy systems their own slide, and the order of the items on it is the
argument. The properties are:

- legacy systems use obsolete programming languages, platforms and operating systems;
- they are often poorly documented;
- they are often very large code bases;
- there is a lack of knowledge among the company's employees about handling and architecture of the
  legacy system.

Then the slide adds the line that makes the whole topic urgent: **nevertheless, legacy systems
oftentimes perform critical tasks in a company.**

That last line is the pivot of the slide. Each property alone would be survivable — old
technology is old technology, missing documentation is a nuisance, a large code base is a large
code base. What makes a legacy system hard is the combination, and the combination becomes lethal
precisely because the system is still *load-bearing*. You cannot switch it off, and you cannot
rebuild it without understanding it, and understanding it is exactly what the missing documentation
and the lost knowledge make hard.

This is where the lecture's other pieces line up. The slide on the problems of reverse
engineering says the compilation process loses information such as method and attribute names, so
interpretation and expert knowledge become necessary during analysis; that static analysis cannot
always state whether code is actually executed in practice; and that the process can only be
partially automated due to the analyst's own high level of effort. The legacy system is that
general case in concentrated form, because it adds the two missing pieces: no documentation and no
internal knowledge.

The course's learning objectives name the topic explicitly — "Explain the challenges of legacy
systems and how they can be renewed" — which is why the deck closes the legacy-system slides with
the three renewal procedures on [[legacy-system-renewal]]. Legacy systems are the input to the
reengineering process; the three renewal strategies are the answer to their properties.

The deck handles the technical flavour of "legacy" once, on a slide of its own: a reference to a
Medium article, "7 COBOL examples with explanations", is shown as the source for the example
code. That slide is a pointer to external reading material, not a claim about the lecture's
content, and nothing on this page draws on the article's contents.

## Formal Definition / Statement

The slide's statement, verbatim:

> "Legacy Systems
> - Properties of legacy systems:
>   - Legacy systems use obsolete programming languages, platforms and operating systems
>   - Often poorly documented
>   - Often very large code base
>   - Lack of knowledge of the employees in the company about handling and architecture of legacy
>     system
> - Nevertheless, legacy systems oftentimes perform critical tasks in a company"

(The first bullet is paraphrased from the slide's original wording.)

Note what the slide does **not** contain: there is no formal definition of "legacy system" on it.
The term is characterised by a list of properties, stated with hedges — "often" for documentation
and code-base size, "oftentimes" for critical tasks. Even the obsolete-technology property is a
property rather than a threshold, and the deck never says when a system counts as legacy.

The supporting material from elsewhere in the same deck frames the same phenomenon:

> "Software Aging
> - Software requirements change over time
> - Software is adapted to new requirements after release
> - Adding functionality that is inappropriate to the architecture of the software"

> "Loss of Software Quality
> - The quality of software decreases with time (software aging):
>   - Software becomes more error-prone
>   - Loss of performance
>   - Deterioration of maintainability
>   - General deterioration of the architecture"

So a legacy system, on the lecture's reading, is one that has been through the aging process long
enough for the properties on the legacy-systems slide to have accumulated: obsolete technology
stack, missing documentation, large code base, lost organisational knowledge.

## Key Properties

- **Obsolete technology stack.** The languages, platforms and operating systems in use are
  obsolete. The deck does not list which ones it means.
- **Documentation is typically absent.** The slide says "often poorly documented" — what exists may
  be inadequate rather than missing entirely.
- **The code base is typically very large.** Stated as "often very large code base", with no
  number.
- **Organisational knowledge has been lost.** Employees lack knowledge of the handling and
  architecture of the legacy system. This is a property of the company, not of the code.
- **The system is business-critical.** "Nevertheless, legacy systems oftentimes perform critical
  tasks in a company." This is stated as an overriding fact about legacy systems, and it is what
  removes "rewrite it" as an easy option.
- **The combination is the difficulty.** No single property on the slide is fatal; the interaction
  of missing documentation, lost knowledge and criticality is what makes these systems hard to
  renew.
- **It is the input to the reengineering process.** The deck's process diagram starts from "Program
  Code in poor Quality"; the legacy-system slide is the practical statement of what that means.
- **The renewal options are three.** Packing, migration, and replacement in one fell swoop — see
  [[legacy-system-renewal]].
- **It ties into the course's stated learning objectives.** "Explain the challenges of legacy
  systems and how they can be renewed" appears alongside "Understand the concepts of Software
  Aging, Reengineering, Refactoring, Code Smells".

## Worked Example

The lecture's running fragment is the clearest piece of legacy code in the deck:

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

Seen through the legacy-systems slide, this fragment carries three of the four properties at once,
and it is worth reading them off explicitly because the deck does not make the connection itself:

**Obsolete stack and old style.** The code is plain C-like source with `read`/`print` as external
calls, no modular structure, no error handling, and names that give no hint of intent beyond `x`,
`a`, `min` and `max`.

**Poorly documented.** The fragment has no names that describe what it does. `a` is a flag
signalling whether the value was clamped, but nothing in the code says so. The documentation gap
is not the absence of a file; it is the absence of any hint of intent inside the artefact.

**Lost knowledge.** The behaviour of the fragment has to be recovered by reading it — the work the
deck's reverse-engineering slides describe, splitting it into basic blocks B1 to B5 and drawing
the intraprocedural control-flow graph — because nobody is available to explain it.

**Business-critical.** The fragment is the kind of small, dependable piece of logic that companies
depend on and nobody wants to touch: it reads an input, clamps it into `[min, max]`, and reports
both the clamped value and whether clamping happened. That is the pattern behind the slide's line
that legacy systems "oftentimes perform critical tasks in a company".

*Constructed illustration:* the deck does not present this fragment as a legacy system, and does
not attach the four legacy properties to it; the reading above applies the slide's properties to
the lecture's own code fragment. The deck's own legacy example is the COBOL reference slide
pointing at "7 COBOL examples with explanations" on Medium, presented purely as a source pointer.

## Common Pitfalls

- **Treating "legacy" as a synonym for "old".** The slide's properties are about documentation,
  size, lost knowledge and obsolete technology *in combination*. A ten-year-old system that is
  well documented, moderately sized and understood by the team does not exhibit that profile.
- **Reading "often" and "oftentimes" as "always".** The hedges are the professor's, and the deck
  gives no rule for when a property is present.
- **Assuming the documentation gap can be filled by reading the code alone.** The deck notes the
  loss of information during compilation, the need for expert knowledge, and that the process
  "can only be partially automated due to the analyst's own high level of effort". Where
  organisational knowledge is also gone, analysis alone does not close the gap.
- **Treating criticality as an argument against renewal.** The slide's "nevertheless" clause is
  about why renewal is hard, not why it is unnecessary. The whole point of the renewal slide that
  follows is to act on such a system.
- **Confusing legacy with maintenance.** Maintenance is adaptation of the software according to the
  customer's wishes; reengineering serves the developer. A legacy system patched for a new
  customer requirement is being maintained, not reengineered; see [[reengineering-vs-maintenance]].
- **Expecting the deck to define the term.** There is no formal definition on these slides, only a
  property list. Any threshold — age, size, technology — would be an addition.
- **Reusing the COBOL article as lecture content.** The article is a pointer on one slide. The
  deck does not summarise or quote it.
- **Assuming the size claim has a number attached.** "Often very large code base" is the whole of
  the statement; there is no figure for lines of code, developers or modules anywhere in the deck.

## Connections

- [[reengineering]] — the process a legacy system is normally put through; the deck's diagram
  starts from "Program Code in poor Quality".
- [[software-aging]] — the mechanism behind the property list: quality erodes as requirements
  drift onto an architecture that never fitted them.
- [[legacy-system-renewal]] — the deck's answer to this slide: packing, migration, replacement.
- [[reverse-engineering]] — the step that recovers what the missing documentation does not say.
- [[refactoring-and-code-smells]] — the code-level clean-up inside a legacy system, which the
  deck separates from architecture-level work.
- [[architecture-smell]] — the architecture-level defects that accumulate in a long-lived system.
- [[reengineering-vs-maintenance]] — customer-facing patching versus developer-facing
  reconstitution.
- [[control-flow-graph]] — the recovery of the lecture's fragment.
- [[program-slicing]] — making a large legacy code base tractable by cutting it down to the
  statements that matter for one question.

## Open Questions

- **There is no definition of "legacy system".** The slide gives four properties and no criterion
  for membership. Nothing in the deck says whether legacy is a property of age, technology,
  documentation, size, or organisational knowledge, or how many of the four must hold.
- **The scale and the criticality are both left unquantified.** "Often very large code base" is
  the only size statement — no number of lines, modules, developers or years — and the slide says
  legacy systems "oftentimes perform critical tasks in a company" without saying what makes a task
  critical.
- **The interaction between the four properties is not discussed.** The deck does not say which
  combinations are typical, or whether the properties feed each other.
- **No criteria for choosing a renewal strategy are given.** The deck moves directly from the
  legacy-system properties to the three renewal procedures without saying how the properties
  should influence the choice between them.
