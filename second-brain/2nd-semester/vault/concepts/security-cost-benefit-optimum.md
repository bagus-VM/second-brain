---
title: "The Cost-Benefit Optimum in Security"
tags: [concept, advanced-it-security, semester-2]
course: "Advanced IT Security"
source_count: 1
status: current
last_updated: 2026-10-20
prerequisites: ["[[security-policy-mechanism-assurance]]"]
---

## One-line Summary
The optimal security level is the point where the cost of security-enhancing mechanisms and the expected cost of violations cross — and it lies strictly inside the range, well short of 100% security.

## Core Intuition

The lecture's "Cost vs. benefit" slide is a hand-drawn graph, and the exam-relevant content is in its geometry, not in its labels. Three curves share one pair of axes, and two of them are the components of the third. Reading the figure as "the two curves cross, so that is the optimum" is close, and wrong in a way the drawing deliberately makes visible: the *crossing point* of the two component curves and the *minimum* of the total-cost curve are at different x-positions, with the optimum slightly to the right of the crossing.

The intuition behind that offset is the mechanism cost. At the crossing, the marginal spending on security exactly equals the marginal saving on violations. The total-cost curve's minimum is where the *slopes* balance, and because the mechanism-cost curve is convex — it steepens as you push security further — the balance point sits a little to the right of the crossing. Past the optimum, each additional unit of security costs more than it saves; before it, each unit saves more than it costs.

The broader framing comes from the "What does Security Mean?" slide: security is a relative notion, measured by how much effort (time, money, …) an attacker must invest to compromise a system, and the cost/benefit ration of security investment is a must. This page is that ration, drawn. The second half of the intuition is that the optimum is not 100% security: at the right end of the x-axis the mechanism cost has climbed far above the violation cost, which has decayed to nearly zero. The optimum is interior.

## Formal Definition / Statement

**Axes.** x = Security level, with a tick marked "100%". y = Cost.

**The three curves, as drawn.**

1. **Expected total cost** — U-shaped. High on the left (nothing protected, everything a
   violation), dipping to a minimum, then rising steeply to the upper right. The minimum is marked
   with a small circle on a vertical dotted line; the right-hand branch is drawn **dashed
   (dash-dot)**.
2. **Cost for security enhancing mechanisms** — monotonically increasing and convex: it leaves
   the origin almost flat and steepens as it goes right.
3. **Expected total cost for violations** — monotonically decreasing, falling from the upper left
   to nearly zero at the right.

**The precise geometry.** The two lower curves — mechanism cost and violation cost — **cross each
other below the minimum of the total-cost curve**. That minimum sits **slightly to the right of
the crossing**, at the marked circle on the vertical dotted line, whose x-axis label reads
"Optimal level".

```
  Cost
   ^                                    . - - - .      Expected total cost
   |                              . - -'           ' -.   (dashed right branch)
   |                        . - -'
   |                 . ----'
   |        .------'          . . . . . .           Cost for security
   |    .--'              . -'                 . -.   enhancing mechanisms
   |  .'        . -----'                  .-'
   | .'    . --'  <-- crossing          .-'
   |.'  .-'                            /
   |  .'                         .---'      Expected total cost
   |.'                      .--'            for violations
   +--------------------------------------------->
   |      |                |   |        |  100%
   |      |                |   |        |
   |      |          crossing  (o)  Optimal level
   |      |                |   |
   +--------------------------------------------->
                    Security level
```

Read the figure as: the dotted line through the circle marks the optimal security level, the
total-cost minimum is on that line, and the crossing of the two component curves is to the *left*
of it and *below* the minimum.

**Relation to residual risk.** The risk slide states that there always remains a residual risk, and
the cost figure agrees: risk is never driven to zero, so the violation-cost curve never truly
reaches zero either, and the "optimal" point is a trade, not a solution.

## Key Properties

- **The optimum is a cost minimum, not a maximum-security point.** 100% security is on the axis to show how far past the optimum it lies: there the mechanism cost stands far above the violation cost.
- **Two component curves, one total curve.** The expected total cost is the sum of the mechanism cost and the violation cost. The U-shape is the sum of a rising and a falling function; that is why the minimum is interior.
- **The crossing and the minimum are not the same x-position.** This is the detail the drawing encodes and the most common exam miss. At the crossing the two component costs are equal in value; at the minimum of the total curve the two *derivatives* balance. The optimum lies slightly to the right of the crossing.
- **The dashed branch is the over-investment region.** The dash-dot right-hand branch marks where each further unit of security costs more than the violations it removes. It is a warning, not an alternative design.
- **Marginal reasoning, not average reasoning.** The decision is made at the margin: does the next unit of security save more than it costs? Averages mislead, because the two curves are monotone in opposite directions. Since risk never reaches zero, neither does the violation cost, and the trade-off is permanent.
- **The graph is a decision aid, not a model.** Hand-drawn, unquantified, axis-free beyond the 100% tick. It gives the *shape* of the decision, never the *number* of your optimum. Moving right means the attacker must invest more effort; the mechanism curve prices the defender's side.

## Worked Example

Take a concrete system and put numbers on the shape — the lecture's figure gives no numbers, so the arithmetic below illustrates the geometry rather than deriving it from the deck.

