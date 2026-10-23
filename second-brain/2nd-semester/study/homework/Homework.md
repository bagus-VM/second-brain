---
title: "Homework — WS 2026/27"
tags: [meta, homework, semester-2]
status: current
last_updated: 2026-10-22
---

# Homework

Solutions for every exercise sheet present in `raw/`. Each folder holds the written answer **and** the runnable artifact where one exists — nothing here is hand-waved where it could be executed instead. The one deliberate exception is the two Mining Software Repositories sheets, whose owner forbids AI assistance; those are described but deliberately not solved (see the note below the coverage audit).

| Course | Sheet | Deliverable | State |
|--------|-------|-------------|-------|
| Energy Informatics I | Tutorial 1 (disc. 20/22 Oct) | `energy-informatics-1/tutorial-01.md` | written, all 3 tasks |
| Introduction to Deep Learning | Exercise 1 | `introduction-to-deep-learning/exercise-01-solution.md` + `exercise-01-solutions.py` | written, script runs, output pasted from a real run, cross-checked against the official solution notebook |
| Introduction to Deep Learning | Exercise 2 — PyTorch (coding) | `introduction-to-deep-learning/exercise-02-solutions.py` | **run**: 9 tasks implemented, degree 1/2/3/9 compared, losses measured; output in `output-exercise-02.txt` |
| Introduction to Deep Learning | Exercise 2 — paper (MML 2.4, derivatives, probability) | `introduction-to-deep-learning/exercise-02-math.py` + `exercise-02-solution.md` | **run**: every claim verified numerically; output in `output-exercise-02-math.txt` |
| Introduction to Deep Learning | Environment for the above | `introduction-to-deep-learning/requirements-exercise-02.txt` | pinned (torch 2.14.1+cpu, numpy 2.4.6); both scripts reproduce the recorded output byte for byte from a clean venv |
| Machine Learning for Cybersecurity | Lecture 2 spam exercise + reading assignment | `machine-learning-for-cybersecurity/spam-classifier/spam-classifier-solution.md` + `spam_classifier.py` | written, classifier trained and evaluated on the real LingSpam dataset |
| Machine Learning for Cybersecurity | Lab 1 — the professor's own notebook | `machine-learning-for-cybersecurity/lab-1-basics.md` | walkthrough of `Lab1-Basics-CC.ipynb` with its real outputs; three findings recorded |
| Machine Learning for Cybersecurity | Student paper presentation (20 min, Nov 3 or Oct 29) | `machine-learning-for-cybersecurity/presentation-papers.md` | all three assigned papers summarised from their abstracts; format and preparation notes |
| Dependable Distributed Systems | Exercise 1 (14 Oct 2026) | `dependable-distributed-systems/exercise-01-solution.md` | written, all 6 tasks answered; availability arithmetic computed |
| Dependable Distributed Systems | Exercise 2 (21 Oct 2026) | `dependable-distributed-systems/exercise-02-solution.md` + `logical-clocks.py` | **run**: Lamport and vector timestamps computed, all 175 linear extensions checked, both total orders verified |
| Virtual Machines and Runtime Systems | Exercise Sheet 1 (due 22.10.2026) | `virtual-machines-and-runtime-systems/sheet-01/` | written, all three linking modes and the JIT built and executed |
| Reverse- and Reengineering | Homework 1 (20.10.2026) — CFG, PDG and slicing | `reverse-and-reengineering/hw01-solution.md` + `hw01-slices.py` | **run**: intra-procedural CFG and PDG built and the backward and forward slices computed by a script that models the program, not drawn by hand |
| Reverse- and Reengineering | Homework 2 (27.10.2026) — x86-64 assembly to C | `reverse-and-reengineering/hw02-solution.md` + `hw02-verify.py` | written and verified: both functions recovered to C, the assembly CFG reconstructed, and the recovered C checked against the sheet's own machine code |
| Mining Software Repositories | Exercise 1 (due 21.10.2026) — mining Git and Jira | `mining-software-repositories/exercise-01.md` | task sheet, tooling mechanics and method notes — **no AI-written solution by design**; the working scripts and the analysis are the student's own work |
| Mining Software Repositories | Exercise 2 (due 28.10.2026) — mining GitHub PRs and issues | `mining-software-repositories/exercise-02.md` | task sheet, API mechanics and method notes — **no AI-written solution by design**, for the same reason |

