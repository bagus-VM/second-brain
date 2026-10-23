---
title: "Ways Towards Dependability"
tags: [concept, dependable-distributed-systems, semester-2, fault-tolerance]
course: "Dependable Distributed Systems"
source_count: 3
status: current
last_updated: 2026-10-21
prerequisites: ["[[dependability-attributes]]"]
---

## One-line Summary
There are exactly four ways to make a system more dependable: stop faults from happening, keep working despite them, take faults away once they are there, and predict how many will come.

## Core Intuition

The framing comes from the fault-error-failure chain ([[fault-error-failure-chain]]). If faults are the cause and failures are the outcome, then a dependability strategy is simply a decision about *where in that chain to intervene*. Each of the four strategies picks a different position:

- Prevention intervenes **before** the fault occurs.
- Removal intervenes **after** a fault has existed, reducing how many or how severe the remaining ones are.
- Forecasting does not intervene at all: it estimates the future so that planning and investment can be justified.
- Tolerance intervenes **after** the fault has occurred but **before** the failure becomes visible, by keeping the service correct anyway.

The four questions are stated in the slides as questions, and that phrasing is deliberate: "how to prevent the occurrence of faults?", "how to deliver correct service in the presence of faults?", "how to reduce the number/severity of faults?", "how to estimate the future incidence of faults?" An exam answer that names a strategy without matching it to its question loses the point.

Prevention and removal both reduce the fault population; the difference is timing and locus. Removal is a feedback loop: faults are found (during design, or during operations) and eliminated, so the population shrinks over time. Prevention is a barrier: faults are stopped at the door. Fault tolerance is qualitatively different because it does not reduce the number of faults at all — it makes them irrelevant to the delivered service, which is why it is the main topic of the lecture.

## Formal Definition / Statement

The lecture lists exactly four ways towards dependability.

| Strategy | The question it answers | Means (as given in the slides) |
|---|---|---|
| **Fault prevention** | How to prevent the occurrence of faults? | Avoid design defects (good process; tools; etc.); shielding, robust design, good operational procedures etc. for runtime faults |
| **Fault tolerance** | How to deliver correct service in the presence of faults? | The main topic of the lecture |
| **Fault removal** | How to reduce the number/severity of faults? | Verification & validation (design phase); corrective & preventive maintenance (operations) |
| **Fault forecasting** | How to estimate the future incidence of faults? | Simulation, modeling, prediction (data from models); historical data, accelerated life testing, etc. (data from real systems) |

Two structural observations follow directly from the table.

**Prevention and removal are both anti-fault, but they differ in phase.** Prevention is largely a *design-time* activity aimed at the root causes: process discipline, tooling, and — for runtime faults — shielding, robust design, and sound operational procedures. Removal is split by phase too, but the split is *within* removal: verification and validation during design, corrective and preventive maintenance during operations. Corrective maintenance removes faults that have already caused failures; preventive maintenance removes faults that have not yet caused any.

**Forecasting is the only one that produces knowledge rather than robustness.** The slides distinguish its two data sources explicitly: data from models (simulation, modeling, prediction) versus data from real systems (historical data, accelerated life testing). This distinction is the practically important one, because model-based estimates inherit the model inaccuracies the course warns about (see [[model-accuracy-tractability]]), whereas historical and life-test data are grounded in reality but expensive and slow to obtain.

The overall taxonomy is visualised in the lecture by two classification trees — the "Dependability Tree" (source: DSSA) and the "Fault Tolerance Tree" (source: Avizienis et al., *Basic concepts and taxonomy of dependable and secure computing*, TDSC v1(1), March 2004) — whose layout is presented as an image rather than as text. The trees exist to organise these terms, but the text layer of the slides does not expose their internal branching.

## Key Properties

- **Exactly four.** The enumeration is closed; anything else in an answer is a category error.
- **Each strategy is bound to a question.** Prevention → avoid; tolerance → continue; removal → reduce; forecasting → estimate.
- **Fault tolerance is the only strategy that does not reduce faults.** It changes the consequence, not the cause.
- **Prevention acts on design defects and runtime faults with different tools** — process and tooling for the former, shielding and operational procedures for the latter.
- **Removal has a design-phase and an operations-phase arm.**
- **Forecasting draws on two different epistemic sources**: models versus real-system data.
- **Strategies are complements, not substitutes.** The lecture's J. Gray (1985) framing — better to prevent errors than to repair them later, in a predictable and repeatable manner — argues for prevention, but the main topic remains tolerance, since prevention can never reach zero.
- **Everything that works will fail at some time**, so no amount of prevention eliminates the need for the other three.

