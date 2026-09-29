---
title: "Lecture 8: Program Slicing"
tags:
  - software-analysis
  - program-slicing
  - ssa
  - pdg
  - dependence-graph
course: Software Analyse
status: current
last_updated: 2026-06-19
---

# Lecture 8: Program Slicing

## One-line Summary

Program slicing extracts the subset of program statements that may affect (backward slice) or be affected by (forward slice) a variable at a given program point, using Program Dependence Graphs built on SSA form.

## Core Intuition

Program slicing answers the question: "Which statements are relevant to this variable at this point?" It's like asking "if I only cared about the value of `x` at line 10, what could I delete without changing that value?" The answer is everything *not* in the backward slice of `x` at line 10.

The key insight is that **slicing = graph reachability**. Build a graph where edges represent "may affect" relationships, then the slice is just everything reachable from your query point.

## Formal Definition

### Static Single Assignment (SSA) Form

In SSA, every variable is assigned **exactly once**. At merge points (where control flow joins), **phi functions** (φ) merge different versions:

```
x₁ = 5
if (cond)
    x₂ = x₁ + 1
else
    x₃ = x₁ + 2
x₄ = φ(x₂, x₃)  // at merge point
```

### Computing SSA

1. **Compute dominance frontiers**: DF(X) = {Y | X dominates a predecessor of Y, but X does not strictly dominate Y}
2. **Place phi functions**: For each variable `v` defined at node X, insert `v = φ(...)` at every node in DF(X). Then iterate: DF(X ∪ {phi nodes}) until fixpoint → **Iterated Dominance Frontier (IDF)**
3. **Rename variables**: Walk the dominator tree, giving each definition a fresh version number; phi operands pick up the current version for that predecessor

### Program Dependence Graph (PDG)

- **Nodes**: Same as [[control-flow-graph]] (one per statement/basic block)
- **Edges**:
  - **Control dependence**: `s₁ →ᶜ s₂` if `s₂` executes conditionally on `s₁`
  - **Data dependence**: `s₁ →ᵈ s₂` if `s₁` defines a value used by `s₂` (reaching definitions)

### Slicing

- **Backward slice** of variable `v` at statement `s`: all nodes from which there is a path to the use of `v` at `s` in the PDG
- **Forward slice** of variable `v` at statement `s`: all nodes reachable from the definition of `v` at `s` in the PDG

### Slice Extraction

Remove all statements not in the slice. The remaining program computes the same value for the slicing criterion.

### Interprocedural Slicing — System Dependence Graph (SDG)

For multi-procedure programs, extend each procedure's PDG:
- **Formal-in / Formal-out nodes**: represent parameters and return values at procedure entry
- **Actual-in / Actual-out nodes**: represent arguments and results at call sites
- **Call edges**: connect actual nodes to formal nodes
- **Summary edges**: direct dependence from formal-in to formal-out (bypassing the callee body)

**Two-phase algorithm**:
1. Phase 1: Walk upward through call graph (from caller to callee entry)
2. Phase 2: Walk downward, respecting call-site context

### Dynamic Slicing

Slice computed for a **specific input** and **specific execution trace**. Only includes statements that *actually* affected the variable in that run — more precise than static slicing, but requires trace information.

## Key Properties

| Property | Detail |
|----------|--------|
| SSA uniqueness | Each variable has exactly one definition (except φ) |
| IDF fixpoint | Phi placement terminates because CFG is finite |
| PDG completeness | Captures all control and data dependences |
| Slice correctness | Extracted program preserves the slicing criterion |
| Interprocedural precision | Summary edges prevent "call-string" explosion |
| Dynamic precision | Fewer false positives than static slice |

## Worked Example

### Backward Slice Example

```c
// Program:
1: x = input()
2: y = 5
3: if (x > 0)
4:     z = x + y
5: else
6:     z = y * 2
7: print(z)
```

**Slicing criterion**: variable `z` at statement 7

