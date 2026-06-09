---
title: "Interprocedural Sign Analysis — Deep Study Guide"
tags: [concept, software-analyse, dataflow-analysis, lattice-theory, abstract-interpretation, bytecode, semester-1]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-05
prerequisites: ["[[java-for-software-analysis]]"]
---

## One-line Summary
*Track the sign (−, 0, +) of every integer value in Java bytecode to find division-by-zero and negative-array-index bugs without running the code.*

## Core Intuition

Imagine you're debugging code. You run it with one input and check if it crashes. But what about all the OTHER inputs? You can't test them all.

**Static analysis** flips this: instead of running the code, you *analyze* it. You ask: "Is there ANY possible execution path where this divisor could be zero?" If yes, flag it.

But "any possible value" is too broad — it would flag everything. So we use **abstraction**: instead of tracking the exact value of each variable (which is impossible in general), we track just its *sign*:
- Is it definitely negative? (−)
- Is it definitely zero? (0)
- Is it definitely positive? (+)
- Could it be multiple of these? (composite values like 0+ means "could be zero or positive")

This is the core idea of **abstract interpretation**: replace concrete values with abstract ones that capture just enough information to answer your question.

---

## The Lattice — Your Abstract Domain

### What is a Lattice?

A lattice is a mathematical structure with:
- A **partial order** (some elements are "above" others)
- A **join** operation (combine two elements to get their least upper bound)
- A **top** element (⊤, "could be anything")
- A **bottom** element (⊥, "impossible / no value")

For sign analysis, the lattice looks like this:

```
                    ⊤ (TOP — could be −, 0, or +)
               /    |    \
            ±0     ±      0+
           / \    / \    / \
          0   −  −   +  0   +
           \  |  /   /  /
            ⊥ (BOTTOM — impossible)
```

Wait, that's the full Hasse diagram. Let me draw it properly:

```
Level 3:           ⊤                  ordinal 7 (111)
                 / | \
Level 2:      ±0   ±   0+            ordinals 3, 5, 6
              / \  / \ / \
Level 1:    0    −     +              ordinals 2, 1, 4
              \   |   /
Level 0:       ⊥                      ordinal 0 (000)
```

**Reading the lattice:**
- ⊤ means "I have no idea what the sign is — it could be anything"
- 0+ means "I know it's either zero or positive, but not negative"
- + means "I know it's definitely positive"
- ⊥ means "this is impossible / undefined" (division by zero lands here)

### The Bitmask Encoding — Why It's Brilliant

Each singleton sign gets one bit:
- MINUS (−) = bit 0 = 001 = ordinal 1
- ZERO (0) = bit 1 = 010 = ordinal 2
- PLUS (+) = bit 2 = 100 = ordinal 4

Composite values are just bitwise OR of singletons:
- ZERO_MINUS = 010 | 001 = 011 = ordinal 3
- PLUS_MINUS = 100 | 001 = 101 = ordinal 5
- ZERO_PLUS = 100 | 010 = 110 = ordinal 6
- TOP = 100 | 010 | 001 = 111 = ordinal 7
- BOTTOM = 000 = ordinal 0

**This makes lattice operations trivial:**
- **join(a, b) = a | b** (bitwise OR)
- **a ≤ b ⟺ (a | b) == b** (a's bits are a subset of b's bits)
- **a contains singleton s ⟺ (a & s) != 0** (bitwise AND test)

**Why does this work?** Because the lattice IS the powerset of {−, 0, +}, ordered by subset inclusion. The powerset lattice is isomorphic to the bitmask lattice. This is a standard trick in abstract interpretation.

---

## Transfer Functions — How Values Change

### The Core Problem

When the bytecode says `IADD` (integer add), and the two operands on the stack have abstract sign values LHS and RHS, what's the sign of the result?

You need a **transfer function**: `sign(LHS + RHS) = ?`

### Singleton Rules

For two KNOWN singletons, the rules are intuitive:

