---
title: "Communication Link Models"
tags: [concept, dependable-distributed-systems, semester-2, network-models]
course: "Dependable Distributed Systems"
source_count: 2
status: current
last_updated: 2026-10-21
prerequisites: ["[[distributed-system-properties]]"]
---

## One-line Summary
A communication link model states what a channel between two processes is allowed to do to messages — lose them, duplicate them, invent them, or do none of that.

## Core Intuition

Every guarantee a distributed protocol offers to its clients is ultimately a promise about messages, so before promising anything one has to say what a message is allowed to suffer. That is what a link model does: it fixes the weakest behaviour the channel may exhibit, and the protocol then has to survive exactly that.

The interesting move in the lecture is that the weak models are not useless. Fair-loss links allow messages to be lost, and yet the model is still "weak but useful" because it is precise about *how much* loss there may be: a fair-loss link may drop a message, but it may not drop one forever if the sender keeps retransmitting periodically. That is the right level of abstraction for a real network — lossy, but not a black hole, and never inventive.

The ladder runs from weak to strong: fair-loss, stubborn, perfect (equivalently reliable), and authenticated perfect. Each rung removes one pathology — fair-loss permits loss, stubborn removes loss but keeps the retransmission machinery, perfect removes duplication and spurious messages as well, and authenticated perfect adds correct sender identification. Choosing a rung is choosing how much defensive machinery the protocol must carry. The channel is modelled as a real object rather than a black box, because the point-to-point model introduces explicit queues and an explicit runtime step; that structure is what makes the link models expressible in the first place.

## Formal Definition / Statement

**Point-to-point communication.** Between processes p and q:

1. Process p sends a message m to q by executing `send(m)`, which adds m to p's send queue.
2. The channel transports m from p's send queue to q's receive queue.
3. q's runtime system calls `deliver(m)`, which delivers m to process q and removes m from the receive queue.

| Link model | Properties guaranteed |
|---|---|
| **Fair-loss** (weak but useful) | No infinite message losses — if a message is periodically repeated, it will eventually arrive; no infinite number of message duplications; no spurious messages (delivery of messages that have not been sent) |
| **Stubborn** | The message is repeated infinitely often over a fair-loss link; this results in guaranteed delivery without spurious messages |
| **Perfect / reliable** | No loss of messages; no duplication; no spurious messages |
| **Authenticated perfect** | A perfect link with correct sender identification |

**Where the models sit.** The link models belong to the "modelling communication" part of the models agenda, alongside modelling processes and modelling time. From the modelling introduction: a model is accurate insofar as analysing it yields truths about the system, and tractable if such analysis is actually possible; an accurate *and* tractable model includes exactly those attributes that affect the phenomena of interest.

## Key Properties

- **Explicit queues.** The send queue, the channel, and the receive queue are separate objects, so transport and delivery are distinct events.
- **Delivery is a runtime action.** `deliver(m)` is performed by q's runtime system, not the channel, keeping the channel's behaviour separate from the process's.
- **Fair-loss bounds the damage.** Loss may be repeated, but not infinitely, provided the sender retransmits periodically.
- **No spurious messages, in every model.** Even the weakest link never invents a message that was not sent.
- **Stubbornness is a retransmission strategy.** It converts a fair-loss link into guaranteed delivery without changing the protocol above it.
- **Perfectness is not security.** A perfect link says nothing about who sent the message; that is the gap authenticated perfect links close.
- **The models are composable assumptions.** Each is strictly stronger than the previous, so protocol proofs can be stated relative to the weakest rung that suffices.

## Worked Example

Two nodes exchange messages: A must know B received a request, and B must know A is still alive.

Step 1 — start with the weakest realistic channel, a fair-loss link. The channel may lose the request, may duplicate it, but will not invent one. Because the model is fair rather than arbitrary, a periodic retransmission is guaranteed to get through eventually. A duplicated request is possible, so B must handle the same request twice — idempotence, not deduplication by assumption.

