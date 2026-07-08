---
title: "Lecture 8 - Operational Amplifiers: Inverting and Non-Inverting"
tags: [lecture, microelectronics, semester-1]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-07-08
prerequisites: [[microelectronics-lecture-7]], [[mosfet]], [[cmos-inverter]]
---

## One-line Summary
*Two OpAmp circuits (inverting and non-inverting) set their gain using external resistors, thanks to negative feedback.*

## Core Intuition
An OpAmp has enormous open-loop gain, far more than you usually want. Negative feedback tames that gain: you feed part of the output back to the inverting input, and the OpAmp drives its output to whatever voltage makes the two inputs equal. The gain then depends on the resistor ratio in your feedback network, not on the OpAmp's internal gain. This is why OpAmp circuits are predictable and stable.

## Formal Definition / Statement

### Inverting Amplifier

Input applied through resistor R1 to the - (inverting) terminal. The + (non-inverting) terminal is grounded. Feedback from output to the - terminal through resistor R2.

Gain: Vout/Vin = -R2/R1

The negative sign means 180 degree phase shift: a positive input produces a negative output.

**Virtual short circuit principle:** Negative feedback forces the - terminal to approximately the same potential as the + terminal. Since the + terminal is grounded (0 V), the - terminal sits at virtual ground. The input voltage Vin appears across R1, and the output voltage Vout appears across R2. The same current flows through both resistors, giving Vout/Vin = -R2/R1.

Input impedance = R1 (the input signal sees R1 to virtual ground).

### Non-Inverting Amplifier

Input applied to the + terminal. Feedback from output to - terminal through voltage divider R2, R1. R1 connects from - terminal to ground.

Gain: Vout/Vin = 1 + R2/R1

No phase inversion. Input impedance is very high (ideally infinite), since the input connects directly to the OpAmp's high-impedance + terminal.

### Comparison

| Property | Non-inverting | Inverting |
|---|---|---|
| Gain formula | 1 + R2/R1 | -R2/R1 |
| Phase | 0 degrees (no inversion) | 180 degrees (inverted) |
| Input impedance | Very high (ideal: infinite) | R1 |
| Minimum gain | 1 (unity buffer when R2=0) | Any magnitude, including < 1 |

Both circuits:
- Set gain entirely by external resistor ratio R2/R1
- Are independent of the OpAmp's internal open-loop gain (as long as it is large enough)
- Rely on negative feedback and the virtual short circuit principle

## Key Properties

- Inverting amplifier gain: -R2/R1 (magnitude set by resistor ratio, sign is negative)
- Non-inverting amplifier gain: 1 + R2/R1 (always >= 1)
- Both gains are independent of OpAmp internal gain (due to negative feedback)
- Virtual short circuit: the - terminal tracks the + terminal due to feedback
- Inverting amplifier input impedance: R1 (lower than non-inverting)
- Non-inverting amplifier input impedance: very high (set by OpAmp input impedance)

## Worked Example

Inverting amplifier with R1 = 2 kOhm, R2 = 10 kOhm:

Gain = -R2/R1 = -10000/2000 = -5

If Vin = 0.2 V, then Vout = -1.0 V.

The input signal is amplified by 5 and inverted.

Non-inverting amplifier with the same resistor values:

Gain = 1 + R2/R1 = 1 + 5 = 6

If Vin = 0.2 V, then Vout = 1.2 V.

Same resistors, different gain, because the non-inverting topology adds 1.

## Common Pitfalls

- The inverting amplifier has a negative sign. Students forget the sign and report a positive gain. The sign matters: it means 180 degree phase shift.
- The inverting amplifier's input impedance is R1, not infinity. This is a key difference from the non-inverting configuration and matters when the signal source has non-negligible output impedance.
- Virtual ground is not real ground. The - terminal of the inverting amplifier sits at approximately 0 V, but it cannot sink or source current to ground. All current through R1 flows through R2 to the output.
- The non-inverting amplifier cannot have gain < 1 (minimum is 1). If you need attenuation, use the inverting configuration with R2 < R1.
- The gain formulas assume the OpAmp has enough open-loop gain. With finite open-loop gain A, the closed-loop gain deviates slightly from the ideal formula.

## Connections

- [[microelectronics-lecture-7]] - Previous lecture introduced OpAmp basics, ideal properties, and the non-inverting amplifier. This lecture adds the inverting configuration.
- [[common-source-amplifier]] - The inverting amplifier's 180 degree phase shift is analogous to the common-source amplifier's inversion.
- [[analog-amplifier]] - General amplifier concepts: gain, input/output impedance, bandwidth.
- [[cmos-inverter]] - The inverting amplifier inverts, just as the CMOS inverter inverts its input.
- [[mosfet]] - OpAmps are built from MOSFETs (or BJTs), biased in their active region.

## Open Questions

- How does the bandwidth of the inverting vs non-inverting amplifier compare for the same gain magnitude? Does the feedback network affect bandwidth differently?
- What happens to the virtual short circuit assumption when the OpAmp approaches its slew rate limit or saturation?
