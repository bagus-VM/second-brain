---
title: "The Cost Model of Defect Prediction"
tags: [concept, mining-software-repositories, semester-2, defect-prediction]
course: "Mining Software Repositories"
source_count: 1
status: current
last_updated: 2026-10-22
prerequisites: ["[[defect-prediction]]"]
---

## One-line Summary

A defect prediction model is worth using only if it saves more quality-assurance money than it
costs to run and maintain, and that comparison — not the AUC — is what the cost model computes.

## Core Intuition

The lecture frames costs with the same four-cell diagram used for the prediction pipeline, and
each cell now carries a cost:

```
Input: Software -> Output: Prediction of defects -> Reaction: Correction of defects -> Result: Less post-release defects
```

The cost factors on the slide attach to those cells:

- Introduction of a prediction model (INIT), maintenance of the model, running predictions (EXEC)
  — on the input/output side
- Costs for quality assurance (QA), costs for correction (DEF) — on the reaction side
- Costs through missed defects — on the result side

And the slide asks the question that motivates the chapter: **"If there are only costs, why use
defect prediction at all?"** The answer on the slide is that there are always costs and the goal
is to minimize them — the trivial models (no prediction at all) define that floor.

The chapter rests on a distinction the slides make crisply: **"Costs for correction can be
ignored, as they are required to be spent regardless of whether defects are predicted or reported
by users."** That is why `cost_DEF` in the formula is the *loss from missed defects*, not the
cost of fixing what was found.

Two references carry the chapter: S. Herbold, "On the Costs and Profit of Software Defect
Prediction", *IEEE TSE* 47(11), 2617-2631, 2021, and Steffen Tunkel, Steffen Herbold, "Exploring
the relationship between performance metrics and cost saving potential of defect prediction
models", *Empirical Software Engineering*, 2022.

## Formal Definition / Statement

**The general cost model**, as printed:

```
cost = C_INIT + C_EXEC + Σ_{s∈S: h_s=1} qa_s + Σ_{d∈D_MISS} loss(d) + Σ_{d∈D_PRED} q_fd · loss(d)
```

where, per the slides:

- `cost_INIT = C_INIT` — maintenance of the model; "Modelled as constants!"
- `cost_EXEC = C_EXEC` — running predictions; "Modelled as constants!"
- `qa_s` — "Quality assurance costs for" software artifact `s` (e.g., class, file, or defective
  commit), summed over `s ∈ S: h_s = 1`, the artifacts predicted as defective
- `loss(d)` — the loss due to defect `d`; "Probability of not finding d"
- `q_fd` — the probability of not finding defect `d`; applied to `d ∈ D_PRED` (predicted), while
  `d ∈ D_MISS` (not predicted) contributes `loss(d)` unconditionally

The "Costs for Finding and Fixing Defects" slide splits this: `cost_QA = Σ_{s∈S:h_s=1} qa_s` is
the cost of quality assurance on predicted-defective artifacts; `cost_DEF = Σ_{d∈D_MISS} loss(d)
+ Σ_{d∈D_PRED} q_fd · loss(d)` is the cost of the defects themselves — "Missed = Not found", "Less
post-release bugs or not predicted".

**Initial and execution costs.** The slide is emphatic: "Determined by tool market", "Independent
of predictions!", "Modelled as constants!" — that is, independent of the software market *and*
of the prediction model.

**Trivial models.** Two baselines, printed with the same summations:

- Same QA for everything (`cost_all`): QA is applied to all artifacts, so `h_s = 1` for every
  `s ∈ S`.
- No quality assurance (`cost_none`): QA is applied to nothing, so no `qa_s` term appears.

The slides print both with the same formula skeleton, differing only in the label.

**Profit.** "Profit in relation to same QA for everything", as printed:

```
profit = cost_all − cost
       = Σ_{s∈S: h_s=0} qa_s − C_INIT − C_EXEC − Σ_{d∈D_MISS} (1 − q_fd) · loss(d)
```

The slide labels the two parts: the first sum is "Saved QA costs", the second is "Costs for
defects that are now missed". The `h_s = 0` set is exactly the artifacts the model declared clean
and therefore no longer quality-assured.

**Estimating `qa_s` and `loss(d)`.**

