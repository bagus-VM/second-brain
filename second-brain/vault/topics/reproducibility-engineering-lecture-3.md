---
title: "Reproducibility Engineering – Lecture 3: Hypotheses"
tags: [topic-overview, reproducibility-engineering, semester-1]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

# Reproducibility Engineering – Lecture 3: Hypotheses

## One-line Summary
How to formulate testable research hypotheses and structure experiments for reproducible science.

## Core Intuition
A good hypothesis is the backbone of reproducible research. If a claim is vague or untestable, no experiment can confirm or refute it—and others cannot reproduce the work. Zobel's guidelines (from *Writing for Computer Science*) emphasize that hypotheses must be **precise**, **specific**, and **unambiguous**, while making clear what is *not* being claimed.

## Key Concepts

### Hypothesis Formulation
- [[hypothesis-formulation]] — Properties of a good hypothesis and Zobel's guidelines.
- A good hypothesis is: PRECISE, SPECIFIC, UNAMBIGUOUS, states its LIMITATIONS.
- A bad hypothesis is: LOOSE, CONTRADICTORY.

### Presenting Experiments
- [[presenting-experiments]] — detailed guide on structuring experiments sections (setup → results → discussion)
- Typical structure: **Setup → Results → Discussion**.
- Setup: datasets, baselines, evaluation metrics.
- Results: what the data shows (with figures).
- Discussion: interpretation, limitations, context.

### Levels of Equivalence
- [[levels-of-equivalence]] — Bitwise identity, structural equivalence, functional equivalence, behavioral equivalence.
- Critical for comparing computational experiments and determining if two implementations are "the same."

### Comparing Methods
- Requires careful use of comparatives, adverbs, and clear metrics.
- Statistical comparison is non-trivial—single runs are insufficient.

## Connections
- [[reproducibility-crisis]] — Poor hypothesis testing contributes to the crisis.
- [[repeat-reproduce-replicate]] — Hypotheses guide what counts as a successful replication.
- [[computational-reproducibility-in-ml]] — Equivalence levels matter for ML reproducibility.
- [[research-artifacts]] — Hypotheses shape what artifacts are needed.

## Source
- In-Class Exercise Sheet 3, Reproducibility Engineering, Summer 2026, Prof. Scherzinger.
- Based on Justin Zobel, *Writing for Computer Science*, chapter on "Hypotheses, Questions, and Evidence."
