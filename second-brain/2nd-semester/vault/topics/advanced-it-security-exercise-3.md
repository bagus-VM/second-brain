---
title: "Advanced IT Security — Exercise 3 Overview (Hash Functions and Symmetric Cryptography)"
tags: [topic, advanced-it-security, semester-2, exercise, cryptography]
course: "Advanced IT Security"
source_count: 1
status: current
last_updated: 2026-11-12
prerequisites: ["[[advanced-it-security-lecture-2]]", "[[advanced-it-security-lecture-3]]"]
---

## One-line Summary
Exercise 3 asks students to explain cryptographic hashes versus CRCs, compare pre-image and birthday collision work, and reason about confidentiality and key compromise in symmetric-key communication.

## Core Map

```
Exercise 3 (discussion date printed: 12 Nov 2026)
├── Q1: cryptographic hash functions
│   ├── CRC vs adversarial integrity
│   ├── collisions are inevitable for finite outputs
│   └── 64-bit vs 128-bit pre-image and birthday work
└── Q2: symmetric cryptography
    ├── encryption/decryption notation and key relation
    ├── ciphertext visibility, denial, and key compromise
    └── Alice → Bob → Charlie: confidentiality limits of a relay
```

## Key Concepts at a Glance

| Page | What the sheet tests |
|------|----------------------|
| [[cryptographic-hash-functions]] | Distinguish cryptographic security properties from error-detection checksums. |
| [[birthday-bound]] | Compare generic pre-image work (2ⁿ) with collision work (about 2ⁿᐟ²). |
| [[symmetric-encryption]] | Apply encryption/decryption notation and reason about a shared key and a relay. |
| [[one-time-pad]] | A concrete symmetric cipher, though the sheet does not ask specifically about it. |

## Exercise Structure

Question 1 has three parts: explain why CRCs are not cryptographic hashes; explain why finite-output hash functions necessarily have collisions without concluding that they are automatically insecure; and compare approximate pre-image and birthday-collision attempts for 64-bit and 128-bit outputs. Question 2 asks for the symmetric-encryption principle and notation, analyzes an interceptor who lacks the key (including whether they can block delivery and what key compromise changes), then considers Alice sending to Charlie through Bob when Alice and Bob, and Bob and Charlie, hold different shared keys. The final part asks how Alice could keep plaintext confidential from Bob.

This page records the task scope only; it does not provide answers or computations.

## Exam-Relevant Points

- The sheet explicitly separates collision existence from practical collision-finding cost.
- It tests order-of-growth reasoning as hash output length changes, not just memorized names.
- Confidentiality is not availability: an interceptor may be unable to decrypt yet still prevent delivery.
- A relay that possesses the keys used on each leg may see plaintext between decrypting and re-encrypting; the final sub-question asks for an end-to-end alternative.
- The source has a duplicated subpart label in Q1 and Q2; its question numbering is preserved here by question name, not repaired.

## Connections

- [[advanced-it-security-lecture-2]] — hash functions, CRC distinction, and birthday-bound setup.
- [[advanced-it-security-lecture-3]] — symmetric encryption, key roles, and adversarial games.
- [[birthday-bound]] and [[cryptographic-hash-functions]] — the hash concepts tested by Q1.
- [[symmetric-encryption]] — canonical Semester 1 explanation of the shared-key model.
- [[advanced-it-security]] — the course page and exercise rules; exercise material is examinable.

## Open Questions

- The discussion date is stated as 12 November 2026; a submission deadline is not stated.
- No official solution file was present among today's downloaded sources.
- The sheet asks approximately how many attempts but does not specify success-probability conventions or a computational rate; it is an order-of-magnitude exercise.