**Addition:**
| LHS + RHS | − | 0 | + |
|-----------|---|---|---|
| **−**     | − | − | ⊤ |
| **0**     | − | 0 | + |
| **+**     | ⊤ | + | + |

Why? `− + − = −` (always negative). `− + + = ⊤` (could be anything — depends on magnitudes, which we don't track). `0 + x = x` (zero is identity).

**Subtraction:** Implemented as `LHS + NEG(RHS)`. Negate the RHS, then apply addition rules.

**Multiplication:**
| LHS × RHS | − | 0 | + |
|-----------|---|---|---|
| **−**     | + | 0 | − |
| **0**     | 0 | 0 | 0 |
| **+**     | − | 0 | + |

Why? `− × − = +` (negative times negative is positive). `0 × anything = 0`. `+ × − = −`.

**Division:**
| LHS ÷ RHS | − | 0 | + |
|-----------|---|---|---|
| **−**     | + | ⊥ | − |
| **0**     | 0 | ⊥ | 0 |
| **+**     | − | ⊥ | + |

**CRITICAL:** Division by zero gives ⊥ (BOTTOM). This is how we detect the bug! When the analysis hits ⊥, it means "this path is impossible" or "this is a runtime error."

**Java integer division twist:** `−1 / 2 = 0` in Java (truncation toward zero). So `− / −` could give + OR 0. The implementation uses ZERO_PLUS instead of just + for same-sign division. Similarly, `+ / −` gives ZERO_MINUS (could be 0 or −).

### The Pairwise Decomposition — The Hard Part

**The problem:** What about composite values? What is `(0+) + (−)`?

**WRONG approach:** Use a lookup table indexed by composite values. This is imprecise because it has to handle every possible composite, and the conservative answer is usually TOP.

**RIGHT approach (pairwise decomposition):**

```
result = BOTTOM
for each singleton a in {−, 0, +}:
    if a ⊆ LHS:          // a's bit is set in LHS
        for each singleton b in {−, 0, +}:
            if b ⊆ RHS:  // b's bit is set in RHS
                result = result ∨ singletonRule(op, a, b)
return result
```

**Worked example:** `(0+) + (−)`

Step 1: Decompose 0+ into singletons: {0, +}
Step 2: Decompose − into singletons: {−}
Step 3: Compute all pairs:
- 0 + − = −
- + + − = ⊤
Step 4: Join results: − ∨ ⊤ = ⊤

**Another example:** `(0+) − (0−)`

Decompose: 0+ = {0, +}, 0− = {0, −}
Pairs:
- 0 − 0 = 0
- 0 − (−) = 0 + + = +
- + − 0 = +
- + − (−) = + + + = +
Join: 0 ∨ + ∨ + ∨ + = **0+**

**Why is this correct?** Because the transfer functions are **monotone** over the lattice. If a ⊆ LHS and b ⊆ RHS, then f(a,b) ⊆ f(LHS,RHS). So computing f on all singleton pairs and joining gives you the most precise possible result for composite inputs.

**Why not just use a full lookup table?** Because there are 8×8 = 64 possible input pairs, and you'd need to precompute all of them. The pairwise approach only needs 3×3 = 9 singleton rules, and everything else is computed automatically. It's also less error-prone.

---

## Inter-procedural Analysis — Going Beyond One Method

### The Problem

```java
int getZero() { return 0; }
void test() {
    int x = getZero();
    int result = 100 / x;  // BUG!
}
```

If you only analyze `test()` in isolation, you see `x` comes from a method call. Without inter-procedural analysis, you'd have to assume `x` could be anything (⊤). You'd miss the definite bug.

### The Solution: Recursive Analysis

When the interpreter encounters a method call (`INVOKEVIRTUAL`, `INVOKESTATIC`, etc.):
1. Look up the callee method in the class's method map
2. Create a **fresh** Analyzer + Interpreter for the callee
3. Run the analysis on the callee to completion
4. Find all `IRETURN` instructions in the callee
5. Read the abstract value from the top of the stack at each return point
6. **Join** all return values — this gives the callee's abstract return value
7. Use that value as the result of the method call in the caller

**Example trace:**
```
test():
  INVOKE getZero()  →  analyze getZero():
                          ICONST_0  →  push ZERO
                          IRETURN   →  return ZERO
                        result = ZERO
  IDIV 100 / ZERO   →  divisor is ZERO → ERROR
```

**Context-insensitive:** The method is analyzed once regardless of call site. If `getZero()` is called from 10 places, it's analyzed once and the same abstract return value is used everywhere. This loses precision (the return value might depend on arguments) but is much simpler and faster.

---

## Bytecode to Abstract — The Interpreter Mapping

### How ASM's Interpreter Framework Works

ASM provides an abstract `Interpreter` class with hooks for each bytecode instruction type:

| Hook | Bytecode | Implementation |
|------|----------|----------------|
| `newOperation` | ICONST_*, BIPUSH, SIPUSH, LDC | Evaluate constant → sign |
| `unaryOperation` | INEG | NEG transfer function |
| `binaryOperation` | IADD, ISUB, IMUL, IDIV | Binary transfer function |
| `naryOperation` | INVOKE* | Recursive inter-procedural analysis |
| `merge` | (at join points) | SignValue.join (lattice join) |

**Key insight:** The ASM `Analyzer` does the fixpoint iteration automatically. You just provide the transfer functions via the Interpreter hooks. The analyzer maintains a worklist of instructions to process, and iterates until the abstract state stabilizes (fixpoint).

### Fixpoint Iteration — Why It's Needed

```java
int x = 0;        // x = ZERO
while (x < 10) {  // x could be 0..9
    x = x + 1;    // x could be 0+ still
}
// After loop: x = 0+ (could be zero or positive)
```

The loop creates a cycle in the control flow graph. The analyzer needs to iterate:
1. First pass: x = ZERO at loop entry, x = ZERO_PLUS after +1
2. Second pass: x = ZERO_PLUS at loop entry (merged with initial), x = ZERO_PLUS after +1
3. No change → fixpoint reached.

This is why it's called a "dataflow analysis" — abstract values *flow* through the program until they stabilize.

---

## Bug Detection — Post-Analysis Check

After the analysis converges, `SignAnalysisImpl` inspects every instruction:

| Instruction | Check | Condition | Report |
|-------------|-------|-----------|--------|
| IDIV | Divisor (stack top) | Exactly ZERO | ERROR: Division by Zero |
| IDIV | Divisor (stack top) | Maybe zero (e.g., 0+) | WARNING: Maybe Division by Zero |
| IALOAD | Index (stack top) | Exactly MINUS | ERROR: Negative Array Index |
| IALOAD | Index (stack top) | Maybe negative (e.g., ±) | WARNING: Maybe Negative Array Index |
| IASTORE | Index (stack top) | Same as IALOAD | Same |

**"Maybe" predicates:** `isMaybeZero()` returns true if the ZERO bit is set in the composite value. So for TOP (111), `isMaybeZero()` = true. For ZERO_PLUS (110), `isMaybeZero()` = true. For PLUS (100), `isMaybeZero()` = false.

---

## The ASM Framework — What You Need to Know

### What is ASM?

ASM is a Java bytecode manipulation framework. It provides:
- **ClassReader:** Reads `.class` files
- **ClassNode / MethodNode:** In-memory representation of bytecode
- **Analyzer:** Generic dataflow analysis engine (worklist algorithm)
- **Interpreter:** Abstract class you override to define transfer functions
- **Frame:** Abstract state at each instruction (local variables + operand stack)

### How the Analysis Uses ASM

```
ClassReader → ClassNode (contains all methods)
                ↓
        Map<String, MethodNode>  (key = "name:descriptor")
                ↓
        SignInterpreter(methods)  ← custom interpreter
                ↓
        Analyzer.analyze(class, method)
                ↓
        Frame<SignValue>[]  ← one frame per instruction
                ↓
        Check IDIV, IALOAD, IASTORE for bugs
```

---

## Test Cases — Trace These By Hand

### 1. `divZeroCall()`
```java
public static void divZeroCall() {
    int x = 0;
    int result = 100 / x;
}
```
Bytecode: ICONST_0 → ICONST → BIPUSH 100 → ILOAD x → IDIV
- x = ZERO, divisor = ZERO → IDIV with ZERO divisor → ERROR

### 2. `divMaybeZeroCall(int x)`
```java
public static void divMaybeZeroCall(int x) {
    if (x > 0) {
        int result = 100 / x;
    }
}
```
- x starts as TOP (parameter, unknown)
- `x > 0` branch doesn't narrow the sign (we don't track conditions!)
- At IDIV: divisor = TOP → isMaybeZero = true → WARNING

