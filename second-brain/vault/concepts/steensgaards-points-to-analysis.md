---
title: "Steensgaard's Points-to Analysis"
tags: [concept, software-analyse, semester-1, points-to-analysis, steensgaard]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[points-to-analysis]]", "[[union-find-data-structure|Union-Find]]"]
---

## One-line Summary
Steensgaard's points-to analysis is a fast, equality-based algorithm for [[points-to-analysis|points-to analysis]] that runs in O(n · α(n, n)) time (almost linear) using a [[union-find-data-structure|Union-Find]] data structure — at the cost of precision, since any two variables that ever share an assignment end up in the same points-to equivalence class.

## Core Intuition
The [[points-to-analysis|points-to problem]] has a precision/scalability tradeoff. Steensgaard's 1996 algorithm sits at the "scalable" end: it answers the question "where might this variable point?" in almost-linear time by using *equality* constraints (pts(a) = pts(b) after `a = b`) instead of *subset* constraints (pts(b) ⊆ pts(a)).

The key insight: if you treat points-to sets as *equivalence classes* — and union them whenever two variables become aliased — you can implement the analysis with [[union-find-data-structure|Union-Find]], which is amortised nearly constant time per operation.

The price: precision. In the lecture's example, after `a = &i; b = &k; a = &j;`:
- pts(a) is the *set containing both i and j* (Steensgaard's merges with the previous pts(a))
- pts(b) is {k}

If a later statement says `c = *q` where pts(q) includes a, the analysis must union c with *everything* in the equivalence class containing a. This can cascade.

For real-world code with millions of variables, Steensgaard's is fast enough to run on every compilation. For deep object-oriented programs, the precision loss is too painful — use [[andersens-points-to-analysis|Andersen's]] instead.

## Formal Definition / Statement

For each statement kind, Steensgaard's analysis generates an *equality* constraint:

