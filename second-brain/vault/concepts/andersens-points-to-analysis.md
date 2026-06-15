---
title: "Andersen's Points-to Analysis"
tags: [concept, software-analyse, semester-1, points-to-analysis, andersen, inclusion-based]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[points-to-analysis]]", "[[steensgaards-points-to-analysis|Steensgaard's analysis]]"]
---

## One-line Summary
Andersen's points-to analysis is a precise, subset-based (inclusion-based) algorithm for [[points-to-analysis|points-to analysis]] that runs in O(n³) worst-case time — the practical sweet spot between [[steensgaards-points-to-analysis|Steensgaard's]] speed and full pointer-precision, and the foundation of most modern static analyzers.

## Core Intuition
[[steensgaards-points-to-analysis|Steensgaard's]] analysis is fast but imprecise: it merges points-to sets when two variables become aliased, so two variables that ever share an assignment end up in the same equivalence class. Andersen's 1994 analysis fixes this by using *subset constraints*: after `a = b`, only require pts(b) ⊆ pts(a) — they can have overlapping but distinct sets.

The tradeoff: subset constraints require solving a system of inclusions, not just union operations. The standard approach is a worklist algorithm that propagates points-to sets through the constraints until no new facts are added. Worst case: O(n³) for n variables (the cubic factor comes from the worst-case size of the inclusion graph).

In practice, with modern engineering (BDD-based encoding, demand-driven propagation, online cycle detection), Andersen's analysis scales to multi-million-line programs. Production tools like DOOP, WALA, and Infer all use variants of Andersen's.

**Reference**: Andersen, L. O. (1994). "Program Analysis and Specialization for the C Programming Language." PhD thesis, University of Copenhagen.

## Formal Definition / Statement

For each statement kind, Andersen's analysis generates a *subset* (inclusion) constraint:

| C | Java | Constraint (Andersen) |
|---|------|----------------------|
| `a = &b` | `a = new A()` | {l_b} ⊆ pts(a) |
| `a = b` | `a = b` | pts(b) ⊆ pts(a) |
| `a = *b` | `a = b.f` | pts(*b) ⊆ pts(a), where pts(*b) = ∪ {pts(l) | l ∈ pts(b)} |
| `a.f = b` | `a.f = b` | pts(b) ⊆ pts(*a), where pts(*a) = ∪ {pts(l) | l ∈ pts(a)} |
| `*a = b` | — | pts(b) ⊆ pts(*a) |

**Algorithm** (worklist-based):
1. For each statement, generate the inclusion constraints
2. Initialise: pts(v) = ∅ for all v
3. Process constraints:
   - For each constraint `pts(x) ⊆ pts(y)`: if there's an element l in pts(x) that's not in pts(y), add l to pts(y) and re-process all constraints that mention pts(y) (or pts(*y) for field-sensitive analyses)
4. Repeat until no changes (worklist empty)

**Complexity**: O(n³) worst case, where n is the number of variables. The cubic factor comes from the worst-case constraint graph.

**Termination**: pts(v) only grows; there are finitely many objects, so the analysis terminates.

## Key Properties

### Why Andersen's is more precise than Steensgaard's
For the program:
```c
int *a = &i;
int *b = &k;
a = &j;
int **p = &a;
int **q = &b;
p = q;
int *c = *q;
```
- **Steensgaard**: pts(a) = {i, j}, pts(c) = {i, j, k} (merged classes)
- **Andersen**: pts(a) ⊇ {i, j}, pts(c) ⊇ {k} (precise — c only inherits from b's set, not a's)

Andersen doesn't merge equivalence classes; it tracks each variable's points-to set independently. The cost is solving the inclusion constraints.

### Why Andersen's is O(n³) in the worst case
The cubic factor comes from the worst case of "every constraint adds an element to every other constraint's target". For n variables, there are O(n²) constraints (one per statement × one per variable), and each can add up to n elements → O(n³).

In practice, real programs don't hit this worst case, and modern engineering reduces the constant factor dramatically.

### Engineering tricks for scalability
- **BDD-based encoding**: encode points-to sets as binary decision diagrams; the analysis becomes a BDD-based constraint propagation, much faster in practice
- **Online cycle detection**: detect strongly connected components in the constraint graph; each SCC is solved once
- **Demand-driven propagation**: only compute points-to facts needed for a specific query
- **Difference propagation**: track which facts are "new" in each iteration to avoid redundant work
- **Wavefront / worklist priority**: process more-likely-to-trigger constraints first

These tricks can reduce Andersen's from O(n³) to O(n²) or better in practice.

### Subset-based vs equality-based
| | Andersen (subset) | Steensgaard (equality) |
|---|---|---|
| Constraint for `a = b` | pts(b) ⊆ pts(a) | pts(a) = pts(b) |
| Data structure | Worklist of constraints | Union-Find |
| Complexity | O(n³) | O(nα(n,n)) |
| Precision | Precise | Imprecise |
| Scalability | Needs engineering tricks | Scales naturally |

### The four "kinds" of constraints
Andersen's analysis handles all four pointer operation kinds:
- **Referencing** (a = &b / a = new A()): creates a fresh object reference
- **Aliasing** (a = b): one variable's points-to set is a subset of another's
- **Dereferencing read** (a = *b / a = b.f): a gets the points-to set of everything *b might point to
- **Dereferencing write** (*a = b / a.f = b): everything *a might point to gets b's points-to set

The two dereferencing kinds involve the "points-to of points-to" — for field-sensitive analyses, this includes field information.

## Worked Example

The lecture's example (slides 82-94):
```c
int i, j, k;
int *a = &i;       // {i} ⊆ pts(a)
int *b = &k;       // {k} ⊆ pts(b)
a = &j;             // {j} ⊆ pts(a); combined: pts(a) = {i, j}
int **p = &a;       // {a} ⊆ pts(p)
int **q = &b;       // {b} ⊆ pts(q)
p = q;              // pts(q) ⊆ pts(p); combined: pts(p) ⊇ {a, b}
int *c = *q;        // pts(*q) ⊆ pts(c); pts(*q) = pts(b) = {k}; so pts(c) ⊇ {k}
```

Final Andersen points-to sets:
- pts(i) = {i}, pts(j) = {j}, pts(k) = {k} (primitives don't point to anything)
- pts(a) = {i, j}  (precise)
- pts(b) = {k}     (precise)
- pts(p) ⊇ {a, b}  (precise — p *might* point to a or b)
- pts(q) ⊇ {b}     (precise — q *might* point to b)
- pts(c) ⊇ {k}     (precise — c *might* point to k)

The key difference from Steensgaard: c does NOT point to {i, j, k} — only to {k}. This is because Andersen doesn't merge p and q's equivalence classes; it keeps them distinct.

The lecture walks through the assignments one at a time, showing the points-to graph growing (slides 83-94).

## Common Pitfalls

- **Andersen's analysis is still a *may* analysis**. It says "v may point to {x, y, z}" — it doesn't say "v definitely points to x in this execution". A *must* points-to analysis is a different (and harder) problem.
- **Andersen's is *not* the most precise points-to analysis**. There are even more precise variants (e.g., flow-sensitive, context-sensitive, field-sensitive combinations). Andersen's is the practical sweet spot.
- **O(n³) is the worst case, not the typical case**. For real programs, with modern engineering, Andersen's scales to millions of LOC. Don't reject Andersen's on asymptotic grounds alone.
- **Field-insensitive Andersen is much faster but loses precision**. For Java, you almost always want field sensitivity (at least for "interesting" fields).
- **Andersen's for Java must handle the entire class hierarchy and dynamic dispatch**. The simple constraint generation assumes every call site resolves to one method; real Java has multiple targets per call site.
- **Andersen's is "inclusion-based" but not "unification-based"**. Steensgaard's is unification-based (merges equivalence classes). The difference is more than syntactic: it affects the lattice structure and the propagation algorithm.

## Connections

- [[points-to-analysis]] — the general topic
- [[steensgaards-points-to-analysis|Steensgaard's analysis]] — the fast alternative
- [[interprocedural-analysis]] — the interprocedural setting
- [[context-sensitivity]] — for precise interprocedural points-to
- [[aliasing]] — what the analysis enables reasoning about
- [[abstract-interpretation]] — Andersen's is an instance of abstract interpretation
- [[software-analyse-lecture-7]] — the lecture

## Open Questions

- Are there algorithms between Andersen's O(n³) and Steensgaard's O(nα) that give meaningful precision gains over Steensgaard at moderate cost? (Yes: "pseudounification", "Bjarne's analysis", etc.)
- How do modern tools (DOOP, WALA, PADDLE, Soot, Infer) implement Andersen's at scale? What BDD-based tricks do they use?
- For object-oriented programs, is *call-string* context sensitivity the right choice, or is *object sensitivity* better?
- Can Andersen's be made fully flow-sensitive (distinguishing points-to sets at different program points) without exploding the analysis state? What are the practical tradeoffs?
- What is the relationship between Andersen's and [[abstract-interpretation|abstract interpretation]]? Is Andersen's a particular abstract domain (the "powerset of object labels" domain) with a particular abstract transformer (the subset-propagating worklist)?
