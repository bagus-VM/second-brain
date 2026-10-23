---
title: "Synchronous vs Asynchronous Models"
tags: [concept, dependable-distributed-systems, semester-2, network-models]
course: "Dependable Distributed Systems"
source_count: 3
status: current
last_updated: 2026-10-21
prerequisites: ["[[distributed-system-properties]]", "[[communication-link-models]]"]
---

## One-line Summary
An asynchronous system makes no promises about how fast anything happens, while a synchronous system promises bounded speeds and bounded delays, and that promise is what buys cheaper and simpler protocols.

## Core Intuition

The distinction looks like a technicality and is actually a trade in a different currency. Time is the one resource a distributed system does not have in common: there is no shared clock, only local ones that can be synchronized with limited accuracy, and no upper bound on communication delay, so a failure cannot be distinguished from a slow node. Given that, a designer has to pick a stance on time, and the two stances here are deliberately asymmetric.

Calling a system asynchronous is a *non-assumption*. It constrains nothing; it simply declines to constrain anything. Every real system satisfies the asynchronous assumptions, because a bound on delay that nobody enforces is not a bound. So a protocol correct under an asynchronous model is correct everywhere — the portable choice, safe on every platform, including ones whose timing nobody has characterised.

Calling a system synchronous is the opposite: a real constraint with teeth. It constrains how the implementation must work. The scheduler that multiplexes processors must not break the process-speed bound; queuing delays, unpredictable routings, and retransmissions caused by errors must not break the channel-delay bound. And the lecture notes that this implies every processor has access to approximately rate-synchronized real-time clocks. To claim synchrony you must have paid for the hardware and the implementation discipline that make the claim true. Having paid, you may rule out certain system behaviours — which is what lets you use protocols simpler in complexity and cheaper in overhead than the asynchronous ones would require. The choice is not "which is true" but "what am I willing to assume and pay for": asynchrony is the pessimistic default, synchrony a paid upgrade that buys efficiency.

## Formal Definition / Statement

**Asynchronous system:** we make no assumptions about process execution speeds and/or message delivery delays.

**Synchronous system:** we do make assumptions about these parameters. The relative speeds of processes are assumed to be bounded, and the delays associated with communications channels also are.

**Asynchrony is a non-assumption.** Every system "is" asynchronous, i.e. satisfies the assumptions that are made. An algorithm for an asynchronous system can be used on every system.

**Synchrony constrains the implementation:**

- The scheduler that multiplexes processors must not violate the constraints on process execution speeds.
- Queuing delays, unpredictable routings, and retransmission due to errors must not violate the constraints on channel delays.
- This implies that all processors in the system have access to approximately rate-synchronized real-time clocks.

**Benefit of asserting synchrony.** In asserting that a system is synchronous, certain system behaviours are ruled out. This enables simpler protocols (in complexity) and cheaper protocols (in overhead) than required in an asynchronous system.

**Other models in the spectrum:** partial synchrony, timed-asynchronous, wormholes. The lecture defers the details to later lectures.

**Context.** The lecture frames distributed systems as models about processes: multiple processes communicating over narrow-bandwidth, high-latency channels, with some processes and channels faulty.

**Wrap-up of the models part.** What to remember: how to model processes and process failures, how to model communication in a distributed system, and how to model time in a distributed system.

## Key Properties

- **Asynchrony is the safe default.** An asynchronous algorithm runs correctly on any system, including ones with far stronger timing properties.
- **Synchrony is a commitment, not a description.** It constrains the scheduler, the queues, the routing, and the clock hardware.
- **Bounds on process speed and on channel delay are separate assumptions**, and the lecture states both.
- **Rate-synchronized real-time clocks are a consequence** of taking synchrony seriously, not a separate requirement.
- **Timing rules out behaviour**, and excluded behaviour is what makes protocols smaller and cheaper.
- **The spectrum is not binary.** Partial synchrony, timed-asynchronous, and wormholes sit between the two poles.
- **Time is the third leg of the modelling agenda**, alongside processes (and their failures) and communication.

## Worked Example

