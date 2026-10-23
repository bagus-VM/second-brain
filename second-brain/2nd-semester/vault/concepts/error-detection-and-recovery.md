---
title: "Error Detection and Recovery"
tags: [concept, dependable-distributed-systems, semester-2, fault-tolerance]
course: "Dependable Distributed Systems"
source_count: 7
status: current
last_updated: 2026-10-21
prerequisites: ["[[ways-towards-dependability]]"]
---

## One-line Summary
Fault tolerance has two moving parts — detect the error, then recover from it — and the lecture splits each of them into concrete sub-strategies you can pick from.

## Core Intuition

The whole architecture of fault tolerance is captured in a short list the lecture gives as the elements of fault tolerance:

```
Error detection
Recovery
    Error handling
        Backward recovery
        Forward recovery
        Compensation / masking
    Fault handling
```

The ordering matters. Detection comes first because recovery cannot be targeted without knowing that something went wrong; and recovery comes in two flavours because the two problems are genuinely different. **Error handling** deals with the corrupted *state* the system is in right now: it must be undone, overwritten, or hidden. **Fault handling** deals with the *cause* that is still present in the system: it must be diagnosed, isolated, worked around, or reset.

The division is why a system can be recovered from an error without the underlying fault being fixed — the state is clean, the cause remains, and the same thing will happen again unless fault handling also runs. Conversely, fault handling without error handling leaves the system in a bad state even after the cause is removed.

The lecture's framing of recovery is "restore a system state with errors and (possibly) faults into one without errors and faults". That parenthetical is the honest part: recovery is not always able to remove the fault too, which is precisely the gap that error masking papers over.

## Formal Definition / Statement

**Error detection, reactive.** Detects and reports errors at run-time, during operation.

| Technique | Purpose |
|---|---|
| Parity bits on memory, data buses, ALU, etc. | Detect corruption of stored or in-flight data |
| Coverage and flow-checking | Did the software hit all required checkpoints? |
| Multi-version comparison and majority voting | Compute multiple times and compare |

**Error detection, proactive.** The idea is to activate any faults before they can affect real computations. Detection happens at development-time, offline.

| Technique | Purpose |
|---|---|
| Execute self-tests, data consistency checks | Expose faults while the system is still in a controlled setting |
| Exercise the system to activate faults | Force latent faults to manifest |
| Memory scrubbing daemon | Periodically reads/resets all memory locations |

**Recovery.** Objective: restore a system state with errors and (possibly) faults into one without errors and faults. Two routes.

### Fault handling (4 items)

| Step | What it does | Example from the slides |
|---|---|---|
| **Fault diagnosis** | Identify the cause; once diagnosed, avoid using that resource / performing that operation again | Also known as the "Don't do that" solution |
| **Fault isolation** | Eliminate access to the source of the fault; exclude the faulty component from use | Shut down defective server in a server farm |
| **System reconfiguration** | Switch in spares or reassign tasks | Route traffic to a backup component |
| **System reinitialization** | Rebooting after repair or reconfiguration | Rebooting to perform "software rejuvenation" |

The slide's preamble to fault handling is: record faults to avoid later reactivation.

### Error handling (3 items)

| Strategy | Direction | Means given in the slides |
|---|---|---|
| **Roll-back** | Return the system to its state before the error occurred | Database commit (all-or-nothing execution semantics): if error, undo all partial results to restore a clean system state. Checkpoint/rollback: periodically snapshot system state and restore upon error to avoid failure. "Reboot is a very drastic rollback (reboot) to a checkpoint (a fresh system image)." |
| **Roll-forward** | Move the system forward into an error-free state | Retry to obtain an error-free result; proceed on and let the error flush itself out of the system — replication where a backup takes over after the working replica fails |
| **Error compensation / masking** | Provide correct service without an explicit recovery step | The system state has enough redundancy that the correct service can be provided without any noticeable glitch; recovery is achieved without explicit error detection |

**Masking: good and bad.** Good — the user is blissfully unaware of anything bad happening; fault/failure transparency is a great way to build systems. Bad — it rests on the independent-failure assumption and does not deal adequately with design faults.

## Key Properties

- **Reactive detection trades coverage for zero latency cost.** Parity and voting add overhead to every operation; proactive detection pays the cost offline instead.
- **Proactive detection is about activation, not observation.** The goal is to make a latent fault fire while nobody depends on the result.
- **Roll-back needs a clean earlier state.** Hence checkpoints: without a snapshot there is nothing to roll back to.
- **Roll-forward needs somewhere to roll into.** Retry only works if the failure is transient; replication only works if a good copy exists.
- **Masking needs no detection at all** — recovery is implicit in the redundancy of the state.
- **Fault handling and error handling are complementary.** One fixes the state, the other removes or routes around the cause.
- **Every strategy has a silent failure mode.** Roll-back can lose committed work; roll-forward can propagate the error; masking hides design faults; reinitialization loses in-memory state.
- **Detection quality bounds everything downstream.** A missed error turns into a failure that no recovery action can undo.

