---
title: "Software Analyse Exam — Codebase Defense Prep"
tags: [exam-prep, software-analyse, codebase-explanation, semester-1]
course: "Software Analyse"
status: current
last_updated: 2026-06-16
prerequisites: ["[[sign-analysis]]", "[[readability-classifier]]"]
---

## Exam Intel

**Big part of exam:** Explain your own project codebases and the concepts inside them.

This means:
- Walk through code line by line
- Explain design decisions (why you did X, not Y)
- Articulate the underlying static analysis / ML concepts
- Justify implementation choices
- Trace through examples by hand

---

## Project 1: Readability Classifier — What You Must Explain

### Architecture Walkthrough

**Practice saying this out loud:**

"The readability classifier is a two-phase ML pipeline. Phase 1 (Preprocess) extracts four static metrics from 200 Java code snippets and writes them to CSV with ground-truth labels. Phase 2 (Classify) loads the CSV into WEKA, standardizes features, trains logistic regression with 10-fold cross-validation, and reports accuracy."

### Key Design Decisions — Be Ready to Justify

**Q: Why four metrics instead of just LOC?**
A: LOC captures size but not structure. Token entropy captures vocabulary diversity. Halstead volume balances length against vocabulary size. Cyclomatic complexity captures control flow branching. Together they measure different dimensions of cognitive load.

**Q: Why Shannon entropy of tokens?**
A: It measures vocabulary burden. Low entropy = repetitive/predictable code. High entropy = many unique identifiers to track. Real code has medium entropy. It's one proxy for "how many things do I need to hold in my head."

**Q: Why Halstead volume specifically?**
A: Halstead proposed that software follows linguistic laws. Volume = N × log₂(η) balances total code length (N) against vocabulary diversity (η). A 100-line method with 5 unique variables has low volume. A 10-line method with 30 unique variables has high volume. It captures density, not just size.

**Q: Why cyclomatic complexity?**
A: McCabe's metric counts independent paths through code. More paths = more test cases = more things to reason about. Each `if`, `for`, `&&`, `?:` adds a branch. Base complexity is 1 (straight line). M > 10 is considered high-risk.

**Q: Why standardize features before logistic regression?**
A: Features have wildly different scales (NumberLines: 10-40, HalsteadVolume: 0-500+). Without z-score normalization, large-valued features dominate the model. Standardization puts all features on mean=0, std=1 scale.

**Q: Why logistic regression instead of SVM/Random Forest?**
A: Logistic regression gives probability estimates (not just Y/N), has interpretable coefficients (you can see which features matter), and uses a linear decision boundary (less overfitting on small datasets). With only 200 samples, simplicity wins.

**Q: Why 10-fold cross-validation?**
A: Dataset is small (200 samples). Can't afford a separate test set. 10-fold CV uses all data for both training and testing, with each sample tested exactly once. Seed=1 for reproducibility.

**Q: Why threshold 3.6 for readability labels?**
A: Ground truth is mean of 9 human raters on 1-5 scale. Threshold 3.6 splits dataset ~50/50 between readable (Y) and not-readable (N), avoiding class imbalance.

### Code Walkthrough — Practice Tracing

**HalsteadVolumeFeature.java:**
```
1. Parse snippet with JavaParser
2. Create OperatorVisitor and OperandVisitor
3. Visit AST with both visitors
4. Extract N1 (total operators), n1 (unique operators), N2 (total operands), n2 (unique operands)
5. N = N1 + N2, n = n1 + n2
6. If n == 0, return 0.0 (avoid log(0))
7. Return N * log2(n)
```

**TokenEntropyFeature.java:**
```
1. Parse snippet, get token range
2. Build frequency map: for each token, count occurrences
3. For each unique token, compute p = count / total
4. Entropy = -Σ p * log2(p)
5. Return entropy
```

**CyclomaticComplexityFeature.java:**
```
1. Parse snippet
2. Create CyclomaticComplexityVisitor
3. Visit AST — visitor counts decision points (if, for, while, case, &&, ||, ?:)
4. Return visitor.getComplexity() + 1
```

