---
title: "Software Analyse Projects Overview"
tags: [software-analyse, course, projects, semester-1]
course: "Software Analyse"
status: current
last_updated: 2026-06-05
---

# Software Analyse Projects — Two Assignments Explained

## Overview

You have **two distinct projects** in this course:

1. **ss26sareadability-practice-putra01** — Readability Classifier (FINISHED ✓)
2. **ss26sasign-putra01** — Interprocedural Sign Analysis for Java Bytecode (ONGOING)

---

## Project 1: Code Readability Classifier

**Status:** FINISHED (submitted)

**Location:** `/home/rediwnl/Documents/Vault/second-brain/projects/software-analyse/ss26sareadability-practice-putra01/`

### What It Does

This project builds a **machine learning pipeline** to classify source code snippets as "readable" or "not readable" based on six static code metrics.

**Input:** 200 Java code snippets (`.jsnp` files, each 10–40 LOC)
**Output:** Binary classification (Y/N) with a logistic regression classifier trained on labeled data

### Architecture

```
Readability Analysis Pipeline
├── PREPROCESS STAGE
│   ├── Read each .jsnp snippet
│   ├── Compute 5 metrics per snippet:
│   │   ├── NumberLinesFeature (LOC including blanks)
│   │   ├── TokenEntropyFeature (Shannon entropy of token stream)
│   │   ├── HalsteadVolumeFeature (software complexity metric)
│   │   ├── CyclomaticComplexityFeature (control flow complexity)
│   │   └── [Also computed but unused in CSV: OperandVisitor, OperatorVisitor]
│   ├── Load ground-truth readability scores (truth_scores.csv)
│   └── Output: CSV file with 200 rows (header + data)
│
└── CLASSIFY STAGE
    ├── Load CSV as WEKA Instances
    ├── Train logistic regression (10-fold cross-validation, seed=1)
    └── Report accuracy/precision/recall
```

### Key Files

| File | Purpose |
|------|---------|
| `ReadabilityAnalysisMain.java` | Entry point; orchestrates preprocess + classify |
| `features/` | Five metric implementations |
| `utils/Preprocess.java` | Converts snippets → CSV |
| `utils/Classify.java` | CSV → WEKA → logistic regression |
| `utils/Parser.java` | Parses Java snippets using JavaParser library |
| `resources/snippets/*.jsnp` | 200 test code samples |
| `resources/truth_scores.csv` | Ground truth (rater scores) |

### Core Metrics Implemented

#### 1. **NumberLinesFeature**
- **What:** Count of all lines (code, blank, comments)
- **Implementation:** Split on `\r?\n` and count
- **Why:** Code duplication/length often correlates with readability issues

#### 2. **TokenEntropyFeature**
- **What:** Shannon entropy of token frequency distribution
- **Formula:** H = -Σ p(token) × log₂(p(token))
- **Why:** High entropy = many unique tokens = harder to follow; low entropy = repetitive/predictable
- **Example:** `for(int i=0; i<n; i++)` has low entropy (repeated `i`); random variable names have high entropy

#### 3. **OperatorVisitor + OperandVisitor**
- **Operators:** Count `=`, `+`, `&&`, `?:`, etc.
- **Operands:** Count variables, literals, field accesses
- **Why:** Input to Halstead metric (see below)

#### 4. **HalsteadVolumeFeature**
- **What:** N × log₂(n) where N = total ops/operands, n = unique ops/operands
- **Intuition:** Balances code length against vocabulary size
- **Range:** Lower = simpler; higher = more complex
- **Example:** 50 lines with 3 unique operands = low volume (simple); 10 lines with 30 unique operands = high volume (complex)

#### 5. **CyclomaticComplexityFeature**
- **What:** Count branching points (if, for, while, case, &&, ||, ?:)
- **Intuition:** Number of independent paths through code
- **Range:** 1 = straight line; 5 = complex; 10+ = hard to read
- **Example:**
  ```java
  if (x > 0) {
    for (int i = 0; i < n; i++) { // +2 complexity
      y = (z > 0) ? a : b;         // +1 for ternary
    }
  }
  // Total: 4 paths through this fragment
  ```

### Pipeline Flow (End-to-End)

```bash
$ mvn compile test
```

1. **Preprocess** reads 200 snippets
2. Computes 5 features per snippet
3. Looks up truth label from CSV
4. Outputs: `dataset.csv` (201 rows: 1 header + 200 data)
5. **Classify** loads CSV into WEKA
6. Trains logistic regression on 10-fold CV
7. Reports: Accuracy, Precision, Recall

### Test Coverage

- **Unit tests:** Each metric tested in isolation (e.g., HalsteadVolumeFeatureTest)
- **Integration tests:** Full pipeline tested (Preprocess → CSV → WEKA → Evaluate)
- **Edge cases:** Empty code, single token, division by zero in entropy (caught)

---

## Project 2: Interprocedural Sign Analysis

**Status:** ONGOING (100% tests passing; ready for submission)

**Location:** `/home/rediwnl/Documents/Vault/second-brain/projects/software-analyse/ss26sasign-putra01/`

### What It Does

