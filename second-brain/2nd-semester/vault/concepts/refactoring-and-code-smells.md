---
title: "Refactoring and Code Smells"
tags: [concept, reverse-and-reengineering, semester-2, refactoring, code-smells]
course: "Reverse- and Reengineering"
source_count: 1
status: current
last_updated: 2026-10-22
prerequisites: ["[[reengineering]]"]
---

## One-line Summary
Refactoring is the restructuring of a program's inner shape while keeping its outer behaviour
exactly the same, and a code smell is the observable symptom that says the inner shape needs
that treatment.

## Core Intuition

The lecture slides state the whole idea in three lines: refactoring is part of the restructuring
process; it improves the internal structure of code while accurately maintaining the external
behaviour of the program; and it requires intensive testing of the refactorized program to avoid
errors due to refactoring — regression testing.

The word that carries the concept is **"internal"**. Everything a user of the program can observe
— outputs, side effects, the ordering of effects — must survive the change untouched. What may
change is everything nobody can observe: how the work is partitioned into methods, how the data
is shaped, how deep the conditionals nest. Since the semantics are supposed to be invariant, any
behaviour change is a defect introduced by the refactoring, not by the program.

That is why the slides make testing **intensive** and name the consequence directly: regression
testing. If the behaviour is meant to be untouched, the test suite is the only instrument that
can tell you whether it was in fact untouched.

The second idea on the slides is the division of refactoring into two parts: **code refactoring**
and **architecture refactoring**. The split is by level of intervention, not by technique. Code
refactoring works inside the existing design — improving methods, reorganising data, splitting
conditionals. Architecture refactoring changes the structure of the software architecture itself,
including, as the slides put it, the extreme case of changing the software architecture. Each
level has its own smell vocabulary and its own remedy: a code smell requires code refactoring,
an architecture smell requires architecture refactoring.

The third idea is the smell itself. The slides define a code smell as poor quality or poorly
structured program code, and list what they consider typical: unused functionality; too much or
too little functionality in a method or class; code duplicates; a parameter list too long; message
chains too long; and too many levels of nesting, with nested if-statements as the example. A smell
is not a bug — the program still runs — but it is a structured warning that the code will be
expensive to change later, which under the lecture's software-aging story is exactly how a system
becomes hard to maintain.


## Formal Definition / Statement

Restructuring, from the same deck, is the enclosing notion:

> "Restructuring:
> - Transformation of a system from one form into another
> - The new form of the system has the same semantics and the same external behavior as the old
>   form"

Refactoring is stated as a component of that:

> "Refactoring
> - Refactoring is part of the restructuring process
> - Improve the internal structure of code while accurately maintaining the external behavior of
>   the program
> - Intensive testing of the refactorized program to avoid errors due to Refactoring (→ regression
>   testing)
> - Refactoring is divided into two parts: code refactoring, architecture refactoring"

And the smell:

> "'Code smell' describes poor quality or poorly structured program code"

The catalogue the slides give for code smells:

| Smell | What the slides point at |
|---|---|
| Unused functionality | Code that is never needed by anything |
| Too much or too little functionality in a method or class | Wrong-sized units of decomposition |
| Code duplicates | The same logic written more than once |
| Parameter list too long | A method that wants too many inputs |
| Message chains too long | Long traversals of object relationships |
| Too many levels of nesting (e.g. nested if-statements) | Deeply indented control flow |

The closing line of that slide is the rule that ties smell to remedy: **"Code smell requires code
refactoring."** Note what the slide does *not* say: it does not say a code smell requires
*architecture* refactoring. That is the subject of the companion page [[architecture-smell]].

Two further anchors come from the deck's front matter. The course content list names "Automatic
refactoring to improve program structure" as one of the things the semester covers, and the
references slide lists "Refactoring: Improving the Design of Existing Code" by Martin Fowler.
Neither slide develops them further; they mark refactoring as a named course topic with a
standard literature behind it.

## Key Properties

- **Behaviour preservation is the invariant.** The defining constraint of refactoring is that the
  external behaviour of the program is accurately maintained. Structure changes; semantics do not.
- **Refactoring is a part of restructuring, not the whole of it.** Restructuring is the broader
  transformation "from one form into another" with the same semantics and the same external
  behaviour; refactoring is the code-shaped part of it. The reengineering process on the slides
  has restructuring as its middle stage, and refactoring sits inside that stage.
- **Two levels, not one.** Refactoring divides into code refactoring and architecture refactoring.
  The two are treated differently: architecture refactoring "cannot be automated and requires human
  expert knowledge", whereas code refactoring is the level at which the concrete named methods
  live.
- **Testing is mandatory, not optional.** The slides demand intensive testing of the refactorized
  program, and name the technique: regression testing. This is a property of refactoring as a
  method, not advice bolted on afterwards.
- **Smells are catalogue items with a prescribed cure.** The pairing "code smell → code
  refactoring" is one-directional in the deck.
- **Smells are structural, not functional.** Unused functionality and code duplicates are both
  invisible in the program's output.
- **The smell list is not exhaustive.** The slides say "typical examples", so the six items are a
  sample of a category, not a closed definition.
