---
title: "Software Analyse — Definitions & Formulas Cheatsheet"
tags: [exam-prep, cheatsheet, software-analyse, semester-1]
course: "Software Analyse"
exam_date: "2026-07-31"
status: current
last_updated: "2026-07-28"
---

# Software Analyse — Cheatsheet

> Definitions and formulas only. Excluded topics are NOT listed here. For context, see [[software-analyse-exam-prep]] and [[software-analyse-concepts-by-project]].

---

## Foundations

### Rice's Theorem

Every non-trivial semantic property of a Turing-complete program is undecidable.

### Soundness and Completeness

| Term | Definition |
|------|-----------|
| Sound | If the analysis says X, X is actually true (no false negatives for the property) |
| Complete | If X is true, the analysis says X (no false positives) |
| Trade-off | Rice's theorem forces sacrificing one: sound = over-approximation, complete = under-approximation |
| Static analysis | Always an approximation — cannot be both sound and complete for non-trivial properties |

### Static vs Dynamic Analysis

| Property | Static | Dynamic |
|----------|-------|---------|
| Scope | All possible executions | One specific execution |
| Soundness | Sound (over-approximates) | Exact for observed run |
| Precision | Imprecise (false positives from infeasible paths) | Precise (no false positives observed) |
| Completeness | Covers all paths | Incomplete (misses bugs from other inputs) |

---

## Readability (Project 1)
![[Pasted image 20260730213021.png]]
### Shannon Entropy

H = -Σ p(token) × log₂(p(token))

- p(token) = count of token / total token count
- 0 × log₂(0) = 0 by convention (L'Hôpital's rule)
- Low entropy ≈ 0: repetitive, predictable code
- High entropy ≈ log₂(n): all tokens unique, diverse vocabulary

### Halstead Volume

V = N × log₂(η)

- N = N₁ + N₂ (total operators + total operands)
- η = η₁ + η₂ (unique operators + unique operands)
- N₁ = total operator count, n₁ = unique operator count
- N₂ = total operand count, n₂ = unique operand count
- If η = 0, return 0 (avoid log(0))

### Cyclomatic Complexity

M = E - N + 2P

- E = edges in CFG, N = nodes in CFG, P = connected components (usually 1)
- Simplified: M = (number of decision points) + 1
- Decision points: `if`, `for`, `while`, `case`, `&&`, `||`, `?:`
- Base: M=1 (straight-line code), M>10 = high defect risk

### ML Pipeline

| Component | Detail |
|-----------|--------|
| Feature standardization | Z-score: x' = (x - μ) / σ. Puts all features on mean=0, std=1 scale |
| Why standardize | Halstead ranges 0-500, TokenEntropy 0-5. Without normalization, large features dominate |
| Logistic regression | Probability estimates, interpretable coefficients, ridge λ=10⁻⁶ |
| 10-fold cross-validation | All 200 samples used for train+test. Each tested exactly once. Seed=1 for reproducibility |
| Threshold 3.6 | Mean of 9 human raters on 1-5 scale. ≥3.6 = readable (Y). Splits ~50/50, avoids class imbalance |

### Tokens and AST

| Term | Definition |
|------|-----------|
| Token | Category + value (e.g., KEYWORD:if, IDENT:x) |
| Lexeme | The raw text slice from source |
| Parse tree | Full grammar derivation (all non-terminals, tokens, punctuation) |
| AST | Abstracts away syntactic sugar, keeps only semantically meaningful constructs |
| `ConditionalExpr` | AST node for ternary `a ? b : c` (counted as decision point) |
| `VariableDeclarator` | `int x = 1` — the `=` is implicit, not an AssignExpr. OperatorVisitor counts it specially |

---

## JVM & Bytecode

### JVM Architecture

| Property | Detail |
|----------|--------|
| Type | Stack-based VM (not register-based) |
| Operand stack | Instructions push/pop. `ICONST_3` pushes 3. `IADD` pops two, pushes sum |
| Local variables | Slot 0 = `this` (instance methods), then parameters, then locals. `ILOAD_1` pushes slot 1 |

### Key Instructions

