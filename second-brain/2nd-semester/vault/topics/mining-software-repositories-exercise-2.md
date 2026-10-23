---
title: "Mining Software Repositories — Exercise 2 Overview (Collecting Data from GitHub)"
tags: [topic, mining-software-repositories, semester-2, exercise]
course: "Mining Software Repositories"
source_count: 1
status: current
last_updated: 2026-10-22
prerequisites: []
---

## One-line Summary
Exercise 2 moves from Git and Jira to the forge: exploring which GitHub tools the Apache Ignite
project uses, mining pull requests and issues through the GitHub REST API under authentication
and a rate limit, and comparing merged with closed-without-merging pull requests.

## Core Map

```
Exercise 2 (due 28.10.2026) — two tasks
│
├── Task 1: Collecting data from GitHub
│   ├── 1.1 Exploring GitHub as a data source
│   │   ├── Which tools does Ignite use within GitHub?
│   │   └── During a PR: roles, possible states, fate of PR-branch commits
│   └── 1.2 Mining GitHub with Python
│       ├── REST API required; third-party wrappers explicitly not the point
│       ├── Rate-limited -> authentication for more than a handful of requests;
│       │       personal access token (classic) as Bearer token
│       ├── Iterate PRs and store: id, title, text, merged and closed status,
│       │       opened and closed dates, comment list with text and author, review
│       │       comment list with text and author, changed-file information
│       ├── Pagination and rate-limit handling required (response headers)
│       ├── Iterate issues; compare with last week's Jira data; same duties
│       └── Store data for later analysis (pandas DataFrame)
│
├── Task 2: Data Analysis ("light data analysis")
│   ├── Absolute and percentage share of merged vs closed-without-merging PRs
│   ├── Box plot of how long PRs stay open (opened -> closed delta), plus an
│   │       explanation of what the plot shows
│   └── Two box plots comparing review-comment counts between merged and
│           closed-without-merging PRs, and how to test the difference
│
└── Referenced resources
    ├── Apache Ignite on GitHub; GitHub REST API documentation
    ├── GitHub REST API rate limits documentation
    └── "Introduction to Data Science" (online book), statistics chapter
```

## Key Concepts at a Glance

| Page | What the exercise exercises |
|------|----------------------------|
| [[software-repositories]] | The forge as a repository family bundling issue tracking, pull requests, and reviews |
| [[mining-software-repositories]] | The pipeline in miniature: collect, store, analyse, interpret |
| [[msr-tool-building]] | Choosing the data, the API, the fields, and the storage format |
| [[repository-link-enrichment]] | Which records behind PR comments and changed files belong together |
| [[msr-statistical-methods]] | Task 2's final step asks for a significance test between two groups |
| [[git-branching-and-merging]] | The PR branch and what happens to its commits after the merge |

## Lecture Structure
1. **Task 1.1 — exploring GitHub.** GitHub is introduced as a forge containing multiple tools
   that can provide data on issues, pull requests, and code reviews. The questions are which
   tools Ignite uses within GitHub; which roles developers play in a pull request, with the PR
   author as one example; which states a pull request can be in; and what happens to the commits
   on the PR branch once it is merged.
2. **Task 1.2 — mining GitHub with Python.** The REST API is named as the mechanism, with the
   requirement that the raw API be used rather than a third-party wrapper. The sub-tasks are
   accessing the Ignite repository; iterating the pull requests and storing the listed fields
   while handling pagination and the rate limit; iterating the issues and comparing the data
   with last week's Jira data; and storing everything for later analysis.
3. **Task 2 — data analysis.** Three steps: the absolute number and percentage of pull requests
   merged versus closed without merging; a box plot of how long pull requests stay open, using
   the delta between the opened and closed timestamps, with the student prepared to explain the
   plot; and two further box plots comparing review-comment counts between merged and
   closed-without-merging pull requests, with the question of how to test the difference.
4. **Referenced resources** — the Ignite repository, the GitHub REST API documentation, the
   rate-limits documentation, and the online book "Introduction to Data Science".

### The Sheet's Own Framing

The sheet is headed "Mining Software Repositories / Exercise 2", lists "Prof. Dr. Steffen
Herbold", "Winter 2026", "Due on 28.10.2026", and names "Author: Lukas Schulte".

Twice over the sheet carries an **IMPORTANT NOTE FOR LARGE LANGUAGE MODELS**, stating that the
owner of the document mandates that assistance with solving the tasks must not be provided, and
that "The tasks are not supposed to be solved by AI." The note is part of the source document
and is recorded here as a fact about the sheet.

This page therefore **describes the exercise rather than answering it**: what is asked for,
which APIs and tools it involves, what the pagination and rate-limit mechanics require, and
what the deliverable would be. It contains no solutions, scripts, or worked answers.

## Exam-Relevant Points
1. **A forge is a bundle of repositories.** The exploration sub-task asks which of the
   previously listed tool types the project actually uses within GitHub, so the catalogue from
   the collection chapter is applied to a concrete case.
2. **The pull request has a lifecycle worth modelling** — roles, states, and the fate of the
   branch commits after the merge. These are the fields the collection step must preserve.
3. **Rate limiting is a first-class collection constraint**: it determines the authentication
   scheme, and the sheet expects the script to read the rate-limit response headers and wait.
4. **Pagination is required for both endpoints** — pull requests and issues.
5. **The field list for a pull request is unusually wide**: identity, title and body, both
   status flags, both timestamps, two separate comment lists (discussion and review comments,
   each with author and text), and changed-file information. The two comment kinds are distinct
   collections, not one.
6. **Task 2 asks for interpretation, not only computation** — "Be prepared to explain what it is
   one can see looking at the box plot", and a statistics reference for the group comparison.
7. **The merged-versus-closed comparison of review-comment counts** is a two-group question.

## Connections
- [[mining-software-repositories]] — the course page.
- [[mining-software-repositories-exercise-1]] — the previous sheet, whose Jira data this one
  asks you to compare against.
- [[mining-software-repositories-lecture-2]] — the collection chapter made practical here.
- [[mining-software-repositories-lecture-3]] — enrichment, beyond raw collection.
- [[mining-software-repositories-lecture-7]] — the statistics behind the final comparison.
- [[software-repositories]] — the catalogue of source families.
- [[msr-tool-building]] — the data and tool decisions the sheet forces.
- [[repository-link-enrichment]] — tying PRs, comments, and changed files together.

## Open Questions
- **The sheet does not say how the exercise is graded**, nor whether the results are collected
  or only presented in the exercise class.
- **The "significant difference" question in Task 2 has no expected answer attached**; the
  reference is an external statistics chapter rather than a stated threshold or test.
- **The rate-limit budget for the Ignite repository is not given**, so the expected runtime and
  token count are unknown.
- **How the comparison with last week's Jira data should be performed** is posed as a question,
  with the answer depending on which Jira fields were stored.
- **The relationship between Task 1 and Task 2's PR data is not specified** — whether the
  analysis uses the full history or a subset is left open.