## Worked Example

Consider a distributed database replicated across a datacenter (as the lecture's other slides illustrate with a server farm that can have a defective server shut down, see [[error-detection-and-recovery]]). Apply each strategy in turn.

1. **Fault prevention.** At design time, the team avoids design defects through good process and tools: a reviewed schema, a disciplined migration procedure, capacity planning so that no node is deliberately overloaded. For runtime faults, shielding (isolating the storage engine from noisy neighbours), robust design, and good operational procedures such as staged rollouts are applied so that a bad release does not become a fault in production.

2. **Fault removal.** During the design phase, verification and validation try to find faults before release: property-based tests over the commit protocol, checking that the all-or-nothing semantics hold under crash injection. During operations, corrective maintenance fixes what slipped through, and preventive maintenance replaces components whose wear is heading towards a fault. Over time the fault population shrinks.

3. **Fault forecasting.** Two sources are combined. From models: a simulation of the replication protocol under message loss and delay, to estimate how many incidents a given redundancy level produces per year. From real systems: historical incident data and accelerated life testing of disks, to estimate the hardware fault rate that the simulation then uses as input. The output is a number of expected incidents per year, which is what makes a redundancy investment comparable to other spending.

4. **Fault tolerance.** None of the three above changes the fact that a node will eventually die, so the system must keep serving. Error detection, then recovery, then redundancy are what make the failure invisible to the user. The lecture makes clear that fault tolerance is the main topic precisely because the other three cannot reduce the fault count to zero.

The four strategies stack: prevention lowers the incoming fault rate, removal lowers the residual population, forecasting sizes the remaining risk, and tolerance absorbs whatever is left.

## Common Pitfalls

- **Missing one of the four** or adding a fifth. The taxonomy is fixed and complete.
- **Mixing prevention and removal.** Prevention stops faults from occurring (shielding, robust design, good process); removal takes faults out of the system once they are in it (V&V, corrective and preventive maintenance). "Avoid design defects" belongs to prevention, not removal.
- **Attaching the wrong data source to forecasting.** Simulation and modeling come from models; historical data and accelerated life testing come from real systems. The slide labels them explicitly.
- **Treating fault tolerance as a way of reducing faults.** It does not; the fault still happens, the service just stays correct.
- **Forgetting that the lecture names fault tolerance as the main topic**, which is a strong hint about exam weighting of the following slides.
- **Inventing structure for the Dependability Tree and Fault Tolerance Tree.** Their layout is an image; the text layer gives only the title and the source citation.
- **Assuming prevention alone suffices.** J. Gray's point is that everything that works will fail at some time, so tolerance remains necessary.

## Connections

- [[fault-error-failure-chain]] — the chain that these four strategies position themselves against.
- [[dependability-attributes]] — prevention, removal and forecasting move the metrics; tolerance holds the service up while failures happen.
- [[error-detection-and-recovery]] — the machinery that implements fault tolerance.
- [[redundancy-forms]] — the structural redundancy that tolerance and masking rely on.
- [[fault-tree]] — the classical structured way to reason about how faults combine into failures, complementary to forecasting.
- [[dependable-distributed-systems-lecture-1]] — the lecture in which this taxonomy appears.

## Open Questions

- The slides do not say how the four strategies are prioritised or traded off against each other for a given system, nor whether there is an ordering beyond the lecture's own emphasis on fault tolerance.
- No quantitative guidance is given on how accurate model-based forecasting is expected to be, and the slide's remark that error models become inaccurate under malicious faults is left as an assertion.
- The slides do not specify how "severity" should be measured in the fault removal question, so the criteria for deciding that one fault is worse than another are unstated.
- Whether the four strategies apply unchanged to a distributed system, given the added exposure to communication failures and correlated component failures, is not discussed.
- The internal branching of the Dependability Tree and the Fault Tolerance Tree is not given in the text layer, so the slides do not settle how the four strategies relate to that tree structure.
