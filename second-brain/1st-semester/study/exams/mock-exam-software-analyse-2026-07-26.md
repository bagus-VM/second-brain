---
title: "Mock Exam — Software Analyse (Antwort-Wahl-Verfahren)"
tags: [exam-prep, mock-exam, software-analyse, multiple-choice, semester-1]
course: "Software Analyse"
exam_date: "2026-07-31"
format: "Antwort-Wahl-Verfahren (single-best-answer + multiple-select)"
status: current
last_updated: 2026-07-26
prerequisites: []
---

# Mock Exam — Software Analyse

> *40 questions. Einfachauswahl (single-best-answer) unless marked **[Mehrfachauswahl]** (zero, one, or more correct). 90 minutes. No notes. This is not a half-measure.*
>
> Scope: Lectures 2–10 + all 3 projects. Excluded topics per professor: symbolic execution, SSA, interprocedural slicing, MOP, heap analysis, fault localization, delta debugging, AOP, trace levels, DU/UD chains, available/live/very-busy expressions, loop detection, grammars, predictive parsing, SDT, naturalness, lexical analysis, compiler workflow.

---

## Section 1 — Foundations (Soundness, Completeness, Rice's)

### Q1. Rice's theorem states that:

a) Every non-trivial semantic property of programs is decidable
b) Every non-trivial semantic property of programs is undecidable
c) Only syntactic properties are undecidable
d) Static analysis can be both sound and complete for any non-trivial property

> [!note]- Solution
> **b)** Rice's theorem: every non-trivial semantic property of a Turing-complete language is undecidable. Static analysis must therefore approximate, trading soundness or completeness.

---

### Q2. A static analysis reports "no division by zero possible" for a program that actually has a div-by-zero on some input. This analysis is:

a) Sound but not complete
b) Complete but not sound
c) Both sound and complete
d) Neither

> [!note]- Solution
> **b)** Soundness = no false negatives (if analysis says "safe", it IS safe). Here the analysis said "safe" but it wasn't → false negative → unsound. Completeness = no false positives (if analysis says "unsafe", it IS unsafe). Completeness with respect to the property "detects bug" — but the framing is property-specific. Precise framing: for a safety property, soundness means catching ALL violations. Missing one → unsound. But many textbooks flip the names depending on the property direction. The reliable rule: soundness = the analysis result is truthful with respect to the concrete semantics.

---

### Q3. Rice's theorem forces static analysis to make a trade-off between soundness and completeness. Which statement best captures this?

a) Any non-trivial analysis must sacrifice soundness or completeness — a decidable approximation can't have both
b) Soundness and completeness can both be achieved if the analysis is fast enough
c) Soundness is always more important than completeness
d) Completeness is always more important than soundness

> [!note]- Solution
> **a)** Non-trivial semantic properties are undecidable (Rice). A decidable approximation must sacrifice: either miss some real issues (unsound), or flag some non-issues (incomplete). Both can't coexist for undecidable properties.

---

### Q4. [Mehrfachauswahl] Which of the following are consequences of Rice's theorem for static analysis?

a) Any sound analysis of a non-trivial property must be an over-approximation
b) Any complete analysis must miss some real bugs
c) Perfect precision and perfect recall are simultaneously unachievable
d) Dynamic analysis is also covered by Rice's theorem and is undecidable in the same way

> [!note]- Solution
> **a), c).** (a) A sound analysis that catches all real issues can't also avoid false positives (else it would decide the property). (c) Precision/recall trade-off is the direct consequence. (b) is wrong — a *complete* analysis with respect to the "reports all bugs" property would report all bugs, but that would make it decidable. The trap: completeness and soundness are dual; sacrificing one is enough for decidability. (d) is wrong — Rice's theorem is about *static* (non-executing) analysis. Dynamic analysis runs the program, sidestepping undecidability by observing actual executions (but becomes input-dependent).

---

## Section 2 — JVM & Bytecode

### Q5. The JVM is a:

a) Register-based virtual machine
b) Stack-based virtual machine
c) Hybrid (both registers and stack)
d) Pure interpreter with no operands

> [!note]- Solution
> **b)** JVM is a stack machine: instructions push/pop on an operand stack. `ICONST_5` pushes 5; `IADD` pops two ints, pushes their sum. This contrasts with register-based VMs (e.g. LuaJIT's Lua VM, Dalvik) where instructions name operand registers directly.

---

### Q6. Which bytecode instruction is used to invoke a static method?

a) INVOKEVIRTUAL
b) INVOKESTATIC
c) INVOKESPECIAL
d) INVOKEINTERFACE

