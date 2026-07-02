---
title: "Path Profiling"
tags: [concept, software-analyse, semester-1, profiling, symbolic-execution]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-07-02
prerequisites: [control-flow-graph]
---

## One-line Summary
Path profiling counts how often each execution path through a function runs, using the Ball-Larus algorithm to encode paths as integer sums with minimal instrumentation overhead.

## Core Intuition
Edge profiling (counting how often each branch is taken) doesn't tell you which path through the function was actually executed — different paths can share the same edge frequencies. Path profiling solves this by assigning each path a unique number and counting occurrences. The trick is encoding path numbers efficiently so you don't have to instrument every branch.

## Formal Definition / Statement
Given a control-flow graph (CFG) with entry and exit nodes, a path is a sequence of edges from entry to exit. Path profiling assigns an integer to each edge such that the sum of integers along any path yields a unique path identifier.

**Ball-Larus Algorithm:**
1. Convert the CFG to a DAG (remove backedges for cyclic CFGs)
2. Build a maximum-cost spanning tree from entry to exit
3. Assign integer increments to chords (edges not in the spanning tree) so that each path through the DAG has a unique sum
4. Instrument only the chord edges — add the increment to a running counter
5. At each exit node, record the counter value as the path number

**Path reconstruction:** Given a path sum R at exit, start at entry and walk the CFG. At each branch, follow the edge whose value v satisfies v ≤ R, then set R := R − v.

## Key Properties
- **Unique encoding**: each path through the DAG gets a distinct integer
- **Minimal instrumentation**: only chord edges need instrumentation (not all edges)
- **Overhead**: O(chords) per function, typically much less than total edges
- **Cyclic CFGs**: backedges are removed, dummy edges added (entry→merge, branch→exit), and backedge instrumentation resets the counter
- **Based on**: event counting algorithm from the Ball-Larus 1996 paper

## Worked Example
```
Entry → A (edge value: 0)
A → B (edge value: 0)    // in spanning tree
A → C (edge value: 1)    // chord
B → Exit (edge value: 0) // in spanning tree
C → Exit (edge value: 0) // in spanning tree
```
- Path Entry→A→B→Exit: sum = 0+0+0 = 0 → path 0
- Path Entry→A→C→Exit: sum = 0+1+0 = 1 → path 1

Only the chord edge A→C has a non-zero increment. One instrumentation point distinguishes two paths.

## Common Pitfalls
- Confusing path profiling with edge profiling — edge counts don't uniquely identify paths
- Forgetting that cyclic CFGs need dummy edges and backedge counter resets
- Assuming the spanning tree can be arbitrary — maximum-cost spanning tree minimizes the number of chord instrumentations
- Thinking path profiling is practical for functions with many loops — the number of paths grows exponentially with loop nesting depth

## Connections
- [[control-flow-graph]] — Ball-Larus operates directly on the CFG structure
- [[symbolic-execution]] — symbolic execution explores paths systematically; path profiling counts them empirically
- [[concolic-execution]] — concolic execution generates inputs for specific paths; path profiling measures which paths are actually taken
- [[software-analyse-lecture-10]] — Ball-Larus path profiling is covered in Lecture 10
- [[fault-localization]] — path frequencies can inform which paths to investigate first
- [[dynamic-analysis]] — path profiling is a dynamic analysis technique (observes real executions)

## Open Questions
- How does path profiling interact with inlined functions (CFG size explosion)?
- What's the practical limit on the number of distinct paths before the encoding overflows?
