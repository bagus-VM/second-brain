---
title: "Semester 2 — Master Index"
tags: [meta, index, semester-2]
status: current
last_updated: 2026-10-22
---

# Semester 2 — Master Index

> Maintained by Professor White. Generated from note frontmatter; re-run `vault/tools/generate_index.py` after an ingest.

**Courses:** 9 registered · **Concept pages:** 88 · **Topic pages:** 33

---

## Courses

| Course | Professor | Exam | Page |
|--------|-----------|------|------|
| [[advanced-it-security]] | Posegga | 05.04.2027 | active |
| [[ai-engineering-lab]] | — | report-based | current |
| [[dependable-distributed-systems]] | Reiser | TBD | active |
| [[energy-informatics-1]] | de Meer | 17.02.2027 / 24.03.2027 | active |
| [[introduction-to-deep-learning]] | Lemmerich | TBD | active |
| [[machine-learning-for-cybersecurity]] | Reiser | portfolio | active |
| [[mining-software-repositories]] | Herbold | 10.02.2027 / 22.03.2027 (preliminary) | active |
| [[reverse-and-reengineering]] | Hammer | two dates via Campus Portal (90 points / 90 min) | active |
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

### Dependable Distributed Systems

| Page | Summary | Sources | Status |
|------|---------|---------|--------|
| [[clock-synchronization-problem]] | Physical clocks never agree, they only disagree at different rates — and the first thing that breaks when they disagree is any snapshot o… | 1 | current |
| [[communication-link-models]] | A communication link model states what a channel between two processes is allowed to do to messages — lose them, duplicate them, invent t… | 2 | current |
| [[dependability-attributes]] | Dependability is measured on three axes — reliability, maintainability, and availability — which describe how long a system works, how fa… | 6 | current |
| [[distributed-system-properties]] | A distributed system is several independent computers joined by a network that run shared protocols so that, to the people using them, th… | 4 | current |
| [[error-detection-and-recovery]] | Fault tolerance has two moving parts — detect the error, then recover from it — and the lecture splits each of them into concrete sub-str… | 7 | current |
| [[failure-models]] | A failure model is an assumption about how a component in a distributed system is allowed to misbehave, ranging from "stops forever" up t… | 3 | current |
| [[fault-error-failure-chain]] | A fault is a broken part, an error is the broken state that part creates, and a failure is what the user finally notices when the service… | 5 | current |
| [[lamport-logical-clocks]] | A counter per process that answers "which of these two events came first?" correctly whenever one event could have influenced the other —… | 2 | current |
| [[model-accuracy-tractability]] | A model is a simplification you are allowed to argue with — but only if the simplification is both faithful to reality and small enough t… | 1 | current |
| [[redundancy-forms]] | Redundancy comes in exactly three flavours — extra copies, extra tries, and extra information — and every dependable technique in the cou… | 2 | current |
| [[resilience-vs-dependability]] | Dependability is the quality of a service you can justifiably rely on, while resilience adds the requirement that this reliability surviv… | 3 | current |
| [[synchronous-vs-asynchronous-models]] | An asynchronous system makes no promises about how fast anything happens, while a synchronous system promises bounded speeds and bounded… | 3 | current |
| [[vector-clocks]] | Lamport's counter tells you that one event might have caused another; the vector version tells you exactly which — and what it costs you… | 1 | current |
| [[ways-towards-dependability]] | There are exactly four ways to make a system more dependable: stop faults from happening, keep working despite them, take faults away onc… | 3 | current |

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

### Reverse- and Reengineering