Consider a leader election protocol among five nodes that must decide a leader or declare failure.

Step 1 — what the asynchronous model gives. No bounds on process speeds or message delays, so a node that has not answered cannot be declared dead; it may simply be slow. A time-based election therefore relies on a heuristic timeout, and a timeout firing too early declares a healthy node dead. The protocol must use heartbeats, repeated rounds, and mechanisms such as terms or epochs to resolve the case where a slow node returns after being declared dead — a protocol with a lot of machinery in it.

Step 2 — what the synchronous model changes. Process speeds and channel delays are bounded, so a node that has not answered within the bound can be declared dead with confidence. The election needs one round of messages plus a timeout of the known bound, and no ambiguity handling. Complexity and overhead both drop.

Step 3 — check whether the claim is affordable. To assert synchrony, the implementation must ensure the scheduler does not starve a process beyond the process-speed bound, and that queueing, routing, and error-induced retransmission stay inside the channel-delay bound. Doing this properly implies real-time clocks that are approximately rate-synchronized across the processors. If the deployment cannot pay for that, the synchronous proof is unavailable and the asynchronous protocol is the correct choice.

Step 4 — note the portability direction. The asynchronous protocol is correct on the synchronous system as well; the synchronous protocol is not correct on a system violating its bounds. The asynchronous design is a superset of correctness, at the price of extra machinery; the synchronous design is a subset of applicability, at the price of implementation constraints.

Step 5 — locate the middle ground. Partial synchrony, timed-asynchronous, and wormholes are the models for systems that are mostly asynchronous but have occasional bound violations or differently-shaped time. The lecture defers them, but their existence is the reason one does not treat the choice as binary. And the synchrony decision determines whether a crashed process can be distinguished from a slow one — the fail-stop versus fail-silent distinction in [[failure-models]].

## Common Pitfalls

- **Thinking asynchronous is a pessimistic claim about a particular system.** It is a non-assumption, satisfied by every system.
- **Assuming the asynchronous protocol is "worse" and should be avoided.** It is the one usable on every system; the synchronous one only on systems that honour their bounds.
- **Ignoring that synchrony constrains the implementation.** The scheduler, queues, routing, and retransmission behaviour must all respect the bounds, and approximately rate-synchronized real-time clocks are implied.
- **Conflating bounded process speed with bounded channel delay.** The lecture lists them as two distinct assumptions.
- **Believing synchrony lets you ignore failures.** Synchrony rules out *behavioural* patterns, not the possibility of faulty processes and channels; the fault models are orthogonal to the time model.
- **Forgetting the spectrum.** Partial synchrony, timed-asynchronous, and wormholes exist and are only deferred, not absent.
- **Missing the wrap-up structure.** Processes and process failures, communication, and time are the three things to remember; time is the third.

## Connections

- [[distributed-system-properties]] — variable delays, partial ordering of events, and the absence of a common clock motivate the discussion.
- [[failure-models]] — synchrony decides whether crash and slow are distinguishable (fail-stop vs. fail-silent).
- [[communication-link-models]] — link guarantees and time bounds interact: a timeout is only meaningful under a delay bound.
- [[lamport-logical-clocks]] and [[vector-clocks]] — the tools for ordering events when real time is unavailable.
- [[clock-synchronization-problem]] — the hard part of making a synchronous claim true in practice.
- [[model-accuracy-tractability]] — why one accepts the synchrony cost for a tractable protocol.

## Open Questions

- The slides give no numeric bounds implied by synchrony, nor say who is responsible for establishing them in a real deployment.
- The lecture says synchrony implies access to approximately rate-synchronized real-time clocks but does not say how accurate "approximately" may be, or how clock drift is handled.
- Partial synchrony, timed-asynchronous, and wormholes are named but their definitions are explicitly deferred, so the source does not say where each sits relative to the two poles.
- The slides do not say whether a synchrony assumption may be taken for channels while assuming asynchrony for processes, or whether the two must be chosen together; the statement is given in terms of one system.
- No cost comparison is given for the simpler/cheaper protocols enabled by synchrony, only the qualitative claim.
