---
title: "Software Analyse Exam Prep — MC Exam Structure"
tags: [exam-prep, software-analyse, multiple-choice, semester-1]
course: "Software Analyse"
exam_date: "2026-07-31"
exam_format: "Multiple choice questions"
status: current
last_updated: 2026-07-22
prerequisites: []
---

## Exam Intel

**Format:** Multiple choice
**Date:** July 31, 2026
**Content:** Covers lectures 2–10 topics below + all 3 projects (readability, sign analysis, slicing)
**Note:** Lecture 11 (Agentic Coding) is not in scope for the exam.

---

## ⛔ EXCLUDED Topics (Confirmed by Professor)

These topics will **NOT** appear on the exam:

| Lecture | Excluded Topic |
|---------|---------------|
| 2. Syntax | Naturalness (Language models) |
| 2. Syntax | General Compiler workflow |
| 2. Syntax | Lexical analysis |
| 3. Parsing | Grammars |
| 3. Parsing | Predictive Parsing |
| 3. Parsing | Syntax directed translation |
| 4. Control flow | Loop Detection |
| 5. Dataflow | DU/UD chains |
| 5. Dataflow | Available expressions, Live variables, Very busy expressions |
| 6. Abstract interpretation | Meet over all paths (MOP) |
| 7. Interprocedural | Meet over valid paths |
| 7. Interprocedural | Heap analysis |
| 8. Slicing | SSA (Static Single Assignment) |
| 8. Slicing | Interprocedural slicing |
| 9. Dynamic analysis | Trace levels |
| 9. Dynamic analysis | AOP (Aspect-Oriented Programming) |
| 9. Dynamic analysis | Fault localization |
| 9. Dynamic analysis | Delta debugging |
| 10. Symbolic Execution | Symbolic execution |
| 10. Symbolic Execution | Dynamic symbolic execution |

---

## ✅ What IS Actually in the Exam

After removing excluded topics, here's what remains:

### 0. Intro — Soundness & Completeness
- Soundness: if the analysis says X, X is actually true (no false negatives for the property being checked)
- Completeness: if X is true, the analysis says X (no false positives)
- Rice's theorem: non-trivial semantic properties of programs are undecidable
- Static analysis is always an approximation — tradeoff between soundness and completeness
- **Vault:** [[soundness-and-completeness]], [[rices-theorem]], [[software-analysis]]

---

### 1. JVM & Bytecode (Full)
- Stack-based vs register-based VM
- JVM instruction types (load/store, arithmetic, control, stack manipulation)
- Bytecode for method calls (INVOKEVIRTUAL, INVOKESTATIC, INVOKESPECIAL)
- How local variables map to slots
- Operand stack before/after specific instructions
- **Vault:** [[java-for-software-analysis]]

### 2. Readability
- Tokens and lexemes: tokenization process, token types, lexeme vs token distinction
- **Vault:** [[tokenization-and-token-types]], [[lexical-analysis]]

#### Readability (Full)
- Shannon entropy: H = -Σ p·log₂(p)
- Halstead Volume: V = N × log₂(n) (operators vs operands)
- Cyclomatic Complexity: M = E - N + 2P
- Feature standardization (z-score), 10-fold cross-validation, threshold 3.6
- **Vault:** [[readability-classifier]]
- **Project connection:** Readability classifier project

### 3. Parsing — AST
- Abstract Syntax Tree: structure, how it differs from parse tree
- AST nodes represent program constructs (expressions, statements, declarations)
- **Vault:** [[abstract-syntax-tree]], [[parse-tree]]

---

### 3. Sign Analysis (Full)
- Sign lattice: {⊥, -, 0, +, -0, -+, 0+, ⊤}
- Bitmask encoding, join = bitwise OR
- Pairwise decomposition for binary operations
- Java integer division truncates toward zero
- Division by zero → BOTTOM
- **Vault:** [[sign-analysis]]
- **Project connection:** Sign analysis project

