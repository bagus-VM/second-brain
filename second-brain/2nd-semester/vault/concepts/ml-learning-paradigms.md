---
title: "ML Learning Paradigms and the AI/ML/DL Distinction"
tags: [concept, ml-security, semester-2, ml-basics]
course: "Machine Learning for Cybersecurity"
source_count: 1
status: current
last_updated: 2026-10-19
prerequisites: ["[[ml-task-taxonomy]]"]
---

## One-line Summary

L1 splits machine learning two ways: vertically into AI ⊃ ML ⊃ DL, and horizontally into six training paradigms that differ in where the learning signal comes from.

## Core Intuition

A model needs a source of error signal. Supervised learning takes it from labels a human attached; unsupervised learning invents one from the data's own structure; reinforcement learning takes it from an environment that rewards and punishes; active learning decides *which* labels to buy; ensemble learning averages away many weak models. The paradigm determines what you can promise: a labelled model can be scored on accuracy, an unlabelled one cannot.

In security the paradigm is usually forced by the data, not chosen: labels are the scarce resource. Malware samples need analysis; user behaviour has no ground truth at all.

## Formal Definition / Statement

| Term | Definition on the slide |
|---|---|
| **Artificial Intelligence (AI)** | a broad concept, the science of making things "smart", i.e. making machines perform human tasks |
| **Machine Learning (ML)** | an approach to AI using a system that learns from experience; it recognises patterns from examples rather than explicit programming; if a system decides from data rather than algorithms and can change its behaviour, it is ML |
| **Deep Learning (DL)** | a set of *techniques for implementing* ML, usually based on multi-layered artificial neural networks |

ML ⊂ AI; DL ⊂ ML techniques. The slide adds that ML is "intended not only for AI" — it also reduces effort on ordinary tasks.

| Paradigm | Slide label | Learning signal |
|---|---|---|
| **Supervised** | "task-driven approach" | a labelled dataset (e.g. files plus *is it malware?*); the model decides about new data |
| **Unsupervised** | "data-driven approach" | no labelled data; the model must "somehow mark" the data, e.g. find anomalies — *generally more powerful, less precise* |
| **Semi-supervised** | — | combines supervised and unsupervised approaches |
| **Reinforcement** | "environment-driven approach" | the model must learn environment properties and react to a changing environment |
| **Active learning** | — | actively selecting which data items to label |
| **Ensemble learning** | — | combining different simple models; an extension of supervised learning (random forest pictured) |

## Key Properties

- **The paradigms are orthogonal to the tasks.** Any task on [[ml-task-taxonomy]] can be approached supervised or unsupervised; what changes is the data requirement and the evaluation.
- **"More powerful, less precise" is the lecture's own trade-off** for unsupervised learning. It finds things nobody labelled, but cannot confirm that what it found is what you wanted.
- **Labels cost money, and active learning admits it.** Rather than labelling a random sample, the model asks for the items where a label buys most.
- **Reinforcement learning assumes a responsive environment.** The slide gives it no security example — security environments are adversarial and non-stationary, so the environment moves while you learn.
- **Ensembles reduce variance; they are not a new task.** Random forest is the canonical case.

## Worked Example

**Spam filtering (supervised).** LingSpam ships with spam/ham labels; the classifier trains on them and is scored on held-out mail — the L2 exercise.

**User behaviour (unsupervised).** L1 states that user behaviour is "a complex layer and an unsupervised learning problem": as a rule there is no labelled dataset and no idea what to look for. The model flags outliers — an unusual login time — and accepts that outliers are not necessarily threats.

**Malware triage (active).** A sandbox produces thousands of unlabelled samples a day; an analyst can label a few dozen. Active learning picks the samples nearest the boundary, so analyst hours buy the most separation.

## Common Pitfalls

- **Treating the three acronyms as synonyms.** A rules engine can be called AI; it is not ML, because nothing changed its behaviour based on data.
- **Assuming unsupervised is cheap.** It avoids labelling cost and pays in precision and explainability.
- **Forgetting that a supervised security model only knows past attacks.** Its labels describe what was seen — the root of the adversarial-ML topic later.
- **Reading "ensemble" as "better".** It reduces variance at the cost of interpretability — which matters when a decision must be justified to an analyst.

## Connections

- [[ml-task-taxonomy]] — what the model outputs; this page is how it is trained.
- [[ml-for-security-domains]] — which paradigm each domain forces.
- [[naive-bayes-text-classification]] — supervised learning with a generative assumption.
- [[classification-metrics]] — the evaluation a labelled paradigm permits.

## Open Questions

- Security examples exist for only two paradigms (supervised spam, unsupervised user behaviour). Reinforcement learning is asserted as "environment-driven" with no example — is one expected?
- Active learning is one line long; whether a specific acquisition strategy is examinable is unstated.
