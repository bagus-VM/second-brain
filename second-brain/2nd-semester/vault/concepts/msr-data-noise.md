---
title: "Noise in Heuristic MSR Data"
tags: [concept, mining-software-repositories, semester-2, data-noise, validity]
course: "Mining Software Repositories"
source_count: 1
status: current
last_updated: 2026-10-22
prerequisites: ["[[mining-software-repositories]]"]
---

## One-line Summary

Heuristic MSR data is never clean: every wrong assumption behind a heuristic becomes noise, and a
study's validity depends on measuring that noise rather than assuming it away.

## Core Intuition

The lecture's argument is short. "Wrong assumptions on what the data should be, lead to noise when
heuristics are used", and "Amount of noise impacts validity". But noise is not fatal: "Noisy data
can still be analyzed", and "It is possible to draw valid conclusions or build tools based on
noisy data". What is not acceptable is ignoring it — "analysis needs to take noise into account
(!)". And you can only account for noise you understand: "We need to understand noise to understand
how to take it into account and how it affects results".

So the chain is: a heuristic makes an assumption → the assumption is wrong for some data → those
data points are noise → the noise has a size and a direction → the study must tolerate it, remove
it, model it, or reduce it at the source. The lecture walks one enrichment pipeline end to end —
link commits to issues, label issues as bugs, find bug-fixing commits, find bug-introducing
commits — and puts a number on each step.

Two distinctions carry the weight. **Noise is not the same as error**: a commit with no issue link
is a missed link (a false negative of the linking heuristic), while an issue labelled
"improvement" that is really a bug is a wrong label. And **random and directional noise differ**:
"If noise is randomly distributed (e.g., Gaussian noise) this is easier to ignore than noise in a
specific direction" — "Noise may introduce biases".

## Formal Definition / Statement

The unit of data quality here is the *assumption*: an unjustified belief that what the heuristic
finds is what is actually there. The slide lists eight assumptions behind SZZ — that commit
message numbers relate to issues, that developers reference bugs and label issues correctly, that
"Bugs are bugs, features are features", that every line touched in a fix relates to the bug, that
the last change to such a line may have introduced it, that bugs were introduced by the last
change and not already dormant, and that changes after the bug reporting date can still be
responsible. "These assumptions do not always hold!" — "Each is a source of noise".

**Noise in commit-issue links.** Three strategies are compared: **SZZ**, "match numbers within
commit messages to issues (e.g., 1 to NUTCH-1)"; **JL**, "match complete Jira identifier to
issues (e.g., NUTCH-1)"; and **JLM**, "manually validated link from commit to issue". Evidence
base: "Data is based on 18,721 manually validated links" (Herbold et al. 2022, *Empirical Software
Engineering* 27, 42).

**Noise in issue types.** "Median of 42% mislabeled as bug!" The base is "11,295 issues that are
linked to a commit", and the plot "uses RFE and IMPR together as IMPROVEMENT" (Herzig et al. 2013,
ICSE, pp. 392-401). The reason, quoted from that paper: "The definition of a bug not only differs
between users and developers but also between developers themselves. … But a data miner building a
defect prediction model must distinguish between bugs and non-bugs. Otherwise, the prediction
model would predict changes, not defects".

**Resulting noise in bug-fixing commits.** "SZZ misses about one in five bug fixing commits and
only about half of the commits identified as bug fixing are actually bug fixing!" and "Better issue
linking can only avoid missing bugs, the source are wrong issue types!" — "This noise affects bug
introducing commits as well!"

**Noise in bug-introducing changes.** "Sample shows that using git blame often works but can be
very unreliable." "Other data from issue tracker (e.g., affected versions field) even more
unreliable!" "Other literature agrees that the last change is correct about 70% of the time". A
refined variant: "JLMIV+R: Date of last bug introducing change. Uses manually validated bug fixes,
git blame ignores whitespaces, comments, and refactorings".

**Tangled changes in bug fixes.** The slide asks "Which lines contribute to the fix?" and reports
"All code (289,904 lines)". The extracted text prints: "Bug fix: 25,1%", "No bug fix: 4,5%", "No
consensus: 8,9%", "Test/Doc/Whitespace: 1,5%", "Whitespace: 4,1%", "Unrelated improvement: 0,5%",
"Refactoring: 1,8%", "Documentation: 14%", "Test: 39,6%", and concludes "Assuming changes address
single aspects is very often wrong!" (Herbold et al. 2022, *Empirical Software Engineering* 27,
125).

**The five responses to noise** are the chapter's taxonomy: ignore it; account for it during data
collection; account for it during the analysis; manually clean the data; or improve the heuristics
and then proceed with one of the others.

## Key Properties

