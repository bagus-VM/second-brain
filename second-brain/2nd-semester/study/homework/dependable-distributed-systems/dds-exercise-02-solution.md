---
title: "Exercise 2 — Models and Logical Clocks (Solutions)"
tags: [homework, dependable-distributed-systems, semester-2]
course: "Dependable Distributed Systems"
source_count: 2
status: current
last_updated: 2026-10-21
prerequisites: []
---

# Dependable Distributed Systems — Exercise 2

Source: `dds26-exercise02.pdf` (Reiser, WS 2026/27, discussion 21 October 2026).
Sheet instruction: **"Prepare answers before the exercise class. In class you will present
them."**

Everything numeric in this sheet is **computed**, not asserted. The script
`logical-clocks.py` in this folder derives the Lamport and vector timestamps, enumerates all
175 linear extensions of the happens-before relation to prove the assignment is forced by
causality rather than by the order in which concurrent events happen to be listed, and checks
both total orders for consistency with causality. The recorded output is in
`output-logical-clocks.txt`.

---

## 2.1 Does the statement satisfy the synchronous assumption?

> "On my server, no request ever takes more than 1 week to be processed."

**Formally: yes.** The synchronous assumption is that the relative speeds of processes and the
delays of the communication channels are *bounded*. A week is a finite bound, so the statement
satisfies the assumption. The trap in this question is the instinct that a week is "not
bounded" because it is so large — but the assumption asks for a bound, not a small one.

**But the bound is useless, and that is the real answer.** The slide states what synchronicity
buys: "In asserting that a system is synchronous, we rule out certain system behaviors. This
enables us to employ simpler protocols (complexity), cheaper protocols (overhead) than required
in an asynchronous system." The saving comes from *exploiting* the bound — setting a timeout
just above the worst case, and knowing that after it, the node is really dead. A one-week
timeout is not a protocol optimisation; it is a protocol that has given up.

So the answer has two halves, and both belong in the presentation: the assumption is met, and
meeting it is worth nothing.

**The narrower reading, which the statement does not settle.** The claim bounds *request
processing* on *this server*. The synchronous model needs bounds on the relative speeds of
processes and on channel delays *system-wide*. A bound on one server's request latency implies
bounds on the components along that request's path, but it says nothing about the other
processes, other links, or other workloads. Whether the intended scope is "this server" or "my
whole system" changes what follows, and the statement does not say which is meant.

---

## 2.2 Models in distributed systems

### (a) True or false

| Statement | Answer | Reason |
|-----------|--------|--------|
| "A model is accurate only if it is tractable" | **F** | These are two independent properties, and the slide separates them: a model "is accurate to the extent that analyzing it yields truths about the object of interest", and separately "is tractable if such an analysis is actually possible". The slide's own emphasis is that *defining* an accurate model is easy while defining an **accurate + tractable** model is the hard part — which is only a difficulty if the two come apart. An accurate but intractable model is the normal case: full fidelity to a real system is usually unanalysable. |
| "Models of distributed systems make it possible to predict the feasibility and costs of algorithms or protocols" | **T** | This is precisely the pair of questions the lecture says models are built to answer: **Feasibility** — "What classes of problems can be solved?", which "can head off wasted effort in design, implementation, and testing"; and **Cost** — "For those classes that can be solved, how expensive must the solution be?", which "support[s] evaluating any solution we devise" and avoids "designs requiring protocols that are inherently slow or expensive". |
| "In an asynchronous system you make the assumption that for most messages the time between sending and receiving the message is infinite" | **F** | The slide's definition of asynchronous is that "we make no assumptions about process execution speeds and/or message delivery delays" — and the slide makes the philosophical point sharply: "Postulating that a system is asynchronous is a non-assumption." A model that asserts infinite delay for most messages is making an assumption, and it is a *different* assumption. The unbounded-delay model is the one used as a hypothesis in impossibility arguments, where an adversary may delay messages indefinitely; that is not the same thing as assuming no bounds exist in the system. The phrase "for most messages" is also a hedge that fits no model on the slide. |
| "Using a Byzantine fault model instead of a crash fault model has only advantages" | **F** | The hierarchy of fault classes is nested, and Byzantine ("arbitrary") sits outermost — it contains every other class. So a Byzantine-tolerant protocol *is* crash-tolerant. But the containment runs the wrong way for the claim: a crash-tolerant protocol need not tolerate Byzantine behaviour, and moving up the hierarchy costs something. The requirement on the number of replicas is the visible price — tolerating $f$ Byzantine faults needs a substantially larger quorum than tolerating $f$ crashes — and the guarantees obtainable are correspondingly weaker. "Only advantages" is false: generality is bought with overhead. |
| "Algorithms designed for an asynchronous system model can be used without modification in a synchronous system" | **T** | The slide states it directly: "Postulating that a system is asynchronous is a non-assumption. Every system 'is' asynchronous (i.e. satisfies assumptions that are made). Algorithm for asynchronous system . . . can be used on every system!" A synchronous system is a special case of an asynchronous one, so an asynchronous-correct algorithm is correct on it. The asymmetry runs the other way and is why the slide can say synchronous systems permit "simpler protocols (complexity), cheaper protocols (overhead)": those savings are only accessible to algorithms designed *for* the stronger assumption. |