### 4. Control Flow Analysis
- Control flow graphs (CFG)
- Basic blocks
- Dominance & post-dominance
- Control dependence
- Natural loops (structure only — no loop detection algorithms)
- Dominator tree
- **Vault:** [[control-flow-graph]], [[basic-block]], [[dominance]], [[post-dominance]], [[control-dependence]], [[natural-loop]], [[dominator-tree]]
- ❌ ~~Loop Detection~~ (excluded)

### 5. Data Flow Analysis
- Gen/kill analysis framework
- Iterative dataflow algorithm (forward/backward, must/may)
- Reaching definitions (forward, may)
- Dead code elimination
- Common subexpression elimination
- Register allocation
- **Vault:** [[data-flow-analysis]], [[gen-kill-analysis]], [[iterative-data-flow-analysis]], [[reaching-definitions]], [[dead-code-elimination]], [[common-subexpression-elimination]], [[register-allocation]]
- ❌ ~~DU/UD chains~~ (excluded)
- ❌ ~~Available expressions, Live variables, Very busy expressions~~ (excluded)

### 6. Abstract Interpretation
- Monotone framework
- Lattice-theoretic framework
- Galois connection: (α, γ)
- Minimal fixpoint algorithm
- Distributive framework (when MOP = MFP)
- Widening/narrowing for infinite-height lattices
- **Vault:** [[monotone-framework]], [[lattice]], [[galois-connection]], [[minimal-fixed-point-algorithm]], [[distributive-framework]], [[abstract-interpretation]], [[widening-narrowing]]
- ❌ ~~Meet over all paths (MOP)~~ (excluded — but know MOP vs MFP relationship for distributive framework)

### 7. Interprocedural Analysis
- Context-insensitive vs context-sensitive analysis
- Cloning/inlining context sensitivity
- Call strings
- Points-to analysis (Steensgaard's, Andersen's)
- **Vault:** [[context-sensitivity]], [[cloning-context-sensitivity]], [[inlining-context-sensitivity]], [[call-strings]], [[points-to-analysis]], [[steensgaards-points-to-analysis]], [[andersens-points-to-analysis]], [[aliasing]]
- ❌ ~~Meet over valid paths~~ (excluded)
- ❌ ~~Heap analysis~~ (excluded)

### 8. Program Slicing
- Forward/backward slicing
- Program Dependence Graph (PDG = CDG ∪ DDG)
- Dynamic slicing (execution trace based)
- **Vault:** [[program-slicing]], [[program-dependence-graph]], [[dynamic-slicing]]
- ❌ ~~SSA~~ (excluded)
- ❌ ~~Interprocedural slicing / SDG~~ (excluded)

### 9. Dynamic Analysis
- Static vs dynamic analysis tradeoffs
- Instrumentation (bytecode modification)
- Method call instrumentation
- **Vault:** [[dynamic-analysis]], [[static-vs-dynamic-analysis]], [[program-traces]]
- ❌ ~~Trace levels~~ (excluded)
- ❌ ~~AOP~~ (excluded)
- ❌ ~~Fault localization~~ (excluded)
- ❌ ~~Delta debugging~~ (excluded)

### 10. Symbolic Execution — ENTIRELY EXCLUDED
- ❌ ~~Symbolic execution~~ (excluded)
- ❌ ~~Dynamic symbolic execution / Concolic execution~~ (excluded)

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

### 4. Control Flow Analysis

| Subtopic | Vault Page | Coverage |
|----------|-----------|----------|
| CFG | [[control-flow-graph]] | ✅ Good |
| Basic blocks | [[basic-block]] | ✅ Good |
| Dominance | [[dominance]], [[dominator-tree]] | ✅ Good |
| Post-dominance | [[post-dominance]] | ✅ Good |
| Control dependence | [[control-dependence]] | ✅ Good |
| Natural loops | [[natural-loop]] | ✅ Good |

**Key MC angles:**
- CFG construction from code
- Identifying basic blocks (single entry, single exit)
- Dominator tree: node A dominates B if every path to B goes through A
- Post-dominator tree: reverse CFG, find dominators
- Control dependence: B is control-dependent on A if A post-dominates B's predecessor but not B
- ❌ ~~Loop detection algorithms~~ (excluded)

---

### 5. Data Flow Analysis

