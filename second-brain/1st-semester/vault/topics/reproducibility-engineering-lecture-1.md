---
title: "Reproducibility Engineering — Lecture 1 Overview"
tags: [topic, reproducibility-engineering, semester-1]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
Lecture 1 establishes the foundational vocabulary (repeat/reproduce/replicate), the motivation (reproducibility crisis), and the practical requirements (artifact availability) for the entire course.

## Core Map

```
                    [[reproducibility-crisis]]
                           │
                           ▼
              Why do we need reproducibility?
                           │
           ┌───────────────┼───────────────┐
           ▼               ▼               ▼
   Computational      Empirical       Statistical
   reproducibility    reproducibility  reproducibility
           │               │               │
           └───────┬───────┴───────────────┘
                   ▼
      [[repeat-reproduce-replicate]]
         Who? How? Same or different?
                   │
                   ▼
        [[research-artifacts]]
           What do we preserve?
                   │
                   ▼
      [[artifact-availability]]
         How do we share it?
```

## Key Concepts

| Concept | Why It Matters |
|---------|---------------|
| [[repeat-reproduce-replicate]] | Defines the three levels of verification; foundational vocabulary for the course |
| [[reproducibility-crisis]] | Motivates the entire field — ~90% of researchers acknowledge a crisis |
| [[types-of-reproducibility]] | Computational, empirical, and statistical each require different strategies |
| [[research-artifacts]] | The tangible outputs that enable verification |
| [[artifact-availability]] | ACM's standard for making artifacts findable and citable |

## The Big Takeaway
Reproducibility isn't a nice-to-have — it's a prerequisite for science to function. The crisis is real (52% of researchers call it significant), and the solution is systematic: define what we mean (the three R's), preserve what matters (artifacts), and share it properly (archival repositories with DOIs). This course is about the engineering practices that make this possible.

## From the Exercise Sheet
The in-class exercise tested the ability to classify scenarios as repetition, reproduction, or replication. Key pattern:
- **Same person/setup** → Repetition
- **Different person + your artifacts** → Reproduction
- **Different person + their own setup** → Replication

The exercise also asked students to reflect on their own Bachelor thesis — whether they could reproduce their own work 24 hours later. This is a powerful reality check: if you can't reproduce your own work, no one else can either.

## Connections to Future Lectures
- Version control (Git) → enables artifact preservation
- Containers (Docker) → enables computational reproducibility
- Workflow management → automates reproducible pipelines
- Data management → ensures input data is preserved
