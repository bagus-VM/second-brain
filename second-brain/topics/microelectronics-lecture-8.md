---
title: "Lecture 8: Operational Amplifiers (Inverting and Non-Inverting)"
tags: [concept, semester-1, microelectronics]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-07-08
prerequisites: [[microelectronics-lecture-7]]
---

## One-line Summary
The inverting amplifier flips the input signal and sets gain with two resistors, using the virtual short circuit principle shared with the non-inverting amplifier.

## Core Intuition
Negative feedback forces the OpAmp's two input terminals to the same voltage. This is the virtual short circuit. Once you accept that, the gain of both inverting and non-inverting amplifiers falls out of simple resistor divider analysis. The OpAmp's enormous internal gain is what makes the virtual short hold, but the closed-loop gain depends only on the external resistors.

## Formal Definition / Statement

**Inverting amplifier.** The input signal connects to the inverting (-) terminal through resistor R1. The non-inverting (+) terminal is grounded. Feedback from the output to the - terminal goes through R2.

Closed-loop gain (infinite internal gain):

Vout/Vin = -R2/R1

The negative sign indicates a 180 degree phase inversion: a positive input produces a negative output.

**Virtual short circuit.** Negative feedback forces the - terminal to approximately the same potential as the + terminal. Since the + terminal is grounded (0 V), the - terminal sits at virtual ground. This means Vin appears entirely across R1, and Vout appears entirely across R2. The current through R1 equals the current through R2 (since the OpAmp input draws no current), giving:

Vin/R1 = -Vout/R2  =>  Vout/Vin = -R2/R1

**Comparison of inverting and non-inverting amplifiers:**

| Property | Non-inverting | Inverting |
|---|---|---|
| Gain formula | 1 + R2/R1 | -R2/R1 |
| Phase | In phase (0 degrees) | Inverted (180 degrees) |
| Input impedance | High (OpAmp input impedance) | R1 |
| Gain polarity | Always positive and >= 1 | Can be any magnitude, negative |

Both amplifiers set gain through external resistor ratios, independent of the OpAmp's internal gain. Both rely on negative feedback and the virtual short circuit principle.

## Key Properties / Complexity

- Inverting amplifier gain magnitude \|Vout/Vin\| = R2/R1, set entirely by the resistor ratio
- Input impedance of the inverting amplifier equals R1 (not the OpAmp's input impedance), because the - terminal is at virtual ground
- Non-inverting amplifier input impedance is high (the OpAmp's own input impedance)
- Non-inverting gain is always >= 1; inverting gain magnitude can be less than, equal to, or greater than 1
- Both circuits require the OpAmp's internal gain to be much larger than the closed-loop gain for the virtual short approximation to hold
- The virtual short is not a physical connection. It is an approximation that holds because negative feedback drives the input difference toward zero

## Worked Example

**Inverting amplifier with R1 = 10 kOhm, R2 = 100 kOhm, Vin = 50 mV.**

Gain = -R2/R1 = -100/10 = -10.

Vout = -10 * 50 mV = -500 mV.

The output is inverted and 10x larger than the input.

Current through R1: I = Vin/R1 = 50 mV / 10 kOhm = 5 uA.
Current through R2: I = -Vout/R2 = 500 mV / 100 kOhm = 5 uA. Same current, confirming the virtual short analysis.

**Non-inverting amplifier with same resistors, Vin = 50 mV.**

Gain = 1 + R2/R1 = 1 + 10 = 11.

Vout = 11 * 50 mV = 550 mV, in phase with the input.

Same resistors, different circuit topology, different gain and phase. The inverting amplifier gives -10x. The non-inverting gives +11x.

## Common Pitfalls

- Forgetting the negative sign in the inverting amplifier gain. The 180 degree phase inversion is the defining feature.
- Confusing the input impedance. The inverting amplifier's input impedance is R1, not the OpAmp's high input impedance. This is because the - terminal sits at virtual ground.
- Thinking the virtual short means the two terminals are physically connected. They are not. The OpAmp output adjusts to make them nearly equal in voltage.
- Using R2/R1 for the non-inverting gain instead of 1 + R2/R1. The extra "1" comes from the direct path from input to output.
- Assuming both amplifiers have the same input impedance. They do not. This is a common exam question.

## Connections

[[microelectronics-lecture-7]] - This lecture extends the non-inverting OpAmp configuration from Lecture 7 to the inverting configuration and compares them.
[[analog-amplifier]] - OpAmps are the practical realization of analog voltage amplifiers with external gain control.
[[common-source-amplifier]] - The common-source stage provides the internal voltage gain that makes the virtual short approximation valid.
[[mosfet]] - CMOS OpAmps are built from MOSFETs, and the ideal input impedance assumption relies on MOSFET gate insulation.

## Open Questions

- What happens when the OpAmp's internal gain is not large enough for the virtual short approximation? How much error does this introduce?
- How does frequency affect the virtual short assumption? At high frequencies the OpAmp gain drops, so the approximation must break down.
- How do you choose between inverting and non-inverting topologies in practice beyond input impedance considerations?
