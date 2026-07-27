---
title: "Program Slicing"
tags:
  - software-analysis
  - program-slicing
  - debugging
  - dependence
course: Software Analyse
source_count: 1
status: current
last_updated: 2026-06-19
---


## One-line Summary

Extract the subset of statements that may affect (backward) or be affected by (forward) a variable at a program point.

## Core Intuition

Program slicing answers: "If I only care about variable `v` at statement `s`, what parts of the program matter?" Everything else can be deleted without changing `v`'s value at `s`.

Think of it as **focused program extraction**. A debugger uses backward slicing to show you "here's everything that could have influenced this value." A tester uses forward slicing to find "here's everything this input could affect."

The key insight: **slicing = graph reachability on the [[program-dependence-graph]]**.

## Formal Definition

**Slicing criterion**: C = (s, v) — variable `v` at statement `s`

**Backward slice** BS(C): The set of all statements (and their definitions) that may transitively affect the value of `v` at `s`.

Computation: Start at the use of `v` at `s` in the PDG. Follow all incoming edges (data dependence and control dependence) backwards. Collect all reachable nodes.

**Forward slice** FS(C): The set of all statements whose value may be transitively affected by `v` at `s`.

Computation: Start at the definition of `v` at `s` in the PDG. Follow all outgoing edges forward. Collect all reachable nodes.

**Slice extraction**: Remove all statements not in the slice. The resulting program computes the same value for the slicing criterion.

## Key Properties / Complexity

| Property | Detail |
|----------|--------|
| Correctness | Extracted program preserves the slicing criterion's value |
| Minimality | Not guaranteed — minimal slicing is undecidable |
| Backward ⊆ Program | Always a subset of the original program |
| Composability | Can chain slices (slice of a slice) |
| Interprocedural | Extends to multi-procedure programs via SDG |
| Dynamic variant | More precise for specific inputs |

## Worked Example

### Program:
```c
1: x = input()
2: y = 10
3: if (x > 0)
4:     z = x + 1
5: else
6:     z = x - 1
7: w = y * 2
8: print(z)
```

### Backward slice of `z` at statement 8:
- `z` at 8 ← data dependence from `z` at 4 and `z` at 6
- `z` at 4 ← data dependence from `x` at 1
- `z` at 6 ← data dependence from `x` at 1
- Statements 4 and 6 ← control dependence from statement 3
- Statement 3 ← data dependence from `x` at 1

**Slice**: {1, 3, 4, 5, 6, 8}
**Excluded**: {2, 7} — `y` and `w` don't affect `z`

### Extracted program:
```c
1: x = input()
3: if (x > 0)
4:     z = x + 1
5: else
6:     z = x - 1
8: print(z)
```

### Forward slice of `x` at statement 1:
Everything that `x` affects: {1, 3, 4, 5, 6, 8} — same result in this case.

## Common Pitfalls

1. **Confusing backward and forward**: Backward = "what affects this?" (debugging). Forward = "what does this affect?" (impact analysis).

2. **Assuming slices are minimal**: Slicing is conservative — it includes everything that *may* affect the criterion. The minimal slice (excluding everything that doesn't *actually* affect it) is undecidable.

3. **Ignoring control dependence**: If you only follow data dependence edges, you'll miss the conditional branches that guard the relevant statements. The slice will be unsound.

4. **Forgetting transitive closure**: Slicing is not one step — it's the full transitive reachability. A statement might not directly use `v`, but might define something that `v` depends on.

5. **Aliasing in interprocedural slicing**: Without [[points-to-analysis]], you might miss dependences through pointer parameters.

6. **Treating dynamic slices as static**: Dynamic slices are input-specific. A dynamic slice for input A might not be valid for input B.

## Connections

- [[program-dependence-graph]] — the graph on which slicing is computed
- [[control-dependence]] — one type of edge in the PDG
- [[data-flow-analysis]] — reaching definitions feed data dependence
- [[static-single-assignment]] — SSA makes dependencies explicit for slicing
- [[interprocedural-analysis]] — context for multi-procedure slicing
- [[system-dependence-graph]] — PDG extension for interprocedural slicing
- [[dynamic-slicing]] — input-specific variant
- [[points-to-analysis]] — resolves aliasing for precise slicing
- [[software-analyse-lecture-8]] — Source lecture: Program Slicing (SSA → dominance frontiers → φ → PDG → slicing)

## Open Questions

1. Can we compute **optimal** (smallest) slices? (Undecidable in general, but approximations exist)
2. How does slicing help with **program comprehension** and **reverse engineering**?
3. What is the relationship between slicing and **differential analysis** (what changed between versions)?
4. Can we slice **concurrent programs** soundly? (Thread slicing, happens-before slicing)
5. How do **IDE features** (find all references, refactor) relate to slicing?
6. What is **conditioned slicing**? (Slice parameterized by input conditions)

## Formal Definition / Statement

*To be filled.*
