---
title: "Search-Based Software Engineering"
tags: [course, semester-2, search-based-software-engineering]
professor: "Prof. Dr. Gordon Fraser"
semester: "WS 2026/27"
exam_date: "written or oral, depends on number of participants; no date stated in the ingested material"
credits: "not stated in the ingested material"
language: "English"
source_count: 8
status: active
last_updated: 2026-11-07
prerequisites: ["profound knowledge of Java", "software testing practice (JUnit 5, Mockito)", "version control with git", "basic algorithm and complexity theory (P, NP)"]
---

## One-line Summary

Treat software-engineering problems as optimisation problems: define a representation, a fitness
function and move operators, then let a metaheuristic search — and prove that it worked with
statistics rather than a single run.

## Course Information

- **Professor:** Prof. Dr. Gordon Fraser — Chair of Software Engineering II
- **Exercise organiser / lecturer of the organisational deck:** Patric Feldmeier — room IM 126,
  patric.feldmeier@uni-passau.de
- **Lecture:** **Tuesday 08:00–10:00**, (IM) HS 11
- **Exercises:** **Wednesday 08:00–10:00**, (IM) SR 07
- **Communication:** the Stud.IP forum, the exercise class, e-mail for personal matters
- **Registration (from the organisational deck):** window **12.10.2026 – 03.11.2026**, and it is
  **binding** — "there's no going back". The registration deadline for the exam is printed as the
  same date, 2026-11-03.
- **Replaces Energy Informatics 1** in this vault: the student dropped Energy Informatics 1 on
  2026-11-07 and registered Search-Based Software Engineering instead.

## Assessment

