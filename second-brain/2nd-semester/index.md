---
title: "Semester 2 — Master Index"
tags: [meta, index, semester-2]
status: current
last_updated: 2026-10-20
---

# Semester 2 — Master Index

> Maintained by Professor White. Generated from note frontmatter; re-run `vault/tools/generate_index.py` after an ingest.

**Courses:** 7 registered · **Concept pages:** 48 · **Topic pages:** 15

---

## Courses

| Course | Professor | Exam | Page |
|--------|-----------|------|------|
| [[advanced-it-security]] | Posegga | 05.04.2027 | active |
| [[ai-engineering-lab]] | — | report-based | current |
| [[energy-informatics-1]] | de Meer | 17.02.2027 / 24.03.2027 | active |
| [[introduction-to-deep-learning]] | Lemmerich | TBD | active |
| [[machine-learning-for-cybersecurity]] | Reiser | portfolio | active |
| [[scaling-database-systems]] | Scherzinger | TBD | active |
| [[virtual-machines-and-runtime-systems]] | Größlinger | 11.02.2027 / 01.04.2027 | active |

## Concept Pages by Course

### Energy Informatics I

| Page | Summary | Sources | Status |
|------|---------|---------|--------|
| [[alternating-current-basics]] | AC is a sinusoid; its descriptive numbers are amplitude, period and frequency, and the value that matters for power and for the 230 V soc… | 1 | current |
| [[demand-side-integration]] | Once supply becomes volatile and moves into the low-voltage grid, the controllable side of the balance has to become demand — which turns… | 1 | current |
| [[ict-energy-footprint]] | Computing consumes a measurable share of global energy, and the fastest-growing parts — cloud, AI, blockchain — are exactly the parts tha… | 1 | current |
| [[paris-agreement-climate-goals]] | The 2015 Paris Agreement sets a "well below 2 °C, pursue 1.5 °C" target to avoid irreversible tipping points; the EU's 20/20/20 package t… | 1 | current |
| [[power-grid-fundamentals]] | The grid is a two-level hierarchy — transmission above, distribution below — held together by one shared frequency that reports the deman… | 1 | current |
| [[sector-coupling]] | Sector coupling is the interoperability of the electricity, gas and thermal systems under one integrated energy management, so that flexi… | 1 | current |

### Introduction to Deep Learning

| Page | Summary | Sources | Status |
|------|---------|---------|--------|
| [[deep-learning-history-timeline]] | Deep learning is eighty years of slow progress, one long winter, one rebranding in 2006, and a data-and-hardware-driven explosion from 20… | 1 | current |
| [[gradient-descent-for-neural-networks]] | Gradient descent is the general method of approximately minimising a differentiable function by repeatedly stepping against its gradient;… | 1 | current |
| [[jupyter-notebook-state]] | A notebook cell's stored output is a snapshot of one particular execution, not a property of the code beside it — so editing a definition… | 1 | current |
| [[linear-algebra-for-deep-learning]] | The demo notebook implements the linear algebra a neural network does internally — dot product, vector addition, normalisation, matrix mu… | 1 | current |
| [[neural-network-training-loop]] | Training a neural network is a fixed five-step cycle — forward pass, loss, zero the gradients, backpropagate, step the optimiser — repeat… | 1 | current |
| [[polynomial-regression-and-overfitting]] | Polynomial regression fits a linear model to the powers of the features, so it is linear regression on transformed inputs — and the degre… | 1 | current |
| [[python-environment-management]] | A virtual environment is a per-project box holding one Python interpreter and one exact set of packages; `uv` creates that box, installs… | 2 | current |
| [[python-for-deep-learning]] | Python is the lingua franca of machine learning not because it is fast, but because it is readable, dynamically typed, garbage-collected,… | 1 | current |
| [[pytorch-tensors-and-autograd]] | PyTorch gives you NumPy-style array arithmetic on tensors that remember the function they were produced by, so that gradients of any comp… | 1 | current |
| [[representation-learning]] | Representation learning is machine learning in which the features are not handed over but learned from data; deep learning is the part of… | 1 | current |

### Machine Learning for Cybersecurity