| Instruction | Purpose |
|-------------|---------|
| ICONST_0..5, BIPUSH, SIPUSH, LDC | Push constants |
| ILOAD, ISTORE | Load/store local variable |
| IADD, ISUB, IMUL, IDIV | Integer arithmetic |
| IFEQ, IFGT, GOTO | Control transfer |
| DUP, POP | Stack manipulation |
| INVOKEVIRTUAL | Instance method dispatch (virtual on `this` receiver) |
| INVOKESTATIC | Static method call (no instance) |
| INVOKESPECIAL | Constructors (`<init>`), private methods, super calls |
| INVOKEINTERFACE | Interface dispatch via interface table |
| IALOAD | Array load (stack: [arrayref, index] → [value]) |
| IASTORE | Array store (stack: [arrayref, index, value] → []) |
| IRETURN | Return integer from method |

### Stack Tracing

```
ICONST_3    → stack: [3]
ICONST_4    → stack: [3, 4]  (4 on top)
IADD        → pops 4 and 3, pushes 7 → stack: [7]
```

---

## Sign Analysis (Project 2)
![[Pasted image 20260730213001.png]]
### Sign Lattice (Bitmask Encoding)

| Value | Symbol | Ordinal | Bits | Meaning |
|-------|--------|---------|------|---------|
| BOTTOM | ⊥ | 0 | 000 | Impossible / undefined |
| MINUS | {−} | 1 | 001 | Definitely negative |
| ZERO | {0} | 2 | 010 | Definitely zero |
| ZERO_MINUS | {0,−} | 3 | 011 | Zero or negative |
| PLUS | {+} | 4 | 100 | Definitely positive |
| PLUS_MINUS | {+,−} | 5 | 101 | Positive or negative |
| ZERO_PLUS | {0,+} | 6 | 110 | Zero or positive |
| TOP | ⊤ | 7 | 111 | Could be anything |

Lattice: powerset of {−, 0, +} ordered by subset inclusion.

### Lattice Operations

| Operation | Formula |
|-----------|---------|
| join(a, b) | `a.ordinal() \| b.ordinal()` (bitwise OR) |
| a ≤ b | `(a.ordinal() \| b.ordinal()) == b.ordinal()` |
| contains(a, singleton) | `(a & singleton) != 0` (bitwise AND) |
| isMaybeZero(v) | v has ZERO bit set (v == ZERO \|\| v == ZERO_MINUS \|\| v == ZERO_PLUS \|\| v == TOP) |
| isMaybeNegative(v) | v has MINUS bit set |

### Transfer Rules (Singletons)

| Operation | Rule |
|-----------|------|
| NEG | Flip: −→+, +→−, 0→0. Composites: ZERO_MINUS ↔ ZERO_PLUS |
| ADD(a, b) | Either zero → return other. Same sign → same sign. Mixed → TOP |
| SUB(a, b) | Rewrite as ADD(a, NEG(b)) |
| MUL(a, b) | Either zero → ZERO. Same sign → PLUS. Different → MINUS |
| DIV(a, b) | If b=ZERO → BOTTOM. If a=ZERO → ZERO. Same sign → ZERO_PLUS. Different → ZERO_MINUS |

### Java Integer Division Truncation

`−1 / 2 = 0` (truncation toward zero, NOT floor division which gives −1).

This means: same-sign division (−/− or +/+) yields ZERO_PLUS (could be 0 or +), not just PLUS.

### Pairwise Decomposition

```
result = BOTTOM
for each singleton a in LHS:
    for each singleton b in RHS:
        result = join(result, evalSingleton(OP, a, b))
return result
```

Only 3×3=9 singleton rules needed. No 8×8 lookup table.

**Worked example:** (0+) − (0−) = {0,+} − {0,−}
- Pairs: 0−0=0, 0−(−)=+, +−0=+, +−(−)=+
- Join: 0 ∨ + ∨ + ∨ + = 0+ = ZERO_PLUS

### Error Detection

| At instruction | Check | ERROR | WARNING |
|----------------|-------|-------|---------|
| IDIV | Divisor (stack top) | Exactly ZERO | isMaybeZero (ZERO bit set) |
| IALOAD | Index (stack top) | Exactly MINUS | isMaybeNegative (MINUS bit set) |
| IASTORE | Index | Exactly MINUS | isMaybeNegative |

