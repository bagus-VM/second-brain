---
title: "Code Readability Classifier — Deep Study Guide"
tags: [concept, software-analyse, machine-learning, halstead, cyclomatic-complexity, entropy, semester-1]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-05
prerequisites: ["[[java-for-software-analysis]]"]
---

## One-line Summary
*Extract static metrics from code snippets, train a logistic regression classifier, predict whether humans find code readable.*

## Core Intuition

The question: can a machine predict whether a human will find a piece of code "readable"?

The answer from Scalabrino et al.'s research: yes, but only with ~70-80% accuracy using static metrics alone. The trick is that "readability" isn't one thing — it's a combination of code length, vocabulary diversity, structural complexity, and control flow complexity. No single metric captures it, but combining them with machine learning gets you reasonable predictions.

The pipeline has two phases:
1. **Feature extraction** — turn each code snippet into a vector of numbers
2. **Classification** — train a model to map vectors to Y/N labels

This is the standard supervised learning pattern. Nothing exotic. The interesting part is *which* features matter and *why*.

---

## The Four Metrics — Theory Deep Dive

### 1. Number of Lines (LOC)

**What it measures:** **Raw size of the code snippet**.

**Why it matters for readability:**
- Longer code = **more cognitive load** (working memory is limited to ~7 chunks)
- Longer methods are harder to understand than shorter ones
- But it's a crude proxy — 100 lines of simple code may be more readable than 10 lines of dense code

**Implementation detail:** Counts ALL lines including blanks and comments. This is intentional — blank lines and comments are part of the visual structure that affects readability perception.

**Exam angle:** This is the simplest metric. If they ask "why not just use LOC?", the answer is: LOC doesn't capture *how* the code is structured, just how much of it there is.

---

### 2. Token Entropy (Shannon Entropy of Token Distribution)

**What it measures:** **How diverse/uniform the vocabulary of the code is**.

**Formula:**
```
H = -Σ p(token) × log₂(p(token))
```

where `p(token)` = frequency of that token / total token count.

**Intuition:**
- **Low entropy (H ≈ 0):** Almost all tokens are the same. Example: `x = x + x + x` — very repetitive, easy to predict what comes next.
- **High entropy (H ≈ log₂(n)):** All tokens are unique. Example: `a = b + c * d / e - f` — every symbol is different, harder to track.
- **Medium entropy:** Real code. Some keywords repeat (`if`, `return`, `int`), some identifiers are unique.

**Why it matters for readability:**
- High entropy = many unique identifiers = more names to track in your head
- But also: code with ZERO entropy (all same token) isn't readable either
- Entropy captures the *vocabulary burden* on the reader

**Implementation detail:** The implementation counts ALL JavaTokens from the parser, including whitespace and punctuation. The comment in the source says: "since we are interested in the readability of code as perceived by a human, tokens also include whitespaces." This is a deliberate design choice — whitespace IS part of how humans read code.

**Worked example:**
```java
int x = 1;
int y = 2;
int z = x + y;
```
Tokens: `int`, `x`, `=`, `1`, `;`, `int`, `y`, `=`, `2`, `;`, `int`, `z`, `=`, `x`, `+`, `y`, `;`
- `int` appears 3 times, `=` 3 times, `;` 3 times, `x` 2 times, `y` 2 times
- `z`, `1`, `2`, `+` each appear once
- Total: 17 tokens, 8 unique
- p(int) = 3/17, p(=) = 3/17, p(;) = 3/17, p(x) = 2/17, p(y) = 2/17, p(z) = 1/17, p(1) = 1/17, p(2) = 1/17, p(+) = 1/17
- H = -(3×(3/17)×log₂(3/17) + 2×(2/17)×log₂(2/17) + 4×(1/17)×log₂(1/17))
- H ≈ 2.76 bits

**Exam angle:** Know the formula. Be able to compute it by hand. Understand what high vs. low entropy means. Know that `0 × log₂(0) = 0` by convention (L'Hôpital's rule).