**Classify.java:**
```
1. Load CSV with CSVLoader (read all bytes first to avoid file handle issues on Windows)
2. If first attribute is non-numeric (filename), delete it
3. Set class index to last attribute (Truth)
4. Create Standardize filter
5. Create Logistic classifier with ridge=1e-6
6. Wrap in FilteredClassifier
7. Evaluate with 10-fold CV, seed=1
8. Return Evaluation object
```

### Pitfalls to Mention

- **VariableDeclarator trick:** JavaParser doesn't represent `int x = 1` as AssignExpr. OperatorVisitor has special handling to count `=` in VariableDeclarator with initializer.
- **OperandVisitor manual traversal:** For FieldAccessExpr, don't call super.visit() to avoid double-counting via NameExpr. Manually visit scope instead.
- **Division by zero in entropy:** If a token appears 0 times, p=0, and 0*log(0) is undefined. Convention: 0*log(0) = 0 (L'Hôpital's rule).
- **Empty code snippets:** Return 0.0 for all metrics if parsing fails.

---

## Project 2: Sign Analysis — What You Must Explain

### Architecture Walkthrough

**Practice saying this out loud:**

"The sign analysis is an interprocedural dataflow analysis on Java bytecode. It tracks the abstract sign (−, 0, +) of every integer value through the program using a lattice and transfer functions. When two control flow paths merge, their abstract values are joined using lattice join. After the analysis converges to a fixpoint, it checks every IDIV instruction for division-by-zero and every IALOAD/IASTORE for negative array index."

### Key Design Decisions — Be Ready to Justify

**Q: Why use a lattice with bitmask encoding?**
A: The sign lattice is isomorphic to the powerset of {−, 0, +} ordered by subset inclusion. Each singleton gets one bit: MINUS=001, ZERO=010, PLUS=100. Composite values are bitwise OR of singletons. This makes lattice operations trivial: join(a,b) = a|b, a≤b ⟺ (a|b)==b, contains(a,s) ⟺ (a&s)≠0. It's a standard trick in abstract interpretation.

**Q: Why pairwise decomposition instead of lookup tables?**
A: A lookup table indexed by composite values (8×8=64 entries) would be imprecise — the conservative answer for most composites is TOP. Pairwise decomposition only needs 3×3=9 singleton rules, and everything else is computed automatically by iterating over all singleton pairs and joining results. It's more precise, less error-prone, and easier to verify.

**Q: Why is division by zero = BOTTOM, not TOP?**
A: BOTTOM means "undefined/impossible." TOP means "could be anything." Division by zero is undefined behavior — it's not that the result could be any sign, it's that the operation has no valid result. In the lattice, BOTTOM is the bottom element (no information), TOP is the top element (all information). They're opposite ends.

**Q: Why does Java integer division give ZERO_PLUS for same-sign division?**
A: Java truncates toward zero. So −1/2 = 0, not −1. This means same-sign division (e.g., −/− or +/+) can produce either a positive result OR zero, depending on magnitudes. Since we don't track magnitudes, the most precise answer is ZERO_PLUS (could be 0 or +).

**Q: Why is inter-procedural analysis context-insensitive?**
A: Context-sensitive analysis would track call stacks and analyze each call site separately. This is more precise but exponentially more expensive. Context-insensitive analysis analyzes each method once regardless of call site. If a method returns different signs depending on arguments, we join all possibilities. This loses precision but is much simpler and faster. For this project, context-insensitive is sufficient.

**Q: Why doesn't the analysis track condition narrowing?**
A: `if (x > 0)` doesn't narrow x to PLUS inside the then-branch. The analysis only tracks dataflow through operations (IADD, ISUB, etc.), not through conditional branches. Adding condition narrowing would require path-sensitive analysis, which is much more complex. The current analysis is conservative — it may report false positives (warnings that aren't real bugs), but it never misses a real bug (soundness).

