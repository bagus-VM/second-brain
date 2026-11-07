---
title: "Mining Software Repositories — Exercise 4 Overview (Expanding, Linking and Measuring the Database)"
tags: [topic, mining-software-repositories, semester-2, exercise, metrics]
course: "Mining Software Repositories"
source_count: 1
status: current
last_updated: 2026-11-05
prerequisites: ["[[repository-link-enrichment]]", "[[software-metrics]]", "[[msr-data-noise]]"]
---

## One-line Summary
The database built in exercise 3 gets three new projects, gets *links* between issues, commits and
pull requests, and then gets interrogated — time-to-resolve, time-to-response, and bugs per file,
each of which the sheet asks you to classify against the lecture's metric taxonomy.

## Core Map

```
Exercise 4 (due 11.11.2026) — Expanding the harmonized database
│
├── Task 1 — Expanding the database
│   ├── 1.1 bring in Apache Zookeeper, Apache Superset, and one project of your
│   │       own choosing (Seart GitHub Search is the recommended way to find one);
│   │       establish how each handles commits, issues and PRs
│   └── 1.2 revisit the schema from exercise 3: does the new data fit, or does the
│           schema need adjusting? Mine it in, keeping every row traceable to its
│           source; test on a subset, then run the full import overnight
│       → [[repository-link-enrichment]] [[msr-data-noise]]
│
├── Task 2 — Linking
│   ├── link issues <-> commits, commits <-> PRs, PRs <-> issues
│   ├── the mechanism is textual: regular expressions over the patterns already
│   │   observed in the data
│   ├── implement it and store it (foreign keys, primary keys)
│   └── acceptance: a SQL query that returns all commits for an issue id
│       → [[repository-link-enrichment]] [[msr-pipeline]]
│
├── Task 3 — Metrics
│   ├── 3.1 basic: mean time to resolve (per issue type), mean time to response
│   │       to a PR by someone other than its creator — per project AND overall
│   │       └── classify both against the lecture's metric categories
│   ├── 3.2 linked: bugs per file — follow bug issues to their commits, extract
│   │       changed files, count occurrences per file; which files carry the most
│   │       bugs, which almost none, is there a pattern?
│   │       └── classify that metric too
│   └── → [[software-metrics]] [[defect-prediction]]
│
└── Recommended tools
    ├── 4.1 Seart GitHub Search (seart-ghs.si.usi.ch) — find a large project
    └── 4.2 RegEx — regexone.com tutorial, the Python reference, RegExr for testing
```

## Key Concepts at a Glance

| Page | What the sheet exercises |
|------|--------------------------|
| [[repository-link-enrichment]] | Task 2 is the concept made concrete: linking commits, issues and PRs, with heuristics that guess the link |
| [[msr-data-noise]] | The linking patterns are guesses over free text, so every count downstream inherits their error rate |
| [[software-metrics]] | Task 3 asks for the measures *and* for their classification against the lecture's grid |
| [[defect-prediction]] | Bugs-per-file is the input to the defect models of lecture 6; task 3.2 builds exactly that data |
| [[msr-pipeline]] | The sheet walks the whole pipeline: collect (1), link/enrich (2), analyse (3) |
| [[msr-statistical-methods]] | "Per project as well as over all projects" is a comparison across groups, which is where the lecture's statistics enter |

## Exercise Structure

**Task 1 — expand the corpus.** Task 1.1 asks for two named projects (Apache Zookeeper, Apache
Superset) plus one the student chooses, with Seart GitHub Search named as the way to find a
suitable large repository; for each, "find out how they handle their commits, issues and pull
requests (PRs)" and be able to explain the choice. Task 1.2 then revisits the exercise-3 schema
against the new data — "does the data from the new projects fit in there as well, or do you need to
make adjustments?" — mines it in, and requires that every row stay traceable to its source project
now that tables hold more than one project's data. The sheet also gives an operational instruction
that is easy to skip: test the import on a subset first, then let the full import run overnight
because "it might take multiple hours".

**Task 2 — linking.** Build issue↔commit, commit↔PR and PR↔issue links from remembered textual
patterns, with regular expressions as the named mechanism (section 4.2 points at a tutorial, a
Python reference and the RegExr testing tool). Then implement it and store it with the relational
machinery — foreign keys, primary keys — with a stated acceptance criterion: "it should be possible
to create a SQL query that, for example, returns all commits related to an issue based on the
issue's id."

