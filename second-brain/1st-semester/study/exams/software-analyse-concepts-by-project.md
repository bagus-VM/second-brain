---
title: "Software Analyse — Concepts Grouped by Project"
tags: [exam-prep, software-analyse, projects, semester-1]
course: "Software Analyse"
exam_date: "2026-07-31"
status: current
last_updated: 2026-07-28
prerequisites: ["[[software-analyse-exam-prep]]", "[[software-analyse-codebase-defense]]"]
---

# Software Analyse — Concepts Grouped by Project

> The exam is MC but tests understanding of concepts as implemented in your three projects.
> This page groups every in-scope exam concept under the project that exercises it.
> Cross-cutting concepts that apply to multiple projects are listed under each project they touch.

---

## Project 1: Readability Classifier

**Location:** `projects/software-analyse/ss26sareadability-practice-putra01/`
**Status:** FINISHED (submitted)
**Exam topics covered:** Readability metrics, ML pipeline, tokens/lexemes, AST

### What the project does

Two-phase ML pipeline: (1) extract static code metrics from 200 Java snippets, (2) train logistic regression on those metrics to classify readable vs. not readable.

### Concepts exercised by this project

#### Readability Metrics (Lecture 2)

**Shannon Entropy** — [[readability-classifier]]
- Formula: H = -Σ p(token) × log₂(p(token))
- Measures vocabulary diversity. High entropy = many unique tokens. Low = repetitive.
- Worked example: 8 tokens, 2 unique (`int`, `=` appear twice), 4 singletons → H = -(2×0.25×(-2) + 4×0.125×(-3)) = 2.5 bits.
- Implementation: frequency map over token stream, compute p = count/total for each.
- Pitfall: 0×log₂(0) = 0 by convention (L'Hôpital), not undefined. Guard against division by zero in entropy.

**Halstead Volume** — [[readability-classifier]]
- Formula: V = N × log₂(η) where N = total operators+operands, η = unique operators+operands.
- N = N₁ + N₂ (total operators + total operands). η = η₁ + η₂ (unique operators + unique operands).
- Measures code density, not just length. 100 lines with 5 variables = low volume. 10 lines with 30 variables = high volume.
- Implementation: OperatorVisitor counts `=`, `+`, `&&`, `?:` etc. OperandVisitor counts variables, literals, field accesses.
- Pitfall: JavaParser's `VariableDeclarator` with initializer (`int x = 1`) is NOT an AssignExpr. OperatorVisitor has special handling to count the `=`.

**Cyclomatic Complexity** — [[readability-classifier]]
- Formula: M = E - N + 2P (or: decision points + 1)
- McCabe's metric: counts independent execution paths. Each `if`, `for`, `while`, `case`, `&&`, `||`, `?:` = +1.
- M=1 = straight line, M>10 = high defect risk.
- Implementation: `CyclomaticComplexityVisitor` visits AST nodes, counts decision points, returns count+1.
- Pitfall: ternary `?:` is counted as a decision point (`ConditionalExpr` in JavaParser).

**Number of Lines** — [[readability-classifier]]
- Count of all lines including blanks and comments. Split on `\r?\n`.
- Correlates with readability but is the weakest single metric (captures size, not structure).

#### Machine Learning Pipeline

**Feature Standardization (z-score)** — [[readability-classifier]]
- Halstead ranges 0-500, TokenEntropy 0-5. Without normalization, large-valued features dominate.
- Z-score: x' = (x - μ) / σ. Puts all features on mean=0, std=1 scale.
- Implemented with WEKA's `Standardize` filter wrapped in `FilteredClassifier`.

**Logistic Regression** — [[readability-classifier]]
- Gives probability estimates (not just Y/N), interpretable coefficients, linear decision boundary.
- Less overfitting than SVM/RF on small datasets (200 samples).
- Ridge parameter: λ=1e-6 for regularization.

**10-Fold Cross-Validation** — [[readability-classifier]]
- With only 200 samples, holding out a test set is wasteful. 10-fold CV uses all data: each sample tested exactly once.
- Fixed seed=1 → `new Random(1)` ensures fold split is reproducible.
- Pitfall: CV is an evaluation method, not normalization. Standardization happens inside each fold to avoid leakage.

**Threshold 3.6** — [[readability-classifier]]
- Ground truth is mean of 9 human raters on 1-5 scale. Threshold 3.6 splits ~50/50 readable vs. not readable.
- Avoids class imbalance. This is a LABEL threshold, not a feature scaling threshold.

#### Tokens and Lexemes (Lecture 2)

**Tokenization** — [[tokenization-and-token-types]]
- Splitting source code into tokens (keywords, identifiers, operators, literals, comments).
- Token = category+value (e.g., KEYWORD:if, IDENT:x). Lexeme = the raw text slice.
- Used by TokenEntropyFeature: JavaParser token stream → frequency distribution → entropy.

**AST** — [[abstract-syntax-tree]], [[parse-tree]]
- JavaParser builds AST from source code. Visitor pattern walks the tree to extract metrics.
- AST vs. parse tree: AST preserves only semantically meaningful constructs. Parse tree includes all grammar symbols.
- ConditionalExpr, IfStmt, ForStmt, BinaryExpr, AssignExpr — AST node types used by the metrics.

### Project 1 exam checklist

- [ ] Can you compute Shannon entropy given a token frequency table?
- [ ] Can you compute Halstead volume given N and η?
- [ ] Can you count cyclomatic complexity given a code snippet (decision points + 1)?
- [ ] Can you explain why standardization is needed (different feature scales)?
- [ ] Can you explain why 10-fold CV with a fixed seed (not a separate test set)?
- [ ] Can you explain: threshold 3.6 is for labeling, standardization is for features?
- [ ] Can you explain the VariableDeclarator `=` special case?

---

## Project 2: Sign Analysis

**Location:** `projects/software-analyse/ss26sasign-putra01/`
**Status:** FINISHED (all tests passing)
**Exam topics covered:** Sign lattice, transfer functions, bitmask encoding, interprocedural analysis, abstract interpretation, JVM bytecode, context sensitivity

### What the project does

Tracks abstract sign (−, 0, +) of integer values through Java bytecode using a lattice and transfer functions. After analysis converges, checks every IDIV instruction for division-by-zero and IALOAD/IASTORE for negative array index.

### Concepts exercised by this project

#### JVM & Bytecode (Lecture 1)

**Stack-based VM** — [[java-for-software-analysis]]
- JVM pushes/pops on an operand stack. `ICONST_3` pushes 3. `IADD` pops two, pushes sum.
- Local variables: slot 0 = `this` (instance methods), then parameters, then locals. `ILOAD_1` pushes slot 1.
- Instruction types: load/store (ILOAD, ISTORE), arithmetic (IADD, ISUB, IMUL, IDIV), control (IFEQ, IFGT, GOTO), stack (DUP, POP).
- Method calls: INVOKEVIRTUAL (instance dispatch), INVOKESTATIC (static method), INVOKESPECIAL (constructors, private, super).
- Sign analysis reads bytecode: ICONST_0 → ZERO, BIPUSH 100 → PLUS, IDIV → division transfer, IFEQ → branch.
- Worked example: `ICONST_3 ICONST_4 IADD` → stack before IADD is [3, 4] with 4 on top → IADD pops both, pushes 7.

#### Sign Lattice (Lecture 6: Abstract Interpretation)

**Lattice structure** — [[sign-analysis]], [[lattice]], [[abstract-interpretation]]
- Powerset of {−, 0, +} ordered by subset inclusion. 8 elements + BOTTOM.
- BOTTOM ⊂ {−} ⊂ {−,0} ⊂ ... ⊂ {−,0,+} = TOP.
- Join = set union = bitwise OR. Meet = set intersection = bitwise AND.
- isLessOrEqual: a ≤ b ⟺ (a | b) == b.

**Bitmask encoding** — [[sign-analysis]]
- MINUS=001 (1), ZERO=010 (2), PLUS=100 (4).
- ZERO_MINUS=011 (3), PLUS_MINUS=101 (5), ZERO_PLUS=110 (6).
- TOP=111 (7). BOTTOM=000 (0).
- join(a, b) = values()[a.ordinal() | b.ordinal()] — bitwise OR of ordinals.
- isMaybeZero(v) = (v & ZERO) != 0. isMaybeNegative(v) = (v & MINUS) != 0.
- UNINITIALIZED = sentinel for unassigned variables, NOT a lattice value.

**Transfer relations** — [[sign-analysis]]
- NEG: flip signs. 0 → 0, - → +, + → -. Composites: ZERO_MINUS (0,-) flips to ZERO_PLUS (0,+).
- ADD: same sign → same sign. Either zero → the other. Mixed → TOP.
- SUB: rewrite as lhs + NEG(rhs), apply ADD rules.
- MUL: 0 × x = 0. Same sign → +. Different → -.
- DIV: 0 / x = 0. x / 0 = BOTTOM (undefined). Same sign → ZERO_PLUS. Different → ZERO_MINUS.
- Java integer division truncates toward zero: -1/2 = 0, NOT -1.
- MINUS / MINUS → ZERO_PLUS (could be 0 or +, depending on magnitudes).

**Pairwise decomposition** — [[sign-analysis]]
- For composite operands, decompose into singletons and compute pairwise.
- result = BOTTOM. For each singleton a in LHS, for each singleton b in RHS: result = join(result, evalSingleton(OP, a, b)).
- Only needs 3×3=9 singleton rules. No 8×8 table.
- Worked example: (0+) - (0-). Decompose: {0,+} and {0,-}. Pairs: 0-0=0, 0-(-)=+, +-0=+, +-(-)=+. Join: 0 ∨ + ∨ + ∨ + = 0+.

#### Abstract Interpretation (Lecture 6)

**Galois connection (α, γ)** — [[galois-connection]], [[abstract-interpretation]]
- α: concrete → abstract (abstraction). e.g., α(5) = PLUS, α(-3) = MINUS, α(0) = ZERO.
- γ: abstract → concrete (concretization). γ(PLUS) = {x ∈ ℤ | x > 0}.
- Sign analysis uses the sign lattice as the abstract domain.

**Minimal fixpoint (MFP)** — [[minimal-fixed-point-algorithm]]
- ASM's Analyzer runs the worklist algorithm automatically. You provide transfer functions.
- Monotone transfer functions on a finite-height lattice (8 elements) converge in ≤ 7 steps per variable.
- No widening needed (finite lattice). Widening is needed for infinite-height lattices (intervals).

**Distributive framework** — [[distributive-framework]]
- When transfer functions are distributive: f(a ⊔ b) = f(a) ⊔ f(b). Then MOP = MFP (no precision lost).
- Sign analysis's pairwise decomposition is monotone (preserves over-approximation soundness).
- MOP (meet over all paths) is excluded from the exam, but the MOP=MFP condition is testable.

**Soundness and completeness** — [[soundness-and-completeness]], [[rices-theorem]]
- Rice's theorem: non-trivial semantic properties are undecidable. Static analysis approximates.
- Sound analysis: no false negatives for the property it checks. Sign analysis never misses a real div-by-zero.
- Incomplete: may have false positives (warnings that aren't real bugs) because condition narrowing is not implemented.
- PITFALL: `if (x > 0)` does NOT narrow x to PLUS inside the then-branch. x remains TOP at IDIV → WARNING.

#### Data Flow Analysis (Lecture 5)

**Gen/kill framework** — [[gen-kill-analysis]], [[data-flow-analysis]]
- Sign analysis is a forward may analysis: values flow from definitions to uses. At join points, values merge (join = OR).
- GEN(insn) = abstract value produced by instruction. KILL = old value replaced by new.
- Fixpoint iteration: apply transfer functions until values stop changing.

**Reaching definitions** — [[reaching-definitions]]
- Forward may analysis (union at joins). Definition reaches a point if any path carries it there.
- In sign analysis: abstract value of a variable reaches every use point reachable from its definition.

#### Interprocedural Analysis (Lecture 7)

**Context-insensitive analysis** — [[context-sensitivity]]
- Each method analyzed once regardless of how many callers. Fast, but loses precision.
- Sign analysis project: `getZero()` returns ZERO everywhere it's called, regardless of arguments.
- Contrast with context-sensitive: cloning (duplicate method per call site) or call strings (track call stack).

**Interprocedural recursion in the project** — [[interprocedural-analysis]]
- When bytecode calls a method in the same class: create new Analyzer, analyze callee, extract return value (join all IRETURN instructions), propagate back to caller.
- External method calls (not in same class) → return TOP (unknown).

### Project 2 exam checklist

- [ ] Can you trace the join of ZERO_PLUS (110) and PLUS_MINUS (101)?
- [ ] Can you compute MINUS / MINUS and explain why it's ZERO_PLUS (not PLUS)?
- [ ] Can you explain why division by exactly ZERO gives BOTTOM (not TOP)?
- [ ] Can you decompose (0+) - (0-) by hand and arrive at 0+?
- [ ] Can you explain why `if (x > 0)` doesn't narrow x → WARNING, not ERROR?
- [ ] Can you explain pairwise decomposition (3×3 singleton rules vs 8×8 table)?
- [ ] Can you explain context-insensitive analysis (one analysis per method)?
- [ ] Can you explain why no widening is needed (finite lattice, 8 elements)?
- [ ] Can you trace `ICONST_3 ICONST_4 IADD` stack states?
- [ ] Can you explain the inter-procedural analysis (same-class calls only)?

---

## Project 3: Slicing

**Location:** `projects/software-analyse/ss26saslicing-putra01/`
**Status:** FINISHED
**Exam topics covered:** Control flow graphs, basic blocks, dominance, post-dominance, control dependence, data dependence, PDG, program slicing (static + dynamic), dataflow analysis (reaching definitions, usedBy/definedBy), bytecode instrumentation, dynamic analysis

### What the project does

Implements an intra-procedural dynamic backward slicer for Java bytecode using ASM and JGraphT. Builds CFG → PDT → CDG → DDG → PDG, then computes backward slices over the PDG. For dynamic slicing, instruments bytecode to track line coverage, runs a test, removes unvisited nodes from the PDG.

### Concepts exercised by this project

#### Control Flow Analysis (Lecture 4)

**Control Flow Graph** — [[control-flow-graph]], [[basic-block]]
- CFG: nodes = basic blocks (single entry, single exit, no internal jumps). Edges = control transfers.
- Basic block leaders: first instruction, jump targets, instructions after jumps.
- Project: `CFGExtractor` builds CFG from bytecode using ASM. Synthetic Entry and Exit nodes connected to boundaries.

**Dominance** — [[dominance]], [[dominator-tree]]
- A dominates B iff every path from Entry to B passes through A. Entry dominates everything.
- Strict dominance: A dominates B and A ≠ B. Immediate dominator: the closest strict dominator.
- Dominator tree: edges from each node to its immediate dominator.

**Post-dominance** — [[post-dominance]], [[dominator-tree]]
- Post-dominance on the reversed CFG: B post-dominates A iff every path from A to Exit passes through B.
- Post-dominator tree = dominator tree of the reversed CFG, rooted at original Exit.
- Project: `PostDominatorTree.computeResult()` — reverse CFG, compute dominator sets by fixpoint iteration, find immediate dominators, add edges n → idom(n).

**Control dependence** — [[control-dependence]]
- B is control-dependent on A iff A post-dominates a predecessor of B but A does NOT post-dominate B.
- Intuition: B's execution hinges on the branching decision at A.
- CDG built using Ferrante-Ottenstein-Warren (FOW) algorithm.
- Project: `ControlDependenceGraph.computeResult()` — for each edge A→S in CFG, find LCA of A and S in PDT, walk from S up to L, add CDG edges A→x for each node x on path.
- PITFALL: Do NOT add edges from Entry. Do NOT make unmarked nodes dependent on Entry.

#### Data Flow Analysis (Lecture 5)

**Reaching definitions** — [[reaching-definitions]], [[gen-kill-analysis]]
- Forward may analysis (union at join points). Definition reaches a point if it does so on at least one path.
- IN(n) = ⋃ OUT(p) for all predecessors p. OUT(n) = GEN(n) ∪ (IN(n) \ KILL(n)).
- KILL kills definitions of the SAME variable, not just definitions from the same node.
- Project: `DataDependenceGraph.computeResult()` — compute reaching definitions, add data-dependence edge from each reaching def to each use.

**usedBy / definedBy** — [[data-flow-analysis]]
- `usedBy(insn)` = variables read by instruction (frame.getUses()). `definedBy(insn)` = variables written (frame.getDefinitions()).
- Implemented using asm-defuse library's `DefUseAnalyzer` which records def/use sets per instruction.
- Cache analyzer per MethodNode to avoid recomputation.

**Dead code elimination** — [[dead-code-elimination]]
- A definition is dead if it never reaches any use and has no side effects. Can be removed.
- Backward may analysis: liveness flows from uses backward to definitions.

**Register allocation** — [[register-allocation]]
- Uses liveness information to assign variables to registers. Variables that don't overlap in lifetime can share a register.

#### Program Slicing (Lecture 8)

**Program Dependence Graph** — [[program-dependence-graph]]
- PDG = CDG ∪ DDG. Combines control dependence edges and data dependence edges.
- Slicing = graph reachability on the PDG.
- Project: `ProgramDependenceGraph.computeResult()` — union of CDG and DDG, store as single ProgramGraph.

**Backward slice** — [[program-slicing]]
- Criterion (p, v): variable v at program point p. All statements that may affect v at p.
- Computed by backward graph traversal from criterion node in PDG. Collect all transitive predecessors.
- Project: `backwardSlice(pCriterion)` — worklist starting from criterion, add all predecessors transitively. Includes criterion node itself.
- Result: set of nodes that can influence the criterion's value.

**Forward slice** — [[program-slicing]]
- Criterion (p, v): which statements are affected by v at p. Forward graph traversal from criterion.
- Not implemented in the project, but exam may ask about the concept.

**Dynamic slicing** — [[dynamic-slicing]], [[program-slicing]]
- Uses recorded execution trace, not just program structure. Only includes statements that actually affected v in that run.
- More precise (fewer false positives than static), but requires trace.
- Dynamic slice ≤ static slice (always smaller or equal).
- Project flow: (1) build PDG, (2) instrument bytecode, (3) run test → CoverageTracker records visited lines, (4) simplify PDG by removing unvisited nodes, (5) backwardSlice on reduced PDG.

#### Dynamic Analysis (Lecture 9)

**Static vs dynamic tradeoff** — [[static-vs-dynamic-analysis]], [[dynamic-analysis]]
- Static: all possible executions → sound (over-approximation, catches all potential issues) but imprecise (false positives from infeasible paths).
- Dynamic: one specific execution → exact, no false positives for observed paths, but incomplete (misses bugs triggered by other inputs).
- Project: the slicing project implements both. Static slice is computed purely from PDG. Dynamic slice filters PDG by execution trace.

**Bytecode instrumentation** — [[dynamic-analysis]]
- Modifying compiled bytecode at load time or build time to insert monitoring code. No source changes.
- Project: `LineCoverageTransformer.transform()` — ClassFileTransformer using ASM9. `InstrumentationAdapter.visitLineNumber()` inserts `CoverageTracker.trackLineVisit(line)` call after each LINENUMBER instruction.
- Two common approaches: method-entry instrumentation (log method name at entry) and call-site instrumentation (log before each call).
- Heisenberg effect: instrumentation changes program behavior (mostly performance).

**Coverage tracking** — [[dynamic-analysis]]
- `CoverageTracker.trackLineVisit(int)` adds line number to static `LinkedHashSet<Integer>`.
- `CoverageTracker.getVisitedLines()` returns set of lines executed during test run.
- Used by `SlicerUtil.simplify()` to remove unvisited nodes from PDG for dynamic slicing.

#### CFG Concepts Used Throughout

**DataDependenceGraph construction steps** — [[data-flow-analysis]]
1. For each node, compute GEN (definitions from definedBy) and KILL (definitions of same variable).
2. Entry node defines method parameters (slot 0 = this for non-static, then args by slot size).
3. Initialize: OUT(n) = GEN(n) for all, IN(n) = ∅.
4. Iterate until fixpoint: IN(n) = ⋃OUT(p), OUT(n) = GEN(n) ∪ (IN(n) \ KILL(n)).
5. Build DDG: for each node n, for each used variable v, add edge from reaching def's node to n.

**SlicerUtil.simplify** — [[dynamic-slicing]]
- Get visited lines from CoverageTracker.
- Create reduced ProgramGraph: only nodes whose line number was visited.
- Only keep edges whose both endpoints survive.
- Entry/Exit have line number -1, so they are removed (correct for dynamic: only real executed lines matter).

### Project 3 exam checklist

- [ ] Can you define a basic block (single entry, single exit, no internal jumps)?
- [ ] Can you define dominance (every path Entry→B passes through A)?
- [ ] Can you define post-dominance (every path A→Exit passes through B)?
- [ ] Can you define control dependence (A post-dominates B's predecessor but not B)?
- [ ] Can you explain PDG = CDG ∪ DDG?
- [ ] Can you explain backward slice (graph reachability backward in PDG from criterion)?
- [ ] Can you explain forward slice (graph reachability forward from criterion)?
- [ ] Can you explain why dynamic slice ≤ static slice (fewer false positives)?
- [ ] Can you explain bytecode instrumentation (modifies bytecode to insert monitoring, no source change)?
- [ ] Can you trace the reaching definitions fixpoint for a small CFG?
- [ ] Can you explain the FOW algorithm for CDG construction (LCA in PDT, walk from S to L)?

---

## Cross-Cutting Concepts (Apply to All Projects)

These concepts don't belong to one project but are tested across them:

### Foundations (Lecture 1)

- [[rices-theorem]] — Non-trivial semantic properties are undecidable. Static analysis must approximate.
- [[soundness-and-completeness]] — Soundness = no false negatives for property checked. Completeness = no false positives. Trade-off forced by Rice's theorem.
- [[static-vs-dynamic-analysis]] — Static: all executions, sound, imprecise. Dynamic: one execution, precise, incomplete.

### Data Flow Analysis (Lecture 5) — used in Project 2 and 3

- [[data-flow-analysis]] — General framework: forward/backward × must/may.
- [[gen-kill-analysis]] — Forward may (reaching defs): union at joins, GEN adds defs, KILL removes same-var defs.
- [[reaching-definitions]] — Forward may: definitions that reach a point on at least one path.
- [[iterative-data-flow-analysis]] — Initialize, iterate until fixpoint, merge at join points.

### Abstract Interpretation (Lecture 6) — used in Project 2

- [[monotone-framework]] — Transfer functions must be monotone for fixpoint to exist.
- [[lattice]] — Partial order with join (⊔) and meet (⊓). Sign lattice = powerset of {−,0,+}.
- [[galois-connection]] — (α, γ) connects concrete and abstract domains.
- [[minimal-fixed-point-algorithm]] — Iterative algorithm computes MFP (≤ MOP for non-distributive).
- [[distributive-framework]] — When MOP = MFP (distributive transfer functions). Know the condition even though MOP itself is excluded.
- [[widening-narrowing]] — For infinite-height lattices (not needed for sign analysis: 8 elements).

### Interprocedural Analysis (Lecture 7) — used in Project 2

- [[context-sensitivity]] — Context-insensitive: one analysis per method. Context-sensitive: per call site.
- [[cloning-context-sensitivity]] — Duplicate method body per call context.
- [[call-strings]] — Track sequence of call sites. Longer = more context, state-space explosion.
- [[points-to-analysis]] — Steensgaard (union-find, fast, imprecise) vs. Andersen's (subset-based, cubic, precise).
- [[aliasing]] — Two pointers alias if they point to same object.

### Control Flow Analysis (Lecture 4) — used in Project 3

- [[control-flow-graph]] — Nodes = basic blocks, edges = control transfers.
- [[dominance]] — A dominates B iff every path Entry→B passes through A.
- [[post-dominance]] — B post-dominates A iff every path A→Exit passes through B.
- [[control-dependence]] — B control-dependent on A: A post-dominates B's predecessor but not B.
- [[dominator-tree]] — Immediate dominator edges.
- [[natural-loop]] — Loop structure (not loop detection algorithms: excluded).

---

## How the Three Projects Map to Each Other

The exam tests whether you can explain your own codebases and the concepts in them. Here's how the projects interconnect:

```
Project 1 (Readability)                Project 2 (Sign Analysis)          Project 3 (Slicing)
│                                      │                                  │
├─ Tokens, lexemes                     ├─ JVM bytecode                    ├─ CFG, basic blocks
├─ AST (JavaParser)                    ├─ Sign lattice (8 elements)        ├─ Dominance, post-dominance
├─ Shannon entropy                     ├─ Bitmask encoding                 ├─ Control dependence (CDG)
├─ Halstead volume                     ├─ Transfer functions               ├─ Data dependence (DDG)
├─ Cyclomatic complexity               ├─ Pairwise decomposition           ├─ PDG = CDG ∪ DDG
├─ Feature standardization             ├─ Fixpoint iteration (ASM)         ├─ Reaching definitions
├─ Logistic regression                 ├─ Interprocedural (same class)     ├─ Backward slice
├─ 10-fold CV, seed=1                  ├─ Context-insensitive              ├─ Dynamic slicing
└─ Threshold 3.6                       ├─ Soundness (conservative)         ├─ Bytecode instrumentation
                                      └─ Galois connection (α, γ)         └─ Coverage tracking

Shared concepts:
├─ Rice's theorem → undecidability → approximation
├─ Soundness vs completeness tradeoff
├─ Static vs dynamic analysis (P2: static, P3: both)
├─ Data flow analysis framework (P2: sign propagation, P3: reaching definitions)
├─ Abstract interpretation (P2: sign lattice, P3: CFG as abstraction)
└─ JVM bytecode (P2: reads and interprets, P3: reads and instruments)
```

### Reading the projects' code on the exam

The exam "big part tests ability to explain own codebases." MC questions describe code snippets or analysis scenarios and ask you to identify the correct result, concept, or limitation. 

For each project, know:
1. **Which exam topic each component maps to** (documented above)
2. **The data structures** (P2: SignValue enum, P3: ProgramGraph)
3. **The algorithms** (P2: pairwise decomposition + fixpoint, P3: FOW for CDG, worklist for backward slice)
4. **The design decisions** (P2: bitmask over lookup, P3: node reuse for stable IDs)
5. **The pitfalls** (P2: IASTORE stack layout, P3: no Entry edges in CDG)

---

## Connections

- [[software-analyse-exam-prep]] — Full MC exam topic map with excluded topics
- [[software-analyse-codebase-defense]] — Codebase walkthrough prep with practice Q&A
- [[mock-exam-software-analyse-2026-07-26]] — 40-question mock exam
- [[readability-classifier]] — Deep dive into Project 1 metrics
- [[sign-analysis]] — Deep dive into Project 2 lattice theory
- [[program-slicing]] — Deep dive into Project 3 slicing
- [[java-for-software-analysis]] — JVM/bytecode/Java ecosystem reference
- [[data-flow-analysis]] — General dataflow framework
- [[abstract-interpretation]] — Theoretical foundation
- [[control-flow-graph]] — CFG construction and analysis
- [[program-dependence-graph]] — PDG = CDG ∪ DDG

---

## Open Questions

- None remaining — all three projects complete, all exam topics mapped.