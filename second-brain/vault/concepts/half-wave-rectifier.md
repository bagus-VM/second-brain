---
title: "Half-Wave Rectifier"
tags: [concept, microelectronics, semester-1]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: ["[[rectifier]]", "[[diode]]"]
---

## One-line Summary
A half-wave rectifier uses a single diode to pass only one half of the AC waveform, producing pulsating DC with large gaps between pulses.

## Core Intuition
The simplest [[rectifier]] — a single [[diode]] acts as a one-way gate. During the positive half-cycle, current flows through the diode to the load. During the negative half-cycle, the diode blocks current. Result: only positive half-cycles appear at the output, with gaps where negative cycles were blocked.

## Formal Definition / Statement
A half-wave rectifier is a [[rectifier]] circuit using a single [[diode]] that passes only one half (positive or negative) of the AC input waveform.

**Output characteristics:**
- Peak output voltage: Vpeak = Vm - Vd (where Vd ≈ 0.7V for Si)
- Average (DC) output voltage: Vdc = Vm/π ≈ 0.318 Vm
- RMS output voltage: Vrms = Vm/2
- Ripple frequency: equal to input frequency f
- Rectification efficiency: η = Pdc/Pac ≈ 40.6%
- Form factor: FF = Vrms/Vdc ≈ 1.57

## Key Properties / Complexity
- Simplest rectifier design (one diode)
- Low efficiency (~40.6%)
- Large ripple component
- Ripple frequency equals input frequency (f)
- Requires large filter capacitor for smooth DC

## Worked Example
Input: 10V peak AC at 60Hz
- Vpeak(out) = 10 - 0.7 = 9.3V
- Vdc = 9.3/π ≈ 2.96V
- Vrms = 9.3/2 = 4.65V
- Output has 60Hz ripple

## Common Pitfalls
- Confusing half-wave with full-wave rectifier output — half-wave has gaps
- Forgetting the diode voltage drop in calculations

## Connections
- [[rectifier]] — parent concept
- [[diode]] — the single active component
- [[full-wave-rectifier]] — more efficient alternative
- [[bridge-rectifier]] — most common full-wave implementation

## Open Questions
- When is half-wave rectification preferred over full-wave despite lower efficiency?
