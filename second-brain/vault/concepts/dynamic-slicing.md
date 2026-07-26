---
title: "Dynamic Slicing"
tags:
  - software-analysis
  - program-slicing
  - dynamic-analysis
  - debugging
course: Software Analyse
source_count: 1
status: current
last_updated: 2026-06-19
---

# Dynamic Slicing

## One-line Summary

Slice computed for a specific input and execution trace, capturing only statements that actually affected a variable at a point.

## Core Intuition

Static slicing is conservative: it includes everything that *might* affect a variable across *all possible inputs*. Dynamic slicing is precise: it includes only what *actually did* affect the variable in *one specific execution*.

Think of it this way: if you're debugging a crash and you know the exact input that caused it, you don't care about code paths that weren't taken. Dynamic slicing gives you the minimal set of statements that contributed to the bug *for that input*.

## Formal Definition

**Dynamic slicing criterion**: C = (s, v, I) — variable `v` at statement `s` for input `I`

**Dynamic backward slice** DBS(C): The set of statements that actually affected the value of `v` at `s` during the execution of the program on input `I`.

### Computation

1. **Execute** the program on input `I$, recording the execution trace (sequence of executed statements and their data flow)
2. **Build a dynamic dependence graph**: Like a PDG, but only include edges that were actually traversed in this execution
3. **Compute reachability**: Backward slice = all nodes from which there is a path to the use of `v` at $s$ in the dynamic dependence graph

### Dynamic Dependence Graph

- **Nodes**: Executed statement instances (a statement executed twice = two nodes)
- **Edges**: 
  - Dynamic data dependence: definition at instance i reaches use at instance j in this trace
  - Dynamic control dependence: instance j was executed because of the branch at instance i in this trace

## Key Properties / Complexity

| Property | Detail |
|----------|--------|
| Precision | More precise than static slicing (fewer false positives) |
| Input-specific | Valid only for the specific input used |
| Trace required | Requires execution trace (memory and time overhead) |
| Soundness | Sound for the specific input (not for all inputs) |
| Minimality | Closer to minimal than static slice, but still not guaranteed minimal |
| Non-monotonic | Adding more inputs doesn't necessarily make the slice larger |

## Worked Example

### Program:
```c
1: x = input()
2: y = 10
3: if (x > 0)
4:     z = x + y
5: else
6:     z = x - y
7: w = z * 2
8: print(w)
```

### Input: x = 5

**Execution trace**: 1, 2, 3 (true), 4, 7, 8

**Dynamic dependence graph** (for this trace):
- 1 →ᵈ 3 (x used in condition)
- 1 →ᵈ 4 (x used in x + y)
- 2 →ᵈ 4 (y used in x + y)
- 4 →ᵈ 7 (z used in z * 2)
- 7 →ᵈ 8 (w used in print)

Note: Statement 6 is NOT in the trace (the else-branch was not taken).

**Dynamic backward slice of `w` at 8**: {1, 2, 4, 7, 8}

**Static backward slice of `w` at 8**: {1, 2, 3, 4, 5, 6, 7, 8} — the whole program

**Difference**: Dynamic slice excludes statements 3, 5, 6 because they weren't executed or weren't relevant for this input.

### Input: x = -3

**Execution trace**: 1, 2, 3 (false), 6, 7, 8

**Dynamic backward slice of `w` at 8**: {1, 2, 6, 7, 8}

Now statement 4 is excluded (then-branch not taken), and statement 6 is included.

## Common Pitfalls

1. **Confusing dynamic with static**: Dynamic slices are input-specific. A dynamic slice for input A is not valid for input B.

2. **Trace explosion**: Execution traces can be huge (millions of statements). Storing and analysing them is expensive.

3. **Instance vs. statement**: Dynamic slicing tracks statement *instances* (a statement executed twice = two nodes). Forgetting this leads to incorrect slices.

4. **Assuming dynamic slices are minimal**: They're more precise than static slices, but still not guaranteed minimal. Some statements in the dynamic slice might not have *actually* changed the value.

5. **Ignoring loops**: In a loop, a statement might be executed many times. Each iteration is a separate instance in the dynamic dependence graph.

6. **Side effects**: If the program has side effects (I/O, global state), the dynamic slice must account for them.

## Connections

- [[program-slicing]] — dynamic slicing is a variant of program slicing
- [[static-vs-dynamic-analysis]] — dynamic slicing is a dynamic analysis technique
- [[program-dependence-graph]] — dynamic slicing uses a dynamic dependence graph
- [[data-flow-analysis]] — dynamic data flow is traced from execution
- [[control-dependence]] — dynamic control dependence from actual branch outcomes
- Debugging — primary application of dynamic slicing (produces the minimal relevant code subset for a specific failing run)
- [[software-analyse-lecture-8]] — Source lecture: Program Slicing (static + dynamic slicing introduced together)

## Open Questions

1. How do we **compress execution traces** to make dynamic slicing scalable?
2. Can we combine static and dynamic slicing? (**Conditioned slicing**: slice for a class of inputs)
3. How do we handle **concurrent programs** with dynamic slicing? (Thread-aware dynamic slicing)
4. What is the relationship between dynamic slicing and **delta debugging**?
5. Can we use dynamic slicing for **test case minimization**?
6. How do we compute dynamic slices **online** (during execution, not post-mortem)?
