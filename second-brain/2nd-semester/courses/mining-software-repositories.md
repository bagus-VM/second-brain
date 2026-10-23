---
title: "Mining Software Repositories"
tags: [course, semester-2, mining-software-repositories]
professor: "Prof. Dr. Steffen Herbold"
semester: "WS 2026/27"
exam_date: "preliminary: Wed 10 Feb 2027 14:00–16:00 and Mon 22 Mar 2027 10:00–12:00"
credits: "not stated in the ingested material"
language: "English"
source_count: 11
status: active
last_updated: 2026-10-22
prerequisites: ["machine learning and data-science foundations (data cleaning, feature engineering, statistics, ML)", "software engineering incl. processes and quality assurance", "good programming knowledge (Python, pandas, matplotlib, scikit-learn)", "knowledge about working with and setting up databases"]
---

## One-line Summary
Repositories are the largest untapped corpus of software-engineering evidence; this course turns
commit, issue, review and CI data into claims you can defend — and teaches the statistics and
validity machinery that keeps those claims honest.

## Course Information

- **Instructor:** Prof. Dr. Steffen Herbold — steffen.herbold@uni-passau.de
- **Exercise author/organiser:** Lukas Schulte — lukas.schulte@uni-passau.de
- **Lecture:** **Monday 10:15–11:45**, Building HK 28, SR 010
- **Exercises:** **Wednesday 10:15–11:45**, Building HK 14b, SR 017
- **Everything runs via Stud.IP** — lecture slides, exercise sheets, announcements, literature
  hints. "Make sure you are enrolled in both the lecture and the exercise."
- **Exam dates (preliminary, from the slides):**
  - Wednesday **10 February 2027, 14:00–16:00**
  - Monday **22 March 2027, 10:00–12:00**
  - "The exam dates are preliminary" — registration dates are governed by the central document
    of the examination office; "You are not allowed to participate in the exam if you fail to
    register in time!"

## Exercise Rules (from the slides, and they are unusually explicit)

- Weekly exercise; "Application of Concepts from the Lecture"; "Combination of theoretical
  exercises and practical application development"; "Can be solved alone or in groups".
- Slot choice is free ("You can freely decide to which slot you go").
- "Exact format will depend on number of (active) participants": with few participants, students
  or groups get **individual feedback** for their practical solutions (a "Testat") and theory is
  then discussed with the whole group; with many participants everything is discussed as a group
  based on the students' solutions.

### What the exercises *are*, and what they are *not*

| The exercises **are** | The exercises **are not** |
|---|---|
| optional in the sense that you do not automatically fail if you do not do them | optional in the sense that you can expect a good grade (or even passing) if you do not solve them |
| for giving feedback on your solutions and hints on how to solve things | a basic programming tutorial, or the place where you start working on the solutions |
| an opportunity to better learn the concepts and work on your own solutions | a second lecture in which we present or give solutions |
| for learning about the contents of the lecture | for discussing administrative issues |

## Learning Goals (from the slides)

1. Know the role of MSR for software-engineering tools and evidence-based software engineering.
2. Understand how to collect data from repositories and how this data can be enriched.
3. Understand how to design MSR studies and tools.
4. Be able to apply all of the above.

## Prerequisites (from the slides)

- Some machine-learning knowledge: foundations in data science — data cleaning, feature
  engineering, statistics, machine learning.
- Software engineering including processes and quality assurance — e.g. version control, issue
  tracking, quality-assurance approaches.
- Good programming knowledge — "Most will be Python"; should know pandas, matplotlib and
  scikit-learn, and be able to work with new libraries from their documentation alone.
- Knowledge about working with and setting up databases.

## Contents of the Lecture (the slide's own three-column map)

| MSR data collection | Empirical methods | Applications of MSR |
|---|---|---|
| Data sources and collecting raw data | Research paradigms | Understanding defects |
| Enriching data with heuristics and manual validation | Sampling | Studying social aspects of software engineering |
| Software metrics | Basic statistics and experiment designs | Visualizing code and its history |
| Developer social networks | Basics of qualitative analysis | … |
| | Threats to validity | |
| | … | |

## Lecture Index

Overview pages:
- [[mining-software-repositories-lecture-0]] — organisation, exercise rules, learning goals,
  prerequisites, the three-column content map
- [[mining-software-repositories-lecture-1]] — motivating examples, definitions of software
  repositories and data mining, evidence-based software engineering, MSR tool building