| C | Java | Constraint (Steensgaard) |
|---|------|---------------------------|
| `a = &b` | `a = new A()` | pts(a) = {l_b} (create new equivalence class) |
| `a = b` | `a = b` | pts(a) = pts(b) (union the equivalence classes) |
| `a = *b` | `a = b.f` | for each l ∈ pts(b), pts(a) = pts(l) (union a with all the l's classes) |
| `*a = b` | `a.f = b` | for each l ∈ pts(a), pts(l) = pts(b) (union b with all the l's classes) |

The algorithm maintains a partition of variables into equivalence classes, where two variables are in the same class iff they have the same points-to set.

**Algorithm**:
1. Initialise: every variable is in its own class
2. For each statement in program order:
   - If `a = &b`: create a fresh class for a containing {l_b}
   - If `a = b`: union(class(a), class(b))
   - If `a = *b`: union(class(a), class(l)) for each l ∈ class(b)
   - If `*a = b`: union(class(b), class(l)) for each l ∈ class(a)
3. Repeat until no unions happen (or just process once with [[union-find-data-structure|Union-Find path compression]])

**Complexity**: O(n · α(n, n)) where n is the number of variables, using Union-Find with path compression and union by rank. α is the inverse Ackermann function — for all practical purposes, a constant.

**Reference**: Steensgaard, B. (1996). "Points-to analysis in almost linear time." POPL '96.

## Key Properties

### Tradeoffs
- **+**: Fast — O(n · α(n, n)) per statement, can analyse millions of LOC
- **+**: Simple — Union-Find, no constraint solver
- **+**: Used in production compilers (e.g., GCC's early points-to analysis)
- **−**: Imprecise — any aliasing union merges entire equivalence classes
- **−**: No field sensitivity in the basic form
- **−**: No context sensitivity in the basic form

### Why it's imprecise — a comparison with Andersen
For the program:
```c
int *a = &i;
int *b = &k;
a = &j;
int **q = &b;
p = q;
int *c = *q;
```
- **Steensgaard**: pts(a) = {i, j} (merged), pts(q) = {a, b} (p=q merged the classes), pts(c) = pts(b) ∪ pts(a) = {i, j, k}
- **Andersen**: pts(a) = {i, j} (subset), pts(q) ⊇ pts(p) ∪ {a, b} (subset), pts(c) ⊇ pts(b) = {k}

Steensgaard's c points to {i, j, k}; Andersen's c points to {k}. Steensgaard is correct (c *could* point to any of these in some execution) but loose.

### Insensitive to flow, context, fields
- **Flow-insensitive**: statement order doesn't matter. Steensgaard's treats the program as a set of constraints, not an ordered sequence.
- **Context-insensitive**: call sites are not distinguished. The same procedure is analysed once.
- **Field-insensitive** (in the basic form): all fields of an object share one points-to set.

These are not bugs; they're simplifications. Each simplification trades precision for scalability.

### The "equality" trick
The key idea that makes Steensgaard's fast: instead of tracking precise subset relations, treat points-to sets as *equivalence classes*. `a = b` becomes "merge a's class with b's class" — a Union-Find operation. No need to propagate subsets through the whole program.

This works because Union-Find with path compression is amortised nearly O(1) per operation. So the whole analysis is O(n · α(n, n)).

## Worked Example

The lecture's running example (slides 70-78):
```c
int i, j, k;
int *a = &i;       // pts(a) = {i}
int *b = &k;       // pts(b) = {k}
a = &j;             // Steensgaard: pts(a) = pts(a) ∪ {j} = {i, j}
int **p = &a;       // pts(p) = {a}
int **q = &b;       // pts(q) = {b}
p = q;              // Steensgaard: pts(p) = pts(q) = {a, b} (union)
int *c = *q;        // for each l ∈ pts(q) = {a, b}, pts(c) = pts(l) = pts(a) ∪ pts(b) = {i, j, k}
```

Final Steensgaard points-to sets:
- pts(a) = {i, j}
- pts(b) = {k}
- pts(c) = {i, j, k}  (the imprecision — c *might* point to a's or b's targets, and the analysis merged them)
- pts(p) = pts(q) = {a, b}  (also imprecise — p and q share an equivalence class)

This matches the lecture's slide 78.

## Common Pitfalls

- **Steensgaard is unsound for aliasing-sensitive code if you naively extend it**. The "equality" trick is *sound* (it over-approximates) but can be unnecessarily imprecise.
- **Steensgaard's precision loss is not uniform across programs**. For deeply nested pointer manipulation, it can be catastrophically imprecise. For typical imperative code with simple aliasing, it's often acceptable.
- **The "almost linear" claim depends on the input being pointer-manipulation-heavy but not deeply recursive**. For some pathological inputs, the analysis can degrade.
- **Field sensitivity is a separate axis**. The basic Steensgaard algorithm is field-insensitive. Field-sensitive variants exist but are more expensive.
- **Steensgaard's analysis can be made context-sensitive**, but the basic version is not. The hybrid "Steensgaard's analysis with call strings" is a common extension.

## Connections

- [[points-to-analysis]] — the general topic
- [[andersens-points-to-analysis|Andersen's analysis]] — the precise alternative
- [[union-find-data-structure|Union-Find]] — the data structure behind Steensgaard's
- [[aliasing]] — what the analysis enables reasoning about
- [[interprocedural-analysis]] — the interprocedural setting
- [[context-sensitivity]] — a precision axis Steensgaard's doesn't address in the basic form
- [[software-analyse-lecture-7]] — the lecture

## Open Questions

- Are there algorithms between Steensgaard's O(nα) and Andersen's O(n³) that give *some* of Andersen's precision at lower cost?
- For object-oriented programs, can Steensgaard's be made object-sensitive? Field-sensitive? How expensive does it get?
- How do production tools (DOOP, WALA) implement variants of Steensgaard's for Java? What are the engineering tricks?
- Is there a meaningful "precision ladder" — Steensgaard < bset < Andersen < flow-sensitive < context-sensitive < object-sensitive — with associated complexity ladders?
