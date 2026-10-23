---
title: "Software Repositories"
tags: [concept, mining-software-repositories, semester-2, data-sources]
course: "Mining Software Repositories"
source_count: 2
status: current
last_updated: 2026-10-22
prerequisites: ["[[mining-software-repositories]]"]
---

## One-line Summary

A software repository is not one thing but a family of stores — version control, issue trackers,
review systems, CI servers, telemetry, artifact registries, forges, chats, wikis and Q&A sites —
each recording a different slice of what happened during software evolution.

## Core Intuition

The introduction slides open with a definition and then immediately contradict the singular
framing: "Many different kinds of repositories!". The slide's own catalogue is Continuous
integration systems, Issue tracker, Forges that combine many aspects, Code review tools, Q&A
sites, Source code management and version control, and Developer chats — followed by "… and
more!". The collection lecture makes the same point at greater length, grouped by *type of
data*: source code, version control systems, issue tracking systems, code review tools,
continuous integration systems, artifact repositories, forges, communication tools, wikis, and Q&A
sites and developer forums, plus requirements engineering, test management and project
management tools. The governing sentence is: "Every tool that any developer uses that records
data is a potential MSR data source" — the catalogue is open-ended by construction, not by
laziness.

Two working rules follow. First, selection is problem-driven: "First determine what you want to
know or achieve, then determine what you need to achieve this", with the explicit warning "Not:
this data is conveniently available for me, what can I do with this" — though in practice "often
a combination of both". Second, "Raw data means unprocessed data": linking between sources,
heuristic enrichment and human annotation are deferred to later chapters. A repository here is
the *input* to enrichment, not the analysis.

## Formal Definition / Statement

Three definitions answer three different questions.

**ISO/IEC/IEEE 24765:2017**, quoted verbatim:

- "collection of all system element or software‐related artifacts belonging to a system"
- "location/format in which such a collection is stored"
- "organized and persistent data storage that allows data retrieval"

**From the homepage of the 23rd International Conference on Mining Software Repositories:**
"software data such as source control systems, defect tracking systems, code review repositories,
archived communications between project personnel, question-and-answer sites, CI build servers,
and run-time telemetry."

**Kagdi, Collard & Maletic (2007):** "artifacts that are produced and archived during software
evolution".

And the term the field borrows its name from, per Merriam-Webster: data mining is "the practice
of searching through large amounts of computerized data to find useful patterns or trends", with
three key aspects — large amounts of computerized data, searching, finding useful patterns or
trends. The lecture is explicit that the term is used generically, "similar to data science",
as a "broad category for analyzing data". Combining the two gives the field's own equation:
"Data from software repositories + Data collection + Data analysis = Mining Software
Repositories (MSR)".

## Key Properties

**Version control is the oldest layer and the richest.** Centralized VCS keeps the database on a
server; decentralized VCS means "clients and servers all keep full copies of the version control
database". SVN and many others store "sequences of deltas": to obtain a file's state at version
5 three deltas are applied. Git instead "stores snapshots of each file" — each change leads to a
new snapshot. The snapshot choice is what makes the rename heuristic possible and what makes
raw diffs a computed artefact rather than a stored one.

**A commit is a structured record.** Each commit has a size (lines added and deleted), a tree
listing contents, an author (name and email), a committer (with email), a message, and author
and committer dates — the author/committer distinction being what allows attribution.

**The commit history is a DAG, not a list.** Commits are organized as a Directed Acyclic Graph,
though "Not strictly enforced. It is possible to create cycles!". Commits may have more than two
parents or children. Commits without a parent are root or orphan commits, and a repository can
have several; a common GitHub case is a gh-pages branch "that is completely independent of the
development branches (i.e., no merges between these branches)".

**Mining Git has promises and perils.** The promises: local copies allow mining local progress
never visible centrally; commit, branch and merge information give rich history; Git records all
conflict-resolution information; commits may be signed, "creating an official paper trail"; the
complete repository is locally available with "no communication with server required for
collecting data"; and many VCSs have converters to Git such as svn2git. The perils: branching is normal behaviour, "There is no single
mainline!", so you cannot assume a linear development path — the slides give C1 committed to
branch B1 in March, C2 to B2 in April, B2 merged to main in May, B1 merged in June, where "From
the perspective of main, C2 happened before C1 (as in: merged before), from a developer
perspective the work on C1 was finished before C2".

**Renames are detected by similarity, not equality.** Because Git stores snapshots, "the
difference between two states needs to be computed somehow" and a rename must be calculated too.
Git's heuristic: "Rename = delete old file and create new file with the same content"; when a
file is deleted, Git checks whether a file with "similar enough" content is created. The reason
for similarity is the move-class refactoring: moving Foo.java from src/de/ugoe/cs/examples to
src/de/up/cs/examples and changing its first line yields no exact match but high similarity.
"Default value is that 50% similarity is required, but can be configured".

**Diffs are algorithm-dependent.** "Same two files can have very different diffs! Depends on
algorithm!" and that this "May affect validity of data and analysis".

