---
title: "Advanced IT Security — Lecture 1: Introduction to Cryptography (Hashes, MACs, and the Two Kinds of Security)"
tags: [topic, advanced-it-security, semester-2, lecture, cryptography]
course: "Advanced IT Security"
source_count: 2
status: current
last_updated: 2026-11-04
prerequisites: ["[[advanced-it-security-lecture-0b]]"]
---

## One-line Summary
The deck that opens cryptography proper: what cryptology is and is not, the old and the new paradigm (mutually trusting parties vs commerce with trusted third parties), the unconditional/conditional divide, the three cryptographic services, and — as far as the ingested 16 slides go — the whole treatment of hash functions: MDC vs MAC, OWHF vs CRHF, and the three resistance properties.

## Core Map

```
Advanced IT Security — Lecture 1, "Introduction to Cryptography"  (16 slides, 20261102_1_Symmetric.pdf)
│
├── What cryptography is (slides 3–4)
│   ├── cryptology = cryptography + cryptanalysis
│   ├── cryptography: mathematical techniques for confidentiality, data
│   │   integrity, entity authentication, data origin authentication
│   └── the slide's own disclaimer: cryptography does not *solve* security
│       problems, it transforms them into other (hopefully easier) ones
│
├── Why it is needed: two secure end systems over an insecure channel (5–8)
│   ├── old paradigm: A and B trust each other; the intruder is an outsider
│   │   who can read, delete and insert messages
│   ├── new paradigm: electronic commerce, A and B do NOT trust each other
│   │   → protection is needed against insider fraud too, and a trusted
│   │     third party (TTP) is needed to settle disputes
│   └── law enforcement: LEA interception; key recovery (keys to their owner)
│       vs key escrow (keys to the LEA) — organisation, not mathematics
│
├── How security is claimed (9)
│   ├── unconditional security: holds against unbounded computing power
│   │   → measured with information theory
│   └── conditional security: breakable in principle, but beyond a realistic
│       adversary → measured with complexity theory
│       → [[unconditional-vs-conditional-security]]
│
├── Cryptographic security services (10)
│   ├── data confidentiality ← encryption hides content
│   ├── data integrity ← hash / integrity-check functions detect changes
│   └── data origin authentication ← digital signatures and MACs
│
└── Hash functions — the deck's payload (11–16)
    ├── definition (HAC): ease of computation + compression (11–12)
    ├── functional classification: MDC (unkeyed) vs MAC (keyed) (13)
    │   ├── OWHF: pre-image + 2nd pre-image resistant (passwords)
    │   └── CRHF: 2nd pre-image + collision resistant
    │       → [[mdc-vs-mac]]
    └── security properties: pre-image, 2nd pre-image, collision (14–16)
        → [[cryptographic-hash-functions]]
```

## Key Concepts at a Glance

| Page | One-line idea |
|------|---------------|
| [[cryptographic-hash-functions]] | Compression plus ease of computation, and three resistance properties whose implication direction (collision ⇒ 2nd pre-image, **not** pre-image) is the exam's favourite trap. |
| [[unconditional-vs-conditional-security]] | Unbounded adversary → information theory → no attack can exist; bounded adversary → complexity theory → no attack is affordable. Different claims, not different degrees. |
| [[mdc-vs-mac]] | Unkeyed digest detects change only with a trusted reference; keyed digest authenticates the source, which is why a hash travelling with its own message proves nothing. |

## Lecture Structure

| Slide | Content |
|-------|---------|
| 1–2 | Title (*Introduction to Cryptography*) with the Don Alvarez epigraph on cryptography as a framework for paranoid delusions |
| 3 | Agenda: 1 Introduction · 2 Hash functions & MACs · 3 Symmetric key cryptography · 4 Public key cryptography · 5 Digital signatures · 6 Authentication — key establishment |
| 4 | Cryptology = cryptography + cryptanalysis; the modern definition; the "transforms problems" note |
| 5 | Origins: Alice and Bob, two secure end systems, an insecure channel, an enemy listening; cryptography as an enabling technology |
| 6 | Old paradigm: A and B trust each other; the intruder reads, deletes, inserts |
| 7 | New paradigm: customer/merchant, mutual distrust, insider fraud, TTP |
| 8 | Law enforcement: LEA interception, key recovery vs key escrow |
| 9 | Unconditional vs conditional security, information vs complexity theory |
| 10 | The three cryptographic security services |
| 11 | Hash functions for integrity checks; hash value = message digest = checksum |
| 12 | Definition per HAC: ease of computation, compression; unkeyed vs keyed `h(x,k)` |
| 13 | Manipulation detection codes (OWHF/CRHF) vs message authentication codes |
| 14 | The three security properties, in HAC's wording |
| 15 | The properties drawn as four one-way arrows (ease of computation is the trivial axis) |
| 16 | OWHF vs CRHF property lists, the three Notes, and the named functions SHA-1, RIPEMD-160, MD5 |

