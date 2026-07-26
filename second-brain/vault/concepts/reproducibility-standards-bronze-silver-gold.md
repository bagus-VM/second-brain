---
title: "Reproducibility Standards: Bronze, Silver, Gold"
tags: [concept, reproducibility-engineering, semester-1]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

# Reproducibility Standards: Bronze, Silver, Gold

## One-line Summary
A tiered framework (Bronze / Silver / Gold) from Heil et al. (2021) that defines progressively stricter reproducibility standards for machine learning in the life sciences.

## Core Intuition
Full reproducibility is hard. Rather than a binary pass/fail, the Bronze/Silver/Gold model gives researchers achievable milestones: start by sharing data and code (Bronze), make it easy to re-run (Silver), and make the entire analysis deterministic and one-command reproducible (Gold).

## Formal Definition / Statement
From Heil et al. (2021), "Reproducibility standards for machine learning in the life sciences":

| Requirement | Bronze | Silver | Gold |
|---|---|---|---|
| Data published and downloadable | ✓ | ✓ | ✓ |
| Models published and downloadable | ✓ | ✓ | ✓ |
| Source code published and downloadable | ✓ | ✓ | ✓ |
| Dependencies set up in a single command | | ✓ | ✓ |
| Key analysis details recorded | | ✓ | ✓ |
| Analysis components set to deterministic | | | ✓ |
| Entire analysis reproducible with a single command | | | ✓ |

**Bronze**: the raw materials (data, code, models) are available.
**Silver**: dependencies and key parameters are documented so setup is frictionless.
**Gold**: the full pipeline is deterministic and reproducible with a single command.

## Key Properties / Complexity
- **Progressive**: each tier subsumes the previous one.
- **Practical**: focuses on what a third party needs to *actually re-run* the experiment.
- **Life sciences focus**: designed for ML in biomedical research, but applicable broadly.
- **Single-command ideal**: the Gold standard eliminates manual setup steps.

## Worked Example
A deep learning model for medical image classification:
- *Bronze*: authors upload the trained model weights, training dataset (on Zenodo), and Python scripts (on GitHub). A reader can download and inspect them.
- *Silver*: a `requirements.txt` or `environment.yml` is provided; running `pip install -r requirements.txt` sets up all dependencies. Key hyperparameters are documented in the README.
- *Gold*: a single `make reproduce` or `./run.sh` command trains the model from scratch, evaluates it, and generates all paper figures. Random seeds are fixed for determinism.

## Common Pitfalls
- Stopping at Bronze (publishing code) without documenting dependencies -- the code is "available" but not runnable.
- Assuming Gold is always achievable -- some experiments depend on non-deterministic hardware (GPUs, distributed systems).
- Confusing "code available" with "reproducible" -- a GitHub repo without documentation is Bronze at best.

## Connections
- [[levels-of-reproducibility]] -- the tiers operationalise the availability/repeatability/confirmability dimensions.
- [[computational-reproducibility-in-ml]] -- the standards were designed specifically for ML reproducibility challenges.
- [[workflow-reproducibility]] -- the Gold standard's "single command" requirement is a workflow reproducibility goal.
- [[provenance-in-reproducibility]] -- Silver and Gold tiers implicitly require rich provenance records.

## Open Questions
- Should there be a "Platinum" tier that includes formal verification or guaranteed containerised environments?
- How do the tiers generalise beyond the life sciences to other ML domains?
- What role should badging play as an incentive mechanism?
