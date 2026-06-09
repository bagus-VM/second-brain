---
title: "Control Dependence"
tags: [concept, software-analyse, semester-1, control-flow]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [post-dominance, dominance, control-flow-graph]
---

## One-line Summary

Statement b is control dependent on statement a if a's evaluation directly determines whether b will execute — formally captured via the [[post-dominance|post-dominator tree]] and [[control-flow-graph|CFG]] edges, and represented in the Control Dependence Graph (CDG).

## Core Intuition

Not all statements depend on all prior decisions. `y += x` inside an `if` is control dependent on the `if` condition — it only executes when the condition is true. But `return y` after the `if` is *not* control dependent on the condition (it executes regardless). Control dependence captures this "my execution depends on that branch's outcome" relationship.

## Formal Definition / Statement

**b is control dependent on a** if and only if:
1. There exists a directed path from a to b in the [[control-flow-graph|CFG]] such that every node on the path (excluding a) is [[post-dominance|post-dominated]] by b.
2. a is **not** post-dominated by b.

**Interpretation**: For b to be control dependent on a, a must have at least two outgoing edges (be a branch node), and one of those paths leads through b while b post-dominates all intermediate nodes on that path. This means a "directly determines" whether b executes.

**CDG Construction Algorithm:**
1. Find set S of CFG edges (A, B) where B is **not** an ancestor of A in the post-dominator tree
2. For each edge (A, B) in S, find L = LCA(A, B) in the post-dominator tree (least common ancestor)
3. Traverse backwards in the post-dominator tree from B to L, marking each visited node; mark L only if L = A
4. All marked nodes are control dependent on A

## Key Properties

- Every node that is not control dependent on any branch is control dependent on the entry node
- Control dependence is not the same as data dependence — two statements can be control dependent without sharing any variables
- The CDG is a directed graph; edges go from the controlling branch to the controlled statement
- For structured programs (if/else, while, for), control dependence directly mirrors the nesting structure
- The CDG is the basis for **program slicing**: a slice with respect to a statement includes all statements on which it is control or data dependent

## Worked Example

```python
def testMe(x, y):
    if x <= y:          # A (Entry)
        if x == y:      # B
            print(...)  # C
        if x > 0:       # D
            if y == 17: # E
                return True   # F
    return False        # H
```

Dominators and post-dominators determine control dependence:

| Node | Dominators    | Post-Dominators |
|------|---------------|-----------------|
| A    | {A}           | {A,B,I}         |
| B    | {A,B}         | {B,I}           |
| C    | {A,B,C}       | {C,E,I}         |
| D    | {A,B,D}       | {D,E,I}         |
| E    | {A,B,C,E}     | {E,I}           |
| F    | {A,B,C,E,F}   | {F,I}           |
| H    | {A,B,H}       | {H,I}           |
| I    | {A,B,I}       | {I}             |

Control dependencies:
- C is control dependent on **B** (B's true branch goes through C; B is not post-dominated by C)
- D is control dependent on **B** (B's false branch goes through D)
- F is control dependent on **E** (E's true branch goes through F)
- H is control dependent on **B** (the else-path of B leads to H)
- B is control dependent on **A** (A's true branch leads to B)

```
A → B → C
  ↘   ↘ D → E → F
        ↘ H
```

## Common Pitfalls

- Confusing control dependence with dominance/post-dominance — they are *derived from* these but are a distinct relation
- Forgetting condition 2 (a is not post-dominated by b): without it, you'd incorrectly say sequential statements are control dependent on each other
- Not realising that control dependence is asymmetric: if b depends on a, a does not necessarily depend on b
- In switch/case without break, multiple cases can be control dependent on the same switch node

## Connections

- [[post-dominance]] – the CDG construction algorithm directly uses the post-dominator tree
- [[dominance]] – dominance is used as a building block; the LCA step in CDG construction uses the post-dominator tree
- [[control-flow-graph]] – control dependence is defined on the CFG
- [[dominator-tree]] – the post-dominator tree (a variant) is traversed during CDG construction
- Program slicing and debugging tools use the CDG to determine which statements affect a given point
- Testing: branch coverage targets all control dependencies

## Open Questions

- How does control dependence extend to interprocedural analysis?
- What is the relationship between control dependence and program dependence graphs (PDGs)?
- How do we handle control dependence in the presence of exceptions and non-local control flow?
