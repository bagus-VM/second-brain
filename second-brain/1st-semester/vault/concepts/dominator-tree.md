---
title: "Dominator Tree"
tags: [concept, software-analyse, semester-1, control-flow]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [dominance, control-flow-graph]
---

## One-line Summary

The dominator tree is a tree where each node's parent is its [[dominance|immediate dominator (idom)]], providing a compact representation of the full dominance relation over a [[control-flow-graph|CFG]].

## Core Intuition

The full dominance relation can be huge — O(n²) pairs. But because dominance is a transitive partial order, knowing just the immediate dominator of each node is enough to reconstruct the entire relation. The dominator tree encodes this: if a is an ancestor of b in the tree, then a dom b.

## Formal Definition / Statement

Given a [[control-flow-graph|CFG]] G = (N, E) with dominance relation computed:

- **Strict dominators** of n: SDOM(n) = DOM(n) \ {n}
- **Immediate dominator** idom(n): the strict dominator of n that is closest to n (i.e., no other strict dominator of n is dominated by idom(n) but not by n)
- The **dominator tree** T has the same node set N, with parent(n) = idom(n) for all n ≠ entry

**Computing IDOM from DOM:**
1. For each node n, set IDOM(n) = SDOM(n) = DOM(n) \ {n}
2. For each node p in IDOM(n), check if p has a dominator (other than itself) that is also in IDOM(n). If so, remove p from IDOM(n).
3. The remaining element is idom(n) — the strict dominator closest to n.

## Key Properties / Complexity

- The dominator tree is unique for a given CFG
- The entry node is always the root
- A is an ancestor of B in the dominator tree ⟺ A dom B
- The tree height can be O(n) in the worst case (linear chain), but is typically O(log n) for structured programs
- Dominator tree edges are *not* necessarily edges in the original CFG

## Worked Example

From a CFG with blocks 1–10:

| Block | DOM              | SDOM           | IDom |
|-------|------------------|----------------|------|
| 1     | {1}              | {}             | -    |
| 2     | {1,2}            | {1}            | 1    |
| 3     | {1,3}            | {1}            | 1    |
| 4     | {1,3,4}          | {1,3}          | 3    |
| 5     | {1,3,4,5}        | {1,3,4}        | 4    |
| 6     | {1,3,4,6}        | {1,3,4}        | 4    |
| 7     | {1,3,4,7}        | {1,3,4}        | 4    |
| 8     | {1,3,4,7,8}      | {1,3,4,7}      | 7    |
| 9     | {1,3,4,7,8,9}    | {1,3,4,7,8}    | 8    |
| 10    | {1,3,4,7,8,10}   | {1,3,4,7,8}    | 8    |

Dominator tree:
```
        1
       / \
      2   3
          |
          4
        / | \
       5  6  7
              |
              8
             / \
            9  10
```

To verify: Does 3 dominate 9? Check if 3 is an ancestor of 9 in the tree: 3→4→7→8→9. Yes! ✓

## Common Pitfalls

- Confusing dominator tree edges with CFG edges — they are completely different
- Forgetting that idom(n) is always *unique* (proven property of dominance)
- Building the tree before computing dominance — the tree is derived *from* the dominance computation

## Connections

- [[dominance]] – the dominator tree is derived from the dominance relation
- [[natural-loop]] – a back edge n→d creates a loop; d is the header and appears as an ancestor of n in the dominator tree
- [[post-dominance]] – the post-dominator tree is the analogous structure for the reversed CFG
- [[control-dependence]] – the CDG construction algorithm traverses the post-dominator tree
- SSA construction uses dominance frontiers computed from the dominator tree

## Open Questions

- How does the Lengauer-Tarjan algorithm compute the dominator tree in nearly-linear time?
- What are dominance frontiers and how do they relate to SSA form φ-node placement?
