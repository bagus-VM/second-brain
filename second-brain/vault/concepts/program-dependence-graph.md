---
title: "Program Dependence Graph (PDG)"
tags:
  - software-analysis
  - dependence-graph
  - pdg
  - slicing
course: Software Analyse
source_count: 1
status: current
last_updated: 2026-06-19
---


## One-line Summary

Graph combining control and data dependence edges over CFG nodes — the complete dependence map of a program.

## Core Intuition

The PDG answers two questions for every pair of statements:
1. **Control dependence**: "Does statement B execute only because statement A's condition was true?"
2. **Data dependence**: "Does statement B use a value defined by statement A?"

Together, these edges capture **everything** that matters for [[program-slicing]]. If there's no path in the PDG from A to B, then A cannot affect B — and you can safely delete A if you only care about B.

## Formal Definition

**PDG** = (N, E_c, E_d) where:
- **N**: Nodes = statements (or basic blocks) from the [[control-flow-graph]]
- **E_c**: Control dependence edges — `s₁ →ᶜ s₂` iff `s₂` is control-dependent on `s₁`
- **E_d**: Data dependence edges — `s₁ →ᵈ s₂` iff `s₁` defines a value that reaches `s₂` (reaching definitions)

### Control Dependence

`s₂` is control-dependent on `s₁` if:
1. There exists a path from `s₁` to `s₂` such that `s₂` is post-dominated by the target of the branch at `s₁`
2. `s₁` can affect whether `s₂` executes

Intuitively: "If I change the outcome of the branch at `s₁`, does `s₂` sometimes execute and sometimes not?"

### Data Dependence

`s₁ →ᵈ s₂` if:
1. `s₁` defines a variable `v`
2. `s₂` uses `v`
3. There is an execution path from `s₁` to `s₂` along which `v` is not redefined (reaching definition)

### Slicing = Reachability

- **Backward slice** of `v` at `s`: all nodes from which there is a path to the use of `v` at `s`
- **Forward slice** of `v` at `s`: all nodes reachable from the definition of `v` at `s`

## Key Properties / Complexity

| Property | Detail |
|----------|--------|
| Completeness | Captures all control and data dependences |
| Slicing equivalence | Slice = graph reachability on PDG |
| Single-entry | Typically has a unique entry node (START) |
| Transitive closure | Dependences are transitive (path = dependence chain) |
| Interprocedural extension | Becomes [[system-dependence-graph]] for multi-procedure programs |
| SSA connection | [[static-single-assignment]] makes data dependence edges explicit |

## Worked Example

### Program:
```c
1: x = input()
2: y = 5
3: if (x > 0)
4:     z = x + y
5: else
6:     z = y * 2
7: print(z)
```

### PDG edges:

**Control dependence** (from statement 3):
- 3 →ᶜ 4 (then-branch)
- 3 →ᶜ 6 (else-branch)

**Data dependence**:
- 1 →ᵈ 3 (x used in condition)
- 1 →ᵈ 4 (x used in x + y)
- 2 →ᵈ 4 (y used in x + y)
- 2 →ᵈ 6 (y used in y * 2)
- 4 →ᵈ 7 (z used in print)
- 6 →ᵈ 7 (z used in print)

### Backward slice of `z` at 7:
Start at 7, follow edges backward:
- 7 ← 4 (data), 7 ← 6 (data)
- 4 ← 1 (data), 4 ← 2 (data), 4 ← 3 (control)
- 6 ← 2 (data), 6 ← 3 (control)
- 3 ← 1 (data)

**Slice**: {1, 2, 3, 4, 6, 7} — the whole program in this case.

### If we change the program:
```c
1: x = input()
2: y = 5
3: if (x > 0)
4:     z = x
5: else
6:     z = x * 2
7: print(z)
```

Now `y` is not used in either branch. PDG edges from 2 go nowhere useful.

**Backward slice of `z` at 7**: {1, 3, 4, 6, 7} — statement 2 is excluded.

## Common Pitfalls

1. **Confusing control and data dependence**: Control = "does it execute?" Data = "does it compute the right value?" Both are needed for sound slicing.

2. **Missing transitive dependences**: If A →ᵈ B and B →ᵈ C, then A affects C. Slicing must compute the full transitive closure.

3. **Ignoring the START node**: The entry node has control dependence edges to all statements that are not unconditionally executed. Forgetting it leads to unsound slices.

4. **Intraprocedural limitation**: A single PDG only covers one procedure. For multi-procedure programs, you need a [[system-dependence-graph]].

5. **Aliasing**: Without [[points-to-analysis]], you can't build accurate data dependence edges for pointer-based programs.

6. **Granularity**: PDG nodes can be statements, basic blocks, or even individual operations. The choice affects precision and size.

## Connections

- [[control-flow-graph]] — basis for PDG nodes
- [[control-dependence]] — one type of PDG edge
- [[data-flow-analysis]] — reaching definitions feed data dependence edges
- [[program-slicing]] — slicing = reachability on PDG
- [[system-dependence-graph]] — interprocedural extension
- [[static-single-assignment]] — makes data dependence explicit
- [[dominance]] — used to compute control dependence
- [[reaching-definitions]] — underpins data dependence
- [[software-analyse-lecture-8]] — Source lecture: Program Slicing (SSA → dominance frontiers → φ → PDG → slicing)

## Open Questions

1. How do we handle **memory and pointers** in the PDG? (Field-sensitive, context-sensitive)
2. Can we build **incremental PDGs** that update efficiently when the program changes?
3. What is the relationship between PDGs and **program dependency networks** in machine learning?
4. How do we visualize large PDGs effectively? (Graph layout, abstraction)
5. Can PDGs capture **information flow** for security analysis? (Tainted data, declassification)

## Formal Definition / Statement

*To be filled.*
