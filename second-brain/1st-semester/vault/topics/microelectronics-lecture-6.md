---
title: "CMOS Logic Gates and Digital Circuits"
tags: [topic, microelectronics, semester-1, course-microelectronics]
course: "Introduction to Microelectronics"
source_count: 2
status: current
last_updated: 2026-06-14
prerequisites: ["[[microelectronics-lecture-5]]", "[[cmos-inverter]]"]
sources: ["raw/lectures/introduction_to_microelectronics/Microelectronics6_2026.pdf"]
---

## One-line Summary
CMOS (Complementary MOS) combines an [[nmos-transistor]] pull-down network and a [[pmos-transistor]] pull-up network on the same chip to build every digital logic gate — inverter, NAND, NOR, XOR — with near-zero static power dissipation; the lecture walks through each gate and shows how an arbitrary Boolean function is realised by structuring the pull-up and pull-down networks as duals of each other.

## Core Intuition
The single [[cmos-inverter]] is the CMOS cell that proves the principle: an nMOS and a pMOS, gated by the same input, never conduct at the same time, so the steady-state current from V_DD to GND is essentially zero — only the brief switching transient draws power. Every more complex CMOS gate is a *generalisation* of this idea. Instead of one nMOS and one pMOS, you build:

- a **pull-down network (PDN)** of nMOS transistors connecting output to GND
- a **pull-up network (PUN)** of pMOS transistors connecting output to V_DD

The two networks are **logically dual** — exactly one of them conducts for any input combination. When the PDN conducts, the PUN is off and the output is pulled LOW. When the PDN is off, the PUN conducts and the output is pulled HIGH. This complementary structure is why CMOS gates idle at near-zero static power.

The pull-down and pull-up networks are constructed so that they implement, respectively, the function and its complement:

- **Parallel branches conduct for "OR"** in a given network.
- **Series branches conduct for "AND"** in a given network.
- The PDN implements F (the function); the PUN implements ¬F (the dual).

So a CMOS NAND gate has a PDN of two nMOS in **series** (both must be on → output LOW), and a PUN of two pMOS in **parallel** (either one being on → output HIGH). The dual pattern is what gives NAND, NOR, and arbitrarily complex gates their characteristic symmetric structure.

The XOR gate is the instructive exception: you cannot build XOR with a single complementary CMOS stage in a way that is fully restoring and ratio-less. It requires either a transmission-gate (pass-transistor) trick, a multi-stage implementation, or a more clever transistor arrangement. The lecture devotes 4 slides to showing different XOR constructions.

## Formal Definition / Statement

### CMOS gate construction rule

Given a Boolean function F(A, B, C, ...):

1. Build the **PDN** (pull-down, nMOS, to GND):
   - AND relationship → series connection of nMOS
   - OR relationship → parallel connection of nMOS
   - PDN is "on" (conducting) exactly when F = 1
2. Build the **PUN** (pull-up, pMOS, to V_DD):
   - Implement ¬F, the complement of F
   - PUN is "on" (conducting) exactly when ¬F = 1, i.e. F = 0

When F = 1, PDN conducts and PUN is open → output = GND.
When F = 0, PUN conducts and PDN is open → output = V_DD.
The output is therefore ¬F, but the PDN is built from F, so the gate is named after the function it pulls *down* — which is F, and the output is F̄.

### The standard gates

| Gate | PDN (nMOS) | PUN (pMOS) | Output |
|------|-----------|-----------|--------|
| Inverter (NOT) | single nMOS | single pMOS | ¬A |
| NAND | 2 nMOS in **series** | 2 pMOS in **parallel** | ¬(A ∧ B) |
| NOR | 2 nMOS in **parallel** | 2 pMOS in **series** | ¬(A ∨ B) |
| AND | NAND + inverter (two stages) | — | A ∧ B |
| OR | NOR + inverter (two stages) | — | A ∨ B |
| XOR | not constructible in a single complementary stage; needs transmission gate or 6+ transistor design | — | A ⊕ B |

### nMOS and pMOS silicon layout

The lecture opens with a top-view of an nMOS transistor and a pMOS transistor in silicon:

- **nMOS**: p-substrate; two n+ source/drain regions; polysilicon gate crossing over thin oxide; **no bulk (body) electrode** drawn in the standard cell (substrate is common).
- **pMOS**: the complement — n-well inside p-substrate; two p+ regions; same gate/oxide structure.

This is the "stick diagram" view of the devices from Lecture 5, now placed in their CMOS context: a CMOS gate is just one nMOS device and one pMOS device sharing the same input, mirrored in their wells.

### XOR — the gate that breaks the rule

A complementary CMOS gate is *ratio-less* — its output is always connected to either V_DD or GND through a conducting transistor, so the output is always a strong logic level. The XOR function, F = A ⊕ B = AB̄ + ĀB, cannot be implemented this way: the PDN that conducts for F has two parallel branches, each of which is a series pair. There is no dual pMOS network that perfectly complements it while keeping the output always driven. Solutions:

- **Transmission-gate XOR** (12 transistors): use both an nMOS and a pMOS in parallel as a switch controlled by A and Ā; route input B through two such switches. This is the textbook approach.
- **6T XOR** (six transistors): a clever static CMOS design with cross-coupled pMOS loads, used in dense arithmetic logic units.
- **Two-stage implementation** (e.g., A⊕B = (A∧¬B)∨(¬A∧B)): build it from AND/OR/INV stages at the cost of more delay.

The lecture shows all four of these on the slides. The takeaway for exams: when asked "can you build XOR in standard CMOS?", the answer is **no in one stage; yes with transmission gates**.

## Key Properties / Complexity

