---
title: "CMOS Logic Gates"
tags: [concept, microelectronics, digital-logic, semester-1, course-microelectronics]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[cmos-inverter]]", "[[nmos-transistor]]", "[[pmos-transistor]]"]
---

## One-line Summary
The CMOS logic family builds every Boolean function as a *complementary* pair of networks: an nMOS pull-down network (PDN) that conducts when the function is true, and a pMOS pull-up network (PUN) that conducts when the function is false; this structure gives near-zero static power, full output swing, and high noise margin, with the exception of XOR which cannot be built in a single stage this way.

## Core Intuition
The CMOS logic family is the *standard implementation* of digital circuits because of one structural property: at any input combination, **exactly one** of the PDN or PUN conducts. The output is therefore always tied to a power rail (V_DD or GND) through a low-resistance path. This gives three things at once:

1. **Static power ≈ 0** — no DC path from V_DD to GND in steady state
2. **Full output swing** — the output reaches a clean V_DD or GND
3. **High noise margin** — any disturbance to the output must fight the conducting transistor

The construction rule for any Boolean function F(A, B, C, ...):

1. Build a **pull-down network of nMOS** transistors that conducts exactly when F = 1
   - AND between conditions → nMOS in **series**
   - OR between conditions → nMOS in **parallel**
2. Build a **pull-up network of pMOS** transistors that conducts exactly when F = 0 (i.e. when ¬F = 1)
   - Same series/parallel rules, applied to ¬F
3. Connect the output node between the two networks

The two networks are always **logical duals** of each other. The output of the gate is ¬F when the PDN implements F — this is why CMOS "NAND" is called NAND: the *output* is the AND inverted, even though the *PDN* implements AND.

The family covers the inverter, NAND, NOR, and arbitrary compound gates (e.g., AOI — AND-OR-Invert — and OAI — OR-AND-Invert), all built from the same series/parallel-of-switches rule. The notable exception is XOR, which is *binate* (A appears both as A and as Ā in the function) and cannot be implemented in a single complementary stage.

## Formal Definition / Statement

**Series-parallel network equivalence to Boolean expressions:**
- nMOS (or pMOS) in **series** ↔ AND of their on-conditions
- nMOS (or pMOS) in **parallel** ↔ OR of their on-conditions
- nMOS conducts when V_GS > V_TH (positive gate voltage)
- pMOS conducts when V_GS < V_TH (negative gate voltage for standard enhancement)

**Standard gates summary:**

| Gate | Transistor count | PDN | PUN | Output |
|------|-----------------|-----|-----|--------|
| Inverter (NOT) | 2 | single nMOS | single pMOS | ¬A |
| 2-input NAND | 4 | 2 nMOS series | 2 pMOS parallel | ¬(A∧B) |
| 3-input NAND | 6 | 3 nMOS series | 3 pMOS parallel | ¬(A∧B∧C) |
| 2-input NOR | 4 | 2 nMOS parallel | 2 pMOS series | ¬(A∨B) |
| AND (composite) | 6 | NAND + INV | | A∧B |
| OR (composite) | 6 | NOR + INV | | A∨B |
| AOI21 (¬(AB+C)) | 6 | (nMOS series AB) ‖ nMOS C | dual pMOS | ¬(AB+C) |
| XOR | not possible in 1 stage | | | A⊕B |
| XOR via TG | 12 | transmission-gate network | | A⊕B |
| XOR via 6T | 6 | ratioed cross-coupled | | A⊕B |

**A note on pMOS complement:** when porting a network from nMOS (PDN) to pMOS (PUN), every series connection becomes a parallel connection and vice versa, because pMOS activates on the opposite gate polarity. So the PDN of series-AB becomes the PUN of parallel-AB, and the PDN of parallel-AB becomes the PUN of series-AB. The two networks are *topological duals*.

## Key Properties / Complexity

- **Static power ≈ 0**: only switching transients draw current
- **Dynamic power per transition**: P = α · C_L · V_DD² · f (switching activity × load cap × V² × clock)
- **Propagation delay**: t_p ≈ 0.69 · R_eq · C_L (where R_eq depends on which network is conducting)
- **Full output swing** (rail-to-rail) → high noise margin
- **Ratio-less**: output level is independent of transistor sizing ratios (in contrast to pseudo-nMOS, ratioed logic, dynamic logic)
- **High input impedance**: oxide is insulating → no DC gate current
- **Universally complete**: {NAND} alone or {NOR} alone can implement any Boolean function

## Worked Example

**Build a CMOS gate for F = ¬(AB + C) (an AOI21 — AND-OR-Invert with 2 AND inputs and 1 OR input):**

The PDN conducts when F = 0, i.e. when ¬F = AB + C = 1. So the PDN is: (nMOS_A series nMOS_B) parallel with (nMOS_C). 

The PUN is the dual: (pMOS_A parallel pMOS_B) series with (pMOS_C). 

- 2 nMOS in series (for AB) + 1 nMOS in parallel with that pair (for the OR with C) = 3 nMOS
- 2 pMOS in parallel (for Ā∨B̄) + 1 pMOS in series with that pair = 3 pMOS
- Total: 6 transistors

This is a standard cell. The output is ¬(AB + C) = ¬(AB)·¬C. The "Invert" in the AOI name is the inversion inherent in static CMOS: the PDN implements AB+C, but the output is the inverse, so the gate function is ¬(AB+C).

## Common Pitfalls
- **"AND and OR can be built directly in CMOS"** → false. Static CMOS gives you NAND, NOR, NOT for free. AND/OR need an output inverter.
- **"XOR is one stage of static CMOS"** → false. XOR is the binate-function exception. Use transmission gates (12T) or a 6T ratioed design or a multi-stage NAND/NOR tree.
- **Confusing PDN function and gate function** — the PDN implements F, the output is ¬F. So a NAND gate's PDN is series nMOS (implements AND), and the output is ¬AND = NAND.
- **Series nMOS stacks are slow** — each series transistor adds on-resistance. NAND with N inputs has N series nMOS; the falling edge slows linearly.
- **Series pMOS stacks are even slower** — hole mobility is lower. NOR gates (series pMOS) have slower rising edges than NAND (series nMOS) have falling edges. This is why NAND is preferred as a primitive.

## Connections
- [[cmos-inverter]] — the 2-transistor atomic CMOS cell
- [[cmos-nand-gate]] — the workhorse 4T gate
- [[cmos-nor-gate]] — the dual of NAND
- [[cmos-xor-gate]] — the gate that breaks the rule
- [[nmos-transistor]] — the pull-down device
- [[pmos-transistor]] — the pull-up device
- [[mosfet]] — the underlying transistor
- [[mosfet-operating-regions]] — CMOS gates switch transistors between cutoff and triode; saturation is mostly avoided in digital design
- [[digital-logic]] — Boolean function implementation
- [[digital-circuit-design]] — building arithmetic, memory, control from these gates
- [[threshold-voltage]] — V_TH determines the switching threshold
- [[microelectronics-lecture-6]] — source lecture

## Open Questions
- At advanced nodes (3nm, 2nm GAA), are the transistor-count and ratio-less properties of static CMOS still worth the silicon cost, or do ratioed / dynamic logic styles return in niche roles?
- Why did NMOS-only logic (with a resistive or depletion-mode pull-up) lose out to CMOS in the 1980s? (Static power dissipation was the killer for VLSI.)