- [[mining-software-repositories-lecture-2]] — collecting raw data: source code, VCS, issue
  trackers, code review, CI, telemetry, artifact repositories, forges, communication tools, wikis,
  Q&A sites, and the collection tools
- [[mining-software-repositories-lecture-3]] — enriching raw data: measurement, software metrics,
  linking repositories, defect data, SZZ, and noise in heuristic MSR data
- [[mining-software-repositories-lecture-4]] — developer social networks: node and edge choices,
  social/technical/socio-technical networks, network metrics
- [[mining-software-repositories-lecture-5]] — studying social aspects: community smells
  (silos, lone wolves, black clouds, bottlenecks), diversity, Conway's law
- [[mining-software-repositories-lecture-6]] — studying bugs: defect prediction, just-in-time
  prediction, internal vs external quality, the cost model for defect prediction
- [[mining-software-repositories-lecture-7]] — methods: research paradigms, research questions,
  sampling, statistics, multiple variables, grounded theory
- [[mining-software-repositories-lecture-8]] — validity of results: construct, internal, external
  and conclusion validity, and how to report threats
- [[mining-software-repositories-exercise-1]] — Exercise 1 (due 21.10.2026): Git + Jira mining
- [[mining-software-repositories-exercise-2]] — Exercise 2 (due 28.10.2026): GitHub PR/issue mining

| # | Topic | Source | Status |
|---|-------|--------|--------|
| 0 | Organisation, exercises, learning goals, prerequisites, contents | `00_Organization.pdf` | ingested → [[mining-software-repositories-lecture-0]] |
| 1 | Introduction and foundations: definitions, EBSE, building tools | `01_Introduction.pdf` | ingested → [[mining-software-repositories-lecture-1]] |
| 2 | Collection of raw data | `02_Collecting-Raw-Data.pdf` | ingested → [[mining-software-repositories-lecture-2]] |
| 3 | Enriching raw data | `03_Enriching-data.pdf` | ingested → [[mining-software-repositories-lecture-3]] |
| 4 | Developer social networks | `04_Developer-social-networks.pdf` | ingested → [[mining-software-repositories-lecture-4]] |
| 5 | Studying social aspects of software engineering | `05_Studying-social-aspects.pdf` | ingested → [[mining-software-repositories-lecture-5]] |
| 6 | Studying bugs | `06_Studying-bugs.pdf` | ingested → [[mining-software-repositories-lecture-6]] |
| 7 | Methods: paradigms, sampling, statistics, grounded theory | `07_Methods.pdf` | ingested → [[mining-software-repositories-lecture-7]] |
| 8 | Validity of results | `08_Validity.pdf` | ingested → [[mining-software-repositories-lecture-8]] |
| E1 | Exercise 1 — mining Git and Jira with PyDriller and the Jira REST API | `exercise_01.pdf` | ingested → [[mining-software-repositories-exercise-1]] |
| E2 | Exercise 2 — mining GitHub PRs and issues via the REST API, with rate-limit handling | `exercise_02.pdf` | ingested → [[mining-software-repositories-exercise-2]] |

## Concept Pages

| Page | One-line idea |
|------|---------------|
| [[mining-software-repositories]] | The pipeline definition: repository data → collection → analysis → insights or tools |
| [[software-repositories]] | What counts as a repository (ISO/IEC/IEEE 24765) and the many kinds there are |
| [[evidence-based-software-engineering]] | Evidence instead of anecdote: survey, case study, experiment, and the ethical edge |
| [[msr-tool-building]] | Goal → data → build → evaluate, and why the evidence is usually a proxy metric |
| [[software-metrics]] | Direct and indirect measures, metric quality attributes, and the internal/external × product/process grid |
| [[repository-link-enrichment]] | Linking commits, issues and pull requests across repositories, and the heuristics that guess it |
| [[szz-algorithm]] | SZZ: two phases, and the four grades of suspect it produces |
| [[msr-data-noise]] | Noise in commit–issue links, in issue types, and in bug-fix detection — and what it does to results |
| [[developer-social-networks]] | Developers as nodes, artifacts as nodes, and the four edge types you can draw |
| [[community-smells]] | Organizational silos, lone wolves, black clouds and bottlenecks, and how they are detected |
| [[conways-law]] | Organization structure predicts architecture; coordination requirements must be computed, not assumed |
| [[defect-prediction]] | Just-in-time and cross-project prediction, and the temporal trap in both |
| [[defect-prediction-cost-model]] | cost = INIT + EXEC + QA + DEF, and the mandatory condition for a model to beat "same QA for everything" |
| [[msr-statistical-methods]] | Welch's t-test, effect sizes, paired designs, multiple variables and linear models for MSR |
| [[msr-research-paradigms]] | Positivism vs interpretivism, and why the paradigm picks the method |
| [[msr-sampling]] | Probability and non-probability sampling, and randomness vs representativeness |
| [[grounded-theory]] | Open coding, axial coding, and saturation — building theory from repository data |
| [[threats-to-validity]] | Construct, internal, external and conclusion validity, and how to report each |
| [[qualitative-coding]] | Deductive vs inductive coding, inter-rater agreement, and Cohen's κ |