### 3. `divZeroIndirectCall()`
```java
public static int getValueIndirect() { return getZero(); }
public static int getZero() { return 0; }
public static void divZeroIndirectCall() {
    int x = getValueIndirect();
    int result = 100 / x;
}
```
- `getValueIndirect()` calls `getZero()` → returns ZERO
- `divZeroIndirectCall()`: x = getValueIndirect() = ZERO
- IDIV with ZERO divisor → ERROR
- This tests **transitive** inter-procedural analysis (two levels deep)

### 4. `allCases()`
```java
int top = ZERO_PLUS - ZERO_MINUS;  // 0+ minus 0- = ?
// Decompose: {0,+} minus {0,−}:
// 0-0=0, 0-(−)=+, +-0=+, +-(−)=+
// Join: 0∨+∨+∨+ = 0+
// So top = 0+
int result = 100 / top;  // 0+ includes zero → WARNING
int[] arr = new int[10];
arr[top];  // 0+ is never negative → no warning
```

---

## Common Pitfalls (Exam & Implementation)

1. **Never use simple lookup tables for composites.** Always decompose into singletons and compute pairwise. The lookup table gives imprecise (too conservative) results.

2. **Division by zero = ⊥, not TOP.** BOTTOM means "undefined/impossible." TOP means "could be anything." They're opposite ends of the lattice.

