---
title: "Union-Find Data Structure"
tags: [concept, software-analyse, semester-1, data-structure, union-find, points-to-analysis]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[steensgaards-points-to-analysis|Steensgaard's analysis]]"]
---

## One-line Summary
Union-Find (also called Disjoint Set Union) is a data structure that maintains a partition of elements into disjoint sets, supporting two operations — find (which set is an element in?) and union (merge two sets) — in amortised nearly-constant time per operation; it is the engine that makes [[steensgaards-points-to-analysis|Steensgaard's points-to analysis]] O(n · α(n, n)) instead of O(n²).

## Core Intuition
Steensgaard's points-to analysis treats points-to sets as *equivalence classes*. Two variables are in the same class iff they have the same points-to set. The analysis needs:
- A way to ask "what class is variable v in?" — find
- A way to merge two classes — union

A naive implementation (e.g., a list of sets with linear-time lookups) gives O(n) per find and O(n) per union, for a total of O(n²). **Union-Find** with two optimisations — *path compression* (during find, make every visited node a direct child of the root) and *union by rank* (always attach the smaller tree under the root of the larger) — gives amortised O(α(n, n)) per operation, where α is the inverse Ackermann function.

For n = 10⁶, α(n, n) < 5. So in practice, Union-Find is constant-time per operation. This is what makes Steensgaard's points-to analysis scale.

## Formal Definition / Statement

A **Union-Find data structure** maintains a partition of a set of n elements into disjoint subsets, supporting:
- **find(x)**: return a representative (canonical element) of the subset containing x
- **union(x, y)**: merge the subsets containing x and y into one subset

Optimisations:
- **Path compression**: during find, make every node on the path to the root a direct child of the root. After this, repeated finds on the same elements are O(1).
- **Union by rank/size**: always attach the root of the smaller tree under the root of the larger tree. This keeps the tree height logarithmic.

**Time complexity** (with both optimisations):
- find: O(α(n, n)) amortised
- union: O(α(n, n)) amortised
- n operations total: O(n · α(n, n))

For all practical purposes, α(n, n) ≤ 5, so this is constant time.

## Key Properties

### Why Union-Find works for Steensgaard's
In Steensgaard's analysis:
- Each variable starts in its own set
- `a = b` becomes union(find(a), find(b))
- `a = &i` becomes a fresh set for a containing {i}
- `a = *b` becomes union(find(a), find(l)) for each l ∈ find(b)
- `*a = b` becomes union(find(b), find(l)) for each l ∈ find(a)

Every operation is a find or a union. The total work is O(n · α(n, n)).

### Why path compression + union by rank
- **Path compression alone**: O(log n) amortised per operation (Tarjan 1975)
- **Union by rank alone**: O(log n) amortised per operation
- **Both together**: O(α(n, n)) amortised (Tarjan 1975)

The combination is provably optimal among all "natural" Union-Find algorithms.

### When Union-Find is not enough
- Union-Find maintains a *partition* (disjoint sets). If you need overlapping sets, use a different data structure.
- For [[andersens-points-to-analysis|Andersen's]] analysis (subset-based, not equality-based), Union-Find is not directly applicable — the analysis is more complex and requires a worklist.

### Real-world applications of Union-Find
- Steensgaard's points-to analysis (the lecture's focus)
- Kruskal's algorithm for minimum spanning trees
- Network connectivity (find connected components)
- Image segmentation (union pixels into regions)
- Percolation theory
- Online algorithms for graph problems

## Worked Example

For the program:
```c
int *a = &i;       // pts(a) = {i}: create a new class {a: {i}}
int *b = &k;       // pts(b) = {k}: create a new class {b: {k}}
a = &j;             // Steensgaard: pts(a) = pts(a) ∪ {j} = {i, j}: just add j to a's class
int **p = &a;       // pts(p) = {a}: create class {p: {a}}
int **q = &b;       // pts(q) = {b}: create class {q: {b}}
p = q;              // Steensgaard: pts(p) = pts(q) = {a, b}: union class of p and class of q
int *c = *q;        // for each l ∈ pts(q) = {a, b}, union class of c with class of l
```

Union-Find operations:
1. make_set(a), make_set(b), make_set(p), make_set(q), make_set(c)
2. Class {a: {i}}: fresh
3. Class {b: {k}}: fresh
4. Add j to a's class: {a: {i, j}}
5. Class {p: {a}}: fresh
6. Class {q: {b}}: fresh
7. union(p, q): merge {p: {a}} and {q: {b}} into {p, q: {a, b}}
8. union(c, a) (l=a ∈ pts(q)): merge {c: {}} and {a: {i, j}} into {a, c: {i, j}}
9. union(c, b) (l=b ∈ pts(q)): merge {a, c: {i, j}} and {b: {k}} into {a, b, c: {i, j, k}}

Final: {a, b, c: {i, j, k}} — a, b, c all share the same points-to set. This is the imprecision of Steensgaard's.

With path compression, every find operation makes the queried element a direct child of the root, so subsequent finds are O(1).

## Common Pitfalls

- **Union-Find does not support set intersection or element removal**. If you need to remove an element from a set, use a different data structure.
- **Path compression changes the tree structure**. This is fine for amortised analysis but means the tree is "destroyed" after many operations. If you need a persistent (immutable) data structure, look at persistent Union-Find.
- **The amortised O(α(n, n)) bound is tight**. No Union-Find algorithm with a "find" and "union" interface can be asymptotically faster.
- **Union-Find is not thread-safe** in its basic form. Concurrent Union-Find requires careful synchronisation.

## Connections

- [[steensgaards-points-to-analysis|Steensgaard's analysis]] — the canonical application
- [[points-to-analysis]] — the broader topic
- [[andersens-points-to-analysis|Andersen's analysis]] — the precise alternative (uses worklist, not Union-Find)
- [[interprocedural-analysis]] — the broader setting
- data-structures — the general category

## Open Questions

- Are there asymptotically faster Union-Find algorithms for special cases (e.g., offline algorithms, where all unions are known in advance)?
- Can Union-Find be made fully persistent? What's the cost?
- How does concurrent Union-Find (with multiple threads) compare to single-threaded Union-Find in practice?
- Is there a meaningful "precision ladder" for points-to analyses where Union-Find (Steensgaard) sits at the imprecise end?
