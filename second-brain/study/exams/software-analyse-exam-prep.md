---
title: "Software Analyse Exam Prep — MC Exam Structure"
tags: [exam-prep, software-analyse, multiple-choice, semester-1]
course: "Software Analyse"
exam_date: "2026-07-31"
exam_format: "Multiple choice questions"
status: current
last_updated: 2026-07-15
prerequisites: []
---

## Exam Intel

**Format:** Multiple choice
**Date:** July 31, 2026
**Content:** Covers all 10 lecture topics below + all 3 projects (readability, sign analysis, slicing)

---

## Topic Map — Exam Topics to Vault Coverage

### 1. JVM & Bytecode

| Subtopic               | Vault Page                                              | Coverage |
| ---------------------- | ------------------------------------------------------- | -------- |
| JVM concepts           | [[java-for-software-analysis]]                          | ✅ Good   |
| Stack calculation      | (embedded in sign-analysis, java-for-software-analysis) | ⚠️ Check |
| Bytecode understanding | [[java-for-software-analysis]]                          | ✅ Good   |

**Key MC angles:**
- Stack-based vs register-based VM
- JVM instruction types (load/store, arithmetic, control, stack manipulation)
- Bytecode for method calls (INVOKEVIRTUAL, INVOKESTATIC, INVOKESPECIAL)
- How local variables map to slots
- Operand stack before/after specific instructions

---

### 2. Readability

| Subtopic | Vault Page | Coverage |
|----------|-----------|----------|
| General pipeline | [[readability-classifier]] | ✅ Good |
| Token Entropy | [[readability-classifier]] (section) | ✅ Covered |
| Halstead Volume | [[readability-classifier]] (section) | ✅ Covered |
| Cyclomatic Complexity | [[readability-classifier]] (section) | ✅ Covered |

**Key MC angles:**
- Shannon entropy formula: H = -Σ p·log₂(p)
- What counts as operator vs operand in Halstead (N1, n1, N2, n2)
- Halstead Volume: V = N × log₂(n)
- Cyclomatic complexity: M = E - N + 2P (or decision points + 1)
- Feature standardization (z-score) and why it matters for logistic regression
- 10-fold cross-validation purpose
- Threshold 3.6 for binary classification

**Project connection:** Readability classifier project. MC questions will test if you understand the metrics, not just that you implemented them.

---

### 3. Sign Analysis

| Subtopic | Vault Page | Coverage |
|----------|-----------|----------|
| General | [[sign-analysis]] | ✅ Good |
| Lattice | [[lattice]], [[sign-analysis]] | ✅ Good |
| Transfer Relations | [[sign-analysis]] (transfer functions section) | ✅ Good |

**Key MC angles:**
- Sign lattice structure: {⊥, -, 0, +, -0, -+, 0+, ⊤}
- Bitmask encoding: MINUS=001, ZERO=010, PLUS=100
- Join operation: bitwise OR
- Pairwise decomposition for binary operations
- Java integer division truncates toward zero (-1/2 = 0, not -1)
- Division by zero → BOTTOM (undefined), not TOP (could be anything)
- Condition narrowing NOT implemented (conservative/sound)

**Project connection:** Sign analysis project. Expect questions on lattice operations and transfer function behavior.

---

### 4. Static & Dynamic Slicing

| Subtopic | Vault Page | Coverage |
|----------|-----------|----------|
| General | [[program-slicing]], [[dynamic-slicing]] | ✅ Good |
| CFG | [[control-flow-graph]] | ✅ Good |
| PDT | [[post-dominance]], [[dominator-tree]] | ✅ Good |
| CDG | [[control-dependence]] | ✅ Good |
| DDG | (in [[program-dependence-graph]]) | ✅ Covered |
| Data dependence | [[du-chains-ud-chains]] | ✅ Good |
| Control dependence | [[control-dependence]] | ✅ Good |
| Slicing applied | [[program-slicing]] | ✅ Good |

**Key MC angles:**
- Post-dominator tree construction (reverse CFG, find dominators)
- CDG: node B is control-dependent on node A if A post-dominates B's predecessor but not B
- DDG: variable v at node n2 depends on node n1 if there's a path where v is not redefined
- PDG = CDG ∪ DDG
- Backward slice: all nodes that affect a variable at a point
- Forward slice: all nodes affected by a variable at a point

**Project connection:** Slicing project. MC questions on CFG construction, dependence graphs, and how slicing uses them.

---

### 5. Dataflow Analysis

