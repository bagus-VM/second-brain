---
title: "Cryptographic Security Games"
tags: [concept, cryptography, semester-2, advanced-it-security]
course: "Advanced IT Security"
source_count: 1
status: current
last_updated: 2026-11-12
prerequisites: ["[[symmetric-encryption]]"]
---

## One-line Summary
A cryptographic security game makes a security claim precise by specifying what an attacker knows, what queries it may make, how it wins, and how small its success probability must be.

## Core Intuition
“Secure” is incomplete unless the attacker and the protected property are specified. A game turns that vague claim into a repeatable challenge: give an adversary defined access, then ask whether it can do better than the allowed baseline.

## Formal Definition / Statement
A game-based definition specifies (1) adversary input, (2) an oracle modeling permitted observations or queries, (3) a winning condition, and (4) a bound on success. The lecture's general criterion is that every efficient adversary wins with at most negligible probability (or no significantly greater probability than random guessing in the stated example).

## Key Properties
- Ciphertext-only: attacker receives ciphertexts and tries to recover plaintexts or key.
- Known-plaintext: attacker receives plaintext/ciphertext pairs.
- Chosen-plaintext: attacker chooses plaintexts to be encrypted.
- Adaptive chosen-plaintext: later choices may depend on prior encryption results.
- Chosen-ciphertext: attacker submits ciphertexts for decryption and sees plaintexts.
- Different oracle access produces different security notions; a result under one game does not automatically imply security under another.

## Worked Example
For the lecture's conventional-encryption indistinguishability game, an attacker submits a message x. In one case the oracle returns its encryption under a fixed random key; in the other it returns an encryption of an unrelated random message. The attacker wins by telling the cases apart. Security requires that an efficient attacker cannot distinguish them substantially better than guessing. This is the lecture's intuition, not a full modern IND-CPA definition.

## Common Pitfalls
- Saying “the algorithm is secure” without naming the attack model or winning condition.
- Treating ciphertext-only and chosen-ciphertext security as equivalent.
- Confusing computational security with unconditional security.
- Calling a particular example a complete modern definition when the slide gives only a sketch.

## Connections
- [[symmetric-encryption]] — the cipher family whose confidentiality games are discussed.
- [[unconditional-vs-conditional-security]] — distinguishes bounded computational attackers from unbounded ones.
- [[cryptographic-hash-functions]] — hash security can also be phrased as an adversarial game with a property-specific win condition.

## Open Questions
- The lecture does not define negligible probability formally or state a security parameter.
- The conventional-encryption example is an intuition sketch; exact challenge-query restrictions are not fully specified.
