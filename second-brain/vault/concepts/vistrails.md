---
title: "VisTrails"
tags: [concept, reproducibility-engineering, semester-1]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

# VisTrails

## One-line Summary
VisTrails is a scientific workflow management system that provides integrated provenance capture, version control, and visualisation to support [[workflow-reproducibility]].

## Core Intuition
Most workflow tools let you build and run pipelines. VisTrails adds a critical extra layer: it automatically tracks every change you make to a workflow (version provenance) and records exactly what happened during each execution (execution provenance), making the full history of your experiment accessible and reproducible.

## Formal Definition / Statement
VisTrails (Freire & Silva) is an open-source system that combines:
- Workflow creation and execution (visual programming interface).
- Automatic [[provenance-in-reproducibility]] capture (prospective, execution, and version).
- A version-tree visualisation showing the evolution of workflows.
- Support for multiple computational backends (VTK, matplotlib, R, etc.).

It was designed to address the problem that scientists iterate on workflows many times but typically only keep the final version, losing valuable exploratory history.

## Key Properties / Complexity
- **Version tree**: a DAG of workflow versions, enabling comparison and rollback.
- **Change-based provenance**: records diffs between workflow versions, not just snapshots.
- **Mashups**: lightweight "apps" that parameterise workflows for non-expert users.
- **Open source**: freely available, though the project's current maintenance status is debated (as of the exercise sheet, the answer is likely "No" -- the project is no longer actively maintained).

## Worked Example
A researcher creates a visualisation pipeline in VisTrails:
- v1: load data → plot scatter.
- v2: add normalisation step before plotting.
- v3: switch from scatter to heatmap.

VisTrails stores the version tree, so the researcher can compare v1 vs v3 outputs, or re-run v2 with different parameters. All execution results are cached.

## Common Pitfalls
- Assuming VisTrails solves environment reproducibility (it captures workflow structure, not OS-level dependencies).
- Confusing version provenance with git -- VisTrails versions are workflow-level, not file-level.
- The tool's niche adoption means community support may be limited.

## Connections
- [[workflow-reproducibility]] -- VisTrails is a concrete implementation of workflow reproducibility principles.
- [[provenance-in-reproducibility]] -- VisTrails captures all three provenance types.
- [[levels-of-reproducibility]] -- VisTrails was used in the paper that defined the three levels framework.

## Open Questions
- Is VisTrails still usable for new projects, or has it been superseded by tools like Nextflow, Snakemake, or Pachyderm?
- How does its provenance model compare to W3C PROV?
