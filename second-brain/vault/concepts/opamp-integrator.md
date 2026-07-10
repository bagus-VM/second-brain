---
title: "OpAmp Integrator"
tags: [concept, microelectronics, semester-1]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-07-10
prerequisites: ["[[microelectronics-lecture-8]]", "[[capacitor]]", "[[analog-amplifier]]"]
---

## One-line Summary
*Replace the feedback resistor with a capacitor, and the OpAmp outputs the integral of the input signal.*

## Core Intuition
An inverting amplifier's gain is -Z2/Z1. If Z2 is a capacitor (impedance 1/jωC) and Z1 is a resistor (impedance R), the gain becomes -1/(jωRC). In the time domain, this means the output is proportional to the integral of the input. The capacitor accumulates charge over time — longer time = more accumulated charge = more output voltage. Low-frequency signals (slow changes) accumulate more, high-frequency signals (fast oscillations) cancel out. This is why the integrator is a low-pass filter.

## Formal Definition / Statement

**Circuit:** Inverting amplifier configuration with:
- Z1 = R (input resistor)
- Z2 = C (feedback capacitor)

**Frequency domain:**
Gain = -Z2/Z1 = -1/(jωRC)

**Time domain:**
Vout(t) = -(1/RC) ∫₀ᵗ Vin(τ) dτ + Vout(0)

The output is the negative scaled integral of the input, plus an initial condition Vout(0).

**For a constant input Vin = V:**
Vout(t) = -(V/RC) · t — a linear ramp (the integral of a constant is a linear function).

## Key Properties

- Low-pass behavior: gain magnitude |1/(ωRC)| decreases with frequency
- At DC (ω=0), gain is infinite (capacitor is open circuit → no feedback → OpAmp saturates)
- Practical fix: add a large resistor Rf in parallel with C to limit DC gain to -Rf/R
- The output is 90° phase-shifted from the input (integration adds -90°)
- Used in analog computers, waveform generation (triangle from square wave), PID controllers
- The capacitor voltage cannot change instantaneously → smooths sharp transitions

## Worked Example

Integrator with R = 10 kΩ, C = 1 μF, Vin = 1 V (constant step input):

RC = 10×10³ × 1×10⁻⁶ = 0.01 s

Vout(t) = -(1/0.01) · 1 · t = -100t V/s

After 1 ms: Vout = -100 × 0.001 = -0.1 V
After 10 ms: Vout = -100 × 0.01 = -1.0 V
After 50 ms: Vout = -5.0 V (OpAmp saturates at -Vsupply)

The output ramps down linearly until it hits the negative supply rail.

## Common Pitfalls

- **Forgetting DC saturation.** Without a parallel resistor, any DC offset in the input causes the output to ramp to infinity (in practice, to the supply rail). Always add Rf for practical circuits.
- **Confusing the sign.** The inverting integrator outputs the *negative* integral. A positive input produces a negative-going ramp.
- **Ignoring initial conditions.** Vout(0) is set by the capacitor's initial charge. In a real circuit, you may need to reset the capacitor before each integration.
- **Thinking the capacitor is a short at high frequencies.** It is — and that's why high frequencies are attenuated (low gain). The integrator naturally filters out high-frequency noise.

## Connections

- [[opamp-differentiator]] — the dual circuit: swap R and C positions
- [[microelectronics-lecture-8]] — inverting amplifier topology is the foundation
- [[microelectronics-lecture-9]] — lecture that introduces integrators and differentiators
- [[capacitor]] — the component that makes integration possible (charge accumulation)
- [[analog-amplifier]] — integrator is a frequency-dependent amplifier
- [[negative-feedback]] — the feedback mechanism that makes the circuit stable

## Open Questions

- How does the integrator behave with a non-ideal OpAmp (finite bandwidth, input bias current)?
- What is the effect of capacitor leakage resistance on long-term integration accuracy?
- How do you build a practical integrator that doesn't require manual capacitor reset?