| Subtopic | Vault Page | Coverage |
|----------|-----------|----------|
| Data dependence | [[du-chains-ud-chains]] | ✅ Good |
| Reaching definitions | [[reaching-definitions]] | ✅ Good |
| Reachable uses | [[liveness-analysis]], [[live-variable-analysis]] | ✅ Good |
| Du/UD chains | [[du-chains-ud-chains]] | ✅ Good |
| Iterative dataflow (forward/backward, must/may) | [[iterative-data-flow-analysis]], [[data-flow-analysis]] | ✅ Good |
| Available expressions | [[available-expressions]] | ✅ Good |
| Live variables | [[live-variable-analysis]] | ✅ Good |
| Very busy expressions | [[very-busy-expressions]] | ✅ Good |

**Key MC angles:**
- Forward vs backward analysis: reaching defs (forward), live variables (backward)
- Must vs may: available expressions (must), reaching defs (may)
- Gen/kill sets for each analysis type
- Iterative algorithm: initialize, iterate until fixpoint
- DU chains: definition → all uses; UD chains: use → all definitions
- Union for may analyses, intersection for must analyses

---

### 6. Abstract Interpretation

| Subtopic | Vault Page | Coverage |
|----------|-----------|----------|
| Lattice theoretic framework | [[lattice]], [[galois-connection]] | ✅ Good |
| Minimal fixpoint algorithm | [[minimal-fixed-point-algorithm]] | ✅ Good |
| Meet over all paths | [[mop-vs-mfp]] | ✅ Good |
| Abstract interpretation (zero/sign analysis) | [[abstract-interpretation]], [[zero-analysis-worked-example]] | ✅ Good |

**Key MC angles:**
- Galois connection: (α, γ) between concrete and abstract domains
- α (abstraction): concrete → abstract; γ (concretization): abstract → concrete
- MOP (meet over all paths) vs MFP (minimal fixpoint)
- When MOP = MFP: distributive framework condition
- Height of lattice determines convergence speed
- Widening/narrowing for infinite-height lattices

---

### 7. Interprocedural Analysis

| Subtopic | Vault Page | Coverage |
|----------|-----------|----------|
| Limitations | [[context-sensitivity]] | ✅ Good |
| Meet over valid paths | [[valid-paths]] | ✅ Good |
| Context sensitivity (cloning, inlining, call strings) | [[context-sensitivity]], [[cloning-context-sensitivity]], [[call-strings]] | ✅ Good |
| Heap analysis | [[aliasing]], [[andersens-points-to-analysis]] | ✅ Good |

**Key MC angles:**
- Context-insensitive: analyze each method once regardless of caller
- Call strings: track call context as sequence of call sites
- Cloning/inlining: duplicate method analysis per call context
- Valid paths vs all paths (exclude infeasible interprocedural paths)
- Procedure summaries: abstract effect of a method (NOTE: excluded from exam per your list)
- Heap analysis: points-to sets, Andersen's analysis

---

### 8. Slicing (Advanced)

| Subtopic | Vault Page | Coverage |
|----------|-----------|----------|
| SSA | [[static-single-assignment]], [[phi-function]] | ✅ Good |
| Forward/backward slicing | [[program-slicing]] | ✅ Good |
| Interprocedural slicing | [[system-dependence-graph]] | ✅ Good |
| Dynamic slicing | [[dynamic-slicing]] | ✅ Good |

**Key MC angles:**
- SSA: each variable assigned exactly once; φ-functions at join points
- Backward slice criterion: (p, V) — at program point p, which statements affect V?
- Forward slice criterion: (p, V) — which statements are affected by V at p?
- SDG = PDGs + parameter-in/parameter-out edges + call edges
- Dynamic slicing uses execution trace, not just program structure

---

### 9. Dynamic Analysis

| Subtopic | Vault Page | Coverage |
|----------|-----------|----------|
| Problems of static analysis | [[static-vs-dynamic-analysis]] | ✅ Good |
| Components of dynamic analysis | [[dynamic-analysis]] | ✅ Good |
| Trace levels | [[program-traces]] | ✅ Good |
| Method call instrumentation | (in [[dynamic-analysis]]) | ⚠️ Check |
| AOP | [[aspect-oriented-programming]] | ✅ Good |
| Fault localization | [[fault-localization]] | ✅ Good |
| Delta debugging | [[delta-debugging]] | ✅ Good |

**Key MC angles:**
- Static: over-approximation, sound but imprecise; Dynamic: exact but incomplete
- Instrumentation: bytecode modification to record execution
- Trace levels: method entry/exit, statement, instruction
- AOP: aspects, pointcuts, join points, advice
- Delta debugging: binary search for minimal failing input
- Fault localization: spectrum-based (suspiciousness = failed_with / total_with)

