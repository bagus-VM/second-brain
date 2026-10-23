---
title: "The SZZ Algorithm"
tags: [concept, mining-software-repositories, semester-2, defect-analysis]
course: "Mining Software Repositories"
source_count: 1
status: current
last_updated: 2026-10-22
prerequisites: ["[[mining-software-repositories]]"]
---

## One-line Summary

SZZ identifies bug-fixing commits by linking commit-message numbers to issues, then traces each
changed line back through blame to the change that last touched it — producing candidates,
suspects and hard suspects for the bug introduction.

## Core Intuition

The chapter's fourth block is "Collecting defect data", and it starts from the vocabulary the
course uses throughout:

- **Error** — "human action that produces an incorrect result".
- **Fault, bug** — "manifestation of an error in software".
- **Failure** — "termination of the ability of a system to perform a required function", "an
  externally visible deviation from the system's specification".
- **Defect** — "imperfection or deficiency in a work product where that work product does not
  meet its requirements or specifications and needs to be either repaired or replaced". The slide
  notes: "Usually used as synonym for fault and bug".

The chain on the slide is: developer makes an error → code contains fault → failure.

The second intuition is that MSR can only reach part of that chain. "Detection of failures the
task of software testing — Requires execution of the software and not within the domain of MSR".
What MSR *can* do is analyse "Reporting of failures", because that "Data contained within the
issue tracker", and analyse bug-fixing and bug-introducing commits, because "Changes that
introduce and fix bugs are tracked within the VCS".

The third intuition is that bug *fixes* are findable, and bug *introductions* are not directly
recorded — they must be reconstructed. That reconstruction is SZZ.

## Formal Definition / Statement

**Information about bugs**, as the slide lists it:

- *Reported bugs* — "Analyze data from the issue tracker. Most issue trackers have a specific
  field to identify the type of issue. Allows explicit labeling of issues as bug. Some tools do
  not have this (e.g., GitHub, GitLab) and use labels instead."
- *Bug fixes* — "Commits within the VCS that remove the bug from the code".
- *Bug introducing changes* — "Commits within the VCS that introduce a new bug into the code".
- *Buggy code* — "A snapshot of the software that contains a known bug, including knowledge
  about the location of the bug. Often paired with a clean version without the bug".

**The generic approach to finding bug-introducing changes** is three steps: "Find bug fixing
commit — Consider what was changed within the bug fix — Use version control system to identify
when this was last changed". The slide's "Visualization of the bug introduction" makes it
concrete: "1. Create diff for bug fixing commit — 2. Use git blame to identify bug introduction"
(Rodríguez-Pérez et al., "How bugs are born", EMSE 25, 1294–1340, 2020).

**SZZ** is "Named after the authors Śliverski, Zimmermann, and Zeller" and "Combines issue
linking with finding bug fixes and bug introducing changes. Consists of two phases. In the first
phase, bug fixes are identified — Based on a combination of number-based issue linking
(syntactic check) and heuristics to validate the link like keywords or author matching. In the
second phase, bug introducing changes are identified — Based on finding last changes to lines
and plausibility filters." Reference: Śliwerski, Zimmermann & Zeller, "When do changes induce
fixes?", MSR '05, 1–5.

**The two phases in full, as the slides print them.**

*Phase 1 — bug fixing:* "Determine if there is any number within the commit. If a number is found
and there is a bug issue matching this number, the commit is identified as bug fixing, if

- at least two of the following properties are fulfilled:
  - the issue was resolved as fixed at least once
  - the author of the commit is assigned to the issue
  - the title or description of the issue is contained in the commit message
  - one or more files that are changed by the commit are attached to the issue
- only one of the above properties is fulfilled and additionally, one of the following is
  fulfilled:
  - the commit message contains a term like bug or fix
  - the number in the commit points to an issue, e.g., because it starts with 'Bug #NUMBER'
  - the commit only contains numbers".

*Phase 2 — bug introducing:* "For each line that was changed in the fixing commit, identify the
last change to that line as candidate for an introducing change. Candidates are considered to be
bug introducing, if

- the date of the change was before the reporting date of the issue
- all other candidates are suspect
- suspects that are part of a bug fixing commit are considered as bug introducing due to the
  partial fix rule of SZZ
- suspects that are part of a commit that has other bug introducing changes are considered as bug
  introducing due to the weak suspect rule of SZZ
- all other suspects are not considered to be bug introducing and called hard suspects".

## Key Properties

**Two labeling strategies exist, and each has a characteristic error.** Keyword labeling scans
commit messages with regular expressions for "bug, fix, error, fault, failure, issue, patch".
"Keywords lack context" — "We added some tests to prevent future bugs" is wrongly identified as
bug fixing, producing false positives; while "Aligns code with prior changes to work correctly"
is missed, producing false negatives. "More keywords (e.g., correct) reduce false negatives,
but increase false positives — Typical recall/precision trade-off".

**Link-based labeling avoids the context problem but adds process assumptions.** "If a commit
references a bug issue, the commit is likely a bug fix — Avoids issues of keyword matching. Does
not depend on single words without context anymore." The price: "Makes assumptions on the
development process — Active use of issue tracker to track all bugs" and "Existence of links
between commits and bugs". "Violating these assumptions leads to false negatives, i.e., missing
bugs". The slide is blunt: "Quality of data depends on rigor of developers linking issues. If
issues are not created, typed as bug, or not linked, this approach fails. Depends on project!" —
illustrated by three projects: "Sometimes very accurate / Sometimes mixed / Sometimes sporadic".