### (b) When are crash-recovery and fail-silent practically identical?

**The case:** a system of $n$ processes on an asynchronous network, with at most $f$ faulty
processes, **no failure detector**, and the additional assumption that a crashed process **never
recovers** — it stays down for the rest of the execution.

In that setting the two models are observationally identical *for the surviving processes*.
Under crash-recovery, a process that stops forever is faulty, and the "recovery" part of the
model simply never fires. Under fail-silent, other processes are not reliably notified. So from
the outside, in both models, the crashed process is simply silent: it sends nothing, and nobody
can prove it is dead rather than slow. The fail-silent qualifier adds nothing once recovery is
ruled out, because the only thing it would have added — the *possibility* of later reappearing —
has been removed.

The assumption that does the work is **asynchrony**. In a synchronous system, a crash is
reliably detectable (the process misses a deadline), and fail-silent is impossible by
construction — which is exactly what the slide's fail-stop model says: "All other operational
processes reliably detect the crash." So the coincidence of the two models is a direct
consequence of the failure-detection problem that the lecture's later consensus material
exists to solve.

---

## 2.3 Properties of logical clocks

Given $C(a) < C(b)$.

### (a) With Lamport clocks

| Statement | Verdict |
|-----------|---------|
| $a \to b$ (a causally before b) | **Undecidable.** $C(a) < C(b)$ is *necessary* for $a \to b$ but not *sufficient*. The slide's property is one-directional: $e_1 \to e_2 \implies t(e_1) < t(e_2)$, and "The other direction $t(e_1) < t(e_2) \Rightarrow e_1 \to e_2$ does not hold!" A smaller counter is evidence of possible causation, never proof. |
| $b \to a$ | **Certainly false.** If $b \to a$, the ordering property would give $C(b) < C(a)$, contradicting the premise. A process's own counter also never decreases, so $C(b) < C(a)$ is impossible here. |
| a happened before b in real time | **Undecidable.** Real-time order and causal order are independent. If $a \to b$ then a precedes b physically, but $a \to b$ is itself undecidable here; and if the two are concurrent, either physical order is possible. The Lamport counter measures causal depth, not elapsed time. |
| b happened before a in real time | **Undecidable.** Same reasoning — and note this is *not* the same as "$b \to a$", which is certainly false. Real-time precedence without causation is perfectly possible. |
| a and b are concurrent (neither $a \to b$ nor $b \to a$) | **Undecidable.** Since $b \to a$ is certainly false, they are concurrent exactly when $a \to b$ is false — and whether $a \to b$ holds cannot be determined from $C(a) < C(b)$. |

### (b) With vector clocks, $V(a) < V(b)$

Here the verdict changes on every line, and the reason is single: for vector clocks the relation
"<" *is* the causal relation. The slide states it as an equivalence — "Creates a causal order:
$t(e_1) < t(e_2) \Leftrightarrow e_1 \to e_2$" — and defines it as
$t(e_1) < t(e_2) \Leftrightarrow (\exists i:\, a_i \le b_i) \land (\exists i:\, a_i < b_i)$.

