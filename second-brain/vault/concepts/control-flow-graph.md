---
title: "Control Flow Graph"
tags: [concept, software-analyse, semester-1, control-flow]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [abstract-syntax-tree]
---

## One-line Summary

A Control Flow Graph (CFG) is a directed graph G=(N,E) where ==nodes represent statements== (or [[basic-block|basic blocks]]) and ==edges model the possible transfer of control between them== during program execution.

## Core Intuition

Source code executes in a sequence — that sequence is the control flow. A CFG strips away syntactic details (types, declarations, expressions) and captures only ==*what can execute next after what*==. This abstraction makes it tractable to reason about reachability, optimisation, and testing.

## Formal Definition / Statement

A **Control Flow Graph** is a directed graph G = (N, E) where:
- N is a set of nodes, each representing a statement or basic block
- E ⊆ N × N is a set of directed edges representing control flow
- There is a unique **entry node** n₀ (no incoming edges from outside the procedure)
- There is a unique **exit node** n_f (no outgoing edges to outside the procedure)

**Definitions:**
- **Predecessor**: n_i is a predecessor of n_j if (n_i, n_j) ∈ E → Pred(n_j) = { n_i | (n_i, n_j) ∈ E }
- **Successor**: n_j is a successor of n_i if (n_i, n_j) ∈ E → Succ(n_i) = { n_j | (n_i, n_j) ∈ E }
- **Branch node**: a node with |Succ(n)| > 1
- **Join node**: a node with |Pred(n)| > 1

## Key Properties / Complexity

- CFGs are much simpler than [[abstract-syntax-tree|ASTs]]: fewer node types, less redundancy, only simple expressions
- CFGs lose block structure — harder to report errors or unparse back to readable code
- The unique entry/exit assumptions simplify analysis algorithms (e.g., [[dominance]])
- Every Java control structure maps to a CFG pattern:
  - `if`/`else` → branch node with two outgoing edges
  - `for`/`while` → back edge creating a [[natural-loop]]
  - `do-while` → body executes before the condition is tested (no branch before body)
  - `switch` → multiple outgoing edges from the switch node
  - `break` → edge directly to the loop exit
  - `try/catch` → edge from the try body to the catch block on exception

## Worked Example

```java
public int foo(int x) {
    int y = 0;           // Entry → node 2
    while(x >= 0) {      // node 2 → node 4 (branch)
        if(x % 2 == 0)   // node 4 → node 5 (branch)
            y += x;       // node 5 → node 6 (true branch)
        x--;              // node 7
    }                     // node 7 → node 4 (back edge!)
    return y;             // node 10 → Exit
}
```

CFG:
```
Entry → 2(y=0) → 4(x>=0?)
              ↙ T       F ↘
        5(x%2==0?)      10(return y) → Exit
        ↙ T     F ↘
      6(y+=x)  7(x--)
         ↘      ↙
          4  (back edge)
```

Edge types: forward edges (Entry→2, 2→4, 4→5, 4→10, 5→6, 5→7) and back edges (7→4, 6→4) forming a [[natural-loop]].

## Common Pitfalls

- Confusing AST nodes with CFG nodes — a single AST statement may span multiple CFG nodes, and a single CFG node may contain multiple AST statements (when collapsed into [[basic-block|basic blocks]])
- Forgetting the back edge in loops — without it, the CFG doesn't model iteration
- Ignoring implicit control flow (`exceptions`, `break`, `continue`) which requires special edges
- Assuming the CFG captures all program semantics — it models *flow*, not *data*

## Connections

- [[basic-block]] – CFGs are often compressed by grouping consecutive non-branching nodes into basic blocks
- [[dominance]] – defined and computed on CFGs; the entry node dominates all others
- [[post-dominance]] – the dual relation, computed by reversing CFG edges
- [[control-dependence]] – derived from the CFG and the [[dominator-tree|post-dominator tree]]
- [[natural-loop]] – identified by back edges in the CFG
- [[abstract-syntax-tree]] – CFG is derived from the AST by walking it and adding flow edges

## Open Questions

- How do we handle irreducible control flow (loops with multiple entry points) that don't arise from structured code?
- In interprocedural analysis, how do we connect per-procedure CFGs into a whole-program representation (call graph)?