- **Refactoring presupposes a program whose behaviour is known.** Behaviour must be pinned down
  before it can be preserved. For legacy code where nobody knows what the program should do, this
  is the gap the reverse-engineering half of the reengineering process exists to close — see
  [[reengineering]].

## Worked Example

The lecture's running fragment is a small piece of legacy C, and it happens to exhibit two of the
listed smells at once:

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

**The smells.** The two branches carry the *same* assignment `a=1;` — that is **code duplicates**.
The program decides between "above the ceiling" and "below the floor" through a chain of
conditionals on the same variable, the shape the slide flags as **too many levels of nesting (e.g.
nested if-statements)**. Whether the clamping logic counts as "too much or too little
functionality in a method" depends on the enclosing method, which the fragment does not show.

**The refactoring.** The slide's third named code-refactoring method — *splitting of complex
conditional expressions* — applies here, and *restructuring of the data organization* (combining
several primitive variables into a common object) applies to the pair `x` and `a`, which travel
together as "the value and whether it was clamped". A shape that preserves external behaviour
would compute the clamped value and derive the flag from the comparison result rather than
duplicating the assignment in each branch.

**The check.** Because behaviour must be preserved, the refactored fragment is put through
intensive testing: for `x` above `max`, `x` must come out as `max` and `a` as `1`; below `min`,
`x` must come out as `min` and `a` as `1`; inside the range, `x` unchanged and `a` as `0`. Those
are the three leaves of the lecture's intraprocedural control-flow graph for this fragment. Every
path through the original must produce the same output as the corresponding path through the
refactoring.

*Constructed illustration:* the lecture does not print a refactored version of this fragment; the
clamped-value-and-derived-flag shape above is a reconstruction from the listed refactoring
methods, and the three test cases are derived from the lecture's own CFG for this fragment rather
than from any test file shown in the deck.

## Common Pitfalls

- **Treating refactoring as feature work.** Any change that alters observable behaviour is not
  refactoring, whatever else it is called. The slides' wording is "accurately maintaining the
  external behavior of the program".
- **Skipping the regression test because "the change was small".** Behaviour preservation is a
  claim about the artefact, not about the programmer's intent, and small changes are exactly where
  unnoticed behaviour changes live.
- **Confusing the two levels of refactoring.** A method-level cleanup cannot fix a cyclic class
  dependency, and an inheritance-hierarchy change is more than tidying.
- **Fixing a code smell with architecture refactoring, or the reverse.** The deck's rule is
  direct: code smell requires code refactoring, architecture smell requires architecture
  refactoring.
- **Reading "unused functionality" as "delete it".** The slide lists it as a smell; it does not
  specify the remedy or authorise removal. In a legacy system the unused-looking code may encode
  behaviour nobody currently calls but that the business depends on elsewhere.
- **Treating the smell catalogue as a checklist to clear mechanically.** The slides give six
  typical examples and a set of methods; no rule says when a smell is worth touching.
- **Assuming the semantics are already pinned down.** Refactoring preserves semantics it knows
  about. On code whose behaviour was never specified, "preserving" it means deciding what it is
  first — the reverse-engineering half of the loop.
- **Overlooking the middle of the reengineering process.** Refactoring is a part of
  restructuring, which is a part of reengineering. Refactoring alone yields better-shaped code,
  not a reconstituted system in a new form.

## Connections

- [[reengineering]] — refactoring is the code-level part of the restructuring stage of the
  reengineering loop.
- [[architecture-smell]] — the level above this one, with its own remedy (architecture
  refactoring) and its own automation constraint.
- [[software-aging]] — why the smell catalogue matters: quality erodes as requirements drift onto
  an architecture that never fitted them.
- [[reengineering-vs-maintenance]] — refactoring serves the developer, maintenance the customer.
- [[control-flow-graph]] — the regression test for the lecture's fragment has one case per branch
  of its intraprocedural CFG.
- [[program-dependence-graph]] — the two `a=1` assignments are equivalent with respect to `a`,
  which is what makes them duplicates.
- [[program-slicing]] — isolates the statements that matter for one question, shrinking the blast
  radius of a refactoring.
- [[basic-block]] — the unit the lecture splits the fragment into before analysing it.
- [[reverse-engineering]] — recovers the behaviour a refactoring must preserve.

## Open Questions

- **The catalogue and the decision procedure are both missing.** "Code smell" is defined as poor
  quality or poorly structured code, and the six items are introduced as typical examples, so
  whether the list is exhaustive is not stated. The deck also gives no severity rule, no cost
  model, and no statement about whether every smell should be removed.
- **The boundary of "external behaviour" is undefined.** The slides do not say whether
  performance, memory footprint or error messages count as external behaviour — which matters for
  a legacy system where performance degradation is a listed symptom of aging.
- **The relation between the two refactoring levels is not specified.** The deck does not say how
  to decide which level a given smell lives at.
- **No test strategy is given.** Regression testing is named as necessary and "intensive", but the
  deck does not say how to construct tests for a legacy system whose behaviour was never
  specified.
