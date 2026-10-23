---
title: "Architecture Smell"
tags: [concept, reverse-and-reengineering, semester-2, architecture-smell, refactoring]
course: "Reverse- and Reengineering"
source_count: 1
status: current
last_updated: 2026-10-22
prerequisites: ["[[reengineering]]", "[[refactoring-and-code-smells]]"]
---

## One-line Summary
An architecture smell is a structural weakness at the level of the software architecture itself,
and its remedy is architecture refactoring — the one refactoring activity the lecture says cannot
be automated.

## Core Intuition

The lecture draws a clean two-level picture. Refactoring splits into **code refactoring** and
**architecture refactoring**. Each level has its own smell vocabulary and its own prescribed
cure. A code smell — poor quality or poorly structured program
code, such as duplicates or too many levels of nesting — requires code refactoring. An
**architecture smell** "describes vulnerabilities at the software architecture level", and the
slide closes with the parallel rule: **architecture smell requires architecture refactoring**.

The word doing the work in that definition is **"vulnerabilities"**. A code smell is a local
blemish: a method is too long, a list of parameters too long, two blocks of code saying the same
thing. An architecture smell is a weakness in the *arrangement* of the system: classes that depend
on each other in a circle, a hierarchy that has forked into parallel branches, a package that has
grown into something no longer one thing. Local refactoring cannot remove these, because the
defect is in the arrangement itself. That is why the deck gives each level its own remedy rather
than one generic clean-up.

The second thing the slides make explicit is the limit of automation. Architecture refactoring
"cannot be automated and requires human expert knowledge". This contrasts with the rest of the
lecture, which is built around semi-automatic analysis: control-flow graphs recovered by tools,
program dependence graphs computed by algorithms, slicing performed by slice algorithms. Those
tools operate on *code*. Judging whether a class hierarchy should be flattened, or two packages
merged, is a design decision, and the deck locates it with the human expert.

The third thread is the relation to the reengineering loop. Architecture refactoring belongs to
the middle stage of the process — restructuring, where the rediscovered requirements and design
become an improved form, followed by forward engineering into improved code. The deck's slide on
architectural rediscovery states that deriving software architecture from existing program code
"requires knowledge of software architectures and programming language used as well as successful
post-documentation". Architecture is thus the layer where reverse engineering, post-documentation
and restructuring meet, and where judgement cannot be replaced by an algorithm.

Restructuring itself is the frame that holds all of this: a transformation of a system from one
form into another, where the new form has the same semantics and the same external behaviour as
the old form. Architecture refactoring is the architecture-level half of that transformation.

## Formal Definition / Statement

The slide's definition and its rule, verbatim:

> "'Architecture smell' describes vulnerabilities at the software architecture level
> - Typical examples for 'Architecture smell':
>   - Cyclic use of classes or unused classes
>   - Parallel or too deep inheritance hierarchies
>   - Packages or components too large or too small
>   - break through/violation of stratification
> Architecture smell requires architecture refactoring"

And the remedy slide:

> "Architecture Refactoring
> - Denotes improvement of structure of software architecture
> - Methods for code refactoring are e.g.:
>   - Change of inheritance hierarchy
>   - Split or merge of packages
>   - extreme case: change of software architecture
> - Architecture refactoring cannot be automated and requires human expert knowledge"

The catalogue, unpacked against the definition:

| Architecture smell | What it means for the structure |
|---|---|
| Cyclic use of classes or unused classes | The dependency graph has a cycle, or a component nothing depends on |
| Parallel or too deep inheritance hierarchies | The type structure has split into parallel branches, or grown layers too deep to follow |
| Packages or components too large or too small | The partition into units no longer matches what the units do |
| Break through / violation of stratification | A layer boundary has been crossed, or the layering rule is otherwise broken |

The enclosing definitions from the same deck:

> "Restructuring:
> - Transformation of a system from one form into another
> - The new form of the system has the same semantics and the same external behavior as the old
>   form"

> "Refactoring
> - Refactoring is part of the restructuring process
> - ... Refactoring is divided into two parts: code refactoring, architecture refactoring"

Note a slip in the source: the architecture-refactoring slide says "Methods for code refactoring
are e.g." where it means the methods for *architecture* refactoring. The listed items — change of
inheritance hierarchy, split or merge of packages, change of software architecture — are
architecture-level operations, as the slide's own heading says.

## Key Properties

- **It is a level, not a technique.** Architecture smell names the architectural tier of the
  quality problem. Code refactoring methods do not reach it.
- **The remedy is prescribed one-to-one.** "Code smell requires code refactoring" /
  "architecture smell requires architecture refactoring" — the pairing is the slide's own closing
  statement, not an inference.
- **It cannot be automated.** The deck states this without hedging: architecture refactoring
  "cannot be automated and requires human expert knowledge".
- **Its methods include the drastic.** The list runs from change of inheritance hierarchy, through
  split or merge of packages, to the "extreme case: change of software architecture".
- **Stratification is a first-class concern.** One of the four typical examples is a break
  through / violation of stratification, which puts layer boundaries on the same footing as
  class-level dependencies and package sizes.
- **It lives under the behaviour-preservation constraint.** Architecture refactoring is part of
  refactoring, part of restructuring, and restructuring keeps "the same semantics and the same
  external behavior". A new architecture with new behaviour is a rewrite, not a refactoring.
