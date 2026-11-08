---
title: "Attack Tree"
tags: [concept, iot-security, semester-1]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: ["[[threat-modeling]]"]
---

## One-line Summary
An attack tree is a structured diagram modelling how an attacker could achieve a specific security goal, branching into sub-goals and methods — used as part of security analysis in IoT development.

## Core Intuition
Start with the attacker's goal at the top ("steal data from smart lock"), then ask "how?" at each level. The tree branches into increasingly specific methods. This makes abstract threats concrete and helps prioritise defenses.

## Formal Definition / Statement
**Attack Tree:** A structured diagram modelling how an attacker could achieve a specific goal, branching into sub-goals and methods. Each node represents an attack step; children of a node are alternative or combined methods to achieve that step.

- **Root node:** Attacker's ultimate goal
- **Intermediate nodes:** Sub-goals
- **Leaf nodes:** Specific, actionable attack methods
- **AND/OR gates:** Whether all children must succeed (AND) or any one (OR)

## Key Properties / Complexity

### Structure
- Hierarchical decomposition of attack goals
- OR nodes: any child suffices (alternative paths)
- AND nodes: all children required (combined attack)
- Leaf nodes: concrete, estimable attack steps

### Use in IoT
- Part of the Security required property in IoT development
- Used alongside [[fault-tree|fault trees]] for safety analysis
- Informs [[threat-modeling|threat modeling]] with concrete attack paths
- Supports risk assessment by estimating probability and cost at leaf nodes

### Benefits
- Makes threats concrete and actionable
- Enables quantitative risk analysis (cost/probability at leaves)
- Identifies single points of failure (critical OR nodes)
- Communicates risks to non-technical stakeholders

## Worked Example
**Goal: Unlock smart door remotely**

```
Unlock smart door (OR)
├── Exploit cloud API (OR)
│   ├── SQL injection in web interface
│   ├── Steal API credentials from mobile app
│   └── Brute-force weak password
├── Compromise ZigBee network (OR)
│   ├── Sniff network key during pairing
│   └── Replay captured unlock command
└── Physical attack (OR)
    ├── Extract firmware via JTAG
    └── Factory reset to default credentials
```

Each leaf can be estimated for cost, skill required, and probability.

## Common Pitfalls
- Building trees too shallow (missing real attack paths) or too deep (analysis paralysis)
- Not quantifying leaf nodes (trees become decorative, not analytical)
- Forgetting AND conditions (some attacks require multiple simultaneous steps)
- Only modelling technical attacks, ignoring social engineering

## Connections
- [[fault-tree]] — Complementary analysis for safety/hazards
- [[threat-modeling]] — Attack trees formalize threat identification
- [[security-by-design]] — Attack trees inform design decisions
- [[iot-attack-taxonomy]] — Attack types populate tree branches
- [[attack-surface-analysis]] — Attack surfaces define the scope of the tree

## Open Questions
- How do we maintain attack trees as systems evolve?
- Can attack trees be automatically generated from architecture models?
- How do we model attacker learning and adaptation over time?
