---
title: "Search-Based Software Engineering — Lecture 0 Overview (Organisation)"
tags: [topic, search-based-software-engineering, semester-2, organisation]
course: "Search-Based Software Engineering"
source_count: 1
status: current
last_updated: 2026-11-07
prerequisites: []
---

## One-line Summary

The organisational deck: Fraser lectures, Feldmeier runs the exercises, four individually-written
Java assignments on Artemis plus a written-or-oral exam are the assessment, registration closed on
2026-11-03 and is binding, and the plagiarism rule explicitly names LLM use.

## Core Map

```
Organisation (17 slides)
│
├── People and times
│   ├── Lecture  — Prof. Dr. Gordon Fraser, Tue 08:00–10:00, IM HS 11
│   ├── Exercises — Patric Feldmeier, Wed 08:00–10:00, IM SR 07, room IM 126
│   └── Contact   — patric.feldmeier@uni-passau.de, Stud.IP forum, exercise class
│
├── Assessment
│   ├── Four assignments (implement search-based algorithms)
│   ├── Portfolio of assignment solutions + exam
│   ├── Written or oral exam — depends on number of participants
│   ├── Passing the exam is required for passing the course
│   └── ≥ 50 % of the points over all four assignments AND passing the exam
│
├── The four assignments
│   ├── A1 Test Case Prioritisation  — Simulated Annealing & Evolutionary Algorithm
│   ├── A2 Test Suite Minimisation   — NSGA-II
│   ├── A3 Neuroevolution            — "Testing Games with Neatest"
│   └── A4 Genetic Invariant Generation — evolutionary search for invariants
│
├── Mechanics
│   ├── Artemis — https://artemis.m.uni-passau.de, ZIM credentials
│   ├── HEAD of main branch at the deadline is what is graded
│   ├── Maven scaffold + task description on Artemis
│   ├── Implement functionality and unit tests; CI runs both
│   └── Java, JUnit 5, Mockito, git
│
└── Rules
    ├── Registration 12.10.2026 – 03.11.2026, binding
    ├── Hard-coded solutions score no points
    ├── No group work — single-person assignments
    ├── Identical characteristic parts ⇒ plagiarism, all involved fail
    └── LLMs tend to produce similar solutions → keep logs if you use them
```

## Key Concepts at a Glance

| Page | Core idea |
|------|-----------|
| [[search-based-software-engineering]] | The course page: people, dates, assessment, lecture index |
| [[sbse-paradigm]] | What the course is about — optimisation applied to software-engineering problems |
| [[metaheuristics]] | The algorithm class the assignments implement |
| [[simulated-annealing]] / [[evolutionary-algorithm]] | A1's two algorithms |
| [[search-algorithm-evaluation]] | How assignment quality and algorithm comparisons are judged |

## Lecture Structure

1. **Title and contact** — Patric Feldmeier, room IM 126, university e-mail.
2. **Timetable** — lecture Tuesday 08:00–10:00 in IM HS 11 with Prof. Dr. Gordon Fraser;
   exercises Wednesday 08:00–10:00 in IM SR 07 with Patric Feldmeier.
3. **Grading** — "Four assignments requiring you to implement search-based algorithms"; "grade is
   based on portfolio of assignment solutions and exam"; "written or oral exam — depends on number
   of participants"; "passing exam is requirement for passing the course".
4. **Course registration** — "Registration window: from now on until 2026–11–03"; "registration is
   binding (there's no going back)"; "≥ 50 % points over all four assignments & passing of
   oral/written exam required for passing course".
5. **Testing** — "'Why Testing is Important' … quality of submission: your responsibility (i.e.,
   write test cases!); part of the grade for an assignment will be determined by testing (e.g.
   coverage, mutation score)."
6. **The assignments**, one slide each, with release / introduction / due dates.
7. **Artemis** — the submission platform, its CI behaviour, and the rule that the HEAD of main at
   the deadline is what is evaluated.
8. **How an assignment looks** — Maven scaffold, task description on Artemis, implement
   functionality and unit tests, push and let Artemis compile and test, plus an ungraded example.
9. **Necessary skills** — "profound knowledge of Java", "testing software (JUnit 5, Mockito, etc.)",
   "version control (git)".
10. **Rules** — points, hard-coded solutions, exam registration, no group work, plagiarism, LLM logs.
11. **Questions** — Stud.IP forum, the exercise class, e-mail for personal matters.

## Exam-Relevant Points

1. **The pass condition is a conjunction, and both halves bite.** "≥ 50 % points over all four
   assignments & passing of oral/written exam required for passing course" — assignment points
   alone do not pass the course, and the exam alone does not either.
2. **The exam format is undecided at the start**: "written or oral exam — depends on number of
   participants". The exam is described as "focused on assignments".
3. **Hard-coded solutions score zero** — the point of the assignments is a search, not a lookup
   table of expected answers.
4. **The plagiarism rule names large language models explicitly**, which is unusual and worth
   knowing: "characteristical parts of two or more solutions are identical ⇒ plagiarism"; "you are
   responsible for proving to us that you did not plagiarize"; "LLMs tend to create similar
   solutions → keep logs of LLMs if you are using them"; "in case of plagiarism: all involved
   students fail the course immediately". Unlike the two MSR sheets and the hardware-security
   seminar, this course does **not** forbid LLM use — it requires that you can prove the work is
   yours.
5. **Only the HEAD of the main branch at the deadline counts.** Nothing submitted by e-mail or
   after the deadline is considered, and "commit early and often" is the mitigation.
6. **Registration was binding and closed on 2026-11-03** — after that date there is no route into
   the course through this deck's process.

## Connections

- [[search-based-software-engineering]] — the course page this deck defines.
- [[search-based-software-engineering-lecture-1]] — the first content lecture.
- [[simulated-annealing]], [[evolutionary-algorithm]], [[search-algorithm-evaluation]] — the
  material behind A1's "Simulated Annealing & Evolutionary Algorithm".
- [[mining-software-repositories]] — the other Herbold/Fraser-adjacent course in the semester, with
  a very different assessment rule (its sheets forbid AI assistance outright).

## Open Questions

- **The assignment dates disagree between this deck and the introduction deck.** Organisational
  slide 10 gives A3 release 2026-12-22 and introduction 2026-12-22; the introduction deck's
  tentative plan gives "Assignment 3 release 15.12". Which is current is not stated.
- **A3's algorithm is named twice, differently**: the assignment slide says "Testing Games with
  Neatest", the introduction deck says "Neuroevolution" for the 15.12/22.12 lectures. Whether
  "Neatest" is a tool, a typo or a project name is not explained.
- **No credit points (ECTS) appear anywhere in the deck.**
- **What "portfolio of assignment solutions" means as a grade component is not defined** — whether
  it is the 50 % threshold, a weighted mark, or both.
- **The exam dates are not given**, and the registration deadline for the exam (2026-11-03, the same
  date as course registration) is earlier than any exam date mentioned, which is unusual and
  unexplained.
- **Whether the ungraded example assignment is available before A1's release is not stated.**