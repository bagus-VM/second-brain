---
title: "Availability in Information Security"
tags: [concept, iot-security, cia-triad, semester-1]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-22
prerequisites: []
---
## One-line Summary
*The assurance that systems and data are accessible to authorized users when needed, forming the 'A' in the CIA triad.*

## Core Intuition
A perfectly encrypted system that's always down is useless. Availability ensures that the security measures you implement don't make the system unusable, and that attackers can't make it unusable either. For IoT, availability is especially critical — if a medical device monitor goes offline, a patient could be at risk. If a smart grid controller is DDoSed, power distribution fails.

## Formal Definition / Statement
Availability is the property that ensures timely and reliable access to information and system resources.

**Threats to availability:**
- Denial of Service (DoS/DDoS) attacks
- Hardware failures (disk crash, power outage)
- Software failures (crash, deadlock, resource exhaustion)
- Natural disasters (flood, fire, earthquake)
- Human error (misconfiguration, accidental deletion)

**Countermeasures:**
- **Redundancy**: duplicate hardware, failover systems, load balancing
- **Backups**: regular, tested, off-site backups with defined RPO/RTO
- **DoS protection**: rate limiting, traffic filtering, CDN, DDoS mitigation services
- **High availability (HA)**: clustering, active-passive failover, active-active architectures
- **Disaster recovery**: documented DR plan, alternate sites, recovery procedures
- **Capacity planning**: ensuring sufficient resources for peak loads

**Metrics:**
- Uptime percentage: 99.9% (8.76 hours downtime/year), 99.99% (52.6 min/year), 99.999% (5.26 min/year)
- Mean Time Between Failures (MTBF)
- Mean Time To Recovery (MTTR)
- Recovery Point Objective (RPO): maximum acceptable data loss
- Recovery Time Objective (RTO): maximum acceptable downtime

**In IoT specifically:**
- Battery life affects availability of mobile/sensor devices
- Network connectivity (cellular, Wi-Fi, LoRa) affects reachability
- Firmware updates can cause temporary unavailability
- Physical access restrictions may prevent maintenance

## Key Properties / Complexity
- Availability is often in tension with confidentiality and integrity (security measures can reduce availability)
- High availability (99.999%) is expensive and complex
- IoT devices have unique availability challenges: battery, connectivity, physical access
- DoS attacks directly target availability
- Availability must be designed in, not added after the fact

## Worked Example
Ensuring availability for an IoT fleet management system:
- **Architecture**: Active-active deployment across 3 cloud regions
- **Load balancing**: DNS-based failover with health checks every 30 seconds
- **Data replication**: Synchronous replication between regions (RPO = 0)
- **Device resilience**: Devices cache last known instructions locally; continue operating during cloud outage
- **DoS protection**: Rate limiting at API gateway, WAF rules, traffic scrubbing
- **Monitoring**: 24/7 alerting on latency spikes, error rates, connectivity drops
- **RTO**: 5 minutes for regional failover
- **Uptime target**: 99.99% (52 minutes downtime/year)

Incident: Cloud region us-east-1 goes down at 3 AM. DNS health checks detect failure in 30 seconds. Traffic routes to eu-west-1 within 2 minutes. Devices reconnect to new endpoint. Total downtime: 2 minutes 15 seconds.

## Common Pitfalls
- **Availability vs security**: Overly aggressive security (firewall rules, authentication) can block legitimate access
- **Single points of failure**: One overlooked SPOF can negate all redundancy investments
- **Untested failover**: Failover that's never tested often fails when needed
- **IoT-specific**: Battery depletion = permanent unavailability; no 'reboot' for a dead sensor
- **Cost**: High availability is expensive; 99.999% costs 10-100× more than 99.9%
- **Data consistency**: Active-active systems may have consistency challenges during failover

## Connections
- [[cia-triad]] — Availability is the 'A' in Confidentiality, Integrity, Availability
- [[denial-of-service]] — Primary attack vector targeting availability
- [[information-assurance]] — Broader framework encompassing availability
- [[risk-assessment-frameworks]] — Availability requirements drive risk assessment priorities
- [[iot-secure-design]] — Secure design must balance security with availability
- [[network-security-fundamentals]] — Network redundancy and failover for availability

## Open Questions
- How do availability requirements interact with confidentiality and integrity when they conflict in practice (e.g., strict access controls that block legitimate failover)?
- What is the right availability target for resource-constrained IoT devices with intermittent connectivity?
