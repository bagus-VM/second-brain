---
title: "Security Evaluation and Assurance Levels"
tags: [concept, advanced-it-security, semester-2]
course: "Advanced IT Security"
source_count: 1
status: current
last_updated: 2026-10-20
prerequisites: ["[[security-policy-mechanism-assurance]]"]
---

## One-line Summary
Security evaluation asks whether a product delivers the security service it promised and states the degree of trust in that claim — and because deeper inspection costs more, complex systems and high assurance are close to mutually exclusive.

## Core Intuition

The lecture closes with one slide and one quotation. Gollmann: *"Security evaluation checks whether
a product delivers a promised security service. We have to state the function of the security
system the required degree of assurance (trust) in its security."* Two bullet properties follow, and
both are about cost.

First: a high level of assurance implies an inspection of a system at a very detailed level.
Assurance is not a certificate somebody stamps; it is evidence produced by detailed inspection, and
detailed inspection is expensive, slow, and effort-scaling in the size and complexity of the
artefact.

Second: complex systems and a high level of assurance tend to be mutually exclusive. This is the
consequence, and it is the real content of the slide. A large, tangled system cannot be inspected at
the level of detail a high assurance claim requires. So the choice is not "be complex and be secure"
— it is a forced trade between complexity and assurance.

Assurance is therefore the third element of the policy/mechanism/assurance triple and the expensive
one: policy is cheap to write, mechanism is what you build anyway, but *proving* the mechanism does
what the policy says is an additional, unbounded activity. And it belongs inside the security cost
the cost/benefit optimum accounts for — not as overhead on top of the mechanism-cost curve, but
inside it.

## Formal Definition / Statement

**The quotation, as given on the slide (D. Gollmann):**

> "Security evaluation checks whether a product delivers a promised security service. We have to state the function of the security system the required degree of assurance (trust) in its security"

Two obligations are packed into that sentence and both are required:

1. **The function must be stated.** "The function of the security system" — the security service the
   system is supposed to deliver is part of what evaluation checks. A promised service with no
   stated function cannot be evaluated, because there is nothing to compare behaviour against.
2. **The degree of assurance must be stated.** "The required degree of assurance (trust) in its
   security" — the output is not a yes/no verdict but a stated level of trust.

**The two properties, as given:** a high level of Assurance-Level implies an inspection of a system
at a very detailed level; and complex systems and a high levels of assurance tend to be mutually
exclusive.

**Placement in the triple.** The "Elements of Security" slide defines assurance as *correctness of
security — does it really work?* Security evaluation is the activity that answers that question. A
detailed inspection is a cost that mechanism deployment triggers but does not eliminate, so the
optimum is not computable from mechanism prices alone.

**What the slide does not contain.** No named assurance scale. The slide names no EAL, no TCSEC
level, no number of levels, and no procedure for producing the evaluation. Any scale the reader
brings to this page is imported from elsewhere — [[common-criteria]] is a useful cross-reference, but
the lecture names none, and this page does not attribute one to it.

## Key Properties

- **Evaluation is comparative against a promise.** The object of evaluation is not "the system" in the abstract but the delivery of a *promised* security service. No promise, no evaluation.
- **Two things must be stated, not one.** The function and the required degree of assurance. A verdict without a level of trust is an opinion, not a security evaluation.
- **Assurance is evidence, produced by inspection.** The more assurance claimed, the more detailed the inspection must be. The link is monotonic, and it is how assurance gets expensive.
- **Complexity and assurance compete for the same budget.** The second bullet is a consequence of the first: inspection effort scales with the thing inspected, so a complex system caps the attainable assurance level.
- **The trade-off is forced, not accidental.** The slide says the two "tend to be mutually exclusive" — a claim about the shape of the design space, not about resource scarcity. The trust claim is also relative: bound to a specific system, function and inspection depth, and invalidated by a firmware change.
- **Assurance is the expensive element, and it belongs in the optimum.** Policy and mechanism are design work; assurance is verification work, which does not improve the product, it only establishes trust in it. That is why it is the element most often skipped and most often asserted without evidence — and why raising the assurance level moves you right on the x-axis of the cost/benefit figure.

## Worked Example

A manufacturer of industrial control devices wants to claim, in a tender document, that its
controller "is secure". The evaluation slide forces two statements that a security engineer would
otherwise avoid.

**Step 1 — state the function.** "Secure" is not a function. Which security service is promised?
Pick one and write it precisely: *the controller authenticates the operator station and rejects
unauthenticated command sequences on its service interface*. That is testable: feed it unauthenticated
commands, observe the behaviour, compare with the promise. Note the "first job: identify threats and
security goals" from the lecture's opening slide — the promised function is the goal, and it is
relative to a threat.

