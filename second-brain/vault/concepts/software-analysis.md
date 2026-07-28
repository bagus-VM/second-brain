---
title: "Software Analysis"
tags: [concept, software-analyse, semester-1]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
Software analysis is the process of automatically extracting information about a program from its source code or artefacts to determine whether properties hold.

## Core Intuition
Instead of manually reading code to check if it's correct, we build tools that inspect programs and tell us things about them. The key insight: we want to answer the question "Does program P satisfy property φ?" — but doing this perfectly is impossible (see [[rices-theorem]]), so we use approximations.

## Formal Definition / Statement
Given a program P and a property of interest φ, software analysis determines whether P satisfies φ. The analysis operates on various artefacts:
- Source code
- Java bytecode
- Execution traces
- Git history

The process uses automatic tools to extract information, rather than manual inspection.

## Key Properties / Complexity
- ****Structural properties** must hold at design time** (e.g., indentation rules, visibility of attributes, code length)
- ****Behavioural properties** must hold during execution** (e.g., termination, execution time, crash conditions)
- Analysis operates on an **internal representation** of the program (not raw source text)
- The pipeline: Source Code → Internal Representation → Analysis Algorithm → Result

An ****internal representation (IR)**** is a data structure or model that captures the program’s:
- Syntax (what constructs are present: loops, functions, conditions, etc.)
- Semantics (what those constructs mean: control flow, data flow, types, etc.)
- Relationships (which code calls which, which variables are used where, etc.)
## Worked Example
Consider a C program:
```c
char* format = "a = %d";
int a = compute_value();
sprintf(buf, format, a);
```
If `a` is actually a float, this is a bug. A software analysis tool could detect this type mismatch automatically, without running the program.

## Common Pitfalls
- Assuming analysis can give perfect answers — it cannot (Rice's theorem)
- Confusing what the code *says* with what the code *does* — analysis must bridge this gap
- Forgetting that analysis operates on abstractions, not the full reality of all possible executions

## Connections
- [[static-vs-dynamic-analysis]] — the two major families of analysis techniques
- [[rices-theorem]] — fundamental limitation on what analysis can achieve
- [[abstract-interpretation]] — the core technique for making analysis tractable
- [[soundness-and-completeness]] — tradeoffs every analysis must make
- [[hierarchy-of-analysis]] — the four reasoning paradigms (deduction, observation, induction, experimentation)
- [[code-clones]] — a concrete application of character/token-level analysis

## Open Questions
- How do we choose the right abstraction level for a given analysis?
- What properties are practically decidable vs. requiring approximation?
- How do neural/ML-based analysis tools fit into the traditional framework?