## Exam-Relevant Points

1. **The three-way terminology split** — cryptography (building), cryptanalysis (breaking), cryptology (the union). Slide 4's wording is the exam's wording, including the "cryptography does not solve security problems" line, which is the question a *why* answer is graded against.
2. **Old vs new paradigm, and why a TTP appears.** Old: two parties who trust each other, one outsider intruder. New: parties who do not trust each other, an insider threat as well, and a TTP to settle disputes. The TTP is needed because arbitration between mutually distrusting parties has nowhere else to come from.
3. **The adversary's resource model** as the *fundamental* difference between unconditional and conditional security — not the size of the key, and not "practical vs theoretical".
4. **The three services and which primitive provides each.** Confidentiality ← encryption; integrity ← hash/integrity functions; origin authentication ← signatures and MACs. Mapping a scenario to the right service is the standard task shape (cf. exercise 1's CIA task).
5. **The three hash properties, defined with the free variable.** Pre-image: target given, find input. Second pre-image: input given, find *another* input with the same digest. Collision: find any two. Ordering and implications follow from the free variable.
6. **The implication that holds and the one that does not.** Collision resistance ⇒ second pre-image resistance (slide Note 1); collision resistance does **not** ⇒ pre-image resistance (Note 3), with practical CRHFs usually being pre-image resistant anyway (Note 2).
7. **MDC vs MAC as the keyed/unkeyed split**, and the direct consequence for the origin-authentication service.
8. **Key recovery vs key escrow** — two definitions that sound alike and are not: recovery returns a key to its owner, escrow hands it to a law-enforcement agency.

## Connections

- [[advanced-it-security-lecture-0]] and [[advanced-it-security-lecture-0b]] — the vocabulary this deck builds on (assets, risk, CIA, attackers, integrity as a definition landscape).
- [[advanced-it-security-exercise-1]] — the previous sheet: terminology, attackers, policy/mechanism/assurance.
- [[advanced-it-security-exercise-2]] — the sheet that exercises this deck, question for question (discussion 05.11.2026).
- [[cryptographic-hash-functions]], [[mdc-vs-mac]], [[unconditional-vs-conditional-security]] — the three pages this deck produced.
- [[integrity-definition-landscape]] — lecture 0's version of "what integrity is not", which this deck's integrity service inherits.
- [[gsm-security-political-constraints]] — the LEA/key-escrow theme in its applied, political form.
- `raw/lectures/Advanced IT Security/Vorlesung/20261102_1_Symmetric.pdf` — the deck (16 pages, extracted 2026-11-04).

## Open Questions

- **The file is named `20261102_1_Symmetric.pdf`, but the deck contains no symmetric encryption.** It is titled "Introduction to Cryptography" and ends at slide 16 on hash functions; symmetric ciphers are agenda item 3, i.e. the *next* deck. Whether the rest of the lecture 1 material follows in a separate file, or whether this single file is the whole of "lecture 1", is not stated by the material.
- **Agenda items 3–6 (symmetric, public key, signatures, key establishment) have no slides in `raw/` yet** — this is the course's largest gap, and it is the material the exam is built on.
- **MACs are deferred on the slide itself ("see later"),** so the deck's "rule" for agreeing a key is not present; the sheet's 2(e) answer has to be built from the classification slide alone.
- **The Don Alvarez epigraph is decorative**, but the slide's own disclaimer ("cryptography does not solve security problems") is the testable version of it — the two should not be confused in an answer.
