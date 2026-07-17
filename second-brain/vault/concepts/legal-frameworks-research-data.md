---
title: "Legal Frameworks for Research Data"
tags: [concept, reproducibility-engineering, semester-1, law, copyright, data-protection, trade-secrets]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-07-17
prerequisites: ["[[fair-data-principles]]"]
---

## One-line Summary
Research data sits at the intersection of copyright, data protection (GDPR), trade secrecy, and database rights -- each framework protects a different aspect.

## Core Intuition
When you store research data, you're not just dealing with files on a disk. You're operating inside a legal landscape where multiple frameworks overlap. A single database might contain: personal data protected by GDPR, a schema protected by copyright, contents protected by the sui generis database right, and confidential business information protected by trade secrecy. Understanding which framework applies to which layer is essential for reproducible (and legal) research data management.

## Formal Definition / Statement
Four legal frameworks apply to research data, each protecting a different aspect:

### 1. Copyright
Protects **creative expression**, not ideas or facts. In a database context:
- **Schema design** -- if sufficiently original (not trivial field names like `firstName`)
- **Source code** -- stored procedures, UDFs, application code
- **GUI and API design** -- if they reflect creative choices
- **Stored content** -- images, text, audio that are creative works themselves

Key distinction: copyright protects the *structure and code*, not the *data itself*. Facts (temperature readings, gene sequences) are not copyrightable.

### 2. Data Protection (GDPR)
Protects **personal data of identifiable living individuals**. Applies when research data contains names, emails, health records, or any information that can identify a person.
- Requires a lawful basis for processing (consent, legitimate interest, etc.)
- Data minimization: collect only what you need
- Right to erasure: individuals can request deletion
- Storage limitation: don't keep data longer than necessary

GDPR is not about protecting the *database* -- it's about protecting the *people whose data is in it*.

### 3. Trade Secret Protection
Protects **confidential business information** that derives value from not being publicly known. In a database context:
- Customer lists
- Proprietary datasets compiled at significant cost
- Internal algorithms and methodologies

Protection requires active secrecy measures (NDAs, access restrictions, encryption). Once the information becomes public, protection is lost.

### 4. Sui Generis Database Right (EU)
Protects the **substantial investment** in obtaining, verifying, or presenting database contents. See [[sui-generis-database-right]] for the full treatment.

## Key Properties

### Layered protection
A single database can be protected by multiple frameworks simultaneously:
- The *schema* by copyright (if original)
- The *personal records* by GDPR
- The *compilation of data* by sui generis rights
- The *business data* by trade secrecy

### Facts vs. expression
Copyright protects expression, not facts. The temperature reading "23.5°C" is a fact -- not copyrightable. A creative visualization of temperature data *is* copyrightable. This is why the sui generis right exists: to protect the investment in compiling facts that copyright can't reach.

### Research exceptions
Most frameworks include exceptions for research:
- **Copyright**: fair use / fair dealing for research and education
- **GDPR**: exemptions for scientific research (with safeguards)
- **Sui generis**: privileged use for research purposes

These exceptions are what make reproducible research legally possible.

### Jurisdiction matters
- GDPR is EU law but applies to any entity processing EU residents' data
- Sui generis is EU-only (no US equivalent)
- Copyright is international (Berne Convention) but details vary by country
- Trade secrecy is national law (EU Trade Secrets Directive, US DTSA)

## Worked Example
A university research team collects patient health data for a medical study:
- **GDPR applies** because the data contains personal health information
- **Copyright applies** to the database schema (creative design choices) and any analysis code
- **Trade secrecy** may apply to the specific methodology if the university treats it as confidential
- **Sui generis** protects the compiled dataset if obtaining it required substantial investment

When sharing the data for reproducibility:
- GDPR requires anonymization or pseudonymization
- Copyright licenses (e.g., CC-BY) govern reuse of creative elements
- Sui generis rights may restrict bulk extraction by third parties
- Trade secrecy is lost if the data is published openly

## Common Pitfalls
- **Confusing data and metadata.** GDPR protects personal *data*; metadata (collection date, instrument type) is usually not personal data.
- **Assuming open data is unprotected.** Even openly published databases retain sui generis rights and copyright.
- **Forgetting that facts aren't copyrightable.** You can't copyright a temperature reading. You can copyright a creative arrangement of temperature readings.
- **Ignoring jurisdiction.** A database created in Germany is protected by EU sui generis rights even if accessed from the US.

## Connections
- [[fair-data-principles]] -- FAIR's "Reusable" principle requires clear licensing (R1.1)
- [[sui-generis-database-right]] -- the EU-specific right protecting database investment
- [[gdpr-compliance]] -- GDPR as it applies to IoT (from IoT Security course)
- [[privacy-by-design]] -- designing systems with GDPR compliance from the start
- [[data-provenance]] -- provenance records support legal compliance (R1.2)
- [[reproducibility-engineering-sheet-11]] -- IC_11 exercises on legal frameworks

## Open Questions
- How does the Oracle v. Google ruling (API copyright) affect research API design?
- Can AI-generated database schemas be copyrighted? (No clear legal answer yet.)
- How do you balance FAIR's accessibility goals with GDPR's data minimization principle?
