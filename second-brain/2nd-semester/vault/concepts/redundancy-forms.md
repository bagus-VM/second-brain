---
title: "Forms of Redundancy"
tags: [concept, dependable-distributed-systems, semester-2, redundancy]
course: "Dependable Distributed Systems"
source_count: 2
status: current
last_updated: 2026-10-21
prerequisites: ["[[error-detection-and-recovery]]"]
---

## One-line Summary
Redundancy comes in exactly three flavours — extra copies, extra tries, and extra information — and every dependable technique in the course is built out of one of them.

## Core Intuition

Redundancy is the raw material of fault tolerance. The lecture's error-masking slide says it plainly: if the system state has enough redundancy, correct service can be provided without any noticeable glitch. So the question is not *whether* to add redundancy but *what kind*, and the answer depends on what is scarce: space, time, or bits of information.

- If **space** is the constraint, add copies: another disk, another node, another path for the message.
- If **time** is the constraint, add attempts: send it again, compute it again.
- If **information** is the constraint, add bits: a parity bit, a checksum, a signature.

The three are not alternatives but a small orthogonal kit. A RAID array is space redundancy. A retransmission is time redundancy. An ECC word is value redundancy. Most real mechanisms combine them — majority voting, for instance, is space redundancy (several copies) whose verdicts are compared to detect value-level disagreements, and it is also a re-computation, hence partly time redundancy.

The cost of redundancy is not free and differs per form. Space redundancy costs hardware and coordination; time redundancy costs latency (the user waits for the second attempt); value redundancy costs bandwidth and a small arithmetic overhead on every message, and it buys the least: it can detect or correct errors in the data, but it says nothing about the logic that produced the data.

The lecture's two taxonomy trees — the "Dependability Tree" (source: DSSA) and the "Fault Tolerance Tree" (source: Avizienis et al., *Basic concepts and taxonomy of dependable and secure computing*, TDSC v1(1), March 2004) — organise the dependability vocabulary, but their layout is presented as an image; the text layer exposes only the titles and the citation.

## Formal Definition / Statement

The slide gives **exactly three** forms of redundancy.

| Form | Definition as given | Examples listed on the slide |
|---|---|---|
| **Space redundancy** | Several copies of the same component | Same information stored in several disks; different nodes compute the same result in parallel; messages disseminated along different paths |
| **Time redundancy** | Doing the same thing more than once, in the same or different ways | Retransmission of lost messages; repeating computations that have aborted |
| **Value redundancy** | Adding extra information about the data being stored or sent | Codes that allow the detection or correction of integrity errors; parity bit or ECC added to memory chips or disk structures; frame check sequences or cyclic redundancy in transmitted data; cryptographic message signatures |

Reading the table carefully, each example maps onto the definition of its row:

- Space redundancy duplicates a *component* — and "component" is deliberately broad. A disk is a component, a computing node is a component, and a communication path is a component. Disseminating a message along different paths is therefore space redundancy applied to the network, not a separate category.
- Time redundancy duplicates an *attempt*. Retransmission and recomputation differ in what is repeated, not in the principle: the same operation is performed again, either identically or in a different way.
- Value redundancy adds *redundant information about data*, never additional data items. Codes detect or correct integrity errors; a parity bit or ECC is attached to memory chips or disk structures; frame check sequences and cyclic redundancy protect transmitted data; cryptographic message signatures protect data against alteration. The value-redundancy family thus spans both accidental corruption (parity, ECC, CRC) and adversarial alteration (signatures) — which connects it to the security side of the course (see [[cia-triad]] and [[security-relationship-model]]).

## Key Properties

- **Exactly three forms**, and the classification is by *what is duplicated*, not by *what is protected*.
- **Space redundancy protects against the loss of a component**, including the loss of a communication path.
- **Time redundancy protects against transient loss** of a message or an aborted computation.
- **Value redundancy protects the content**, detecting or correcting errors in stored or transmitted data.
- **The three compose.** Majority voting uses space redundancy to produce several results and a comparison to detect a wrong one; a multi-path broadcast uses space redundancy for the paths and value redundancy for per-message checksums.
- **Value redundancy is the cheapest and the weakest.** It adds a small overhead but cannot fix a wrong computation, only a corrupted representation of a computation.
- **Redundancy enables error masking**, which the lecture presents as the desirable property: the user is blissfully unaware, and fault/failure transparency results.
- **Redundancy has limits that the lecture states:** error masking rests on the *independent-failure assumption* and does not deal adequately with *design faults*. A replicated component with the same bug in every copy is not protected.
- **Redundancy is a cost**, and the taxonomy does not prescribe how much to buy; that decision belongs to the fault-forecasting side (see [[ways-towards-dependability]]).