- **Architecture has to be recovered before it can be fixed.** The deck's architectural rediscovery
  slide says that deriving software architecture from existing program code requires knowledge of
  software architectures, of the programming language used, and successful post-documentation. An
  architecture smell you have not seen cannot be refactored.

## Worked Example

The lecture's running fragment is deliberately small:

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

Read against the architecture-smell catalogue, this fragment exhibits **none** of the four
architecture smells, and the deck does not claim it does. It is a single method with primitive
variables and no classes, no packages, no inheritance and no layers, so there is no architecture
here to smell. What it does exhibit is code-level material — the duplicated `a=1;` in both
branches and the if/else-if chain on the same variable — which is why the deck treats it as a
code-refactoring example. Keeping the levels apart on a concrete artefact is the fastest way to
remember which catalogue belongs to which remedy.

Where the architecture level *does* enter the lecture is one step earlier, in the slides on
post-documentation and architectural rediscovery. To reach an architecture-smell analysis of the
fragment's surrounding system, an analyst would first have to do what those slides describe:
present the existing code in a clearer form, extract higher-language constructs from archaic code
(loops, parameters, abstract data types), and derive the software architecture from that
post-documentation — which requires knowledge of software architectures and of the programming
language used.

*Constructed illustration:* the deck gives no architecture-smell example of its own. The following
illustrates the catalogue's first item — cyclic use of classes — and is not source material.
Suppose a class `Clamp` holding `x`, `min` and `max` calls a class `Report` to print the result,
and `Report` calls back into `Clamp` to fetch the value for formatting. Neither class can be
understood, tested or replaced on its own, because each needs the other to be complete. That is a
cyclic use of classes at the architecture level, and it is not a code smell: no individual method
is poorly written, so no amount of internal improvement of methods will remove it. The
corresponding architecture refactoring would change the dependency structure — a split or merge of
packages, or in the extreme case a change of the software architecture — exactly the kind of move
the deck says requires human expert knowledge and cannot be automated.

## Common Pitfalls

- **Applying code-refactoring methods to an architecture smell.** Improving the internals of
  methods does nothing about a cyclic dependency between classes.
- **Confusing a cycle between classes with a cycle in the control flow.** The lecture builds
  intraprocedural and interprocedural control-flow graphs and a call graph whose nodes are method
  names; a cyclic *class* dependency is a different object, at the architecture tier, and control
  flow appears in none of the deck's four architecture-smell items.
- **Treating "unused class" as trivially deletable.** The slide lists unused classes as an
  architecture smell but does not say what to do about them. In a legacy system an apparently
  unused class may be part of an architecture that documentation and organisational memory have
  lost track of.
- **Believing the extreme case is optional.** The method list runs to "extreme case: change of
  software architecture"; treating a full architecture change as out of scope because it is
  expensive inverts the deck's ordering.
- **Expecting a tool to do it.** A tool can show the dependency cycle or the package sizes;
  deciding what the architecture should become is the expert's part.
- **Losing the behaviour-preservation constraint.** Restructuring must keep the same semantics
  and external behaviour, and architecture refactoring is part of restructuring.
- **Skipping the rediscovery step.** The deck's architectural rediscovery slide puts
  post-documentation and knowledge of software architectures *before* architecture can be worked
  on. Fixing an architecture you have not recovered is guesswork.
- **Reading the "methods for code refactoring" wording literally.** It is a slip on the slide; the
  listed items are architecture-refactoring methods.

## Connections

- [[reengineering]] — architecture refactoring belongs to the restructuring stage of the
  reengineering process.
- [[refactoring-and-code-smells]] — the sibling level: code smells and code refactoring, with the
  same one-to-one pairing rule.
- [[software-aging]] — "general deterioration of the architecture" is a listed symptom of aging,
  and an architecture smell is a local instance of it.
- [[legacy-systems]] — large, undocumented legacy code bases are where architecture smells
  accumulate.
- [[legacy-system-renewal]] — packing, migration and replacement are the three routes by which a
  legacy architecture gets replaced or worked around.
- [[reverse-engineering]] — the step that recovers the architecture in the first place.
- [[software-analysis]] — the field whose tools recover the dependency and structure information
  an architecture analysis needs.
- [[interprocedural-analysis]] — the analysis between methods whose results feed the
  architectural view.

## Open Questions

- **"Stratification" is never defined.** One of the four typical examples is a "break
  through/violation of stratification", but the deck does not say what a stratified architecture
  is, what a violation looks like, or how it is detected.
- **"Parallel or too deep inheritance hierarchies" is not unpacked, and no detection method is
  given.** The deck does not say how many levels count as "too deep", how many branches count as
  "parallel", how an architecture smell is found in practice, or how it is measured.
- **The three architecture-refactoring methods are not related to each other.** Change of
  inheritance hierarchy, split or merge of packages, and change of software architecture are listed
  without saying when one applies rather than another, or whether they compose.
- **"Cannot be automated" is asserted, not argued.** The deck does not say which parts resist
  automation and why. The course content list nonetheless names "Automatic refactoring to improve
  program structure" among the semester's topics, and the two statements are never reconciled in
  the slides.
