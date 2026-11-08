---
title: "Full-Wave Rectifier"
tags: [concept, microelectronics, semester-1]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: ["[[rectifier]]", "[[diode]]"]
---

## One-line Summary
A full-wave rectifier uses two or four diodes to pass both halves of the AC waveform, producing pulsating DC with no gaps — more efficient than half-wave.

## Core Intuition
Instead of wasting the negative half-cycle like a [[half-wave-rectifier]], a full-wave rectifier flips it to positive. Two common implementations: centre-tapped transformer with 2 diodes, or [[bridge-rectifier]] with 4 diodes. The result: twice as many pulses per cycle, smoother output, and higher efficiency.

## Formal Definition / Statement
A full-wave rectifier is a [[rectifier]] circuit that converts both halves of the AC input waveform to DC output. Two configurations:

1. **Centre-tapped transformer:** 2 diodes + centre-tapped transformer
2. **Bridge configuration:** 4 diodes ([[bridge-rectifier]])

**Output characteristics:**
- Peak output voltage: Vpeak = Vm - 2Vd (bridge) or Vm - Vd (centre-tap)
- Average (DC) output voltage: Vdc = 2Vm/π ≈ 0.636 Vm
- RMS output voltage: Vrms = Vm/√2
- Ripple frequency: 2f (twice input frequency)
- Rectification efficiency: η ≈ 81.2%
- Form factor: FF ≈ 1.11

## Key Properties / Complexity
- Uses both halves of AC waveform
- Higher efficiency than half-wave (~81.2% vs ~40.6%)
- Ripple frequency is 2× input frequency (easier to filter)
- Bridge configuration doesn't need centre-tapped transformer

## Worked Example
Input: 10V peak AC at 60Hz, bridge rectifier:
- Vpeak(out) = 10 - 2(0.7) = 8.6V
- Vdc = 2 × 8.6/π ≈ 5.48V
- Ripple frequency: 120Hz

## Common Pitfalls
- Forgetting the two diode drops in bridge configuration (2 × 0.7V)
- Confusing centre-tap and bridge configurations

## Connections
- [[rectifier]] — parent concept
- [[half-wave-rectifier]] — simpler but less efficient
- [[bridge-rectifier]] — most common full-wave implementation
- [[diode]] — active components

## Open Questions
- How does the choice between centre-tap and bridge affect cost and efficiency?