This project implements a **static program analysis** that detects bugs in Java bytecode by reasoning about sign (−, 0, +) of integer values **without executing the code**.

**Purpose:** Find division-by-zero errors and negative array access bugs before runtime.

**Example:**
```java
public void divideByX(int x) {
  int result = 100 / x;  // BUG if x is zero!
}
```
**Analysis output:**
```
divideByX: Line 3 | IDIV | Divisor is MAYBE_ZERO → WARNING
```

### Why This Matters

Sign analysis is a **dataflow analysis**. Instead of executing all possible inputs, you track abstract values:
- `-` (definitely negative)
- `0` (definitely zero)
- `+` (definitely positive)
- `±` (could be negative or zero)
- `0+` (could be zero or positive)
- `±0` (could be any of the three)
- `⊤` (unknown / any value)

Rules propagate through operations:
- `+ + + = +` (positive + positive = positive)
- `+ + - = ⊤` (positive + negative = could be anything)
- `+ × - = -` (positive times negative = negative)
- `x / 0 = ⊥` (division by zero is undefined; analysis stops here)

### Architecture

```
Sign Analysis (Java Bytecode)
├── Load .class file (ASM framework)
├── Build method map ("methodName:descriptor" → method node)
├── For each method:
│   ├── Run dataflow Analyzer with SignInterpreter
│   │   ├── Track abstract sign value on stack & locals
│   │   ├── Propagate through bytecode instructions
│   │   └── Handle method calls recursively (inter-procedural)
│   ├── Check each instruction:
│   │   ├── IDIV: divisor sign → ERROR if zero, WARNING if maybe zero
│   │   ├── IALOAD/IASTORE: index sign → ERROR if negative, WARNING if maybe negative
│   │   └── (Other ops: just propagate)
│   └── Output: Line# | Instruction | Problem Type
└── Report findings
```

### Core Concepts

#### 1. **SignValue Lattice**
```
            ⊤ (TOP — unknown)
       /    |    |    \
    ±0   ±   0+   ± 
    /  \ | \ / | / \
  -   0   +
    \  | /
      ⊥ (BOTTOM — undefined)
```

Represented as an enum with **bitmask encoding**:
```java
BOTTOM=0    // 000
MINUS=1     // 001
ZERO=2      // 010
ZERO_MINUS=3    // 011 (0 OR -)
PLUS=4      // 100
PLUS_MINUS=5    // 101 (+ OR -)
ZERO_PLUS=6     // 110 (0 OR +)
TOP=7       // 111 (all three)
```

**Key operation:** `join(a, b) = values()[a.ordinal() | b.ordinal()]`
- This models the lattice: when two paths converge, their values merge
- Example: `join(MINUS, PLUS) = PLUS_MINUS` (could be either sign now)

#### 2. **Transfer Relation** (How Values Change)

For operation `OP(lhs, rhs)`:

| Operation | Rule |
|-----------|------|
| **NEG** | Flip ±: `-→+`, `+→-`, `0→0`, composites swap accordingly |
| **ADD** | Same sign → same sign. Either zero → the other. Mixed → TOP |
| **SUB** | Rewrite as `lhs + NEG(rhs)`, then apply ADD rules |
| **MUL** | `0 × x = 0`. Same sign → `+`. Different → `-`. |
| **DIV** | `0 / x = 0`. `x / 0 = ⊥` (undefined). Same sign → `+`. Different → `-`. |

**Precision trick:** Instead of pattern-matching on composite values (imprecise), decompose into singletons and compute pairwise:

```
result = ⊥
for each singleton s_a in lhs:
  for each singleton s_b in rhs:
    result = join(result, table[OP, s_a, s_b])
```

Example: `(0+) - (0-) = ?`
- Decompose: `0+` = {0, +}, `0-` = {0, -}
- Pairwise: 0-0=0, 0-(-) = +, (+)-0 = +, (+)-(-) = +
- Join: 0 ∨ + ∨ + ∨ + = 0+ ✓

This precision is critical: a naive lookup would incorrectly say `0+` (too conservative).

#### 3. **Inter-procedural Analysis**

When bytecode calls a method **in the same class**, recursively analyze the callee:
1. Create new Analyzer for called method
2. Run it to completion
3. Extract the return value (join all IRETURN instructions)
4. Propagate that value back to the caller

Example:
```java
public int getSign(int x) {
  return (x > 0) ? 1 : -1;  // Always ±
}

public void test() {
  int s = getSign(42);
  int result = 100 / s;  // OK: s is never zero
}
```
Analysis traces into `getSign()`, determines it returns `±`, so division is safe.

### Key Files

| File | Purpose |
|------|---------|
| `SignValue.java` | Enum + lattice operations (join, isLessOrEqual) |
| `SignLattice.java` | Delegates to SignValue (unused; mostly for structure) |
| `SignTransferRelation.java` | Implements pairwise transfer rules (ADD, SUB, MUL, DIV, NEG) |
| `SignInterpreter.java` | ASM Interpreter that applies transfer rules to bytecode |
| `SignAnalysisImpl.java` | Loads class, builds method map, runs analysis |
| `SignAnalysisMain.java` | CLI entry point |
| `test/SignValueTest.java` | Tests lattice operations & bitmask logic |
| `test/SignLatticeTest.java` | Tests lattice properties (monotonicity) |
| `test/SignTransferRelationTest.java` | Tests singleton/composite pairwise rules |
| `test/SignAnalysisImplTest.java` | Functional tests on PublicFunctional.java test methods |
| `examples/PublicFunctional.java` | Test methods (divZeroCall, ifelse, etc.) |
| `expected-results/public-functional-*.txt` | Expected analysis outputs |