## Coverage audit — every exercise file in `raw/`, and where it is answered

Audited 2026-10-22. Every file under a `Ubung/` folder (plus the exercise-like notebooks) is listed
here, so a new sheet can be checked against this table in one glance.

| Source file in `raw/` | Answered in | Status |
|----------------------|-------------|--------|
| `Energy Informatics 1/Ubung/Tutorial_1.pdf` | `energy-informatics-1/tutorial-01.md` | complete — 3 tasks, all sub-questions |
| `Introduction to Deep Learning/Ubung/15-10-2026/01-hw-intro-py-tasks.ipynb` | `introduction-to-deep-learning/exercise-01-solution.md` | complete — every notebook task |
| `Introduction to Deep Learning/Ubung/15-10-2026/01-homework.pdf` | same file, "Setup" section | complete — the three setup tasks (uv, VS Code, kernel) |
| `Introduction to Deep Learning/Ubung/15-10-2026/01-hw-intro-py-solutions.ipynb` | — | the professor's own solutions; used as a **cross-check**, not an exercise |
| `Introduction to Deep Learning/Ubung/15-10-2026/01-slides.pdf` (+ `-slim`) | — | session slides, not exercises (`-slim` is a strict subset of the full deck) |
| `Introduction to Deep Learning/Ubung/15-10-2026/01-demo.ipynb` | `vault/concepts/linear-algebra-for-deep-learning.md` | demo, not an exercise — but its content was worth a concept page |
| `Introduction to Deep Learning/Ubung/15-10-2026/01-notebook-issue.ipynb` | `vault/concepts/jupyter-notebook-state.md` | demo, not an exercise — the notebook-state trap, worked out |
| `Machine Learning for Cybersecurity/Vorlesung/Lab1-Basics-CC.ipynb` | `machine-learning-for-cybersecurity/lab-1-basics.md` | complete — all 28 cells, real outputs |
| `Dependable Distributed Systems/Ubung/dds26-exercise01.pdf` | `dependable-distributed-systems/exercise-01-solution.md` | complete — all 6 tasks; 1.3(c) availability computed |
| `Dependable Distributed Systems/Ubung/dds26-exercise02.pdf` | `dependable-distributed-systems/exercise-02-solution.md` + `logical-clocks.py` | complete — 2.6(a) and 2.6(b) timestamps computed and verified over all 175 linear extensions |
| `Introduction to Deep Learning/Ubung/22-10-2026/02-homework.pdf` | `introduction-to-deep-learning/exercise-02-solution.md` + `exercise-02-math.py` | complete — MML 2.4 (a–e), derivatives (a–e), probability (a–d), every claim verified numerically |
| `Introduction to Deep Learning/Ubung/22-10-2026/02-hw-intro-pytorch-tasks.ipynb` | `introduction-to-deep-learning/exercise-02-solutions.py` | complete — 9 tasks, model trained, degrees 1/2/3/9 compared by measured train and validation loss |
| `Introduction to Deep Learning/Ubung/22-10-2026/02-slides.pdf` | `vault/topics/introduction-to-deep-learning-exercise-2.md` | session slides, not exercises |
| `Introduction to Deep Learning/Ubung/22-10-2026/02-demo.ipynb` | `vault/concepts/pytorch-tensors-and-autograd.md`, `vault/concepts/neural-network-training-loop.md` | demo, not an exercise — but it is where the autograd and training-loop content lives |
| `Introduction to Deep Learning/Vorlesung/01_introduction_to_dl.pdf` | `vault/topics/introduction-to-deep-learning-lecture-1.md` | lecture slides, not exercises |
| `Virtual Machine and Runtime System/Ubung/14-10-2026/01.pdf` (+ `addrs.c`, `eval.c`) | `virtual-machines-and-runtime-systems/sheet-01/` | complete — both problems, built and executed |
| `Advanced IT Security/Ubung/Advanced_IT-Security__Introduction.pdf` | `vault/topics/advanced-it-security-exercise-0.md` | no exercises in it — 5 slides of course logistics only |
| `Energy Informatics 1/Ubung/EnInf_I_Organisational.pdf` | `vault/topics/energy-informatics-1-lecture-0.md` | no exercises in it — organisational information |
| `Machine Learning for Cybersecurity/Ubung/` | — | **empty folder** — no sheet published yet |
| `Reverse and Re-Engineering/Ubung/hw01.pdf` | `reverse-and-reengineering/hw01-solution.md` | complete — CFG, PDG, backward and forward slices; all three computed by script |
| `Reverse and Re-Engineering/Ubung/hw02.pdf` | `reverse-and-reengineering/hw02-solution.md` | complete — both functions recovered to C, the assembly CFG reconstructed, the computed function identified |
| `Mining Software Repositories/Ubung/exercise_01.pdf` | `mining-software-repositories/exercise-01.md` | task sheet and method notes only — **no AI-written solution by design**; the working scripts and the analysis are the student's own work |
| `Mining Software Repositories/Ubung/exercise_02.pdf` | `mining-software-repositories/exercise-02.md` | task sheet and method notes only — **no AI-written solution by design**, for the same reason |
| `Bitcoin and Cryptocurrencies Technologies/` | — | **no material at all** |