```
qa_s = C_QA · size(s)          ("Usually unknown")
loss(d) = C_DEF                 ("Mean costs per defect")
```

"Can be considered as ratio!": if `C = C_DEF`, then `C_QA / C = 1` and `qa_s = size(s)`;
symmetrically `loss(d) = C` per defect. The slide's third form is "Defect costs per 'size unit'".

**The mandatory condition.** "Defect prediction is only better than a trivial model, if" — the
printed condition is:

```
|D| · σ_{d∈D_PRED}(1 − p_qf)  <  C  <  |D| · σ_{d∈D_MISS}(1 − p_qf)
```

with `σ_{s∈S:h_s=1} size(s)` and `σ_{s∈S:h_s=0} size(s)` also printed on the same slide as the
size terms on each side. The slide's takeaway: "Only requires a rough estimation of C to know if
cost saving is possible!"

**Model performance metrics**, listed on the slide: precision, recall, F-measure, G-measure,
MCC (Matthews Correlation Coefficient), "N of I-80%", "N of B-20%", Area Under the LOC/Bugs
Curve, Area Under the Curve. Beside them the question: "Can I see the profit through these
metrics?" — answered with "No" and "RQ: Are metrics and costs correlated?!"

**The generalisation study.** Two kinds of models are built: within-project models based on
bootstrap samples ("Used to model relationship between metrics and costs"), and cross-project /
cross-version models ("Used to determine if modelled relationship generalizes"). The results: in
bootstrap data, "Log-normal distributions of cost saving potential", "Mean at about 1000 LOC",
"Almost no negative cost savings"; in realistic settings, "In general similar, but now we have a
mirrored log-normal distribution for negative cost-saving potential, i.e., losses", with "Models
without cost-saving potential (none) are typically trivial models, e.g., predicting no defects at
all". The verdict slide: **"Correlations between variables do not generalize!"** — in bootstrap
data "Works!", but "knowledge strongly correlated with confounder: bias in test data", where "bias
means class level imbalance, i.e., there are much fewer defective artifacts than clean ones".
Generalization "Does not work!" and "Also does not work between cross-version and cross-project!"
The stated reason: **"Because costs vary strongly between instances! Only cost modeling captures
this!"**

## Key Properties

- **Cost, not accuracy, is the objective.** The metric list ends with "No" for the question
  whether the profit is visible in the metrics.
- **Correction costs are constant and therefore drop out.** They are paid whether or not a model
  exists.
- **`C_INIT` and `C_EXEC` are constants of the tool market.** They are "Independent of
  predictions!", which makes the profit formula decompose into a savings term and a loss term.
- **A defect that is predicted is not a defect that is found.** `q_fd` is the probability of not
  finding `d` *even though it was predicted*; only missed defects contribute `loss(d)`
  unconditionally.
- **QA cost is paid per artifact, and the model's job is to shrink the QA set.** `Σ_{s:h_s=1} qa_s`
  is what the model controls; `Σ_{s:h_s=0} qa_s` is what it saves.
- **Profit can be negative.** The realistic-settings distribution is mirrored, i.e. there is a
  mass of losses; a model can make things worse.
- **The trivial models define the floor.** `cost_all` and `cost_none` bracket the achievable
  range; a prediction model has to beat them.
- **Size is used as a proxy for cost.** "The cost model computes the costs for both individually,
  based on size — Size is a proxy here for the costs, i.e., an indirect measure which comes with
  some threats to validity."
- **The other metrics assume a homogeneous cost world.** "The other metrics (mostly) rely on the
  confusion matrix which assumes that all missed bugs costs the same and all quality assurance
  measures cost the same."
- **Correlations found on bootstrap data are artefacts of the sampling.** "bias in test data" —
  class imbalance — is named as the confounder that makes the bootstrap relationship look real.

## Worked Example

The lecture's worked example for the metric-versus-cost question is the **LOC/bugs curve**, which
appears in the metric list as "Area Under the LOC/Bugs Curve" and in the plotting slides as the
"Bootstrap data" and "Realistic settings" comparisons, with "Dashed lines at 1,000 and 10,000"
and, in the realistic-settings plot, an "additional dashed line at 0".

