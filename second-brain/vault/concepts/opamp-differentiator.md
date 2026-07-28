---
title: "OpAmp Differentiator"
tags: [concept, microelectronics, semester-1]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-07-10
prerequisites: ["[[microelectronics-lecture-8]]", "[[capacitor]]", "[[analog-amplifier]]"]
---

## One-line Summary
*Replace the input resistor with a capacitor, and the OpAmp outputs the derivative of the input signal.*

## Core Intuition
The differentiator is the dual of the integrator. Instead of accumulating charge over time (integration), the capacitor responds to *changes* in voltage. A rapid change in input voltage causes a large current through the capacitor (I = C dV/dt), which the feedback resistor converts to an output voltage. A constant input produces zero output — no change, no current, no output. This makes the differentiator a high-pass filter: it passes fast changes and blocks slow ones.

## Formal Definition / Statement

**Circuit:** Inverting amplifier configuration with:
- Z1 = C (input capacitor)
- Z2 = R (feedback resistor)

**Frequency domain:**
Gain = -Z2/Z1 = -jωRC

**Time domain:**
Vout(t) = -RC · dVin(t)/dt

The output is the negative scaled derivative of the input.

**For a linear ramp input Vin = kt:**
Vout = -RC · k — a constant output proportional to the ramp rate.

## Key Properties / Complexity

- High-pass behaviour: gain magnitude |ωRC| increases with frequency
- At DC (ω=0), gain is zero (capacitor blocks DC → no output)
- At very high frequencies, gain is very large → noise amplification
- Practical fix: add a small resistor Rs in series with C to limit high-frequency gain to -R/Rs
- The output is 90° phase-shifted from the input (differentiation adds +90°)
- Used in edge detection, rate-of-change sensing, control systems

## Worked Example

Differentiator with R = 10 kΩ, C = 1 μF, input is a triangle wave: Vin ramps from 0 to 5 V in 1 ms, then back to 0 V in 1 ms.

RC = 10×10³ × 1×10⁻⁶ = 0.01 s

During rising ramp (dV/dt = 5/0.001 = 5000 V/s):
Vout = -0.01 × 5000 = -50 V → saturates at -Vsupply

During falling ramp (dV/dt = -5000 V/s):
Vout = -0.01 × (-5000) = +50 V → saturates at +Vsupply

In practice, the output would be clipped at the supply rails, producing a square wave. This shows why the differentiator needs gain limiting (add Rs in series with C) for practical signals.

## Common Pitfalls

- **Noise amplification.** The differentiator amplifies high-frequency noise aggressively. Always add a series resistor to limit gain.
- **Confusing the sign.** The inverting differentiator outputs the *negative* derivative. A positive slope produces a negative output.
- **Thinking it works at DC.** The capacitor blocks DC, so the differentiator has zero gain at DC. It only responds to changes.
- **Instability.** The differentiator is more prone to oscillation than the integrator because high-frequency gain increases without limit. The series resistor is not optional in practice.

## Connections

- [[opamp-integrator]] — the dual circuit: swap R and C positions
- [[microelectronics-lecture-8]] — inverting amplifier topology is the foundation
- [[microelectronics-lecture-9]] — lecture that introduces integrators and differentiators
- [[capacitor]] — the component that makes differentiation possible (I = C dV/dt)
- [[analog-amplifier]] — differentiator is a frequency-dependent amplifier
- [[negative-feedback]] — the feedback mechanism that makes the circuit stable

## Open Questions

- How does the series resistor Rs affect the frequency response? What is the new cutoff frequency?
- Can you build a practical differentiator without the noise problem using active filtering?
- How do real-world capacitor non-idealities (ESR, dielectric absorption) affect differentiation accuracy?