**SZZ's assumptions are listed explicitly, and they do not always hold.** The slide enumerates:
"Numbers in commit messages are usually related to issues", "Developers reference bugs within the
commit message", "Developers label issues correctly", "Bugs are bugs, features are features, …",
"Every line that was touched in a bug fix is related to the bug", "Bugs were introduced by the
last change to a line and not already dormant for a longer period of time", "Changes after the
bug reporting data can still be responsible for the bug". Conclusion: "These assumptions do not
always hold! … Each is a source of noise."

**The improvements to SZZ are mostly about excluding lines that cannot introduce bugs.** Exclude
"changes to whitespaces and comments — Cannot cause bugs (in most languages)". Use a refactoring
detection algorithm (RefactoringMiner, RefDiff) to exclude refactorings, because "Refactorings,
by definition, do not modify the logic". Ignore "meta-changes, like copying the complete file
path or modifying file permissions".

**The basic variant is still the standard.** "Basic SZZ variant still in use — Study from 2018
shows that SZZ without changes is still used by 40% of papers using SZZ" (Rodríguez-Pérez, Robles &
González-Barahona, 2018, on reproducibility and credibility of SZZ; and Kim, Zimmermann, Pan &
Whitehead, ASE 2006, for the automatic identification of bug-introducing changes).

## Worked Example

The deck's SZZ visualisation uses a timeline of seven commits, c1 to c7, two issues (Bug 1 and
Bug 2) with reporting dates, and links from commits to issues. The slides build up in five
steps.

*Step 1 — sample data.* Commits c1 … c7 on a time axis, with links from commits to issues, the
issue reporting dates for Bug 1 and Bug 2, and "Blamed changes" recorded.

*Step 2 — bug fixing.* Two commits are identified as fixes: "c7 is fixing bug 1" and "c3 is
fixing bug 2".

*Step 3 — candidates.* Blaming the lines changed by those fixes yields "c1, c2, c3, and c4 are
candidates for bug 1" and "c2 is candidate for bug 2".

*Step 4 — introducing vs suspect.* Comparing the candidates' dates to the issue reporting dates
splits them: "c1 is before the reporting date of bug 1 and bug introducing for bug 1", "c2, c3
and c4 are after the reporting date and suspects for bug 1", and "c2 … bug introducing for bug
2".

*Step 5 — partial fix, weak suspect, hard suspect.* The remaining classification follows the
two rules: "c2 is a weak suspect for bug 1, because it is introducing for bug 2" (weak suspect
rule); "c3 is a partial fix for bug 1" (partial fix rule — c3 is itself a bug-fixing commit for
bug 2, and is therefore treated as bug-introducing for bug 1); and "c4 is a hard suspect for
bug 1, because it is not introducing or fixing for another bug".

The classification in one view: **introducing** = before the reporting date; **weak suspect** =
introducing for another bug; **partial fix** = part of a bug-fixing commit; **hard suspect** =
none of the above.

## Common Pitfalls

- **Reading a candidate as a confirmed cause.** Phase 2 produces candidates from blame; the
  candidate is only "bug introducing" if it predates the reporting date.
- **Treating the number match as the link.** Phase 1 requires two of four properties (or one
  plus one of three).
- **Ignoring the reporting-date rule.** Candidates after the report date become suspects, and
  the deck's own assumption list flags that this assumption itself is debatable.
- **Confusing weak suspect and partial fix.** Both are promoted to bug-introducing, but by
  different rules — one because it introduces another bug, the other because it is itself a fix.
- **Assuming blame gives the truth.** "Sample shows that using git blame often works but can be
  very unreliable", and other literature "agrees that the last change is correct about 70% of the
  time".
- **Applying SZZ where the assumptions do not hold.** Link-based labeling "Depends on project!".
- **Assuming improvements have been adopted.** 40% of SZZ-using papers still use it unchanged.

## Connections

- [[szz-algorithm]] — this page; the two phases, the rules, and the worked sample.
- [[mining-software-repositories]] — the pipeline stage this algorithm belongs to.
- [[repository-link-enrichment]] — phase 1 is a link-detection problem.
- [[msr-data-noise]] — the measured error rates of SZZ and its inputs.
- [[defect-prediction]] — the main downstream consumer of bug-introducing change data.
- [[defect-prediction-cost-model]] — how a predicted defect becomes an actionable warning.
- [[software-metrics]] — defect density and related measures built on this data.
- [[git-patches-and-diffs]] — the diffs and blame results SZZ consumes.
- [[git-dag-structure-and-internals]] — the commit history SZZ walks.
- [[threats-to-validity]] — the checks the assumption list implies.

## Open Questions

- **The slide gives the two-phase rule set but not the weights or thresholds used in practice
  by the original implementation.** How the "title or description … contained in the commit
  message" property is matched is unspecified.
- **The worked sample is described in prose but the underlying commit data is not given**, so
  the classification cannot be independently recomputed from the slides.
- **Whether the weak suspect and partial fix rules should apply when the other bug's issue is
  itself mislabeled is not addressed** — the two rules assume the other bug is real.
- **The 70% figure for blame correctness and the 40% unchanged-usage figure are cited without
  the studies' conditions**, so they cannot be transferred to another repository population.
- **No guidance is given on when SZZ is not worth applying at all**, as against when it is worth
  applying with the improvements.
