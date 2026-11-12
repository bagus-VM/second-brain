---
title: "Mining Software Repositories — Exercise 5 Solution (SZZ and Manual Validation)"
tags: [homework, mining-software-repositories, semester-2, exercise, szz]
course: "Mining Software Repositories"
source_count: 1
status: current
last_updated: 2026-11-12
prerequisites: ["[[szz-algorithm]]", "[[msr-data-noise]]", "[[threats-to-validity]]"]
---

## What was run

Source: `raw/lectures/Mining Software Repositories/Ubung/exercise_05.pdf`. Due 18.11.2026.

`szz-exercise-05.py` encodes the appendix history (five commits, one file, five issues) and runs
three variants: issue-linked detection, line-level blame, and file-level blame. Recorded output is
in `output-szz-exercise-05.txt`. The script asserts its own answers before printing them.

## Task 1.1 — Implement SZZ

The algorithm, in the form the sheet allows:

1. **Find bug-fixing commits.** A commit is a fix candidate when its message references an issue
   whose tracker type is `bug`. In the appendix that is only `42d921a2` (`Fixes ISSUE-0002`).
2. **Take the lines the fix removed or replaced.** At line level these are the lines that carried
   the defect: `import math` and `return math.divide(a, b)`.
3. **Blame the parent revision.** For each removed line, find the commit that introduced it. That
   commit is the bug-introducing commit.
4. **File-level substitute (this sheet).** Because changed lines were not collected, step 2 is
   replaced by "the whole file changed", and step 3 by "the last commit that touched the file
   before the fix". This is a strict approximation, and the appendix is built to show what it costs.

Line-level SZZ needs `git blame` on the parent of the fix; file-level SZZ only needs the commit
list. The implementation here simulates blame by carrying each line's origin through the history,
which is exactly what `git blame` reports for this linear five-commit case.

## Task 1.2.1 — Assumptions and where they break

| Assumption | What it buys | Where it breaks |
|---|---|---|
| The bug is reported and typed `bug` | Fix commits can be found by issue link | A real bug filed as `feature` or `task` is invisible; a `feature` whose title says "bug-free" is a trap (ISSUE-0004) |
| The fixing commit references the issue | One commit identifies the fix | Partial fixes, squash merges, and commits that close an issue without naming it |
| The fix removes the offending line | Blame points at the line that caused the defect | Fixes that add a guard elsewhere, rewrite the file, or delete the function |
| The blamed commit introduced the bug | Blame is causal | Refactors and moves: a later commit relocates a line without introducing the defect |
| One commit per bug, linear history | Simple walk back | Multi-commit fixes, reverts, rebases, force-pushes |
| File granularity is enough (this sheet) | Works without line data | Any later commit that touched the file becomes a candidate even if it changed something unrelated |
| Issue tracker types are accurate | Type filter is the entry point | Keyword-matching "fix" or "bug" without the type field mislabels feature work |

The last row is the one the appendix is really about: the file-level substitute does not find the
commit that wrote the bug, it finds the commit that last touched the file.

## Task 1.2.2 — Manual SZZ on the appendix

**Result: the bug-introducing commit is `24f914fd` (02.01.2023, lukas).**

Walk-through:

1. `42d921a2` (06.01.2023) is the only bug fix: it references ISSUE-0002, which is typed `bug`.
2. It removes two lines: `import math` and `    return math.divide(a, b)`, replacing the second
   with `    return a * b`.
3. Both removed lines were introduced by `24f914fd` (02.01.2023), the commit that added the
   `multiply` function and imported `math`.
4. `3f5b0912` (05.01.2023) reordered the imports and bumped the version, but it did not write
   `math.divide` — it only kept it as context. A file-level SZZ blames this commit anyway, because
   it is the last commit to touch the file. **That is a false positive.**

Verbatim output:

```
== issue-linked bug fixes ==
  42d921a2  Fixes ISSUE-0002: replace division by multiplication

== line-level SZZ (the definition) ==
  fix 42d921a2 removes 'import math' -> introduced by 24f914fd
  fix 42d921a2 removes '    return math.divide(a, b)' -> introduced by 24f914fd

== file-level SZZ (this sheet's substitute) ==
  fix 42d921a2 -> last commit touching the file: 3f5b0912
```

**Do breaking assumptions threaten the result?** Yes, in three distinct ways:

- **File granularity changes the answer.** Line-level SZZ says `24f914fd`; file-level says
  `3f5b0912`. The latter is wrong by construction, not by luck.
- **Keyword matching adds noise.** `3f5b0912`'s message says "Change version to **fix** value
  0.0002", but it links ISSUE-0003, a feature. A detector that greps for "fix" treats it as a bug
  fix and blames `160f0625` and `24f914fd`. One of those (`160f0625`, the initial commit) is a
  false positive caused only by the word "fix".
- **Issue titles mislead.** ISSUE-0004 is titled "bump version to 1.0 for **bug-free** release" and
  typed `feature`; ISSUE-0005 asks for division support and is still `open`. Neither is a bug
  report, and neither has a fixing commit.

## Data defects in the sheet itself

Flagged rather than silently repaired:

