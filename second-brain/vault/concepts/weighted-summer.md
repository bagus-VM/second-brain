---
title: "Weighted Summer (Voltage Adder)"
tags: [concept, microelectronics, semester-1]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-07-10
prerequisites: ["[[microelectronics-lecture-8]]", "[[analog-amplifier]]"]
---

## One-line Summary
*Multiple input signals, each with its own resistor, are summed by the OpAmp into a single output.*

## Core Intuition
The inverting amplifier's virtual ground means each input resistor sees the input voltage across it independently. The currents from all inputs add up at the inverting terminal, and the feedback resistor converts this total current back to a voltage. Each input contributes proportionally to 1/Ri — a smaller resistor means more current, more weight. This is analog addition with adjustable weights, and it works because the virtual ground prevents the inputs from interfering with each other.

## Formal Definition / Statement

**Circuit:** Inverting amplifier with n input resistors R1, R2, ..., Rn connected to the inverting terminal. Single feedback resistor Rf.

**Output:**
Vout = -Rf × (V1/R1 + V2/R2 + ... + Vn/Rn)

Each input Vi is weighted by the ratio Rf/Ri.

**Special cases:**
- All resistors equal (R1 = R2 = ... = Rn = R): Vout = -(Rf/R) × (V1 + V2 + ... + Vn)
- Rf = R: Vout = -(V1 + V2 + ... + Vn) — pure summation (inverted)
- Different Rf/Ri ratios: each input has a different weight

## Key Properties

- Each input is independent (virtual ground isolates inputs from each other)
- The output is inverted (negative sum)
- To get a non-inverted sum, follow with an inverting amplifier (gain = -1)
- Weights are set by resistor ratios — precise and stable
- Used in audio mixing (each channel has its own volume control via Ri)
- Used in DAC circuits (binary-weighted resistors: R, 2R, 4R, 8R, ...)
- Input impedance for each channel is Ri

## Worked Example

Three inputs: V1 = 1 V, V2 = 2 V, V3 = 3 V
Resistors: R1 = 10 kΩ, R2 = 20 kΩ, R3 = 30 kΩ, Rf = 60 kΩ

Vout = -60k × (1/10k + 2/20k + 3/30k)
     = -60k × (0.0001 + 0.0001 + 0.0001)
     = -60k × 0.0003
     = -18 V → saturates at -Vsupply

With Rf = 10 kΩ:
Vout = -10k × (1/10k + 2/20k + 3/30k)
     = -10k × (0.0001 + 0.0001 + 0.0001)
     = -10k × 0.0003
     = -3 V

Equal-weight case (all R = 10 kΩ, Rf = 10 kΩ):
Vout = -(1 + 2 + 3) = -6 V

## Common Pitfalls

- **Forgetting the inversion.** The output is always negative (for positive inputs). If you need a positive sum, add an inverting stage with gain = -1.
- **Assuming inputs are isolated.** They are — at the virtual ground. But if the OpAmp saturates, the virtual ground breaks and inputs can couple.
- **Not considering input impedance.** Each input channel sees Ri to virtual ground. If the source has non-negligible output impedance, the effective weight changes.
- **Ignoring the current summing node.** All input currents meet at the inverting terminal. The OpAmp must source/sink the total current through Rf.

## Connections

- [[voltage-follower]] — used after a weighted summer to buffer the output
- [[microelectronics-lecture-8]] — inverting amplifier is the building block
- [[microelectronics-lecture-9]] — lecture that introduces weighted summers
- [[analog-amplifier]] — weighted summer is a multi-input amplifier
- [[negative-feedback]] — virtual ground enables independent input weighting

## Open Questions

- How does component tolerance (resistor precision) affect the accuracy of the weights?
- Can you build a weighted summer with non-inverting topology? What are the trade-offs?
- How does the weighted summer relate to the R-2R ladder DAC?