**Issue trackers are versatile.** An issue can be a requirement, a change request, a bug report, a
question, or a task. Bugzilla and Jira expose "separate fields in meta data"; GitHub has "No
specialized fields. Instead labels for everything", so "Analysis of metadata is more difficult".
Issues have a life cycle — New, Assigned, Closed, Rejected, Duplicate, Reopened,
Verified/Tested, Implemented — and "All changes to the issue are reported as events", so "Data
collection from issue trackers must also capture events". The lecture's framing: "Issue tracking
= process tracking".

**Code review systems carry process data and VCS data.** For a GitHub pull request the obvious
data is issue-style tracking data, comments on individual lines, overall comments and
approval/rejection ratings; "The tricky part: data about the code change — This is actually VCS
data". Dedicated tools such as Gerrit may serve "just for the patches", in which case "Tracking
of patches required, cannot be offloaded to parallel mining of VCS system".

**CI provides a remedy for retrospective build failure.** CI data provides build logs, metadata
about the build, the version built, test results and sometimes coverage or static analysis
warnings. The raw logs "requires subsequent parsing" and are "often very heterogeneous".

**Other sources.** Telemetry is "Sometimes the only way to observe system behavior", e.g.
distributed systems like Apache Spark where execution logs appear on a specialized history
server. Artifact repositories (PyPi, Maven Central, npm, Dockerhub) let dependencies be
retrieved on demand rather than bundled, and let binaries be analyzed "without having to compile
source code". Forges combine many sources into one platform — GitHub has "over 100 million
registered developers" — and are "As data source ideal for MSR!", also enabling ecosystem data
about contributor overlap and popularity "measured through stars". Inner-source development
hosts a forge like GitHub Enterprise inside a company, which "Enables studies within companies".
Communication tools cover mailing lists, IRC, Slack and Mattermost; the warning is that "Tools
without login require identify matching when processing data" — three addresses of one person
must be recognised as one node.

## Worked Example

Take GitHub as the forge example. A single project page yields, per the slides, project metadata
(license, tags, homepage), data about popularity, social data about users and contributors, the
systems discussed earlier in the chapter "sometimes directly integrated", and the ability to host
a binary as a package or as releases. From that one page an MSR study can derive the commit
history, the issue tracker, pull-request reviews and CI runs — and, from the forge as a whole,
ecosystem data such as which developers contribute to which projects.

A second worked example is the failure case. The collection lecture's slide "Working with source
code is hard!" shows building the latest release of PyTorch (state March 2023) — "and we have
not done an analysis yet". The measurement behind that slide: "on average only 38% of Maven
snapshots from the Apache Foundation can still be build without additional effort". Hence
"Because dynamic analysis is so difficult, most MSR studies rely on static analysis".

## Common Pitfalls

- **Treating "repository" as a synonym for a Git clone.** The ISO "location/format" clause and
  the MSR conference's list both point far wider.
- **Selecting data sources by convenience.** The slides reject "this data is conveniently
  available for me".
- **Assuming a linear history.** "There is no single mainline!" — ordering commits by date
  rather than by graph position mis-orders development.
- **Assuming rename detection is exact.** It is a similarity heuristic with a default 50%
  threshold.
- **Ignoring events in issue trackers.** If only the current state is collected, the history of
  the issue is lost.
- **Collapsing identities.** Slack and IRC have no login; un-disambiguated accounts create
  ghost nodes.
- **Expecting retrospective builds to work.** Only 38% of the sampled Maven snapshots still
  build.

## Connections

- [[mining-software-repositories]] — the pipeline whose first stage these repositories feed.
- [[repository-link-enrichment]] — how the separate sources are joined into one dataset.
- [[msr-data-noise]] — the error rates attached to the heuristics built on this raw data.
- [[software-metrics]] — measurement theory applied to what these sources record.
- [[developer-social-networks]] — the network models built on version-control and
  communication data.
- [[community-smells]] — community structure derived from issue-tracker and VCS data.
- [[git-dag-structure-and-internals]] — the object model behind the commit DAG described here.
- [[git-branching-and-merging]] — branch and merge semantics behind the merge commits.
- [[git-patches-and-diffs]] — the diff format and its algorithm dependence.
- [[temporal-networks]] — the time dimension of commit, issue and discussion data.

## Open Questions

- **The three ISO clauses are not reconciled with each other or with Kagdi et al.** Whether a
  local checkout counts as a "location/format in which such a collection is stored" is open.
- **No criterion is given for completeness.** "Every tool that any developer uses that records
  data is a potential MSR data source" is a maximal statement with no scoping rule.
- **The problem-driven rule and the convenience rule are left in unresolved tension.** The
  slides acknowledge "In reality often a combination of both" without saying how to justify the
  combination.
- **Retention and completeness of forges is unaddressed.** Build data "sometimes only retained
  for a certain timeframe" is stated for CI, but nothing is said about how much issue or review
  history survives.
