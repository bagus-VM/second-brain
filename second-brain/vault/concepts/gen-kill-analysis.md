---
title: "Gen/Kill Analysis"
tags: [concept, software-analyse, semester-1, data-flow]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [control-flow-graph]
---

## One-line Summary

Gen and kill sets are the local transfer functions that describe how each statement creates or invalidates data flow facts, forming the building blocks of every data flow equation.

## Core Intuition

Each statement has a *local* effect on the set of facts that hold at a program point. **Gen** (generate) captures facts the statement creates. **Kill** captures facts the statement invalidates. The overall effect is: the output facts are the input facts minus what was killed, plus what was generated.

## Formal Definition / Statement

For a statement `s`:

- **gen(s)**: set of facts *created* by executing s
- **kill(s)**: set of facts *destroyed* by executing s

Transfer function (forward analysis):
```
OUT(s) = gen(s) ∪ (IN(s) - kill(s))
```

Transfer function (backward analysis):
```
IN(s) = gen(s) ∪ (OUT(s) - kill(s))
```

The specific definitions of gen and kill depend on the analysis:
- [[reaching-definitions]]: gen = {v_n | v defined at n}, kill = {v_x | v defined elsewhere}
- [[available-expressions]]: gen = {e | e computed at s}, kill = {e | e contains variable modified at s}
- [[live-variable-analysis]]: gen = {v | v used at s}, kill = {v | v modified at s}
- [[very-busy-expressions]]: gen = {e | e evaluated at s}, kill = {e | e contains variable modified at s}

## Key Properties

- Gen and kill are purely *local* properties — they depend only on the statement itself, not on surrounding context
- For **must** analyses (available expressions, very busy), gen and kill have opposite semantics: gen means "definitely produced", kill means "possibly invalidated"
- The transfer function is always **monotone**: adding facts to IN never removes facts from OUT (set inclusion is preserved)
- Gen/kill sets partition the effect of a statement into what it *creates* and what it *destroys*

## Worked Example

For the statement `x := a + b`:

| Analysis | gen | kill |
|---|---|---|
| Reaching definitions | {x_def} | {x_other} (all other defs of x) |
| Available expressions | {a+b} | {a+b, a*b, ...} (any expr containing x) |
| Live variables | {a, b} | {x} |
| Very busy expressions | {a+b} | {a+b, ...} (any expr containing x) |

## Common Pitfalls

- Forgetting that in reaching definitions, gen includes the *current* definition (tagged with its location)
- In available expressions, killing an expression that *uses* a modified variable (not just the same expression)
- Confusing the direction: in backward analyses, gen/kill swap their intuitive "before/after" meaning

## Connections

- Used by every concrete data flow analysis: [[reaching-definitions]], [[available-expressions]], [[live-variable-analysis]], [[very-busy-expressions]]
- [[data-flow-analysis]] defines the framework; gen/kill provide the instantiation
- [[iterative-data-flow-analysis]] repeatedly applies gen/kill transfer functions

## Open Questions

- How do gen/kill sets generalise to non-set-based domains (e.g., constant propagation with a lattice)?
- Can gen/kill be automatically derived from the semantics of a statement?