| Statement | Verdict |
|-----------|---------|
| $a \to b$ | **Certainly true.** It is the definition. |
| $b \to a$ | **Certainly false.** The relation is antisymmetric: $V(b) < V(a)$ cannot hold alongside $V(a) < V(b)$. |
| a happened before b in real time | **Certainly true.** Causality requires physical precedence: an event cannot influence a later one. |
| b happened before a in real time | **Certainly false.** |
| a and b are concurrent | **Certainly false.** The vector order is exactly the causal order, so causally-related means not concurrent. |

**The point of the exercise.** Lamport timestamps give a *one-way* implication, so from
$C(a) < C(b)$ alone you cannot conclude anything about whether the events are causally related
and you cannot rule out concurrency. Vector timestamps give the *equivalence*, so the same
question becomes decidable. That is the entire justification for the extra $N-1$ numbers per
message — see [[vector-clocks]].

---

## 2.4 Logical clocks and fault tolerance

> Can a crash of a single process violate the ordering property $a \to b \Rightarrow C(a) < C(b)$?

**No.** The ordering property is a property of the *algorithm*, not of the system's health, and a
crash cannot break it. The reasoning:

1. **A crash only removes events.** A crashed process stops executing steps, so it contributes
   fewer events to the history. It never introduces a new event, and it never changes the
   relative order of events that did occur.
2. **Causal dependencies arise only from program order and message passing.** Both are
   unaffected by an unrelated process crashing.
3. **A counter never decreases.** The receive rule $C_i := \max(C_i, t_m) + 1$ and the local rule
   $C_i := C_i + 1$ are both monotone. So the timestamps of the surviving events are exactly the
   values they would have had in a run with no crash at all.

The proof of the property proceeds by induction over the two ways an event can be causally
dependent on an earlier one — it follows from a local step on the same process, or from a
message received from one — and neither induction step mentions whether any *other* process is
alive. A crash is invisible to the argument.

**The caveat worth adding in the presentation.** A crash preserves the property but can destroy
the *information* the property carries. Under the crash-recovery model, a process that restarts
and loses its local state must reconstruct its counter, and nothing in the algorithm tells it
what value to resume from. If it restarts at zero, its subsequent events carry timestamps
smaller than the ones it has already sent. The property $a \to b \Rightarrow C(a) < C(b)$ still
holds for every pair of events — the `max` in the receive rule protects the receiver, and the
sender's own counter is still monotone within its new incarnation. What is lost is the causal
*link* across the crash: a process that had causally depended on the pre-crash events of the
restarted process no longer has evidence of it, because the restarted process's new incarnation
has a fresh, smaller counter. The ordering property is a guarantee about timestamps, not about
the completeness of the causal history, and a crash can break the latter without touching the
former.

---

## 2.5 Total order with vector clocks

The lecture's scalar construction: Lamport clocks define a partial order, and the total order
is obtained by comparing the tuples $(C_k, k)$ — first the clock, and when the clocks are equal,
the node ID. Vector clocks define a partial order too, so the same move is available: compare
the tuples $(V_k, k)$.

**The construction.**

$$V(a) <' V(b) \iff \big(\text{compare } V(a) \text{ and } V(b) \text{ lexicographically}\big) \ \lor\ \big(V(a) = V(b) \land a.\text{node} < b.\text{node}\big)$$

Two points make this a total order, and one makes it the *right* one.

1. **Componentwise comparison is not a total order.** The natural relation "$\le$ componentwise"
   is a partial order: two vectors such as $(1,0,0)$ and $(0,1,0)$ are incomparable. So the
   comparison must be **lexicographic** — compare component 1, then component 2, and so on —
   which is a total order on fixed-length vectors. (This is exactly the mistake to avoid: the
   scalar version compares $C$ with $<$, which is total because a scalar *is* totally ordered;
   vectors are not.)