### Key Properties

| Property | Detail |
|----------|--------|
| Condition narrowing | NOT implemented. `if (x > 0)` doesn't refine x to PLUS. Conservative = sound |
| Context sensitivity | Context-insensitive: each method analyzed once regardless of caller |
| Interprocedural | Only recurses for methods in same class. External calls → TOP |
| UNINITIALIZED | Sentinel for unassigned variables, NOT a lattice value |
| Fixpoint | ASM's Analyzer runs worklist algorithm automatically. Finite lattice (8 elements) → converges in ≤7 steps |
| Widening | NOT needed (finite-height lattice). Needed for infinite-height (intervals) |

---

## Abstract Interpretation

### Galois Connection (α, γ)

| Function | Direction | Definition |
|----------|-----------|-----------|
| α (abstraction) | Concrete → Abstract | α(5) = PLUS, α(-3) = MINUS, α(0) = ZERO |
| γ (concretization) | Abstract → Concrete | γ(PLUS) = {x ∈ ℤ \| x > 0} |

Adjunction: α monotone, γ monotone, γ∘α = best safe approximation.

### Monotone Framework

| Property | Requirement |
|----------|-------------|
| Transfer functions | Must be monotone: a ≤ b → f(a) ≤ f(b) |
| Lattice | Finite height → guaranteed termination (≤ height × CFG size iterations) |
| Fixpoint | Iterative algorithm computes MFP (minimal fixpoint) |

### Distributive Framework

Distributive: f(a ⊔ b) = f(a) ⊔ f(b)

When distributive: MOP = MFP (no precision lost). Iterative algorithm gives the ideal result.

For non-distributive: MFP ≤ MOP (MOP more precise but undecidable in general).

### Widening / Narrowing

| Technique | When needed | What it does |
|-----------|-------------|-------------|
| Widening | Infinite-height lattices (e.g., intervals [0,0]→[0,1]→[0,2]→...) | Coarsens value after bounded steps to force convergence (e.g., →[0,∞)) |
| Narrowing | After widening | Refines the over-approximation back toward the precise result |

Sign lattice: 8 elements, finite height, NO widening needed.

---

## Control Flow Analysis (Project 3)
![[Pasted image 20260730213045.png]]
### Basic Block

Maximal sequence of instructions with single entry (first instruction) and single exit (control leaves only after last instruction). No internal jumps.

Leaders: first instruction, jump targets, instructions following jumps.

### Dominance

| Term | Definition |
|------|-----------|
| A dominates B | Every path from Entry to B passes through A |
| Strict dominance | A dominates B AND A ≠ B |
| Immediate dominator (idom) | The unique strict dominator closest to B |
| Dominator tree | Edges from each node to its immediate dominator |

### Post-Dominance

| Term | Definition |
|------|-----------|
| B post-dominates A | Every path from A to Exit passes through B |
| Post-dominator tree | Dominator tree of the reversed CFG, rooted at original Exit |
| Construction | Reverse CFG, compute dominator sets by fixpoint, find idom, add edges n → idom(n) |

### Control Dependence

