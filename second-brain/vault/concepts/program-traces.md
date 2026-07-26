---
title: Program Traces
tags:
  - concept
  - software-analyse
  - semester-1
  - dynamic-analysis
course: Software Analyse
source: software-analyse-lecture-9
source_count: 1
status: current
last_updated: 2026-07-02
---

## One-line Summary

Program traces record the executed instructions and runtime attributes (data state, call stack, object instances) during a program run.

## Core Intuition

When a program executes, every instruction leaves a footprint. A program trace captures these footprints in order — which methods were called, what values variables held, and how the call stack evolved. Think of it as the program's flight recorder: a sequential log of everything that happened at runtime, enabling you to replay, analyse, and debug after the fact.

## Formal Definition / Statement

A program trace $T$ for a program $P$ on input $I$ is a sequence of events $(e_1, e_2, \ldots, e_n)$ where each event $e_i$ records an executed statement or method invocation along with associated attributes such as variable values, the call stack state, and object instance information.

Traces can be collected at different granularity levels:
- **Application level** — manual logging inserted by the developer
- **Instrumentation level** — automatic monitoring via libraries (e.g., [[aspect-oriented-programming|AspectJ]])
- **Virtual Machine level** — built-in language tracing facilities
- **Operating System level** — system-level tracers (e.g., DTrace on BSD/Linux/macOS)

## Key Properties / Complexity

- **Faithfulness** — a trace faithfully represents one specific execution on one specific input
- **Completeness** — traces can record every executed instruction (full trace) or a subset (sampled trace)
- **Overhead** — collecting traces introduces performance and storage costs; seconds of execution can produce hundreds of MB
- **Heisenberg effect** — observing (tracing) a program alters its behaviour (timing, memory usage), analogous to the quantum mechanical observer effect
- **Method call instrumentation** — two strategies: *entry instrumentation* (log at the start of each method) vs *call site instrumentation* (log before each call-site)
- **Call graph vs Call tree vs Calling context tree** — a call graph has no context sensitivity; a call tree is context-sensitive showing the full call sequence; a calling context tree collapses nodes sharing the same hierarchical context. All are built on the [[control-flow-graph]].

## Worked Example

```python
def foo(x):
    return x + 1

def bar(y):
    z = foo(y)
    return z * 2

bar(3)
```

A method-level trace (call tree) would be:
```
bar(3)
  └─ foo(3)
       └─ returns 4
  └─ returns 8
```

The calling context tree collapses repeated calls:
- If `foo` is called from both `bar` and `baz`, the call graph shows one node for `foo`; the call tree shows two separate invocations; the calling context tree shows `foo` once under each caller.

## Common Pitfalls

- **Assuming traces are representative** — a trace reflects one execution path on one input; it does not capture all possible behaviours
- **Ignoring storage overhead** — naive full tracing of long-running programs quickly becomes infeasible
- **Overlooking the Heisenberg effect** — instrumentation can change thread scheduling, mask race conditions, or alter performance characteristics
- **Confusing call graph with call tree** — a call graph loses context (you cannot distinguish `A→B→A` from `A→B, B→A`), which matters for [[fault-localization]]

## Connections

- Traces are the foundation for [[dynamic-slicing]] — slices are computed over recorded execution traces
- [[fault-localization]] techniques (Tarantula, Ochiai) use execution matrices built from traces of passing and failing test runs
- [[delta-debugging]] uses traces to isolate the minimal difference between working and failing inputs
- [[static-vs-dynamic-analysis]] contrasts trace-based (dynamic) approaches with static (code-level) analysis
- [[control-flow-graph]] underpins the call graph, call tree, and calling context tree derived from traces
- [[software-analyse-lecture-9]] — Source lecture: Dynamic Analysis (traces, instrumentation, AOP, fault localization, delta debugging)

## Open Questions

- How do modern profilers implement insertion-based vs sampling-based trace collection, and what are the accuracy trade-offs?
- What is the practical storage limit for traces in real-world systems, and how do compression techniques (e.g., trace summarisation) address this?
