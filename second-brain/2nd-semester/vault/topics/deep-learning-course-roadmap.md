---
title: "Deep Learning Course Roadmap"
tags: [topic, deep-learning, semester-2, roadmap]
course: "Introduction to Deep Learning"
source_count: 1
status: current
last_updated: 2026-10-19
prerequisites: []
---

## One-line Summary
Fifteen weeks from Python syntax to graph neural networks, where each week's homework is either a pen-and-paper derivation or a coding task — and that split, not the topic list, determines how to prepare.

## The Schedule
Provisional, as printed in exercise 1:

| Week | Content | Homework |
|------|---------|----------|
| 1 | Introduction to Python | Coding, paper |
| 2 | Introduction to PyTorch | Coding |
| 3 | Gradient descent, evaluation metrics | Pen and paper |
| 4 | Automatic differentiation, stochastic gradient descent | Coding, paper |
| 5 | Multi-layer perceptrons | Coding |
| 6 | Loss functions, advanced programming | Paper |
| 7 | Activation functions, parameter initialization | Coding, paper |
| 8 | Improving training with optimizers and regularization | Coding |
| 9 | Convolutional neural networks I | Paper |
| 10 | Convolutional neural networks II | Coding, paper |
| — | Christmas break | — |
| 11 | Recurrent neural networks | Coding, paper |
| 12 | Word embeddings | Paper |
| 13 | Transformers | Coding, paper |
| 14 | Pretrained models, autoencoders, GANs | — |
| 15 | Graph neural networks, interpretability, recap | — |

Weeks 1–2 are tooling; 3–8 the core, one optimiser and one model taken apart; 9–13 architectures in the order they were invented; 14–15 breadth.

## How the Course Is Assessed
- **Workload:** 1 ECTS ≈ 30 hours. Two identical Thursday sessions, 12:15–13:45 and 14:15–15:45, SR 029 (WIWI); one group in Stud.IP.
- **Homework is not graded.** It is the learning mechanism, not an assessment.
- **In-class tests do not affect the final grade.** Retrieval practice improves learning (Roediger et al., 2011); the tests double as exam preparation. The schedule notes "Test 1" and "Test 2" without legible weeks.
- **Timing:** do the homework the day after the exercise, while the worked examples are fresh.
- **Questions:** in class anytime; afterwards the non-anonymous Stud.IP forum, preferred over email.
- **Final exam: written, 90 minutes** (established by lecture 1, not by the exercise-1 sheet). No prerequisites to participate, no bonus. It covers everything from lectures *and* exercises, may contain some coding, and **explicitly includes the first and the last lecture**. A resit is offered before the next semester. The date is not yet announced.

> **The two schedules disagree.** The table above is the 15-*week* plan from exercise 1. Lecture 1's
> "Course Overview (tentative)" gives 15 *dated sessions* with a different topic mapping
> (Introduction; Foundations of ML ×2; Single-Layer NN ×2; Multi-Layer NN ×3; CNN ×2; RNN;
> Language Models; Transformers; Generative Models; Explainability & Wrap-up). Both are recorded;
> which one the exam follows is not stated. See [[introduction-to-deep-learning-lecture-1]].

## Dependency Map
| Layer | Weeks | Needs |
|-------|-------|-------|
| Python, `uv`, Jupyter | 1 | — |
| PyTorch tensors, autograd | 2 | Python |
| Gradient descent, metrics | 3 | PyTorch |
| Autodiff, SGD | 4 | gradient descent |
| MLP, losses, activations, init, optimizers | 5–8 | SGD |
| CNN I–II | 9–10 | MLP |
| RNN, embeddings, transformer | 11–13 | sequence modelling, then attention |
| Pretrained, autoencoders, GANs | 14 | CNN/transformer backbones |
| GNN, interpretability | 15 | all of the above |

Compressed: **Python → PyTorch → gradient descent and metrics → autodiff and SGD → MLP → losses → activations and init → optimizers and regularization → CNN → RNN → embeddings → transformers → pretrained/autoencoders/GANs → GNNs and interpretability.**

## Study Strategy
Read the homework column before the session, not after. Weeks 3, 6, 9, and 12 are paper-only: the weeks where you must derive and write, which a coding-only habit leaves untested. Weeks 2, 5, and 8 are coding-only.

The mixed weeks (1, 4, 7, 10, 11, 13) are where the two skills meet: derive the update rule on paper, then implement it. Preparing for one alone covers roughly half the course; weeks 14–15, with no homework entry, are for consolidation.

## Open Questions
- The exam **date** is not stated; the format and length now are (90 minutes, written). The exam dates "will be announced as soon as possible".
- Weeks 14–15 show no homework type; real or a layout artifact is undeterminable.
- The week table above and lecture 1's dated session table disagree on the topic-to-week mapping. Both are recorded; which the exam follows is open.
- Logistics: [[introduction-to-deep-learning]]; week-1 tooling: [[python-environment-management]]; the first lecture: [[introduction-to-deep-learning-lecture-1]]; the first PyTorch session: [[introduction-to-deep-learning-exercise-2]].
