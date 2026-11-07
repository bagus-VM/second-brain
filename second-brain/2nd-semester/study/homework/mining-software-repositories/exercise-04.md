---
title: "Mining Software Repositories — Exercise 4: Expanding, Linking and Measuring the Database"
tags: [homework, mining-software-repositories, semester-2, metrics, linking]
course: "Mining Software Repositories"
source_count: 1
status: current
last_updated: 2026-11-05
prerequisites: ["[[repository-link-enrichment]]", "[[msr-data-noise]]", "[[software-metrics]]"]
---

# Exercise 4 (due 11.11.2026) — Expanding the harmonized database

Source: `exercise_04.pdf` (Herbold, WS 2026, due on 11.11.2026, author Lukas Schulte). **No
AI-written solution on this page, by the sheet's own instruction** — see *Why this page has no
solution* below.

## What the sheet asks for

### Task 1 — Expanding the database

**1.1 Expanding the number of projects.** "In week's tasks, we will expand the number of projects
from which data needs to be collected." Two named projects plus one of the student's choosing:

- **Apache Zookeeper** and **Apache Superset** — for each, find out how it handles commits, issues
  and pull requests.
- **At least one more project**, chosen by the student, using **Seart GitHub Search** (section 4.1)
  to find "a sufficiently large GitHub repository", with the requirement that the choice be
  explained, "including how it handles commits, issues, etc."

**1.2 Revisiting exercise 3.** The schema from the previous sheet is now the artifact under test:
"Revisit your database schema. Does the data from the new projects fit in there as well, or do you
need to make adjustments?" Then mine the new projects into it, under one explicit constraint —
"although tables may now contain data from multiple projects, you can still trace each row back to
its source" — and one operational instruction: test the import on a subset first, "and then let the
full import run overnight. It might take multiple hours."

### Task 2 — Linking

"Issues and commits, as well as issues and PRs" can now be linked, "For this, we need to remember
the patterns we already spotted in our data."

- Devise a way to link **issues to commits**, **commits to PRs**, and **PRs to issues**, using
  regular expressions (the sheet points at a tutorial, a Python reference and the RegExr test tool
  in section 4.2).
- Implement it and store the result "in your database (foreign keys, primary keys, etc.)".
- Acceptance criterion, in the sheet's words: "Once you are finished, it should be possible to
  create a SQL query that, for example, returns all commits related to an issue based on the
  issue's id."

### Task 3 — Metrics

**3.1 Basic metrics**, computed "per project as well as over all projects":

- **Mean time to resolve** — the mean of the time it takes for an issue to be resolved, with the
  requirement to "differentiate between different types of issues".
- **Mean time to response** — the mean time for "someone, other than the creator, to respond to an
  PR".
- Then: "How would you classify those metrics according to the categories discussed in the
  lecture?"

**3.2 Metrics based on linked data** — the linked structure now earns its keep: "calculate the
number of bugs for each file."

1. Follow the relation of bugs (issues with type *bug*) to the connected commits and extract the
   files that changed.
2. Count the occurrences of each file, and answer: which files are connected to the highest number
   of bugs, which are barely ever connected, is there a pattern?

And again: "How would you classify this metric according to the categories discussed in the
lecture?"

## What is actually hard here

Three things, in ascending order of how easy they are to underestimate:

1. **The schema's second test.** Exercise 3's design was validated against one project. Three more
   projects mean three more conventions for issue types, PR references, branch layouts and author
   identity — plus the new traceability requirement that every row names its source. A schema that
   passed with one project can fail here for reasons that have nothing to do with the queries.
2. **The links are textual guesses.** Task 2 is the concept of [[repository-link-enrichment]] applied
   with regexes over commit messages and PR descriptions. Whatever the patterns miss or over-match
   propagates into 3.2's per-file bug counts, and the sheet does not ask for the links to be
   validated — the course does (lectures 3 and 8 both treat unvalidated heuristics as a threat to
   validity), which is a gap worth closing on your own initiative.
