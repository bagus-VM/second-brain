---
title: "Computational Reproducibility in Machine Learning"
tags: [concept, reproducibility-engineering, semester-1]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

# Computational Reproducibility in Machine Learning

## One-line Summary
Machine learning experiments face unique reproducibility challenges -- stochastic training, hardware-dependent floating-point behaviour, and complex dependency chains -- that require deliberate standards and practices to overcome.

## Core Intuition
ML models are not just code; they are products of code + data + hardware + random seeds + hyperparameters. Changing any one of these can change the result. Reproducibility in ML means controlling *all* of these factors, not just sharing the script.

## Formal Definition / Statement
Heil et al. (2021) argue that "for machine-learning models in the life sciences to become *trusted*, scientists must prioritize computational reproducibility." The core problem: most ML papers only *report* results (narrative reproducibility), but do not provide enough information to independently *recompute* them (computational reproducibility). The gap between these two is the reproducibility crisis in ML.

Key challenges:
1. **Stochasticity**: random initialisation, data shuffling, dropout -- results vary across runs.
2. **Hardware dependence**: GPU floating-point non-determinism, different CUDA versions.
3. **Dependency complexity**: deep learning stacks have hundreds of transitive dependencies.
4. **Compute cost**: reproducing a large ML experiment may require expensive GPU clusters.

## Key Properties
- **Narrative vs computational reproducibility**: reporting results ≠ enabling re-computation.
- **Hardware problem**: even with identical code and data, different GPU architectures may produce slightly different results due to non-deterministic floating-point operations.
- **Compute-intensive reproducibility**: the article recommends providing pre-computed intermediate results for expensive analyses.
- **Badging**: journals can award reproducibility badges to incentivise sharing -- a sociological solution to a technical problem.

## Worked Example
A team trains a BERT-based classifier for clinical text:
- They publish the model, code, and data (Bronze).
- But they trained on 8×A100 GPUs for 3 days -- most readers cannot replicate this.
- Solution: provide the trained model weights, pre-computed predictions, and a lightweight evaluation script that runs on a laptop. This achieves functional reproducibility of the *results* even if full *re-training* is impractical.

## Common Pitfalls
- Assuming "works on my machine" is reproducible.
- Not fixing random seeds (Python, NumPy, PyTorch/TensorFlow, CUDA).
- Ignoring hardware non-determinism in floating-point operations.
- Sharing code without specifying the exact hardware (GPU model, driver version) used.

## Connections
- [[reproducibility-standards-bronze-silver-gold]] -- the tiered standards were designed to address ML-specific challenges.
- [[levels-of-reproducibility]] -- ML experiments often achieve high availability but low confirmability due to compute costs.
- [[workflow-reproducibility]] -- ML pipelines benefit from workflow automation for reproducibility.
- [[provenance-in-reproducibility]] -- tracking hyperparameters, seeds, and hardware is execution provenance.

## Open Questions
- How do we handle the trade-off between full re-training reproducibility and practical compute budgets?
- Should journals require Gold-level reproducibility for ML papers?
- Can containerisation (Docker, Singularity) fully solve the hardware-dependence problem?