2. **The node ID tie-break is redundant but harmless.** Two distinct events never carry the same
   vector timestamp, because the increment of the own component is what distinguishes them — so
   the tie-break never fires. It is included for symmetry with the scalar construction and for
   the case where a process is cloned and two incarnations share a component.
3. **It is a linear extension of the causal order.** If $a \to b$ then $V(a) \le V(b)$
   componentwise with $V(a) \ne V(b)$, so at the first index where the two vectors differ,
   $V(a)$'s component is strictly smaller — and lexicographic comparison therefore gives
   $V(a) <' V(b)$. Causality is never contradicted. The script checks this mechanically for
   every causally related pair.

**Note what this is not.** The total order is a *convention*, not a fact. Lexicographic
comparison is a way of making a partial order total, and different tie-breaks give different
total orders — the same situation as the Lamport case, where the tie-break is the node ID.
What the vector version buys is not a different total order but a *different partial order*:
one in which concurrency is visible instead of hidden.

---

## 2.6 Logical clocks — example

**The diagram.** Three processes, time running left to right:

```
P1 :  e1,1 ------> e1,2 --------> e1,3
P2 :  e2,1 --------------> e2,2
P3 :  e3,1 -----------------> e3,2
                     m1  (e2,1 -> e3,2)
```

Program order: e1,1 → e1,2 → e1,3; e2,1 → e2,2; e3,1 → e3,2. One message: **m1, sent by e2,1
and received by e3,2.** (The diagram was read out of the PDF's vector geometry — lifeline
positions, dot coordinates, and the arrowhead endpoint — because the text layer garbles the
labels.)

### (a) Lamport timestamps

Rule: local action or send → $C := C + 1$; receive of a message carrying $t_m$ →
$C := \max(C, t_m) + 1$. Each process starts at 0.

| Step | Event | Action | Counter | Timestamp |
|------|-------|--------|---------|-----------|
| 1 | e1,1 | local on P1 | $C_1 = 0 + 1$ | **1** |
| 2 | e3,1 | local on P3 | $C_3 = 0 + 1$ | **1** |
| 3 | e2,1 | local on P2; **sends m1** with $t_m = 1$ | $C_2 = 0 + 1$ | **1** |
| 4 | e1,2 | local on P1 | $C_1 = 1 + 1$ | **2** |
| 5 | e3,2 | **receives m1** ($t_m = 1$) | $C_3 = \max(1, 1) + 1$ | **2** |
| 6 | e2,2 | local on P2 | $C_2 = 1 + 1$ | **2** |
| 7 | e1,3 | local on P1 | $C_1 = 2 + 1$ | **3** |

**Deriving a total order.** Use the lecture's construction: compare the tuples $(C_k, k)$,
i.e. clock first, node ID to break ties.

| Event | $C$ | node | tuple |
|-------|-----|------|-------|
| e1,1 | 1 | 1 | (1, 1) |
| e2,1 | 1 | 2 | (1, 2) |
| e3,1 | 1 | 3 | (1, 3) |
| e1,2 | 2 | 1 | (2, 1) |
| e2,2 | 2 | 2 | (2, 2) |
| e3,2 | 2 | 3 | (2, 3) |
| e1,3 | 3 | 1 | (3, 1) |

**Total order:**

$$e_{1,1} < e_{2,1} < e_{3,1} < e_{1,2} < e_{2,2} < e_{3,2} < e_{1,3}$$

### (b) Vector timestamps

Rule: local event on $P_i$ → $C_i[i] := C_i[i] + 1$; send → the message carries the sender's
vector; receive on $P_i$ → increment the own component, then $C_i[k] := \max(C_i[k], t_m[k])$
for all $k$. $N = 3$.

| Step | Event | Vector | Reasoning |
|------|-------|--------|-----------|
| 1 | e1,1 | **(1, 0, 0)** | P1's own component incremented |
| 2 | e3,1 | **(0, 0, 1)** | P3's own component incremented |
| 3 | e2,1 | **(0, 1, 0)** | P2's own component incremented; m1 now carries (0, 1, 0) |
| 4 | e1,2 | **(2, 0, 0)** | P1's own component incremented again |
| 5 | e3,2 | **(0, 1, 2)** | own component → 1, then merge with (0, 1, 0): component 2 becomes 1, component 3 stays 2 |
| 6 | e2,2 | **(0, 2, 0)** | P2's own component incremented again |
| 7 | e1,3 | **(3, 0, 0)** | P1's own component incremented again |