### How to Use

```bash
$ mvn clean compile test

# Run specific test
$ mvn test -Dtest=SignValueTest

# Analyze a class from command line (after full build)
$ java -cp target/classes:target/dependency/* \
    de.uni_passau.fim.se2.sa.sign.SignAnalysisMain \
    -c path/to/PublicFunctional.class \
    -m "divZeroCall"
```

### Test Examples

#### Division by Zero (ERROR case)
```java
public static void divZeroCall() {
  int x = 0;
  int result = 100 / x;  // Line N: x is definitely zero
}
```
**Expected output:**
```
divZeroCall: Line N | IDIV | Divisor is ZERO → ERROR
```

#### Maybe Zero (WARNING case)
```java
public static void divMaybeZeroCall(int x) {
  if (x > 0) {
    int result = 100 / x;  // x could still be zero (path analysis doesn't track condition)
  }
}
```
**Expected output:**
```
divMaybeZeroCall: Line N | IDIV | Divisor is MAYBE_ZERO → WARNING
```

#### All Cases (Complex, No Warnings)
```java
int top = ZERO_PLUS - ZERO_MINUS;  // Decomposes to (0-0=0, 0-(-) = +, (+)-0 = +, (+)-(-) = +)
                                     // Result: 0+
array[top];  // Index can only be 0 or +, never negative → NO WARNING
```

### Current Status

- ✅ All lattice operations implemented
- ✅ Transfer relation fully decomposable (no imprecision)
- ✅ Inter-procedural analysis working
- ✅ All unit tests passing
- ✅ All functional tests passing
- ✅ Ready for submission

---

## Comparison: Readability vs. Sign Analysis

| Aspect | Readability | Sign Analysis |
|--------|-------------|---------------|
| **Input** | Source code (Java) | Bytecode (JVM .class) |
| **Goal** | Classify readability → ML | Find bugs → Static analysis |
| **Technique** | Feature extraction + ML | Dataflow + lattice theory |
| **Abstraction** | Concrete metrics | Abstract signs (−, 0, +) |
| **Precision** | Probabilistic | Conservative (sound) |
| **Output** | Binary label + confidence | Line# + ERROR/WARNING |
| **Complexity (Academic)** | Moderate | High (lattice theory) |

---

## Study Strategy

### For Readability Project
- **Already done.** Focus on understanding the metrics if you need to explain them.
- **Key insight:** Machine learning on code is just feature engineering + standard classifiers.
- **Review:** Feature implementations, CSV formatting, WEKA usage.

### For Sign Analysis Project
- **Current phase:** Testing; ready to submit.
- **To solidify understanding:**
  1. Read SignValue.java — understand ordinal encoding
  2. Read SignTransferRelation.java — trace a few pairwise examples by hand
  3. Read SignInterpreter.java — see how bytecode instructions map to transfers
  4. Run tests locally: `mvn test`
  5. Study PublicFunctional.java test cases — manually trace through bytecode in your head

### Common Pitfalls to Avoid (Sign Analysis)
1. **Never use simple lookup tables.** Decompose composites into singletons.
2. **Handle BOTTOM explicitly.** It's the bottom of the lattice; don't confuse with TOP.
3. **IALOAD/IASTORE both check stack top (index), not the array reference.**
4. **Inter-procedural calls:** Only recurse if callee is in the same class AND returns int.
5. **isSubTypeOf override:** Use `isLessOrEqual`, not `equals()`, or IRETURN checks fail.

---

## Deep Study Pages

For exam-ready understanding, see the dedicated vault pages:

- [[readability-classifier]] — Deep dive into all four metrics (Halstead, entropy, cyclomatic complexity, LOC), the ML pipeline, and worked examples you can trace by hand.
- [[sign-analysis]] — Deep dive into lattice theory, pairwise decomposition, inter-procedural analysis, fixpoint iteration, and test cases to trace by hand.
- [[java-for-software-analysis]] — Java survival guide: classes, enums, generics, visitors, Maven, JavaParser, ASM, WEKA, picocli, JUnit — everything you need to read both codebases.

---

## Where to Go From Here

- **Readability:** Submitted, done. Move on to exam prep.
- **Sign Analysis:** Likely ready to submit (all tests pass). Verify:
  - `mvn clean test` → all green
  - `mvn clean compile` → no compilation errors
  - Check that expected-results match actual output
  - Then submit.

---

## Memory Note

Both projects belong to **Software Analyse (ss26)**. Exam date: **July 31, 2026**. The assignment material (especially Sign Analysis lattice theory) is exam-relevant — understand decomposition and pairwise evaluation, not just implementation.