**Ignoring noise is a legitimate choice under stated conditions.** It is an "Easy low effort
solution" and "Never ideal from a validity point of view, but can still be a good solution",
depending on the amount of noise, the cost of removing it, the type of analysis ("Noise can often
(safely) be ignored when fitting models, but cannot easily be ignored when evaluating models"),
the strength of the effect studied ("weak effects are more likely hidden by noise"), and the type
of noise.

**Training and evaluating on the same noise differ.** For training, "Theoretical frameworks like
the statistical query model even proof that optimal solutions can still be found if certain
conditions are fulfilled", and more data is usually needed. For evaluation, noise "would enable
overfitting on noise (i.e., models could learn noise and we would not detect this)", with both
error directions named: "Underestimation of performance because noisy data would be inadvertently
counted as mistakes" and "Overestimation of performance if both the model and the noise are
biased". The "Feasible solution": "Train with large amounts of possibly noisy data, evaluate with
smaller amount of clean data".


**Filtering during collection trades noise for bias.** "When we require issue links to determine
bugs, commits that do not link to issues cannot be bug fixing"; measuring the linking ratio tells
you "this development practice was followed", so "We can measure this for projects and only
analyze projects with high linking ratios". The cost: "Introduces biases into the data" — such
projects "often have other quality assurance measures in place", and "it is unclear how results
transfer" to projects without a rigorous process.

**White noise is handled by statistics; outliers need filters.** "White noise is for many
statistical approaches not a problem and already accounted for" — it "Reduces power of statistics
and can be dealt with through more data", and is "Usually modelled as a random variable with an
expected value of zero". Outliers instead need filtering: "data from 1970 usually indicates a
broken timestamp".

**Manual cleaning is the most accurate and least scalable option.** "Often, humans can identify
the noise"; it is the "Usually most accurate solution to deal with noise"; but it is "Very
expensive and labor intensive", since "Humans also make mistakes", and "Human effort does not
scale well".

**Better heuristics are the general fix.** They "Reduce the general problem", "Can be used by
others as well", and "Any improvement must be validated to measure the effect. Ideally, the impact
on prior research should also be determined". Directions given: more complex data processing;
removing assumptions on the development process; including automated cleaning steps like outlier
detection; and including "measures for the certainty of the heuristic", which "Enables subsequent
manual analysis and correction of only the data with a low certainty".

**Some causes are structural.** The slide lists "Simplified assumptions" and "Misalignment of
developer interests and MSR goals", and notes that the same reasoning "also applies to tangling":
the developer's notion of "worth fixing" and the researcher's need for a binary label are
different questions.



## Worked Example

The deck's own demonstration is the automatic bug/non-bug classifier, built because "Data in
repositories is often mislabeled" and "Cleaning this data requires a large amount of effort". The
solution: "Train a machine learning model on a large amount of easily available noisy data" and
"Evaluate this model on a smaller amount of cleaned data". Two configurations are compared:

- **FTA** — "a fastText model trained on a smaller cleaned data set. This leads to higher
  precision, but at the cost of recall because less data was available."
- **FTA-UV** — "trained on a large amount of noisy data instead. The noise reduced precision, but
  the larger data set helped to improve the recall."

(Herbold, Trautsch & Trautsch 2020, *Empirical Software Engineering* 25, 5333-5369.) The pair is
the chapter's thesis in miniature: the noise is not removed, it is placed where it hurts least.

The c1-c7 timeline carries the same argument through SZZ: c7 fixes bug 1 and c3 fixes bug 2; c1,
c2, c3 and c4 are candidates for bug 1 because they touched lines the fix of bug 1 changed; c2
precedes the reporting date of bug 2; c2 becomes a weak suspect for bug 1 because it is
bug-introducing for bug 2; c3 is a partial fix for bug 1; and c4 is a hard suspect for bug 1
"because it is not introducing or fixing for another bug". These classifications rest on
assumptions the tangling data shows are often false: a fix commit that also adds tests and
refactors gives blame-based attribution no way to separate the parts.

## Common Pitfalls

- **Treating a heuristic's output as a fact.** Every label is a claim about an assumption.
- **Reading a missed link as a bug.** The two link-noise directions need different fixes.
- **Ignoring label noise while blaming the linking.** "Better issue linking can only avoid missing
  bugs" — the 42 % mislabeling needs a label fix, not a regex.
- **Evaluating a model on data as noisy as its training data.** Overfitting on noise becomes
  invisible.
- **Using noise as a filter without naming the bias.** Restricting a study to strict-linking
  projects improves data validity and destroys generalisability.
- **Treating white noise and directional noise the same.** Random noise reduces power;
  systematic false positives bias the estimate.

- **Assuming manual cleaning is cheap or unbiased.** It needs trained raters and does not scale.
- **Quoting the tangling numbers as a clean partition.** The categories overlap.

## Connections

- [[repository-link-enrichment]] — the heuristics whose error rates this page measures.
- [[szz-algorithm]] — the algorithm whose assumptions produce most of the noise here.
- [[mining-software-repositories]] — the pipeline whose enrichment stage this noise belongs to.
- [[software-metrics]] — measurement quality attributes that the noise degrades.
- [[threats-to-validity]] — the frame in which "Amount of noise impacts validity" is evaluated.
- [[defect-prediction]] — the downstream consumer hurt by the 42 % mislabeling.
- [[qualitative-coding]] — the manual-cleaning option taken seriously, with raters and agreement.
- [[msr-statistical-methods]] — the machinery handling white noise and outliers.

## Open Questions

- **The tangling slide's labels and percentages do not line up unambiguously in the extracted
  text.** The text layer prints "Test/Doc/Whitespace: 1,5%" next to separate "Whitespace: 4,1%",
  "Documentation: 14%" and "Test: 39,6%" lines, and the category order does not match the label
  order in the way a pie chart would require. The percentages above are reproduced exactly as
  printed; which label each belongs to on the rendered slide cannot be settled from the text
  alone.
- **No confidence intervals or significance tests accompany the noise figures.** The 18,721
  validated links and 11,295 issues are point estimates, with no indication of how stable the
  "median of 42 %" and "one in five" are across projects.
- **The trade-off between noise and bias in Option 2 is named but not quantified**, and the
  chapter does not say how the noise rate generalises: all figures come from specific studies.
- **The "about 70 % of the time" correctness of last-change attribution is attributed to "other
  literature"** without naming the studies, so it cannot be compared with the deck's own figures.
