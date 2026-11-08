---
title: "Identity Life Cycle and Privacy in IoT"
tags: [topic, iot-security, semester-1, course-iot-security, identity-management, privacy]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-19
prerequisites: ["[[iot-lecture-6]]", "[[iot-lecture-5]]", "[[iot-lecture-4]]"]
sources: ["Russell & Van Duren, Practical Internet of Things Security, 2nd ed., 2019, Ch. 7"]
---

## One-line Summary
Identity lifecycle management (from device bootstrapping through deactivation) and privacy engineering (from Privacy by Design through regulatory compliance) are the organisational and architectural controls that turn cryptographic primitives ([[iot-lecture-6]]) into a defensible, legally compliant IoT deployment.

## Core Intuition

Lectures 1–6 gave us the *technical* toolbox: threat models, hardware roots of trust, secure boot, cryptographic primitives. Lecture 7 asks the harder question: **who is this device, who is allowed to talk to it, and what can it do with the data it collects?**

The answer has two halves:

1. **Identity lifecycle** — every IoT device needs a unique, verifiable identity from the moment it leaves the factory to the moment it is decommissioned. Without identity, there is no authentication, no authorisation, no audit trail. Identity is the *sine qua non* of IoT security.

2. **Privacy** — IoT devices are sensors that observe human behaviour. Even if the device is perfectly secure against attackers, it can still violate the user's privacy by design. Privacy must be engineered in, not bolted on after a regulatory fine.

The two halves interact: strong identity (pseudonymous certificates, short-lived tokens) is itself a privacy technique. Weak identity management (shared credentials, permanent identifiers) is a privacy liability.

## Formal Definition / Statement

### 1. Device Identity

A device identity is a set of attributes that uniquely identifies an IoT device in a system:

| Attribute | Purpose | Example |
|---|---|---|
| **Manufacturer** | Trust anchor provenance | "Acme Sensors Ltd." |
| **Device type** | Capability class | "Temperature sensor, model T-200" |
| **Serial number** | Unique instance identifier | "SN-00A4F2B7" |
| **Deployment date** | Lifecycle tracking | "2026-03-15" |
| **Location** | Physical context | "Building 3, Floor 2, Room 214" |

The identity is bound to cryptographic credentials during **secure bootstrapping** — the one-time process where a device receives its initial credentials (keys, certificates) in a trusted environment (factory, provisioning station).

### 2. Secure Bootstrapping and Credential Provisioning

The bootstrapping problem: how does a device that has never been on the network obtain its first credentials securely?

**Approaches:**
- **Factory provisioning**: credentials injected during manufacturing (most secure, requires trusted factory)
- **Pre-shared key (PSK) bootstrap**: device ships with a symmetric key; uses it to authenticate to a provisioning server that issues long-term credentials
- **Certificate-based bootstrap**: device ships with a manufacturer-issued device certificate; uses it to obtain operational credentials from a registration authority
- **Out-of-band channel**: QR code, NFC tap, or physical button press to transfer initial credentials

### 3. Account Lifecycle

Device and user accounts progress through states:

```
[Provisioned] → [Active] → [Monitored] → [Updated] → [Suspended] → [Deactivated/Deleted]
```

- **Monitoring**: continuous assessment of device behaviour (anomaly detection, compliance checks)
- **Updates**: credential rotation, firmware updates, policy changes
- **Suspension**: temporary revocation of access when anomalous behaviour detected
- **Deactivation/Deletion**: permanent removal of identity and credentials; must be irreversible and verifiable

### 4. Authentication Credentials

| Credential type | Strengths | Weaknesses | IoT suitability |
|---|---|---|---|
| **Passwords** | Simple, universal | Guessable, phishable, shared | Poor (unless device has UI) |
| **Symmetric keys** | Fast, small | Key distribution problem, no non-repudiation | Good for constrained devices |
| **Certificates (X.509)** | Strong, scalable, non-repudiation | Storage/compute overhead | Good for gateways, high-end devices |
| **Biometrics** | Non-transferable | Privacy concern, sensor cost | Limited (consumer devices only) |