**Step 2 — pick a candidate assurance level and price the inspection.** Suppose the manufacturer
wants to claim a *high* assurance level. By the slide's first property, that requires an inspection
"at a very detailed level": the authentication code path of the service interface, the key storage
and key lifecycle, the firmware update path (a second attack surface), the build and provisioning
chain, and the physical interface.

**Step 3 — apply the complexity property.** The controller is a real industrial product: a
safety-relevant controller with a real-time operating system, a bootloader, a field-bus stack, and
backward-compatible legacy interfaces. The inspection above is a large effort, and the slide's
second property bites: complex systems and a high assurance level tend to be mutually exclusive.

**Step 4 — the two honest options.**

- **Option A: reduce complexity, then claim high assurance.** Rationalise the product down to a
  single well-defined function on a single hardened interface, inspect that reduced scope, and state
  a high degree of assurance *for that function*. The claim is narrower and defensible. Cost: a
  smaller product, and the legacy interfaces — the attack surface a competitor would use — have to
  be dealt with somehow.
- **Option B: keep the complexity, state a lower assurance level, and reduce the exposure the
  missing assurance leaves open.** The tender carries a modest, explicitly stated degree of trust,
  plus compensating measures (access control on the service interface, physical protection of the
  cabinet, monitoring for unauthenticated commands) that reduce the residual risk. Cost: a weaker
  claim in a competitive tender, and a standing residual risk to accept and document.

**Step 5 — where the cost lands, and what must not appear in the tender.** Either option adds to
the mechanism-cost side of the cost/benefit curve, because inspection effort and compensating
measures are both real spend. The optimum is not "the cheapest system"; it is the level of security
whose marginal cost equals its marginal saving, and the assurance level determines how expensive the
right-hand side of that equation is. And "Our device is secure" as an unaccompanied claim must not
appear in the tender at all.


## Common Pitfalls

- **Claiming an assurance level the lecture never named.** The slide names no EAL, no TCSEC level, no scale. Writing "EAL4+" as if the lecture had introduced it is an import; it may be right later in the course, but it is not from this material.
- **Dropping the "state the function" half.** Evaluation without a stated function has nothing to compare behaviour against, and the quotation puts both halves in one sentence.
- **Treating assurance as a free add-on.** The inspection effort is the cost, and the cost grows with the assurance level requested. Asking for the highest level is asking for the most expensive inspection.
- **Ignoring the complexity/assurance exclusion.** Complex systems and high assurance "tend to be mutually exclusive" — a strong statement, and one an answer that only says "it is expensive" understates.
- **Confusing assurance with functionality testing.** Assurance is an inspection of the system's security properties against a stated promise at a stated trust level. A passing functional test is one piece of evidence, not the degree of trust.
- **Assuming the assurance claim transfers.** It is bound to a specific system, function and inspection depth; a firmware change invalidates it.
- **Skipping the assurance step entirely in a design review.** "The mechanism is implemented, so we are done" is the classic triple violation this lecture's final slide exists to prevent.

## Connections

- [[security-policy-mechanism-assurance]] — the third element of the triple, "does it really work?", priced here as the expensive one.
- [[security-cost-benefit-optimum]] — the figure that must absorb the inspection cost; the assurance level is a decision variable on that curve.
- [[common-criteria]] — the reader's route to a concrete assurance scale; the lecture names none.
- [[security-relationship-model]] — the promised security service is a protection requirement, and evaluation checks that the safeguards meet it.
- [[security-terminology-and-risk-model]] — the compact statement of the same material, and the reminder that residual risk is never zero.
- [[risk-assessment-frameworks]] — the formalised procedures that structure an evaluation, and the standards route the Safeguards slide points at.
- [[risk-perception-and-dread-risk]] — why the assurance level claimed in a tender is rarely the affordable one.
- [[security-by-design]] — the practice that makes the assurance claim cheap to obtain, by removing complexity before the evaluation starts.

## Open Questions

- The slide names no assurance scale: no EAL, no TCSEC level names, no ordinal levels, no procedure. Whether the course introduces a scale later, or expects it to stay abstract, is not stated in lecture 0. The link to [[common-criteria]] is a cross-reference for the reader, not a lecture claim.
- The quotation's grammar is compressed ("We have to state the function of the security system the required degree of assurance (trust) in its security"). Whether the two stated items are both outputs of the evaluation, or whether the first is an input and the second the output, is not clarified. Nor is the relationship between assurance level and the residual risk the course insists always remains: a high assurance level presumably bounds the residue, but no bound is given.
- "Tend to be mutually exclusive" is a qualitative claim. Whether the lecture intends a strict impossibility or a practical cost trade, and where the boundary lies for a given system size, is not stated. Whether evaluation is performed on the product, on the process that produced it, or on both is likewise not addressed.