| Page | Summary | Sources | Status |
|------|---------|---------|--------|
| [[architecture-smell]] | An architecture smell is a structural weakness at the level of the software architecture itself, and its remedy is architecture refactori… | 1 | current |
| [[binary-reverse-engineering]] | Binary reverse engineering is the analysis of a program when the artefact available is machine code rather than source, spanning the abst… | 2 | current |
| [[legacy-system-renewal]] | The lecture names three procedures for renewing a legacy system — packing it behind a modern shell, migrating it component by component,… | 1 | current |
| [[legacy-systems]] | A legacy system is an old, poorly documented, often enormous piece of software whose handling and architecture nobody at the company unde… | 1 | current |
| [[reengineering-vs-maintenance]] | Maintenance adapts the software to the customer's wishes; reengineering reconstitutes the system so the developer can work on it again —… | 1 | current |
| [[reengineering]] | Reengineering is the examination and alteration of an existing system in order to reconstitute it in a new form — the full round trip fro… | 2 | current |
| [[refactoring-and-code-smells]] | Refactoring is the restructuring of a program's inner shape while keeping its outer behaviour exactly the same, and a code smell is the o… | 1 | current |
| [[reverse-engineering]] | Reverse engineering is the analysis of a system that supports understanding it — identifying its components and artifacts, discovering th… | 2 | current |
| [[software-aging]] | Software aging is the progressive loss of software quality after release, caused by changing requirements and by adaptations that do not… | 1 | current |
| [[x86-assembly-and-abi]] | The x86 family is a CISC instruction set whose 16-, 32- and 64-bit generations differ in registers, addressing modes and calling conventi… | 1 | current |

### Mining Software Repositories

| Page | Summary | Sources | Status |
|------|---------|---------|--------|
| [[community-smells]] | Community smells are the social counterparts of code smells: patterns in a community's communication structure that indicate a deeper pro… | 1 | current |
| [[conways-law]] | Conway's law says a system's architecture copies the communication structure of the organisation that built it, and socio-technical congr… | 1 | current |
| [[defect-prediction-cost-model]] | A defect prediction model is worth using only if it saves more quality-assurance money than it costs to run and maintain, and that compar… | 1 | current |
| [[defect-prediction]] | Defect prediction learns from historic defect data to flag which software artifacts are likely defective, and in the just-in-time variant… | 1 | current |
| [[developer-social-networks]] | A developer social network is a graph whose nodes and edges you choose, and every research claim about how developers work depends on tho… | 1 | current |
| [[evidence-based-software-engineering]] | Evidence-based software engineering applies the logic of evidence-based medicine to technical decisions: gather rigorous evidence first,… | 1 | current |
| [[grounded-theory]] | Grounded theory builds a theory out of data by coding it inductively — and the lecture's chosen variant, Straussian grounded theory, work… | 1 | current |
| [[mining-software-repositories]] | MSR is a pipeline: take the data a repository already records, collect it in a form you can analyse, analyse it, and end up with either a… | 2 | current |
| [[msr-data-noise]] | Heuristic MSR data is never clean: every wrong assumption behind a heuristic becomes noise, and a study's validity depends on measuring t… | 1 | current |
| [[msr-research-paradigms]] | The paradigm you adopt — positivism, interpretivism or pragmatism — decides how you frame the research question, which methods you reach… | 1 | current |
| [[msr-sampling]] | Sampling decides which data a study looks at, how that data was drawn, and how far the resulting claim may travel — and randomness alone… | 1 | current |
| [[msr-statistical-methods]] | The statistics that make an MSR claim defensible: hypothesis testing to decide whether an observation is likely random, effect sizes to s… | 1 | current |
| [[msr-tool-building]] | Building an MSR tool is a four-step procedure — fix the goal, fix the data, build, then run an experiment — and the evidence you end up w… | 1 | current |
| [[qualitative-coding]] | Coding is the assignment of labels to data by humans, and the machinery that makes such labels trustworthy — multiple raters, agreement s… | 2 | current |
| [[repository-link-enrichment]] | Link enrichment is the task of establishing which commit belongs to which issue, which pull request belongs to which commit — from explic… | 1 | current |
| [[software-metrics]] | A software metric is the operationalization of a measurement: a rule-derived number that represents an attribute of a product or a proces… | 1 | current |
| [[software-repositories]] | A software repository is not one thing but a family of stores — version control, issue trackers, review systems, CI servers, telemetry, a… | 2 | current |
| [[szz-algorithm]] | SZZ identifies bug-fixing commits by linking commit-message numbers to issues, then traces each changed line back through blame to the ch… | 1 | current |
| [[threats-to-validity]] | Validity is not a feeling but a structured assessment: five dimensions of threats, each with a named list, each of which makes a result l… | 1 | current |

