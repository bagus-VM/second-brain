---
title: "Lecture 5: Data Flow Analysis – Topic Overview"
tags: [topic-overview, software-analyse, semester-1, data-flow]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary

Lecture 5 introduces data flow analysis — a family of compile-time techniques that track how information propagates along control-flow paths to enable optimisations and bug detection.

## Core Topics

### Foundations
- [[data-flow-analysis]] — the general framework: gen/kill sets, IN/OUT equations, iterative fixed-point computation
- [[gen-kill-analysis]] — how each statement generates and kills data flow facts
- [[iterative-data-flow-analysis]] — the worklist algorithm that solves data flow equations to a fixed point

### Forward Analyses
- [[reaching-definitions]] — which assignments (definitions) of a variable may reach a given program point without being killed (forward, may)
- [[available-expressions]] — which expressions have already been computed on every path to a point and not invalidated since (forward, must)

### Backward Analyses
- [[live-variable-analysis]] — which variables will be used on some future path before being redefined (backward, may)
- [[very-busy-expressions]] — which expressions will be evaluated on every future path before being invalidated (backward, must)

### Chain Structures
- [[du-chains-ud-chains]] — definition-use chains and use-definition chains that connect definitions to their uses

## Classification Matrix

| Analysis | Direction | Kind | Join |
|---|---|---|---|
| [[reaching-definitions]] | Forward | May | ∪ |
| [[available-expressions]] | Forward | Must | ∩ |
| [[live-variable-analysis]] | Backward | May | ∪ |
| [[very-busy-expressions]] | Backward | Must | ∩ |

## Connections

- Builds on [[control-flow-graph]] from earlier lectures
- Enables [[dead-code-elimination]], [[common-subexpression-elimination]], [[register-allocation]]
- [[du-chains-ud-chains]] are derived from [[reaching-definitions]] and [[live-variable-analysis]]
- Foundation for more advanced analyses: constant propagation, pointer analysis

## Open Questions

- How do we handle inter-procedural data flow (across function boundaries)?
- What is the relationship between data flow analysis and abstract interpretation?
- How do widening/narrowing operators accelerate convergence for infinite lattices (e.g., constant propagation)?