B is control-dependent on A iff:
- A post-dominates a predecessor of B
- A does NOT post-dominate B
- (B's execution depends on the branching decision at A)

### Natural Loops (structure only — no loop detection algorithms)

| Term | Definition |
|------|-----------|
| Natural loop | Single entry point (header) that dominates all nodes in the loop |
| Header | The single entry node, dominates the back-edge target |
| Back edge | Edge from node A to a dominator of A |
| Loop body | All nodes reaching the back-edge target without going through the header |

### CDG Construction (Ferrante-Ottenstein-Warren)

```
for each edge A → S in CFG:
    if A is Entry: skip
    L = getLeastCommonAncestor(A, S) in PDT
    x = S
    while x != L:
        add edge A → x in CDG
        x = predecessor of x in PDT
```

Do NOT add edges from Entry. Do NOT make unmarked nodes dependent on Entry.

---

## Data Flow Analysis

### Framework Dimensions

| Direction | Forward (def → use) | Backward (use → def) |
|-----------|--------------------|--------------------|
| May (union at joins) | Reaching definitions | Live variables |
| Must (intersection at joins) | Available expressions | Very busy expressions |

Only reaching definitions is in scope. The others are listed for context: forward/backward and must/may dimensions are testable, but the specific excluded analyses are not.

### Reaching Definitions (Forward May)

```
IN(n)  = ⋃ OUT(p)         for all predecessors p of n
OUT(n) = GEN(n) ∪ (IN(n) \ KILL(n))
```

- GEN(n) = definitions produced at n
- KILL(n) = definitions of the same variable at n (kills ALL definitions of that variable, not just from same node)
- Join = union (may analysis: reaches if ANY path carries it)
- Initialize: IN(n) = ∅, OUT(n) = GEN(n)

### Iterative Algorithm (Worklist)

```
for all n: IN(n) = ∅, OUT(n) = GEN(n)   (∅ for may, AllFacts for must)
worklist = all nodes
while worklist not empty:
    n = pick from worklist
    oldOUT = OUT(n)
    IN(n) = ⋃ OUT(p)   (or succ for backward)
    OUT(n) = GEN(n) ∪ (IN(n) \ KILL(n))
    if OUT(n) ≠ oldOUT:
        worklist += successors(n)   (or predecessors for backward)
```

### Dataflow Analyses in Scope

| Analysis | Direction | Must/May | Join | Scope |
|----------|-----------|----------|------|-------|
| Reaching definitions | Forward | May | Union | ✅ In scope |
| Dead code elimination | Backward | May | Union | ✅ In scope (concept) |
| Common subexpression elimination | — | — | — | ✅ In scope (concept) |
| Register allocation | Backward | — | — | ✅ In scope (concept) |

**Excluded:** Available expressions, live variables, very busy expressions, DU/UD chains.

---

## Interprocedural Analysis

### Context Sensitivity

| Technique | How | Precision | Cost |
|-----------|-----|-----------|------|
| Context-insensitive | Analyze each method once | Low | Cheap |
| Cloning/inlining | Duplicate method body per call site | High | Expensive (method count explodes) |
| Call strings | Track sequence of call sites | Medium-High | State-space explosion with long strings |
| Procedure summaries | Summary of callee effect as transfer function | Medium | Moderate (summary must be context-dependent for precision) |

### Points-to Analysis

| Algorithm | Approach | Time | Precision |
|-----------|----------|------|-----------|
| Steensgaard | Unification (union-find) | Near-linear | Less precise (any shared allocation site → unification) | No (flow-insensitive) |
| Andersen's | Subset-based constraints | Cubic | More precise (distinguishes p→obj1 and q→obj1) | No (flow-insensitive) |

Both are flow-insensitive (do not consider order of statements). Andersen's is field-sensitive if configured. Steensgaard is field-insensitive by default.

### Call String

Sequence of call sites leading to the current method. Longer = more context, but state space explodes. Practical: cap length (k-call-string sensitivity).

---

## Program Slicing (Project 3)

### Slicing Definitions

| Term | Definition |
|------|-----------|
| Backward slice BS(p, v) | All statements that may affect the value of v at program point p |
| Forward slice FS(p, v) | All statements whose value may be affected by v at p |
| Slice extraction | Remove all statements not in the slice. Result preserves the criterion's value |
| Computation | Graph reachability on the PDG (backward: predecessors, forward: successors) |

### Program Dependence Graph

PDG = CDG ∪ DDG

| Graph | Edges | Source |
|-------|-------|--------|
| CDG (Control Dependence Graph) | Control dependences | Post-dominator tree (FOW algorithm) |
| DDG (Data Dependence Graph) | Data dependences | Reaching definitions (def → use) |
| PDG | Union of CDG + DDG | Both |

### Backward Slice Algorithm

```
slice = {}
worklist = {criterion}
while worklist not empty:
    n = worklist.poll()
    if n not in slice:
        slice.add(n)
        for pred in PDG.predecessors(n):
            worklist.add(pred)
return slice
```

Slice includes the criterion node itself.

### Dynamic Slicing

| Property | Static | Dynamic |
|----------|--------|---------|
| Uses | Program structure (PDG) | Execution trace + PDG |
| Precision | Conservative (includes infeasible paths) | Precise (only executed lines) |
| Size | Larger | Dynamic slice ≤ static slice |
| Requirements | Just code | Must record trace (instrumentation) |

### Dynamic Slice Workflow (Project 3)

1. Build PDG from bytecode
2. Instrument bytecode (insert `CoverageTracker.trackLineVisit(line)`)
3. Run test → CoverageTracker records visited lines
4. Simplify PDG: remove nodes whose line was NOT visited
5. Backward slice on reduced PDG

### Bytecode Instrumentation

| Concept | Definition |
|---------|-----------|
| Instrumentation | Modify bytecode at load/build time to insert monitoring code. No source changes |
| InstrumentationAdapter | `visitLineNumber()` inserts `INVOKESTATIC CoverageTracker.trackLineVisit` after each LINENUMBER |
| LineCoverageTransformer | ClassFileTransformer using ASM9. Only instruments target package, skips Test classes |
| CoverageTracker | Static `LinkedHashSet<Integer>` of visited lines |
| SlicerUtil.simplify | Remove unvisited nodes from PDG. Keep only edges where both endpoints survive. Entry/Exit (line -1) are removed |

---

## Quick-Reference: All Formulas

| Formula | Context |
|---------|--------|
| H = -Σ p × log₂(p) | Shannon entropy (readability) |
| V = N × log₂(η) | Halstead volume (readability) |
| M = E - N + 2P | Cyclomatic complexity |
| M = decision_points + 1 | Cyclomatic complexity (simplified) |
| x' = (x - μ) / σ | Z-score standardization |
| join(a, b) = a \| b | Sign lattice join (bitwise OR) |
| a ≤ b ⟺ (a \| b) == b | Sign lattice order |
| IN(n) = ⋃ OUT(p) | Reaching definitions (forward may) |
| OUT(n) = GEN(n) ∪ (IN(n) \ KILL(n)) | Dataflow transfer function |
| PDG = CDG ∪ DDG | Program dependence graph |
| f(a ⊔ b) = f(a) ⊔ f(b) | Distributive framework condition |
| MOP = MFP | When distributive |
| −1 / 2 = 0 | Java integer division truncates toward zero |
| 0 × log₂(0) = 0 | Entropy convention |

---

## Trap: Common Exam Mistakes

| Wrong | Right |
|-------|-------|
| MINUS / MINUS = PLUS | MINUS / MINUS = ZERO_PLUS (truncation toward zero: could be 0 or +) |
| Division by zero = TOP | Division by zero = BOTTOM (undefined, not "anything") |
| `if (x > 0)` narrows x to PLUS | NOT implemented. x stays TOP → WARNING, not ERROR |
| oneOf = "at least one" | oneOf = EXACTLY one. anyOf = at least one |
| Reaching definitions is backward | Forward, may (union at joins) |
| PDG = DDG only | PDG = CDG ∪ DDG (both control and data dependence) |
| Static slice < dynamic slice | Dynamic slice ≤ static slice (dynamic is smaller or equal) |
| Cyclomatic complexity base = 0 | Base = 1 (straight-line code has one path) |
| VariableDeclarator `=` is AssignExpr | No. JavaParser makes it implicit. OperatorVisitor counts it specially |
| Widening needed for sign lattice | No. 8 elements = finite height = converges automatically |
| MOP is on the exam | MOP itself excluded. Only the MOP=MFP condition (distributive) is testable |
| IASTORE checks stack top | IASTORE stack: [arrayref, index, value]. Index is stackSize-2, NOT stackSize-1. Your code checks stackSize-1 for both IALOAD and IASTORE — potential bug |
| Steensgaard is field-sensitive | No. Both Steensgaard and Andersen's are flow-insensitive. Andersen's can be field-sensitive if configured |
| Natural loop requires loop detection algorithm | No. Loop detection algorithms are excluded. Only the structural definition (header, back edge, loop body) is testable |
| Procedure summaries are context-sensitive by default | No. A summary loses precision unless it is context-dependent (parameterized by call context) |