**Scenario.** A research institute stores student examination results on a file server. Two investments are on the table: (A) full-disk encryption, (B) read-access control with per-student access logs. Take the following annual cost model, in arbitrary currency units, with security level s ∈ [0, 1]:

- Expected total cost of violations: V(s) = 4000 − 4000·s. (At s = 0, 4000 units of expected loss; at s = 1, zero.)
- Cost of security-enhancing mechanisms: M(s) = 2500·s² + 500·s. (Convex: at s = 0.5, 875; at s = 1, 3000.)

**Step 1 — the crossing of the two component curves.** Set M(s) = V(s):

2500s² + 500s = 4000 − 4000s
2500s² + 4500s − 4000 = 0
s = [−4500 + √(4500² + 4·2500·4000)] / (2·2500) = [−4500 + √60 250 000] / 5000
√60 250 000 ≈ 7762.1, so s ≈ (3262.1)/5000 ≈ 0.6524.

At the crossing, M = V ≈ 1390 units, so the total cost there is ≈ 2781.

**Step 2 — the minimum of the total cost curve.** T(s) = M(s) + V(s) = 2500s² − 3500s + 4000. T′(s) = 5000s − 3500 = 0 ⇒ s* = 0.70. T″ = 5000 > 0, so this is the minimum. T(0.70) = 1225 − 2450 + 4000 = 2775. And M(0.70) = 1225 + 350 = 1575; V(0.70) = 4000 − 2800 = 1200.

**Step 3 — the geometry against the lecture's figure.** The crossing is at s ≈ 0.6524; the minimum of the total curve is at s* = 0.70. The optimum sits to the **right** of the crossing, by roughly 0.048 in security level. At the crossing the total cost is ≈ 2781, at the optimum ≈ 2775 — about 6 units less, a marginal improvement in value, but a different *position*. The hand-drawn figure draws the crossing and the marked minimum at the same point, so this offset is an arithmetic consequence of the convex mechanism-cost curve, not something the figure resolves on its own.

**Step 4 — the 100% check.** At s = 1: M = 3000, V = 0, T = 3000 — 225 units *more* than at the optimum, buying zero additional reduction in expected loss. The 100% tick is on the axis so the reader can see that mechanism cost has run far above the now near-zero violation cost. The optimum is strictly interior.

**Step 5 — the residual.** Even at s = 0.70, V = 1200 units of expected violation cost remain. The lecture's statement that a residual risk always remains is the same fact: risk is reduced, never eliminated.

## Common Pitfalls

- **Saying "the optimum is where the two curves cross" and stopping.** The lecture's figure places the minimum of the total-cost curve slightly to the *right* of that crossing, on the vertical dotted line labelled "Optimal level". The crossing is where the two component costs are equal; the optimum is where the total is smallest.
- **Drawing the optimum on the 100% tick.** The tick shows the far end of the range, where mechanism cost has climbed far above violation cost. Maximum security is maximum cost, not the answer.
- **Reading the dashed branch as "the curve continues like this".** The dash-dot right-hand branch marks over-investment, where additional security costs more than it saves.
- **Treating the figure as quantitative.** It is a hand-drawn conceptual graph with one labelled tick. It gives shape, not numbers, and the lecture supplies no function for any of the three curves.
- **Forgetting that "cost" includes assurance.** The mechanism-cost curve is where evaluation and assurance effort is charged.
- **Assuming risk reaches zero at the optimum.** The risk slide's residual-risk statement says otherwise.
- **Confusing the x-axis with attacker effort.** Moving right means the attacker must invest more effort; the graph prices the defender's side of that bargain.

## Connections

- [[security-policy-mechanism-assurance]] — the mechanism-cost curve is where the policy/mechanism/assurance deliverables are paid for, and assurance is the expensive part.
- [[security-relationship-model]] — risks indicate protection requirements, and the requirements are what this figure prices against the value of the assets.
- [[security-evaluation-and-assurance-levels]] — evaluation and assurance are part of the security cost the optimum must account for.
- [[risk-perception-and-dread-risk]] — the same curve read psychologically: perception distorts where on the x-axis the organisation actually lands.
- [[security-terminology-and-risk-model]] — the same cost/benefit ration at glossary level rather than graph level.
- [[risk-assessment-frameworks]] — the procedures that produce the numbers a real optimum calculation needs.
- [[cia-triad]] — the protection goals whose failure produces the violation-cost component of the total.

## Open Questions

- The figure gives no functional form for any of the three curves, no units, and no data. Whether the course later supplies a quantitative model is not stated in lecture 0.
- The vertical dotted line, the circle and the "Optimal level" label are the only precise markers, and the source is a hand-drawn graph. The exact relative offset between the crossing and the minimum cannot be read quantitatively — only its direction and its smallness are reliable.
- Whether the total-cost curve's minimum is always to the right of the crossing, or only in the convex case drawn, is not discussed. With a concave mechanism-cost curve the offset would reverse.
- The relationship between the optimum and the residual-risk statement is asserted by adjacency on the slides rather than argued. Whether "optimal" includes the residual in the objective, or treats it as a separate acceptance decision, is not said.
