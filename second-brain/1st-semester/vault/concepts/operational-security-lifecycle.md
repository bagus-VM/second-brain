---
title: "Operational Security Life Cycle"
tags: [concept, iot-security, semester-1]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: ["[[security-by-design]]", "[[devops-security]]"]
---

## One-line Summary
The operational security life cycle for IoT spans four phases — Define, Implement/Integrate, Operate and Maintain, and Dispose — ensuring security is enforced from conception through decommissioning.

## Core Intuition
Security isn't a product you install once. It's a process that must be maintained throughout the entire life of an IoT system — from defining policies, through deployment and operation, to secure disposal when devices are retired.

## Formal Definition / Statement
The Operational Security Life Cycle has four phases:

### 1. Define Phase
- Define system security policies
- Define system roles

### 2. Implement/Integrate Phase
- Configure gateways and network security
- Bootstrap and securely configure devices
- Set up threat intelligence and vulnerability monitoring
- Set up deception mechanisms
- Train stakeholders

### 3. Operate and Maintain Phase
- Manage assets
- Manage credentials
- Manage firmware and patch updates
- Monitor the system
- Perform penetration testing
- Manage incidents

### 4. Dispose Phase
- Secure disposal
- Data purging
- Inventory removal
- Data archival/records maintenance

## Key Properties / Complexity

### Lifecycle Security Enforcement
Security should be enforced throughout the development and operational lifecycle of ALL IoT devices and hubs. This is distinct from the [[secure-development-lifecycle|SDLC]] which focuses on development; the operational lifecycle covers deployment through disposal.

### Key Practices by Phase
- **Define:** [[threat-modeling|Threat modeling]], policy definition
- **Implement:** Device hardening, network segmentation, deception
- **Operate:** Continuous monitoring, pen testing, incident response, credential rotation
- **Dispose:** Data destruction, secure wipe, removing from inventory

## Worked Example
**Smart Factory IoT Lifecycle:**
1. **Define:** Policy: all sensors must authenticate before data transmission; roles: operator, admin, auditor
2. **Implement:** Deploy sensors with unique credentials, configure VLANs, set up SIEM for monitoring
3. **Operate:** Monthly pen tests, quarterly credential rotation, continuous firmware updates via [[ota-updates|OTA]]
4. **Dispose:** End-of-line sensors have flash wiped, removed from asset database, data archived per retention policy

## Common Pitfalls
- Skipping the Define phase and jumping to deployment
- Ignoring the Dispose phase — old devices with data are a security risk
- Not maintaining threat intelligence after initial deployment
- Treating "set and forget" as acceptable for IoT devices

## Connections
- [[security-by-design]] — Security starts before the lifecycle
- [[secure-development-lifecycle]] — Development lifecycle precedes operational lifecycle
- [[devops-security]] — DevOps bridges development and operations
- [[ota-updates]] — Critical for Operate and Maintain phase
- [[iot-compliance-frameworks]] — Compliance requirements across the lifecycle
- [[resilience-iot]] — Resilience is an operational concern

- [[iot-lecture-1]] — IoT Security Landscape — course overview
- [[iot-lecture-4]] — IoT Secure Design — best practices
- [[iot-lecture-5]] — IoT Security Hardware — PUFs, TPMs, secure boot

## Open Questions
- How do we manage the lifecycle of devices that may operate for 10-20 years?
- Who is responsible for security after a manufacturer goes out of business?
- How do we handle devices that can't be updated but can't be replaced?
