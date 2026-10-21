---
title: "Courses — Semester 2"
tags: [meta, semester-2]
status: current
last_updated: 2026-10-20
---

# Courses — WS 2026/27

Registry of the courses in this semester, with what has actually been ingested into `raw/`.
Two courses were dropped after the 2026-10-20 ingest — see *Dropped courses* below.

| Course | Professor | Exam | Material in raw/ | Concepts | Lecture pages |
|--------|-----------|------|------------------|----------|---------------|
| [[advanced-it-security]] | Posegga | 05.04.2027 (written) | lecture 0 (Basics) + exercise intro | 7 | [[advanced-it-security-lecture-0]], [[advanced-it-security-exercise-0]] |
| Bitcoin and Cryptocurrencies Technologies | — | — | none | 0 | — |
| [[energy-informatics-1]] | de Meer | 17.02.2027 / 24.03.2027 | L0 motivation + organisation + tutorial 1 | 6 | [[energy-informatics-1-lecture-0]] |
| [[introduction-to-deep-learning]] | Lemmerich | TBD (written, 90 min) | L1 + exercise 1 + exercise 2 | 10 | [[introduction-to-deep-learning-lecture-1]], [[introduction-to-deep-learning-exercise-1]], [[introduction-to-deep-learning-exercise-2]], [[deep-learning-course-roadmap]] |
| [[machine-learning-for-cybersecurity]] | Reiser | portfolio | L1 + L2 + L3 + Lab 1 | 13 | [[machine-learning-for-cybersecurity-lecture-1]], [[machine-learning-for-cybersecurity-lecture-2]], [[machine-learning-for-cybersecurity-lecture-3]] |
| [[scaling-database-systems]] | Scherzinger | TBD | 4 organisation sheets (no lecture slides yet) | 3 | [[scaling-database-systems-exercise-0]] |
| [[virtual-machines-and-runtime-systems]] | Größlinger | 11.02.2027 / 01.04.2027 | s00, s01, s02 + sheet 1 | 9 | [[virtual-machines-and-runtime-systems-lecture-1]], [[virtual-machines-and-runtime-systems-lecture-2]], [[virtual-machines-and-runtime-systems-exercise-1]] |
| [[ai-engineering-lab]] | — | report-based | project repo + report | existing artifacts | — |

## Dropped courses

**Hardware-Oriented Security** (Katzenbeisser) and **Reverse- and Reengineering** (Hammer) were
dropped by the student on 2026-10-20. Their course pages, 24 concept pages, 4 lecture pages,
2 homework solutions and all raw lecture PDFs were removed from the vault. Nothing from either
course is in scope for exam prep.

## Standing gaps

- **Bitcoin and Cryptocurrencies Technologies** — folder exists in `raw/lectures/`, no files. No page created; nothing to synthesize.
- **Advanced IT Security** — lecture 0 (Basics) is ingested; lectures 1–6 have no slides in `raw/` yet.
- **Scaling Database Systems** — new course. Only organisational sheets (prerequisites, exercise
  scheduling, Docker server, Praktomat) are in `raw/`; `raw/lectures/Scaling Database Systems/Vorlesung/`
  exists but is empty, so **no lecture slides have been ingested** and the technical content of the
  course is not yet in the vault. The three concept pages cover project structure, tooling and the
  submission workflow — nothing else.
- **Machine Learning for Cybersecurity** — the three papers assigned for the student presentations are referenced by URL on L3 slide 36, but the PDFs themselves are not in `raw/`. Their abstracts were read and are summarised in `study/homework/machine-learning-for-cybersecurity/presentation-papers.md`.
- Exam dates marked TBD were not in the ingested material. They are not guessed.
