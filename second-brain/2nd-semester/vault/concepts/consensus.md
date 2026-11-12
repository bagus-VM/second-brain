---
title: "Consensus"
tags: [concept, dependable-distributed-systems, semester-2, distributed-algorithms]
course: "Dependable Distributed Systems"
source_count: 1
status: current
last_updated: 2026-11-10
prerequisites: ["[[atomic-broadcast]]", "[[synchronous-vs-asynchronous-models]]"]
---

## One-line Summary
Consensus lets processes propose values and requires every correct process to decide the same valid value exactly once.

## Core Intuition
A distributed group needs a shared choice even though each member starts with its own proposal and messages arrive at different times. Consensus separates four promises: someone correct eventually decides, correct processes agree, the decision came from a proposal, and nobody decides twice. Atomic broadcast can solve consensus by having every process broadcast its proposal and deciding the first delivered value; conversely, repeated consensus instances can order reliably broadcast messages.

## Formal Definition / Statement
Each process may issue `Propose(v)` and eventually issue `Decide(v)`. The lecture's regular consensus properties are:

- **Termination:** every correct process eventually decides some value.
- **Agreement:** no two correct processes decide different values.
- **Validity:** if a correct process decides `v`, some process previously proposed `v`.
- **Integrity:** no process decides twice.

The lecture also lists variants: uniform agreement extends agreement to decisions by faulty processes; uniform integrity extends validity to faulty deciders; and two stronger validity formulations constrain the decision when all processes, or all correct processes, propose the same value.

## Key Properties
- Termination is liveness; agreement, validity, and integrity constrain which executions are allowed.
- Validity is not necessarily “decide my own proposal” or “decide the majority”; it is a source-of-value condition.
- Regular agreement quantifies over correct processes only. Uniform agreement also accounts for a process that decides and later becomes faulty.
- Atomic broadcast to consensus uses total order to make every process observe the same first delivered proposal.
- Reliable broadcast plus a sequence of multi-value consensus instances can implement atomic broadcast: reliably disseminate candidates, decide a set for each round, then deliver that set in a deterministic order.
- A reduction between abstractions transfers the difficulty; it does not prove that either primitive is implementable under every failure model.

## Worked Example
In a failure-free asynchronous system with three processes, a simple coordinator protocol solves consensus. Each process sends its proposal to coordinator `P1`. `P1` waits for all three, chooses the proposal from the smallest process ID, and broadcasts that value as the decision. Every process decides that value.

This protocol has two communication steps and, with broadcasts implemented as three unicasts, `3 + 3 = 6` messages. Termination follows because all processes are correct and links eventually deliver; agreement follows because there is one coordinator decision; validity follows because it selects an actual proposal; integrity follows because each process decides once. These claims rely on the stated no-fault assumption.

## Common Pitfalls
- Agreement alone does not ensure a decision ever occurs; that is Termination.
- Validity does not require selecting a majority value unless the chosen consensus variant says so.
- “All correct processes agree” is weaker than uniform agreement if a faulty process may decide first.
- A coordinator protocol that waits for all proposals is not fault tolerant: one crash can block it.
- Atomic broadcast and consensus are equivalent only under suitable definitions and transformations; do not confuse one protocol's assumptions with the abstraction's definition.

## Connections
- [[atomic-broadcast]] — the lecture gives both directions of the relationship between atomic broadcast and consensus.
- [[byzantine-reliable-broadcast]] — reliable dissemination is one input primitive for constructing atomic broadcast.
- [[broadcast-order-semantics]] — total order is the property that makes the first-delivery reduction work.
- [[synchronous-vs-asynchronous-models]] — timing and failure assumptions govern implementability.
- [[dependable-distributed-systems-lecture-5]] — definitions and pseudocode transformations.
- [[dependable-distributed-systems-exercise-5]] — a coordinator construction in the failure-free model and proof exercises.

## Open Questions
- The slides note that other consensus definitions differ slightly but do not select one as the course-wide standard.
- The lecture states the asynchronous atomic-broadcast impossibility result but does not prove it here; its relation to consensus is introduced at a high level.