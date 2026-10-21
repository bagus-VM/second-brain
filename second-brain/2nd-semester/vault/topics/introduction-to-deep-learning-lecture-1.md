---
title: "Introduction to Deep Learning — Lecture 1: Introduction and Overview"
tags: [topic, deep-learning, semester-2, lecture]
course: "Introduction to Deep Learning"
source_count: 1
status: current
last_updated: 2026-10-20
prerequisites: []
---

## One-line Summary
The opening lecture: what deep learning is, how the field got here in eighty years, and what is
still unsolved — plus the course organisation that tells you how the exam will be built.

## Core Map

```
Introduction to Deep Learning — Lecture 1
│
├── Welcome & motivation
│   ├── Applications: medical imaging, fraud detection, speech, object detection,
│   │   translation, games, chat bots, image generation, image-to-image translation
│   ├── Nobel Prizes 2024 (Physics: Hopfield & Hinton; Chemistry: Baker, Hassabis & Jumper)
│   └── 2024 Turing Award (Barto & Sutton, reinforcement learning)
│
├── Course organisation
│   ├── Lectures: Friday 10:15–11:45 (WIWI) HS 8, 16.10.2026 – 05.02.2027
│   ├── Exercises: Master Thu 12:15–13:45 or 14:15–15:45 (WIWI) SR 029
│   │              Bachelor Tue 14:00–14:45
│   ├── Language: English
│   ├── Exam: written, 90 minutes, covers EVERYTHING incl. first and last lecture,
│   │         may contain some coding, resit before next semester
│   └── Assumed knowledge: linear algebra, calculus, statistics
│
├── What is deep learning?
│   ├── AI ⊃ Machine Learning ⊃ Representation Learning ⊃ Deep Learning
│   ├── "Deep learning is a buzzword" — a marketing trick
│   ├── Representation learning: learn φ as well as g
│   └── → [[representation-learning]]
│
├── A short history
│   └── 1943 → 2026 → [[deep-learning-history-timeline]]
│
└── Current challenges
    ├── Trustworthiness: hallucinations, interpretability, robustness, bias
    ├── Safety & society: alignment, agents, deepfakes, jobs
    └── Resources & rules: energy, data, copyright, EU AI Act
```

## Key Concepts at a Glance

| Page | One-line idea |
|------|---------------|
| [[representation-learning]] | Deep learning's actual claim: learn the *features*, not just the mapping from features to output. |
| [[deep-learning-history-timeline]] | Eighty years from McCulloch-Pitts to agents that write and run code — and the two AI winters along the way. |
| [[pytorch-tensors-and-autograd]] | The tensor, the computation graph, and how `.backward()` replaces a hand-derived chain rule. |
| [[neural-network-training-loop]] | The five steps, and why `zero_grad` sits in the middle of them. |
| [[gradient-descent-for-neural-networks]] | Why a network with activation functions forces the numerical path. |
| [[polynomial-regression-and-overfitting]] | The first overfitting experiment: what model capacity costs you in validation loss. |
| [[deep-learning-course-roadmap]] | The full 15-week map with the homework type per week. |

## Lecture Structure

**Welcome and motivation.** The lecture opens with a parade of applications — medical image
classification (glioma vs. no tumour), fraud detection, speech recognition, object detection,
translation, deep learning in games, chat bots in 2021 and 2023, image generation in 2022, and
image-to-image translation. Then the Nobel Prizes: 2024 in Physics to John Hopfield and Geoffrey
Hinton "for foundational discoveries and inventions that enable machine learning with artificial
neural networks", and 2024 in Chemistry to David Baker (computational protein design) and Demis
Hassabis and John Jumper (protein structure prediction, AlphaFold).

**Course organisation** — and this is the part that matters most for exam prep:

- Lectures: **Friday 10:15–11:45**, (WIWI) HS 8, from **16.10.2026 to 05.02.2027**.
- Exercises: Master students **Thursday 12:15–13:45 or 14:15–15:45** in (WIWI) SR 029;
  Bachelor students **Tuesday 14:00–14:45**. Attendance is not mandatory but strongly recommended.
- Language: English. Slides go online in Stud.IP; "no intentional omissions, but completeness of
  the slides is not guaranteed" and "**the spoken word counts**" for exam content — so the slides
  are not a complete record of the exam scope.
- No lecture recording: the course is under development, recording raises the threshold for
  interaction, and speaking "off the record" is wanted.
- **Exam: a written exam of 90 minutes.** No prerequisites to participate (no exercise-score
  requirement), no bonus. It covers **everything covered in the course** — lectures *and*
  exercises — **may contain some coding**, and explicitly **includes the first and the last
  lecture**. A resit is offered before the next semester. Dates for both exams will be announced.