**Q: Why check the stack top for IALOAD/IASTORE?**
A: JVM stack layout for IALOAD: [arrayref, index]. The index is on top. For IASTORE: [arrayref, index, value]. Again, index is second from top, but we check stack top because the value was just popped. Actually, wait — let me verify this. For IALOAD, the stack is [..., arrayref, index], so index is at stackSize-1. For IASTORE, the stack is [..., arrayref, index, value], so value is at stackSize-1, index is at stackSize-2. The code checks stackSize-1 for both. This might be a bug, or I'm misunderstanding the stack state at the point of the check.

### Code Walkthrough — Practice Tracing

**SignValue.java:**
```
1. Enum with 9 values: BOTTOM(0), MINUS(1), ZERO(2), ZERO_MINUS(3), PLUS(4), PLUS_MINUS(5), ZERO_PLUS(6), TOP(7), UNINITIALIZED(8)
2. join(other): if this==BOTTOM return other; if other==BOTTOM return this; return values()[this.ordinal() | other.ordinal()]
3. isLessOrEqual(other): if this==BOTTOM return true; if other==BOTTOM return false; return (this.ordinal() | other.ordinal()) == other.ordinal()
4. isMaybeZero(v): returns true if v has ZERO bit set (v==ZERO || v==ZERO_MINUS || v==ZERO_PLUS || v==TOP)
5. isMaybeNegative(v): returns true if v has MINUS bit set
```

**SignTransferRelation.java:**
```
1. evaluate(int): concrete int → abstract sign (negative→MINUS, 0→ZERO, positive→PLUS)
2. evaluate(NEG, v): flip signs (MINUS↔PLUS, ZERO→ZERO, composites swap accordingly)
3. evaluate(OP, lhs, rhs): 
   - If either is BOTTOM, return BOTTOM
   - If either is UNINITIALIZED, handle special cases (0*anything=0, 0/anything=0, divbyzero=_BOTTOM)
   - Otherwise: pairwise decomposition
     - result = BOTTOM
     - for each singleton a in {MINUS, ZERO, PLUS}:
       - if a ⊆ lhs (bitwise AND test):
         - for each singleton b in {MINUS, ZERO, PLUS}:
           - if b ⊆ rhs:
             - result = result.join(evalSingleton(OP, a, b))
     - return result
4. evalSingleton(op, a, b): dispatch to addSingletons/mulSingletons/divSingletons
5. addSingletons(a, b): if either is ZERO return other; same sign → same sign; mixed → TOP
6. mulSingletons(a, b): if either is ZERO return ZERO; same sign → PLUS; different → MINUS
7. divSingletons(a, b): if b==ZERO return BOTTOM; if a==ZERO return ZERO; same sign → ZERO_PLUS; different → ZERO_MINUS
```

**SignInterpreter.java:**
```
1. Extends ASM's Interpreter<SignValue>
2. newValue(type): if type==null return BOTTOM; if type==VOID return null; else return TOP
3. newOperation(insn): handle ICONST_*, BIPUSH, SIPUSH, LDC — evaluate constant → sign
4. copyOperation(insn, v): return v (identity)
5. unaryOperation(insn, v): handle INEG → NEG transfer; IINC → TOP (increment by unknown amount)
6. binaryOperation(insn, v1, v2): handle IADD/ISUB/IMUL/IDIV → binary transfer
7. naryOperation(insn, values): handle method calls — inter-procedural analysis
   - If method is in same class:
     - Create fresh Analyzer + SignInterpreter
     - Analyze callee method
     - Find all IRETURN instructions
     - Join stack top at each return point
     - Return joined value
   - Else: return TOP
8. merge(v1, v2): return v1.join(v2)
```

**SignAnalysisImpl.java:**
```
1. Load .class file with ClassReader
2. Build method map: "name:descriptor" → MethodNode
3. Find target method
4. Create SignInterpreter(classInternalName, methods)
5. Create Analyzer(interpreter)
6. analyzer.analyze(class, method) → Frame<SignValue>[]
7. extractAnalysisResults(method, frames):
   - For each instruction:
     - Track line number (LineNumberNode)
     - If IDIV: check divisor (stack top) for ZERO or MAYBE_ZERO
     - If IALOAD/IASTORE: check index (stack top) for MINUS or MAYBE_NEGATIVE
     - Add AnalysisResult to multimap keyed by line number
8. Return SortedSetMultimap<Integer, AnalysisResult>
```

