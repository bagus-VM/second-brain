---
title: "Bridge Rectifier"
tags: [concept, microelectronics, semester-1]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: ["[[diode]]", "[[full-wave-rectifier]]"]
---
## One-line Summary
A full-wave rectifier using four diodes in a bridge configuration that eliminates the need for a center-tap transformer.

## Core Intuition
During each half-cycle of the AC input, two diodes conduct and two block, routing current through the load in the same direction regardless of input polarity. The output sees both halves of the AC waveform, doubling the effective frequency and reducing ripple compared to a half-wave rectifier.

## Formal Definition / Statement
A bridge rectifier consists of four diodes arranged in a diamond (bridge) configuration. The AC source connects to two opposite nodes, and the load connects to the remaining two nodes. During the positive half-cycle, diodes D1 and D2 conduct while D3 and D4 are reverse-biased. During the negative half-cycle, D3 and D4 conduct while D1 and D2 are reverse-biased. The result is unidirectional current through the load for both half-cycles.

## Key Properties / Complexity
- Full-wave rectification without a center-tap transformer
- PIV (Peak Inverse Voltage) per diode = Vpk - 2Vd (two diode drops in the conduction path)
- Output frequency = 2 × input frequency
- Two diodes always in series with the load, so output voltage is Vpk - 2Vd (vs Vpk - Vd for center-tap)
- Higher transformer utilization factor than half-wave
- Smoother output requires smaller filter capacitor

## Worked Example
Given a 120Vrms AC source with a bridge rectifier (silicon diodes, Vd = 0.7V):
- Vpk = 120 × √2 ≈ 169.7V
- Vout(peak) = 169.7 - 2(0.7) = 168.3V
- PIV per diode = 169.7 - 0.7 = 169V
- Output frequency = 120Hz (if input is 60Hz)

## Common Pitfalls
- Forgetting that TWO diode drops appear in the conduction path (not one), reducing output voltage more than center-tap configurations.
- Confusing PIV with the peak output voltage — PIV is across each reverse-biased diode.
- Assuming the bridge rectifier eliminates ripple — it still needs a filter capacitor for smooth DC.

## Connections
- Requires understanding of [[diode]] forward and reverse behavior.
- Compared with [[full-wave-rectifier]] using center-tap transformer.
- Output often fed into voltage regulator circuits.
- Building block of [[power-supply]] design.

## Open Questions
- How does the bridge rectifier behave with non-ideal diodes (dynamic resistance, reverse leakage)?
- What are the thermal considerations for the diodes at high current levels?
