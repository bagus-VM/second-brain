---
title: "Fault Tree"
tags: [concept, iot-security, semester-1]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: ["[[threat-modeling]]"]
---

## One-line Summary
A fault tree is a structured diagram modelling how system failures can lead to a hazardous state — used for safety analysis in IoT systems where security failures can cause physical harm.

## Core Intuition
While attack trees ask "how could an attacker succeed?", fault trees ask "how could the system fail?" In IoT, these overlap: a security breach can cause a system failure that leads to a hazard (e.g., a hacked medical device causing patient harm).

## Formal Definition / Statement
**Fault Tree:** A structured diagram modeling how system failures can lead to a hazardous state. Used as part of hazard analysis in the Safety required property of IoT development.

- **Root node:** The hazardous state (top-level undesired event)
- **Intermediate nodes:** System failure modes
- **Leaf nodes:** Root causes (component failures, human errors, environmental factors)
- **AND/OR gates:** Whether all failures must coincide (AND) or any single failure suffices (OR)

## Key Properties / Complexity

### Structure
- Top-down decomposition from hazard to root causes
- OR gates: any single failure can contribute to the hazard
- AND gates: multiple simultaneous failures required
- Quantitative analysis: assign failure probabilities to leaves, compute hazard probability

### Use in IoT Safety
- Required for **Design for Safety** in IoT
- Paired with [[attack-tree|attack trees]] for comprehensive analysis
- Informs hardware protection measures (anti-tamper, redundancy)
- Critical for IoT in healthcare, automotive, industrial control

### Relationship to Attack Trees
| Aspect | Attack Tree | Fault Tree |
|--------|------------|------------|
| Focus | Attacker actions | System failures |
| Root | Attack goal | Hazardous state |
| Causes | Intentional attacks | Failures, errors, accidents |
| Use case | Security analysis | Safety analysis |

## Worked Example
**Hazard: Chemical plant overheating**

```
Chemical plant overheats (OR)
├── Temperature sensor fails (OR)
│   ├── Hardware malfunction
│   ├── Firmware crash
│   └── Sensor tampered with (security → safety)
├── Cooling system fails to activate (OR)
│   ├── Control signal not received
│   ├── Actuator jammed
│   └── Command spoofed by attacker (security → safety)
└── Processing system gives wrong command (OR)
    ├── Logic error in control software
    ├── Corrupted sensor data not detected
    └── Integrity attack on sensor data (security → safety)
```

Note how security attacks appear as root causes of safety hazards.

## Common Pitfalls
- Treating security and safety as separate concerns — in IoT, security failures cause safety hazards
- Not including malicious causes (attacks) in fault trees
- Over-complicating trees with unlikely failure modes
- Not quantifying probabilities

## Connections
- [[attack-tree]] — Complementary analysis for security attacks
- [[threat-modeling]] — Fault trees formalize failure analysis
- [[security-by-design]] — Safety is a required design property
- [[resilience-iot]] — Resilience includes anticipating and withstanding failures
- [[operational-security-lifecycle]] — Safety analysis in the Define phase

## Open Questions
- How do we combine attack trees and fault trees into unified risk models?
- What failure probability data is available for IoT components?
- How do we model cascading failures across interconnected IoT systems?
