---
title: "Mining Software Repositories — Lecture 2 Overview (Collection of Raw Data)"
tags: [topic, mining-software-repositories, semester-2, data-collection]
course: "Mining Software Repositories"
source_count: 1
status: current
last_updated: 2026-10-22
prerequisites: []
---

## One-line Summary
Chapter 2 is the data-source catalogue: it argues that any tool a developer uses is a potential
MSR source, walks each family of sources and what it records, then surveys the collection
toolchain — off-the-shelf suites, hand-built tools, and reused datasets.

## Core Map
```
Chapter 2 — Collection of raw data
│
├── Data sources
│   ├── "Infeasible to list all data sources"
│   ├── Problem-driven selection: know first, then decide what you need
│   ├── "Raw data means unprocessed data" -> enrichment deferred
│   └── Catalogue by type: source code; VCS; issue trackers; review tools;
│           CI; artifact repositories; forges; chats; wikis; Q&A sites
│                   -> [[software-repositories]]
│
├── Source code and version control
│   ├── Static vs dynamic analysis; only 38% of Maven snapshots still build
│   ├── Centralized vs decentralized; deltas (SVN) vs snapshots (Git)
│   ├── Commits: author vs committer, message, tree, timestamps
│   ├── Branches, HEAD, merge commits; the Git DAG
│   │       -> [[git-dag-structure-and-internals]] [[git-branching-and-merging]]
│   ├── Promises and perils of mining Git (Bird et al. 2009)
│   ├── Rename heuristic (default 50% similarity)
│   └── Textual diffs and the diff-algorithm validity issue
│           -> [[git-patches-and-diffs]]
│
├── Issue tracking and code review
│   ├── Issue fields, types, lifecycles, events and change history
│   ├── Issue tracking as process tracking
│   ├── Pull requests: dual role; reviews inside PRs; Gerrit patch-based
│
├── CI, telemetry, artifact repositories, forges
│   ├── CI data = build data; remedy for retrospective builds
│   ├── Telemetry variants; dependency graph from binaries
│   └── Forges: ecosystems, inner-source
│
├── Communication tools, wikis, Q&A sites
│   ├── Email archives, IRC, Slack/Mattermost, identity matching
│   └── Wikis for documentation; community pulse
│
└── Tools for data collection
    ├── Off-the-shelf: Grimoire Labs, SmartSHARK, PyDriller, LISA
    ├── Static analysis chain: linters, PMD, SonarCube, SLOCCount, CKJM
    ├── Building your own: APIs (access, pagination, rate limits), scraping
    └── Reusing data: GitHub Archive, Stack Exchange dump, MSR data track
```

## Key Concepts at a Glance

| Page | Core idea |
|------|-----------|
| [[software-repositories]] | The catalogue of source families and the rule that selection is problem-driven, not convenience-driven |
| [[git-dag-structure-and-internals]] | Commits form a DAG with root and orphan commits, and more than two parents is normal |
| [[git-branching-and-merging]] | Branches are pointers, HEAD points at a branch, merges create commits with two parents |
| [[git-patches-and-diffs]] | Diffs are textual and algorithm-dependent, so the diff algorithm can change the validity of a result |
| [[msr-tool-building]] | The collection toolchain: off-the-shelf suites, hand-built tools, or reused data |

## Lecture Structure
1. **Why no complete list exists** — every tool a developer uses is a candidate source; the
   rule is to know what you want first, then what you need.
2. **Source code** — files and projects as artifacts; static analysis (text, AST, control-flow
   graphs) versus dynamic analysis; the PyTorch and Maven-snapshot examples showing why most MSR
   work stays static.
3. **Version control** — CVS, SVN, Mercurial, Git; centralized versus decentralized; deltas versus
   snapshots; the anatomy of a commit; branches, HEAD, merge commits; the commit DAG; Bird et
   al.'s promises and perils, including rewritten history and no single mainline.
4. **Tracking changes to files** — the rename heuristic and why similarity rather than equality
   is used; textual diffs and the warning that different diff algorithms produce different diffs
   for the same two files.
5. **Issue trackers** — fields and types, the lifecycle, events as the record of every change, and
   the choice between storing a description as-of-collection or as-originally-created.
6. **Code review** — pull requests as merge vehicle and review mechanism; the code change itself
   lives in the VCS; Gerrit's patch-based approach and lost comment locations.

7. **CI, telemetry, artifact repositories, forges** — build data as a remedy for retrospective
   builds, the parsing burden of build logs, telemetry variants, dependency analysis from
   binaries, forge ecosystems and inner-source.
8. **Communication tools, wikis, Q&A sites** — mail archives, IRC and chat metadata, the identity
   matching problem, documentation evolution, and the community pulse.
9. **Collection tools** — Grimoire Labs, SmartSHARK, PyDriller, LISA; the static-analysis
   toolchain; building your own via APIs or scraping, with the warning that scraping brings
   noise; reusing shared datasets.

## Exam-Relevant Points
1. **"Raw data means unprocessed data."** Linking, enrichment, and human annotation belong to
   later chapters; collecting a link between two sources during collection is already an
   enrichment decision.
2. **Selection is problem-driven.** The slides state the anti-pattern explicitly: not "this data
   is conveniently available for me, what can I do with this".
3. **Git stores snapshots, not deltas.** Every diff has to be computed, and the rename heuristic
   defaults to 50 % similarity.
4. **The diff algorithm is a validity issue.** Aligning review comments with mined changes
   assumes the same diff algorithm was used.
5. **Mining Git has perils**: no single mainline, rewritten history, and often no way to tell
   which branch a commit was made on.
6. **Issue data must capture events**, because the common assumption that fields stay constant
   is false — descriptions get edited and comments get deleted.
7. **CI data is the remedy for retrospective builds**, but raw build logs are heterogeneous and
   often retained only for a limited period.
8. **Collection tools come in three kinds** — off-the-shelf suites, tools built for one study,
   and reused datasets — each with its own effort-versus-control trade-off.

## Connections
- [[mining-software-repositories]] — the course page.
- [[mining-software-repositories-lecture-1]] — where the repository definitions come from.
- [[mining-software-repositories-lecture-3]] — enrichment, deferred here.
- [[mining-software-repositories-exercise-1]] — the sheet that makes this chapter practical.
- [[git-dag-structure-and-internals]] — the commit graph in detail.
- [[git-branching-and-merging]] — branches, HEAD, and merges.
- [[git-patches-and-diffs]] — diffs, the rename heuristic, their validity consequences.
- [[msr-tool-building]] — the collection toolchain and trade-offs.

## Open Questions
- **No numbers are given for the cost of collection** at any source — no storage sizes, no
  runtime for mining a full history.
- **The 38 % Maven-snapshot figure** is attributed to Tufano et al. (2017) and dated to the state
  of the ecosystem at that time; the slides do not say whether it still holds.
- **Identity resolution across chat and email is named as a problem** ("herbold@cs.uni-goettingen,
  steffen.herbold@kit.edu, … are all the same person!") but no method is proposed.
- The API slide mentions access rights, pagination, and rate limits but gives no concrete limits.
