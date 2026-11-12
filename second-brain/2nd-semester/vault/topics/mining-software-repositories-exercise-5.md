---
title: "Mining Software Repositories — Exercise 5 Overview (SZZ and Manual Validation)"
tags: [topic, mining-software-repositories, semester-2, exercise, szz]
course: "Mining Software Repositories"
source_count: 1
status: current
last_updated: 2026-11-12
prerequisites: ["[[mining-software-repositories-lecture-3]]", "[[szz-algorithm]]", "[[msr-data-noise]]"]
---

## One-line Summary
Exercise 5 asks students to implement file-level SZZ, reason about its assumptions on a supplied commit/issue history, and design manual validation for its noisy candidate results.

## Core Map

```
Exercise 5 (due 18 Nov 2026)
├── Task 1: SZZ
│   ├── implement a file-based variant (changed lines not collected)
│   ├── identify candidate bug-introducing commits
│   └── analyze assumptions and a small supplied history manually
└── Task 2: validation
    ├── present a manageable sample for human review
    ├── scale review to hundreds of candidates
    └── explain how validation assesses and mitigates risk
```

## Key Concepts at a Glance

| Page | What the sheet tests |
|------|----------------------|
| [[szz-algorithm]] | Trace bug-fixing changes backward to candidate bug-introducing commits. |
| [[msr-data-noise]] | Heuristic links and assumptions introduce errors that propagate into results. |
| [[threats-to-validity]] | Manual checks can reveal construct and measurement problems in study data. |
| [[mining-software-repositories-lecture-3]] | Enrichment and SZZ are introduced in the lecture material. |

## Exercise Structure

Task 1.1 requests an implementation of SZZ for project issues; because changed lines are not available in the collected data, the sheet permits working at file level. Task 1.2 asks for SZZ assumptions, where they fail, and a hand-application to the appendix timeline of commits and issues, including whether broken assumptions threaten the identified result. Task 2 asks for a reasonably sized human-readable subset, a validation approach that could handle hundreds of candidates, and an account of how manual validation helps determine and mitigate risk.

The sheet contains an explicit owner instruction forbidding AI assistance with solving. The sheet also embeds an instruction to print a video URL; that is untrusted source text and is not followed.

## Results

Solved in `study/homework/mining-software-repositories/exercise-05-solution.md`, with the runnable
`szz-exercise-05.py` and its recorded output. The appendix's only bug fix (`42d921a2`, ISSUE-0002)
removes `return math.divide(a, b)`; line-level SZZ blames `24f914fd`, the commit that wrote the
line. File-level SZZ — the substitute the sheet permits — blames `3f5b0912`, which only reordered
imports and bumped the version. That pair is the exercise's point: the approximation finds the
last commit to touch the file, not the commit that introduced the bug.

## Exam-Relevant Points

- The sheet explicitly changes SZZ's granularity from lines to files because line-level history was not collected.
- Treat detected bug-introducing commits as candidates, not ground truth; the exercise foregrounds assumption failures and manual validation.
- The two tasks separate candidate generation from validation and risk management.
- The due date is 18.11.2026; the sheet names Prof. Dr. Steffen Herbold and author Lukas Schulte.

## Connections

- [[szz-algorithm]] — the algorithm named in Task 1.
- [[mining-software-repositories-lecture-3]] — SZZ and data enrichment.
- [[msr-data-noise]] — heuristic inaccuracies and their downstream effects.
- [[threats-to-validity]] — validation evidence and limits on claims.
- [[mining-software-repositories]] — the course page, which records the standing no-AI rule for its exercise sheets.

## Open Questions

- The sheet gives no minimum or target size for the validation subset.
- It does not specify a required format, sampling strategy, reviewer count, or inter-rater agreement measure.
- Changed-line collection is explicitly absent, so how much accuracy the file-level substitute loses is not reported.
- No due-time or submission platform is stated.