Step 2 — note what fair-loss does *not* buy. It says nothing about a bound on how long the loss persists; "eventually" is a liveness statement, not a latency bound. And since the link is not synchronous, B cannot use a silence to conclude A is dead — a silent B and a slow B are the same observation.

Step 3 — move up to a stubborn link. The link now repeats the message infinitely often over the fair-loss link, so the message is guaranteed to arrive and no spurious messages appear. Duplication becomes the normal case rather than an exception, so a protocol written to be idempotent under fair-loss is unchanged; what changes is that a "no response" case now really means the message will eventually get there, so timeouts become liveness alarms rather than possible permanent loss.

Step 4 — move up to a perfect (reliable) link. No loss, no duplication, no spurious messages. The protocol layer can assume a one-to-one correspondence between sends and deliveries, removing a whole class of duplicate-handling logic. Note this is an *assumption the analysis makes*, not a property the implementation provides.

Step 5 — move up to an authenticated perfect link. Delivery is still one-to-one and lossless, but the receiver also learns the correct identity of the sender, which is what makes it safe to let a received message trigger state changes. Perfectness still gives no confidentiality: an eavesdropper can read what passes along the channel. That limitation is exactly what the eavesdropping fault class in [[failure-models]] introduces.

Step 6 — sanity check the choice. A protocol proved only against fair-loss links is correct on a perfect link too, since the perfect link satisfies the fair-loss guarantees; a protocol proved only against perfect links is not safe on a fair-loss link. The hierarchy direction decides what may be assumed when.

## Common Pitfalls

- **Equating "reliable" with "rarely loses".** In the lecture's table, reliable and perfect are the same rung, and both forbid loss. Confusion with the everyday sense of a reliable network (best effort, usually fine) is the most common misreading.
- **Missing the fair-loss nuance.** "No infinite message losses" is conditional on periodic repetition; a one-shot message sent once may indeed be lost forever under a fair-loss link.
- **Confusing duplication with spuriousness.** Fair-loss permits a finite number of duplications; it never permits an unsent message to appear. These are two different pathologies.
- **Treating stubborn links as a receiver-side fix.** Stubbornness is about repeating the message over the link, i.e. retransmission; it is not a mechanism the receiver performs.
- **Over-reading "perfect".** Perfect links say nothing about authentication, ordering, or confidentiality; authentication is a separate, stronger rung.
- **Losing the queue semantics.** `send(m)` enqueues, the channel moves it, `deliver(m)` dequeues and hands it over. Skipping the runtime step loses the distinction between "in flight" and "received".
- **Forgetting that this is the channel half of the model.** Failure responsibility is assigned to both processors and communications channels; a link model only covers the second.

## Connections

- [[failure-models]] — the processor-side counterpart, and the same hierarchy-of-assumptions logic applied to processes.
- [[distributed-system-properties]] — the "unreliable communication" and "variable delays" properties these models formalise.
- [[synchronous-vs-asynchronous-models]] — determines whether a timeout can be trusted to conclude that a message is lost.
- [[fault-error-failure-chain]] — a link's loss is the error that the protocol's recovery machinery must handle.
- [[model-accuracy-tractability]] — why one picks the weakest link model that still supports the guarantee.

## Open Questions

- The slides give the link models as a list of properties but do not say whether fair-loss implies bounded per-message loss counts or only the eventual-arrival property; the wording only rules out infinite loss.
- It is not stated whether ordering (FIFO per channel) is assumed for any model; the point-to-point slide mentions queues but no ordering guarantee.
- The source does not say how a fair-loss link is realised in practice, or whether the periodic retransmission is the sender's responsibility or a guarantee the link gives.
- The relationship between authenticated perfect links and the eavesdropping fault class is not drawn, even though confidentiality is out of scope for a perfect link.
- The lecture does not say whether the link models and the point-to-point queue model sit at the same level of abstraction, or whether the point-to-point model is the substrate the link models are defined on.
