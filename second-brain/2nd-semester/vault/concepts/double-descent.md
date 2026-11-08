---
title: "Double Descent"
tags: [concept, introduction-to-deep-learning, semester-2, machine-learning, generalization]
course: "Introduction to Deep Learning"
source_count: 1
status: current
last_updated: 2026-10-23
prerequisites: ["[[polynomial-regression-and-overfitting]]"]
---

## One-line Summary
The classical story says validation error is U-shaped in model capacity; double descent is the modern
observation that past the point where the model fits the training data, error comes down again — so
"bigger models overfit" is not the whole truth.

## Core Intuition

The classical picture is a trade-off with a right answer. A model too simple cannot represent the
data (underfitting, high error on both training and validation); a model too flexible starts fitting
the noise (overfitting, low training error and high validation error); in between there is a minimum,
and you pick the capacity there. Every textbook bias-variance curve looks like this, and it is why
regularisation and early stopping are taught in the same breath.

The lecture then puts a second curve next to it and points out that the U is only half of the story.
Plot error against **parameters per training instance** instead of raw capacity, and once the model
has enough parameters to interpolate the training data exactly, test error does not merely stall —
it peaks and then falls again. The peak is the **interpolation threshold**; the second fall is the
**double descent**. The regime beyond the threshold is exactly the regime that classical wisdom says
to avoid, and it is where modern networks live.

Why it matters for the course: the deep-learning model class is not exhausted at the interpolation
threshold. A network with more parameters than training points still has many parameter settings that
fit the data, and that surplus is where generalisation comes from. The lecture flags it as the
exception that makes the classical advice insufficient rather than wrong.

## Formal Definition / Statement

**Classical view (slide 23, left curve).** With model capacity on the x-axis (e.g. number of
parameters), training error falls monotonically and validation error is U-shaped. Choose the capacity
with the lowest error on held-out validation data.

**The lecture's counter-curve (slide 23, right).** x-axis: **parameters / training instances**.
Test error falls, meets the training-error curve at the **interpolation threshold** — where the model
fits the training data perfectly — and then falls again on the other side.

Slide's own wording: "**Deep learning: 'double descent' — very large networks fit the training data
perfectly and still generalize well.**"

**The two citations on the slide:**

- Belkin et al., *Reconciling modern machine-learning practice and the classical bias-variance
  trade-off*, PNAS, 2019.
- Nakkiran et al., *Deep Double Descent: Where Bigger Models and More Data Hurt*, ICLR, 2020 —
  labelled on the slide as the source of the (schematic) curves.

**Underfitting and overfitting, for contrast (slide 22):** overfitting is "adapting too precisely to
the training data (including its noise)", "learning by heart": good on training data, bad on new data.
The classical trigger is "too many parameters compared to the number of data instances". Underfitting
is the opposite — the model is too simple to capture the structure of the data.

## Key Properties

- **The threshold is the interesting place.** Everything classical happens before it; everything
  surprising happens at and after it.
- **The x-axis matters.** "Model capacity" gives the U-shaped curve; "parameters per training
  instance" gives the descent-descent curve, because the second axis moves as the dataset grows.
- **The two descents are different phenomena.** The first fall is classical approximation; the second
  occurs in a regime where the model already fits the training data exactly, so it cannot be about
  approximation at all.
- **The threshold is a peak, not a wall.** Error does not stay high past it, which is what the
  classical view would predict.
- **More data can hurt.** Nakkiran et al.'s title is not decoration: in this framing, moving a task
  closer to the threshold by changing the data can raise error.
- **The lecture labels its curves "schematic".** No dataset, architecture or measurement is given on
  the slide — the evidence is the two papers.
- **It does not cancel overfitting as a concept.** Slide 22 still teaches underfitting and overfitting
  as the classical frame, and the polynomial exercise still shows textbook overfitting; double descent
  is stated as the deep-learning exception.

## Worked Example