## Topic Pages

| Page | Summary | Sources | Status |
|------|---------|---------|--------|
| [[Topics]] | Chapter-level overviews: one page per lecture (or exercise unit), tying that session's concepts together and pointing at the pages it pro… | — | current |
| [[advanced-it-security-exercise-0]] | The only Advanced IT Security material in `raw/` is the exercise introduction: Thursdays from 29.10.2026, English, no credit points, but… | 1 | current |
| [[advanced-it-security-lecture-0]] | The lecture that fixes the vocabulary: what "secure" means, what a security solution is made of, what risk actually is — and why every on… | 1 | current |
| [[deep-learning-course-roadmap]] | Fifteen weeks from Python syntax to graph neural networks, where each week's homework is either a pen-and-paper derivation or a coding ta… | 1 | current |
| [[dependable-distributed-systems-exercise-1]] | Six tasks that turn lecture 1 into something you have to argue: pick the right property, pick the right attribute, separate dependability… | 1 | current |
| [[dependable-distributed-systems-exercise-2]] | The sheet where the models become a T/F exercise and the logical clocks become arithmetic: one trick question about synchrony, five T/F i… | 2 | current |
| [[dependable-distributed-systems-lecture-1]] | The first lecture does two jobs: it establishes what a distributed system is and what it therefore cannot have, then it builds the vocabu… | 1 | current |
| [[dependable-distributed-systems-lecture-2]] | One lecture, three movements: what a model is and why you need one that is both faithful and analysable, the taxonomy of failures and cha… | 1 | current |
| [[energy-informatics-1-lecture-0]] | Lecture 0 sets up the whole course: computing is a large and growing energy load, the electrical grid is a real-time balancing act with h… | 1 | current |
| [[introduction-to-deep-learning-exercise-1]] | The first session is not deep learning: it is the Python on-ramp the whole course stands on, plus an opinionated toolchain (`uv`, VS Code… | 5 | current |
| [[introduction-to-deep-learning-exercise-2]] | The first week in which the course stops being about Python: PyTorch's tensors and autograd on one side, the fact that a network's loss c… | 3 | current |
| [[introduction-to-deep-learning-lecture-1]] | The opening lecture: what deep learning is, how the field got here in eighty years, and what is still unsolved — plus the course organisa… | 1 | current |
| [[machine-learning-for-cybersecurity-lecture-1]] | Two foundations in one session: security as a cost/benefit discipline with its own vocabulary, and machine learning as a task taxonomy th… | 1 | current |
| [[machine-learning-for-cybersecurity-lecture-2]] | The first working pipeline of the course: pandas → scikit-learn → metrics on credit-card fraud, then Naive Bayes derived from Bayes' rule… | 1 | current |
| [[machine-learning-for-cybersecurity-lecture-3]] | Metrics and ROC curves get their own pass, KNN and the two regressions are added to the toolbox, and the ROC is then re-examined through… | 1 | current |
| [[mining-software-repositories-exercise-1]] | Exercise 1 asks you to build a small mining pipeline by hand: explore Git and Jira as data sources, collect commits with PyDriller and is… | 1 | current |
| [[mining-software-repositories-exercise-2]] | Exercise 2 moves from Git and Jira to the forge: exploring which GitHub tools the Apache Ignite project uses, mining pull requests and is… | 1 | current |
| [[mining-software-repositories-lecture-0]] | The organizational deck fixes the frame for the whole course: two lecturers, a Monday lecture and a Wednesday exercise slot, two prelimin… | 1 | current |
| [[mining-software-repositories-lecture-1]] | Chapter 1 argues that software development is decided by anecdote where it could be decided by evidence, defines what a software reposito… | 1 | current |
| [[mining-software-repositories-lecture-2]] | Chapter 2 is the data-source catalogue: it argues that any tool a developer uses is a potential MSR source, walks each family of sources… | 1 | current |
| [[mining-software-repositories-lecture-3]] | Chapter 3 covers the step between raw collection and analysis: operationalizing raw events into metrics, linking artefacts across reposit… | 1 | current |
| [[mining-software-repositories-lecture-4]] | Chapter 4 turns software development into a graph: it fixes the graph vocabulary, then asks the two questions every network definition mu… | 1 | current |
| [[mining-software-repositories-lecture-5]] | Chapter 5 applies the network machinery twice: detect four community smells from two undirected graphs — silos, lone wolves, black clouds… | 1 | current |
| [[mining-software-repositories-lecture-6]] | Chapter 6 takes defect data seriously: it lays out defect prediction as a pipeline with three checkable questions, shows why just-in-time… | 1 | current |
| [[mining-software-repositories-lecture-7]] | Chapter 7 is the methods chapter: the paradigm decides how a question is framed, sampling decides which data the claim rests on, statisti… | 1 | current |
| [[mining-software-repositories-lecture-8]] | Chapter 8 turns "trust" into a structured assessment: five dimensions of validity, each with named threat lists, and a reporting discipli… | 1 | current |
| [[reverse-and-reengineering-exercise-1]] | Four drawings that turn the lecture's graph vocabulary into practice — an intra-procedural CFG, a dependence graph, two backward slices,… | 1 | current |
| [[reverse-and-reengineering-exercise-2]] | Homework 2 puts the lecture's x86 material to work: recover two functions' arguments and their equivalent C from assembly, then draw the… | 1 | current |
| [[reverse-and-reengineering-lecture-1]] | Software ages, reengineering is the response, and control-flow graphs, dependence graphs and slicing are the analysis machinery that make… | 1 | current |
| [[reverse-and-reengineering-lecture-2]] | Lecture 2 gives reverse engineering its definition, its ladder of artefacts, its static and dynamic toolkits, and the x86 instruction set… | 1 | current |
| [[virtual-machines-and-runtime-systems-exercise-1]] | Two problems that turn lecture 2's slides into running code: observe segment boundaries from inside a program and a library under three l… | 1 | current |
| [[virtual-machines-and-runtime-systems-lecture-1]] | Three definitions that the rest of the course leans on: abstraction (loses detail) versus virtualization (preserves state transitions), e… | 1 | current |
| [[virtual-machines-and-runtime-systems-lecture-2]] | Everything the C runtime system does at run time: process memory layout and the loader, dynamic libraries and `dlopen`, error handling wi… | 1 | current |

## Gaps

- Bitcoin and Cryptocurrencies Technologies: `raw/` folder empty, no page.
- Dropped on 2026-10-20: Hardware-Oriented Security — all pages and raw sources removed.
- Reverse- and Reengineering was dropped on 2026-10-20 and has since been re-registered; new material (2 lectures, 2 homework sheets) was ingested on 2026-10-22. The Term 2 exam timeframe is printed as '22.03.-09.04.2025' and is flagged as a typo on the course page.
- Mining Software Repositories (new registration, ingested 2026-10-22): 9 lecture decks and 2 exercise sheets. The two exam dates are explicitly preliminary; credit points and exam format are not stated in the material.
- Dropped on 2026-10-21: Scaling Database Systems — all pages and raw sources removed.
- Advanced IT Security: lecture 0 (Basics) is ingested; lectures 1-6 have no slides in `raw/` yet.
- Dependable Distributed Systems: lectures 1-2 and exercises 1-2 ingested; the 12-topic semester plan is preliminary, so topics 3-12 have no slides in `raw/` yet.
- The two Mining Software Repositories exercise sheets carry an explicit instruction from their owner that they must not be assisted by AI, so no AI-written solution exists for them; the vault holds the task sheet, the tooling mechanics and the method notes, and the working scripts and analysis are the student's own work.
- Exam formats/dates marked TBD were not in the source material and are not guessed.