> [!note]- Solution
> **b)** INVOKESTATIC — static methods don't need an instance. INVOKEVIRTUAL is for instance methods (virtual dispatch on `this` receiver). INVOKESPECIAL is for constructors (`<init>`), private methods, and superclass calls. INVOKEINTERFACE dispatches via interface table.

---

### Q7. What is the operand stack state immediately before `IADD` executes in this bytecode?

```
ICONST_3
ICONST_4
IADD
```

a) [3, 4] (3 at top)
b) [3, 4] (4 at top)
c) []
d) [7]

> [!note]- Solution
> **b)** `ICONST_3` pushes 3: [3]. `ICONST_4` pushes 4 on top: [3, 4] (4 at top). IADD pops two operands (4 first, then 3), adds → 7, pushes: [7]. Before IADD = [3, 4] with 4 at the top.

---

### Q8. In JVM bytecode, how are local variables typically accessed?

a) By name
b) By slot index (0 = `this` for instance methods, then parameters, then locals)
c) By reference to a global symbol table
d) Via the operand stack only

> [!note]- Solution
> **b)** Local variables live in slots indexed from 0. For instance methods slot 0 is `this`; slots 1..n hold parameters; subsequent slots hold locals declared in the method body. `ILOAD_1` pushes the value of slot 1; `ISTORE_2` pops into slot 2. Long/double values occupy two consecutive slots.

---

## Section 3 — Readability

### Q9. Given a code snippet with 8 tokens where `int` and `=` each appear twice and four other tokens appear once each (6 unique total) — the Shannon entropy is closest to:

a) 1.5 bits
b) 2.5 bits
c) 3 bits
d) 8 bits

> [!note]- Solution
> **b)** Two tokens with p=2/8=0.25 (log₂(0.25)=-2), four tokens with p=1/8=0.125 (log₂(0.125)=-3). H = -Σ p·log₂(p) = -(2×0.25×(-2) + 4×0.125×(-3)) = -(-1 + -1.5) = 2.5 bits. Key: entropy uses H = -Σ p·log₂(p); by convention 0·log₂(0)=0. High entropy = diverse vocabulary; low = repetitive.

---

### Q10. Halstead Volume V is computed as:

a) V = N × log₂(η) where N = total operators + operands, η = unique operators + operands
b) V = η × log₂(N)
c) V = N₁ + N₂
d) V = (N₁ + N₂) / (η₁ + η₂)

> [!note]- Solution
> **a)** V = N × log₂(η). N = (N₁ + N₂) total operators + operands. η = (η₁ + η₂) unique operators + operands. Halstead's theory treats code as a language with vocabulary size η and "length" N.

---

### Q11. Cyclomatic complexity M = E − N + 2P. What does "2P" represent in a method with a single connected component (P=1)?

a) Two entry points
b) The "+2" baseline — a method with no decision points has exactly one path (M=1)
c) Two operands
d) Two basic blocks

> [!note]- Solution
> **b)** For a single method P=1, M = E − N + 2. With no branches, the CFG has E edges, N nodes, and M resolves to 1 (the only path). The equivalent formula "decision points + 1" makes the baseline explicit. McCabe's original threshold: M > 10 → high defect risk.

---

### Q12. [Mehrfachauswahl] Why is feature standardization (z-score) applied before logistic regression in the readability classifier?

a) HalsteadVolume ranges 0–500 while TokenEntropy is 0–5 — without normalization HalsteadVolume dominates the linear weights
b) Standardization is the same as 10-fold cross-validation
c) Z-score puts all features on mean=0, std=1 scale so the model treats each contribution comparably
d) Standardization replaces the need for the threshold 3.6

> [!note]- Solution
> **a), c).** (a) and (c) describe the same reason: wildly different feature scales → the linear model's coefficients bias toward large-valued features. Standardization equalizes them. (b) is wrong — CV is an evaluation method, not normalization. (d) is wrong — the threshold 3.6 binarizes ground-truth scores (readable Y/N label), separate from feature scaling.

---

### Q13. 10-fold cross-validation with seed=1 in WEKA is used in the readability project because:

