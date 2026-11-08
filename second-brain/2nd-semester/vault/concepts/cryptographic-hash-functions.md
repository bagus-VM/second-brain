---
title: "Cryptographic Hash Functions"
tags: [concept, advanced-it-security, semester-2, cryptography]
course: "Advanced IT Security"
source_count: 2
status: current
last_updated: 2026-11-04
prerequisites: []
---

## One-line Summary
A function that compresses an arbitrary-length input to a fixed-length digest, is cheap to compute, and is hard to invert — with three distinct "hard" properties (pre-image, second pre-image, collision resistance) that are routinely confused for one another.

## Core Intuition
Hashing turns "is this message unchanged?" into "is this short string still the same?", which is a question cheap storage and cheap comparison can answer. The price is that a fixed-length output cannot be injective, so collisions must exist; cryptographic hashing is the art of making them *impossible to find* rather than impossible to exist. The three resistance properties are three different search problems, and their difficulty ordering is the exam's favourite move: collision resistance implies second-pre-image resistance, but not pre-image resistance, because the attacker's freedom differs in each.

## Formal Definition / Statement
HAC's minimum definition — a hash function `h` has at least:

- **Ease of computation**: given `h` and an input `x`, computing `h(x)` is easy.
- **Compression**: `h` maps inputs of arbitrary length to fixed-length results.

*Unkeyed* hashing is what "hash function" usually means; a **keyed** hash function is `h(x, k)`, taking an arbitrary-length input `x` and a fixed-length key `k`.

**Security properties** (HAC's three, with the free variable that defines each):

| Property | Adversary is given | Must find | Formal statement |
|---|---|---|---|
| Pre-image resistance (one-way) | a target value `y` | any `x` with `h(x) = y` | for any given `y`, computationally infeasible to find `x` so that `h(x) = y` |
| Second pre-image resistance | a specific input `x` | a different `x' ≠ x` | given `x`, computationally infeasible to find `x' ≠ x` so that `h(x) = h(x')` |
| Collision resistance | — | any two distinct inputs | computationally infeasible to find `x` and `x'`, `x ≠ x'`, so that `h(x) = h(x')` |

**Functional classification** (the lecture's slide 13):

- **MDC — manipulation detection code** (also modification detection code / message integrity code): *unkeyed*, used to detect changes to a document. Two kinds:
  - **OWHF** (one-way hash function): ease of computation, compression, pre-image resistance, second-pre-image resistance.
  - **CRHF** (collision-resistant hash function): ease of computation, compression, second-pre-image resistance, collision resistance.
- **MAC — message authentication code**: *keyed* (`h(x, k)`), used to assure both the source of a message and its integrity. See [[mdc-vs-mac]].

## Key Properties
- **Collision resistance implies second pre-image resistance** (slide Note 1): finding a collision for a *given* `x` is a special case of finding any collision — any algorithm for the general problem solves the restricted one, so the restricted one cannot be easier. The converse fails.
- **It does not imply pre-image resistance** (Note 3): pathological constructions are collision resistant while being easy to invert. In practice, CRHFs are preimage resistant as well (Note 2) — but that is an empirical property of the designs used, not a theorem.
- **Hence the strength ordering:** collision resistance ⊇ second pre-image resistance, and pre-image resistance sits on its own axis. Collision resistance is usually the *hardest* to achieve in practice because the *birthday bound* applies: with an `n`-bit digest, collisions are expected after about `2^(n/2)` evaluations, whereas pre-images need about `2^n`.
- **Intended use decides the required property.** Storing passwords needs an OWHF (pre-image resistance is the point: the digest must not be inverted to the password). Binding a document to its digest needs a CRHF (an attacker who can find any second input with the same digest has forged the document).
- **Fixed output length, so integrity is only as strong as the digest.** The digest must be stored or transmitted through a trusted channel; a hash value that travels with its own message protects against nothing against an active attacker.
- Named in the lecture as well-known: **SHA-1, RIPEMD-160, MD5**.

## Worked Example
Exercise sheet 2, Question 2(c) asks for the matching in the other direction, and it is the clean test of whether the three definitions are separable:

| Situation | Property |
|---|---|
| Given a hash value `y`, find a message `m` with `h(m) = y` | **pre-image resistance** |
| Given a message `m`, find `m' ≠ m` with `h(m) = h(m')` | **second pre-image resistance** |
| Find *any* two different messages `m ≠ m'` with `h(m) = h(m')` | **collision resistance** |

The pattern to read off: (a) has no input at all, (b) has the input fixed and only the target free, (c) has both free. Freedom increases from (a)/(b) to (c), which is why collision resistance is the strongest of the three.

For a 32-bit digest the *size* question (sheet 2(d)) is arithmetic: `2^32 = 4 294 967 296` possible values — and the matching collision estimate, from the birthday bound, is about `2^16 = 65 536` evaluations by the usual rule of thumb (the exact formula `sqrt(2·2^32·ln 2) ≈ 77 163` for a 50 % chance; the two agree to within the accuracy that matters). That 4-billion-versus-tens-of-thousands gap is exactly why digest length is chosen from the birthday bound, not from the pre-image bound.

## Common Pitfalls
- **Calling any of the three "the" hash property.** "SHA-1 is broken" means collisions are findable; it does not mean pre-images are. Answer the property that was asked about.
- **Assuming collision resistance gives pre-image resistance.** The slide's Note 3 says the opposite: pathological counterexamples exist. State the implication in the direction that holds (collision ⇒ second pre-image).
- **Confusing "hash" with "authenticate".** An unkeyed digest proves nothing about *who* produced a message; see [[mdc-vs-mac]].
- **Confusing compression with collision freedom.** Compression is a statement about lengths (arbitrary in, fixed out) and is exactly what makes collisions unavoidable; resistance is about the *difficulty of finding* them.
- **Comparing digests with `==`/byte-wise `strcmp` in real code** — a classic timing side channel when the digest is secret; the lecture's material does not raise it, but the exam's integrity framing makes it fair game.
- **Computing a digest in the same untrusted place the digest is stored** — an integrity check whose reference value can be rewritten by the same attacker protects against nothing.

## Connections
- [[mdc-vs-mac]] — the keyed/unkeyed split, and why an ordinary digest cannot authenticate a sender.
- [[unconditional-vs-conditional-security]] — "computationally infeasible" is a *conditional* security claim, and this is the page that says what that means.
- [[integrity-definition-landscape]] — the same theme from lecture 0: integrity is about the data's history, not its truth.
- [[advanced-it-security-lecture-1]] — the deck this page came from (slides 11–16).
- [[advanced-it-security-exercise-2]] — Question 2 works these definitions out in the exam's own phrasing.
- [[hashing]] (Semester 1) — hashing as a data-structure technique; this page is the cryptographic contract, not the collision-strategy one.

## Open Questions
- **The lecture names SHA-1, RIPEMD-160 and MD5 without stating their digest lengths or their status**; the deck's slide 16 is the end of the material ingested, so the "which of these is still safe" discussion is not in this source.
- **The HAC reference is cited by slide but not given as a full bibliographic entry** in the deck; the definition quoted above is the slide's own wording.
- **No construction is shown** (Merkle–Damgård, sponge) — how a fixed-length digest is actually built from a compression function is not covered in the ingested slides.