Note component 2 of e3,2: it is 1, inherited from the message P2 sent. That single entry is the
record of the message, and it is exactly what the Lamport counter throws away.

**Deriving a total order.** Compare the vectors lexicographically, with the node ID as a
tie-break (Exercise 2.5):

| Event | Vector | lexicographic rank |
|-------|--------|--------------------|
| e3,1 | (0, 0, 1) | 1 |
| e2,1 | (0, 1, 0) | 2 |
| e3,2 | (0, 1, 2) | 3 |
| e2,2 | (0, 2, 0) | 4 |
| e1,1 | (1, 0, 0) | 5 |
| e1,2 | (2, 0, 0) | 6 |
| e1,3 | (3, 0, 0) | 7 |

**Total order:**

$$e_{3,1} < e_{2,1} < e_{3,2} < e_{2,2} < e_{1,1} < e_{1,2} < e_{1,3}$$

**Two things worth saying out loud in the presentation.**

*The two total orders differ, and that is not a contradiction.* The Lamport order puts e1,1
first; the vector order puts e3,1 first. Both are valid linear extensions of the same causal
order — the script verifies that for every causally related pair — and they differ because the
tie-breaks differ. Any total order over concurrent events is a convention.

*The partial orders differ, and that is the substantive difference.* Compare e1,2 and e3,2: both
have Lamport timestamp 2, and their vectors are (2,0,0) and (0,1,2) — incomparable. The
Lamport clock cannot tell you these two events apart in terms of causality; the vector clock
can, because e2,1 → e3,2 makes them causally related while e1,2 is concurrent with both. The
script enumerates all 16 concurrent pairs in this diagram and prints their Lamport and vector
values side by side.

---

## Verification

`logical-clocks.py` was run; `output-logical-clocks.txt` holds the recorded output. It:

- computes both availability figures from 1.3(c) (reproduced here for completeness: A = 0.997268,
  B = 0.994083);
- derives the Lamport and vector timestamps of the 2.6 diagram and the two total orders;
- enumerates **all 175 linear extensions** of the happens-before relation and confirms there is
  exactly **1** distinct Lamport assignment and **1** distinct vector assignment across all of
  them — so the timestamps are forced by causality, not by the order the concurrent events were
  listed in;
- verifies that both total orders are linear extensions of happens-before;
- lists all 16 concurrent pairs with their Lamport and vector values.

---

## Connections

- [[lamport-logical-clocks]] — the algorithm applied in 2.6(a) and the one-way property that 2.3(a) tests.
- [[vector-clocks]] — the algorithm applied in 2.6(b) and the exact causal order that 2.3(b) tests.
- [[synchronous-vs-asynchronous-models]] — the model question in 2.1 and the "no assumptions" reading in 2.2(a).
- [[failure-models]] — the fail-silent, crash-recovery, and Byzantine models of 2.2, and the hierarchy behind the "only advantages" question.
- [[model-accuracy-tractability]] — the accuracy/tractability distinction behind 2.2(a).
- [[clock-synchronization-problem]] — why the logical clocks of 2.6 exist at all.
- [[dependable-distributed-systems-exercise-1]] — the preceding sheet.

## Open Questions

- The sheet does not say how the exercise presentations are graded or whether a grade is attached
  to them at all.
- The diagram's orientation (time running left to right, processes stacked vertically) is
  opposite to the time-space diagram in lecture 2, which runs time downwards. Whether this is
  deliberate is not stated.
- In 2.1, whether the bound is meant to cover the whole system or only the one server is
  ambiguous in the statement, and the two readings lead to different answers.
- The 2.6 question asks for *a* total order; the sheet does not say whether the grader expects
  the specific one derived from the given construction, or any linear extension of the causal
  order.
