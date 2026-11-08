---
title: "Negative Feedback"
tags: [concept, microelectronics, semester-1, introduction-to-microelectronics]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-07-20
prerequisites: [opamp-integrator, opamp-differentiator, weighted-summer, voltage-follower]
---

## One-line Summary
*Negative feedback takes a portion of the output signal and feeds it back to the input in opposite phase, stabilising gain and linearising the amplifier.*

## Core Intuition
Without feedback, an op-amp's open-loop gain is enormous (~10^5 to 10^6) and unpredictable — it varies with temperature, frequency, and component tolerances. Negative feedback sacrifices raw gain to achieve something far more valuable: predictable, stable behaviour determined almost entirely by passive components (resistors, capacitors) rather than the op-amp's internal parameters.

Think of it like a thermostat: the output (room temperature) is constantly compared to the desired setpoint, and the error signal drives the system toward that setpoint. Negative feedback does the same for voltage.

## Formal Definition / Statement
A feedback network is **negative** when the fed-back signal is 180° out of phase with the input at the summing junction. For an op-amp with open-loop gain A and feedback fraction β:

$$V_{out} = \frac{A}{1 + A\beta} \cdot V_{in}$$

When Aβ >> 1 (deep feedback):

$$V_{out} \approx \frac{1}{\beta} \cdot V_{in}$$

This is the **virtual short** condition: the differential input voltage (V+ − V−) ≈ 0.

## Key Properties / Complexity
- **Gain stability:** Closed-loop gain depends only on 1/β (resistor ratio), not on A
- **Bandwidth extension:** Gain-bandwidth product is constant; reducing gain extends bandwidth by the same factor
- **Distortion reduction:** Nonlinear distortion is reduced by factor (1 + Aβ)
- **Input/output impedance:** Series feedback increases input impedance; shunt feedback decreases it
- **Stability condition:** Loop gain Aβ must remain positive at the frequency where |Aβ| = 1 (Barkhausen criterion for oscillation avoidance)

## Worked Example
**Non-inverting amplifier with R1 = 1kΩ, R2 = 9kΩ:**

The feedback fraction β = R1/(R1+R2) = 1k/10k = 0.1

Closed-loop gain = 1/β = 10 (20 dB)

If the op-amp's open-loop gain varies from 100,000 to 50,000 (50% drop), the closed-loop gain changes from:
- 100000/(1+10000) = 9.9990 → 50000/(1+5000) = 9.9980

That's a 0.01% change vs the 50% change in open-loop gain. This is the power of negative feedback.

## Common Pitfalls
- **Phase margin:** At high frequencies, the op-amp's internal poles cause phase shift. If the total phase shift reaches 360° (same as 0°) at the unity-gain frequency, negative feedback becomes positive → oscillation
- **Confusing inverting vs non-inverting:** Both use negative feedback, but the signal enters different input terminals. The inverting configuration has V+ = 0 (virtual ground), while the non-inverting has V+ = Vin
- **Assuming virtual short always holds:** It requires (1) high open-loop gain, (2) negative feedback present, (3) not saturated. If the output is clipped at the supply rail, the virtual short breaks

## Connections
- [[opamp-integrator]] — capacitor in feedback path creates frequency-dependent negative feedback
- [[opamp-differentiator]] — capacitor at input with resistive feedback
- [[weighted-summer]] — multiple inputs share one feedback resistor; superposition + negative feedback
- [[voltage-follower]] — unity gain (β = 1) is the extreme case of negative feedback
- [[common-source-amplifier]] — negative feedback via source degeneration in MOSFETs
- [[opamp-basics]] — the foundation for understanding why negative feedback works

## Open Questions
- How does the Barkhausen stability criterion relate to the phase margin specification in op-amp datasheets?
- What happens to the virtual short approximation when the op-amp is current-limited?