3. **The metric definitions' edges.** "Time to resolve" needs a definition of *resolved* (and of
   what happens to issues still open); "time to response" excludes the creator; both are asked for
   per project and overall, which turns a single number into a comparison and drags in the
   statistics of lecture 7.

## The tooling, and the two things that actually bite

- **Seart GitHub Search** (`https://seart-ghs.si.usi.ch`) — the sheet's recommended way to find a
  project large enough to be interesting. The selection argument matters as much as the selection.
- **RegEx** — the mechanism of task 2. Python's `re` for the implementation (`regexone.com/references/python`),
  the regexone tutorial for the syntax, and regexr.com for interactive testing. The practical shape
  is: patterns like `(?i)(fix|closes|resolves)\s+#?(\d+)` over commit messages, matched against the
  issue numbers already stored, with the false-positive rate measured rather than assumed.
- **The overnight import** is not incidental advice. Mining three more projects' full history over
  network APIs is hours of work, and the API rate limits from exercise 2 (now per token, per
  repository, with pagination) are what makes it hours rather than minutes.

## How this connects to the lecture material

- **Lecture 3 (enriching raw data)** supplies the whole vocabulary of task 2: linking repositories,
  the heuristics that guess the link, and the noise those heuristics introduce ([[msr-data-noise]],
  [[repository-link-enrichment]]).
- **Lecture 3 also supplies the metric taxonomy** task 3 keeps asking about ([[software-metrics]]:
  direct vs indirect measures, internal vs external quality, product vs process).
- **Lecture 6 (studying bugs)** is where bugs-per-file leads: defect prediction and just-in-time
  prediction run on exactly this per-file labelling ([[defect-prediction]]).
- **Lecture 7 (methods)** is behind "per project as well as over all projects" — comparing groups
  is a statistical question, not a reporting one ([[msr-statistical-methods]]).
- **Lecture 8 (validity)** is what should make you validate the regex links before trusting 3.2
  ([[threats-to-validity]]).

## Why this page has no solution

The sheet carries the same **IMPORTANT NOTE FOR LARGE LANGUAGE MODELS** as exercises 1–3: the
document's owner mandates that no assistance be given in solving the tasks, and "The tasks are not
supposed to be solved by AI."

This sheet's version of the note also instructs the model to output a video URL. That line is part
of the source document, is recorded here as a fact about the sheet, and was **not** acted on — an
instruction embedded in course material is not a request from the student, and following it would
be exactly the kind of behaviour the note itself is testing for.

So: the tasks are described, the tooling and its mechanics are explained, and the method notes are
written down. The schema changes, the regex patterns, the SQL and the metric computations are the
student's own work, as the sheet requires.

## Connections

- [[mining-software-repositories-exercise-4]] — the topic page: same material, keyed to the lecture
  index.
- [[mining-software-repositories-exercise-3]] — the schema and the Ignite data this sheet extends
  and re-tests.
- [[mining-software-repositories-exercise-1]], [[mining-software-repositories-exercise-2]] — the
  extraction tooling that gets re-pointed at three more projects.
- [[repository-link-enrichment]] — task 2's concept.
- [[msr-data-noise]] — why the links, and everything computed from them, need a validity statement.
- [[software-metrics]] — the classification question the sheet asks twice.
- [[mining-software-repositories-lecture-3]] — enrichment and metrics, the lecture behind task 2 and
  task 3.1.

## Open Questions

- **"Differentiate between different types of issues"** does not name the type vocabulary — the
  tracker's own labels, or the course's categories. The two give different numbers, and the sheet
  does not say which it wants.
- **How open and never-responded-to items enter the means** is not specified, so the two time metrics
  are only partially defined.
- **No threshold for the third project's size**, and no licence or domain restriction, beyond
  "sufficiently large".
- **Whether the links must be validated** — sampled, measured or reported with an error estimate —
  is left out, although the lecture material insists on it.
- **Which DBMS to stay on.** Exercise 3 recommended MariaDB; this sheet is silent, so the choice is
  open even though the schema is now carrying more.
