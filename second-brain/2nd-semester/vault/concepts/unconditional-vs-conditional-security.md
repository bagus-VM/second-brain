---
title: "Unconditional vs Conditional Security"
tags: [concept, advanced-it-security, semester-2, cryptography]
course: "Advanced IT Security"
source_count: 2
status: current
last_updated: 2026-11-04
prerequisites: []
---

## One-line Summary
Unconditional security holds even against an adversary with unbounded computing power and is therefore measured with information theory; conditional security holds only because breaking it costs more than a realistic adversary can afford, and is therefore measured with complexity theory.

## Core Intuition
"Secure" is never a property of a system on its own — it is a property relative to an adversary with some amount of resources. The two classes differ in *which resource is allowed to be infinite*. If the adversary's computing power is unbounded and the system still holds, the guarantee comes from the structure of information itself (there is simply nothing to learn from the ciphertext), and no future machine can break it. If the adversary is merely computationally bounded, the guarantee is an *estimate of cost* — today's estimate, about today's algorithms and machines — and it is exactly as durable as that estimate.

The practical consequence: only one of the two can be proved in the mathematical sense. The other is a bet on the state of the art, and every "broken" headline in cryptography is a lost bet of this second kind.

## Formal Definition / Statement
The lecture's slide 9 draws the division as a tree:

```
Cryptographic security
├── Unconditional Security
│     System is secure even if the adversary has unbounded computing power.
│     → Security can be measured using information theory.
└── Conditional Security
      System can be broken in principle, but this requires more computing power
      than a realistic adversary would have.
      → Security can be measured using complexity theory.
```

The fundamental difference is therefore **the resource model of the adversary** (unbounded vs bounded), and it determines both the **proof technique** (information-theoretic argument vs reduction to a computational hardness assumption) and the **kind of guarantee** (no attack can exist vs no feasible attack is known).

## Key Properties
- **Information-theoretic security is a statement about distributions, not about algorithms.** Perfect secrecy (Shannon) is the canonical example: the ciphertext is statistically independent of the plaintext, so no computation — however long — extracts information. Its price is normally a key as long as the message (the one-time pad), which is why it is rare in practice.
- **Conditional security is a statement about work.** It is quantified as key length or security parameter, and it presupposes a *model of computation*. Change the model (quantum search, new cryptanalysis, more parallelism) and the estimate changes without the system changing at all.
- **The two are not degrees of the same scale.** A conditionally secure scheme with a large enough parameter is not "almost unconditional"; there is no sequence of conditional guarantees converging to an unconditional one.
- **Conditional security is what real systems use**, and the honest phrasing is "no known attack below X operations" — which is why key lengths are revised over decades while the algorithms stay the same.
- **The distinction is examinable as a *definition*, not as an example list.** Any answer should say unbounded/bounded computing power and information/complexity theory; examples are decoration.

## Worked Example
The 32-bit hash question from exercise sheet 2(d) is a small conditional-security calculation, and it shows the shape of the reasoning:

- There are `2^32 = 4 294 967 296` possible digests.
- A **pre-image** search is expected to need about `2^32` evaluations — unconditional statements are impossible here, because a bounded attacker is exactly the assumption.
- A **collision** search needs only about `2^16 = 65 536` evaluations by the birthday bound (exactly `sqrt(2·2^32·ln2) ≈ 77 163` for 50 % probability).
- Both numbers are *costs*, and the claim "this is secure" therefore means "these costs exceed what a realistic adversary would spend" — conditional security, in the precise sense of the slide.

Contrast the one-time pad: no computation cost protects it; the plaintext is simply unrecoverable from the ciphertext for *any* adversary, and that argument uses no complexity assumption at all.

## Common Pitfalls
- **Saying "it is secure" without the adversary.** Both classes are relative; the slide's division exists precisely to force the resource model into the statement.
- **Treating "unbreakable in practice" as a weaker version of "unbreakable".** It is a different kind of claim, not a fraction of it.
- **Assuming unconditional security is always preferable.** The one-time pad's key distribution problem makes it unusable for most applications; the choice is engineering, not correctness.
- **Reading a complexity-theory claim as permanent.** Conditional security is a statement about the state of the art and is falsified by a better algorithm, not by a failure of the mathematics.
- **Using information theory to argue about a computational scheme.** Shannon entropy bounds say nothing useful about a cipher whose hardness rests on factoring.

## Connections
- [[cryptographic-hash-functions]] — "computationally infeasible" in its definitions is exactly the conditional notion defined here.
- [[mdc-vs-mac]] — the security of a MAC is a conditional claim of the same kind.
- [[security-cost-benefit-optimum]] — lecture 0's version of the same idea: how much security to buy is an economic decision, and it requires the adversary's capability to be named.
- [[risk-perception-and-dread-risk]] — why "secure" claims are often accepted without the adversary being named.
- [[advanced-it-security-lecture-1]] — the deck this page came from (slide 9).
- [[advanced-it-security-exercise-2]] — Question 1(c) asks for exactly this distinction.

## Open Questions
- **The deck does not develop the information-theoretic side** (no perfect-secrecy theorem, no one-time pad in the ingested slides); the 16 slides end at hash functions, so this page stays at the definitional level the source supports.
- **No computational hardness assumptions are named** in the ingested material (factoring, discrete log, generic search), so the "measured using complexity theory" line is not yet backed by a concrete reduction in the course.
