---
title: "Software Analyse — Projects Overview"
tags: [concept, software-analyse, semester-1]
course: "Software Analyse"
source_count: 2
status: current
last_updated: 2026-06-09
prerequisites: ["[[java-for-software-analysis]]"]
---

## One-line Summary
An overview of the two Software Analyse projects: a readability classifier that predicts code quality using static metrics and machine learning, and an interprocedural sign analysis that finds division-by-zero and negative-array-index bugs via abstract interpretation.

## Core Intuition
Both projects apply **static analysis** — extracting information from code without running it — but they answer fundamentally different questions:

- **Readability Classifier:** "Is this code readable?" → *Quality measurement* using metrics (LOC, entropy, Halstead, cyclomatic complexity) fed into a logistic regression model.
- **Sign Analysis:** "Can this code crash?" → *Bug detection* using dataflow analysis over an abstract sign lattice to find division-by-zero and negative array index bugs.

They share the same Java toolchain (Maven, JUnit, picocli) and demonstrate two major branches of static analysis: **metric-based analysis** and **dataflow analysis**.

---

## Project 1: Readability Classifier

**Goal:** Predict whether humans find a code snippet readable (Y/N) based on static metrics alone.

**Pipeline:**
1. **Feature extraction** — Parse each `.jsnp` file with JavaParser, compute four metrics:
   - Number of Lines (LOC)
   - Token Entropy (Shannon entropy of token distribution)
   - Halstead Volume (V = N × log₂(η))
   - Cyclomatic Complexity (M = decision points + 1)
2. **Preprocessing** — Threshold ground truth scores at 3.6 (≥3.6 = readable, <3.6 = not) for a balanced 50/50 split.
3. **Classification** — Load into WEKA, standardize features (z-score), train logistic regression with ridge regularization (λ = 10⁻⁶), evaluate with 10-fold cross-validation.

**Key result:** ~70–80% accuracy. No single metric captures readability alone — the combination matters.

**Full guide:** [[readability-classifier]]

---

## Project 2: Interprocedural Sign Analysis

**Goal:** Find division-by-zero and negative-array-index bugs in Java bytecode without running the code.

**Approach:**
1. **Abstract domain** — Track the sign (−, 0, +) of every integer value using a bitmask-encoded lattice (8 elements, from ⊥ to ⊤).
2. **Transfer functions** — Define how signs propagate through arithmetic operations (IADD, ISUB, IMUL, IDIV) using pairwise decomposition of composite values.
3. **Inter-procedural analysis** — When a method call is encountered, recursively analyze the callee, join all return values, and propagate the result back.
4. **Bug detection** — After fixpoint, scan for IDIV with zero divisor and IALOAD/IASTORE with negative index.

**Key concepts:** Lattice theory, bitmask encoding, pairwise decomposition, ASM framework, fixpoint iteration, context-insensitive analysis.

**Full guide:** [[sign-analysis]]

---

## Comparing the Two Projects

| Aspect | Readability Classifier | Sign Analysis |
|--------|----------------------|---------------|
| **Question** | Is this code readable? | Can this code crash? |
| **Technique** | Metrics + ML (supervised) | Dataflow analysis (abstract interpretation) |
| **Input** | Java source (via JavaParser) | Java bytecode (via ASM) |
| **Output** | Y/N label + probability | Error/warning reports |
| **Framework** | WEKA (ML) | ASM (bytecode analysis) |
| **Theoretical basis** | Software metrics, logistic regression | Lattice theory, transfer functions |

---

## Shared Infrastructure

- **Build system:** Maven
- **CLI framework:** picocli
- **Testing:** JUnit
- **Language:** Java
- **Prerequisite:** [[java-for-software-analysis]]

---

## Connections
- [[readability-classifier]] — Full deep study guide for Project 1.
- [[sign-analysis]] — Full deep study guide for Project 2.
- [[java-for-software-analysis]] — Shared Java ecosystem reference for both projects.
- [[data-flow-analysis]] — Theoretical foundation for sign analysis.
- [[machine-learning-basics]] — Theoretical foundation for the readability classifier's ML pipeline.
- [[software-analyse-lecture-1]] — Source lecture: Software Analyse introduction (Course Roadmap + Projects section)

## Open Questions
- How do the two approaches complement each other in a real software quality workflow?
- Could dataflow analysis improve the readability classifier (e.g., by adding control flow metrics)?
- What other static analysis techniques could be applied to the same course projects?
