---
title: "Static Single Assignment (SSA) Form"
tags:
  - software-analysis
  - intermediate-representation
  - ssa
  - optimization
course: Software Analyse
status: current
last_updated: 2026-06-19
---

# Static Single Assignment (SSA) Form

## One-line Summary

Intermediate representation where each variable is assigned exactly once, making data dependencies explicit.

## Core Intuition

In normal code, a variable like `x` can be assigned many times, making it hard to track which definition reaches which use. SSA solves this by giving every assignment a **unique name** — `x₁`, `x₂`, `x₃` — so there's never ambiguity about which definition you're talking about.

At control flow merge points, **phi functions** (φ) reconcile the different versions: "if we came from the then-branch, use x₂; if from the else-branch, use x₃."

## Formal Definition

A program is in **Static Single Assignment form** if every variable is defined (assigned) at exactly one point in the program text. At control flow join points, **phi functions** merge definitions:

```
x₃ = φ(x₁, x₂)
```

This means: "x₃ gets the value of x₁ if control came from predecessor 1, or x₂ if control came from predecessor 2."

### Construction Algorithm

1. **Compute [[dominance]] frontiers** for each node in the [[control-flow-graph]]
2. **Place phi functions**: For each variable `v` defined at node `X`, insert `v = φ(...)` at every node in DF(X). Iterate: add new definition sites to the set and recompute DF until fixpoint → **Iterated Dominance Frontier (IDF)**
3. **Rename variables**: Walk the dominator tree top-down. Each definition gets a fresh subscript. Phi operands use the current version for the corresponding predecessor.

### Dominance Frontier

DF(X) = {Y | X dominates a predecessor of Y, but X does not strictly dominate Y}

Intuitively: "Y is a point where control flow from X might merge with flow from somewhere else."

## Key Properties

| Property | Detail |
|----------|--------|
| Single definition | Each variable version has exactly one assignment |
| Explicit dependencies | Use-def chains are immediate (no analysis needed) |
| Sparse representation | Only track variables at points where they're defined/used |
| Reaching definitions trivial | The reaching definition of xᵢ at any use is simply xᵢ's unique definition |
| Phi functions are not real | They represent parallel copies resolved by control flow |
| Construction is linear | O(V + E) for well-structured programs with good IDF computation |

## Worked Example

### Input program:
```c
x = 1
if (c)
    x = x + 1
else
    x = x + 2
y = x
```

### SSA form:
```
x₁ = 1
if (c)
    x₂ = x₁ + 1
else
    x₃ = x₁ + 2
x₄ = φ(x₂, x₃)    // merge point
y₁ = x₄
```

### Why φ at the merge?
- The merge block is in DF(then-block) and DF(else-block)
- `x` is defined in both branches → need φ to pick the right version
- `x₁` dominates the merge (it's defined before the branch), but so do x₂ and x₃ via their respective paths

### Dominance frontier computation:
- DF(then-block) = {merge} (then-block dominates itself, a predecessor of merge, but doesn't strictly dominate merge)
- DF(else-block) = {merge}
- IDF({x definition in then, x definition in else}) = {merge} → place φ

## Common Pitfalls

1. **Treating φ as a real operation**: Phi functions don't generate code. They're resolved by the control flow — the runtime "knows" which predecessor was taken.

2. **Forgetting IDF iteration**: If you only place φ at immediate dominance frontiers, you'll miss φ functions needed at higher merge points. Must iterate until no new φ placements occur.

3. **Off-by-one in renaming**: When walking the dominator tree, you must update the "current version" stack as you enter/exit blocks. Forgetting to pop leads to wrong versions.

4. **Phi operands order matters**: The i-th operand of φ corresponds to the i-th predecessor of the block. Getting the order wrong silently corrupts the SSA form.

5. **Memory/arrays in SSA**: SSA is clean for scalar variables. Arrays and heap objects need special treatment (e.g., "memory versions" or field-sensitive SSA).

## Connections

- [[control-flow-graph]] — the graph on which dominance and DF are computed
- [[dominance]] — dominance frontiers drive phi placement
- [[dominator-tree]] — used for the renaming pass
- [[phi-function]] — the merge mechanism in SSA
- [[data-flow-analysis]] — SSA makes reaching definitions trivial; conversely, reaching definitions can construct SSA
- [[reaching-definitions]] — in SSA, the reaching definition is always unique
- [[program-dependence-graph]] — SSA makes data dependence edges explicit
- [[basic-block]] — granularity at which SSA is typically constructed

## Open Questions

1. How do compilers handle **SSA for memory** (arrays, structs, heap)? (Load/store SSA, memory SSA)
2. Is there an **optimal** SSA form (minimal number of φ functions)? (Minimal SSA vs. pruned SSA)
3. How does SSA interact with **register allocation**? (Coalescing, live range splitting)
4. Can SSA be extended to **concurrent programs** with shared memory?
5. What is the relationship between SSA and **continuation-passing style** (CPS)?