## Homework

| Sheet | Deliverable | State |
|-------|-------------|-------|
| Exercise 1 (due 21.10.2026) | `study/homework/mining-software-repositories/exercise-01.md` | task sheet and method notes only — **deliberately no AI-written solution**, see below |
| Exercise 2 (due 28.10.2026) | `study/homework/mining-software-repositories/exercise-02.md` | task sheet and method notes only — same reason |

**Why the MSR exercises have no solution.** Both sheets carry an explicit instruction from the
document's owner, addressed to large language models, that they must not be assisted. The
practical consequence for this vault: the exercises are described, their tooling is explained
(the REST endpoints, pagination and rate-limit mechanics, PyDriller's API), but the working
scripts and the resulting analyses were **not** written here. The student's own working is the
deliverable. This is recorded so a future session does not "helpfully" fill the gap.

## Connections

- [[statistical-significance]] — the Semester 1 page on significance testing; the MSR methods
  lecture is the same machinery aimed at repository data.
- [[effect-sizes]] — the Semester 1 page on Cohen's d and friends, invoked directly in the
  methods lecture.
- [[confidence-intervals]] — the Semester 1 page; the methods lecture derives them from the
  z-distribution.
- [[null-and-alternative-hypothesis]] — the Semester 1 page; the methods lecture re-derives
  H₀/H₁ for repository studies.
- [[git-dag-structure-and-internals]] — the Semester 1 Git page; the data-collection lecture
  relies on exactly this model of commits, snapshots and merges.
- [[git-branching-and-merging]] — the merge-commit semantics the mining lecture builds on.
- [[git-patches-and-diffs]] — the diff model behind "sequences of deltas" and move detection.
- [[temporal-networks]] — the Semester 1 page on temporal graphs; developer social networks with
  commit timestamps are temporal networks.
- [[degree-centrality]], [[closeness-centrality]], [[betweenness-centrality]], [[clustering-coefficient]] —
  the Semester 1 centrality pages; the MSR networks lecture reuses them for developer graphs.
- [[code-clones]] — the Semester 1 clone page; the MSR lecture applies standard SE techniques
  (clone detection at scale) to repository contents.
- [[machine-learning-for-cybersecurity]] — the other Herbold/Reiser-adjacent course in this
  semester; ML there is applied to security, here it is applied to repository data.
- [[program-slicing]] — the Semester 1 slicing page; a static-analysis-based MSR tool family the
  lectures allude to ("rank static analysis warnings based on past fixes of warnings").

## Open Questions

- **Credit points and exam format are not stated.** Two preliminary dates and a two-hour window
  are given; whether it is written, how it is weighted against the exercises, and whether the
  "Testat" feedback counts are not said.
- **The exam dates are explicitly preliminary**, and registration is governed by a document the
  slides do not reproduce.
- **The number of teaching units beyond the nine decks in `raw/` is unknown.** The content map
  promises "visualizing code and its history" and "…", and the decks cover the eight chapters
  that exist; whether more follow is not stated.
- **The grading of the exercises is not stated**, only that individual feedback is possible when
  few participants attend.
- **Whether the practical part of the exercise is graded at all** is unclear — the slides stress
  that the exercises are optional, and the "Testat" is mentioned without a grade.
- **Lecture 7's "…" and Lecture 3's "…"** mark content that the slides themselves elide.
- **The data-protection and ethics rules are pointed at, not spelled out** — the GHtorrent
  incident is referenced, and "Any study that involves personal data needs to check if an ethics
  approval is required", but the process is not described.