### 5. Authorization Frameworks

**X.509 Certificates:**
- The de facto standard for PKI-based authorization
- Bind a public key to an identity via a Certificate Authority (CA) signature
- Chain of trust: root CA → intermediate CA → end-entity certificate
- Certificate revocation lists (CRLs) and OCSP for revocation

**IEEE 1609.2 (WAVE/DSRC for vehicular networks):**
- Implicit certificates: smaller than X.509, no explicit public key field
- Designed for high-speed, short-lived vehicular communications
- Pseudonymous certificates to preserve driver privacy

**OAuth 2.0 (RFC 6749):**
- Delegated authorization framework
- Four roles: resource owner, client, authorization server, resource server
- Grant types: authorization code, implicit (deprecated), client credentials, device code
- **Device Authorization Grant (RFC 8628)**: specifically designed for input-constrained IoT devices (the "enter this code on your phone" flow)

### 6. IoT IAM Infrastructure

**802.1X (Port-based Network Access Control):**
- Supplicant (device) ↔ Authenticator (switch/AP) ↔ Authentication Server (RADIUS)
- EAP methods: EAP-TLS (certificate-based), EAP-TTLS, PEAP
- Provides network-level admission control before the device gets an IP address

**PKI for IoT:**
- Hierarchical CA structure: root CA (offline, air-gapped) → regional/operational intermediate CAs → device certificates
- Scalability challenge: millions of devices need certificates; automated enrollment (EST, CMP) required
- Trust anchor stores: devices need a minimal set of root CA certificates

**Trusted Storage:**
- Keys and credentials must be stored in tamper-resistant hardware ([[trusted-platform-module]], secure element, HSM)
- Software-only key storage is vulnerable to extraction via firmware dump, side-channel, or physical attack

**Revocation:**
- CRLs: periodic list of revoked certificate serial numbers (bandwidth-heavy at scale)
- OCSP: online query per certificate (privacy concern — the OCSP server learns who is connecting to whom)
- OCSP stapling: server queries OCSP on behalf of client
- Short-lived certificates: avoid revocation entirely by making certificates expire quickly (hours/days)

### 7. Decentralized Trust via Blockchain

- **Problem with centralized PKI**: single point of failure, single trust anchor
- **Blockchain-based identity**: device identities registered on a distributed ledger; no single CA
- **Smart contracts for access control**: authorization policies encoded as smart contracts
- **Challenges**: latency, throughput, energy consumption, key management for blockchain transactions
- **Practical status**: mostly research/prototype; Hyperledger Fabric and IOTA are the most cited platforms for IoT

### 8. Privacy Concerns in IoT

**Complex data sharing chains:**
```
Wearable sensor → Smartphone app → Cloud analytics → Insurance company → Employer?
Smart home hub → Voice assistant → Cloud AI → Third-party skill developer → Advertiser?
```

Each hop is a potential privacy violation. The user who consented to the wearable may not know their data reaches an insurer.

**Metadata leakage:**
- Even encrypted traffic reveals: who is communicating, when, how often, message sizes
- Smart meter data at 1-second resolution can identify individual appliances (non-intrusive load monitoring)
- Wi-Fi probe requests reveal device presence and movement patterns

### 9. Privacy-Preserving Approaches

| Technique | Mechanism | Trade-off |
|---|---|---|
| **Pseudonymity** | Replace real identity with pseudonym; pseudonym can be changed | Re-identification possible if pseudonym is stable |
| **Anonymity** | Remove all identifying information | May reduce utility (no personalization) |
| **Short-lived certificates** | Certificates valid for hours, rotated frequently | Limits linkability of device communications |
| **Batch certificates** | One certificate covers a group of devices | Compromise of one certificate affects the batch |
| **Location Obscurer Proxy (LOP)** | Intermediate proxy that obfuscates precise location | Adds latency, requires trusted proxy |

### 10. Privacy Impact Assessment (PIA)

A structured process to identify and mitigate privacy risks *before* deploying a system:

