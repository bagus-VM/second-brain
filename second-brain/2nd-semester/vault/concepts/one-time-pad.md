---
title: "One-Time Pad"
tags: [concept, cryptography, semester-2, advanced-it-security]
course: "Advanced IT Security"
source_count: 1
status: current
last_updated: 2026-11-12
prerequisites: ["[[symmetric-encryption]]"]
---

## One-line Summary
A one-time pad encrypts each message bit by XORing it with a uniformly random secret key bit, giving perfect secrecy only when the key is at least message-length and never reused.

## Core Intuition
The key acts like fresh random noise. For any ciphertext and any candidate plaintext of the same length, exactly one key could have produced it, so observing ciphertext alone does not favor one plaintext over another—provided the pad really is uniform and secret.

## Formal Definition / Statement
For bit strings x and K of equal length n, encryption is c = x XOR K and decryption is x = c XOR K, since XORing the same bit twice cancels it. Perfect secrecy requires a uniformly random key, independent of the message, at least as long as the message, kept secret and used only once.

## Key Properties
- Information-theoretic security does not depend on limiting the adversary's computation.
- Key material must be as long as the protected message.
- Key generation, secure delivery, storage and synchronization are operational burdens.
- Reusing a pad leaks the XOR of the plaintexts: c₁ XOR c₂ = x₁ XOR x₂.
- A pseudorandom generator can make a shorter stream computationally useful, but that is not a one-time pad's unconditional guarantee.

## Worked Example
Let x = 0110010 and K = 1011001. Bitwise XOR gives c = 1101011. Decryption repeats the same operation: 1101011 XOR 1011001 = 0110010. Each key bit flips or preserves its corresponding message bit.

## Common Pitfalls
- “One-time” is literal: using the same pad twice breaks the stated secrecy guarantee.
- A key that merely looks random is not necessarily uniformly random or independent.
- The pad is not practical for ordinary long-lived communication unless key distribution is solved.
- XOR makes decryption work; it does not by itself establish integrity or authenticity.

## Connections
- [[symmetric-encryption]] — the OTP is a symmetric stream cipher with identical encryption/decryption operation.
- [[unconditional-vs-conditional-security]] — the OTP is the lecture's example of unconditional security under strict assumptions.
- [[cryptographic-security-games]] — a formal game can express what an attacker learns from ciphertext.

## Open Questions
- The lecture gives an informal checklist for randomness, not a complete formal probability-space proof.
- The deck does not discuss authenticated encryption or how to prevent active tampering.