### Worked Example — Trace By Hand

**divZeroCall():**
```java
public static void divZeroCall() {
    int x = 0;
    int result = 100 / x;
}
```
Bytecode:
```
ICONST_0       → push ZERO
ISTORE x       → x = ZERO
BIPUSH 100     → push PLUS
ILOAD x        → push ZERO
IDIV           → divisor is ZERO → ERROR
```

**allCases():**
```java
int top = ZERO_PLUS - ZERO_MINUS;
```
Decompose: {0,+} - {0,−}
Pairs:
- 0 - 0 = 0
- 0 - (−) = 0 + + = +
- + - 0 = +
- + - (−) = + + + = +
Join: 0 ∨ + ∨ + ∨ + = **0+**

So top = ZERO_PLUS. Then:
```java
int result = 100 / top;  // divisor is ZERO_PLUS → isMaybeZero=true → WARNING
int[] arr = new int[10];
arr[top];  // index is ZERO_PLUS → isMaybeNegative=false → no warning
```

### Pitfalls to Mention

- **UNINITIALIZED is a sentinel, not a lattice value.** It's used for variables that haven't been assigned yet. Transfer functions handle it specially (0*UNINITIALIZED=0, 0/UNINITIALIZED=0, UNINITIALIZED/0=_BOTTOM).
- **⚠️ IASTORE stack layout bug:** For IALOAD, stack is [..., arrayref, index], so index is at stackSize-1 ✓. For IASTORE, stack is [..., arrayref, index, value], so index is at stackSize-2, NOT stackSize-1. The code checks stackSize-1 for both, which gets the VALUE for IASTORE, not the INDEX. This is a bug, but tests don't catch it because there are no IASTORE test cases in PublicFunctional.java. If the professor asks "how do you handle array writes?", you need to acknowledge this.
- **Inter-procedural analysis only recurses for methods in the same class.** External method calls return TOP.
- **Condition narrowing is NOT implemented.** `if (x > 0)` doesn't narrow x to PLUS.
- **Fixpoint iteration is automatic.** ASM's Analyzer does the worklist algorithm. You just provide transfer functions.

---

## Practice Questions — Answer Out Loud

### Readability Project

1. "Walk me through the HalsteadVolumeFeature implementation."
2. "Why did you use JavaParser instead of regex to count operators?"
3. "What does the VariableDeclarator special case do?"
4. "Explain why you standardize features before logistic regression."
5. "What would happen if you removed the +1 from cyclomatic complexity?"
6. "Why 10-fold cross-validation instead of 5-fold or leave-one-out?"
7. "What's the threshold 3.6 for?"

### Sign Analysis Project

1. "Walk me through the SignValue lattice and explain the bitmask encoding."
2. "Why pairwise decomposition instead of a lookup table?"
3. "Trace through (0+) - (0-) by hand."
4. "Why is division by zero BOTTOM, not TOP?"
5. "Explain the inter-procedural analysis in SignInterpreter.naryOperation."
6. "What does context-insensitive mean?"
7. "Why doesn't the analysis track condition narrowing?"
8. "What's the difference between ERROR and WARNING in the output?"
9. "Trace through divZeroIndirectCall() — how does the analysis find the bug?"
10. "What is UNINITIALIZED_VALUE and why is it special?"

---

## Connections

- [[sign-analysis]] — Full theory deep dive
- [[readability-classifier]] — Full theory deep dive
- [[java-for-software-analysis]] — Java ecosystem refresher
- [[data-flow-analysis]] — General dataflow analysis concepts
- [[abstract-interpretation]] — Theoretical foundation

---

## Open Questions

- Verify IASTORE stack layout — does the code check the right stack position?
- What other abstract domains could you use? (intervals, parity, nullness)
- How would you add condition narrowing?
- What's the difference between sound and complete analysis?
