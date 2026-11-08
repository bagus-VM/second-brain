---
title: "Dominance"
tags: [concept, software-analyse, semester-1, control-flow]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [control-flow-graph]
---

## One-line Summary

**Node a dominates node b (a dom b) if every path from the entry node to b passes through a** — a foundational relation for [[control-flow-graph|CFG]] analysis, loop identification, and SSA construction.

## Core Intuition

If you can't reach node b without first visiting node a, then a "controls" access to b. The entry node trivially dominates everything. Inside a [[natural-loop]], the loop header dominates all loop body nodes. Dominance captures this "you must pass through me" relationship structurally.

## Formal Definition / Statement

Given a [[control-flow-graph|CFG]] G = (N, E) with entry node n₀:

**a dominates b** (a dom b) ⟺ every path from n₀ to b includes a.

**Immediate dominator** (idom): The closest strict dominator of n — the last dominator on any path from entry to n. Every node (except entry) has a unique immediate dominator.

**Dominator properties:**
- **Reflexive**: a dom a (every node dominates itself)
- **Transitive**: a dom b ∧ b dom c → a dom c
- **Antisymmetric**: a dom b ∧ b dom a → a = b

**Computational rules** (for determining a dom b):
1. a = b, OR
2. a is the unique predecessor of b, OR
3. a is the unique predecessor of some predecessor of b

**Algorithm** (iterative fixed-point):
```
D(entry) = {entry}
for each n ≠ entry: D(n) = N  (all nodes)
repeat:
    for each n ≠ entry:
        D(n) = {n} ∪ ∩{D(p) | p ∈ Pred(n)}
    until no D(n) changes
```

## Key Properties / Complexity

- The dominator relation forms a partial order on N
- The **dominator tree**: parent(n) = idom(n); if a is an ancestor of b in the tree, then a dom b
- Entry node dominates all other nodes
- The entry node to a [[natural-loop]] (the header) dominates all other nodes in that loop
- Dominance is computed by iteratively intersecting dominator sets of predecessors until a fixed point is reached
- The algorithm converges because dominator sets can only shrink (monotonically decreasing)

## Worked Example

CFG with 11 nodes (0–10):

```
0 → 1, 9
1 → 2
2 → 3
3 → 4, 8
4 → 5, 6
5 → 7
6 → 7
7 → 8
8 → 9, 10
9 → 1
10 → (exit)
```

Iteration results:

| Block | DOM            | IDom |
|-------|----------------|------|
| 0     | {0}            | -    |
| 1     | {0,1}          | 0    |
| 2     | {0,1,2}        | 1    |
| 3     | {0,1,3}        | 1    |
| 4     | {0,1,3,4}      | 3    |
| 5     | {0,1,3,4,5}    | 4    |
| 6     | {0,1,3,4,6}    | 4    |
| 7     | {0,1,3,4,7}    | 4    |
| 8     | {0,1,3,4,7,8}  | 7    |
| 9     | {0,1,3,4,7,8,9}| 8    |
| 10    | {0,1,3,4,7,8,10}| 8   |

The dominator tree has 0 as root, with children reflecting the IDom column.

## Common Pitfalls

- Confusing "dominates" with "is predecessor of" — dominance requires *all* paths, not just one
- Forgetting the reflexive property: every node dominates itself
- Computing dominance on the wrong graph — it must be on the [[control-flow-graph|CFG]], not the [[abstract-syntax-tree|AST]]
- Not checking convergence of the iterative algorithm — it always terminates because sets only shrink

## Connections

- [[dominator-tree]] – compact representation of the dominance relation via immediate dominators
- [[post-dominance]] – the dual concept: dominance in the reversed CFG
- [[natural-loop]] – back edges are defined as edges n→d where d dom n; the loop header is the dominator
- [[control-dependence]] – computed using the [[post-dominance|post-dominator tree]]
- SSA form construction uses dominance frontiers (not covered in this lecture but builds on dominance)

## Open Questions

- What is the time complexity of the iterative dominance algorithm vs. Lengauer-Tarjan?
- How does dominance extend to irreducible control flow graphs?
