---
title: "Iterative Data Flow Analysis"
tags: [concept, software-analyse, semester-1, data-flow, algorithm]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [control-flow-graph, gen-kill-analysis]
---

## One-line Summary

Iterative data flow analysis is the standard worklist algorithm that solves data flow equations by repeatedly recalculating IN/OUT sets until a fixed point is reached, handling loops and complex control flow without path enumeration.

## Core Intuition

Enumerating all paths through a program is exponential (even without loops). Instead, we assign IN/OUT sets to each basic block, initialise them, and iteratively apply the data flow equations. Whenever a set changes, we add the block's neighbours to a worklist. When the worklist is empty, we've reached a fixed point — the solution is sound and no further iterations will change anything.

## Formal Definition / Statement

**Algorithm** (general template):

```
for all n in nodes:
    IN(n)  = initial value    // ∅ for may, AllFacts for must
    OUT(n) = initial value

worklist = all nodes
while worklist not empty:
    n = pick node from worklist
    oldOUT = OUT(n)
    
    // Apply transfer function:
    IN(n)  = ∪ OUT(m), m ∈ pred(n)         // or succ(n) for backward
    OUT(n) = gen(n) ∪ (IN(n) - kill(n))    // or IN/OUT swapped for backward
    
    if OUT(n) ≠ oldOUT:
        worklist += successors(n)           // or predecessors for backward
```

**Convergence**: Guaranteed when:
1. The fact space is a finite lattice
2. Transfer functions are monotone
3. The meet/join operator is distributive (for precision)

## Key Properties / Complexity

- **Termination**: Guaranteed in at most O(N × |facts|) iterations, where N = number of nodes
- **Precision**: Result is the *least fixed point* (for may analyses) or *greatest fixed point* (for must analyses)
- **Optimal ordering**: Depth-first (topological) for forward analyses, reverse depth-first for backward analyses minimises iterations
- **Worklist vs. round-robin**: Worklist is more efficient — only reprocesses blocks whose inputs changed
- The algorithm generalises to all four classic analyses by changing direction and kind

## Worked Example

Reaching definitions on the GCD loop:

```
Iteration 1:
  A: OUT = {xA, yA, tmpA}      → add B to worklist
  B: IN  = {xA, yA, tmpA}      → add C to worklist
  C: IN  = {xA, yA, tmpA}      → OUT = {xC, yC, tmpC} → add D
  D: IN  = {xA, yA, tmpA}      → OUT = {xA, yA, tmpA} (no change for x, but...)
  E: IN  = {xA, yA, tmpA}      → OUT = {xA, tmpA, yE}

Iteration 2:
  B: IN  = {xA, yA, tmpA, xC, yC, tmpC}  (new facts from loop back-edge)
  ... continues until no changes ...
```

## Common Pitfalls

- Initialising with the wrong value: may analyses start with ∅, must analyses start with AllFacts
- Using a fixed traversal order instead of a worklist — wastes iterations on unchanged blocks
- Forgetting to add *successors* (forward) or *predecessors* (backward) to the worklist
- Not handling the entry/exit nodes correctly (they have special initialisation)
- Assuming one iteration is enough — loops typically require at least two iterations

## Connections

- Solves the equations defined by [[data-flow-analysis]]
- Uses [[gen-kill-analysis]] transfer functions at each step
- Produces the fixed-point solutions used by [[reaching-definitions]], [[available-expressions]], [[live-variable-analysis]], [[very-busy-expressions]]
- Results feed into [[du-chains-ud-chains]]
- The [[control-flow-graph]] determines the iteration order and neighbour relationships

## Open Questions

- How does the chaotic iteration strategy (choosing which node to process next) affect convergence speed?
- What is the connection between iterative data flow analysis and abstract interpretation's Kleene iteration?
- How do widening/narrowing operators modify the basic iterative algorithm for infinite lattices?