| Page | Summary | Sources | Status |
|------|---------|---------|--------|
| [[attacker-classification]] | Abraham et al. (1991) sort attackers into three classes by knowledge of the system and equipment they can afford — and that class, not th… | 1 | current |
| [[classification-metrics]] | Four numbers decide whether a detector is any good, and on security data the most quoted one is the least informative: L2's credit-card m… | 2 | current |
| [[feature-normalization]] | Scaling features to a common range is what stops one large-magnitude column from deciding every distance or every gradient step — and it… | 1 | current |
| [[k-nearest-neighbors]] | KNN classifies a new sample by the majority class of its K closest training samples — no model parameters, no training phase, all the cos… | 1 | current |
| [[linear-regression]] | Linear regression fits a straight line through feature space by minimising the sum of squared residuals, which has a closed-form solution… | 1 | current |
| [[logistic-regression]] | Logistic regression takes a linear function of the features, squashes it through a sigmoid into a probability, and fits it by minimising… | 1 | current |
| [[ml-for-security-domains]] | L1 maps the same three tasks — regression, classification, clustering — onto five security domains, showing that the tasks transfer while… | 1 | current |
| [[ml-learning-paradigms]] | L1 splits machine learning two ways: vertically into AI ⊃ ML ⊃ DL, and horizontally into six training paradigms that differ in where the… | 1 | current |
| [[ml-pipeline-scikit-learn]] | L2's credit-card example is the supervised workflow end to end: inspect with pandas, split features from labels, hold out a test set, fit… | 2 | current |
| [[ml-task-taxonomy]] | L1 reduces machine learning to six task families — regression, classification, clustering, association rules, dimensionality reduction, g… | 1 | current |
| [[naive-bayes-text-classification]] | Naive Bayes picks the class maximising P(d\|c)·P(c), and makes that computable by pretending word occurrences are independent given the c… | 1 | current |
| [[roc-curve]] | A ROC curve plots the true-positive rate against the false-positive rate as the decision threshold is swept from 1 down to 0, so it descr… | 1 | current |
| [[security-terminology-and-risk-model]] | "X is secure" is a meaningless sentence. Security is always security *against something*, at *some cost*, with *some residual risk* — and… | 1 | current |

### Scaling Database Systems

| Page | Summary | Sources | Status |
|------|---------|---------|--------|
| [[minihive-project-structure]] | miniHive is the term project of Scaling Database Systems: a minimalistic version of Hive, built on the command line in Python and tested… | 3 | current |
| [[praktomat-submission-workflow]] | Praktomat is the course's only submission channel: an automatically checking, deadline-enforcing platform where the Final Solution is the… | 2 | current |
| [[rootless-docker-server-access]] | narrow-sea is the course's shared Docker host, reachable only from inside the university network, where each student runs their own rootl… | 1 | current |

### Virtual Machines and Runtime Systems

| Page | Summary | Sources | Status |
|------|---------|---------|--------|
| [[dynamic-linking]] | Static libraries are copied into the binary at link time; dynamic libraries are separate objects mapped into the process's `mmap` area at… | 2 | current |
| [[errno-error-handling]] | C has no exceptions, so functions report failure through their return value and stash the reason in the global `errno` — and the two must… | 1 | current |
| [[exception-handling-implementation]] | Exceptions are implemented so that code which never throws pays nothing: hardware and kernel raise `SIGSEGV`/`SIGFPE`, and the runtime fi… | 1 | current |
| [[process-memory-layout]] | A process is a program in execution — text plus data, where data splits into data, BSS, heap and stack — laid out in a *virtual* address… | 2 | current |
| [[runtime-system]] | A runtime system is everything a program needs at run time but did not get from the compiler — memory, I/O, threads, error handling — del… | 2 | current |
| [[setjmp-longjmp]] | `setjmp` snapshots the processor registers; `longjmp` restores them — giving C an untyped, uncontrolled non-local goto that works by movi… | 1 | current |
| [[thread-emulation-longjmp]] | Threads can be emulated in plain C by keeping one `jmp_buf` per thread and jumping between them — the hard part is not the jump but givin… | 1 | current |
| [[unix-signals]] | A signal is an asynchronous message to a process that an event occurred; you ignore it, die from it, or run a handler — and if the handle… | 1 | current |
| [[virtualization-vs-abstraction]] | Abstraction throws away detail; virtualization preserves the guest's state transitions inside the host. A VM is not an abstraction of a m… | 1 | current |

### Advanced IT Security

