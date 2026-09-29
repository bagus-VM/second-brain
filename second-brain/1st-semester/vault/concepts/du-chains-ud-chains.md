---
title: "DU-Chains and UD-Chains"
tags: [concept, software-analyse, semester-1, data-flow, chains]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [reaching-definitions, live-variable-analysis, control-flow-graph]
---

## One-line Summary

DU-chains (definition-use chains) connect each variable definition to all uses it can reach; UD-chains (use-definition chains) connect each variable use to all definitions that can reach it — the practical data structures derived from reaching definitions and liveness analysis.

## Core Intuition

Data flow analyses tell us *which* facts hold at each point. Chains make this information *actionable* by linking specific definitions to specific uses. A DU-chain answers "where is this value used?" while a UD-chain answers "where did this value come from?" These are essential for optimisations, debugging, and understanding data dependencies.

## Formal Definition / Statement

**DU-chain** for a definition D of variable v:
- The set of all uses U of v such that there exists a **definition-clear path** from D to U
- `DU(D) = { U | there is a path D → ... → U with no redefinition of v }`

**UD-chain** for a use U of variable v:
- The set of all definitions D of v that reach U
- `UD(U) = { D | D reaches U }` — computed directly from [[reaching-definitions]]

**Definition-clear path**: A path from a definition to a use where the variable is not redefined along the path.

## Key Properties / Complexity

- A DU/UD *pair* is a (definition, use) combination with at least one definition-clear path
- A single DU-pair can have *multiple* definition-clear paths
- DU-chains are derived from reaching definitions (forward)
- UD-chains are derived from reaching definitions (or equivalently, from liveness going backward)
- DU-chains are used for: finding all consumers of a definition (for constant propagation, copy propagation)
- UD-chains are used for: finding all producers of a value at a use (for def-use pairs, slicing)

## Worked Example

```java
B1: x = 1;    B2: x = 2;    B3: y = x + 1;
    B4: z > 2?        B5: z = x - 3; x = 4;
                       B6: z = x + 7;
```

DU-chains:
- `DU(x, B1) = {(x, B3), (x, B5)}` — x=1 can reach uses in B3 and B5
- `DU(x, B2) = {(x, B3), (x, B5)}` — x=2 can also reach B3 and B5
- `DU(x, B4) = {(x, B5)}` — x=4 reaches use in B5 only

UD-chains:
- `UD(x, B3) = {(x, B1), (x, B2)}` — both definitions can reach this use
- `UD(x, B5) = {(x, B1), (x, B2), (x, B4)}` — three possible sources
- `UD(x, B6) = {(x, B5)}` — only the most recent definition

## Common Pitfalls

- Confusing DU-pair with DU-path: a pair can have multiple paths
- Forgetting that loops cause definitions from inside the loop to reach back to the loop header
- Not updating chains after program transformations (optimisations invalidate chains)
- Assuming a single definition reaches a use — in general, multiple definitions can reach the same use

## Connections

- Derived from [[reaching-definitions]] (UD-chains directly, DU-chains by inversion)
- Related to [[live-variable-analysis]] (a variable is live at a definition iff it has a non-empty DU-chain)
- [[data-flow-analysis]] provides the framework; chains are the practical output
- Used by [[iterative-data-flow-analysis]] results
- Enables constant propagation, copy propagation, dead code elimination, program slicing

## Open Questions

- How do DU/UD-chains change in SSA (Static Single Assignment) form where each variable has exactly one definition?
- What is the space complexity of storing all DU/UD-chains for large programs?