- Assumed knowledge: linear algebra (vectors, matrices, matrix operations, matrices as
  functions), calculus (minima, maxima, derivatives, partial derivatives and gradients), and
  statistics (data types, joint and conditional probability, likelihood, distributions).

**What is deep learning?** The lecture is blunt: "Deep Learning is a buzzword! The term 'deep
learning' was/is a 'marketing trick'", formerly "multilayer artificial neural networks" or
"multilayer perceptrons". The nesting is AI ⊃ Machine Learning ⊃ Representation Learning ⊃ Deep
Learning. The core claim of representation learning, quoting Goodfellow et al. (2016), is that
machine learning is used to discover *not only* the mapping from representation to output but
*also the representation itself*. The lecture also carries the counterweight: Gary Marcus's
critique that deep learning techniques lack ways of representing causal relationships, have no
obvious ways of performing logical inferences, and remain far from integrating abstract knowledge
— the strongest AI systems use deep learning as one element of a much larger ensemble alongside
Bayesian inference and deductive reasoning.

**A short history.** 1943 to 2026, in one slide deck. The full timeline is on
[[deep-learning-history-timeline]].

**Current challenges**, in the lecture's own three-column layout: trustworthiness
(hallucinations, interpretability, robustness against adversarial attacks and jailbreaks and
prompt injection, bias and fairness); safety and society (alignment, autonomous agents acting in
the real world, deepfakes and misinformation, impact on education and jobs); resources and rules
(energy and compute cost, running out of training data, copyright and privacy of training data,
the EU AI Act).

## Exam-Relevant Points

1. **The exam is 90 minutes, written, and covers everything.** Both the first and the last
   lecture are explicitly in scope — so the history lecture and the explainability wrap-up are
   not optional.
2. **"May contain some coding"** — and the first two sessions have already been code. Expect to
   write or read PyTorch.
3. **"The spoken word counts."** The slides are explicitly incomplete, so the vault's pages are
   the substitute record, not the slides.
4. **Deep learning is a rebranding, not a single invention** — the 2006 Hinton et al. moment.
   This is the exam's version of "what is new in deep learning".
5. **Representation learning is the load-bearing idea**, and the four-level nesting
   (AI/ML/RL/DL) is a standard recall question.
6. **The three challenge columns** — trustworthiness / safety & society / resources & rules — are
   a natural essay question, and the exam covers the *last* lecture, which is exactly where
   explainability lands.
7. **No bonus, no prerequisites.** The in-class retrieval-practice tests are not graded, so they
   are preparation rather than assessment.

## Connections

- [[introduction-to-deep-learning]] — the course page: the 15-week provisional schedule from
  exercise 1, which does not match this lecture's session numbering; both are recorded.
- [[deep-learning-course-roadmap]] — the dependency map for the whole semester.
- [[representation-learning]] — the lecture's central concept.
- [[deep-learning-history-timeline]] — the lecture's history section, in full.
- [[machine-learning-basics]] — the Semester 1 page on the task taxonomy this lecture's
  "Machine Learning Tasks" slide refers to.
- [[ml-task-taxonomy]] — the six task families (classification, regression, structured
  prediction, clustering, reinforcement learning, …) from the sibling course.
- [[word2vec-skip-gram]] — the 2013/2014 word-embedding step in the history.
- [[graph-neural-networks]] — where the roadmap says the course ends up.
- [[python-environment-management]] — the `uv` setup the course's first session drilled.

## Open Questions

- The lecture's course overview lists 15 sessions with topics and dates, and the exercise-1
  material (already in the vault) lists a 15-week plan with a *different* topic-to-week mapping
  — e.g. the lecture deck puts "Foundations of Machine Learning" in sessions 2–3 and "Single-Layer
  Neural Networks" in 4–5, while the exercise sheet puts "Introduction to PyTorch" in week 2 and
  "Gradient descent" in week 3. Which is the authoritative sequence, and whether the second
  lecture is a lecture on foundations or the PyTorch exercise, is not reconciled by the material.
- The lecture states the exam covers the first and last lecture, but the exam date is not
  announced, and the course is explicitly "under development" — so the exam scope itself may
  still move.
- "May contain some coding" is not specified further: whether it means writing PyTorch from
  scratch, completing a notebook, or reading code is not stated.
- The lecture lists a "Deep Learning course roadmap (all 15 weeks)" page in the vault
  ([[deep-learning-course-roadmap]]); whether the session table in the slides or the week table
  in the exercise sheet is the version the exam will follow is open.