a) It produces a deterministic, reproducible evaluation of model accuracy without holding out a separate test set (only 200 samples)
b) It trains the model 10 times on all data
c) It's required by the logistic regression algorithm
d) It guarantees the classifier achieves 100% accuracy

> [!note]- Solution
> **a)** With only 200 samples, holding out a test set is wasteful. 10-fold CV uses all 200 for both training and testing (each sample tested exactly once). The fixed seed ensures the fold split is reproducible — `crossValidateModel(classifier, data, 10, new Random(1))`.

---

## Section 4 — Parsing (AST only)

### Q14. The key difference between a parse tree and an Abstract Syntax Tree (AST) is:

a) ASTs preserve every grammar token including punctuation; parse trees don't
b) Parse trees include every grammar symbol (including intermediate productions), ASTs abstract away syntactic sugar and keep only semantically meaningful constructs (operators, operands, statements)
c) ASTs are only for source code; parse trees are only for bytecode
d) There's no difference — they're synonyms

> [!note]- Solution
> **b)** A parse tree shows the full grammar derivation (every non-terminal expansion, all tokens, parentheses, semicolons — visible as leaves). An AST strips this down to what matters semantically: `IfStmt{cond, then, else}`, `BinaryExpr{op, lhs, rhs}`. AST nodes represent program constructs (expressions, statements, declarations), not grammar rules.

---

### Q15. In JavaParser, which AST node type represents a ternary expression `a ? b : c`?

a) IfStmt
b) ConditionalExpr
c) BinaryExpr
d) SwitchStmt

> [!note]- Solution
> **b)** `ConditionalExpr` — ternary `?:`. Common AST node types: IfStmt, ForStmt, WhileStmt, BinaryExpr (a+b, a==b), UnaryExpr (!a, -a), MethodCallExpr, AssignExpr, VariableDeclarator, FieldAccessExpr, ConditionalExpr. The `CyclomaticComplexityVisitor` counts ternaries as a decision point (+1).

---

## Section 5 — Sign Analysis

### Q16. Given the sign bitmask encoding (MINUS=001, ZERO=010, PLUS=100), what is the join of ZERO_PLUS (110) and PLUS_MINUS (101)?

a) TOP (111)
b) ZERO_MINUS (011)
c) PLUS (100)
d) ZERO (010)

> [!note]- Solution
> **a)** Join = bitwise OR: 110 | 101 = 111 = TOP. The sign lattice IS the powerset of {−, 0, +} ordered by subset inclusion — join is set union, captured by bitwise OR. The bottom (000) is empty set; top (111) is the full set.

---

### Q17. In sign analysis, the result of `MINUS / MINUS` (IDIV transfer function) is:

a) PLUS (100)
b) ZERO_PLUS (110)
c) ZERO (010)
d) TOP (111)

> [!note]- Solution
> **b)** Java integer division truncates toward zero. −1 / 2 = 0 (not −1, as floor division would give). So same-sign division can yield zero or the expected sign. MINUS / MINUS → ZERO_PLUS (could be 0 or +). The naïve "PLUS" answer forgets truncation — the classic exam trap.

---

### Q18. In sign analysis, what is the result when the divisor at IDIV has an abstract value of exactly ZERO?

a) TOP — the result could be anything
b) BOTTOM — the path is impossible / runtime error
c) ZERO — division by zero returns 0
d) A lattice element representing "NaN"

> [!note]- Solution
> **b)** Division by exactly zero → BOTTOM. BOTTOM means "undefined / impossible path". This is how analysis detects the bug: if divisor is exactly ZERO at IDIV → ERROR. If divisor is MAYBE zero (e.g. 0+ contains ZERO bit) → WARNING. Trap: confusing BOTTOM (definitely impossible) with TOP (anything possible) — opposites on the lattice.

---

### Q19. The pairwise decomposition for composite sign operands works by:

a) Looking up the answer in a precomputed 8×8 table
b) For each singleton bit set in LHS and each in RHS, compute the singleton rule, then join (OR) all results
c) Returning TOP for any composite operand
d) Taking the average of the two operand ordinals

> [!note]- Solution
> **b)** Decompose LHS and RHS into singletons {−, 0, +}, apply the 3×3 singleton rules to each pair, join (OR) all partial results. Monotonicity guarantees the result contains all possible concrete outcomes. Beats the 8×8 lookup table — you only encode 9 singleton rules, and the decomposition is automatic. The project uses this.

---

### Q20. Consider: `void f(int x) { if (x > 0) { int r = 100 / x; } }`. The analysis reports:

