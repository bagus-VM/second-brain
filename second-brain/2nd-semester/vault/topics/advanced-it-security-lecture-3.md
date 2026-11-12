---
title: "Advanced IT Security — Lecture 3: Defining Security with Games and Symmetric Ciphers"
tags: [topic, advanced-it-security, semester-2, lecture, cryptography]
course: "Advanced IT Security"
source_count: 1
status: current
last_updated: 2026-11-12
prerequisites: ["[[advanced-it-security-lecture-2]]"]
---

## One-line Summary
The lecture formalizes cryptographic security as an adversarial game, then surveys classical substitution and transposition ciphers before explaining the one-time pad and block-versus-stream encryption.

## Core Map

```
Security model
├── define adversary knowledge and oracle access
├── define winning condition; require negligible success for efficient attackers
│   └── ciphertext / known-plaintext / chosen-plaintext / adaptive / chosen-ciphertext
└── symmetric encryption: same secret key encrypts and decrypts
    ├── historical ciphers: Caesar, substitution, homophonic, Vigenère, transposition
    ├── one-time pad: message XOR random key; information-theoretic security if never reused
    └── modern classification: block cipher vs stream cipher
```

## Key Concepts at a Glance

| Page | One-line idea |
|------|---------------|
| [[cryptographic-security-games]] | A security claim is a specified adversarial experiment, a win condition, and a bound on efficient adversaries' success. |
| [[classical-cipher-cryptanalysis]] | Classical ciphers and Enigma fail when key count obscures frequency patterns, key-period structure or operational weaknesses. |
| [[one-time-pad]] | XOR with a truly random, secret, message-length key gives perfect secrecy only when the key is never reused. |
| [[symmetric-encryption]] | The lecture introduces the shared-key model; the fuller existing Semester 1 page remains canonical. |
| [[advanced-it-security-lecture-2]] | The preceding lecture introduces the notation and attacker's algorithm-knowledge assumption. |

## Lecture Structure

The extracted source begins at printed slide 56 and runs through slide 93. Slides 56–63 introduce games, adversarial input/oracles/output, attack classes, and the three-part recipe for defining security. Slides 64–65 formalize encryption and key pairs; slides 66–71 survey Caesar, monoalphabetic and homophonic substitution, Vigenère, and attacks based on frequency analysis. Slides 72–77 present the one-time pad and its randomness/security conditions. Slides 78–92 cover transposition, composition, Enigma, and why its key space did not prevent practical cryptanalysis. Slides 93 distinguishes block and stream ciphers.

## Exam-Relevant Points

1. State a game-based definition by naming the adversary's information/oracles, its winning condition, and the security bound (efficient adversaries win only with negligible probability).
2. Distinguish ciphertext-only, known-plaintext, chosen-plaintext, adaptive chosen-plaintext, and chosen-ciphertext access by what the attacker may observe or choose.
3. For symmetric encryption, Alice and Bob share secret key material; encryption and decryption are efficiently related. For n parties communicating pairwise, the lecture notes a quadratic number of keys.
4. A one-time pad requires a uniformly random key at least as long as the message, secret delivery, and no reuse. Reuse or weak randomness invalidates the stated guarantee.
5. Classical substitution preserves frequency structure; transposition preserves the letters themselves. Enigma's nominal key-space size did not neutralize implementation-specific and operational weaknesses.
6. The deck's final terminology: block ciphers encrypt fixed-length blocks under a fixed key; stream ciphers encrypt short units under a changing keystream.

## Connections

- [[advanced-it-security-lecture-2]] — defines encryption notation and the assumption that the algorithm is public.
- [[advanced-it-security-exercise-3]] — asks students to apply hash and symmetric-encryption concepts; this page describes, but does not answer, the sheet.
- [[cryptographic-security-games]] and [[one-time-pad]] — the new concept pages for the lecture's formal model and perfect-secrecy example.
- [[symmetric-encryption]] — canonical Semester 1 page; not duplicated here.
- [[unconditional-vs-conditional-security]] — distinguishes the one-time pad's information-theoretic guarantee from computational security.

## Open Questions

- The PDF is a continuation segment, numbered slides 56–93, without a new title or lecture date; the course lecture numbering/date is not stated in this file.
- The slide claims a pairwise key requirement of about n² for n parties but does not state whether it means exactly n(n−1)/2 or a rough order estimate.
- The extraction contains image-only slides (including the Caesar diagram and some historical images); no missing diagram details are inferred.
- The slide's informal randomness checklist is not a formal definition of a uniform random key. The one-time-pad guarantee requires uniform independent key bits.
