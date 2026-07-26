---
title: "Artifact Availability"
tags: [concept, reproducibility-engineering, semester-1]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
The ACM requirement that research artifacts (code, data, etc.) be placed in a publicly accessible archival repository with a DOI.

## Core Intuition
You can't reproduce what you can't access. Artifact availability is the foundational prerequisite for any form of reproducibility. Without access to the original software, data, and equipment, other researchers are left guessing at what was actually done.

## Formal Definition / Statement
The ACM defines **Artifact Availability** as:

> "Author-created artifacts relevant to this paper have been placed on a publicly accessible archival repository. A DOI or link to this repository along with a unique identifier for the object is provided."

Key requirements:
- **Publicly accessible**: Not behind a paywall or institutional login
- **Archival repository**: A stable, long-lived platform (e.g., Zenodo, Figshare, institutional repositories)—not a personal website that might disappear
- **DOI or persistent identifier**: Ensures the artifact can be cited and found even if the hosting platform changes
- **Unique identifier**: Specific version of the artifact, not just a general project page

## Key Properties / Complexity
- **Distinguish from "available on request"**: Artifacts must be proactively shared, not just promised
- **Version-specific**: The artifact should correspond to the exact version used in the paper
- **Includes metadata**: Description, licence, dependencies, how to run
- **Enables badges**: ACM awards badges (Artifacts Available, Artifacts Evaluated, Results Reproduced) to incentivize sharing

## Worked Example
For a Master's thesis on a machine learning system:
- Upload code + data to **Zenodo** (generates a DOI)
- Include a README with build/run instructions
- Document the exact commit hash used for the paper's experiments
- Provide a `requirements.txt` or `Dockerfile` for environment setup
- The Zenodo DOI (e.g., `10.5281/zenodo.123456`) goes in the thesis

## Common Pitfalls
- **GitHub is not archival**: Repositories can be deleted. Use Zenodo or Figshare for DOI-backed archival.
- **Data without code (or vice versa)**: Both are needed for computational reproducibility
- **Undocumented artifacts**: Just dumping files in a repo isn't useful without instructions
- **Sensitive data**: Some data can't be shared (privacy, ethics). Must document what can and cannot be made available, and why.

## Connections
- [[repeat-reproduce-replicate]] — Reproducibility and replicability both require artifact availability
- [[research-artifacts]] — What counts as an "artifact" and what to preserve
- [[reproducibility-crisis]] — Lack of artifact sharing is a major contributor to the crisis

## Open Questions
- How do we handle artifacts that depend on proprietary software or hardware?
- What's the right balance between openness and protecting sensitive data?
- Should artifact availability be mandatory for graduation or just encouraged?
