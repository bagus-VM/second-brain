---
title: "Exercise 5 — Consensus and Broadcast (Solutions)"
tags: [homework, dependable-distributed-systems, semester-2, broadcast, consensus]
course: "Dependable Distributed Systems"
source_count: 1
status: current
last_updated: 2026-11-10
prerequisites: ["[[dependable-distributed-systems-lecture-5]]"]
---

# Dependable Distributed Systems — Exercise 5

Source: `raw/lectures/Dependable Distributed Systems/Ubung/dds26-exercise05.pdf` (Reiser, WS 2026/27; discussion 2026-11-11). The sheet says to prepare answers and present them in class. No AI-prohibition appears in the sheet.

## 5.1 Consensus without faults

Fix a coordinator, say `P1`. Each process `Pi` sends its proposal `(PROPOSE, i, vi)` to `P1`. The coordinator waits for one proposal from every process, selects the proposal with the smallest process identifier, and sends `(DECIDE, v)` to all processes. A process decides once, when it receives that decision.

```text
upon Propose(v) at process Pi:
    send (PROPOSE, i, v) to P1

upon receiving proposals from all n processes at P1:
    v := value proposed by the smallest process identifier
    send (DECIDE, v) to all n processes

upon receiving (DECIDE, v):
    if not decided:
        decided := true
        output Decide(v)
```

Assumptions: no process fails, every point-to-point link eventually delivers, and each process proposes once. The choice rule is deterministic; every process receives the same coordinator decision.

- **Termination:** all proposals eventually reach `P1`; it sends the decision; all processes eventually receive it.
- **Agreement:** only `P1` selects the decision, and it sends that same value to everyone.
- **Validity:** `P1` selects one of the received proposals, so the decision was proposed.
- **Integrity:** the local `decided` guard permits one decision per process.

With the exercise's cost model, collecting proposals costs `n` unicasts in one step; sending the decision costs `n` unicasts in one further step. Total: **2 latency steps, 2n messages**. This deliberately simple algorithm is not fault tolerant: if `P1` crashes, no process decides; if any proposer crashes before sending, `P1` waits forever. Both failures are excluded in 5.1.

## 5.2 Bracha reliable broadcast: Lemmas 2–4

Use `n=3f+1`, reliable links, and the lecture's Lemma 1: no correct process sends `ready` for two different values. A correct process sends at most one `ready` per broadcast instance.

### Lemma 2 — two correct acceptors accept the same value

Suppose correct `p` accepts `v` and correct `q` accepts `u`. Each acceptance requires `2f+1` distinct `ready` senders. Since at most `f` are faulty, each set contains at least `f+1` correct senders. There are exactly `n-f=2f+1` correct processes. Any two subsets of at least `f+1` elements in a universe of `2f+1` elements intersect:

`(f+1) + (f+1) - (2f+1) = 1`.

So some correct process sent both `ready(v)` and `ready(u)`. By Lemma 1, it cannot have sent ready for two values. Therefore `u=v`.

### Lemma 3 — one correct acceptor implies all correct processes accept

If correct `p` accepts `v`, it has received `2f+1` ready messages for `v`. At least `f+1` came from correct processes. Reliable links eventually deliver those `f+1` messages to every correct process `q`. If `q` has not already sent `ready(v)`, the `f+1`-ready rule makes it send `ready(v)` to everyone. Thus every correct process eventually sends `ready(v)`. There are `n-f=2f+1` correct processes, so each correct process eventually receives `2f+1` ready messages for `v` and accepts it.

### Lemma 4 — a correct transmitter's value is accepted by all

Let the correct transmitter send `v`. Every correct process eventually receives `(initial,v)` and sends `echo(v)`. Hence every correct process eventually sees all `n-f=2f+1` correct echoes. For `n=3f+1`,

`(n+f)/2 = (4f+1)/2 = 2f + 0.5`,

so `2f+1 > (n+f)/2`. The echo threshold therefore triggers `ready(v)` at every correct process. Each then receives the `2f+1` ready messages from correct processes and accepts `v`.

## 5.3 Atomic broadcast: latency and message complexity

Assume the stated cost model: point-to-point send is one step and one message; broadcast is `n` simultaneous unicasts, one step and `n` messages. Counts below include the listed token transfers in the token case and exclude local computation/delivery.

### (a) Sequencer variants

| Variant | Communication rounds | Latency | Messages |
|---|---|---:|---:|
| UB: sender unicasts payload to sequencer; sequencer broadcasts payload | 2 | **2** | `1+n` |
| UUB: sender unicasts payload to sequencer; sequencer returns sequence number; sender broadcasts numbered payload | 3 | **3** | `1+1+n = n+2` |
| BB: sender broadcasts payload; sequencer broadcasts the sequence number | 2 | **2** | `n+n = 2n` |

Latency assumes the sender and sequencer are distinct. The sheet does not specify whether to discount self-messages when the sender or sequencer is included in a broadcast; under its explicit broadcast-cost rule, each broadcast is counted as `n` unicasts.

### (b) Circulating token

A token transfer is one point-to-point message and one latency step; once the sender has the token, it broadcasts the payload in one step (`n` messages).

- **(i) Sender already holds the token:** latency **1**, messages **n**.
- **(ii) Worst case before the sender may broadcast:** the token is just past the sender, so it takes `n−1` transfers to return. Then the payload broadcast takes one more step. Latency **n**; messages **(n−1)+n = 2n−1**.

This worst-case count is for one payload and counts only the token's travel until the sender gets it, not the continuing background circulation after the payload. The question explicitly permits ignoring on-demand token requests.

### (c) Communication history

Choose Lamport timestamps. The sender attaches its timestamp to the payload and sends one broadcast, so dissemination uses **n messages** under the stated model. In an asynchronous system there is no known upper bound on message delay. A receiver cannot safely decide that no message with an earlier timestamp is still in flight merely because it has waited a fixed number of steps. Thus delivery latency has **no small fixed constant bound**; it may grow with how long the receiver must wait for evidence that earlier messages cannot arrive. Lamport timestamps order causality but do not by themselves provide that evidence.

## Connections

- [[dependable-distributed-systems-lecture-5]] — source overview and the definitions/protocols used here.
- [[dependable-distributed-systems-lecture-4]] — atomic broadcast and the asynchronous impossibility remark introduced there.
- [[byzantine-reliable-broadcast]] — Bracha protocol and threshold rationale.
- [[atomic-broadcast]], [[consensus]] — ordering families and the consensus reduction.
- [[broadcast-order-semantics]], [[lamport-logical-clocks]] — total order and timestamp background.

## Open Questions

- The sheet specifies best-case latency and a simplified cost model; it does not include processing time, queueing, self-send discounts, retransmission, or failure recovery.
- The token case assumes a continuously circulating token and a known ring order; token loss and recovery are outside this cost exercise.
- The communication-history answer explains why there is no fixed small bound; the sheet does not prescribe a particular timestamp-delivery algorithm or a precise latency formula.
