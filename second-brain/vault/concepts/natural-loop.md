---
title: "Natural Loops"
tags: [concept, software-analyse, semester-1, control-flow]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [dominance, control-flow-graph]
---

## One-line Summary

A natural loop is a set of nodes in a [[control-flow-graph|CFG]] identified by a back edge (an edge from a node to one of its [[dominance|dominators]]), having a single entry point (the header) and at least one path that iterates back to it.

## Core Intuition

Loops are where programs spend most of their time, so identifying them is critical for optimisation. A natural loop is the *minimal* set of nodes that form a loop with a single entry point. It's defined by a back edge n→d where d dominates n — meaning you can't get into the loop body without going through d first. The loop consists of d plus all nodes that can reach n without going through d.

## Formal Definition / Statement

**Back edge**: An edge n→d in the CFG where d dominates n (d is the head, n is the tail).

**Natural loop** for back edge n→d:
- The set {d} ∪ { x | there exists a path from x to n that does not pass through d }
- d is called the **header** of the loop

**Essential properties** of natural loops suitable for optimisation:
1. **Single entry point** (the header) — the loop is entered only through one node
2. **At least one back edge** — ensures there is a way to iterate

**Inner loop**: A loop that contains no other loops. If two loops share the same header, they are merged into a single loop.

## Key Properties

- Unless two natural loops have the same header, they are either **disjoint** or one is **entirely contained** within the other (nesting structure)
- Inner loops (containing no other loops) are the best candidates for optimisation
- Every [[natural-loop|natural loop]] header dominates all other nodes in the loop
- A loop may have multiple back edges pointing to the same header — they are merged into one loop
- Natural loops correspond to structured loop constructs (`for`, `while`, `do-while`) in source code, but can also arise from `goto` or irregular control flow

## Worked Example

CFG with blocks 1–10:

```
1 → 2, 9
1 → 2
2 → 3
3 → 4, 8
4 → 5, 6
5 → 7
6 → 7
7 → 8
8 → 9, 10
9 → 1       (back edge: 9→1, since 1 dom 9? No...)
```

Wait — let's use the lecture's example with known dominator sets:

| Block | DOM              | IDom |
|-------|------------------|------|
| 1     | {1}              | -    |
| 2     | {1,2}            | 1    |
| 3     | {1,3}            | 1    |
| 4     | {1,3,4}          | 3    |
| 5     | {1,3,4,5}        | 4    |
| 6     | {1,3,4,6}        | 4    |
| 7     | {1,3,4,7}        | 4    |
| 8     | {1,3,4,7,8}      | 7    |
| 9     | {1,3,4,7,8,9}    | 8    |
| 10    | {1,3,4,7,8,10}   | 8    |

Back edges and natural loops:

| Back Edge | Header | Natural Loop            |
|-----------|--------|-------------------------|
| 10 → 7    | 7      | {7, 10, 8}              |
| 7 → 4     | 4      | {4, 7, 5, 6, 10, 8}     |
| 4 → 3     | 3      | {3, 4, 7, 5, 6, 10, 8}  |
| 8 → 3     | 3      | {3, 4, 7, 5, 6, 10, 8}  |
| 9 → 1     | 1      | {1, 9, 8, 7, 5, 6, 10, 4, 3, 2} |

**Inner loop**: {7, 8, 10} (from back edge 10→7) — contains no other loops.

**Nesting**: The loop {7, 8, 10} is nested inside {4, 5, 6, 7, 8, 10}, which is nested inside {3, 4, 5, 6, 7, 8, 10}.

## Common Pitfalls

- Confusing natural loops with general cycles in a graph — a natural loop has a single entry header; a cycle can have multiple entry points (irreducible)
- Forgetting to merge loops with the same header — multiple back edges to the same header form one loop, not separate loops
- Not checking that the back edge target actually dominates the source (it must be a *back* edge, not just any cycle-forming edge)
- Assuming natural loops correspond 1:1 with source-level loop constructs — `break`, `continue`, and `goto` can create irregular loops

## Connections

- [[dominance]] – back edges are defined via dominance (n→d where d dom n); the header dominates all loop nodes
- [[control-flow-graph]] – natural loops are subgraphs of the CFG
- [[basic-block]] – loop bodies are composed of basic blocks; the header always starts a new basic block
- [[dominator-tree]] – the nesting structure of loops mirrors the dominator tree hierarchy
- Loop-invariant code motion and other loop optimisations target natural loops
- [[control-dependence]] – loop exit conditions create control dependencies between the condition and the loop body

## Open Questions

- How do we handle irreducible loops (multiple entry points) that cannot be represented as natural loops?
- What is the relationship between natural loops and the "reducible" property of control flow graphs?
- How do we identify and optimise loops in the presence of `break`, `continue`, and early `return`?
