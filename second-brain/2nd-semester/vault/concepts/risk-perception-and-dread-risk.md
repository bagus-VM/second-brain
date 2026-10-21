---
title: "Risk Perception and Dread Risk"
tags: [concept, advanced-it-security, risk, semester-2]
course: "Advanced IT Security"
source_count: 1
status: current
last_updated: 2026-10-20
prerequisites: ["[[security-terminology-and-risk-model]]"]
---

## One-line Summary
People judge risk by feeling, not by statistics — so the numbers that should govern a security
decision are systematically the numbers the decision-maker ignores.

## Core Intuition

Posegga opens lecture 0 of Advanced IT Security with a slide that has no cryptography on it:
*"People perform extremely poorly with managing technical risk."* The point is that this is not a
softness of individuals, it is a property of human risk perception. Fear of spectacular, unlikely
events; suspicion of anything new; suspicion of anything invisible; and the constant confusion of
correlation with causality. Security engineering that ignores this fails not because the mechanism
is wrong but because the budget it gets is allocated by a distorted signal.

This is the uncomfortable part of the course, because it sits next to the cost/benefit curve. That
curve says the optimal security level is where the expected total cost is minimal. The risk
perception material says the level actually chosen will be far from the optimal one, and that the
gap is systematic, not random. So the engineer's job is not only to compute the optimum but to
predict and manage the distortion.

The four listed biases are a compact taxonomy of *how* perception fails:

- **Spectacular versus routine.** A rare, vivid, catastrophic event dominates attention far beyond
  its frequency.
- **Novelty.** Anything new is suspicious — which is exactly the register that a new technology
  triggers, whether it is a new protocol or a new attack.
- **Invisibility.** What you cannot see, you fear more. A remote attack with no observable trace
  produces more perceived risk than a comparable local failure.
- **Correlation read as causation.** Two things that co-occur get treated as one causing the other.

## Formal Definition / Statement

**The cost/benefit model.** Security is a trade-off, and the optimum is where the two cost curves
cross. From the lecture's "Cost vs. benefit" figure, as a function of the *security level* on the
x-axis and *cost* on the y-axis:

- **Expected total cost** is U-shaped: it starts high (everything is a violation, nothing is
  protected) and rises again at the far right (mechanisms cost more than the losses they prevent).
- **Expected total cost for violations** falls monotonically as security increases.
- **Cost for security enhancing mechanisms** rises monotonically as security increases.
- The two cross at the **optimal level**, marked on the axis, and the expected total cost has its
  minimum there. The curve is drawn dashed beyond that point, marking the region where
  over-engineering costs more than it saves. (The crossing and the marked minimum are drawn at
  the same point; see [[security-cost-benefit-optimum]] for what the arithmetic says about the
  gap between them.)

**The perception model.** The lecture cites Paul Slovic, *The Perception of Risk* (Earthscan, 2000),
for the following claims about how people actually manage technical risk:

1. Risk and emotion are inseparable.
2. We fear spectacular, unlikely events.
3. Anything new is suspicious.
4. Anything invisible is suspicious.
5. Correlation is often confused with causality.

## Key Properties

- **The optimum is a cost minimum, not a "maximum security" point.** A system at 100% security
  costs more than the violations it prevents; the lecture's figure marks 100% on the axis and draws
  the rising mechanism-cost curve through it.
- **Perceived risk and actual risk are different quantities.** The lecture's own exercise asks which
  is more common, suicide or homicide; who has the higher risk of being murdered, women or men; which
  of cancer and heart disease kills more women; what the top cause of accidental death in America
  is after motor-vehicle accidents (drug overdose). Each answer contradicts the lay intuition, and
  the exercise is the argument.
- **The exposure base changes the comparison, which is why the lecture normalises.** Risk per
  *exposure* — per flight, per trip, per billion kilometres — is the only way to compare modes of
  transport. Absolute fatality counts are dominated by how many people use each mode.
- **Probability and dread are weighted differently.** The lecture's numbers are the standard
  dread-risk pair: the per-flight commercial-airline death risk over 2000–2007 was about 1 in
  80 million, and the per-trip car-crash risk for an average American 6-mile car trip was about
  1 in 14.6 million — yet roughly 95% of people involved in a plane crash survive it, and
  shark attacks kill around 10 people a year worldwide against about 150 killed by falling coconuts.
  People still perceive flying as far more dangerous than driving, because the aviation accident
  is vivid and visible and the car crash is routine.
- **The same normalisation kills the "rail is safest" intuition.** German 2008 deaths per billion
  kilometres per year (OECD): rail 0.2, air 0.4, car 6, bicycle 30, pedestrian 38, motorcycle 45.
  Driving is the second-lowest figure in that table, and it is the one everybody takes every day —
  invisible, because nobody photographs a commute.
- **Management failure has a cause.** The headline claim is not "people are bad at probabilities" —
  it is that they manage technical risk badly, because the perception mechanism is systematically
  wrong in specific, nameable ways. That makes it a design constraint on the security engineer,
  not an excuse.

## Worked Example

