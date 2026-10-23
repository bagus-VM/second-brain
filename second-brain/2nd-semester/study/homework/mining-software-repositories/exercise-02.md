---
title: "Mining Software Repositories — Exercise 2: mining GitHub PRs and issues"
tags: [homework, mining-software-repositories, semester-2, msr]
course: "Mining Software Repositories"
source_count: 1
status: current
last_updated: 2026-10-22
prerequisites: []
---

# Exercise 2 (due 28.10.2026) — Collecting data from GitHub

> **No AI-written solution is provided for this exercise, on purpose.**
> The sheet carries an instruction from its owner, addressed to large language models, that it
> must not be assisted, and states that *"the tasks are not supposed to be solved by AI."* What
> follows is the **task sheet, the API mechanics and the method notes** — and deliberately **not**
> the working scripts and the resulting analysis.
>
> This is recorded explicitly so that a future session does not "helpfully" fill the gap.

## What the exercise asks

**Task 1 — Collecting data from GitHub.**

1. *1.1 Exploring GitHub as a data source.* GitHub is a forge that contains multiple tools giving
   data about issues, pull requests and code reviews. Using the Apache Ignite project:
   - Which tools does the Ignite project use within GitHub?
   - Focusing on what happens during a PR: in which roles do developers participate (one example
     is the author of the PR)? What are the different states a PR can be in? What happens to the
     commits made on the PR branch once it is merged?
2. *1.2 Mining GitHub with Python.* Write a script that accesses the Apache Ignite repository on
   GitHub via the **REST API** — *"using the REST API is a requirement. Using the abstract wrapper
   of a third-party library to make the requests is not the point of this exercise."* Then:
   - Iterate over the PRs and store: ID, title, text, merged status, closed status, opened and
     closed dates, the list of comments with text and author, the list of review comments with
     text and author, and information about the changed files. Mind **pagination** and **respect
     the rate limit**.
   - Iterate over the issues and store the fields you judge important. How does the data available
     differ from last week's Jira data? Again mind pagination and the rate limit.
   - Store the data in a format usable for later analysis — the sheet suggests a pandas DataFrame.

**Task 2 — Data Analysis.** Light analysis:

1. Compute the absolute number and the percentage of PRs that were merged versus closed without
   merging.
2. Draw a box plot of how long PRs stay open (opened → closed). Be ready to explain what the box
   plot shows.
3. Draw two more box plots comparing the number of review comments between merged PRs and PRs
   closed without merging. **How do you check whether there is a significant difference between
   those two sample groups?** The sheet points at the online book *Introduction to Data Science*
   for the statistics.

## The mechanics that matter

**Authentication is required.** Unlike Exercise 1's unauthenticated endpoints, GitHub's API rate
limit means that *"if we want to make more than a handful of requests, we need to use
authentication"*. The sheet's procedure: create a **personal access token (classic)** at
`https://github.com/settings/tokens`, then send it as a **Bearer token** in the authorization tab
of Postman or Hoppscotch. The exercise therefore assumes the student has a GitHub account.

**Rate limits and the wait.** The sheet's own hint: *"there are rate limit response headers."*
The headers report the limit, the remaining budget and the reset time — so the "solution to wait
until request capacity comes available again" the sheet asks for is: read the headers, and when
the budget is exhausted, sleep until the reset time rather than hammering the endpoint. A script
that ignores the headers will fail partway through a long run, and will fail *silently* if it
also ignores the error response — collecting a truncated dataset that looks complete.

**Pagination again.** Both the PR listing and the issue listing page their results.

**The statistical test.** Task 2.3 is where the course's methods chapter meets the data: the
question "is there a significant difference between these sample groups?" is the hypothesis-testing
machinery of [[msr-statistical-methods]] applied to a concrete dataset, and the sheet's pointer to
the statistics chapter of *Introduction to Data Science* is deliberate. Two things to get right:
the two groups are **independent** samples (a PR is either merged or not — this is the
between-subjects case, not the paired case), and "significant" is not "important" — the effect
size and the confidence interval are what tell you whether the difference is large enough to
matter. The lecture's own slide on this is a live example: it warns that the *correlation*
between variables does not generalise across settings even when the *cost* model does.

**Why this exercise exists at all.** The PR is the unit where social and technical facts meet:
it has an author, reviewers, a discussion thread, a set of changed files, a lifetime, and an
outcome (merged or abandoned). The lecture's social-aspects chapter builds its community smells
(organizational silos, lone wolves, black clouds, bottlenecks) from exactly this kind of data, and
the defect-prediction chapter needs to know which changes were merged and which were not. The
box plot of PR lifetime is the empirical version of the lecture's claim that code review is where
the coordination cost lives.

## Related

- [[mining-software-repositories-exercise-2]] — the topic page for this exercise.
- [[mining-software-repositories-exercise-1]] — Exercise 1, the Git and Jira half.
- [[mining-software-repositories-lecture-2]] — the data-collection lecture.
- [[msr-statistical-methods]] — the significance test and effect size that Task 2.3 asks for.
- [[developer-social-networks]] — the model of the forge as a network of developers and artefacts.
- [[community-smells]] — what the social data in this exercise is used for later.

## Open Questions

- The sheet does not specify which GitHub tools the Ignite project actually uses — that is Task
  1.1's first question, to be answered from the repository itself.
- The exact PR states, roles and merge semantics are not enumerated in the sheet; they are to be
  read off the GitHub documentation and the repository.
- No grading criteria, submission channel or expected output format are stated, and the slide's
  "Testat" mechanism is mentioned without a grade attached.
- The choice of statistical test for Task 2.3 is left to the student, with the statistics chapter
  as the reference; the sheet does not say whether a specific test is expected.
