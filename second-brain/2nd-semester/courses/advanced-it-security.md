---
title: "Advanced IT Security"
tags: [course, semester-2, advanced-it-security]
professor: "Prof. Dr. Joachim Posegga"
semester: "WS 2026/27"
exam_date: "2027-04-05"
credits: "TBD"
language: "English"
source_count: 11
status: active
last_updated: 2026-11-12
prerequisites: []
---

## One-line Summary
A Master's-level security lecture (Posegga) whose exercise course prepares you for a written exam covering everything from lectures and exercises.

## Course Information

- **Lecture:** Prof. Dr. Joachim Posegga
- **Exercise:** Emiliia Gelóczi (emiliia.geloczi@uni-passau.de, ITZ Room 121)
- **Exercise slots:** Thursdays, 10:00–12:00, 12:00–14:00, 14:00–16:00, 16:00–18:00 — room assignments in Stud.IP
- **First exercise:** 29.10.2026
- **Language:** English
- **Exam:** written, 05.04.2027, 10:00–12:00

## Exercise Rules (from the intro sheet)

- Handing in solutions is **not mandatory**; there are **no credit points** for solutions.
- Attendance is **not mandatory** — but "highly recommended".
- Exam content: everything from the lectures **and** everything from the exercises. Exercise material is examinable.

## Lecture Index

Overview pages:
- [[advanced-it-security-lecture-0]] — Lecture 0: Basics
- [[advanced-it-security-lecture-0b]] — Lecture 0b: Basics II (properties beyond CIA, attackers, cell phones)
- [[advanced-it-security-lecture-1]] — Lecture 1: Introduction to Cryptography (hashes, MACs, unconditional vs conditional)
- [[advanced-it-security-lecture-2]] — Lecture 2: Cryptography continued (checksums, birthday bound, MD5/SHA history, HMAC, encryption)
- [[advanced-it-security-exercise-0]] — exercise organisation
- [[advanced-it-security-exercise-1]] — Sheet 1: terminology, attackers, the faulty sensor
- [[advanced-it-security-exercise-2]] — Sheet 2: cryptography, the adversary, hash functions
- [[advanced-it-security-lecture-3]] — Lecture 3: security games, symmetric ciphers, one-time pad
- [[advanced-it-security-exercise-3]] — Sheet 3: hash functions and symmetric cryptography

| # | Topic | Source | Status |
|---|-------|--------|--------|
| 0 | Basics: what security means, the elements of security, risk, CIA | `20261020_0_Basics.pdf` | ingested → [[advanced-it-security-lecture-0]] |
| 0b | Basics II: properties beyond CIA, attacker classes, cell-phone OPSEC | `20261027_0_Basics.pdf` | ingested → [[advanced-it-security-lecture-0b]] |
| 1 | Introduction to Cryptography: cryptology, old vs new paradigm, TTP, key recovery/escrow, unconditional vs conditional security, services, hash functions (MDC/MAC, OWHF/CRHF, three resistance properties) | `20261102_1_Symmetric.pdf` (16 slides) | ingested → [[advanced-it-security-lecture-1]] |
| 2 | Cryptography continued: checksums vs CRC, birthday bound, Merkle-Damgård, hash history, MACs/HMAC, first statement of symmetric encryption | `20261105_1_Symmetric.pdf` (slides 18–55) | ingested → [[advanced-it-security-lecture-2]] |
| 3 | Security games, classical symmetric ciphers, one-time pad, block vs stream ciphers | `20261110_1_Symmetric.pdf` (slides 56–93) | ingested → [[advanced-it-security-lecture-3]] |
| 0 | Exercise organisation | `Advanced_IT-Security__Introduction.pdf` | ingested → [[advanced-it-security-exercise-0]] |
| E1 | Terminology, attacker classification, the faulty sensor, policy/mechanism/assurance | `AdvITSEC_Übung_1.pdf` + `Exercise_1_with_solutions.pdf` (official answers) | ingested → [[advanced-it-security-exercise-1]] |
| E2 | Cryptography and the adversary; hash functions (pre-image / 2nd pre-image / collision, MDC vs MAC, 32-bit digest arithmetic) — discussion 05.11.2026 | `Advanced_IT_Sec_Exercise_2.pdf` | ingested → [[advanced-it-security-exercise-2]] | + official solutions (three extra tasks)

| E3 | Hash functions, birthday work, symmetric encryption and relay confidentiality — discussion 12.11.2026 | `Advanced_IT_Sec_Exercise_3.pdf` | task overview → [[advanced-it-security-exercise-3]] |

## The Course Agenda

Lecture 0 sets out the whole semester:

| # | Topic |
|---|-------|
| 0 | Basics |
| 1 | Symmetric Cryptography |
| 2 | Asymmetric Schemes (PKI) |
| 3 | Authentication |
| 4 | Access Control |
| 5 | Crypto-Protocols |
| 6 | "Real-life" Protocols: SSL/SSH, possibly others depending on time left |

Lecture 0 is the frame for the other six, and it is where the exam's vocabulary comes from:
[[risk-perception-and-dread-risk]], [[security-policy-mechanism-assurance]],
[[security-relationship-model]], [[security-cost-benefit-optimum]],
[[integrity-definition-landscape]], [[gsm-security-political-constraints]],
[[security-evaluation-and-assurance-levels]].

## What the exam asks

The exercise rules fix the scope: **everything from the lectures and everything from the
exercises is examinable.** Lecture 0 already contains the kind of question the exam will use — the
signed-but-wrong temperature reading — so the exam is not going to be about recalling slides.

## Open Questions

- **Later agenda topics remain absent.** The deck `20261110_1_Symmetric.pdf` continues through symmetric cryptography and the one-time pad (slides 56–93), but no material for public-key cryptography, signatures, key establishment, authentication, access control or protocols has been ingested.
- Which of the four Thursday slots is the "real" one? The sheet lists all four with "check rooms in Stud.IP" — the slot structure is unresolved.
- The lecture-0 slides name the exam date (05.04.2027) via the course organisation sheet; whether the written exam's duration and any sub-parts are specified anywhere is not stated.

## Connections

- [[machine-learning-for-cybersecurity]] — the ML-for-security half of the same department's teaching.
- [[introduction-to-deep-learning]] — the other course whose lecture 0 was ingested on the same day.
