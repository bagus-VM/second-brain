---
title: "Workflow Reproducibility"
tags: [concept, reproducibility-engineering, semester-1]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

# Workflow Reproducibility

## One-line Summary
A workflow is reproducible when its complete specification (modules, connections, inputs) and execution environment can be shared and re-executed by others to produce equivalent results.

## Core Intuition
A workflow is a formal, machine-readable description of an experiment's computational steps. If the workflow is fully specified and the environment is captured, anyone can re-run it -- making the experiment reproducible by construction rather than by manual effort.

## Formal Definition / Statement
A computational workflow is a directed acyclic graph (DAG) of processing modules connected by data dependencies. Workflow reproducibility requires:
1. The workflow specification (prospective provenance) is complete and unambiguous.
2. All inputs and parameters are recorded.
3. The execution environment (dependencies, OS, hardware) is documented or containerised.
4. The workflow can be re-executed to produce identical or equivalent outputs.

Tools like [[vistrails]] automate the capture and management of all these components.

## Key Properties / Complexity
- **Explicit structure**: every step and data flow is declared, not implicit.
- **Automation**: reduces human error compared to manual re-execution scripts.
- **Composability**: workflows can be shared, extended, and combined.
- **Provenance integration**: workflow engines automatically record [[provenance-in-reproducibility]] during execution.

## Worked Example
A machine learning experiment workflow:
1. Load dataset (CSV) → 2. Preprocess (normalise, split) → 3. Train model (scikit-learn) → 4. Evaluate (accuracy, F1) → 5. Generate plots.

Each step is a module; the connections define data flow. The workflow engine records all parameters, random seeds, and intermediate results, enabling exact re-execution.

## Common Pitfalls
- Assuming the workflow specification alone is sufficient without capturing the environment (dependency hell).
- Hard-coding absolute paths or machine-specific settings in workflows.
- Not recording random seeds, making stochastic results non-reproducible.

## Connections
- [[provenance-in-reproducibility]] -- workflow engines capture prospective, execution, and version provenance automatically.
- [[vistrails]] -- a specific workflow management system designed for reproducibility.
- [[levels-of-reproducibility]] -- workflow sharing directly improves availability and repeatability.
- [[reproducibility-standards-bronze-silver-gold]] -- the "single command" requirement at Silver/Gold tiers is a workflow reproducibility goal.

## Open Questions
- How do we handle workflows that depend on external services or APIs that may change?
- What is the right granularity for workflow modules?
