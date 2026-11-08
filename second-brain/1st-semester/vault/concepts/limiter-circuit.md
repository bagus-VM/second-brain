---
title: "Limiter Circuit"
tags: [concept, microelectronics, semester-1]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: ["[[diode]]", "[[zener-diode]]"]
---
## One-line Summary
A limiter clips the voltage waveform at a specified threshold, preventing it from exceeding a maximum or dropping below a minimum value.

## Core Intuition
When the input voltage exceeds a threshold (set by diode forward voltage or Zener breakdown voltage), the diode conducts and clamps the output, preventing further voltage rise. Below the threshold, the diode is off and the output follows the input.

## Formal Definition / Statement
A limiter (clipper) circuit uses diodes to remove portions of a signal that exceed specified voltage levels.

**Series Limiter:** Diode is in series with the load. When reverse-biased, the signal is blocked entirely beyond the threshold.
**Parallel (Shunt) Limiter:** Diode is in parallel with the output. When forward-biased, it shorts the signal to ground (or to a reference) above the threshold.
**Dual-Diode (Double-Ended) Limiter:** Two diodes clip both positive and negative peaks, producing a waveform bounded between two thresholds.
**Zener Limiter:** Uses a Zener diode's breakdown voltage as the clipping threshold. Back-to-back Zeners clip at ±(Vz + 0.7V).

## Key Properties / Complexity
- Series limiters block voltage beyond the threshold; parallel limiters shunt excess voltage
- Silicon diode forward drop ≈ 0.7V sets the simplest clipping level
- Zener diodes allow precise clipping at any voltage (Vz)
- Back-to-back Zeners provide symmetrical clipping at ±(Vz + 0.7V)
- Output waveform shape changes — distortion is the trade-off for voltage protection

## Worked Example
Dual-diode limiter with Vref1 = +5V and Vref2 = -5V (ideal diodes):
- Input: 10Vpk sinusoid
- For Vin > +5V: upper diode conducts, output clamped to +5V
- For Vin < -5V: lower diode conducts, output clamped to -5V
- For -5V < Vin < +5V: both diodes off, output = input
- Result: sinusoid with flat tops at ±5V

Zener limiter with Vz = 6.8V back-to-back Zeners:
- Clips at ±(6.8 + 0.7) = ±7.5V

## Common Pitfalls
- Forgetting the diode's forward voltage drop in the clipping level calculation.
- Confusing series and parallel limiter topologies — they behave differently.
- Not accounting for both Zener and forward-biased drops in back-to-back Zener limiters.

## Connections
- Shares [[diode]] physics with [[bridge-rectifier]] and [[clamper-circuit]].
- [[zener-diode]] breakdown voltage determines Zener limiter thresholds.
- Used in signal conditioning and voltage protection circuits.
- Related to voltage regulators (regulators maintain output; limiters just clip).

## Open Questions
- How do you design a limiter for asymmetric clipping levels with a single diode branch?
- What is the frequency response limitation of a limiter at very high frequencies?
