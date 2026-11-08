---
title: "Homework — WS 2026/27"
tags: [meta, homework, semester-2]
status: current
last_updated: 2026-11-05
---

# Homework

Solutions for every exercise sheet present in `raw/`. Each folder holds the written answer **and** the runnable artifact where one exists — nothing here is hand-waved where it could be executed instead. The one deliberate exception is the two Mining Software Repositories sheets, whose owner forbids AI assistance; those are described but deliberately not solved (see the note below the coverage audit).

| Course | Sheet | Deliverable | State |
|--------|-------|-------------|-------|
| Introduction to Deep Learning | Exercise 1 | `introduction-to-deep-learning/idl-exercise-01-solution.md` + `exercise-01-solutions.py` | written, script runs, output pasted from a real run, cross-checked against the official solution notebook |
| Introduction to Deep Learning | Exercise 2 — PyTorch (coding) | `introduction-to-deep-learning/exercise-02-solutions.py` | **run**: 9 tasks implemented, degree 1/2/3/9 compared, losses measured; output in `output-exercise-02.txt` |
| Introduction to Deep Learning | Exercise 2 — paper (MML 2.4, derivatives, probability) | `introduction-to-deep-learning/exercise-02-math.py` + `idl-exercise-02-solution.md` | **run**: every claim verified numerically; output in `output-exercise-02-math.txt` |
| Introduction to Deep Learning | Environment for the above | `introduction-to-deep-learning/requirements-exercise-02.txt` | pinned (torch 2.14.1+cpu, numpy 2.4.6); both scripts reproduce the recorded output byte for byte from a clean venv |
| Machine Learning for Cybersecurity | Lecture 2 spam exercise + reading assignment | `machine-learning-for-cybersecurity/spam-classifier/spam-classifier-solution.md` + `spam_classifier.py` | written, classifier trained and evaluated on the real LingSpam dataset |
| Machine Learning for Cybersecurity | Lab 1 — the professor's own notebook | `machine-learning-for-cybersecurity/lab-1-basics.md` | walkthrough of `Lab1-Basics-CC.ipynb` with its real outputs; three findings recorded |
| Machine Learning for Cybersecurity | Student paper presentation (20 min, Nov 3 or Oct 29) | `machine-learning-for-cybersecurity/presentation-papers.md` | all three assigned papers summarised from their abstracts; format and preparation notes |
| Dependable Distributed Systems | Exercise 1 (14 Oct 2026) | `dependable-distributed-systems/dds-exercise-01-solution.md` | written, all 6 tasks answered; availability arithmetic computed |
| Dependable Distributed Systems | Exercise 2 (21 Oct 2026) | `dependable-distributed-systems/dds-exercise-02-solution.md` + `logical-clocks.py` | **run**: Lamport and vector timestamps computed, all 175 linear extensions checked, both total orders verified |
| Dependable Distributed Systems | Exercise 3 (28 Oct 2026) | `dependable-distributed-systems/dds-exercise-03-solution.md` + `clock-sync.py` | **run**: CNV implemented from the lecture definition and simulated over 7 scenarios (including the n = 3m failure), the worst Byzantine lie brute-forced, four measurements reduced to one offset |
| Virtual Machines and Runtime Systems | Exercise Sheet 1 (due 22.10.2026) | `virtual-machines-and-runtime-systems/sheet-01/` | written, all three linking modes and the JIT built and executed |
| Reverse- and Reengineering | Homework 1 (20.10.2026) — CFG, PDG and slicing | `reverse-and-reengineering/hw01-solution.md` + `hw01-slices.py` | **run**: intra-procedural CFG and PDG built and the backward and forward slices computed by a script that models the program, not drawn by hand |
| Reverse- and Reengineering | Homework 2 (27.10.2026) — x86-64 assembly to C | `reverse-and-reengineering/hw02-solution.md` + `hw02-verify.py` | written and verified: both functions recovered to C, the assembly CFG reconstructed, and the recovered C checked against the sheet's own machine code |
| Reverse- and Reengineering | Homework 3 (03.11.2026) — x86 shifts and the `max` CFG | `reverse-and-reengineering/hw03-solution.md` + `hw03-verify.py` | **run**: `sar`/`shl` recovered, the `max` CFG rebuilt, and `>=` vs `>` settled by compiling both candidates — exact `-O0` round-trip |
| Reverse- and Reengineering | Homework 4 (10.11.2026) — x86-64 pointer swap, control-flow flattening | `reverse-and-reengineering/hw04-solution.md` + `hw04-verify.py` | **run**: `decode` recovered and checked four ways (simulation, exact `-O0` round-trip, the sheet's listing assembled and executed, the aliased call); the flattened `bar` compiled and run against the original — both 5050 |
| Mining Software Repositories | Exercise 1 (due 21.10.2026) — mining Git and Jira | `mining-software-repositories/exercise-01.md` | task sheet, tooling mechanics and method notes — **no AI-written solution by design**; the working scripts and the analysis are the student's own work |
| Mining Software Repositories | Exercise 2 (due 28.10.2026) — mining GitHub PRs and issues | `mining-software-repositories/exercise-02.md` | task sheet, API mechanics and method notes — **no AI-written solution by design**, for the same reason |
| Mining Software Repositories | Exercise 3 (due 04.11.2026) — the harmonized database | `mining-software-repositories/exercise-03.md` | task sheet, schema considerations and tooling only — **no AI-written solution by design**, for the same reason |
| Mining Software Repositories | Exercise 4 (due 11.11.2026) — expanding, linking, metrics | `mining-software-repositories/exercise-04.md` | task sheet, tooling mechanics (Seart search, RegEx) and method notes — **no AI-written solution by design**, for the same reason |
| Virtual Machines and Runtime Systems | Exercise Sheet 3 (due 05.11.2026) — exceptions, memory management | `virtual-machines-and-runtime-systems/sheet-03/` (`mymalloc-bump.c`, `mymalloc-freelist.c`, `test-mymalloc.c`, `sheet-03-solution.md`, recorded output) | **run**: both allocators built and preloaded with `LD_PRELOAD`; 5/5 checks each, block reuse and program-break behaviour recorded from real traces |
| Advanced IT Security | Exercise 2 (discussion 05.11.2026) — cryptography, the adversary, hash functions | `vault/topics/advanced-it-security-exercise-2.md` | written, all nine parts answered; the 32-bit digest count computed (2^32) including the birthday bound; **the official solution deck arrived 2026-11-07** and confirmed every answer, and its three extra tasks (h(x) = x mod 13 collision hunt, hash-or-MAC table, true/false table) are worked on the page |

## Coverage audit — every exercise file in `raw/`, and where it is answered

Audited 2026-10-22 and **not re-audited since** — sheets that arrived after that date (DDS exercise 3-4,
IDL exercise 3, RRE homework 3-4, VMRS sheets 2-3, AITS exercise 1-2, MSR exercises 3-4) are tracked
in the table above and in the semester log rather than in this audit. Every file under a `Ubung/`
folder (plus the exercise-like notebooks) is listed here, so a new sheet can be checked against this
table in one glance.

| Source file in `raw/` | Answered in | Status |
|----------------------|-------------|--------|
| `Introduction to Deep Learning/Ubung/15-10-2026/01-hw-intro-py-tasks.ipynb` | `introduction-to-deep-learning/idl-exercise-01-solution.md` | complete — every notebook task |
| `Introduction to Deep Learning/Ubung/15-10-2026/01-homework.pdf` | same file, "Setup" section | complete — the three setup tasks (uv, VS Code, kernel) |
| `Introduction to Deep Learning/Ubung/15-10-2026/01-hw-intro-py-solutions.ipynb` | — | the professor's own solutions; used as a **cross-check**, not an exercise |
| `Introduction to Deep Learning/Ubung/15-10-2026/01-slides.pdf` (+ `-slim`) | — | session slides, not exercises (`-slim` is a strict subset of the full deck) |
| `Introduction to Deep Learning/Ubung/15-10-2026/01-demo.ipynb` | `vault/concepts/linear-algebra-for-deep-learning.md` | demo, not an exercise — but its content was worth a concept page |
| `Introduction to Deep Learning/Ubung/15-10-2026/01-notebook-issue.ipynb` | `vault/concepts/jupyter-notebook-state.md` | demo, not an exercise — the notebook-state trap, worked out |
| `Machine Learning for Cybersecurity/Vorlesung/Lab1-Basics-CC.ipynb` | `machine-learning-for-cybersecurity/lab-1-basics.md` | complete — all 28 cells, real outputs |
| `Dependable Distributed Systems/Ubung/dds26-exercise01.pdf` | `dependable-distributed-systems/dds-exercise-01-solution.md` | complete — all 6 tasks; 1.3(c) availability computed |
| `Dependable Distributed Systems/Ubung/dds26-exercise02.pdf` | `dependable-distributed-systems/dds-exercise-02-solution.md` + `logical-clocks.py` | complete — 2.6(a) and 2.6(b) timestamps computed and verified over all 175 linear extensions |
| `Dependable Distributed Systems/Ubung/dds26-exercise01-sol.pdf` | `dependable-distributed-systems/dds-exercise-01-solution.md` | the official solutions; used as a **cross-check** — one arithmetic convention and one framing difference recorded on the course page |
| `Dependable Distributed Systems/Ubung/dds26-exercise02-sol.pdf` | `dependable-distributed-systems/dds-exercise-02-solution.md` | the official solutions; used as a **cross-check** — 2.1's split verdict and 2.2(a)'s asterisk recorded on the course page |
| `Dependable Distributed Systems/Ubung/dds26-exercise03.pdf` | `dependable-distributed-systems/dds-exercise-03-solution.md` + `clock-sync.py` | complete — all four tasks; 3.2 answered from an independent CNV implementation because `exercise2-cnv.py` is **not in `raw/`** |
| `Dependable Distributed Systems/Vorlesung/dds2026w-03-ntp.pdf` | `vault/topics/dependable-distributed-systems-lecture-3.md` | lecture slides, not exercises — 6 concept pages produced |
| `Introduction to Deep Learning/Ubung/22-10-2026/02-homework.pdf` | `introduction-to-deep-learning/idl-exercise-02-solution.md` + `exercise-02-math.py` | complete — MML 2.4 (a–e), derivatives (a–e), probability (a–d), every claim verified numerically |
| `Introduction to Deep Learning/Ubung/22-10-2026/02-hw-intro-pytorch-tasks.ipynb` | `introduction-to-deep-learning/exercise-02-solutions.py` | complete — 9 tasks, model trained, degrees 1/2/3/9 compared by measured train and validation loss |
| `Introduction to Deep Learning/Ubung/22-10-2026/02-slides.pdf` | `vault/topics/introduction-to-deep-learning-exercise-2.md` | session slides, not exercises |
| `Introduction to Deep Learning/Ubung/22-10-2026/02-demo.ipynb` | `vault/concepts/pytorch-tensors-and-autograd.md`, `vault/concepts/neural-network-training-loop.md` | demo, not an exercise — but it is where the autograd and training-loop content lives |
| `Introduction to Deep Learning/Vorlesung/01_introduction_to_dl.pdf` | `vault/topics/introduction-to-deep-learning-lecture-1.md` | lecture slides, not exercises |
| `Introduction to Deep Learning/Vorlesung/02_foundations_of_ml.pdf` | `vault/topics/introduction-to-deep-learning-lecture-2.md` | lecture slides, not exercises — 12 concept pages produced |
| `Introduction to Deep Learning/idl-lecture2-numbers.py` (this vault's own) | `vault/concepts/*` for lecture 2 | not a sheet — the computations behind the 12 lecture-2 concept pages; output in `output-idl-lecture2-numbers.txt` |
| `Virtual Machine and Runtime System/Ubung/14-10-2026/01.pdf` (+ `addrs.c`, `eval.c`) | `virtual-machines-and-runtime-systems/sheet-01/` | complete — both problems, built and executed |
| `Advanced IT Security/Ubung/Advanced_IT-Security__Introduction.pdf` | `vault/topics/advanced-it-security-exercise-0.md` | no exercises in it — 5 slides of course logistics only |
| `Machine Learning for Cybersecurity/Ubung/` | — | **empty folder** — no sheet published yet |
| `Reverse and Re-Engineering/Ubung/hw01.pdf` | `reverse-and-reengineering/hw01-solution.md` | complete — CFG, PDG, backward and forward slices; all three computed by script |
| `Reverse and Re-Engineering/Ubung/hw02.pdf` | `reverse-and-reengineering/hw02-solution.md` | complete — both functions recovered to C, the assembly CFG reconstructed, the computed function identified |
| `Mining Software Repositories/Ubung/exercise_01.pdf` | `mining-software-repositories/exercise-01.md` | task sheet and method notes only — **no AI-written solution by design**; the working scripts and the analysis are the student's own work |
| `Mining Software Repositories/Ubung/exercise_02.pdf` | `mining-software-repositories/exercise-02.md` | task sheet and method notes only — **no AI-written solution by design**, for the same reason |
| `Advanced IT Security/Ubung/Exercise_2_with_solutions.pdf` | `vault/topics/advanced-it-security-exercise-2.md` | the official solutions; used as a **cross-check** — every answer confirmed, plus three tasks the sheet PDF did not print |
| `Advanced IT Security/Vorlesung/20261105_1_Symmetric.pdf` | `vault/topics/advanced-it-security-lecture-2.md` | lecture slides (slides 18–55 of the same deck), not exercises — 4 concept pages produced |
| `Introduction to Deep Learning/Vorlesung/03_single_layer_nns.pdf` | `vault/topics/introduction-to-deep-learning-lecture-3.md` | lecture slides, not exercises — 5 concept pages produced |
| `Introduction to Deep Learning/Ubung/03-eval-metrics-gradient-descent/03-PnP-01.jpg`, `03-PnP-02.jpg` | — | the student's **own handwritten** exercise-3 working (pen-and-paper, graph paper), not course material; no solution written from them |
| `Search-Based Software Engineering/Ubung/Organisational.pdf` | `vault/topics/search-based-software-engineering-lecture-0.md` | no exercises in it — organisation, assignments, Artemis, rules |
| `Search-Based Software Engineering/Vorlesung/*.pdf` (5 decks + 3 lab notebooks) | `vault/topics/search-based-software-engineering-lecture-1.md` … `-3` | lecture material, not exercises — 8 concept pages produced; no assignment sheet has been released yet |
| `Bitcoin and Cryptocurrencies Technologies/` | — | **no material at all** |

**The honest summary:** every exercise sheet that exists in `raw/` is now accounted for. Three gaps
remain, and all three are gaps in the *source*, not in the work:

1. **Advanced IT Security** — resolved. The exercise course started 29.10.2026; sheets 1 and 2 are
   answered and both now have their official solution decks folded in (sheet 2's arrived 2026-11-07,
   with three extra tasks). Lectures 0, 0b, 1 and 2 are ingested. What remains absent from `raw/` is
   still the lecture material itself: no cipher is taught, so symmetric cryptography (agenda item 3),
   public-key cryptography, signatures and key establishment have no slides.
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

- **Search-Based Software Engineering** — no assignment sheet in `raw/`; A1 (test case prioritisation)
  releases 2026-11-10 and is due 2026-11-30. The four assignments are graded, individual Java work
  submitted through Artemis, and the plagiarism clause turns on identical characteristic parts — LLM
  use is allowed only if the student can show the work is theirs, so nothing is solved here by design.
- **Bitcoin and Cryptocurrencies Technologies** — no material in `raw/`.

## How these were produced

Two rules, both worth keeping:

1. **If it can be run, it was run.** The spam classifier was trained on the actual dataset, the C programs were compiled and executed, and the Python solutions script's output is pasted from a real invocation (`output.txt` sits next to it). The Hardware-Oriented Security numbers — the middle-square orbit of 407 states and the LCG cycles — were computed by running the generators, not read off a slide. *(That course was dropped on 2026-10-20 and its solution was removed; the rule stands for the remaining courses.)* The same rule produced the Reverse- and Reengineering homework: the CFG, the PDG and the slices were computed by a script, and the recovered C was checked against the sheet's own machine code.
2. **Where the source is ambiguous or wrong, it says so.** Examples: the Deep Learning sheet says "compute 256²" and the official solution notebook settles it; the Kontsewaya paper does not use a ROC curve although the lecture's reading question asks about one; the professor's own lab notebook prints different metrics from the slides, and the reason is not stated in either source. Each of those is flagged in place instead of being quietly patched.
3. **Where the source forbids assistance, assistance stops.** The two MSR exercise sheets are the case in point: they are described and their tooling explained, and nothing more.