---

### 3. Halstead Volume

**What it measures:** A 1970s-era software complexity metric that **combines code length with vocabulary size**.

**Background:** Maurice Halstead proposed four base measures:
- **η₁** (eta-1): number of *unique* operators
- **η₂** (eta-2): number of *unique* operands
- **N₁**: total number of operators
- **N₂**: total number of operands

**Derived measures:**
- ==**Vocabulary:** η = η₁ + η₂==
- ==**Length:** N = N₁ + N₂==
- ==**Volume:** V = N × log₂(η)==

**Intuition:** Volume balances how MUCH code there is (N) against how DIVERSE its vocabulary is (η). A program that's long but uses few unique symbols has low volume. A program that's short but uses many unique symbols has high volume.

**What counts as an operator vs. operand?**
- **Operators:** `=`, `+`, `-`, `*`, `/`, `&&`, `||`, `?:`, `new`, `return`, `if`, `for`, method calls, etc.
- **Operands:** variables, constants, literals, field accesses

**Implementation detail — the VariableDeclarator trick:**
JavaParser doesn't represent `int x = 1` as an `AssignExpr`. The `=` is implicit in `VariableDeclarator`. So the OperatorVisitor has special handling: when visiting a `VariableDeclarator` with an initializer, it counts `=` as an assignment operator. Without this, you'd miss all variable initializations — a massive undercount.

**Implementation detail — OperandVisitor's manual traversal:**
For `FieldAccessExpr` (e.g., `System.out.println`), the visitor does NOT call `super.visit()` to avoid double-counting via `NameExpr`. Instead it manually visits the scope. This means `System` and `out` are counted as separate operands. Same pattern for `MethodCallExpr` and `ArrayAccessExpr`.

**Worked example:**
```java
int result = a + b;
```
- Operators: `=`, `+` → η₁ = 2, N₁ = 2
- Operands: `result`, `a`, `b`, `int` → wait, `int` is a type, not an operand in Halstead.
- Actually: operands are `result`, `a`, `b` → η₂ = 3, N₂ = 3
- N = 5, η = 5
- V = 5 × log₂(5) = 5 × 2.32 = 11.61