**Reading the lecture's own numbers.** The lecture asks: "What's more common in the United States,
(a) suicide or (b) homicide?" and then supplies the global breakdown of murder victims as female
21%, male 79%. Note the structure of the question: the global figures are given, and the student is
expected to notice that the per-capita answer differs from the raw-count intuition. The slide's
follow-up — "Who has a higher risk of being murdered: Women or men?" — is the same move again.
Both questions are about the *denominator*.

**The transport comparison, normalised.** The lecture's German figures (deaths per billion km per
year, 2008) put air at 0.4 and car at 6 — a factor of 15. The US figures put the per-flight
aviation risk at 1 in 80 million and the 6-mile car trip at 1 in 14.6 million — the same
order of magnitude, in both directions depending on which base you pick. Now put the *dread*
figure next to it: about 95% of plane-crash occupants survive, and the everyday killer on the
road is someone else entirely. The statistical case says car travel is the more dangerous act;
the perception says the plane. The gap between those two statements is the entire content of this
page.

**The cost curve as a decision procedure.** Suppose the expected cost of violations falls roughly
linearly with security level and the cost of mechanisms rises roughly linearly too. Then expected
total cost is V-shaped, the optimum is where the slopes balance, and the decision is: *where do
the two marginal curves cross?* The lecture's figure draws the right-hand branch dashed precisely
to say that past the crossing point each additional unit of security costs more than the
violations it removes. This is the operational answer to the risk-perception problem — the
engineer computes the optimum, and the *management* case for stopping there is made explicitly,
rather than assuming the optimum will be selected by default. It is not.

## Common Pitfalls

- **Confusing perceived risk with real risk, in either direction.** The exam trap is symmetric:
  both "flying is dangerous" and "people are irrational, ignore it" are wrong. The lecture's
  position is that perception is *systematically distorted*, not that it is absent.
- **Comparing absolute counts instead of rates.** "Shark attacks kill ~10 a year" says nothing on
  its own; "~150 people die from coconuts" says nothing on its own. The comparison needs a base.
- **Reading "1 in 8 million" as reassurance about the *system*.** It is reassurance about the
  *per-flight* rate. A frequent flyer takes many flights; the per-flight number and the
  per-year number differ by orders of magnitude. The lecture's own framing is per-flight and
  per-trip for this reason.
- **Missing that the "Cost vs. benefit" figure has a minimum, not a plateau.** There is one
  optimal security level. Spending past it is not prudence, it is waste — and the dashed branch
  says so.
- **Treating the five perception claims as generic psychology.** They are a named framework
  (Slovic) applied to *technical* risk management, which is what makes them usable in a security
  argument rather than an aside.
- **Assuming risk perception explains everything.** It explains budget allocation and uptake.
  The mechanism-level questions — what the policy is, what the mechanism does, whether it is
  assured — are settled by the risk model, not by the psychology.

## Connections

- [[security-terminology-and-risk-model]] — the vocabulary this page applies: assets, threats,
  vulnerabilities, safeguards, and the residual risk that never goes to zero. Also the
  cost/benefit framing and the policy/mechanism/assurance triple, all from the same lecture family.
- [[risk-assessment-frameworks]] — the standards-based, formalised version of the risk vocabulary:
  where a structured method replaces the ad-hoc reasoning this page describes.
- [[cia-triad]] — the protection goals whose failure the perceived risk is really about; the
  lecture's own definitions of confidentiality, integrity and availability are the ITSEC ones.
- [[availability]] — DoS and the "prevention is hard in real life" remark from the same lecture.
- [[attacker-classification]] — the other lecture (Machine Learning for Cybersecurity) that makes
  the same point from the attacker's side: risk depends on the attacker class, which is a
  cost/benefit question.
- [[security-by-design]] — the engineering practice that exists because perception cannot be
  relied on to allocate the budget.

## Open Questions

- The lecture presents the risk-perception claims as a research literature to be trusted (Slovic,
  2000) but does not give the study designs behind them. The German 2008 transport figures are
  attributed to OECD; the US figures (shark attacks, coconuts, 95% survival rate) are given without
  a source. Whether the course expects the specific numbers to be reproduced from memory, or only
  the qualitative argument, is not stated.
- The extraction of the PDF turns some slide values into placeholders: the shark-attack figure
  renders as "?10", the flight risk as "1 in 8?0? million" and the car-trip risk as "1 in 1?4?.6
  million". The rendered slide resolves them: 10, **80 million** and **14.6 million**. An earlier
  reading of "8–10 million" for the flight risk was a guess at a damaged character and was wrong;
  the slide is unambiguous once rendered.
- The "Cost vs. benefit" figure is a hand-drawn conceptual curve, not a quantitative model. Whether
  the course later formalises it — a linear cost model, a Brownian-threat model with an optimal
  stopping point, something else — is not stated anywhere in the material ingested so far.
- The lecture asserts that people manage technical risk poorly but does not say what a security
  engineer should concretely *do* about it: compensate for the bias, argue against it, or design so
  that the distorted preference is harmless. The lecture's later material on PKI and protocols may
  answer this; it is not in lecture 0.