1. **Describe** the data flows (what data, from whom, to where, for what purpose)
2. **Identify** privacy risks (unauthorized access, function creep, re-identification)
3. **Assess** likelihood and severity
4. **Mitigate** (minimize data, anonymize, add access controls)
5. **Document** and review periodically

Under GDPR, a Data Protection Impact Assessment (DPIA) is *mandatory* for high-risk processing (large-scale monitoring, profiling, sensitive data).

### 11. Data Retention Policies

- **Principle**: retain data only as long as necessary for the stated purpose
- **Implementation**: automated deletion schedules, data classification, retention periods per data type
- **Challenge**: IoT data may have unknown future value; deleting it forecloses future uses
- **Legal requirements**: GDPR storage limitation principle; sector-specific requirements (HIPAA: 6 years for medical records)

### 12. Privacy by Design (8 Principles)

The lecture extends Cavoukian's original 7 principles to 8:

1. **Proactive not Reactive**: Anticipate and prevent privacy-invasive events before they happen
2. **Privacy as the Default Setting**: No action required by the user; privacy is automatic
3. **Privacy Embedded into Design**: Integral to the architecture, not an add-on
4. **Full Functionality — Positive-Sum, not Zero-Sum**: Privacy and functionality coexist; no false trade-offs
5. **End-to-End Security — Full Lifecycle Protection**: Secure from collection to deletion
6. **Visibility and Transparency**: Keep practices open to scrutiny by users and providers alike
7. **Respect for User Privacy**: User interests are paramount; empower users
8. **Privacy throughout the Organization**: Extend across the entire business process and supply chain (the 8th principle added in the lecture)

### 13. Regulatory Landscape

| Regulation | Jurisdiction | Scope | Key IoT requirement |
|---|---|---|---|
| **GDPR** | EU | All personal data processing | Lawful basis, data minimization, DPIA, right to erasure, 72h breach notification |
| **e-Privacy Regulation** | EU | Electronic communications | Consent for cookies/tracking, confidentiality of communications |
| **HIPAA** | US | Health information | Protected health information safeguards, business associate agreements |
| **COPPA** | US | Children under 13 | Verifiable parental consent, privacy policy requirements |
| **FTC Framework** | US | Unfair/deceptive practices | Reasonable security, truth in privacy promises, data disposal |

### 14. IoT Compliance Monitoring

Five dimensions of compliance monitoring:

1. **Security**: vulnerability scanning, penetration testing, patch compliance
2. **Privacy**: data flow audits, consent management, retention policy enforcement
3. **Trust**: transparency reports, third-party audits, certification marks
4. **Resilience**: fault injection testing, disaster recovery exercises, redundancy verification
5. **Safety**: functional safety assessments (IEC 61508, ISO 26262), hazard analysis

## Key Properties / Complexity

### The Identity-Privacy Tension

Strong identity management and strong privacy are in tension:
- **More identity** = better authentication and accountability, but more data to protect and more privacy risk
- **Less identity** = better privacy (pseudonymity, anonymity), but harder to detect compromised devices and enforce policies

The engineering challenge is finding the right balance for each use case. A medical device needs strong identity (patient safety). A smart lightbulb needs minimal identity (low risk).

### Scalability of PKI for IoT

- Billions of devices need certificates
- Automated enrollment protocols: EST (Enrollment over Secure Transport, RFC 7030), CMP (Certificate Management Protocol, RFC 4210)
- Certificate lifecycle automation: issuance, renewal, revocation at scale
- Root CA protection: offline, air-gapped, hardware security modules

### Consent in IoT

- **Explicit consent**: user actively opts in (checkbox, button press)
- **Implicit consent**: inferred from behaviour or context (controversial)
- **Problem**: IoT devices often lack user interfaces for consent. How does a smart thermostat get consent from a guest?
- **GDPR standard**: consent must be freely given, specific, informed, and unambiguous

### The "Privacy Paradox"

Users say they care about privacy but behave as if they don't (accept all cookies, use "password123"). IoT makes this worse: devices collect data passively, without any user action at all.

## Worked Example

### Smart Home Privacy Architecture

