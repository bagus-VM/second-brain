---
title: "Model Accuracy and Tractability"
tags: [concept, dependable-distributed-systems, semester-2, modelling]
course: "Dependable Distributed Systems"
source_count: 1
status: current
last_updated: 2026-10-21
prerequisites: ["[[distributed-system-properties]]"]
---

## One-line Summary
A model is a simplification you are allowed to argue with — but only if the simplification is both faithful to reality and small enough to analyse.

## Core Intuition

Modelling is the move that makes distributed systems analysable at all. A real system has thousands of components, real-time behaviour, and a failure history nobody recorded. A model throws all of that away and keeps a set of attributes plus rules for how those attributes interact — and that is only worth doing if the throwaway was disciplined.

The lecture's framing is deliberately plural: "There is no single correct model." A model is chosen by the *question being asked*. If you want to know whether an algorithm terminates, you model processes and their failures. If you want to know whether a protocol is cheap, you model the network. If you want to know whether a checkpoint is consistent, you model time. One model cannot answer all three, and pretending otherwise produces conclusions that are true of the model and false of the system.

The two properties that make a model good pull against each other. Accuracy is the easy half: keep everything relevant and you are accurate. Tractability is the hard half: analysis must actually be *possible*. The level of detail is the knob, and setting it is the whole discipline.

## Formal Definition / Statement

A **model** is "a simplification of an object (= system)". More precisely, "a collection of attributes and a set of rules that govern how these attributes interact" — also called a theory.

**Good models**, in the lecture's definitions:

- **Accurate:** "A model is accurate to the extent that analyzing it yields truths about the object of interest."
- **Tractable:** "A model is tractable if such an analysis is actually possible."

These are independent properties. The slide states the key asymmetry: "Defining an accurate model is not difficult; defining an accurate + tractable model is." An accurate+tractable model "will include exactly those attributes that affect the phenomena of interest" — and "Level of detail is a key issue."

**The two questions a distributed-systems model must answer:**

1. **Feasibility.** "What classes of problems can be solved?" — this "can head off wasted effort in design, implementation, and testing."
2. **Cost.** "For those classes that can be solved, how expensive must the solution be?" — this "support[s] evaluating any solution we devise" and lets us "avoid designs requiring protocols that are inherently slow or expensive."

**A model is a set of assumptions.** The slide's exercise slide makes the point explicitly: "What are the assumptions above?" and, in the failure-model section, "Important: these are models = assumptions!" The assumption set is the model's contract with reality, and it is where the risk lies.

The historical illustration on the slides makes the point without needing to be taken seriously as physics: the atom has been modelled as a billiard ball (Dalton, 1803), a plum pudding (Thomson, 1897), a solar system (Rutherford 1911, Bohr 1913), and an electron cloud (1920s). Each was accurate for its question and wrong for the next question.

## Key Properties

- **Model choice is question-driven.** Different questions need different models; there is no single correct one.
- **Accuracy and tractability are separate axes.** A model can be accurate and intractable (a full simulation of the real system) or tractable and inaccurate (a too-coarse abstraction).
- **The attribute set defines the scope.** Attributes outside the set are invisible to the analysis, and therefore cannot influence any conclusion drawn from it.
- **A model is a contract.** Its assumptions are the boundary of what its conclusions apply to.
- **Feasibility and cost are the two outputs.** A model that answers neither is a diagram, not a model.
- **The abstraction is where the risk lives.** A conclusion transferred from model to system is only as strong as the assumptions it rests on.

## Worked Example

The same distributed system, three models, three different questions. Take a cluster of $n$ nodes over a network:

**Model A — processes and failures only.** Nodes are processes that may crash; the network is invisible. *Question answered:* can the algorithm reach a decision if up to $t$ nodes crash? The failure model and the $t$-fault-tolerance threshold carry the whole argument. *Assumption:* the network never corrupts or reorders messages.

**Model B — communication.** The channel is fair-loss: messages may be lost or duplicated, but a periodically repeated message eventually arrives and no spurious messages appear. *Question answered:* does the protocol still terminate, and at what message cost? *Assumption:* no bound on delay, so no timeout can be used to conclude failure.

**Model C — time.** The system is synchronous: relative process speeds and channel delays are bounded. *Question answered:* can a cheaper protocol be used, and what is the timeout value? *Assumption:* the bound exists and is known.

The three models give three different answers to "is this system dependable?" — and none of them is wrong, because each answers a different question. A student who picks Model A and concludes "the system is fault-tolerant" has not made an error of analysis; they have made an error of scope, and the fix is to state the assumption set alongside the conclusion.

## Common Pitfalls

- **Transferring a conclusion outside the model's scope.** The most common exam trap: an answer that is true of the model and silently assumed true of the system.
- **Conflating accuracy with tractability.** "Detailed" is not the same as "good". A model with every real parameter is a simulation, and simulations do not yield theorems.
- **Asking the model a question it was not built for.** Time-related conclusions need the time model; failure-related conclusions need the failure model.
- **Reading "no assumptions" as "no model".** The asynchronous model *is* a model — see [[synchronous-vs-asynchronous-models]].
- **Ignoring the failure model when reasoning about liveness.** A protocol that tolerates crash but not omission is not fault-tolerant, whatever the time model says.

## Connections

- [[synchronous-vs-asynchronous-models]] — the canonical example of one question (feasibility and cost) needing several models.
- [[failure-models]] — the process-level model, and the assumption set that a t-fault-tolerance claim rests on.
- [[communication-link-models]] — the channel-level model, and where fair-loss versus perfect changes the protocol.
- [[distributed-system-properties]] — the properties of the system being modelled; each maps onto a modelling choice.
- [[dependable-distributed-systems-lecture-2]] — the lecture in which this material sits, before the time material that follows it.

## Open Questions

- The slides give no criterion for choosing between models — only that different questions need different models. How one decides that a model is the right one for a given design problem is left open.
- The claim that an accurate+tractable model "will include exactly those attributes that affect the phenomena of interest" is a prescription without a method: nothing says how to find that attribute set for an unfamiliar system.
- No example is given of a model that was accurate but not tractable, nor of a conclusion that changed when the model was refined.
- The relationship between the model's assumption set and the later failure-model hierarchy (which classes a protocol must tolerate) is not drawn explicitly.
