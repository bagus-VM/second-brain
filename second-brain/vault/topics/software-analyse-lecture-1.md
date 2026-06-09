---
title: "Software Analyse - Lecture 1 Overview"
tags: [topic, software-analyse, semester-1]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
Lecture 1 introduces software analysis as a field, its fundamental limitations (Rice's theorem), the core tradeoff (soundness vs completeness), and the four reasoning paradigms, with code clones as a first practical application.

## Core Intuition
Software analysis is about automatically answering "does program P satisfy property φ?" — but this question is fundamentally unanswerable in general (Rice's theorem). So we approximate. The art is choosing the right approximation: abstract interpretation for static analysis, representative test cases for dynamic analysis, and understanding what we sacrifice (soundness vs completeness).

## The Big Picture

### What is Software Analysis?
[[software-analysis]] — extracting information about programs using automatic tools. Two kinds of properties:
- **Structural**: must hold at design time (indentation, visibility, length)
- **Behavioural**: must hold during execution (termination, timing, crashes)

### The Fundamental Limitation
[[rices-theorem]] — all non-trivial semantic properties are undecidable. No tool can perfectly determine if any arbitrary program satisfies an interesting property. This is why we need approximations.

### The Core Tradeoff
[[soundness-and-completeness]] — every analysis must choose:
- **Sound** (over-approximate): catches all errors, but may false alarm
- **Complete** (under-approximate): no false alarms, but may miss errors
- Sound + Complete = impossible (Rice's theorem)

### How We Approximate
[[abstract-interpretation]] — replace concrete values with simplified abstractions. Example: instead of tracking exact integers, track signs (⊕, ⊖, ⊚). Lose precision, gain decidability.

### The Four Paradigms
[[hierarchy-of-analysis]] — four ways to reason about programs:
1. **Deduction** (static): reason from code about all possible runs
2. **Observation** (dynamic): inspect actual program executions
3. **Induction**: generalize from multiple runs to invariants
4. **Experimentation**: systematically isolate causes of effects

### Static vs Dynamic
[[static-vs-dynamic-analysis]] — the two main families:
- Static: analyzes code without running. Challenge: good abstraction.
- Dynamic: observes actual runs. Challenge: representative test cases.

### First Application: Code Clones
[[code-clones]] — detecting duplicated code fragments. A concrete application of character/token-level analysis. Four clone types, four detection strategies.

## Course Roadmap (from Lecture 1)
The lecture previews the full course structure:
1. Characters (this lecture) → Character-level analysis, code clones
2. Tokens → NLP for source code
3. Syntax Trees → [[abstract-interpretation]] (AST representation)
4. Control Flow → Control flow analysis
5. Data Flow → Data flow analysis
6. Dependence Graphs → Program dependence graphs
7. Interprocedural Analysis → Analysis across function boundaries
8. Symbolic Execution → Dynamic symbolic execution
9. Dynamic Analysis → Runtime observation techniques

## Key Relationships
```
[rices-theorem] ──forces──> [abstract-interpretation]
        │                          │
        └──drives──> [soundness-and-completeness]
                           │
                           ├──enables──> [static-vs-dynamic-analysis]
                           │                    │
                           └──underpins──> [hierarchy-of-analysis]
                                                │
                                                └──applied in──> [code-clones]
```

## Connections
- [[software-analysis]] — the overarching concept
- [[rices-theorem]] — why we can't have perfect analysis
- [[abstract-interpretation]] — how we approximate
- [[soundness-and-completeness]] — what we sacrifice
- [[static-vs-dynamic-analysis]] — the two main approaches
- [[hierarchy-of-analysis]] — the four reasoning paradigms
- [[code-clones]] — first practical application

## Next Lecture
- [[software-analyse-lecture-2]] — Tokens and Naturalness of Code (lexical analysis, n-gram models, code naturalness hypothesis)

## Open Questions
- How do the later topics (control flow, data flow, symbolic execution) build on these foundations?
- What's the relationship between the course roadmap and the analysis hierarchy?
- How do real-world tools (e.g., SpotBugs, Infer) combine these techniques?
