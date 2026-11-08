---
title: "Executing a Gradient Descent Step"
tags: [concept, deep-learning, semester-2, optimization, training-dynamics]
course: "Introduction to Deep Learning"
source_count: 2
status: current
last_updated: 2026-10-29
prerequisites: ["[[gradient-descent-for-neural-networks]]", "[[derivatives-cheat-sheet]]"]
---

## One-line Summary

A gradient descent step is three lines of arithmetic — read the gradient where you stand, scale it by alpha, subtract — and the same three lines converge, oscillate or run to infinity depending on alpha and on whether the surface has a minimum at all, so the mechanics rather than the formula is where the content is.

## Core Intuition

The session states the training problem as an optimisation problem — w' = argmin_w (1/n) Σ E(f(x_i; w), y_i), with f(x_i; w) = ŷ_i — and then states one geometric fact: the gradient points in the direction of the steepest local ascent. Everything else follows from that. You cannot see the loss surface, but you can measure its slope at the point you occupy, and stepping against the slope lowers the value at least in a neighbourhood of that point. Nothing about the surface elsewhere is known or used.

The slide's Example 1 shows the well-behaved case: f(x) = x², x0 = 1, α = 0.25. The recorded iterates are 1.00000000 → 0.50000000 → 0.25000000 → 0.12500000 → 0.06250000 → 0.03125000 → 0.01562500 → 0.00781250, converging to 0, the minimum. Each step halves the distance to zero because f′(x) = 2x halves when x halves: on this function the step sizes shrink automatically. That is a property of x², not of gradient descent, and the rest of the session is the evidence.

## Formal Definition / Statement

Slide 27 gives the loop. (1) Initialise the parameters w randomly. (2) Compute ∂E/∂w = [∂E/∂w_0, …, ∂E/∂w_k]^T. (3) Update w_i(t+1) ← w_i(t) − α ∂E/∂w_i(t) for i ∈ [0, k]. Steps 2 and 3 are repeated until convergence or some limit, and α, the learning rate, is "a small positive number (e.g., α = 0.001)".

The optimisation statement the loop serves (slide 25) is

w' = argmin_w (1/n) Σ_{i=1}^{n} E(f(x_i; w), y_i), where f(x_i; w) = ŷ_i,

so the free variables are the parameters and the objective is the error averaged over the data. [[gradient-descent-for-neural-networks]] covers why this iterative route is taken at all and the form of the update rule; the subject here is what executing it actually does.

Gradient ascent needs no new machinery (homework task 1(c)): run the identical loop with the sign flipped, x ← x + α ∇f(x), which is gradient descent on −f because ∇(−f) = −∇f. Every convergence property and every failure mode carries over unchanged.

## Key Properties

- **The gradient is local information only.** The step is computed from the derivative at the current point, so the procedure notices nothing about a minimum elsewhere, a distant floor, or the absence of a floor altogether. That is a strength on non-convex surfaces and the reason its failures are silent.
- **α decides whether the same slope helps or ruins.** On f(x) = 3x² − 1.25(x−1)⁴ + (x−2)⁶ at x0 = 3 the recorded derivative is −16.0000 in both of the configurations that start there. With α = 0.01 the next point is 3.160000, where f = 5.1834; with α = 0.1 the next point is 4.600000, where f = 162.4438. Identical slope, identical starting point, step size differing by a factor of ten, opposite verdict.
- **A minimum need not exist, and the loop does not check.** For f(x, y) = x²y + y² from (2, 4) with α = 1, the recorded gradients are (16.00, 12.00), then (224.00, 180.00), then (89488.00, 56268.00), then (10131142112.00, 8050642164.00). The slide's caption on the following page is the diagnosis: there is no minimum on this surface and "gradient descent happily runs off to −∞".
- **Descending is not converging.** Homework task 1(b) takes one step on g(x, y) = xy² − x³e^(x−y) + sin²(xy) from (1, 1) with α = 1: the gradient is (−2.090703, 3.909297), the next point is (3.090703, −2.909297), and f falls from 0.708073 to −11884.398381. The direction is a genuine descent — the file's own words — and the step is enormous; α = 1 overshoots far past any minimum. A falling loss after one step is not evidence that the run will converge.
- **Saddle points and sharp minima are the stated landscape pathology.** Slide 30 is titled "Issue: many saddle points, sharp minima, …" and credits Li et al., 2017, *Visualizing the Loss Landscape of Neural Nets*. The remedy on the next slide is not a better algorithm but a set of candidate models: differ the weight initialisation, the learning rate α, "and so on".
- **A two-step homework trace.** Task 1(a), f(x, y) = 3xy − 5y², from (0.0, 1.0) with α = 0.1 and f = −5.0: step 1 has gradient (3.0000, −10.0000) and lands on (−0.300000, 2.000000) with f = −21.800000; step 2 has gradient (6.0000, −20.9000) and lands on (−0.900000, 4.090000) with f = −94.683500. The value falls at every step while the point moves further from the start at every step; two steps are not enough to say which of the session's two examples this resembles, and the sheet does not say.

