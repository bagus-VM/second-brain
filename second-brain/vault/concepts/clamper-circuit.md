---
title: "Clamper Circuit"
tags: [concept, microelectronics, semester-1]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: ["[[diode]]", "[[depletion-region]]"]
---
## One-line Summary
A clamper (DC restorer) shifts the DC level of a signal without changing its waveform shape, using a capacitor and diode.

## Core Intuition
The capacitor charges during one part of the signal cycle and then acts as a voltage source in series with the input, effectively "clamping" the waveform to a new DC level. The diode determines the clamping direction and the reference voltage.

## Formal Definition / Statement
A clamper circuit adds or removes a DC component from an AC signal. It consists of a capacitor in series with the signal, a diode that provides a charging path, and optionally a DC bias voltage. The capacitor charges to the peak-to-peak value minus the diode drop during conduction, then maintains that DC offset on the output.

**Positive Clamper:** Clamps the positive peak to a reference (e.g., 0V). Output is shifted upward so the minimum touches 0V.
**Negative Clamper:** Clamps the negative peak to a reference. Output is shifted downward so the maximum touches 0V.

## Key Properties / Complexity
- Waveform shape is preserved; only the DC level changes
- Capacitor must be large enough that its voltage doesn't discharge significantly during non-conduction periods (RC >> T)
- With ideal diode: output shifts by exactly Vpk
- With silicon diode: output shifts by Vpk - 0.7V
- A DC bias voltage can shift the clamping level to any reference

## Worked Example
Positive clamper with a 10Vpk sinusoidal input and silicon diode (Vd = 0.7V):
- During negative half-cycle: diode conducts, capacitor charges to 10 - 0.7 = 9.3V
- During positive half-cycle: diode off, output = Vin + Vc = 10 + 9.3 = 19.3V
- Output range: +0.3V to +19.3V (positive peak clamped to ~0.3V)

## Common Pitfalls
- Forgetting the diode drop shifts the clamping level slightly.
- Assuming the capacitor is a short circuit — it only acts as a DC source after charging.
- Not realising that the output waveform is inverted relative to the input for a negative clamper.

## Connections
- Uses the same [[diode]] and [[depletion-region]] physics as rectifiers.
- Related to [[limiter-circuit]] (both reshape signals, but clampers shift DC level while limiters clip amplitude).
- Used in TV signal processing, DC restoration in oscilloscopes.

## Open Questions
- How does component non-ideality (diode reverse leakage, capacitor ESR) affect clamping accuracy?
- What happens when the input frequency changes relative to the RC time constant?