---

### 10. Symbolic Execution & SE

| Subtopic | Vault Page | Coverage |
|----------|-----------|----------|
| Symbolic Execution | [[symbolic-execution]] | ✅ Good |
| Dynamic Symbolic Execution | [[concolic-execution]] | ✅ Good |

**Key MC angles:**
- Symbolic execution: replace concrete values with symbols, build path conditions
- Path explosion problem: exponential paths through loops/branches
- Constraint solving: SMT solver (Z3) checks path feasibility
- DSE (concolic): combine concrete + symbolic execution
- DSE uses concrete values to simplify constraints, then symbolically explores variations

---

## Coverage Gap Analysis

**Vault coverage: 45+ concept pages for SA topics.** Almost everything is covered.

**Check these pages for completeness (flagged ⚠️ above):**
1. Stack calculation — verify [[java-for-software-analysis]] covers stack-based execution model
2. Method call instrumentation — verify [[dynamic-analysis]] covers bytecode-level instrumentation details

**Missing pages (create if needed):**
- None critical — all major topics have vault pages

---

## Three-Project Connection

The exam is MC but tests understanding of concepts as implemented in your projects:

1. **Readability** (Project 1) → Tests §2 (Readability metrics), §10 (ML pipeline understanding)
2. **Sign Analysis** (Project 2) → Tests §3 (Sign lattice, transfer functions), §6 (Abstract interpretation), §7 (Interprocedural)
3. **Slicing** (Project 3) → Tests §4 (Static slicing, CFG/PDT/CDG/DDG), §5 (Dataflow), §8 (SSA, interprocedural slicing), §9 (Dynamic analysis concepts)

**MC strategy:** Many questions will describe a code snippet or analysis scenario and ask you to identify the correct result, concept, or limitation. You need to be able to:
- Trace sign analysis lattice operations by hand
- Identify which dataflow analysis is being described (forward/backward, must/may)
- Recognize graph types (CFG vs PDT vs CDG vs DDG vs PDG vs SDG)
- Know the tradeoffs of static vs dynamic analysis
- Understand AOP concepts and instrumentation

---

## Connections

- [[sign-analysis]] — Full theory deep dive
- [[readability-classifier]] — Full theory deep dive
- [[program-slicing]] — Full theory deep dive
- [[java-for-software-analysis]] — JVM and bytecode foundation
- [[data-flow-analysis]] — General dataflow framework
- [[abstract-interpretation]] — Theoretical foundation
- [[software-analyse-projects-overview]] — All three projects overview

---

## Open Questions

- Verify stack calculation coverage in java-for-software-analysis page
- Verify method call instrumentation coverage in dynamic-analysis page
- Check if any lecture slides contain MC-style examples worth practicing


---

## Related Resources

### 📖 Software Analyse - Lecture 1 Overview
- Lecture topic: [[software-analyse-lecture-1]]

**Key concepts covered:**
- [[software-analysis]]
- [[rices-theorem]]
- [[soundness-and-completeness]]
- [[abstract-interpretation]]
- [[hierarchy-of-analysis]]
- [[static-vs-dynamic-analysis]]
- [[code-clones]]
- [[software-analyse-projects-overview]]

### 📖 Software Analyse — Lecture 2: Tokens and Naturalness of Code
- Lecture topic: [[software-analyse-lecture-2]]

**Key concepts covered:**
- [[lexical-analysis]]
- [[finite-automata-and-regular-expressions]]
- [[tokenization-and-token-types]]
- [[lex-and-flex]]
- [[ccfinder]]
- [[n-gram-language-models]]
- [[perplexity-and-entropy]]
- [[surprisal-and-code-prediction]]
- [[smoothing-techniques]]
- [[code-naturalness-hypothesis]]
- [[buggy-code-naturalness]]
- [[code-clones]]
- [[abstract-interpretation]]

### 📖 Lecture 3: Parsing – Topic Overview
- Lecture topic: [[software-analyse-lecture-3]]

**Key concepts covered:**
- [[context-free-grammar]]
- [[grammar-ambiguity]]
- [[operator-precedence-associativity]]
- [[parse-tree]]
- [[abstract-syntax-tree]]
- [[predictive-parsing]]
- [[shift-reduce-parsing]]
- [[first-sets]]
- [[left-recursion-elimination]]
- [[left-factoring]]
- [[syntax-directed-translation]]

### 📖 Lecture 4: Control Flow Analysis – Topic Overview
- Lecture topic: [[software-analyse-lecture-4]]