## Worked Example

A distributed key-value store must survive a node failure and the loss of a message. Build it out of the three forms.

**Space redundancy.** The dataset is stored on three disks rather than one, so a single disk failure does not remove the data. Equivalently, three nodes compute the same result in parallel and the store keeps the value agreed by the majority. For the network, the same request is disseminated along different paths, so the loss of one route does not lose the request. Note that all four space-redundancy examples from the slide — several disks, parallel nodes, parallel paths — are the same principle applied at different levels of the system.

**Time redundancy.** The client retransmits a request whose acknowledgement never arrived, because the message may have been lost rather than the server having died. A computation that has aborted is repeated. The repetition may be identical or in a different way: the retry can re-execute the same function, or take a different code path that avoids whatever tripped it.

**Value redundancy.** Each stored block carries a parity bit or ECC, so a corrupted sector is detected and, depending on the code, corrected. Each transmitted message carries a frame check sequence or a cyclic redundancy code, so a corrupted frame is detected on arrival. Cryptographic message signatures extend this to the case where the threat is an attacker rather than noise, and are the point where value redundancy reaches into the security dimension.

**Where the masking comes from.** With three copies in agreement, a single-node failure and a single lost message are absorbed: the user never notices, which is exactly the error-masking property described in [[error-detection-and-recovery]]. The slides state the caveats plainly. The arrangement depends on the independent-failure assumption — the three copies must not fail for the same reason at the same time. And it does not deal adequately with design faults: if all three nodes run the same buggy code, three-space redundancy produces three identical wrong answers, and the majority vote confirms the bug. This is where value redundancy at the level of the *logic* rather than the data would be needed, and the slide's majority-voting example of "compute multiple times and compare" is the standard hook for that idea.

**Where it fails.** Under an attacker who can reach every copy simultaneously, both the independence assumption and the value checks are defeated or neutralised — which is the same point the lecture makes about malicious faults breaking the error models.

## Common Pitfalls

- **Listing a fourth form.** The slide says space, time, value — three.
- **Misclassifying retransmission as space redundancy.** It is time redundancy: the same operation is attempted again. Space redundancy duplicates a *component*, not an attempt.
- **Treating a checksum as a separate category.** Frame check sequences and cyclic redundancy are examples of value redundancy, not a fourth form.
- **Confusing "different nodes compute the same result" with time redundancy.** The duplication there is of components, so it is space redundancy; only repeating the *same* attempt is temporal.
- **Assuming redundancy eliminates the need for detection.** Error masking is one recovery route among backward, forward, and fault handling; detection is still the entry point to the others.
- **Overclaiming the coverage of redundancy.** The slide explicitly flags the independent-failure assumption and the inability of masking to handle design faults.
- **Forgetting the security variant.** Cryptographic message signatures belong to value redundancy, and their presence in this list is the link to integrity and the [[cia-triad]].
- **Inventing branches for the taxonomy trees.** The Dependability Tree and the Fault Tolerance Tree are shown as images; only the titles and the Avizienis citation are recoverable from the text layer.

## Connections

- [[error-detection-and-recovery]] — redundancy supplies the state that makes error masking possible.
- [[ways-towards-dependability]] — redundancy is the concrete embodiment of fault tolerance, the lecture's main topic.
- [[fault-error-failure-chain]] — redundancy breaks the error-to-failure link by ensuring a correct copy exists.
- [[dependability-attributes]] — space redundancy is the standard lever on availability and MTTR.
- [[fault-tree]] — a structured way of reasoning about how redundant components still combine into failures.
- [[dependable-distributed-systems-lecture-1]] — the lecture in which the forms and the two taxonomy trees appear.

## Open Questions

- The slides do not say how the three forms should be selected or combined for a given reliability or availability target, nor how the cost of each form compares.
- How many copies constitute a sufficient majority is not specified, and no rule is given for choosing the voting threshold.
- The slides do not address redundancy in the time dimension of wall-clock: they treat time redundancy as repeated *attempts*, not as delayed or deferred execution.
- The relationship between the three forms and the structure of the "Fault Tolerance Tree" (Avizienis et al., TDSC 2004) is not recoverable from the slides, since the tree is presented only as an image.
- Whether value redundancy can be used to protect a computation rather than only its data representation is left implicit by the "compute multiple times and compare" example and not developed.
- The slides do not say how redundancy interacts with consistency guarantees in a replicated store, and the trade-off between availability and consistency is not addressed in this material.