a) ERROR — x is exactly ZERO inside the then-branch
b) WARNING — x is TOP (parameter), isMaybeZero remains true; condition narrowing is NOT implemented so the `x > 0` guard doesn't refine x to PLUS
c) No report — the guard eliminates the zero possibility
d) BOTTOM — div by zero gives BOTTOM

> [!note]- Solution
> **b)** Parameters start as TOP. `if (x > 0)` does NOT narrow x inside the then-branch — the analysis doesn't track conditions. So x = TOP at IDIV, and isMaybeZero(TOP) = true → WARNING. This is a precision loss, not a missed detection; it's the conservative sound behavior. Without condition narrowing, you get false-positive warnings.

---

## Section 6 — Control Flow Analysis

### Q21. A basic block in a control flow graph is a maximal sequence of instructions such that:

a) It has one entry and multiple exits
b) It has multiple entries and one exit
c) It has a single entry (the first instruction) and a single exit (control leaves only after the last instruction) — no internal jumps
d) It contains exactly one instruction

> [!note]- Solution
> **c)** Single entry, single exit, no internal control-transfer instructions. Leaders (block entries) are: the first instruction, any jump target, any instruction following a jump. Splitting code into basic blocks happens at these boundaries.

---

### Q22. Node A dominates node B in a CFG if:

a) There's a path from A to B
b) Every path from the entry node to B passes through A
c) A is immediately before B
d) A has more edges than B

> [!note]- Solution
> **b)** Dominance is path-based: A dominates B iff every path from entry to B contains A. The entry node dominates every node. Strict dominance: A dominates B and A ≠ B. Immediate dominator: the unique strict dominator closest to B. The dominator tree is built from immediate-dominator edges.

---

### Q23. Post-dominator is defined on the reversed CFG (swap entry/exit). B post-dominates A if:

a) Every path from the exit node to A passes through B
b) Every path from A to the exit node passes through B
c) B is reachable from A
d) B is the immediate successor of A

> [!note]- Solution
> **b)** Post-dominance reverses the edges: B post-dominates A iff every path from A to the exit contains B. Post-dominator tree is built by finding dominators on the reversed CFG. Control dependence uses post-dominance: B is control-dependent on A iff A post-dominates B's predecessor but A does not post-dominate B.

---

### Q24. Node B is control-dependent on node A in a CFG if:

a) B always executes when A executes
b) A post-dominates a predecessor of B but A does not post-dominate B; B's execution depends on the branching decision at A
c) A directly precedes B
d) There's a data flow from A to B

> [!note]- Solution
> **b)** Control dependence: B's execution hinges on the branch decision at A. Formally: A post-dominates some predecessor of B, but A does not post-dominate B. There must be a path from A to B where A post-dominates every node except B. The Control Dependence Graph (CDG), built from the post-dominator tree, is part of the PDG (CDG ∪ DDG) used in slicing.

---

## Section 7 — Data Flow Analysis

### Q25. Reaching-definitions analysis is which kind of dataflow framework?

a) Forward, must (intersection at join points)
b) Forward, may (union at join points)
c) Backward, must
d) Backward, may

> [!note]- Solution
> **b)** Reaching definitions = forward may. "Forward" because information flows from definitions to uses along program order. "May" because a definition reaches a point if it does so on at least one path → join = union. Must analyses (e.g. available expressions) use intersection. Dead-code analysis is backward. The four-axis framework: (forward/backward) × (must/may).

---

### Q26. [Mehrfachauswahl] Which of the following correctly pair dataflow analyses with their direction and must/may?

a) Reaching definitions → forward, may (union)
b) Available expressions → forward, must (intersection)
c) Live variables → backward, may (union)
d) Very busy expressions → forward, must

> [!note]- Solution
> **a), b), c).** (a) forward may; (b) forward must; (c) backward may. (d) is wrong — very busy expressions are **backward, must** (expressions computed on all paths before a point). The pattern: "must" → intersection; "may" → union; "forward" → definition-to-use direction; "backward" → use-to-definition direction.

---

### Q27. Dead code elimination removes a statement if:

a) It's the first statement of the method
b) Its result is never used in any subsequent reachable program point (definition doesn't reach any use), and it has no side effects
c) It's inside a loop body
d) It contains an arithmetic operator

