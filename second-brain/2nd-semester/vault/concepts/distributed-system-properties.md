---
title: "Distributed System Properties"
tags: [concept, dependable-distributed-systems, semester-2, distributed-systems]
course: "Dependable Distributed Systems"
source_count: 4
status: current
last_updated: 2026-10-21
prerequisites: []
---

## One-line Summary
A distributed system is several independent computers joined by a network that run shared protocols so that, to the people using them, the whole thing behaves like one single machine.

## Core Intuition

The lecture draws a line before it draws any properties: a computer network is not a distributed system. The network is only the road; a distributed system is the traffic on that road plus the rules of the road — processes that agree on how to behave together so that a joint activity comes out coherent. That is why the network's own feature list (multiple media, multiple topologies, common communication protocols) says nothing on its own about distribution. Cables and routers do not make a distributed system; a *distributed protocol* coordinating state across machines without shared memory does.

The two canonical definitions pull the same thread from opposite ends. Tanenbaum's is about appearance: users should not care that many computers are underneath. Garg's is about what is structurally missing: no common clock, no shared memory, no exact failure detection. Together they say distribution removes the two oracles a designer leans on — one clock, one memory — and replaces them with partial, bounded substitutes. Every property that follows, from independent failures to the difficulty of determining global state, is a consequence of those three missing oracles. This is also why the course is about *dependability*: the weaknesses listed here are exactly the ones a fault-tolerant design must compensate for.

## Formal Definition / Statement

**Computer network (per lecture):** infrastructure that enables communication between machines; may have multiple media and topologies; has common communication protocols.

**Distributed system (per lecture):** composed of multiple computer systems; they communicate over a computer network; and they form a set of processes that use a common set of distributed protocols to support a coherent execution of distributed activities.

**Tanenbaum:** "A distributed system is a collection of independent computers that appear to the users of the system as a single computer."

**Garg:** three structural properties.

| Garg property | Consequence stated on the slide |
|---|---|
| No common clock | Distributed local clocks can be synchronized with only limited accuracy |
| No shared memory | Common state is not stored centrally; observing global system properties is difficult |
| No exact failure detection | No upper bounds on communication delays; a failure is not distinguishable from a slow node |

**The properties ladder**, built up item by item, structure first and consequences after: several computers → connected by a communication network → distributed global state → independent failures → unreliable communication → variable delays → moderate communication speed → only partial ordering of events → global state difficult to determine → higher administrative costs → often less expensive than centralized supercomputers.

**Centralized vs distributed.**

| Aspect | Centralized | Distributed |
|---|---|---|
| Resources and information | Easy accessibility | Scalability by size, modularity |
| Methods and technologies | Homogeneity | — |
| Operation | Manageability | — |
| Consistency | A global state | — |
| Reliability / availability | — | Redundancy and replication, graceful degradation |
| Cost | — | Cheaper |
| Security | Easier to protect | Able to compensate for the impact of security problems, but not really easy |

**Modelling contrast (lecture 2).** A model is a simplification of a system that lets one reason about it: attributes plus the rules governing how they interact. It is *accurate* insofar as analysing it yields truths about the object of interest, and *tractable* if such analysis is actually possible. The slide's example: two processes A and B exchange messages on a bidirectional channel, neither fails, but the channel may suffer transient failures losing a subset of sent messages. Modelling targets feasibility (which problems can be solved at all) and cost (how expensive solutions must be).

## Key Properties

- **Coherence over reach.** Membership requires a shared protocol, not mere connectivity.
- **Independence of components.** Failures are local and independent; no single death ends the system.
- **No global view.** Global state is not stored centrally and is hard to determine.
- **Imperfect time.** Local clocks synchronize only with limited accuracy, so only a partial ordering of events is observable.
- **Imperfect communication.** Links are unreliable, delays vary, bandwidth is moderate.
- **Approximate failure detection.** Without upper bounds on delay, a crashed node cannot be distinguished from a slow one.
- **The trade is real.** Distribution buys scalability, modularity, redundancy, graceful degradation, and lower cost; it pays in administrative overhead and harder-to-protect security.

## Worked Example

The lecture's examples are a car (Der neue Maybach), the Sun Modular Datacenter, BitTorrent, Sandvine (North America, Fixed Access), Intel, and a gateway/IoT cloud of sensors, actors, edge, core, and IoT services. The last is the most fully described, so it carries the walkthrough.

Step 1 — the architecture. Sensors and actors at the bottom, an edge layer above them, a core above that, IoT services at the top. Each tier is a set of separate computers, and the tiers are connected by a network.

Step 2 — where is the distributed system? The network between tiers is only infrastructure. The system becomes a distributed system where the tiers run a common set of protocols letting a sensor reading and an actuator command be coordinated into one coherent operation.

Step 3 — apply Garg. No common clock, because each tier has local clocks that synchronize only with limited accuracy. No shared memory, because common state is not stored centrally across tiers. No exact failure detection, because no upper bound on communication delay means an unresponsive edge node is indistinguishable from a slow one.

Step 4 — apply the ladder: independent failures (an edge node dies), unreliable communication (tier-to-tier messages lost), variable delays, partial ordering of events, global state difficult to determine, higher administrative costs — and yet often cheaper than a centralised supercomputer. A centralised version would offer easy accessibility, homogeneity, manageability, a global state, and easier-to-protect security, but not the redundancy and graceful degradation that let the distributed version keep serving when one edge node fails.

## Common Pitfalls

- **Calling any networked system a distributed system.** The lecture has a dedicated slide; the defining element is the shared distributed protocol, not the network.
- **Reading the ladder as a flat list.** It is a build-up: later items are consequences of earlier structural ones.
- **Forgetting "distributed global state."** Students jump from "several computers" to "independent failures" and never establish that state is distributed — which is what makes Garg's no-shared-memory point bite.
- **Treating "no exact failure detection" as a networking nuisance.** It follows definitionally from the absence of an upper bound on delay, and recurs in [[failure-models]] and [[synchronous-vs-asynchronous-models]].
- **Reading the comparison table as a scorecard.** Distributed security is "able to compensate for the impact of security problems" but explicitly "not really easy"; and "higher administrative costs" is a slide item, so quoting only the cheapness is a half-credit trap.

## Connections

- [[failure-models]] — the consequences of independent failures and unreliable communication, made into a formal taxonomy.
- [[communication-link-models]] — the "unreliable communication" property formalised as fair-loss, stubborn, perfect, and authenticated perfect links.
- [[synchronous-vs-asynchronous-models]] — the "variable delays" and "partial ordering" properties turned into a modelling choice.
- [[model-accuracy-tractability]] — the accuracy/tractability trade-off the lecture uses to justify models at all.
- [[resilience-vs-dependability]] — why a course on distribution's properties then turns to dependability.

## Open Questions

- The centralized-vs-distributed table does not say under which workload, or at which scale, the distributed column actually wins.
- The property list is a build-up with no claim that every distributed system exhibits all eleven items equally — universal or typical is not stated.
- The IoT cloud slide names the tiers but not the protocols coordinating them, so the source does not identify what makes that architecture a distributed system rather than a network.
- The source does not say how "global state difficult to determine" interacts with the replication needed for consistency — the consistency cell for distributed systems is left blank.
