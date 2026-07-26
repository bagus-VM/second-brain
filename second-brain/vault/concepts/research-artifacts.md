---
title: "Research Artifacts"
tags: [concept, reproducibility-engineering, semester-1]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
The tangible outputs of research—source code, datasets, scripts, configurations, equipment—that are needed to verify and build upon published results.

## Core Intuition
A research paper is just a story about what you did. The artifacts are the proof. Without them, readers must take the author's word for it. With them, anyone can inspect, verify, and extend the work.

## Formal Definition / Statement
Research artifacts encompass all **author-created** materials relevant to a published result. This includes:

- **Source code**: Analysis scripts, simulation code, data processing pipelines
- **Input data**: Datasets, test cases, benchmarks, configuration files
- **Equipment descriptions**: Hardware setups, sensor specifications, lab configurations
- **Output data**: Results, logs, figures, tables
- **Documentation**: READMEs, build instructions, dependency lists
- **Environment specifications**: OS versions, library versions, Dockerfiles

The ACM considers an artifact "relevant" if it's necessary to reproduce the key results claimed in the paper.

## Key Properties / Complexity
- **Completeness**: Missing one artifact (e.g., a preprocessing script) can make the whole chain unreproducible
- **Specificity**: Artifacts should be pinned to exact versions (commit hashes, DOIs, not "latest")
- **Self-contained**: A well-packaged artifact can be understood and run by someone not involved in the original research
- **Provenance**: Clear record of how each artifact was produced

## Worked Example
For a thesis studying climate change simulations:
- Source code: The simulation model (C++ or Python)
- Input data: Historical temperature records, CO2 concentration data
- Configuration: Model parameters, grid resolution, time step
- Output data: Temperature projections, anomaly maps
- Equipment: If using specialized hardware, its specifications
- Scripts: Post-processing scripts that generate thesis figures/tables

## Common Pitfalls
- **"I'll clean it up later"**: Artifacts captured after the fact are often incomplete. Capture during the research process.
- **Only preserving final results**: Intermediate artifacts (raw data, failed experiments) may be needed for debugging or alternative analyses
- **Binary blobs without provenance**: A `.dat` file is useless without knowing its format and origin
- **Ignoring the computational environment**: Code that ran on Python 3.8 with specific library versions may fail on Python 3.12

## Connections
- [[artifact-availability]] — Artifacts must be available in archival repositories
- [[repeat-reproduce-replicate]] — Artifacts are what others use to reproduce/replicate your work
- [[reproducibility-crisis]] — Missing or inaccessible artifacts are a root cause

## Open Questions
- What's the minimum viable set of artifacts for a given research project?
- How do we balance artifact preservation effort with research output?
- Who is responsible for long-term curation of research artifacts—the author, the institution, or the community?
