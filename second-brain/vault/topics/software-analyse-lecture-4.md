---
title: "Lecture 4: Control Flow Analysis – Topic Overview"
tags: [topic-overview, software-analyse, semester-1, control-flow]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [abstract-syntax-tree]
---

## One-line Summary

Lecture 4 introduces control flow analysis: representing program execution as directed graphs ([[control-flow-graph]]), partitioning into [[basic-block]]s, computing [[dominance]] and [[post-dominance]] relations, determining [[control-dependence]], and identifying [[natural-loop]]s for optimisation.

## Core Topics

### Control Flow Representation
- [[control-flow-graph]] – directed graph G=(N,E) where nodes are statements (or blocks) and edges model transfer of control; simplifying assumptions: unique entry node n₀ and unique exit node n_f
- [[basic-block]] – maximal sequence of consecutively-executed statements; the fundamental unit for most control flow analyses

### Dominance Relations
- [[dominance]] – node a dominates b if every path from entry to b passes through a; reflexive, transitive, antisymmetric relation computed via iterative fixed-point algorithm
- [[dominator-tree]] – tree where each node's parent is its immediate dominator (idom); compact representation of the full dominance relation
- [[post-dominance]] – dual of dominance: node d post-dominates n if every path from n to exit passes through d; computed by reversing the CFG and applying the dominance algorithm

### Control Dependence
- [[control-dependence]] – statement b is control dependent on statement a if a directly determines whether b executes; built from the post-dominator tree and CFG edges; foundation for the Control Dependence Graph (CDG)

### Natural Loops
- [[natural-loop]] – identified via back edges (n→d where d dominates n); has a single header entry point; inner loops (containing no other loops) are prime optimisation targets

## Connections

- Builds on [[software-analyse-lecture-3]] – the [[abstract-syntax-tree]] from parsing is the starting point; CFGs are a simpler, flow-oriented abstraction derived from the AST
- CFGs are the foundation for data flow analysis (likely covered in a subsequent lecture): [[liveness-analysis]], [[available-expressions]], [[monotone-framework]]
- [[control-dependence]] is the basis for program slicing and is used in testing (e.g., identifying which predicates affect which statements)
- [[dominance]] is used in SSA (Static Single Assignment) form construction, a key intermediate representation in modern compilers
- Branch coverage in testing directly corresponds to covering all edges in the [[control-flow-graph]]

## Key Exam-Relevant Points

1. Construct a CFG from a given Java method (if/else, for, while, do-while, switch, try/catch, break)
2. Identify basic blocks using the leader algorithm (first statement, branch targets, fall-through targets)
3. Compute dominance sets using the iterative algorithm and build the dominator tree
4. Compute post-dominance by reversing the CFG
5. Determine control dependence relationships using the CDG construction algorithm (find non-ancestor edges in post-dominator tree, find LCA, traverse backwards)
6. Identify natural loops from back edges and compute their node sets
7. Distinguish inner loops and explain why they are good optimisation candidates