3. **Java integer division truncates toward zero.** So −1/2 = 0, not −1. This means same-sign division can produce ZERO_PLUS (not just PLUS) and different-sign can produce ZERO_MINUS (not just MINUS).

4. **Condition narrowing is NOT implemented.** `if (x > 0)` does NOT narrow x to PLUS inside the then-branch. The analysis only tracks dataflow through operations, not through conditional branches. This is why `divMaybeZeroCall` gives a WARNING even though a human can see x > 0.

5. **Inter-procedural analysis is context-insensitive.** If a method can return different signs depending on its arguments, the analysis joins all possibilities. This loses precision but is simpler.

6. **IALOAD/IASTORE check the INDEX, not the array reference.** The array reference is below the index on the stack.

7. **UNINITIALIZED is a sentinel, not a lattice value.** It's used for variables that haven't been assigned yet. It behaves differently from BOTTOM in transfer functions.

---

## Connections

- [[readability-classifier]] — Same course, different project. Readability uses static metrics; sign analysis uses dataflow analysis.
- [[data-flow-analysis]] — Sign analysis IS a dataflow analysis. The fixpoint iteration, the transfer functions, the lattice — these are the core concepts of dataflow analysis.
- [[abstract-interpretation]] — Sign analysis is the simplest example of abstract interpretation. The "abstract domain" is the sign lattice; the "concrete domain" is all possible integer values.
- [[control-flow-graph]] — The analyzer operates on the CFG of bytecode instructions. Join points in the CFG are where merge() is called.
- [[java-for-software-analysis]] — Both projects use Maven, JUnit, picocli. This project also uses ASM extensively.

---

## Open Questions
- How would you extend this to handle condition narrowing (e.g., `if (x > 0)` narrows x to PLUS)?
- What's the difference between context-sensitive and context-insensitive inter-procedural analysis?
- How does this analysis relate to typing systems (which also use lattices)?
- What other abstract domains could you use instead of signs? (e.g., intervals, parity, nullness)
