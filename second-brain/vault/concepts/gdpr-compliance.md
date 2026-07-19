---
title: "GDPR Compliance"
tags:
  - concept
  - iot-security
  - semester-1
  - privacy
  - compliance
course: IoT Security
source_count: 1
status: current
last_updated: 2026-07-02
---

## One-line Summary
GDPR is EU law governing personal data processing — for IoT, it mandates data minimization, purpose limitation, impact assessments, and ongoing compliance monitoring.

## Core Intuition
The General Data Protection Regulation (GDPR) gives individuals control over their personal data. For IoT, this creates unique challenges: devices collect data continuously (often without screens for consent), process it in the cloud (often across borders), and may have limited storage management (making "right to erasure" difficult). GDPR compliance is not a one-time certification — it requires ongoing monitoring, documentation, and the ability to demonstrate compliance at any time.

## Formal Definition / Statement
GDPR (Regulation (EU) 2016/679) establishes principles for lawful processing of personal data:

1. **Lawfulness, fairness, transparency** — process data lawfully with clear notice
2. **Purpose limitation** — collect for specified, explicit, legitimate purposes
3. **Data minimization** — collect only what is adequate, relevant, necessary
4. **Accuracy** — keep data accurate and up to date
5. **Storage limitation** — keep data no longer than necessary
6. **Integrity and confidentiality** — protect with appropriate security
7. **Accountability** — demonstrate compliance

For high-risk processing (most IoT systems), a **Data Protection Impact Assessment (DPIA)** is mandatory before deployment.

## Key Properties
| Property | Detail |
|----------|--------|
| Scope | Any entity processing EU residents' personal data |
| Consent | Must be freely given, specific, informed, unambiguous |
| DPIA | Mandatory for high-risk processing (most IoT qualifies) |
| Right to erasure | Individuals can request data deletion |
| Data portability | Individuals can request data in machine-readable format |
| Breach notification | 72-hour notification requirement for data breaches |
| Penalties | Up to €20M or 4% of global annual turnover |
| Ongoing | Compliance is continuous, not one-time |

## Worked Example
A fitness tracker company deploys an IoT wearable:

**Data collected:** heart rate, location, sleep patterns, user profile
**Processing:** health analytics, personalized recommendations, aggregated research

**GDPR requirements:**
- **Minimization**: Only collect heart rate if needed for stated purpose — don't collect microphone data "just in case"
- **Consent**: On first app connection, present clear consent dialog explaining what data is collected and why (not buried in 50-page terms)
- **DPIA**: Required — health data is "special category" data under GDPR
- **Storage limitation**: Delete raw location data after 30 days if not needed for service
- **Right to erasure**: User can request account deletion; company must delete all personal data within 30 days
- **Security**: Encrypt heart rate data in transit (TLS) and at rest (AES-256)
- **Breach notification**: If database is compromised, notify supervisory authority within 72 hours

**IoT-specific challenge:** The wearable has no screen — consent is collected via the companion app. If the device stores data locally before syncing, how is "right to erasure" enforced on the device itself?

## Common Pitfalls
- **Thinking consent is always required**: GDPR has 6 legal bases for processing; consent is only one. Legitimate interest or contract performance may apply
- **One-time compliance**: GDPR requires ongoing monitoring and documentation — not a checkbox exercise
- **Assuming anonymization solves everything**: Truly anonymized data is not personal data, but pseudonymized data still is
- **Ignoring headless devices**: Devices without screens need alternative consent mechanisms (companion app, voice, web portal)
- **Underestimating penalties**: €20M or 4% of global turnover — both numbers matter
- **Confusing GDPR with security**: GDPR mandates appropriate security but is fundamentally about data protection rights, not cybersecurity

## Connections
- [[legal-frameworks-research-data]] -- GDPR as one of four legal frameworks for research data
- [[privacy-by-design]] -- GDPR Article 25 mandates privacy by design and by default
- [[iot-privacy-concerns]] — IoT-specific privacy challenges beyond GDPR
- [[iot-identity-lifecycle]] — device and user identity management for compliance
- [[data-provenance]] — tracking data origin and processing for accountability
- [[iot-lecture-7]], [[iot-lecture-8]] — source lectures

## Open Questions
- How do IoT manufacturers handle GDPR consent on headless devices (no screen, no keyboard)?
- What are the practical penalties for IoT GDPR violations — has enforcement kept pace with IoT growth?
- How does GDPR interact with edge computing where data is processed on-device?
- Can "legitimate interest" justify continuous IoT data collection without explicit consent?
