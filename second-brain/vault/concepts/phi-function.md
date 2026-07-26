---
title: "Phi Function (φ)"
tags:
  - software-analysis
  - ssa
  - intermediate-representation
course: Software Analyse
source_count: 1
status: current
last_updated: 2026-06-19
---

# Phi Function (φ)

## One-line Summary

Pseudo-assignment in SSA form that merges variable definitions from different control flow paths.

## Core Intuition

In [[static-single-assignment]] form, every variable is assigned exactly once. But at control flow merge points, different paths might bring different versions of a variable. The phi function says: "pick the version that corresponds to the path we actually took."

It's not a real operation — it's a **notational device** that makes the data flow explicit. At runtime, the compiler (or hardware) knows which predecessor was taken and selects the corresponding operand.

## Formal Definition

**Phi function syntax**:
```
x₃ = φ(x₁, x₂)
```

At a merge block with predecessors B₁ and B₂:
- The i-th operand of φ corresponds to the i-th predecessor
- `x₃` gets the value of `x₁` if control came from B₁
- `x₃` gets the value of `x₂` if control came from B₂

**Semantics**: Parallel copy at the beginning of the block. All phi functions in a block execute "simultaneously" — they read the old values before any writes.

### Placement Algorithm

1. Compute [[dominance]] frontiers for each node in the [[control-flow-graph]]
2. For each variable `v` defined at node X, insert `v = φ(...)` at every node in DF(X)
3. Iterate: add new definition sites (from phi placements) to the set, recompute DF until fixpoint → **Iterated Dominance Frontier (IDF)**

### Why IDF?

The dominance frontier DF(X) captures "where control flow from X might merge with flow from elsewhere." If `v` is defined at X, then at any merge point in DF(X), we need a phi to reconcile X's definition with other possible definitions.

But placing a phi creates a *new* definition, which might need another phi at a higher merge point. Hence the iteration.

## Key Properties / Complexity

| Property | Detail |
|----------|--------|
| Not a real operation | Resolved by control flow, not executed sequentially |
| Parallel semantics | All φ in a block read before any write |
| Placement via IDF | Iterated dominance frontier ensures all needed φ are placed |
| Operand order | i-th operand corresponds to i-th predecessor |
| Single static assignment | φ counts as a definition — the result is assigned once |
| Minimal SSA | Minimal φ placement = φ only where absolutely necessary |

## Worked Example

### Input program:
```c
x = 1
if (c)
    x = x + 1
else
    x = x + 2
print(x)
```

### Control flow graph:
```
B1: x = 1
    ↓
B2: if (c)
   ↙    ↘
B3:      B4:
x=x+1    x=x+2
   ↘    ↙
B5: print(x)
```

### SSA construction:

**Step 1: Dominance frontiers**
- DF(B3) = {B5} (B3 dominates itself, a predecessor of B5, but doesn't strictly dominate B5)
- DF(B4) = {B5}
- DF(B1) = {} (B1 dominates everything)
- DF(B2) = {} (B2 dominates B3, B4, B5)

**Step 2: Place phi functions**
- `x` is defined at B1, B3, B4
- DF({B1}) = {} → no phi needed for B1's definition
- DF({B3}) = {B5} → place φ at B5
- DF({B4}) = {B5} → place φ at B5 (same block)
- New definitions: B5 now defines x (via φ)
- DF({B5}) = {} → no more phis needed
- **IDF fixpoint reached**

**Step 3: Rename variables**
```
B1: x₁ = 1
B2: if (c)
B3: x₂ = x₁ + 1
B4: x₃ = x₁ + 2
B5: x₄ = φ(x₂, x₃)   // x₂ from B3, x₃ from B4
    print(x₄)
```

### Why φ at B5?
- B5 has two predecessors: B3 and B4
- B3 defines x₂, B4 defines x₃
- At B5, we don't know which path was taken → need φ to pick the right version

## Common Pitfalls

1. **Treating φ as sequential**: `x₄ = φ(x₂, x₃)` is NOT "first assign x₂ to x₄, then overwrite with x₃." It's a parallel copy — only one operand is selected based on control flow.

2. **Wrong operand order**: The i-th operand must correspond to the i-th predecessor. If you swap them, the φ picks the wrong version.

3. **Forgetting IDF iteration**: Placing φ only at immediate dominance frontiers misses φ functions needed at higher merge points. Must iterate until fixpoint.

4. **Phi in non-join blocks**: Phi functions only make sense at blocks with multiple predecessors. Placing a φ in a block with one predecessor is unnecessary.

5. **Confusing φ with conditional assignment**: `x = c ? a : b` is a real operation. `x = φ(a, b)` is a notational device resolved by control flow.

6. **Memory phi functions**: For arrays and heap objects, you need "memory phi" functions that merge entire memory states. This is more complex than scalar φ.

## Connections

- [[static-single-assignment]] — phi functions are the merge mechanism in SSA
- [[dominance]] — dominance frontiers drive phi placement
- [[dominator-tree]] — used in the renaming pass
- [[control-flow-graph]] — phi functions live at merge points in the CFG
- [[data-flow-analysis]] — phi functions make reaching definitions explicit
- [[program-dependence-graph]] — SSA (with φ) makes data dependence edges clear
- [[software-analyse-lecture-8]] — Source lecture: Program Slicing (SSA → dominance frontiers → φ → PDG → slicing)

## Open Questions

1. What is **minimal SSA** vs. **pruned SSA**? (Minimal = fewest φ; pruned = remove dead φ)
2. How do we handle **phi functions for memory** (arrays, structs)? (Load/store SSA)
3. Can phi functions be **eliminated** efficiently when converting back from SSA? (Coalescing)
4. What is the relationship between phi functions and **μ-η forms** in other IRs?
5. How do phi functions interact with **speculative execution** in hardware?
