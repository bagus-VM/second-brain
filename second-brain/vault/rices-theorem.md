---
title: "Rice's Theorem"
tags: [concept, software-analyse, semester-1]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [software-analysis]
---

## One-line Summary
Rice's theorem states that all non-trivial semantic properties of programs are undecidable — no algorithm can perfectly determine them for all programs.

## Core Intuition
You can't build a perfect bug finder. Not because we're not smart enough, but because mathematics proves it's impossible. Any property that's interesting (non-trivial) and about program behaviour (semantic) cannot be decided for all programs. This is why we need approximations (see [[abstract-interpretation]]).

## Formal Definition / Statement
"All non-trivial semantic properties of programs are undecidable."

Definitions:
- **Non-trivial**: there exists at least one program that has the property and at least one that does not
- **Semantic property**: a property about what the program does (behaviour), not how it looks (syntax)
- **Undecidable**: no automated method can determine whether the property holds for *any* program

Proof sketch (constant-value analysis):
- Suppose we have an analyser that decides if a variable has a constant value in any execution
- Consider: `x = 17; if (TM(j)) x = 18;`
- x is constant if and only if the j-th Turing machine does not halt on empty input
- If the constant-value analyser exists, we have a decision procedure for the halting problem
- The halting problem is known to be impossible → contradiction

## Key Properties
- Applies to *all* programs — there will always be some program the analysis gets wrong
- Applies to *semantic* properties — syntactic properties (like "does the code contain a semicolon?") are decidable
- Does NOT say analysis is useless — it says perfect analysis is impossible
- The escape hatch: approximate (see [[abstract-interpretation]])

## Worked Example
**Property: "Does this variable always have the same value?"**

```c
x = 17;
if (TURING_MACHINE_HALTS(j))
    x = 18;
```

If x = 17 always, then TM(j) never halts. If x could be 18, then TM(j) halts. Deciding constancy = deciding the halting problem = impossible.

## Common Pitfalls
- Thinking Rice's theorem means "we can't analyze programs" — we can, just not perfectly
- Confusing "undecidable" with "useless" — approximate analysis catches most real bugs
- Forgetting the "non-trivial" condition — trivial properties (always true/false) are decidable
- Applying Rice's theorem to syntactic properties — it only applies to semantic ones

## Connections
- [[software-analysis]] — Rice's theorem is the fundamental limitation driving the field
- [[abstract-interpretation]] — the standard approach to work around undecidability
- [[soundness-and-completeness]] — the formal framework for understanding what we sacrifice
- [[static-vs-dynamic-analysis]] — both approaches exist because perfect static analysis is impossible

## Open Questions
- Are there practically-relevant properties that are decidable despite Rice's theorem?
- How does the undecidability result change when we restrict to specific program classes?
- What's the relationship between Rice's theorem and the halting problem in practice?
