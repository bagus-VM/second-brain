---
title: "Provenance in Reproducibility"
tags: [concept, reproducibility-engineering, semester-1]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---


## One-line Summary
Provenance is the documented record of where data originated, how it was transformed, and what occurred during execution — the essential audit trail that makes experiments reproducible.

## Core Intuition
One cannot reproduce what one cannot describe. Provenance captures the *who, what, when, where, and how* of an experiment's lifecycle, turning a black-box pipeline into a transparent, auditable record.

## Formal Definition / Statement
In the VisTrails framework (Freire et al.), provenance for reproducibility is decomposed into three types:

1. **Prospective provenance** — the *description* of an experiment: the specification of the workflow structure, including modules, connections, and inputs. This is the "recipe" or plan.
2. **Execution provenance** — captures information about the *actual execution* of the workflow: what occurred when the workflow was run (runtime values, intermediate outputs, errors).
3. **Version provenance** — captures the *history* of the workflow: all versions of the workflow over time, enabling comparison and rollback.

Together, these three types form a complete record: what was planned, what was done, and how it evolved.

## Key Properties / Complexity
- **Prospective provenance** is the workflow specification (the DAG of modules and connections).
- **Execution provenance** records runtime details: input parameters, intermediate data, timestamps, resource usage.
- **Version provenance** tracks the evolution of the workflow through time (diffs, branches, merges).
- All three are required for full reproducibility; retaining only the final workflow without execution history makes debugging and verification harder.

## Worked Example
A data-analysis pipeline for a genomics study:
- *Prospective provenance*: the workflow definition — "download FASTQ → align with BWA → call variants with GATK → generate report."
- *Execution provenance*: the run log — BWA used four threads, alignment took 2 h 13 m, 3.2 M reads mapped, GATK found 12 403 variants.
- *Version provenance*: the git history — v1 used Bowtie2, v2 switched to BWA after a benchmarking study, v3 added quality filtering.

## Common Pitfalls
- Recording only prospective provenance (the script) but not execution provenance (the run log), making it impossible to diagnose discrepancies.
- Losing version provenance by overwriting files instead of using version control.
- Treating provenance as optional metadata rather than a core component of the experiment.

## Connections
- [[levels-of-reproducibility]] — provenance is the mechanism that enables all three levels.
- [[workflow-reproducibility]] — workflow engines such as [[vistrails]] automate provenance capture.
- [[reproducibility-standards-bronze-silver-gold]] — higher tiers implicitly require richer provenance records.
- [[data-provenance]] — a related but narrower concept focused specifically on data lineage.

## Open Questions
- How much provenance metadata is sufficient without creating prohibitive overhead?
- Can provenance be captured automatically for all types of experiment (wet lab, field studies)?
