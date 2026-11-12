---
title: "Structural Analysis for Decompilation"
tags: [concept, control-flow, semester-2, reverse-and-reengineering]
course: "Reverse- and Reengineering"
source_count: 1
status: current
last_updated: 2026-11-12
prerequisites: ["[[control-flow-graph]]", "[[natural-loop]]"]
---

## One-line Summary
Structural analysis recovers source-like control flow by matching known patterns in a control-flow graph and collapsing each matched region into a higher-level construct.

## Core Intuition
A CFG is a set of basic blocks connected by possible jumps. Common shapes correspond to familiar code: a straight chain is a sequence, a split and join is a conditional, and a back edge often indicates a loop. Recognizing these shapes rebuilds readable structure.

## Formal Definition / Statement
Structural analysis traverses a control-flow graph (the lecture describes post-order traversal), matches subgraphs to region patterns, and collapses matched regions. Acyclic patterns include sequence, if-then, if-then-else and switch; cyclic patterns include while and do-while. Iterative refinement removes or virtualizes edges that prevent a match, leaving them to be represented as `break`, `continue` or `goto` in output.

## Key Properties
- CFG vertices represent straight-line code; edges represent possible control transfers.
- Matching and collapsing patterns proceeds iteratively.
- Indirect jumps complicate CFG recovery because their targets may be computed at runtime.
- Refinement can make progress on graphs that a straightforward pattern matcher cannot structure.
- Semantics preservation matters: a structurally plausible rewrite can execute differently.

## Worked Example
Consider a loop body with a conditional exit edge and a backward edge returning to the loop test. The initial graph is unstructured. The analysis recognizes the back-edge region as a loop, then identifies the conditional exit as a `break`; the output becomes `while (condition) { if (exit_condition) break; body; }`.

## Common Pitfalls
- Assuming every CFG can be represented with only structured constructs.
- Treating any back edge as sufficient proof of a particular source loop.
- Choosing loop membership without checking exits and multiple entries.
- Removing an edge without preserving its behavior in the reconstructed code.

## Connections
- [[control-flow-graph]] — input representation for the analysis.
- [[natural-loop]], [[dominance]] and [[post-dominance]] — graph relationships used to reason about loops and joins.
- [[decompilation]] — the larger task this analysis supports.
- [[reverse-and-reengineering-lecture-5]] — lecture source and examples.

## Open Questions
- The slides give heuristic refinement rules, not a complete algorithm or proof of correctness.
- The treatment of indirect jump targets is only outlined; value-set analysis is named but not developed.