## Worked Example

The slide's own task (slide 34): one step of gradient descent on f(x) = 3x² − 1.25(x−1)⁴ + (x−2)⁶ in three configurations. The derivative, by the sum, constant-factor and chain rules of [[derivatives-cheat-sheet]], is

f′(x) = 6x − 5(x−1)³ + 6(x−2)⁵.

A finite-difference check of that derivative — the output file records a maximum relative error of 1.29e-11 — confirms the analytic form before it is used. At x0 = 2 the derivative is 7.0000 and at x0 = 3 it is −16.0000, both matching f′ above.

| x0 | α | f′(x0) | x1 = x0 − α·f′(x0) | f(x1) |
|---|---|---|---|---|
| 2 | 0.1 | 7.0000 | 1.300000 | 5.1775 |
| 3 | 0.01 | −16.0000 | 3.160000 | 5.1834 |
| 3 | 0.1 | −16.0000 | 4.600000 | 162.4438 |

The first two rows are the method working: a positive slope moves the point down to 1.3, a negative slope moves it up to 3.16, and in both cases the function value lands around 5.18. The third row is the point of the exercise: the same negative slope with a ten-times larger step sends x to 4.6, past the basin, where f = 162.4438 — worse than either starting point. One slope, one function, and the only difference between the second and third rows is alpha.

## Common Pitfalls

- **Reading a single descent as evidence of convergence.** In task 1(b) the value of g drops from 0.708073 to −11884.398381 in one step; a run that falls that far that fast is overshooting, not learning. A run is judged by its sequence of iterates, not by its first step.
- **Treating α as an afterthought.** The slide fixes it as "a small positive number", yet the tasks use α = 0.1, 0.01 and 1, and the third row of the table above is the same function and the same gradient as the second with α ten times larger and a completely different outcome.
- **Assuming a stationary point found is a minimum.** The loop's stopping rule is convergence, i.e. a gradient near zero, and the slide's own landscape figure shows what a gradient near zero can be: a saddle, a flat shelf or a sharp minimum rather than the global answer.
- **Assuming the loss has a minimum at all.** f(x, y) = x²y + y² has none, and the recorded iterates travel from (2, 4) to (−10131231838, −8050698620) in four steps without the loss ever bottoming out.
- **Trusting a computed gradient because it looks plausible.** The script behind these numbers reused one section's gradient variable in the next section, so a section printed the previous function's gradient until the finite-difference check caught it — the same kind of check the output file records as "max rel. err 1.29e-11 / 1.40e-10 / 5.21e-11 / 1.32e-11" for the four functions. A hand-rolled gradient is not trustworthy until an independent numerical derivative agrees with it.
- **Flipping the sign by accident.** Descent subtracts; ascent adds. Since ∇(−f) = −∇f, gradient ascent is not a new algorithm and does not need one.

## Connections

- [[gradient-descent-for-neural-networks]] — why gradient descent exists at all and the update rule w(t+1) = w(t) − α ∂E/∂w; this page takes that rule as given and works out what executing it does.
- [[derivatives-cheat-sheet]] — the rules used to produce every derivative on this page.
- [[pytorch-tensors-and-autograd]] — the same step with the gradient computed automatically instead of by hand.
- [[neural-network-training-loop]] — `optimizer.step()` is exactly this update, applied once per batch inside the five-step loop.
- [[loss-functions-and-empirical-risk]] — what E is, and why the average over the training data is the objective being minimised.
- [[linear-algebra-for-deep-learning]] — the gradient as a vector of partial derivatives, and the notation the update rule is written in.
- [[introduction-to-deep-learning-exercise-3]] — the session containing tasks 1(a)–1(c) and the single-step slide task.

## Open Questions

- **"Until convergence" is never defined.** No tolerance, no gradient norm and no iteration limit appears in the session, so it is not knowable from the material what counts as having converged; the only alternative offered is "or some limit".
- **No rule for choosing α.** The slide's example is α = 0.001, the tasks use 0.1, 0.01 and 1, and the same α that works in one task fails in another. For f(x) = x² the update contracts by the factor 1 − 2α, which reproduces the recorded halving at α = 0.25 and gives a non-converging alternation at α = 1 (background mathematics, not stated in the material); nothing in the slides gives such a bound for a general loss, which is what a student would need.
- **Why α = 1 in task 1(b)?** The slide calls α a small positive number and the task then uses the largest usable value. The file records that the step overshoots, so the task reads as a demonstration, but the sheet does not say whether a complete answer is expected to carry on iterating.
- **No criterion for telling divergence from slow progress at run time.** The task 1(a) trace and the Example 2 trace both show a falling function value with iterates moving away from the start; the material gives no test that separates them.
- **"Candidate models" is the only remedy offered** for saddle points and sharp minima, with no stated budget, selection rule or comparison metric.
- **Task 1(b) offers no closed-form check.** Its gradient involves sin(2) = 0.909297, which the file notes makes both coordinates irrational, and the sheet still asks only for one step.