**Scenario**: A smart home with a voice assistant, smart thermostat, door locks, and security cameras.

**Identity lifecycle:**
1. Each device receives a unique certificate during factory provisioning
2. On first connection, device authenticates to home hub using its certificate
3. Hub issues short-lived session tokens (OAuth 2.0 device grant)
4. Device behaviour monitored by hub; anomalous traffic triggers suspension
5. When device is sold/discarded, credentials revoked and identity deleted from hub

**Privacy by Design:**
1. *Proactive*: Voice assistant processes wake-word detection on-device; raw audio never leaves the device
2. *Default*: Camera recordings stored locally, not in cloud; cloud backup is opt-in
3. *Embedded*: All communication between devices and hub is TLS-encrypted
4. *Full functionality*: User gets full voice assistant features; only processed commands (not audio) sent to cloud
5. *End-to-end*: Encryption from device to cloud; data encrypted at rest on all servers
6. *Transparent*: Privacy dashboard shows what data each device collects and where it goes
7. *Respect user*: Physical microphone mute button; camera shutter; easy data export/deletion
8. *Throughout org*: Manufacturer's cloud team has no raw audio access; only processed commands

**Regulatory compliance:**
- GDPR: DPIA completed before deployment; data minimization (no raw audio stored); right to erasure implemented
- COPPA: parental consent required before voice assistant processes children's voices
- e-Privacy: consent required before any tracking cookies or analytics

## Common Pitfalls

- **Hardcoded credentials**: shipping devices with default passwords (admin/admin) — the #1 IoT security failure
- **Shared credentials**: all devices of the same model using the same certificate — one compromise breaks all devices
- **No revocation mechanism**: if a device is compromised, there's no way to revoke its credentials
- **"Anonymous" data that isn't**: smart meter data at 15-minute intervals can identify individual appliances and occupancy patterns
- **Consent by obscurity**: burying data collection in a 50-page privacy policy nobody reads
- **Function creep**: collecting data for one purpose, then using it for another (thermostat data sold to insurer)
- **Ignoring metadata**: encrypting the payload but leaking traffic patterns, timing, and message sizes
- **No data retention policy**: keeping all data forever "just in case" — violates GDPR storage limitation
- **Treating Privacy by Design as a checklist**: it's an architectural philosophy, not a box-ticking exercise
- **Blockchain as magic**: decentralized identity sounds great but introduces latency, complexity, and new attack surfaces

## Connections

- [[iot-architecture]] — identity and privacy are architectural concerns, not afterthoughts
- [[iot-compliance-frameworks]] — the regulatory requirements that drive privacy engineering
- [[privacy-by-design]] — the 8 principles in detail; this lecture extends the concept page
- [[secure-boot-chain]] — bootstrapping relies on a chain of trust from hardware to identity
- [[asymmetric-encryption]] — certificates and PKI are built on asymmetric cryptography
- [[iot-2-0]] — decentralized identity and blockchain-based trust models
- [[iot-lecture-6]] — cryptographic primitives that underpin identity and privacy mechanisms
- [[iot-lecture-5]] — hardware security (TPMs, secure elements) that protect stored credentials
- [[iot-lecture-4]] — operational security lifecycle includes identity management
- [[iot-data-lifecycle]] — data flows that create privacy risks
- [[iot-secure-design]] — privacy as a secure design goal
- [[nist-iot-cybersecurity]] — NIST framework includes identity management and access control
- [[authentication]] — the security service that identity management enables
- [[key-management-lifecycle]] — credential provisioning and rotation

## Open Questions

- Will decentralized identity (blockchain/DID) replace PKI for IoT, or will they coexist?
- How should consent work for IoT devices in shared spaces (office building, rental apartment)?
- Is short-lived certificate rotation practical for battery-powered devices with limited compute?
- Can Privacy by Design be certified/audited, or is it inherently subjective?
- How do you enforce data retention policies when data has been replicated across multiple cloud services?
- Will the e-Privacy Regulation (still in draft as of 2024) create new obligations for IoT device manufacturers?
