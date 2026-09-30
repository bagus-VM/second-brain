---
title: "Rectifier"
tags: [concept, microelectronics, semester-1]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: ["[[diode]]"]
---

## One-line Summary
A rectifier is a circuit that converts alternating current (AC) to direct current (DC) using diodes to allow current flow in only one direction.

## Core Intuition
AC power alternates direction 50-60 times per second, but most electronic devices need steady DC. A rectifier uses [[diode]]s as one-way valves to "clip off" one or both halves of the AC waveform, producing pulsating DC that can be smoothed with capacitors.

## Formal Definition / Statement
A rectifier is an electrical circuit that converts AC (alternating current) to DC (direct current) using one or more [[diode]]s. The diodes act as unidirectional switches, passing current during one polarity and blocking it during the other. Types include [[half-wave-rectifier]], [[full-wave-rectifier]], and [[bridge-rectifier]].

## Key Properties / Complexity
- Uses [[diode]] forward voltage drop (~0.7V for Si)
- Output is pulsating DC (not smooth)
- Requires filtering (capacitor) for smooth DC output
- Efficiency increases from half-wave to full-wave to bridge rectifier
- Ripple frequency: half-wave = f, full-wave/bridge = 2f

## Worked Example
120V AC (60Hz) → Bridge [[bridge-rectifier]] → Pulsating DC → Capacitor filter → ~165V DC (peak) with ripple

## Common Pitfalls
- Assuming rectifier output is smooth DC — it's pulsating and needs filtering
- Forgetting the diode voltage drop reduces peak output voltage

## Connections
- [[diode]] — the active component in rectifiers
- [[half-wave-rectifier]] — simplest type, one diode
- [[full-wave-rectifier]] — uses both halves of AC
- [[bridge-rectifier]] — four diodes, most common
- [[clamper-circuit]] — related signal processing circuit
- [[limiter-circuit]] — related signal processing circuit

## Open Questions
- How does bridge rectifier efficiency compare to active rectification using MOSFETs?
