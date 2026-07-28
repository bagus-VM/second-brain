---
title: "Dead Code Elimination"
tags: [concept, software-analyse, semester-1]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-22
prerequisites: ["[[live-variable-analysis]]"]
---
## One-line Summary
Dead code elimination removes statements that can never affect the program's output — code that computes values nobody uses or branches nobody can reach.

## Core Intuition
Programs accumulate cruft. Variables are assigned but never read. Code follows branches that can never be taken. Functions are defined but never called. Dead code elimination (DCE) cleans this up. The key insight is that a variable assignment is "dead" if the variable is not **live** at that point — meaning no future path will read it before redefining it. This is exactly what [[live-variable-analysis]] computes. DCE is not just cosmetic: dead code wastes CPU cycles, inflates binary size, and can obscure bugs (dead code that *looks* like it does something important confuses maintainers).

## Formal Definition / Statement

**Dead code elimination** removes statements that cannot affect the program's observable output.

**Types of dead code**:

1. **Dead assignments**: An assignment `x = expr` is dead if x is not in OUT(b) for the block b containing the assignment (x is not live after the assignment). This means no future use will read the value before x is redefined.

2. **Unreachable code**: Code that cannot be reached from the program entry point on any execution path. Detected via control flow analysis (reachability on the [[control-flow-graph]]).

3. **Partially dead assignments**: An assignment to x is partially dead if it is dead on some paths but live on others. Can be optimized with more sophisticated analysis.

**Algorithm for dead assignment elimination**:
1. Run [[live-variable-analysis]] (backward, may) on the [[control-flow-graph]]
2. For each statement `x = expr`:
   - If x ∉ OUT(stmt): the assignment is dead → remove it
3. Repeat until no more changes (removing a definition may make earlier definitions dead)

**Unreachable code elimination**:
1. Starting from the entry node, mark all reachable nodes via BFS/DFS
2. Remove all unmarked nodes and their edges from the CFG

## Key Properties / Complexity

- **Safe**: Removing dead code never changes program behaviour (by definition, it has no effect)
- **Backward analysis dependency**: requires [[live-variable-analysis]] (may analysis, union at joins)
- **Iterative**: Removing one dead assignment may expose others — may require multiple passes
- Dead assignment elimination and unreachable code elimination are independent optimizations
- DCE is idempotent: applying it twice yields the same result
- In SSA form, DCE is trivial: any instruction whose result has no uses is dead
- DCE can interact with [[common-subexpression-elimination]]: CSE may create dead assignments

## Worked Example

```java
// Before DCE
x = 5;          // dead: x is immediately overwritten
y = a + b;      // dead: y is never read
x = 10;
z = x + 1;      // live: z is used in return
return z;
```

Live-variable analysis (backward pass):
- After `return z`: OUT = {} (exit)
- Before `return z`: IN = {z}
- Before `z = x + 1`: IN = {x} (z is killed here, x is needed)
- Before `x = 10`: IN = {} (x is killed here, nothing needed from before)
- Before `y = a + b`: IN = {} (y is killed, a and b not needed)
- Before `x = 5`: IN = {} (x is killed, not needed)

Result: `x = 5` and `y = a + b` are dead assignments.

```java
// After DCE
x = 10;
z = x + 1;
return z;
```

For unreachable code:
```java
if (false) {          // compiler detects this is always false
    x = expensive();  // unreachable code → remove entirely
}
```

## Common Pitfalls

- DCE requires [[live-variable-analysis]] — confusing liveness with reaching definitions gives wrong results
- Not iterating: removing one dead definition can make another dead (transitive effect)
- Side effects: `x = foo()` is not dead if `foo()` has side effects (I/O, state changes). Only pure assignments can be removed.
- In languages with exceptions, an "unused" assignment may have a side effect that throws — must be careful
- Unreachable code elimination and dead assignment elimination are separate passes — don't conflate them
- DCE can change the behaviour of debugging tools (breakpoints on removed code)

## Connections

- [[live-variable-analysis]] — the data flow analysis that identifies dead assignments (a variable is dead iff not live)
- [[data-flow-analysis]] — DCE is a direct application of backward may-analysis
- [[common-subexpression-elimination]] — CSE can create dead assignments that DCE cleans up
- [[control-flow-graph]] — unreachable code elimination operates on the CFG structure
- [[iterative-data-flow-analysis]] — the algorithm that computes liveness to fixed point
- [[reaching-definitions]] — complementary forward analysis (DCE uses backward liveness instead)
- [[software-analyse-lecture-5]] — lecture where DCE is introduced as an application of data flow analysis

## Open Questions

- How does DCE interact with exception handling and finally blocks?
- What is the relationship between DCE and partial redundancy elimination (PRE)?
- How do modern compilers implement DCE in SSA form (where it becomes trivial)?
