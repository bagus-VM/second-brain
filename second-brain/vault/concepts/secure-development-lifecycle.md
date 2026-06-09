---
title: "Secure Development Life Cycle (SDLC)"
tags: [concept, iot-security, semester-1]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: ["[[security-by-design]]"]
---

## One-line Summary
The Secure Development Life Cycle (SDLC) integrates security into every phase of software/system development — from requirements through deployment — using models like Waterfall, Spiral, and Agile.

## Core Intuition
Security can't be tested in at the end. Each SDLC model has different strengths and weaknesses for security, but all must include security activities at every phase. The choice of model affects how quickly you can respond to discovered vulnerabilities.

## Formal Definition / Statement
**Secure Development Life Cycle (SDLC):** Development of security from scratch in the framework of a system, essentially the same as software development from scratch but with security integrated at every phase.

### SDLC Models

**1. Waterfall Development Model**
- Linear sequential design process
- No iterations or feedback (basic version)
- Can be extended with feedback (Royce's iterative waterfall)
- Strengths: Clear milestones, documentation
- Weaknesses: Late discovery of security issues is expensive to fix

**2. Spiral Development Model**
- Addresses iteration issues; based on feedback
- Still mostly one-way regarding progress
- Issues discovered late require a restart
- Strengths: Risk analysis at each spiral
- Weaknesses: Can be slow, restarts are costly

**3. Agile Development Model**
- Not based on an exact plan
- Principles:
  - Individuals and interactions over processes and tools
  - Working software over comprehensive documentation
  - Customer collaboration over contract negotiation
  - Responding to change over following a plan
- Very efficient if supervised and deadlines met
- Otherwise chaotic
- Strengths: Rapid response to security issues
- Weaknesses: Can sacrifice security documentation for speed

## Key Properties / Complexity

### Security Activities per Phase
| Phase | Waterfall | Agile |
|-------|-----------|-------|
| Requirements | Security requirements | Security user stories |
| Design | Threat modelling, architecture review | Security spikes |
| Implementation | Secure coding standards | Pair programming, code review |
| Testing | Penetration testing, SAST/DAST | Continuous security testing |
| Deployment | Security review gate | Automated security CI/CD |
| Maintenance | Patch management | Continuous monitoring |

### Evolution to DevOps
- [[devops-security|DevOps]] extends SDLC by blending development with operations
- Continuous feedback from production informs development
- Critical for IoT where devices are in the field for years

## Worked Example
**Agile SDLC for IoT Firmware:**
1. Sprint planning: security user story "As a user, I want my credentials encrypted at rest"
2. Design: threat model for credential storage
3. Implement: encrypt credentials using device key (protected by TPM)
4. Test: SAST scan, penetration test on credential extraction
5. Deploy: OTA update to test devices
6. Monitor: track authentication failure rates

## Common Pitfalls
- Treating SDLC as a rigid process instead of adapting to context
- Choosing Waterfall for IoT (too slow to respond to field vulnerabilities)
- Choosing Agile without security supervision (becomes chaotic)
- Not including security in every sprint/phase

## Connections
- [[security-by-design]] — SDLC is the process for implementing security by design
- [[devops-security]] — DevOps extends SDLC into operations
- [[threat-modeling]] — Key activity in the Design phase
- [[attack-tree]] — Security analysis tool for design phase
- [[ota-updates]] — Deployment mechanism for IoT SDLC
- [[operational-security-lifecycle]] — SDLC precedes the operational lifecycle

## Open Questions
- Which SDLC model is best for IoT hardware-software co-design?
- How do we maintain security for IoT devices that outlive the development team?
- Can SDLC processes be standardised across the diverse IoT industry?