> [!note]- Solution
> **b)** A definition is dead if it never reaches any use. Combined with no side effects (e.g. `x = 5` with `x` never read), it can be removed. The analysis is a backward may framework: liveness information flows from uses backward to definitions. Pure side-effect-free computation to a dead variable is a classic elimination target.

---

## Section 8 — Abstract Interpretation

### Q28. The Galois connection (α, γ) in abstract interpretation has α as the:

a) Concretization function (abstract → concrete)
b) Abstraction function (concrete → abstract)
c) Both directions
d) A synonym for the transfer function

> [!note]- Solution
> **b)** α: concrete → abstract (abstraction). γ: abstract → concrete (concretization — yields the set of concrete values represented). The adjunction holds: α monotone, γ monotone, and γ∘α gives the best safe approximation. The diagram is concrete_domain ⇄ abstract_domain connected by (α, γ).

---

### Q29. Iterative dataflow on a finite-height lattice is guaranteed to terminate because:

a) The transfer functions are distributive
b) Monotone functions over a finite-height lattice have only finitely many ascending steps before reaching a least fixpoint
c) The analyzer uses a worklist with topological order
d) TOP acts as a sentinel that stops iteration

> [!note]- Solution
> **b)** Monotone functions: each iteration either leaves the value unchanged (fixpoint) or produces a strictly greater element (in the lattice order). A finite-height lattice bounds ascending chains — the algorithm reaches the least fixpoint in at most height × (CFG size) iterations. For infinite-height lattices (intervals), you need widening to force convergence.

---

### Q30. A distributive framework satisfies MOP = MFP (the meet-over-all-paths equals the minimal fixpoint). This means:

a) Any distributive analysis converges instantly
b) For distributive transfer functions, the iterative algorithm computes the IDEAL result (merging each path individually) — no precision is lost
c) MFP is always more precise than MOP
d) Distributivity is required for termination

> [!note]- Solution
> **b)** Distributive transfer functions: f(a ⊔ b) = f(a) ⊔ f(b). This equality means the merge-at-join-points approach (MFP via iterative algorithm) yields exactly the all-paths meet (MOP) — no precision lost. For non-distributive frameworks MFP ≤ MOP (MOP is more precise but undecidable in general). Note: MOP *itself* is excluded from the exam, but you should know the distributive case gives MOP = MFP.

---

### Q31. Widening is needed for:

a) Any lattice with TOP
b) Infinite-height lattices (e.g. interval domain with unbounded bounds) to force convergence by coarsening the value after a bounded number of steps
c) Distributive frameworks only
d) Forward analyses only

> [!note]- Solution
> **b)** Widening accelerates convergence for infinite-height lattices where ascending chains might not stabilize in finite steps (e.g. [0,0] → [0,1] → [0,2] → ...). The widening operator jump-summarizes the trend (e.g. to [0,∞)). Narrowing refines the over-approximation back afterward. The sign lattice is finite-height (8 elements), so no widening needed — terminate in ≤7 steps.

---

## Section 9 — Interprocedural Analysis

### Q32. Context-insensitive analysis analyzes each method:

a) Once per call site (context-sensitive)
b) Once total, regardless of how many distinct callers/argument values invoke it
c) Twice (forward + backward pass)
d) Only if the method mutates shared state

> [!note]- Solution
> **b)** Context-insensitive = one analysis per method, same abstract result for all callers. Fast but loses precision when a method's behavior depends on arguments. The sign analysis project uses this: `getZero()` is analyzed once, its return (ZERO) used wherever it's called. Context-sensitive variants (cloning, call strings) re-analyze per calling context.

---

### Q33. [Mehrfachauswahl] Which statements about Steensgaard's vs Andersen's points-to analyses are correct?

a) Steensgaard is unification-based (equality via union-find) — near-linear time, less precise
b) Andersen's is subset-based — cubic time, more precise
c) Steensgaard is more precise than Andersen's
d) Andersen's can distinguish `p → obj1` and `q → obj1` separately; Steensgaard merges them

> [!note]- Solution
> **a), b), d).** Steensgaard: fast (near-linear via union-find), imprecise because any shared allocation site causes unification. Andersen's: subset constraints, more precise but cubic. (c) is backwards. The project doesn't implement either — it's sign analysis — but the theory lecture covers both as canonical points-to algorithms.

---

### Q34. Call strings as a context-sensitivity technique:

a) Track the sequence of call sites leading to the current method (the longer the string, the more context, but state space explodes)
b) Ignore all call context
c) Always have bounded length by definition
d) Are equivalent to context-insensitive analysis

