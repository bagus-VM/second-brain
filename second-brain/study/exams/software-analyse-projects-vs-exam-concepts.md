---
title: "Software Analyse — 3 Projects vs Exam Concepts"
tags: [exam-prep, software-analyse, projects, semester-1]
course: "Software Analyse"
exam_date: "2026-07-31"
status: current
last_updated: 2026-07-29
prerequisites: ["[[software-analyse-concepts-by-project]]", "[[software-analyse-exam-prep]]", "[[software-analyse-codebase-defense]]"]
---

# Software Analyse — 3 Projects vs Exam Concepts

> The exam is MC, but a big part tests your ability to explain your own codebases.
> This page maps every in-scope exam concept directly to the project that exercises it,
> and tells you exactly where in the code the concept lives and what you must explain.

---

## Project 1: Readability Classifier

**Path:** `projects/software-analyse/ss26sareadability-practice-putra01/`
**Status:** Submitted

**What it does:** Two-phase ML pipeline. Extracts 4 static metrics from 200 Java snippets, trains logistic regression to classify readable vs. not readable.

### Concept → Code Mapping

| Exam Concept | Where in Your Code | What You Must Explain |
|---|---|---|
| Shannon entropy (L2) | `TokenEntropyFeature.java` | H = -Σ p·log₂(p). High entropy = many unique tokens = harder to read. |
| Halstead volume (L2) | `HalsteadVolumeFeature.java` + `OperatorVisitor` + `OperandVisitor` | V = N × log₂(η). N = total ops+operands, η = unique. Balances length vs. vocabulary. |
| Cyclomatic complexity (L2) | `CyclomaticComplexityVisitor.java` | M = decision points + 1. Each `if`, `for`, `while`, `case`, `&&`, `\|\|`, `?:` = +1. |
| Number of Lines (L2) | `NumberLinesFeature.java` | Simplest metric. Split on `\r?\n`. |
| Tokens and lexemes (L2) | JavaParser token stream | Token = category+value. Lexeme = raw text. Used by entropy feature. |
| AST (L3) | JavaParser AST + Visitor pattern | AST preserves semantics, drops grammar noise. Visitor walks tree to extract metrics. |
| Feature standardization | `Classify.java` — WEKA `Standardize` | Z-score: (x-μ)/σ. Halstead 0-500, entropy 0-5. Without it, big features dominate. |
| Logistic regression | `Classify.java` | Probability estimates, interpretable coefficients, linear boundary, less overfitting on 200 samples. |
| 10-fold CV | `Classify.java` | 200 samples too small for test set. Each sample tested once. Seed=1 for reproducibility. |
| Threshold 3.6 | `truth_scores.csv` | Mean of 9 human raters on 1-5 scale. 3.6 splits ~50/50, avoids class imbalance. |

### Key Pitfalls

