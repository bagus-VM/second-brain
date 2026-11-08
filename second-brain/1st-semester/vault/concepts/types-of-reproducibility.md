---
title: "Types of Reproducibility"
tags: [concept, reproducibility-engineering, semester-1]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
Reproducibility comes in distinct flavors—computational, empirical, and statistical—each requiring different strategies to achieve.

## Core Intuition
"Reproducibility" isn't one thing. A computational experiment (running a script) faces different challenges than an empirical one (measuring physical samples) or a statistical one (re-deriving results from the same data). Understanding which type you're dealing with determines what tools and practices you need.

## Formal Definition / Statement
Three commonly distinguished types:

- **Computational reproducibility**: Can someone else re-run your code on your data and get the same output? This is the most achievable form—it requires code, data, and environment to be preserved.
- **Empirical reproducibility**: Can someone else collect new data using the same methods and get consistent results? This involves physical measurements, surveys, or field work.
- **Statistical reproducibility**: Are the statistical conclusions robust? This involves proper study design, adequate sample sizes, and correct analysis methods (avoiding p-hacking, multiple comparisons issues, etc.).

Some frameworks also distinguish:
- **Methodological reproducibility**: Are the methods described in enough detail to be followed?
- **Robustness reproducibility**: Do the conclusions hold under different reasonable analysis choices?

## Key Properties / Complexity
- **Computational reproducibility** is the most tractable in CS—tools like Docker, version control, and dependency management can solve most issues
- **Empirical reproducibility** is harder because physical conditions vary—requires careful protocol documentation
- **Statistical reproducibility** requires understanding of study design and inference—pre-registration helps
- **All three are needed** for full confidence in a result
- **Progressive difficulty**: Computational < Statistical < Empirical (in terms of engineering solutions)

## Worked Example
A CS Master's thesis on a new sorting algorithm:
- **Computational**: Can I re-run the benchmark script and get the same timing numbers? (Needs: code, data, hardware specs, random seeds)
- **Statistical**: Are the performance differences statistically significant with proper tests? (Needs: multiple runs, appropriate tests, corrected p-values)
- **Empirical**: If someone runs the algorithm on a different dataset, does the advantage hold? (Needs: algorithm description, alternative benchmarks)

## Common Pitfalls
- **Focusing only on computational reproducibility**: Code that runs but produces statistically unsound results is reproducibly wrong
- **Assuming deterministic execution**: Floating-point arithmetic, thread scheduling, and I/O can introduce non-determinism
- **Conflating reproducibility with correctness**: A result can be perfectly reproducible and still be wrong
- **Ignoring the statistical dimension**: Running an experiment once and reporting a number is not enough—need variance estimates

## Connections
- [[repeat-reproduce-replicate]] — The three R's describe WHO and HOW; this page describes WHAT is being reproduced
- [[reproducibility-crisis]] — The crisis manifests differently across these types
- [[artifact-availability]] — Different artifact types support different kinds of reproducibility
- [[research-artifacts]] — The materials needed vary by reproducibility type

## Open Questions
- In machine learning, is computational reproducibility even achievable given GPU non-determinism?
- How do we handle reproducibility for research that involves human subjects?
- Should different types of reproducibility have different requirements in the publication process?