**Key concepts covered:**
- [[control-flow-graph]]
- [[basic-block]]
- [[dominance]]
- [[post-dominance]]
- [[control-dependence]]
- [[natural-loop]]
- [[dominator-tree]]
- [[abstract-syntax-tree]]
- [[liveness-analysis]]
- [[available-expressions]]
- [[monotone-framework]]

### 📖 Lecture 5: Data Flow Analysis – Topic Overview
- Lecture topic: [[software-analyse-lecture-5]]

**Key concepts covered:**
- [[data-flow-analysis]]
- [[gen-kill-analysis]]
- [[iterative-data-flow-analysis]]
- [[reaching-definitions]]
- [[available-expressions]]
- [[live-variable-analysis]]
- [[very-busy-expressions]]
- [[du-chains-ud-chains]]
- [[control-flow-graph]]
- [[dead-code-elimination]]
- [[common-subexpression-elimination]]
- [[register-allocation]]

### 📖 Lecture 6: Data Flow Analysis Part 2 — Lattice-Theoretic Framework and Abstract Interpretation
- Lecture topic: [[software-analyse-lecture-6]]

**Key concepts covered:**
- [[monotone-framework]]
- [[data-flow-analysis]]
- [[lattice]]
- [[iterative-data-flow-analysis]]
- [[mop-vs-mfp]]
- [[distributive-framework]]
- [[abstract-interpretation]]
- [[zero-analysis-worked-example]]
- [[minimal-fixed-point-algorithm]]
- [[galois-connection]]
- [[reaching-definitions]]
- [[available-expressions]]
- [[live-variable-analysis]]
- [[very-busy-expressions]]
- [[widening-narrowing]]

### 📖 Lecture 7: Interprocedural and Heap Analysis
- Lecture topic: [[software-analyse-lecture-7]]

**Key concepts covered:**
- [[monotone-framework]]
- [[abstract-interpretation]]
- [[mop-vs-mfp]]
- [[data-flow-analysis]]
- [[interprocedural-analysis]]
- [[context-sensitivity]]
- [[meet-over-valid-paths]]
- [[points-to-analysis]]
- [[steensgaards-points-to-analysis]]
- [[andersens-points-to-analysis]]
- [[heap-analysis]]
- [[valid-paths]]
- [[cloning-context-sensitivity]]
- [[inlining-context-sensitivity]]
- [[call-strings]]
- [[procedure-summaries]]
- [[aliasing]]
- [[union-find-data-structure]]
- [[zero-analysis-worked-example]]
- [[iterative-data-flow-analysis]]

### 📖 Lecture 8: Program Slicing
- Lecture topic: [[software-analyse-lecture-8]]

**Key concepts covered:**
- [[control-flow-graph]]
- [[points-to-analysis]]
- [[dominance]]
- [[dominator-tree]]
- [[control-dependence]]
- [[data-flow-analysis]]
- [[interprocedural-analysis]]
- [[basic-block]]
- [[reaching-definitions]]
- [[static-single-assignment]]
- [[phi-function]]
- [[program-dependence-graph]]
- [[program-slicing]]
- [[system-dependence-graph]]
- [[dynamic-slicing]]

### 📖 Software Analyse - Lecture 9: Dynamic Analysis
- Lecture topic: [[software-analyse-lecture-9]]

**Key concepts covered:**
- [[control-flow-graph]]
- [[aspect-oriented-programming]]
- [[dynamic-slicing]]
- [[program-slicing]]
- [[fault-localization]]
- [[delta-debugging]]
- [[static-vs-dynamic-analysis]]
- [[dynamic-analysis]]
- [[program-traces]]
- [[program-dependence-graph]]
- [[hierarchy-of-analysis]]
- [[software-analysis]]
- [[abstract-interpretation]]
- [[soundness-and-completeness]]

### 📖 Software Analyse - Lecture 10: Dynamic Symbolic Execution
- Lecture topic: [[software-analyse-lecture-10]]

**Key concepts covered:**
- [[static-vs-dynamic-analysis]]
- [[control-flow-graph]]
- [[symbolic-execution]]
- [[concolic-execution]]
- [[hierarchy-of-analysis]]
- [[dynamic-slicing]]
- [[software-analysis]]
- [[abstract-interpretation]]
- [[soundness-and-completeness]]

### 📖 Lecture 11 - Agentic Coding and Software Quality
- Lecture topic: [[software-analyse-lecture-11]]

**Key concepts covered:**
- [[static-vs-dynamic-analysis]]
- [[testing]]
- [[fault-localization]]
- [[debugging]]
- [[design-patterns]]