- **Four assignments**, each requiring you to implement a search-based solution to a
  software-engineering problem. **Java**, **individual work** ("no group work, assignments are
  single-person"), submitted through **Artemis**.
- **Pass condition:** "≥ 50 % points over all four assignments **&** passing of oral/written exam
  required for passing course". Both halves are required.
- **Exam:** "written or oral exam — depends on number of participants", "focused on assignments",
  and "passing exam is requirement for passing the course". **No exam date appears in the
  ingested material** and none is guessed here.
- **Testing is part of the grade:** "part of the grade for an assignment will be determined by
  testing (e.g. coverage, mutation score)", and "quality of submission: your responsibility (i.e.,
  write test cases!)".

### Assignment schedule (organisational deck)

| # | Topic | Algorithm | Released | Introduced | Due |
|---|-------|-----------|----------|------------|-----|
| A1 | Test case prioritisation | Simulated annealing & evolutionary algorithm | 2026-11-10 | 2026-11-11 | 2026-11-30 |
| A2 | Test suite minimisation | NSGA-II | 2026-12-01 | 2026-12-02 | 2026-12-21 |
| A3 | Neuroevolution | "Testing Games with Neatest" | 2026-12-22 | 2026-12-22 (in the lecture) | 2027-01-18 |
| A4 | Genetic invariant generation | Evolutionary search for invariants | 2027-01-19 | 2027-01-20 | 2027-02-15 |

The introduction deck gives a **different** tentative plan — "Assignment 1 release 10.11.,
Assignment 2 release 01.12., Assignment 3 release 15.12., Assignment 4 release 19.01." The
organisational deck is the later and more specific document, so its dates are recorded above and
the discrepancy is flagged rather than resolved.

### Submission mechanics (Artemis)

- Platform: **https://artemis.m.uni-passau.de**, log in with **ZIM credentials**, join the course
  "Search-Based Software Engineering WS27/26".
- **"HEAD of main branch at deadline: taken for our evaluation and grading."** Nothing is graded
  that is not on main at the deadline; "commit early and often" is the stated mitigation.
- Artemis "builds your submissions (like CI), runs your tests, runs our (functional) tests, reports
  you the results".
- Each assignment ships a **Maven project scaffold**, a task description on Artemis, and "an
  example that is not graded"; you implement the functionality **and unit tests**.

### Rules the deck states verbatim

- "Achieve sufficient number of points to pass course."
- "Hard coded solutions: no points at all."
- "No group work, assignments are single-person."
- "Characteristical parts of two or more solutions are identical ⇒ plagiarism. You are responsible
  for proving to us that you did not plagiarize. LLMs tend to create similar solutions → keep logs
  of LLMs if you are using them. In case of plagiarism: all involved students fail the course
  immediately."

**On LLM use, unlike three other courses this semester:** this course does **not** forbid
AI assistance — it makes you responsible for being able to show the work is yours, and it tells you
to keep logs if you use an LLM. That is a materially different rule from the MSR exercise sheets
("the tasks are not supposed to be solved by AI") and from the hardware-security seminar (no
automatic text generation, plagiarism graded 5,0). The practical consequence for this vault: the
assignments are graded individual work, so no solution is written here; the lecture material,
the algorithms and the tooling are ingested in full.

## Contents of the Lecture (the slide's own tentative schedule)

| Date | Topic |
|---|---|
| 13.10. | Introduction; search spaces and fitness landscapes |
| 20.10. | Local search algorithms |
| 27.10. | Local search algorithms |
| 03.11. | Evolutionary search |
| 10.11. | Evolutionary search |
| 17.11. | Multi-objective optimisation |
| 24.11. | Multi-objective optimisation |
| 01.12. | Search-based testing |
| 08.12. | Search-based testing |
| 15.12. | Neuroevolution |
| 22.12. | Neuroevolution |
| 12.01. | Genetic programming |
| 19.01. | Genetic programming |
| 26.01. | SBSE + LLMs |
| 02.02. | SBSE + LLMs |

Course material is delivered as **slides plus Jupyter notebooks / Python** ("1 2 3 … 15 slides,
code"). First exercise: 20.10.

## Lecture Index

Overview pages:

- [[search-based-software-engineering-lecture-0]] — organisation, grading, the four assignments,
  Artemis mechanics, the rules
- [[search-based-software-engineering-lecture-1]] — optimisation problems, metaheuristics, what SBSE
  is, search spaces and fitness landscapes
- [[search-based-software-engineering-lecture-2]] — hill climbing, tabu search, simulated annealing,
  and the statistics for evaluating search algorithms
- [[search-based-software-engineering-lecture-3]] — evolutionary algorithms: the biology deck, then
  evolution strategies and genetic algorithms in the lab

| # | Topic | Source | Status |
|---|-------|--------|--------|
| 0 | Organisation, assessment, assignments, Artemis, rules | `Ubung/Organisational.pdf` (17 slides) | ingested → [[search-based-software-engineering-lecture-0]] |
| 1 | Introduction: optimisation, metaheuristics, SBSE, fitness landscapes | `Vorlesung/1_Introduction.pdf` (88 slides) | ingested → [[search-based-software-engineering-lecture-1]] |
| 2 | Local search: hill climbing, tabu, annealing, evaluation | `Vorlesung/2_LocalSearch.pdf` (55 slides) | ingested → [[search-based-software-engineering-lecture-2]] |
| 2b | Local search, statistics half again | `Vorlesung/3_LocalSearch_Part2.pdf` (19 slides) | **duplicate** of slides 20+ of deck 2; no separate page |
| 2c | Local search lab | `Vorlesung/2_LocalSearch_Jupyter_Part1.pdf` (40 pages) | ingested → [[search-based-software-engineering-lecture-2]] |
| 2d | Local search lab, part 2 | `Vorlesung/3_LocalSearch_Jupyter_Part2.pdf` (47 pages) | ingested → [[search-based-software-engineering-lecture-2]] |
| 3 | Evolutionary algorithms: biology and history | `Vorlesung/4_EvolutionaryAlgorithms_Part1.pdf` (26 slides) | ingested → [[search-based-software-engineering-lecture-3]] |
| 3b | Evolutionary algorithms lab | `Vorlesung/4_EvolutionaryAlgorithms_Jupyter_Part1.pdf` (48 pages) | ingested → [[search-based-software-engineering-lecture-3]] |
| — | Link to the notebook repository | `Vorlesung/GitHub_repository_with_Jupyter_Notebook_sources.url` | a Stud.IP redirect to the GitHub repo, not a document |
| A1–A4 | Assignment sheets | — | **not in `raw/`** — A1 releases 2026-11-10 |

## Concept Pages

| Page | One-line idea |
|------|---------------|
| [[sbse-paradigm]] | Optimisation applied to SE problems (not search engines), and the domains it covers |
| [[metaheuristics]] | Approximation without guarantees; six properties; random search as the baseline |
| [[fitness-landscape]] | Search space + fitness + neighbourhood; the shape predicts the difficulty |
| [[hill-climbing]] | Best neighbour, monotone ascent, stops at whatever local optimum it reaches |
| [[tabu-search]] | Best non-tabu neighbour even if worse, with a short-term memory |
| [[simulated-annealing]] | Accept worse moves with p = min(1, e^(−ΔE/T)) and cool on a schedule |
| [[evolutionary-algorithm]] | Population, selection, recombination, mutation — the (μ/ρ ± λ) family |
| [[search-algorithm-evaluation]] | Random runs make distributions: test, size the effect, correct the family |

## Homework

No assignment sheet is in `raw/` yet — A1 (test case prioritisation, simulated annealing and an
evolutionary algorithm) releases 2026-11-10, introduces 2026-11-11 and is due 2026-11-30. When a
sheet arrives it goes to `study/homework/search-based-software-engineering/` under a name for its
sheet (`a1-test-case-prioritisation.md`), never bare `solution.md`.

Note the standing rule for this course specifically: assignments are graded, individual, and the
plagiarism clause turns on "characteristical parts of two or more solutions" being identical, with
LLM use allowed only if you can show your own work. So the vault's job here is the lecture layer —
representation, operators, fitness, the algorithms, the evaluation machinery — and the student's
implementation stays theirs.

## Connections

- [[mining-software-repositories]] — the sibling course: MSR measures software artifacts, SBSE
  optimises them; both insist on statistics over anecdotes (Herbold's and Fraser's methods
  lectures cover overlapping tests).
- [[machine-learning-for-cybersecurity]] — another course where a proxy metric stands in for the
  real objective, and where a single run of a stochastic method proves nothing.
- [[reverse-and-reengineering]] — shares the Herbold/Fraser chair's taste for tool-driven work
  (Artemis, Maven, JUnit), and its notion of program structure is what test-case prioritisation
  operates on.
- [[metaheuristics]], [[fitness-landscape]], [[search-algorithm-evaluation]] — the three pillars the
  whole course stands on.
- Semester 1 statistics pages — [[statistical-significance]], [[effect-sizes]],
  [[confidence-intervals]], [[null-and-alternative-hypothesis]]: the general machinery this course
  applies to search algorithms.

## Open Questions

- **Exam format, date and weight are not in the material.** "Written or oral — depends on number of
  participants" is all the deck says; credit points are not stated anywhere.
- **The exam registration deadline is printed as 2026-11-03**, the same day the course registration
  window closed, which is earlier than any exam could plausibly be and is not explained.
- **Assignment 3's release date conflicts** between the organisational deck (22.12) and the
  introduction deck (15.12), and its algorithm name ("Testing Games with Neatest" vs
  "Neuroevolution") is not reconciled either.
- **What "portfolio of assignment solutions" contributes to the grade** is undefined beyond the
  50 % threshold.
- **The notebooks reference a `sbse_support` module** (`seed_everything`, `Evaluations`) that is
  not in `raw/`; the repository link is a Stud.IP redirect, so the support code was not available
  when this material was ingested.
- **Deck 3 ("Part 2" of local search) is a strict subset of deck 2** — whether it was a separate
  session or a re-export is not stated in the files.
- **Lecture 4 onward (multi-objective optimisation, NSGA-II) is not in `raw/`** although A2 depends
  on NSGA-II, so assignment 2 currently has no supporting slide material in the vault.