### Why CMOS dominates digital design
- **Near-zero static power**: in steady state, no DC path from V_DD to GND. Power is dissipated only during switching.
- **Full output voltage swing**: output reaches rail-to-rail (0 to V_DD), giving large noise margins.
- **High input impedance**: the gate oxide is insulating → no DC current into the gate → low drive requirement on preceding stages.
- **Scalable**: transistor dimensions can shrink with each process generation (Moore's law) without changing the topology.
- **Ratio-less**: output level does not depend on transistor sizing ratios (in contrast to older NMOS-only or pseudo-nMOS logic).

### Switching power
Dynamic power per gate per transition:
    P_dynamic = α · C_L · V_DD² · f
where α is switching activity, C_L is load capacitance, V_DD is supply voltage, f is clock frequency. This is *the* number to remember for power analysis: power scales with V², which is why every process generation reduces V_DD.

### Delay
Propagation delay through one gate:
    t_p ≈ 0.69 · R_eq · C_L
where R_eq is the equivalent on-resistance of the conducting transistor and C_L is the total load capacitance (own output + input capacitances of fan-out gates). Modern 7nm CMOS: t_p ≈ 10–20 ps per inverter.

### Power-delay product (PDP)
The figure of merit for a digital gate: PDP = P · t_p. Lower PDP = better. CMOS excels here.

## Worked Example

### Two-Input NAND (the workhorse of CMOS logic)

Schematic:
```
VDD ---[pMOS A]---+---[pMOS B]--- VDD
                 |
                 +----- Output (Y)
                 |
GND ---[nMOS A]---+---[nMOS B]--- GND
```
- Both pMOS in parallel between V_DD and output.
- Both nMOS in series between output and GND.
- Both gates driven by the same inputs A and B.

Truth table:

| A | B | PDN (nMOS series) | PUN (pMOS parallel) | Y |
|---|---|------------------|---------------------|---|
| 0 | 0 | off | both on | V_DD (1) |
| 0 | 1 | off | A's pMOS on, B's off | V_DD (1) |
| 1 | 0 | off | A's pMOS off, B's on | V_DD (1) |
| 1 | 1 | on | both off | GND (0) |

This is exactly ¬(A ∧ B) = NAND. The 4-transistor count (plus wells) is the canonical CMOS NAND.

### XOR via transmission gates (12T)

```
B ---+---[TG controlled by A]---+--- Y
    |                          |
    +---[TG controlled by Ā]---+
```
When A = 0, the top TG passes B directly to Y → Y = B = A ⊕ B (since A = 0).
When A = 1, the bottom TG passes ¬B to Y → Y = ¬B = A ⊕ B (since A = 1).
This realises XOR using two transmission gates plus an inverter (for Ā): 6 transistors.

## Common Pitfalls

- **Confusing "pull-down" with "output function"**: a NAND gate's *PDN* implements the AND function, but the gate is called NAND because the *output* is the AND inverted. The naming is symmetric: PDN for F, PUN for ¬F, output = ¬F.
- **Trying to build XOR in a single static CMOS stage**: the textbook CMOS rule (PDN for F, PUN for ¬F) cannot be satisfied for XOR with a single complementary pair. Either accept a multi-stage design, or use transmission gates.
- **Forgetting that AND/OR need an output inverter**: pure CMOS gives you NAND, NOR, NOT for free. AND = NAND + NOT (two stages), OR = NOR + NOT. Don't try to build AND directly with nMOS/pMOS — you can't, in static CMOS.
- **Confusing dynamic and static power**: CMOS is low-*static* power. *Dynamic* power (the αCV²f formula) is what limits modern chips, and it scales with switching activity, not with device count.
- **Ignoring leakage at modern nodes**: at 7nm and below, subthreshold leakage and gate-oxide tunneling make the "zero static power" claim only approximately true. Low-power design uses power gating, multi-Vt libraries, and reverse body bias to fight leakage.
- **Process variation at small geometries**: random dopant fluctuation causes V_T to vary transistor-to-transistor; this affects both speed (mismatch) and leakage (worst-case bits). Exam questions on "what happens when you scale CMOS" should mention these effects.

## Connections
- [[microelectronics-lecture-5]] — nMOS/pMOS transistors, three operating regions, I-V characteristics (this lecture is the application)
- [[mosfet]] — every CMOS gate is a network of MOSFETs
- [[nmos-transistor]] — the pull-down device
- [[pmos-transistor]] — the pull-up device (note: vault has both `pmos-transistor.md` and `pmtransistor.md` — same concept, two slugs; use the canonical `pmos-transistor`)
- [[mosfet-operating-regions]] — CMOS gates switch transistors between cutoff and triode; the saturation region is mostly avoided in digital design
- [[cmos-inverter]] — the atomic CMOS cell; every other gate is a generalisation
- [[digital-logic]] — CMOS is the implementation technology for all Boolean logic
- [[digital-circuit-design]] — the larger discipline of building arithmetic, memory, and control circuits from CMOS gates
- [[threshold-voltage]] — V_TH determines the switching threshold of every gate
- [[microelectronics-lecture-1]] — band theory that ultimately limits how small V_DD can go
- [[microelectronics-lecture-2]] — ion implantation and doping that determines V_TH
- [[microelectronics-lecture-3]] — pn junctions, the body effect, source-body bias

## Open Questions
- The lecture slides show XOR implementations but the lecture notes don't specify which construction the exam expects. (Need to re-verify by checking the recorded lecture or asking the lecturer.)
- How do FinFETs and gate-all-around (GAA) transistors change the CMOS gate picture at 3nm and below?
- What is the smallest meaningful CMOS gate? (Single-electron transistor, or quantum-dot devices, might one day replace CMOS.)
- Does the exam care about the body effect, or only about the gate structure?