**The honest summary:** every exercise sheet that exists in `raw/` is now accounted for. Three gaps
remain, and all three are gaps in the *source*, not in the work:

1. **Advanced IT Security** — the exercise course starts **29.10.2026**; only the organisation
   slides are present. The first real sheet does not exist yet. Lecture 0 (Basics) has since
   arrived and is ingested.
2. **Machine Learning for Cybersecurity** — an `Ubung/` folder exists but is empty; the course uses
   the `Vorlesung/` slot for the lab instead (Lab 1, answered above).
3. **Bitcoin and Cryptocurrencies Technologies** — no files at all, not even a `Vorlesung/` document.

**One deliberate exception to "every sheet is answered".** The two Mining Software Repositories
exercise sheets carry an explicit instruction from their owner, addressed to large language
models, that they must not be assisted — *"the tasks are not supposed to be solved by AI."*
They are therefore **not** solved here: what the vault holds is the task sheet, the tooling
mechanics (REST endpoints, pagination, rate limits, PyDriller's API) and the method notes, so
the student can set the work up and reason about it. The working scripts and the resulting
analysis are the student's own work. This is a deliberate state, not an unfinished one, and it
is recorded on both sheets so a future session does not "helpfully" fill the gap.

## Courses with nothing to solve yet

- **Advanced IT Security** — the exercise course starts 29.10.2026; only the organisation sheet exists.
- **Bitcoin and Cryptocurrencies Technologies** — no material in `raw/`.

## How these were produced

Two rules, both worth keeping:

1. **If it can be run, it was run.** The spam classifier was trained on the actual dataset, the C programs were compiled and executed, and the Python solutions script's output is pasted from a real invocation (`output.txt` sits next to it). The Hardware-Oriented Security numbers — the middle-square orbit of 407 states and the LCG cycles — were computed by running the generators, not read off a slide. *(That course was dropped on 2026-10-20 and its solution was removed; the rule stands for the remaining courses.)* The same rule produced the Reverse- and Reengineering homework: the CFG, the PDG and the slices were computed by a script, and the recovered C was checked against the sheet's own machine code.
2. **Where the source is ambiguous or wrong, it says so.** Examples: the Deep Learning sheet says "compute 256²" and the official solution notebook settles it; the Kontsewaya paper does not use a ROC curve although the lecture's reading question asks about one; the professor's own lab notebook prints different metrics from the slides, and the reason is not stated in either source. Each of those is flagged in place instead of being quietly patched.
3. **Where the source forbids assistance, assistance stops.** The two MSR exercise sheets are the case in point: they are described and their tooling explained, and nothing more.