| Page | Summary | Sources | Status |
|------|---------|---------|--------|
| [[gsm-security-political-constraints]] | GSM's weak points are not oversights: they are the direct consequence of export-control law and lawful-interception regulation, so a fix… | 1 | current |
| [[integrity-definition-landscape]] | Integrity has at least six competing standard definitions, and they disagree along two axes — property or state, and detection or prevent… | 1 | current |
| [[risk-perception-and-dread-risk]] | People judge risk by feeling, not by statistics — so the numbers that should govern a security decision are systematically the numbers th… | 1 | current |
| [[security-cost-benefit-optimum]] | The optimal security level is the point where the cost of security-enhancing mechanisms and the expected cost of violations cross — and i… | 1 | current |
| [[security-evaluation-and-assurance-levels]] | Security evaluation asks whether a product delivers the security service it promised and states the degree of trust in that claim — and b… | 1 | current |
| [[security-policy-mechanism-assurance]] | A security solution has three parts — a policy that states what must hold, a mechanism that enforces it, and assurance that shows the mec… | 1 | current |
| [[security-relationship-model]] | The lecture's "Beziehungen" diagram is the causal backbone of risk management: threats exploit vulnerabilities, both raise risk, risk ind… | 1 | current |

## Topic Pages

| Page | Summary | Sources | Status |
|------|---------|---------|--------|
| [[Topics]] | Chapter-level overviews: one page per lecture (or exercise unit), tying that session's concepts together and pointing at the pages it pro… | — | current |
| [[advanced-it-security-exercise-0]] | The only Advanced IT Security material in `raw/` is the exercise introduction: Thursdays from 29.10.2026, English, no credit points, but… | 1 | current |
| [[advanced-it-security-lecture-0]] | The lecture that fixes the vocabulary: what "secure" means, what a security solution is made of, what risk actually is — and why every on… | 1 | current |
| [[deep-learning-course-roadmap]] | Fifteen weeks from Python syntax to graph neural networks, where each week's homework is either a pen-and-paper derivation or a coding ta… | 1 | current |
| [[energy-informatics-1-lecture-0]] | Lecture 0 sets up the whole course: computing is a large and growing energy load, the electrical grid is a real-time balancing act with h… | 1 | current |
| [[introduction-to-deep-learning-exercise-1]] | The first session is not deep learning: it is the Python on-ramp the whole course stands on, plus an opinionated toolchain (`uv`, VS Code… | 5 | current |
| [[introduction-to-deep-learning-exercise-2]] | The first week in which the course stops being about Python: PyTorch's tensors and autograd on one side, the fact that a network's loss c… | 3 | current |
| [[introduction-to-deep-learning-lecture-1]] | The opening lecture: what deep learning is, how the field got here in eighty years, and what is still unsolved — plus the course organisa… | 1 | current |
| [[machine-learning-for-cybersecurity-lecture-1]] | Two foundations in one session: security as a cost/benefit discipline with its own vocabulary, and machine learning as a task taxonomy th… | 1 | current |
| [[machine-learning-for-cybersecurity-lecture-2]] | The first working pipeline of the course: pandas → scikit-learn → metrics on credit-card fraud, then Naive Bayes derived from Bayes' rule… | 1 | current |
| [[machine-learning-for-cybersecurity-lecture-3]] | Metrics and ROC curves get their own pass, KNN and the two regressions are added to the toolbox, and the ROC is then re-examined through… | 1 | current |
| [[scaling-database-systems-exercise-0]] | Everything the course has told you so far is logistics: when to show up, what to bring, how to run a container, how to hand in a milestone. | 4 | current |
| [[virtual-machines-and-runtime-systems-exercise-1]] | Two problems that turn lecture 2's slides into running code: observe segment boundaries from inside a program and a library under three l… | 1 | current |
| [[virtual-machines-and-runtime-systems-lecture-1]] | Three definitions that the rest of the course leans on: abstraction (loses detail) versus virtualization (preserves state transitions), e… | 1 | current |
| [[virtual-machines-and-runtime-systems-lecture-2]] | Everything the C runtime system does at run time: process memory layout and the loader, dynamic libraries and `dlopen`, error handling wi… | 1 | current |

## Gaps

- Bitcoin and Cryptocurrencies Technologies: `raw/` folder empty, no page.
- Dropped on 2026-10-20: Hardware-Oriented Security and Reverse- and Reengineering — all pages and raw sources removed.
- Advanced IT Security: lecture 0 (Basics) is ingested; lectures 1-6 have no slides in `raw/` yet.
- Scaling Database Systems: new course. Only organisational sheets in `raw/` - `raw/lectures/Scaling Database Systems/Vorlesung/` is empty, so no lecture slides have been ingested and the technical content is not yet in the vault.
- Exam formats/dates marked TBD were not in the source material and are not guessed.
