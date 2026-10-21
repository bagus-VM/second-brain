---
title: "Machine Learning for Cybersecurity — Lecture 1 Overview (Security and ML basics)"
tags: [topic, ml-security, semester-2, security-basics]
course: "Machine Learning for Cybersecurity"
source_count: 1
status: current
last_updated: 2026-10-19
prerequisites: []
---

## One-line Summary
Two foundations in one session: security as a cost/benefit discipline with its own vocabulary, and
machine learning as a task taxonomy the course then maps onto five areas of security work.

## Core Map

```
Lecture 1 — Organisation, Security basics, ML basics
│
├── Organisation
│   ├── Reiser; Tue/Thu slots; paper-driven after week 4
│   └── portfolio: paper presentation ~20%, project ~40%, presentation ~40%
│
├── Security basics
│   ├── "X is secure" is meaningless — relative, threat-specific
│   ├── assets / threats / vulnerabilities / safeguards / residual risk
│   │                                        -> [[security-terminology-and-risk-model]]
│   ├── policy / mechanism / assurance
│   ├── C-I-A (ITSEC), accountability, non-repudiation
│   │                                        -> [[cia-triad]]  (Semester 1 page)
│   └── attacker classes I/II/III (1991)     -> [[attacker-classification]]
│
└── ML basics
    ├── AI ⊃ ML ⊃ DL                         -> [[ml-learning-paradigms]]
    ├── tasks: regression, classification, clustering, association rules,
    │          dimensionality reduction, generative   -> [[ml-task-taxonomy]]
    ├── paradigms: supervised, unsupervised, semi-, reinforcement, active, ensemble
    └── where it is used in security          -> [[ml-for-security-domains]]
        └── network / endpoint / application / user behaviour / process behaviour
```

## Key Concepts at a Glance

| Page | Core idea |
|------|-----------|
| [[security-terminology-and-risk-model]] | Assets, threats, vulnerabilities, safeguards, residual risk; policy vs mechanism vs assurance; risk is always relative to an attacker |
| [[attacker-classification]] | Clever outsiders / knowledgeable insiders / funded organisations (Abraham et al., IBM Systems Journal 1991) |
| [[ml-learning-paradigms]] | AI vs ML vs DL, and the six learning paradigms with what each assumes about labels |
| [[ml-task-taxonomy]] | Six task families, their algorithms, and one cybersecurity example each |
| [[ml-for-security-domains]] | The five security areas and which ML task each uses — plus why "correlation ≠ causation" bites |

## Lecture Structure

1. **What ML + CS is** — CrowdStrike as the cautionary opener: an "AI-powered" sensor that crashed
   millions of machines and caused ~$10bn damage *without an attack*. Then frontier models writing
   spearphishing and agent-automated tool chains.
2. **Organisation** — instructor background, format, literature (papers, announced weekly), portfolio
   assessment, topic list, structure (traditional weeks 1–4, then presentations).
3. **Security basics** — what security is, elements of security, cost/benefit, the mobile-phone
   example, the terminology chain, protection goals, accountability and non-repudiation, attacker
   classes.
4. **ML basics** — the AI/ML/DL distinction, the six tasks, the learning paradigms, then the mapping
   from security area to ML task (network, endpoint, application, user, process behaviour).
5. **The closing slide** — automating simple tasks with AI does not replace understanding them.

## Exam-Relevant Points

1. **Define the terminology without mixing the terms**: a vulnerability is a hole, a threat is
   something that can use it, a safeguard reduces one of them, residual risk never reaches zero.
2. **The attacker classes and why they change the risk model** — the same asset, different risk.
3. **AI vs ML vs DL**, precisely: DL is a set of techniques for *implementing* ML; ML is an approach
   to AI that learns from experience.
4. **Six ML tasks with one security example each** — the lecture does this mapping explicitly, so it is
   exactly the kind of material an exam asks for.
5. **Which ML task applies to which security area** (e.g. clustering for forensics, regression to
   predict the next system call, classification for malware families).
6. **The critique**: correlation is not causation, outliers are not threats, false positives cost
   analyst time. Expect a question that tests whether you can say what ML *cannot* do here.

## Connections

- [[machine-learning-for-cybersecurity]] — course page (portfolio weights, topic list).
- [[machine-learning-for-cybersecurity-lecture-2]] — the first concrete algorithm (Naive Bayes) and
  the metric definitions that make "false positive" measurable.
- [[cia-triad]] — the Semester 1 page already covers C-I-A with the IoT extensions; this lecture's
  version adds the ITSEC wording and accountability/non-repudiation.
- [[risk-assessment-frameworks]] — the standards-based counterpart (NIST CSF, ENISA).

## Open Questions

- The attacker classification is from 1991. What is the equivalent for LLM-driven, agent-automated
  attackers the lecture opens with? The slide raises the tension but never resolves it.
- Which papers are assigned per week? Announced on Stud.IP, not in the slides.
