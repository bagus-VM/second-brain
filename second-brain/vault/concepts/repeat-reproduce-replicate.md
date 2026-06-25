---
title: "Repeat, Reproduce, Replicate"
tags: [concept, reproducibility-engineering, semester-1]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
Three distinct levels of verifying scientific results: repeating (same team/setup), reproducing (different team/same setup), and replicating (different team/different setup).

## Core Intuition
Science requires trust, but trust must be earned through verification. The three terms—repeat, reproduce, replicate—form a hierarchy of increasing independence from the original experiment. Each level adds confidence that the finding is real, not an artifact of a particular team's methods or equipment.

## Formal Definition / Statement
According to the ACM's Artifact Review and Badging terminology:

- **Repeatability** (Same team, same experiment setup): The measurement can be obtained by the same team using the same experimental setup and procedure, obtaining the same results.
- **Reproducibility** (Different team, same experiment setup): The measurement can be obtained by a different team using the same experimental setup and procedure, obtaining the same results.
- **Replicability** (Different team, different experiment setup): The measurement can be obtained by a different team using a different experimental setup and procedure, obtaining the same results.

## Key Properties
- **Repeatability** is the weakest check—only confirms internal consistency
- **Reproducibility** tests whether the procedure is documented well enough for others to follow
- **Replicability** is the strongest check—tests whether the underlying phenomenon is real regardless of how you measure it
- Each level requires more resources and effort to achieve
- The terms are sometimes used differently across disciplines (caution needed)

## Worked Example
From the exercise sheet:
- **Repetition**: Charlie discovers a glowing substance. He asks Alice to visit his lab, use his ingredients, and follow his procedure. → Same setup, same team member present.
- **Reproduction**: An environmental group obtains Nina's software, data, and equipment to check her climate simulation results. → Different team, same setup (artifacts provided).
- **Replication**: Dave bakes cookies that look like muffins. Eve follows the same recipe but bakes in her own kitchen with her own equipment. → Different team, different setup.

Bob collecting water samples from the river Inn weekly (5 samples × 4 weeks) is **repetition**—same team, same setup, repeated measurements.

## Common Pitfalls
- **Confusing reproduce and replicate**: The terms are often swapped in everyday language. In the ACM framework, "reproduce" uses the same setup while "replicate" uses a different one.
- **Assuming repeatability is enough**: A result that only the original team can produce has limited scientific value.
- **Ignoring setup details**: If the experimental setup isn't fully documented, true reproducibility (different team, same setup) becomes impossible.
- **Different definitions across fields**: Some disciplines use "replication" where ACM uses "reproducibility." Always clarify which framework is being used.

## Connections
- [[reproducibility-crisis]] — Many published results fail reproducibility, motivating the entire field
- [[artifact-availability]] — A prerequisite for reproducibility: others need access to your artifacts
- [[research-artifacts]] — The materials (code, data, equipment) that must be shared for reproduction/replication
- [[types-of-reproducibility]] — Different kinds of reproducibility (computational, empirical, statistical)

## Open Questions
- How do these definitions apply when the "same setup" involves complex software environments (e.g., specific library versions, OS)?
- Is replicability always the goal, or are there cases where reproducibility is sufficient?
- How should we handle non-deterministic experiments (e.g., ML training with random seeds)?