Computed in `study/homework/introduction-to-deep-learning/idl-lecture2-numbers.py`, section 4: 15
training points drawn from sin(2·pi·x) with Gaussian noise (sd 0.15), polynomials of increasing degree
fitted by least squares in a centred basis (x' = 2x − 1), tested on a 401-point grid.

| Degree | Parameters | Train MSE | Test MSE |
|--------|-----------|-----------|----------|
| 1 | 2 | 2.150e-01 | 2.122e-01 |
| 3 | 4 | 1.318e-02 | 8.132e-03 |
| 5 | 6 | 4.186e-03 | **3.281e-03** |
| 8 | 9 | 3.395e-03 | 5.133e-03 |
| 11 | 12 | 1.659e-03 | 1.183e-02 |
| 13 | 14 | 4.593e-04 | 4.708e-01 |
| 14 | 15 | **1.172e-14** | **4.547e+00** |
| 15 | 16 | singular — basis exhausted | |

Read it as three regions:

1. **Before the threshold**: test error falls to a minimum at degree 5 (6 parameters), which is the
   classical story, and the minimum is at a capacity well below the number of training points.
2. **Approaching it**: test error climbs by three orders of magnitude from degree 5 to degree 14.
3. **At it**: degree 14 has 15 parameters for 15 points and interpolates exactly (train MSE 1.2e-14,
   i.e. numerically zero) while test MSE is 4.547 — **1386 times the minimum**.

**The honest result: this experiment does not reproduce a second descent, and the reason is
structural.** A degree-`(n−1)` polynomial through `n` points is fully determined, so the model class
*ends* at the interpolation threshold; there is no further capacity to grow into. Past the threshold
in the double-descent sense means "more parameters than data points while still many solutions fit
the data", and a fixed polynomial basis cannot express that. This is not a numerical artefact — the
`singular` row for degree 15 is the basis being exhausted, not a failure of the fitter. The
double-descent curves in the cited papers are neural-network curves, where the parameter count can
pass the number of training points without the function class being used up. The lecture's own
caption ("schematic curves") is consistent with that.

Two smaller things this experiment does show, which are worth keeping: the fit has to be done in a
**centred basis** — with raw monomials on a uniform grid the moment matrix loses numerical rank around
degree 10 and the computation fails in double precision — and the classical minimum appears at
**roughly n/2 parameters, not n**.

## Common Pitfalls

- **Reading the U-shaped curve as the whole truth.** It is the picture before the interpolation
  threshold, and the lecture is explicit that the deep-learning regime lies beyond it.
- **Concluding "more parameters are always better".** Double descent says error falls again past the
  threshold; it does not say the minimum is past the threshold. In the experiment above the minimum
  was at 6 parameters out of 15 points.
- **Confusing the two descents.** The first is approximation; the second happens where the training
  error is already zero, so the classical bias explanation cannot apply.
- **Trying to reproduce it with a model class that is exhausted at interpolation.** The polynomial
  case is exactly that trap, and it is the most common way to "fail" to observe double descent.
- **Treating the lecture's curve as data.** The slide says schematic and cites two papers; the shape
  is imported, not measured in the course.
- **Dropping regularisation and early stopping because "bigger is fine".** They address the region
  before the threshold, which is still most of applied practice.
- **Assuming the threshold is at parameters = instances in every architecture.** The slide's axis is
  parameters per training instance, but where a given model family interpolates depends on the family.

## Connections

- [[polynomial-regression-and-overfitting]] — the classical framing, and the exercise where training
  and validation loss are compared across degrees 1/2/3/9.
- [[loss-functions-and-empirical-risk]] — the empirical risk that goes to zero at the threshold.
- [[cross-validation]] — how the validation curve is actually measured, and why one split is a noisy
  estimate of it in this exact region.
- [[neural-network-training-loop]] — the regime on the right-hand side of the curve.
- [[representation-learning]] — the property that lets a network keep fitting the data with more
  parameters than points without the class being exhausted.
- [[ml-data-and-iid-assumption]] — "Where Bigger Models and More Data Hurt" is a statement about the
  data axis, and about what more data does to the position of the threshold.
- [[introduction-to-deep-learning-lecture-2]] — the lecture this page belongs to.

## Open Questions

- **The lecture gives the shape and no numbers.** No dataset, architecture, or measured curve; the
  slide labels its own curves schematic and cites Belkin et al. 2019 and Nakkiran et al. 2020.
- **The interpolation threshold is marked on the slide but never defined quantitatively** — not as a
  formula, and not as "parameters = instances" in so many words.
- **Why the second descent happens is not explained.** The lecture states the phenomenon; the
  mechanisms usually offered (implicit regularisation, the geometry of overparameterised solution
  sets) are outside its scope.
- **The polynomial demonstration is this vault's own and it fails to show the phenomenon** — recorded
  above as a structural limitation of the model class, not as a contradiction of the papers.
- **Whether the exam expects the two citations** is not stated; they are on the slide, so they are
  fair game for a "what is double descent and where does it come from" question.