## Worked Example

Take a replicated key-value store, the same setting used elsewhere in the lecture, and walk one crash through the machinery.

**Step 1 — detection (reactive).** Node N1 is serving a client write. The value is stored in RAM, and the store checksums its memory pages. The page fails a checksum on read, so the error is detected and reported at run-time. Parity bits over the memory and the data bus would catch the same corruption earlier; a coverage check would additionally confirm that the code path actually executed the checkpoint it should have.

**Step 2 — detection (proactive), as a preventive counterpoint.** Had the faulty cell been found by the scrubbing daemon during a quiet period — the daemon periodically reads and resets all memory locations — it would have been swapped out before any client request ever touched it. The exercise of the system activates the fault in a controlled window rather than during a live request.

**Step 3 — error handling, roll-back.** The write is a database commit with all-or-nothing semantics. The checksum failure is detected before the commit is acknowledged, so all partial results are undone and the system returns to its last clean state. The store's periodic checkpoint is the other option: restore the snapshot instead of continuing. In the extreme, a reboot is a very drastic roll-back to a checkpoint — a fresh system image.

**Step 4 — error handling, roll-forward.** If instead the error had been transient and detected after the write was already durable, the store rolls forward: it retries to obtain an error-free result, or proceeds and lets the error flush itself out of the system. Replication is the structural version of this — the backup replica takes over once the working replica has failed.

**Step 5 — fault handling.** Now the cause is addressed. Diagnosis identifies the defective memory as the cause; the "Don't do that" solution is to avoid using that node or performing that operation again. Fault isolation excludes the faulty component from use — in a server farm, the defective server is shut down. System reconfiguration switches in a spare or reassigns tasks, routing traffic to a backup component. Finally, system reinitialization reboots the machine after repair or reconfiguration; a deliberate reboot also serves as "software rejuvenation", clearing accumulated state before it becomes a fault.

**Alternative, step 5′ — masking.** If the store were designed with space redundancy (see [[redundancy-forms]]), the faulty value could simply be outvoted by the other copies and the client would never notice. That is the good case: fault/failure transparency, no user-visible glitch, and no explicit error detection needed. The bad case is exactly the one the slide names — masking relies on the independent-failure assumption, so a design fault (or an attacker) that corrupts all copies defeats it silently.

## Common Pitfalls

- **Confusing error handling with fault handling.** Error handling fixes the *state*; fault handling deals with the *cause*. Mixing up "roll-back" and "fault isolation" in a diagram is a standard way to lose marks.
- **Listing three fault-handling steps instead of four.** Diagnosis, isolation, reconfiguration, reinitialization — all four.
- **Believing proactive detection happens at run-time.** It is development-time and offline; the scrubbing daemon is the exception in spirit but still works before faults affect real computations.
- **Forgetting that masking requires no explicit error detection.** That is precisely what distinguishes compensation from the other two error-handling strategies.
- **Treating reboot as a recovery strategy on its own.** The slide pins it as a very drastic roll-back to a checkpoint.
- **Claiming masking handles design faults.** The slide explicitly says it does not, and that it relies on independent failures.
- **Assuming roll-forward means the system fixes itself.** It moves forward into an error-free state; if no error-free state is reachable, it cannot be used.
- **Overclaiming detection coverage.** Parity detects single-bit-class corruption; the slides do not claim complete coverage, and silent errors remain the hard case (see [[fault-localization]]).

## Connections

- [[ways-towards-dependability]] — fault tolerance is one of the four strategies, and this page is its content.
- [[redundancy-forms]] — masking and replication both depend on structural redundancy.
- [[fault-error-failure-chain]] — detection interrupts the error-to-failure propagation.
- [[dependability-attributes]] — recovery speed is what MTTR measures.
- [[failure-models]] — a model of which errors are detectable is what makes a detection strategy choice rational.
- [[dependable-distributed-systems-lecture-1]] — the lecture these slides come from.

## Open Questions

- The slides do not quantify detection coverage — they list techniques but never say what fraction of errors each one catches, so no principled way to choose between parity, flow-checking, and majority voting is given.
- How a proactive self-test schedule should be chosen is not settled; the memory scrubbing daemon is named as an example, but the frequency and its cost are not discussed.
- The slides do not say how long a fault should be recorded, nor what "record faults to avoid later reactivation" means operationally in a large server farm.
- Roll-forward is described as letting the error "flush itself out of the system", but no criterion is given for when a roll-forward is safe rather than merely optimistic.
- The interaction between error masking and detection is not specified: the slide says masking needs no explicit error detection, but it is not said whether detection may still be present and simply be unnecessary.
- How much of the recovery machinery is expected to be replicated across a distributed system, and what the cost in consistency or latency is, is not covered in these slides.
