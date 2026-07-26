---
title: "Common Criteria (ISO 15408)"
tags: [concept, iot-security, standards, evaluation, semester-1]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-22
prerequisites: []
---
## One-line Summary
*An international standard for evaluating the security properties of IT products through structured assurance levels.*

## Core Intuition
Different countries had their own security evaluation standards (TCSEC in the US, ITSEC in Europe). Common Criteria harmonized these into a single framework so a product evaluated in Germany is recognized in the US. For IoT, it provides a way to objectively compare the security claims of different devices — critical when deploying devices in sensitive environments like healthcare or critical infrastructure.

## Formal Definition / Statement
Common Criteria (CC, ISO/IEC 15408) is an international framework for specifying and evaluating security requirements for IT products. It defines:

- **Protection Profiles (PP)**: Security requirements for a class of products (e.g., smart cards, network devices). A PP defines what a product SHOULD do.
- **Security Targets (ST)**: Vendor-specific claims about a product's security. Defines what the product CLAIMS to do.
- **Evaluation Assurance Levels (EAL)**: Seven levels (EAL1–E7) of increasing rigor in testing and analysis.

EAL Levels:
- **EAL1**: Functionally tested — basic black-box testing
- **EAL2**: Structurally tested — some access to design docs
- **EAL3**: Methodically tested and checked — development environment review
- **EAL4**: Methodically designed, tested, and reviewed — most common for commercial products
- **EAL5**: Semiformally designed and tested — formal security modelling
- **EAL6**: Semiformally verified design and tested — sophisticated attackers
- **EAL7**: Formally verified design and tested — highest assurance, rare and expensive

## Key Properties / Complexity
- EAL4 is the most common level for commercial IoT products
- Evaluation is performed by accredited labs (Common Criteria Testing Laboratories)
- Mutual Recognition Arrangement (MRA) enables cross-country recognition of certificates
- Evaluation can take 6–18 months and cost $100K–$1M+
- IoT devices typically target EAL2–EAL4 due to cost constraints
- Protection Profiles for IoT are still evolving — no widely adopted IoT-specific PP yet

## Worked Example
A manufacturer of a medical IoT gateway wants to sell to German hospitals. They:
1. Identify a relevant Protection Profile (e.g., for network devices)
2. Write a Security Target documenting their implementation's security claims
3. Submit to an accredited German BSI lab for EAL4 evaluation
4. The lab reviews design docs, tests the product, and issues a certificate
5. The certificate is recognized across all MRA countries (30+ nations)
6. The hospital can procure the device knowing it meets a defined assurance baseline

## Common Pitfalls
- **EAL rating != security level**: EAL4 doesn't mean 'secure' — it means the evaluation process was rigorous. A product can be EAL4 certified and still have vulnerabilities if the Security Target was narrow.
- **Scope matters**: Certification only covers what's in the Security Target. An IoT device might be certified for its crypto module but not its wireless stack.
- **Cost barrier**: Small IoT vendors often can't afford CC evaluation, creating a gap between high-assurance enterprise products and consumer IoT.
- **Snapshot in time**: Certification evaluates a specific version. Updates and patches are not automatically covered.

## Connections
- [[tcg-specifications]] — TPM chips often undergo CC evaluation at EAL4+
- [[fips-140-2]] — Complementary standard focused specifically on cryptographic modules
- [[iec-62443]] — Industrial systems standard that may reference CC evaluation
- [[risk-assessment-frameworks]] — CC evaluation informs risk acceptance decisions
- [[secure-boot-chain]] — Secure boot implementations may be included in CC evaluation scope
- [[iot-compliance-frameworks]] — CC is one of many compliance frameworks for IoT

## Open Questions
- How does this standard/framework apply to resource-constrained IoT devices with limited processing power?
- What are the practical tradeoffs between compliance and actual security improvement?
