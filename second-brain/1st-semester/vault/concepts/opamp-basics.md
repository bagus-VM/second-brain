---
title: "Op-Amp Basics"
tags: [concept, microelectronics, semester-1, introduction-to-microelectronics]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-07-20
prerequisites: [cmos-inverter]
---

## One-line Summary
*An operational amplifier is a high-gain differential amplifier that, combined with negative feedback, performs precise analogue operations on voltages.*

## Core Intuition
An op-amp is the analogue equivalent of a universal building block. Just as NAND gates can build any digital circuit, op-amps with resistors (and capacitors) can build any linear analogue function: amplification, filtering, integration, differentiation, summation, and comparison.

The key insight: the op-amp itself is "dumb" — it just multiplies the voltage difference between its two inputs by a huge number. The *feedback network* (resistors, capacitors) determines what mathematical operation the circuit performs. The op-amp is the muscle; the feedback network is the brain.

## Formal Definition / Statement
An ideal op-amp has:
- **Infinite open-loop gain** (A → ∞)
- **Infinite input impedance** (no current flows into inputs: I+ = I− = 0)
- **Zero output impedance** (can drive any load)
- **Infinite bandwidth** (gain constant at all frequencies)

Practical CMOS op-amps achieve:
- Open-loop gain: 10^4 to 10^6 (80–120 dB)
- Input impedance: 10^12 Ω (MOSFET gate)
- Output impedance: 10–100 Ω
- Gain-bandwidth product: 1–100 MHz

**Two golden rules (with negative feedback):**
1. No current flows into the inputs (I+ = I− = 0)
2. The op-amp output adjusts to force V+ = V− (virtual short)

## Key Properties / Complexity
- **Differential input:** Vout = A × (V+ − V−), where A is open-loop gain
- **Supply rails:** Output cannot exceed VDD or go below VSS (typically within ~100mV of rails for rail-to-rail designs)
- **Slew rate:** Maximum rate of output voltage change, limited by internal bias current and compensation capacitor (typically 0.1–100 V/μs)
- **CMRR:** Common-mode rejection ratio — how well the op-amp rejects signals common to both inputs (typically 80–120 dB)
- **Offset voltage:** Input-referred voltage that must be applied to make output zero (typically 0.1–10 mV)

## Worked Example
**Non-inverting amplifier:**

Given: R1 = 1kΩ (from V− to ground), R2 = 9kΩ (from V− to Vout)

Using golden rule 1: no current into V−, so R1 and R2 form a voltage divider:
- V− = Vout × R1/(R1+R2) = Vout × 0.1

Using golden rule 2: V+ = V−, so Vin = Vout × 0.1
- Gain = Vout/Vin = 10

The gain is set entirely by resistor ratios, not by the op-amp's internal parameters.

## Common Pitfalls
- **Forgetting the power supply:** Op-amps need supply voltages. The output cannot exceed them. A ±15V supply gives max ±15V output (less for non-rail-to-rail)
- **Confusing open-loop with closed-loop gain:** Open-loop gain (A) is the op-amp alone. Closed-loop gain (with feedback) is what you design and use
- **Treating inputs as symmetric in inverting config:** The inverting input gets the signal through a resistor, the non-inverting input is grounded. Both golden rules still apply
- **Ignoring frequency response:** At DC and low frequencies, the ideal model works. At higher frequencies, the gain rolls off (typically −20 dB/decade) and phase shifts, which can cause oscillation

## Connections
- [[negative-feedback]] — the mechanism that makes op-amp circuits predictable and useful
- [[opamp-integrator]] — capacitor in feedback path, integrates input voltage over time
- [[opamp-differentiator]] — capacitor at input, differentiates input voltage
- [[weighted-summer]] — multiple input resistors to one summing junction
- [[voltage-follower]] — unity-gain buffer, simplest op-amp circuit
- [[common-source-amplifier]] — CMOS implementation of differential amplifier stage
- [[mosfet]] — the transistors inside the CMOS op-amp
- [[negative-feedback]] — without it, the op-amp is just a comparator

## Open Questions
- How does the internal frequency compensation (Miller compensation) affect the slew rate?
- What are the trade-offs between bipolar and CMOS op-amp input stages?