**Backward slice**: {1, 3, 4, 5, 6, 7}
- Statement 2 (`y = 5`) is NOT in the slice because `y` is overwritten in both branches before `z` uses it... wait, actually `y` IS used in both branches. Let me re-check.

Actually: `z = x + y` uses both `x` and `y`. `z = y * 2` uses `y`. So `y` is needed. The slice is {1, 2, 3, 4, 5, 6, 7} — the whole program.

**Better example** — remove statement 2:
```c
1: x = input()
2: y = 5         // dead if not used
3: if (x > 0)
4:     z = x
5: else
6:     z = x * 2
7: print(z)
```

Slice of `z` at 7: {1, 3, 4, 5, 6, 7} — statement 2 is excluded.

### SSA Construction Example

```c
x = 1
if (c)
    x = x + 1
else
    x = x + 2
print(x)
```

**SSA form**:
```
x₁ = 1
if (c)
    x₂ = x₁ + 1
else
    x₃ = x₁ + 2
x₄ = φ(x₂, x₃)
print(x₄)
```

**Dominance frontier**: The merge point after the if/else is in DF of both the `then` and `else` blocks → place φ there.

## Common Pitfalls

1. **Forgetting IDF iteration**: Placing φ only at immediate dominance frontiers misses φ functions needed at merge points further up. Must iterate until fixpoint.

2. **Confusing control vs. data dependence**: Control dependence = "does this statement execute?" Data dependence = "does this definition reach this use?" Both are needed for correct slicing.

3. **Ignoring aliasing in interprocedural slicing**: Without [[points-to-analysis]], you can't know which actual parameters correspond to which formal parameters when pointers are involved.

4. **Static vs. dynamic confusion**: Static slicing considers ALL possible inputs (conservative). Dynamic slicing is for ONE specific execution (precise but requires trace).

5. **Phi functions are not real operations**: They represent parallel copy at merge points. Don't treat them as sequential assignments.

6. **Summary edges are essential**: Without them, interprocedural slicing is exponential (must consider all call paths).

## Connections
- [[control-flow-graph]] — basis for PDG nodes
- [[dominance]] — needed for SSA construction (dominance frontiers)
- [[dominator-tree]] — used in variable renaming pass
- [[control-dependence]] — one type of PDG edge
- [[data-flow-analysis]] — reaching definitions feed data dependence edges
- [[interprocedural-analysis]] — context for SDG and interprocedural slicing
- [[points-to-analysis]] — resolves aliasing for precise interprocedural slicing
- [[basic-block]] — granularity of PDG nodes
- [[reaching-definitions]] — underpins data dependence computation
- [[software-analyse-lecture-10]] — symbolic execution and program slicing are complementary: slicing asks "what affects X?", symbolic asks "what inputs reach X?"
- [[static-single-assignment]] — SSA form underlies the PDG construction described here
- [[phi-function]] — merge-point pseudo-assignments that define SSA's structure
- [[program-dependence-graph]] — the central data structure of this lecture
- [[program-slicing]] — slicing = reachability in the PDG, the lecture's main result
- [[system-dependence-graph]] — interprocedural extension of PDG (Section "Interprocedural Slicing")
- [[dynamic-slicing]] — trace-based slice variant, complements the static slice

## Open Questions

1. How does slicing interact with **concurrent programs**? (Thread slicing, race-condition-aware slicing)
2. Can we compute **optimal** (smallest) slices? (The problem is undecidable in general)
3. How do modern compilers use SSA-based slicing for **dead code elimination**?
4. What is the relationship between **abstract interpretation** and slicing precision?
5. How does **incremental slicing** work when the program changes?
6. Can we combine **static and dynamic slicing** for best of both worlds? (Conditioned slicing)

## Lecture Metadata

- **Course**: Software Analyse
- **Lecture number**: 8 (final lecture)
- **Pages**: 167
- **Key themes**: SSA, dominance frontiers, PDG, backward/forward slicing, interprocedural slicing, dynamic slicing
- **Prerequisites**: [[control-flow-graph]], [[dominance]], [[data-flow-analysis]], [[interprocedural-analysis]]
