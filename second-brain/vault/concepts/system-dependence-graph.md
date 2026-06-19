---
title: "System Dependence Graph (SDG)"
tags:
  - software-analysis
  - interprocedural
  - dependence-graph
  - slicing
course: Software Analyse
status: current
last_updated: 2026-06-19
---

# System Dependence Graph (SDG)

## One-line Summary

Extension of PDG to multiple procedures, enabling interprocedural slicing.

## Core Intuition

A single [[program-dependence-graph]] only covers one procedure. But real programs have many procedures calling each other. The SDG connects the PDGs of all procedures into one global graph, capturing:
- **Parameter passing**: how actual arguments at call sites connect to formal parameters at procedure entry
- **Return values**: how formal return values connect back to actual results
- **Summary edges**: direct dependences that bypass the callee body (for efficiency)

The SDG is the foundation of **interprocedural slicing** — slicing that crosses procedure boundaries.

## Formal Definition

**SDG** = union of extended PDGs for all procedures, plus:

### Extended PDG nodes
Each procedure's PDG is extended with:
- **Formal-in nodes**: one per parameter (represent the parameter's initial value)
- **Formal-out nodes**: one per return value (represent the value returned)
- **Actual-in nodes**: at each call site, one per argument (represent the argument value passed)
- **Actual-out nodes**: at each call site, one per return value (represent the value received)

### Edges
- **Call edges**: Connect actual-in → formal-in and formal-out → actual-out
- **Parameter-in edges**: actual-in → formal-in (pass argument to parameter)
- **Parameter-out edges**: formal-out → actual-out (return value to caller)
- **Call-control edges**: Call site → procedure entry (control dependence)
- **Summary edges**: Direct data dependence from actual-in to actual-out (bypassing the callee)

### Summary Edges

A summary edge connects actual-inᵢ to actual-outⱼ at a call site if there is a dependence path from formal-inᵢ to formal-outⱼ inside the callee. This captures "argument i affects return value j" without traversing the callee body.

### Two-Phase Interprocedural Slicing

**Phase 1 (Upward)**: From the slicing criterion, walk backward through the SDG. When reaching an actual-in node, cross to the corresponding formal-in node (enter the callee). When reaching a formal-out node, cross to the corresponding actual-out node (return to caller).

**Phase 2 (Downward)**: From nodes reached in Phase 1, walk forward. When at a formal-in, cross to actual-in. When at actual-out, cross to formal-out. This phase ensures we capture dependences that flow "down" into callees.

The two phases prevent **unrealizable paths** — paths that don't correspond to any actual call sequence.

## Key Properties

| Property | Detail |
|----------|--------|
| Interprocedural | Captures dependences across procedure boundaries |
| Summary edges | Prevent exponential blowup from call-string enumeration |
| Two-phase algorithm | Ensures only realizable paths are considered |
| Context sensitivity | Summary edges provide call-site sensitivity |
| Compositional | Each procedure's PDG can be built independently |
| Scalability | Linear in program size (with summary edges) |

## Worked Example

### Program:
```c
// Procedure: add
int add(int a, int b) {
    return a + b;
}

// Caller: main
void main() {
    x = input()
    y = 5
    z = add(x, y)
    print(z)
}
```

### SDG structure:

**Procedure `add` PDG**:
- Formal-in: `a_in`, `b_in`
- Statement: `ret = a + b`
- Formal-out: `ret_out`
- Edges: `a_in →ᵈ ret`, `b_in →ᵈ ret`, `ret →ᵈ ret_out`

**Procedure `main` PDG**:
- Statements: `x = input()`, `y = 5`, `z = add(x, y)`, `print(z)`
- Actual-in at call: `x_actual_in`, `y_actual_in`
- Actual-out at call: `z_actual_out`
- Edges: 
  - `x = input() →ᵈ x_actual_in`
  - `y = 5 →ᵈ y_actual_in`
  - `z_actual_out →ᵈ print(z)`

**Call edges**:
- `x_actual_in → formal a_in`
- `y_actual_in → formal b_in`
- `formal ret_out → z_actual_out`

**Summary edge**:
- `x_actual_in → z_actual_out` (because `a_in → ret_out` in callee)
- `y_actual_in → z_actual_out` (because `b_in → ret_out` in callee)

### Backward slice of `z` at `print(z)`:
- `print(z) ← z_actual_out` (data)
- `z_actual_out ← x_actual_in` (summary), `z_actual_out ← y_actual_in` (summary)
- `x_actual_in ← x = input()` (data)
- `y_actual_in ← y = 5` (data)

**Slice**: {`x = input()`, `y = 5`, `z = add(x, y)`, `print(z)`} — the whole program.

If `y` were not used in `add`, the summary edge `y_actual_in → z_actual_out` would not exist, and `y = 5` would be excluded.

## Common Pitfalls

1. **Forgetting summary edges**: Without them, interprocedural slicing must traverse every callee body for every call site — exponential blowup.

2. **Unrealizable paths**: A path that goes into a callee but doesn't return, or returns to a different call site, is unrealizable. The two-phase algorithm prevents this.

3. **Aliasing**: If two actual parameters alias the same memory location, the SDG must capture this. Without [[points-to-analysis]], the SDG is unsound.

4. **Recursion**: The SDG can have cycles (recursive calls). Slicing must handle this (typically by computing transitive closure).

5. **Global variables**: Globals create implicit dependences between procedures. They must be represented as additional edges in the SDG.

6. **Phase confusion**: Phase 1 goes "up" (caller → callee entry), Phase 2 goes "down" (callee entry → caller). Mixing them up leads to unsound slices.

## Connections

- [[program-dependence-graph]] — SDG is a collection of extended PDGs
- [[interprocedural-analysis]] — broader context for SDG
- [[program-slicing]] — SDG enables interprocedural slicing
- [[procedure-summaries]] — summary edges are a form of procedure summary
- [[points-to-analysis]] — resolves aliasing for accurate SDG construction
- [[control-flow-graph]] — basis for each procedure's PDG
- [[data-flow-analysis]] — interprocedural data flow feeds SDG edges

## Open Questions

1. How do we handle **higher-order functions** and **callbacks** in the SDG?
2. Can we build **incremental SDGs** that update efficiently when code changes?
3. What is the relationship between SDGs and **call graphs**? (SDG is more precise)
4. How do we slice **object-oriented programs** with virtual dispatch? (Dynamic SDG)
5. Can SDGs capture **information flow** across procedure boundaries for security analysis?
6. How does **modular slicing** differ from whole-program SDG slicing?