> [!note]- Solution
> **a)** Call string = the stack of call sites that brought us to this method. Longer strings = more context sensitivity, but unbounded length causes state-space explosion. Practical implementations cap the length (k-call-string sensitivity). Contrast with cloning/inlining, which duplicates the method body per context.

---

### Q35. Cloning/inlining as a context-sensitivity technique works by:

a) Duplicating the method body (conceptually or in the CFG) for each calling context, then analyzing each copy independently
b) Recording only return values per caller
c) Skipping the callee body entirely
d) Combining all callers into one merge point

> [!note]- Solution
> **a)** Cloning effectively creates a fresh copy of the method for each call site or context, so each copy can have distinct abstract states. More precise than context-insensitive, but blows up method count. Inlining is the same idea at the CFG level — splice the callee's CFG into the caller. The trade-off: precision vs. cost.

---

## Section 10 — Program Slicing

### Q36. The backward slice of variable `v` at program point `p` is:

a) All statements that are affected by `v` at `p`
b) All statements that may affect the value of `v` at `p` (graph reachability backward in the PDG from the criterion)
c) All statements that execute after `p`
d) All statements inside the function containing `p`

> [!note]- Solution
> **b)** Backward slice = "what affects this?" Criterion (p, V) → all statements that could influence V at p, found by traversing control and data dependence edges backward in the PDG from the criterion node. Forward slice = "what does this affect?" — reachability forward from (p, V).

---

### Q37. The Program Dependence Graph (PDG) has edges representing:

a) Only data dependences
b) Only control dependences
c) Both control dependences and data dependences (PDG = CDG ∪ DDG)
d) Only call edges between procedures

> [!note]- Solution
> **c)** PDG = CDG ∪ DDG. CDG (Control Dependence Graph) is built from the post-dominator tree. DDG (Data Dependence Graph) traces reaching definitions from definitions to uses. Forward/backward slicing is reachability in the PDG along these edges. SSA (excluded from exam) and interprocedural slicing / SDG (also excluded) extend this.

---

### Q38. Dynamic slicing, contrasted with static slicing, is:

a) A slice computed over all possible inputs — most conservative
b) A slice computed for one specific execution trace — more precise (fewer false positives) than static, but requires the trace
c) Equivalent to static slicing
d) Always produces a larger slice than static

> [!note]- Solution
> **b)** Dynamic slicing uses a recorded execution trace and only includes statements that actually affected the variable in that run. Removes infeasible-path false positives that static slicing can't avoid. The cost: you must record the trace (instrumentation overhead, terabytes possible). Always smaller than or equal to the static slice.

---

## Section 11 — Dynamic Analysis

### Q39. The fundamental trade-off between static and dynamic analysis is:

a) Static is fast, dynamic is slow
b) Static is sound (over-approximates, catches all potential issues) but imprecise (false positives); dynamic is precise (no false positives for observed paths) but incomplete (only covers tested inputs)
c) Static is always better than dynamic
d) Dynamic is undecidable

> [!note]- Solution
> **b)** Static reasons about ALL possible executions → sound but conservative → false positives on infeasible paths. Dynamic observes ONE execution → exact for that run → no false positives observed → but misses bugs triggered only by other inputs. Neither subsumes the other; hybrid analyses (concolic execution, not on exam) bridge the gap.

---

### Q40. Bytecode instrumentation for dynamic analysis is best described as:

a) Editing the source code by hand to add `print` statements
b) Modifying the compiled bytecode at load time or build time to insert monitoring code (e.g. method entry hooks, call-site recording) without changing source
c) Running the program under a debugger
d) Decompiling the binary back to source

> [!note]- Solution
> **b)** Instrumentation injects monitoring code at the bytecode level (often via ASM or a JVM agent). Two common approaches: method-entry instrumentation (log the method name at the start of each method) and call-site instrumentation (log just before each method call). The observer effect (Heisenberg): instrumentation itself changes program behavior, mostly performance. AOP (excluded from exam) is one way to express instrumentation declaratively.

---

*Let's cook. 🔬*

> *Key self-check questions: Can you trace the lattice join MINUS/0+/TOP by hand? Can you compute Halstead volume given N and η? What does "forward may = union" vs "backward must = intersection" buy you? When is widening necessary? What does `temperature=0` guarantee on a CPU vs GPU?*