| Subtopic | Vault Page | Coverage |
|----------|-----------|----------|
| Gen/kill framework | [[gen-kill-analysis]] | ✅ Good |
| Iterative algorithm | [[iterative-data-flow-analysis]] | ✅ Good |
| Reaching definitions | [[reaching-definitions]] | ✅ Good |
| Dead code elimination | [[dead-code-elimination]] | ✅ Good |
| CSE | [[common-subexpression-elimination]] | ✅ Good |
| Register allocation | [[register-allocation]] | ✅ Good |

**Key MC angles:**
- Forward vs backward analysis (reaching defs = forward)
- Must vs may analyses (reaching defs = may → union)
- Gen/kill sets for each analysis type
- Iterative algorithm: initialize, iterate until fixpoint
- ❌ ~~DU/UD chains~~ (excluded)
- ❌ ~~Available expressions, Live variables, Very busy expressions~~ (excluded)

---

### 6. Abstract Interpretation

| Subtopic | Vault Page | Coverage |
|----------|-----------|----------|
| Monotone framework | [[monotone-framework]] | ✅ Good |
| Lattice theory | [[lattice]] | ✅ Good |
| Galois connection | [[galois-connection]] | ✅ Good |
| Minimal fixpoint | [[minimal-fixed-point-algorithm]] | ✅ Good |
| Distributive framework | [[distributive-framework]] | ✅ Good |
| Abstract interpretation | [[abstract-interpretation]], [[zero-analysis-worked-example]] | ✅ Good |
| Widening/narrowing | [[widening-narrowing]] | ✅ Good |

**Key MC angles:**
- Galois connection: α (abstraction) concrete→abstract, γ (concretization) abstract→concrete
- MFP (minimal fixpoint) — what the iterative algorithm computes
- Distributive framework: when MOP = MFP (know the condition)
- Height of lattice determines convergence speed
- Widening/narrowing for infinite-height lattices
- ❌ ~~MOP itself~~ (excluded — but the MOP=MFP condition is still in scope)

---

### 7. Interprocedural Analysis

| Subtopic | Vault Page | Coverage |
|----------|-----------|----------|
| Context sensitivity | [[context-sensitivity]] | ✅ Good |
| Cloning/inlining | [[cloning-context-sensitivity]], [[inlining-context-sensitivity]] | ✅ Good |
| Call strings | [[call-strings]] | ✅ Good |
| Points-to analysis | [[points-to-analysis]], [[steensgaards-points-to-analysis]], [[andersens-points-to-analysis]] | ✅ Good |
| Aliasing | [[aliasing]] | ✅ Good |

**Key MC angles:**
- Context-insensitive: analyze each method once regardless of caller
- Call strings: track call context as sequence of call sites
- Cloning/inlining: duplicate method analysis per call context
- Steensgaard (union-find, fast, unification) vs Andersen's (subset-based, more precise)
- ❌ ~~Meet over valid paths~~ (excluded)
- ❌ ~~Heap analysis~~ (excluded)

---

### 8. Program Slicing

| Subtopic | Vault Page | Coverage |
|----------|-----------|----------|
| General slicing | [[program-slicing]] | ✅ Good |
| CFG | [[control-flow-graph]] | ✅ Good |
| PDT | [[post-dominance]], [[dominator-tree]] | ✅ Good |
| CDG | [[control-dependence]] | ✅ Good |
| DDG | [[program-dependence-graph]] | ✅ Good |
| Data dependence | [[du-chains-ud-chains]] | ✅ Good |
| Control dependence | [[control-dependence]] | ✅ Good |
| Slicing applied | [[program-slicing]] | ✅ Good |
| Dynamic slicing | [[dynamic-slicing]] | ✅ Good |

**Key MC angles:**
- Backward slice criterion: (p, V) — at program point p, which statements affect V?
- Forward slice criterion: (p, V) — which statements are affected by V at p?
- PDT construction: reverse CFG, find dominators
- CDG: identify control dependence edges
- DDG: trace variable definitions to uses
- PDG = CDG ∪ DDG — combines both dependence types
- Dynamic slicing uses execution trace, not just program structure
- Slicing applied: given code, compute the slice for a given criterion
- ❌ ~~SSA / φ-functions~~ (excluded)
- ❌ ~~Interprocedural slicing / SDG~~ (excluded)