Read through the model: the horizontal axis is size (LOC) and the vertical quantity is the cost
saving potential of a model trained and evaluated at that size. The bootstrap-data curve is
log-normal with its mean around 1,000 LOC and "Almost no negative cost savings" — every point of
that curve predicts profit. The realistic-settings curve is *mirrored*: it has a mass of negative
cost-saving potential (losses), and the models with no cost-saving potential at all are the
trivial ones ("predicting no defects at all"). The difference between the two curves is the
lesson: a metric/cost correlation discovered on bootstrap data does not survive in realistic
settings, because there the class imbalance is real and costs vary strongly between instances.

The arithmetic illustration the slides give for the estimation shortcut: if `C = C_DEF` then
`qa_s = size(s)` and `loss(d) = C`, so the mandatory condition becomes a comparison between the
total size of the QA'd set, the total size of the clean set, and `C` scaled by the number of
defects — and "Only requires a rough estimation of C to know if cost saving is possible!". That
is the practical point of the model: you do not need precise costs, you need to know which side
of the inequality you are on.

## Common Pitfalls

- **Comparing models by AUC and assuming the better one is the cheaper one.** "Can I see the
  profit through these metrics?" — "No".
- **Counting the cost of fixing found defects as a benefit of prediction.** "Costs for correction
  can be ignored, as they are required to be spent regardless".
- **Forgetting `C_INIT` and `C_EXEC` when computing profit,** or treating a predicted defect as
  a fixed defect. `q_fd` is the probability of *not* finding a predicted defect; ignoring it
  inflates the benefit of prediction.
- **Believing a bootstrap-derived correlation generalizes.** "Correlations between variables do not
  generalize!", and the reason is "Because costs vary strongly between instances!".
- **Ignoring class imbalance as a confounder.** "bias in test data" is what makes the bootstrap
  relationship look real.
- **Treating size as a cost measurement.** The slides label it an "indirect measure which comes
  with some threats to validity".

## Connections

- [[defect-prediction]] — the pipeline whose economics this page prices.
- [[software-metrics]] — where `size(s)` and the LOC-based metrics come from.
- [[msr-statistical-methods]] — the significance and effect-size machinery that does *not* answer
  the profit question.
- [[threats-to-validity]] — the slides' own caveat that size-as-cost is a proxy with validity
  threats.
- [[msr-tool-building]] — turning a prediction into a tool whose cost-benefit can be argued.
- [[evidence-based-software-engineering]] — the framing of evidence as a decision aid.
- [[mining-software-repositories-lecture-6]] — the source lecture for this page.

## Open Questions
- **The mandatory condition is ambiguous as printed.** The slide renders it as
  `|D| · σ_{d∈D_PRED}(1 − p_qf) < C < |D| · σ_{d∈D_MISS}(1 − p_qf)` while separately printing
  `σ_{s∈S:h_s=1} size(s)` and `σ_{s∈S:h_s=0} size(s)` as the size terms. The extracted text does
  not establish unambiguously which quantities sit on which side of the inequality, nor whether
  `p_qf` and `q_fd` denote the same quantity. The formulas are quoted as printed.

- **The `cost_all` and `cost_none` formulas are printed essentially identically** to each other
  and to the general cost model, with only the label distinguishing them. The intended
  difference — the set of artifacts receiving QA — is inferred from the labels and the
  surrounding bullets, not legible from the formulas.

- **How `qa_s` and `loss(d)` are estimated in practice is never specified.** The slides say
  `qa_s` is "Usually unknown" and offer the ratio trick, but no method for obtaining `C_QA` or
  `C_DEF` from a project is given, and no example with actual numbers appears.

- **The threshold at which `profit = 0` is never tied to a decision.** The model computes a profit
  but no magnitude of profit is stated as justifying deployment, nor is it said who bears
  `C_INIT`.

- **The scope of the generalisation failure is not bounded.** The slides show that metric–cost correlations from bootstrap data do not generalise cross-project or cross-version, but do not say whether *any* relationship survives in realistic settings.

- **A defect in a predicted-defective artifact can still be missed** (`q_fd`), so the partition of defects and the partition of artifacts are two different cuts, and the slides do not state how a missed defect inside a predicted-defective artifact is accounted for.