- **Version inconsistency.** Commit `3f5b0912` sets `VERSION = version(0.0002)`, but the listing
  for `42d921a2` shows `VERSION = version(0.0001)` as context, with no diff line changing it. The
  script uses 0.0002, the only state consistent with the preceding commit.
- **Duplicate hunk numbering.** In `3f5b0912` the removed lines and the added lines are both
  numbered from `(1)`, so the listing reads as two parallel hunks rather than one unified diff.
  It does not change the result.
- **A `math.divide` that does not exist.** `math.divide(a, b)` is not in Python's `math` module;
  the correct spelling is `a / b`. The sheet's bug is therefore also a NameError, not only a
  wrong-operator bug.

## Task 2.1 — A validation table

One row per **(candidate commit, fix commit)** pair, because the same commit can be blamed by
several fixes and the reviewer has to judge each claim separately.

| Column | Why it is there |
|---|---|
| `candidate` | The commit SZZ blames |
| `fix` | The bug-fixing commit that blamed it |
| `issue` | The bug report the fix closed |
| `file` / `line` | What the claim is about, so the reviewer can open the right diff |
| `changed_line` | The removed line, or `file-level` when line data is missing |
| `heuristic` | Which variant produced the row (line / file / keyword) |
| `label` | `true_positive`, `false_positive`, `unsure` |
| `note` | One sentence of reviewer reasoning |

Generated rows for the appendix:

```
candidate,fix,issue,changed_line,label
24f914fd,42d921a2,ISSUE-0002,"import math",true_positive
24f914fd,42d921a2,ISSUE-0002,"return math.divide(a, b)",true_positive
3f5b0912,42d921a2,ISSUE-0002,file-level,false_positive
```

To validate a row: open the candidate's diff, open the fix's diff, and answer one question — does
the candidate's change create the behaviour the fix repairs? If yes, `true_positive`; if the
candidate is unrelated (import reorder, version bump, formatting), `false_positive`; if the
evidence is insufficient, `unsure`, and an `unsure` row is a finding about the heuristic, not a
failure of the reviewer.

## Task 2.2 — Presenting hundreds of candidates

The bottleneck is reviewer time, not display. What scales:

- **One screen, one row, keyboard verdicts.** Columns as above; `j`/`k` to move, `t`/`f`/`u` to
  label, autosave. Two diffs side by side under the row. A reviewer who has to switch context for
  every row will not finish.
- **Sort by a cheap score first.** File-level-only rows, keyword-only rows, and rows where the
  candidate is the initial commit or a merge go to the bottom — they are the likely false
  positives. Reviewers should spend their attention where the heuristic is least certain.
- **Deduplicate by claim.** Hundreds of fixes can blame the same candidate; collapse to one row
  per `(candidate, fix)` and show "blamed by 7 fixes" as evidence, not seven separate rows.
- **Sample for calibration, then batch.** Label a random sample to estimate precision; if the
  estimate is good enough, label the rest by rule and keep a human audit sample. Do not label
  everything unless the decision needs it.
- **Track progress and disagreement.** A queue with counts (`120 / 400`, `TP 63 / FP 41 / unsure
  16`) and a second reviewer on a subsample. Inter-rater disagreement is a validity signal.
- **Export as CSV/JSON** so the labels feed back into the heuristic instead of dying in a UI.

## Task 2.3 — What manual validation buys

**(a) Determine risk.** Labels turn an unmeasured heuristic into a measured one. From a sample you
get an empirical precision (how many SZZ candidates survive review), a false-positive rate per
heuristic variant (line / file / keyword), and a breakdown by project, author and change size.
That is the input to any decision that uses the data: "if we review the SZZ output, how much of
our review time is wasted?" Without labels, the answer is a guess.

**(b) Mitigate risk.** Validation does three things the raw heuristic cannot:

1. **Filter.** Confirmed false positives are removed before the data drives a decision.
2. **Re-rank.** The features that separate true from false positives (change size, file
   churn, whether the candidate is a merge, distance in history) become a better score.
3. **Bound the claim.** A study can report "file-level SZZ achieves X % precision on our sample"
   instead of presenting candidates as facts — which is exactly what the lecture's validity
   chapter asks for and what the sheet's "risk" wording points at.

The honest limit: validation measures the heuristic on the sample you reviewed. It does not prove
the unreviewed part is equally clean, and it does not fix a granularity error — the appendix's
file-level false positive remains wrong no matter how carefully it is labelled.

## Connections

- [[mining-software-repositories-exercise-5]] — the task overview.
- [[szz-algorithm]] — the two-phase definition this sheet instantiates.
- [[msr-data-noise]] — heuristic noise, which the appendix demonstrates with three concrete traps.
- [[threats-to-validity]] — why an unvalidated heuristic is a construct-validity problem.
- [[mining-software-repositories-lecture-3]] — SZZ and enrichment in the lecture.

## Open Questions

- The sheet does not state what counts as a "reasonably sized" validation subset.
- It does not say whether `unsure` labels are allowed, or how disagreements are resolved.
- The version inconsistency means the appendix cannot be replayed exactly as printed; the
  reconstruction is documented above.