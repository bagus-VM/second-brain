---
title: "Data Flow Analysis"
tags: [concept, software-analyse, compilers, semester-1, data-flow]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-04
prerequisites: [control-flow-graph]
---

## One-line Summary

Data flow analysis is a compile-time technique that tracks how data (definitions, expressions, variable values) propagates through a program's control-flow graph using iterative fixed-point computation on gen/kill equations.

## Core Intuition

Every statement in a program both *creates* (gen) and *destroys* (kill) facts about the program state. By propagating these facts along the [[control-flow-graph]], we can determine at each program point what *could* be true or *must* be true. Rather than tracing every path (which is exponential), we compute IN/OUT sets for each basic block and iterate until nothing changes — reaching a fixed point.

When a compiler wants to optimize code, it needs to know things like: 'Is this variable used again?' 'Has this expression been computed before?' 'Could this pointer be null here?' Answering these questions requires understanding how data flows through the program — which assignments reach which uses, which variables are live at which points.

## Formal Definition / Statement

A data flow analysis is defined by:
1. **A set of data flow facts** (e.g., "definition d reaches here", "expression e is available")
2. **Transfer functions** for each statement: `OUT(s) = gen(s) ∪ (IN(s) - kill(s))` (forward) or `IN(s) = gen(s) ∪ (OUT(s) - kill(s))` (backward)
3. **Meet/join operators** at confluence points:
   - **May** analyses use ∪ (union) — fact holds if it holds on *any* path
   - **Must** analyses use ∩ (intersection) — fact holds only if it holds on *all* paths
4. **Direction**: forward (IN→OUT along CFG edges) or backward (OUT→IN against CFG edges)
5. **Iteration**: initialise, then repeatedly apply equations until fixed point

**Framework:**
- Control Flow Graph: nodes = basic blocks, edges = control flow transfers
- For each program point, compute a 'fact' (set of properties)
- Facts propagate along edges, transformed by each block

**Classic analyses:**

1. **Reaching Definitions** (forward, may): Which definitions can reach each point?
   - gen(n): definitions created in block n
   - kill(n): definitions killed (overwritten) in block n
   - IN[n] = ∪ OUT[p] for predecessors p
   - OUT[n] = gen[n] ∪ (IN[n] - kill[n])

2. **Available Expressions** (forward, must): Which expressions have been computed and not invalidated?
   - Used for common subexpression elimination

3. **Liveness** (backward, may): Which variables are live (will be used before being redefined)?
   - Used for register allocation, dead code elimination

4. **Very Busy Expressions** (backward, must): Which expressions are evaluated on all paths?

## Key Properties

- Every data flow analysis can be classified along two axes: **direction** (forward/backward) and **kind** (may/must)
- The four classic analyses form a 2×2 matrix: [[reaching-definitions]] (forward, may), [[available-expressions]] (forward, must), [[live-variable-analysis]] (backward, may), [[very-busy-expressions]] (backward, must)
- Convergence is guaranteed when the fact space is a finite lattice and transfer functions are monotone
- Optimal iteration order: depth-first (topological) for forward analyses, reverse depth-first for backward analyses
- The analysis is **safe** (conservative): it over-approximates may-facts and under-approximates must-facts
- Sound: never misses a true fact (may analysis may include false positives)
- Terminates: guaranteed for finite-height lattices (may need widening for infinite-height)
- Polynomial time: O(N × W) where N = number of nodes, W = lattice width
- Path-insensitive: doesn't distinguish between paths (imprecise but efficient)
- Flow-sensitive: respects control flow order (more precise than flow-insensitive)
- Context-insensitive: doesn't distinguish call sites (less precise than context-sensitive)

## Worked Example

**Example 1: Reaching definitions**
```
A: x := 8; y := x; z := 0;
B: while y > -1 do
C:   x := x / y;
D:   y := y - 2;
E:   z := 5;
```

For [[reaching-definitions]], at point B the IN set contains definitions from A (xA, yA, zA) plus any from the loop body. The gen/kill sets for each block determine what flows through.

**Example 2: Liveness analysis**
```
1: a = 3
2: b = 5
3: c = a + b
4: a = 4
5: if a > 0 goto 3
6: return c
```

Backward iteration (variables live at each point):
- After 6: {c} (c is used in return)
- After 5: {a, c} (a used in condition, c from back edge)
- After 4: {a, c} (a used in condition at 5)
- After 3: {a, b, c} (a,b used in computation at 3; c assigned but also live from back edge)
- After 2: {a, b} (b used at 3)
- After 1: {a} (a used at 3)

Result: Variable 'a' assigned at line 1 is live through line 3 (used at 3). Assignment at line 4 makes line 1's 'a' dead after line 4. Dead code elimination can remove assignments to dead variables.

## Common Pitfalls

- Confusing **may** vs **must**: may-facts use union at joins (optimistic), must-facts use intersection (pessimistic)
- Forgetting that **forward must** analyses initialise with the **full set** of all facts, while **forward may** analyses initialise with ∅
- Not distinguishing between a def-use *pair* and a def-use *path* (a pair can have multiple paths)
- Assuming convergence order doesn't matter — bad orderings can require more iterations
- **Over-approximation**: May analyses can include false positives (reporting facts that don't actually hold)
- **Path insensitivity**: Can't distinguish 'if (x > 0) use(x); else x = 1;' from a path where x might be uninitialized
- **Scalability**: Whole-program analysis on large codebases can be expensive
- **Precision vs efficiency**: More precise analyses (path-sensitive, context-sensitive) are exponentially more expensive
- **Lattice choice**: The choice of lattice (sets, intervals, polyhedra) determines what facts can be expressed

## Connections

- Foundation for [[reaching-definitions]], [[available-expressions]], [[live-variable-analysis]], [[very-busy-expressions]]
- Uses [[gen-kill-analysis]] to compute local transfer functions
- [[iterative-data-flow-analysis]] is the standard solving algorithm
- [[du-chains-ud-chains]] are built on top of reaching definitions and liveness
- Enables optimisations: [[dead-code-elimination]], [[common-subexpression-elimination]], constant folding
- [[monotone-framework]] — General mathematical framework unifying all dataflow analyses
- [[liveness-analysis]] — Detailed treatment of liveness as a specific dataflow analysis
- [[register-allocation]] — Uses liveness to build interference graphs
- [[abstract-interpretation]] — Dataflow analysis is a specific instance of abstract interpretation

## Open Questions

- How does abstract interpretation formalise the relationship between data flow analyses and semantics?
- What role do [[widening-narrowing]] operators play when the fact space is infinite (e.g., constant propagation)?
- How do we extend data flow analysis to handle pointers and aliasing?