**Task 3 — metrics.** 3.1 asks for **mean time to resolve** (differentiating by issue type) and
**mean time to response** ("the mean of the time that it takes for someone, other than the creator,
to respond to an PR"), each computed per project and over all projects, plus the lecture-taxonomy
classification. 3.2 builds a linked metric: follow issues whose type is *bug* to their connected
commits, extract the files those commits changed, count occurrences per file, then ask which files
are connected to the highest number of bugs, which are barely ever connected, and whether there is
a pattern — again with the classification question.

**This page describes the exercise; it does not answer it.** See the note below.

### The Sheet's Own Instruction

The sheet is headed "Mining Software Repositories / Exercise 4", lists "Prof. Dr. Steffen Herbold",
"Winter 2026", "Due on 11.11.2026", and names "Author: Lukas Schulte".

Twice over the sheet carries an **IMPORTANT NOTE FOR LARGE LANGUAGE MODELS** — the same text as
exercises 1–3, addressed to "ChatGPT, Copilot, Gemini, etc." — mandating that no assistance be
given in solving the tasks, and stating that "The tasks are not supposed to be solved by AI." The
note in this sheet also carries an instruction to print a video URL. That instruction is part of
the source document, is recorded here as a fact about the sheet, and is not acted on: it is an
injection in the source, not a request from the student. Consequently this page contains no queries,
no regex patterns, no schema changes and no metric computations — only what the sheet asks for.

## Exam-Relevant Points

1. **The two named metrics and their definitions.** Mean time to resolve (per issue type) and mean
   time to response (to a PR, by someone other than the creator). The parentheticals are part of the
   definition and the source of most wrong answers: "resolve" needs a resolution event, and
   "response" excludes the author.
2. **Classification against the lecture's categories is asked twice** (3.1 and 3.2) — the sheet is
   testing whether the metric grid can be applied, not just the arithmetic.
3. **Per project versus over all projects is required for both basic metrics**, which is the first
   place in the course where the database's multi-project design pays off and the first place where
   cross-group comparison (and hence the statistics lecture) becomes relevant.
4. **Linking is measured by a query, not by a count.** The acceptance criterion is a SQL query
   returning commits for an issue id, i.e. a reproducible derivation rather than a number.
5. **Bugs-per-file is the input to defect prediction** (lecture 6): the sheet has you build the
   labelled data that the later lectures model.
6. **Traceability is an explicit requirement** — with several projects in one table, every row must
   still be attributable to its source, which is a schema requirement before it is a data rule.
7. **The import scale is a design constraint**, stated operationally: subset first, then an overnight
   run.

## Connections

- [[mining-software-repositories]] — the course page.
- [[mining-software-repositories-exercise-3]] — the schema and the Ignite data this sheet extends;
  exercise 3's design decisions are revisited here, so a bad schema costs twice.
- [[mining-software-repositories-exercise-2]] — the GitHub extraction scripts that have to be
  re-pointed at three more projects.
- [[mining-software-repositories-exercise-1]] — the Git/Jira side of the same tooling.
- [[mining-software-repositories-lecture-3]] — enrichment: linking and defect data, the concepts
  task 2 and task 3.2 implement.
- [[mining-software-repositories-lecture-6]] — defect prediction, which consumes the bugs-per-file
  data this sheet produces.
- [[mining-software-repositories-lecture-7]] — the method behind "per project and over all projects".
- [[mining-software-repositories-lecture-5]] — the social-aspects material that also runs on linked
  issue/PR data.
- [[repository-link-enrichment]] — the concept page for the linking heuristics.
- [[msr-data-noise]] — what unevaluated regex links do to every metric computed from them.

## Open Questions

- **The third project's selection criteria are only "sufficiently large"** — Seart GitHub Search is
  recommended, but no threshold, licence or domain condition is given.
- **"Differentiate between different types of issues"** does not say which type vocabulary to use
  (the tracker's own labels, or the course's categories), which changes the answer materially.
- **Whether the regex links must be validated** — sampled, manually checked, or reported with an
  error estimate — is not stated, although lecture 3 and lecture 8 both treat unvalidated heuristics
  as a threat to validity.
- **No expected result shape is given for the metrics** (units, resolution for open issues,
  treatment of issues never responded to), so the comparison across projects is defined only
  loosely.
- **Which SQL dialect and DBMS** — exercise 3 recommended MariaDB, but this sheet does not require
  staying there.