**Exam angle:** Know the formula V = N × log₂(η). Be able to compute it by hand. Understand the difference between η₁/η₂ (unique) and N₁/N₂ (total). Know why Halstead proposed this (he believed programming follows linguistic laws, like Zipf's law).

---

### 4. Cyclomatic Complexity (McCabe's)

**What it measures:** **The number of independent paths through the code's control flow graph**.

**Formula:** M = E - N + 2P
- E = edges in control flow graph
- N = nodes in control flow graph
- P = connected components (usually 1 for a single method)

**Simplified formula:** M = (number of decision points) + 1

**What counts as a decision point:**
- `if` statements
- `for`, `foreach`, `while`, `do-while` loops
- `catch` clauses
- `?:` ternary operator
- `&&` and `||` (short-circuit evaluation — each is a branch)
- `switch` case labels (each label except `default`)

**Why `+1`?** A method with zero decision points has one path (straight through). So the base complexity is 1, not 0.

**Why it matters for readability:**
- More paths = more test cases needed = more things to reason about
- McCabe's original claim: M > 10 → high risk of defects
- Cyclomatic complexity correlates strongly with testing effort

**Implementation detail:** The `CyclomaticComplexityVisitor` counts decision points WITHOUT the +1. The feature adds +1 when returning: `return visitor.getComplexity() + 1`.

**Worked example:**
```java
if (x > 0) {
    for (int i = 0; i < n; i++) {
        y = (z > 0) ? a : b;
    }
}
```
Decision points: `if` (+1), `for` (+1), `&&` inside for condition? No, just `i < n`. Ternary `?:` (+1). Total: 3.
Cyclomatic complexity = 3 + 1 = **4**.

**Exam angle:** Know the formula. Be able to draw the control flow graph and count edges/nodes. Know the simplified version. Understand why `&&` and `||` each count as a decision point (short-circuit evaluation means the second operand might not execute).

---

## The ML Pipeline

### Phase 1: Preprocess

For each of the 200 `.jsnp` files:
1. Parse with JavaParser (as CLASS_BODY, not full compilation unit)
2. Compute each feature metric
3. Look up the ground truth score (mean of 9 human raters, 1-5 scale)
4. Apply threshold: score ≥ 3.6 → "Y" (readable), score < 3.6 → "N" (not readable)
5. Write to CSV: `filename, feature1, feature2, ..., feature3, feature4, Y/N`

**Why 3.6?** It splits the Scalabrino dataset roughly 50/50 between readable and not-readable, avoiding class imbalance.

### Phase 2: Classify

1. Load CSV into WEKA
2. Drop the filename column (it's not a feature)
3. Set the Truth column as the class attribute
4. Apply Standardize filter (z-score normalization: `(x - μ) / σ`)
5. Train Logistic Regression with ridge regularization (λ = 10⁻⁶)
6. Evaluate with 10-fold cross-validation (seed = 1 for reproducibility)

**Why Standardize?** The features have wildly different scales:
- NumberLines: 10-40
- TokenEntropy: 0-5
- HalsteadVolume: 0-500+
- CyclomaticComplexity: 1-20

Without normalization, HalsteadVolume would dominate. Standardization puts all features on the same scale (mean=0, std=1).

**Why logistic regression?** It's the simplest classifier that gives you:
- A probability estimate (not just Y/N)
- Interpretable coefficients (you can see which features matter)
- A linear decision boundary (simple, less overfitting)

**Why 10-fold CV?** You don't have a separate test set (only 200 samples). 10-fold CV uses all data for both training and testing, with each sample tested exactly once.

---

## Java Concepts You Need

See [[java-for-software-analysis]] for a full Java refresher covering:
- JavaParser library (AST parsing, visitors)
- WEKA library (ML pipeline)
- picocli (CLI framework)
- Maven build system

---

## Common Exam Questions

1. **"Compute the cyclomatic complexity of this code snippet"** — draw the CFG, count decision points, add 1.

2. **"Compute the Halstead volume"** — count unique/total operators and operands, apply formula.

3. **"Compute the token entropy"** — build frequency table, apply Shannon entropy formula.

4. **"Why use multiple metrics instead of just LOC?"** — LOC captures size but not complexity, vocabulary diversity, or control flow structure.

5. **"Why standardize features before logistic regression?"** — different scales cause the model to bias toward large-valued features. Z-score normalization puts all features on equal footing.

6. **"What is 10-fold cross-validation and why use it?"** — split data into 10 parts, train on 9, test on 1, rotate. Use because dataset is small (200 samples) and you need reliable accuracy estimate.

7. **"What does the threshold 3.6 represent?"** — decision boundary on mean rater score. ≥3.6 = readable. Balances class distribution ~50/50.

---

## Connections

- [[sign-analysis]] — Same course, different project. Sign analysis is about *finding bugs*, this is about *measuring quality*.
- [[data-flow-analysis]] — Halstead and cyclomatic complexity are *static analysis* metrics. Sign analysis is also static analysis, but uses dataflow instead of just counting.
- [[machine-learning-basics]] — The classify phase is standard supervised learning. Logistic regression, cross-validation, feature standardization — these are ML fundamentals.
- [[java-for-software-analysis]] — Both projects share the same Java ecosystem: Maven, JUnit, picocli.

---

## Open Questions
- How does the classifier perform with different ML algorithms (SVM, Random Forest)?
- What's the inter-rater agreement among the 9 human evaluators?
- How were the 200 snippets selected? Is there a selection bias?

## Formal Definition / Statement

*To be filled.*

## Key Properties / Complexity

*To be filled.*

## Worked Example

*To be filled.*

## Common Pitfalls

*To be filled.*
