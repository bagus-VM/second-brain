---
title: "Post-Dominance"
tags: [concept, software-analyse, semester-1, control-flow]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [dominance, control-flow-graph]
---

## One-line Summary

Node d post-dominates node n (d pdom n) if every path from n to the exit node passes through d — the dual of [[dominance]], computed by running the dominance algorithm on the reversed [[control-flow-graph|CFG]].

## Core Intuition

[[dominance|Dominance]] answers "what must I pass through to *reach* this node?" — post-dominance answers "what must I pass through *after* this node?" **If every execution path from node n eventually goes through d, then d post-dominates n**. The exit node post-dominates everything, just as the entry node dominates everything.

## Formal Definition / Statement

Given a [[control-flow-graph|CFG]] G = (N, E) with exit node n_f:

**d post-dominates n** (d pdom n) ⟺ every path from n to n_f includes d.

**Post-dominator** properties (analogous to [[dominance]]):
- Reflexive: n pdom n
- Transitive: a pdom b ∧ b pdom c → a pdom c
- Antisymmetric: a pdom b ∧ b pdom a → a = b

**Immediate post-dominator** (ipdom): The closest strict post-dominator; unique for each node.

**Pdom(n)**: The set of post-dominators of node n.

**Computing post-dominance:**
1. Reverse all edges in the CFG
2. The original exit node becomes the "entry" node of the reversed graph
3. Run the [[dominance]] algorithm on the reversed graph
4. The result gives the post-dominator sets and post-dominator tree

Best practice: **start from nodes closest to the exit and work backwards for faster convergence.**

## Key Properties / Complexity

- Post-dominance is the exact dual/mirror of dominance
- The post-dominator tree has the exit node as its root
- If a node has two outgoing edges (branch node), its immediate post-dominator is the merge point — where control flow rejoins
- Post-dominance is essential for computing [[control-dependence]]
- Each node has a unique immediate post-dominator

## Worked Example

Using the "3D PLOT" BASIC program CFG (nodes 1–300):

Post-dominator tree (exit as root):
```
         exit
          |
         300
          |
         210
        / | \
      190 200 ...
       |
      140
     / | \
   110 120 130
    |
   100
    |
    5
    |
    3
   / \
  1    2
```

Which nodes are post-dominated by 110?
→ All nodes whose every path to exit passes through 110: {100, 5, 3, 1, 2} (the pre-loop initialization chain).

Which nodes are post-dominated by 190?
→ 190 is the "NEXT Y" iteration point — nodes 170, 180, 150, 160 (the inner loop body) are post-dominated by 190 because every path from them must pass through 190 to continue or exit the inner loop.

## Common Pitfalls

- Forgetting to reverse the CFG before computing — post-dominance is dominance of the reversed graph
- Confusing post-dominance with dominance: they are different relations (one looks forward from entry, the other backward from exit)
- Not recognising that branch nodes and their post-dominators define the "merge points" in control flow

## Connections

- [[dominance]] — post-dominance is the mirror; same algorithm, reversed graph
- [[control-dependence]] — CDG construction requires the post-dominator tree
- [[dominator-tree]] — the post-dominator tree is the analogous structure (exit as root instead of entry)
- [[control-flow-graph]] — post-dominance is defined on the CFG
- Used in compiler optimisations: if a branch post-dominates a computation, that computation is only needed on one side of the branch

## Open Questions

- How does post-dominance relate to the concept of "necessary" computations in a program?
- In the presence of exceptions, how does post-dominance change (Java try/catch)?