---

### 9. Dynamic Analysis

| Subtopic | Vault Page | Coverage |
|----------|-----------|----------|
| Static vs dynamic | [[static-vs-dynamic-analysis]] | ✅ Good |
| Dynamic analysis | [[dynamic-analysis]] | ✅ Good |
| Instrumentation | [[dynamic-analysis]] | ⚠️ Check |
| Method call instrumentation | [[dynamic-analysis]] | ⚠️ Check |

**Key MC angles:**
- Static: over-approximation, sound but imprecise; Dynamic: exact but incomplete
- Instrumentation: bytecode modification to record execution
- Method call instrumentation: how to hook into JVM execution
- ❌ ~~Trace levels~~ (excluded)
- ❌ ~~AOP~~ (excluded)
- ❌ ~~Fault localization~~ (excluded)
- ❌ ~~Delta debugging~~ (excluded)

---

### 10. Symbolic Execution — ENTIRELY EXCLUDED

~~Symbolic execution~~ and ~~Dynamic symbolic execution / Concolic execution~~ are **NOT on the exam.**

---

## Three-Project Connection

The exam is MC but tests understanding of concepts as implemented in your projects:

1. **Readability** (Project 1) → Tests §2 (Readability metrics)
2. **Sign Analysis** (Project 2) → Tests §3 (Sign lattice, transfer functions), §6 (Abstract interpretation), §7 (Interprocedural)
3. **Slicing** (Project 3) → Tests §4 (CFG/PDT/CDG/DDG), §5 (Dataflow), §8 (Static + Dynamic slicing)

**MC strategy:** Many questions will describe a code snippet or analysis scenario and ask you to identify the correct result, concept, or limitation. You need to be able to:
- Trace sign analysis lattice operations by hand
- Identify which dataflow analysis is being described (forward/backward, must/may)
- Recognize graph types (CFG vs PDT vs CDG vs DDG vs PDG)
- Know the tradeoffs of static vs dynamic analysis
- Understand context sensitivity techniques and points-to analysis

---

## Coverage Gap Analysis

**Vault coverage: ~35 concept pages in scope.** Everything excluded is cleanly removable.

**Check these pages for completeness (flagged ⚠️ above):**
1. Stack calculation — verify [[java-for-software-analysis]] covers stack-based execution model
2. Instrumentation & method call instrumentation — verify [[dynamic-analysis]] covers bytecode-level instrumentation details

**Vault pages now OUT OF EXAM SCOPE (study these only if time permits):**
- [[n-gram-language-models]], [[perplexity-and-entropy]], [[surprisal-and-code-prediction]], [[smoothing-techniques]], [[code-naturalness-hypothesis]], [[buggy-code-naturalness]] — Naturalness
- [[lexical-analysis]], [[finite-automata-and-regular-expressions]], [[tokenization-and-token-types]], [[lex-and-flex]] — Lexical analysis
- [[context-free-grammar]], [[grammar-ambiguity]], [[operator-precedence-associativity]], [[parse-tree]] — Grammars
- [[predictive-parsing]], [[first-sets]], [[left-recursion-elimination]], [[left-factoring]] — Predictive parsing
- [[syntax-directed-translation]] — SDT
- [[du-chains-ud-chains]] — DU/UD chains
- [[available-expressions]], [[live-variable-analysis]], [[very-busy-expressions]] — excluded dataflow analyses
- [[mop-vs-mfp]] — MOP (but know MOP=MFP condition)
- [[meet-over-valid-paths]], [[valid-paths]] — valid paths
- [[heap-analysis]] — heap analysis
- [[static-single-assignment]], [[phi-function]] — SSA
- [[system-dependence-graph]] — interprocedural slicing
- [[program-traces]] — trace levels (but keep for general understanding)
- [[aspect-oriented-programming]] — AOP
- [[fault-localization]], [[delta-debugging]] — fault loc / delta debugging
- [[symbolic-execution]], [[concolic-execution]] — symbolic execution

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