- JavaParser's `VariableDeclarator` with initializer (`int x = 1`) is NOT an `AssignExpr`. `OperatorVisitor` has special handling to count the `=`.
- `0×log₂(0) = 0` by convention (L'Hôpital), not undefined.
- Ternary `?:` counts as a decision point in cyclomatic complexity.

---

## Project 2: Sign Analysis

**Path:** `projects/software-analyse/ss26sasign-putra01/`
**Status:** All tests passing

**What it does:** Interprocedural static analysis on Java bytecode. Tracks abstract sign (−, 0, +) using a lattice. Finds division-by-zero and negative array access bugs without executing code.

### Concept → Code Mapping

| Exam Concept | Where in Your Code | What You Must Explain |
|---|---|---|
| JVM bytecode (L1) | `SignInterpreter.java` — ASM framework | Stack-based VM. `ICONST_3` pushes 3. `IADD` pops two, pushes sum. `ILOAD_1` pushes local slot 1. |
| Sign lattice (L6) | `SignValue.java` | Powerset of {−, 0, +} + BOTTOM. Bitmask: MINUS=001, ZERO=010, PLUS=100. Join = bitwise OR. |
| Transfer functions (L6) | `SignTransferRelation.java` | NEG flips signs. ADD: same→same, zero→other, mixed→TOP. MUL: 0×x=0, same→+, diff→−. DIV: 0/x=0, x/0=BOTTOM, same→ZERO_PLUS, diff→ZERO_MINUS. |
| Pairwise decomposition (L6) | `SignTransferRelation.java` | For composites, decompose into singletons, compute 3×3=9 rules pairwise, join results. More precise than 8×8 lookup. |
| Abstract interpretation (L6) | Entire project | Galois connection: α(concrete)→abstract sign, γ(abstract)→set of integers. |
| Minimal fixpoint (L6) | ASM `Analyzer` | Worklist algorithm runs automatically. Monotone functions on finite lattice (8 elements) converge in ≤7 steps. No widening needed. |
| Data flow analysis (L5) | ASM `Analyzer` + `SignInterpreter` | Forward may analysis. Values flow from defs to uses. At joins, values merge (join = OR). |
| Interprocedural analysis (L7) | `SignInterpreter.naryOperation()` | Same-class calls: new Analyzer, analyze callee, join all IRETURN values, propagate back. External → TOP. |
| Context-insensitive (L7) | Design decision | Each method analyzed once regardless of callers. Fast, loses precision. |
| Soundness (L0) | Design decision | Conservative: no false negatives for div-by-zero. May have false positives (warnings) because condition narrowing not implemented. |

### Key Pitfalls

- Division by zero = BOTTOM (undefined), not TOP (could be anything).
- Java integer division truncates toward zero: −1/2 = 0, not −1. So MINUS/MINUS → ZERO_PLUS.
- `if (x > 0)` does NOT narrow x to PLUS inside the branch. Analysis is path-insensitive.
- IASTORE stack: [arrayref, index, value]. Code checks stackSize−1 for both IALOAD and IASTORE — correct for IALOAD (index is top) but wrong for IASTORE (value is top, index is second). Tests don't catch it. If asked about array writes, acknowledge this.

---

## Project 3: Slicing

**Path:** `projects/software-analyse/ss26saslicing-putra01/`
**Status:** Finished

**What it does:** Intra-procedural dynamic backward slicer for Java bytecode. Builds CFG → PDT → CDG → DDG → PDG, then computes backward slices. For dynamic slicing, instruments bytecode to track coverage, runs a test, removes unvisited nodes from PDG.

### Concept → Code Mapping

| Exam Concept | Where in Your Code | What You Must Explain |
|---|---|---|
| Control Flow Graph (L4) | `CFGExtractor` | Nodes = basic blocks (single entry, single exit). Edges = control transfers. Synthetic Entry/Exit nodes. |
| Basic blocks (L4) | `CFGExtractor` | Leaders: first instruction, jump targets, instructions after jumps. |
| Dominance (L4) | `DominatorTree` | A dominates B iff every path Entry→B passes through A. Entry dominates everything. |
| Post-dominance (L4) | `PostDominatorTree.computeResult()` | Reverse CFG, compute dominator sets by fixpoint, find immediate dominators, add edges n→idom(n). |
| Control dependence (L4) | `ControlDependenceGraph.computeResult()` | B control-dependent on A iff A post-dominates B's predecessor but NOT B. FOW algorithm: for each edge A→S in CFG, find LCA of A and S in PDT, walk from S up to L, add CDG edges A→x. |
| Reaching definitions (L5) | `DataDependenceGraph.computeResult()` | Forward may analysis. IN(n) = ⋃OUT(p). OUT(n) = GEN(n) ∪ (IN(n) \ KILL(n)). KILL kills same-variable defs. |
| usedBy / definedBy (L5) | `asm-defuse` library's `DefUseAnalyzer` | `usedBy(insn)` = variables read. `definedBy(insn)` = variables written. Cache per MethodNode. |
| Program Dependence Graph (L8) | `ProgramDependenceGraph.computeResult()` | PDG = CDG ∪ DDG. Union of control and data dependence edges. |
| Backward slice (L8) | `backwardSlice(pCriterion)` | Graph reachability backward from criterion node in PDG. Collect all transitive predecessors. Includes criterion itself. |
| Dynamic slicing (L8, L9) | `SlicerUtil.simplify()` + `CoverageTracker` | Instrument bytecode → run test → get visited lines → remove unvisited nodes from PDG → backward slice on reduced PDG. Dynamic slice ≤ static slice. |
| Bytecode instrumentation (L9) | `LineCoverageTransformer.transform()` | ClassFileTransformer using ASM9. `visitLineNumber()` inserts `CoverageTracker.trackLineVisit(line)` after each LINENUMBER. |
| Static vs dynamic tradeoff (L9) | Design decision | Static: all executions, sound, imprecise. Dynamic: one execution, precise, incomplete. |

### Key Pitfalls

- Do NOT add CDG edges from Entry. Do NOT make unmarked nodes dependent on Entry.
- Entry/Exit have line number −1, so they are removed in dynamic slicing (correct: only real executed lines matter).
- Dynamic slice is always ≤ static slice (fewer false positives).

---

## How the Three Projects Connect

```
Project 1 (Readability)        Project 2 (Sign Analysis)         Project 3 (Slicing)
│                              │                                 │
├─ Source code (Java)          ├─ Bytecode (JVM .class)          ├─ Bytecode (JVM .class)
├─ JavaParser → AST           ├─ ASM → Frame<SignValue>[]      ├─ ASM + JGraphT → ProgramGraph
├─ Visitor pattern            ├─ Interpreter pattern            ├─ Graph algorithms (FOW, worklist)
├─ Feature extraction         ├─ Transfer functions             ├─ Fixpoint iteration
├─ ML pipeline (WEKA)         ├─ Lattice theory                ├─ PDG construction
└─ Binary classification      └─ Bug detection (div-by-zero)    └─ Program slicing

Shared concepts:
├─ Rice's theorem → undecidability → approximation
├─ Soundness vs completeness tradeoff
├─ Static vs dynamic analysis (P2: static, P3: both)
├─ Data flow analysis framework (P2: sign propagation, P3: reaching definitions)
├─ Abstract interpretation (P2: sign lattice, P3: CFG as abstraction)
└─ JVM bytecode (P2: reads and interprets, P3: reads and instruments)
```

---

## What the Exam Actually Tests

**Format:** Multiple choice. But the professor said a big part tests your ability to explain your own codebases.

MC questions will describe scenarios from your projects and ask you to identify:
- The correct analysis result (e.g., "Given this sign lattice state, what is the output?")
- The concept being demonstrated (e.g., "Which algorithm builds the CDG?")
- The design decision (e.g., "Why context-insensitive?")
- The limitation (e.g., "Why warning instead of error?")

### Excluded Topics (confirmed by professor)

Naturalness, compiler workflow, lexical analysis, grammars, predictive parsing, syntax-directed translation, loop detection, DU/UD chains, available expressions, live variables, very busy expressions, MOP, meet over valid paths, heap analysis, SSA, interprocedural slicing, trace levels, AOP, fault localization, delta debugging, symbolic execution, dynamic symbolic execution.

---

## Study Checklist

### Project 1 — can you:
- [ ] Compute Shannon entropy given a token frequency table?
- [ ] Compute Halstead volume given N and η?
- [ ] Count cyclomatic complexity from a code snippet (decision points + 1)?
- [ ] Explain why standardization is needed (different feature scales)?
- [ ] Explain why 10-fold CV with fixed seed (not a separate test set)?
- [ ] Explain the VariableDeclarator `=` special case?

### Project 2 — can you:
- [ ] Trace the join of ZERO_PLUS (110) and PLUS_MINUS (101)?
- [ ] Compute MINUS / MINUS and explain why it's ZERO_PLUS (not PLUS)?
- [ ] Explain why division by exactly ZERO gives BOTTOM (not TOP)?
- [ ] Decompose (0+) − (0−) by hand and arrive at 0+?
- [ ] Explain why `if (x > 0)` doesn't narrow x → WARNING, not ERROR?
- [ ] Explain pairwise decomposition (3×3 singleton rules vs 8×8 table)?
- [ ] Explain context-insensitive analysis (one analysis per method)?
- [ ] Trace `ICONST_3 ICONST_4 IADD` stack states?
- [ ] Explain the inter-procedural analysis (same-class calls only)?

### Project 3 — can you:
- [ ] Define a basic block (single entry, single exit, no internal jumps)?
- [ ] Define dominance (every path Entry→B passes through A)?
- [ ] Define post-dominance (every path A→Exit passes through B)?
- [ ] Define control dependence (A post-dominates B's predecessor but not B)?
- [ ] Explain PDG = CDG ∪ DDG?
- [ ] Explain backward slice (graph reachability backward in PDG from criterion)?
- [ ] Explain why dynamic slice ≤ static slice?
- [ ] Explain bytecode instrumentation (modifies bytecode, no source change)?
- [ ] Trace the reaching definitions fixpoint for a small CFG?
- [ ] Explain the FOW algorithm for CDG construction (LCA in PDT, walk from S to L)?

---

## Connections

- [[software-analyse-concepts-by-project]] — The detailed concept-by-project mapping (this page is the condensed version)
- [[software-analyse-exam-prep]] — Full MC exam topic map with exclusions
- [[software-analyse-codebase-defense]] — Codebase walkthrough prep with practice Q&A
- [[mock-exam-software-analyse-2026-07-26]] — 40-question mock exam
- [[readability-classifier]] — Deep dive into Project 1 metrics
- [[sign-analysis]] — Deep dive into Project 2 lattice theory
- [[program-slicing]] — Deep dive into Project 3 slicing
- [[java-for-software-analysis]] — JVM/bytecode/Java ecosystem reference

---

## Open Questions

- None — all three projects complete, all exam topics mapped.
