---
title: "Machine Learning for Cybersecurity"
tags: [course, semester-2, ml-security]
professor: "Hans P. Reiser"
semester: "WS 2026/27"
exam_date: "portfolio"
credits: "TBD"
language: "English"
source_count: 3
status: active
last_updated: 2026-10-20
prerequisites: []
---

## One-line Summary
A paper-driven seminar-lecture on where machine learning actually helps in security — and where it quietly fails: detection, malware, adversarial ML, and attacks on LLMs.

## Course Information

- **Instructor:** Hans P. Reiser (hr@sec.uni-passau.de), Full Professor at Passau since 7/2026, part-time at Reykjavik University; research on intrusion detection, malware analysis, digital forensics, Byzantine fault tolerance
- **Format:** Tuesday and Thursday slots used flexibly for lectures, assignment discussions, and student presentations
- **Platform:** Stud.IP — news, slides, exercises, forum
- **Literature:** research papers, announced per week. Book recommendations: Chio & Freeman, *Machine Learning & Security* (O'Reilly 2018); Chebbi, *Mastering Machine Learning for Penetration Testing* (Packt 2018)

## Assessment (portfolio — all parts required, one final grade)

| Component | Weight |
|-----------|--------|
| Paper presentation | ~20% |
| Final project | ~40% |
| Presentation and discussion of final project | ~40% |

## Structure

- **Weeks 1–4:** traditional lectures with introductory material and simple exercises
- **After that:** an introduction lecture per topic, then student paper presentations + discussion, in-class help sessions, and presentation of programming-assignment results

## Topic List

1. Spam detection (A1) → [[naive-bayes-text-classification]]
2. Network intrusion detection (A2, presentations)
3. Malware analysis and classification (A3, presentations)
4. Cyber threat intelligence (presentations)
5. Adversarial machine learning (A4)
6. ML-based attacks and AI agents in cybersecurity (presentations)
7. Attacks on classical classifiers: evasion, poisoning (presentations)
8. Attacks on LLMs/agents: prompt injection, jailbreaks, tool abuse, RAG/data poisoning (presentations)
9. AI in digital forensics (presentations)
10. Privacy and ML

## Lecture Index

Overview pages:
- [[machine-learning-for-cybersecurity-lecture-1]] — Organisation, security basics, ML basics
- [[machine-learning-for-cybersecurity-lecture-2]] — Classification, Naive Bayes, spam exercise
- [[machine-learning-for-cybersecurity-lecture-3]] — Metrics & ROC, KNN, linear/logistic regression, ROC with KNN

| # | Topic | Source | Status |
|---|-------|--------|--------|
| 1 | Organisation, security basics, ML basics | `01_Org_Introduction.pdf` | ingested → 5 pages |
| 2 | Simple classification: Python/ML basics, Naïve Bayes, spam | `02_Spam.pdf` | ingested → 3 pages |
| 3 | More ML basics: metrics & ROC, KNN, linear & logistic regression | `03_ML_Intro.pdf` | ingested → 5 pages |

## Assigned Papers — Student Presentations (from L3)

The network-intrusion-detection block: **select one** of the three papers and present its key insights in
**20 minutes**, on **Nov 3** (or **Oct 29**).

| Paper | Venue | Link |
|--------|-------|------|
| Apruzzese, Laskov, Schneider — *SoK: Pragmatic Assessment of Machine Learning for Network Intrusion Detection* | IEEE EuroS&P 2023 | https://arxiv.org/pdf/2305.00550 |
| Fu, Li, Xu — *Detecting Unknown Encrypted Malicious Traffic in Real Time via Flow Interaction Graph Analysis* (HyperVision) | NDSS 2023 | https://www.ndss-symposium.org/wp-content/uploads/2023/02/ndss2023_s80_paper.pdf |
| Jacobs, Beltiukov, Willinger et al. — *AI/ML for Network Security: The Emperor has no Clothes* | ACM CCS 2022 | https://sites.cs.ucsb.edu/~arpitgupta/pdfs/trustee.pdf |

Details: [[machine-learning-for-cybersecurity-lecture-3]].

## The Course's Own Warning

The lecture opens with CrowdStrike: a security sensor "delivering AI and machine learning" that crashed millions of computers and caused ~$10 bn damage — **without an attack**. Then frontier models writing spearphishing and agent-automated tool chains. The point is not that ML is useless; it is that ML in security fails loudly and at scale. The slide that matters: *automating simple tasks with AI does not replace understanding them*.

## Open Questions

- Which papers are assigned beyond the L3 network-intrusion-detection set? Announced weekly, not in `raw/`.
- Final project scope and deadlines are not in the ingested slides.
- The L3 multi-class confusion matrix names its five classes (normal, Probe, DoS, U2R, R2L) but not the
  dataset it comes from, so no dataset can be attributed to it.
- The "Dynamic Model Update" column of the L3 comparison table marks logistic regression as
  "Complex (Online Learning)", but no online variant is ever introduced in the lecture.
- The rule of thumb for choosing K on the L3 KNN slide is garbled and cannot be recovered as stated.
- Which of the three assigned papers each student presents, and how the presentations are distributed
  across the two dates (Nov 3 / Oct 29), is not stated.
