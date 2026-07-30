---
title: "Lecture 11: FAIR Principles and Legal Aspects of Research Data"
tags: [concept, reproducibility-engineering, semester-1]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-07-29
prerequisites:
  - reproducibility-engineering-lecture-10
  - artifact-availability
  - data-provenance
---

## One-line Summary
Making research data FAIR (Findable, Accessible, Interoperable, Reusable) means applying machine-actionable metadata and persistent identifiers, while legal frameworks (copyright, GDPR, trade secrets, sui generis database right) determine what you can share and how.

## Core Intuition
Reproducibility is not just a technical problem. You can pin every dependency, containerize every pipeline, and record every parameter, but if you are legally prohibited from sharing the dataset, nobody can reproduce your work. FAIR principles define what good data stewardship looks like: persistent identifiers, rich metadata, open standards, clear licenses. Legal frameworks define the constraints: copyright protects creative expression (code, papers, figures) but not facts; GDPR protects personal data; trade secrets protect confidential business information; the EU sui generis database right protects the investment of compiling a database.

The key distinction that trips people up: FAIR does not mean open. FAIR means findable and accessible with a clear protocol. Data can be FAIR and restricted (authenticated access, academic-only license). The goal is machine-actionability: a computational agent should be able to discover, interpret, access, and reuse data without human intervention.

## Formal Definition / Statement

### FAIR Guiding Principles (Wilkinson et al., 2016)

**Findable:**
- (Meta)data are assigned a globally unique and persistent identifier
- Data are described with rich metadata
- Metadata clearly and explicitly include the identifier of the data they describe
- (Meta)data are registered or indexed in a searchable resource

**Accessible:**
- (Meta)data are retrievable by their identifier using a standardized communications protocol
- The protocol is open, free, and universally implementable
- The protocol allows for authentication and authorization where necessary
- Metadata remain accessible even when the data are no longer available

**Interoperable:**
- (Meta)data use a formal, accessible, shared, and broadly applicable language for knowledge representation
- (Meta)data use vocabularies that themselves follow FAIR principles
- (Meta)data include qualified references to other (meta)data

**Reusable:**
- (Meta)data are richly described with accurate and relevant attributes
- (Meta)data are released with a clear and accessible data usage license
- (Meta)data are associated with detailed provenance
- (Meta)data meet domain-relevant community standards

### What FAIR applies to
Research data, algorithms, software tools, workflows. Not physical laboratory equipment. FAIR targets digital research objects.

### FAIR stakeholders
Researchers who produced the data, researchers who reuse it, data publishers, funding agencies, and computational agents (a key design goal: machines should autonomously find and process data).

### Legal frameworks

| Framework | What it protects | Key distinction |
|-----------|------------------|-----------------|
| Copyright | Creative expression (code, papers, figures, schemas with originality) | Facts are NOT copyrightable. Only the creative expression is. |
| GDPR | Personal data of identifiable living individuals (EU residents) | Requires consent and anonymization. Does not apply to deceased persons or fully anonymized data. |
| Trade secrets | Confidential business information under NDA | Sharing under NDA breaks the agreement. |
| Database sui generis right (EU Directive 96/9/EC) | Investment in obtaining, verifying, or presenting database contents | Protects the investment of collecting existing data, NOT the creation of new data. EU-only right. |

## Key Properties / Complexity

### Copyright vs. sui generis: what protects what?

| Artifact | Copyright? | Sui generis? | Notes |
|----------|-----------|-------------|-------|
| Database schema (original) | Yes (literary work) | No | Only if sufficiently original (not trivial like firstName/lastName) |
| Stored procedure / UDF | Yes (software) | No | Code is copyrighted |
| Raw data (temperature records) | No (facts) | Yes (if substantial investment) | Facts are not copyrightable, but compilation investment is |
| GUI | Yes (visual art + code) | No | Creative work |
| API design | Debated (see Oracle v. Google) | No | Interface structure involves creative choices |
| Trivial 2-column schema (firstName, lastName) | No (too trivial) | No | Lacks originality for copyright; no database investment |

### Sui generis database right: key cases

| Case | Ruling | Why |
|------|--------|-----|
| BHB v. William Hill | NOT protected | BHB created data (organizing races). Sui generis protects *obtaining* existing data, not *creating* new data. |
| Toll Collect | NOT protected | Toll records generated as a byproduct of running the system, not obtained through separate substantial investment. |
| University research database | Protected | University made substantial investment in obtaining and verifying data. |

### Sui generis: what violates the right?

| Action | Violates? |
|--------|----------|
| Extracting a single record | No (not a substantial part) |
| Repeatedly extracting individual records until copied | Yes (systematic extraction = substantial) |
| Extracting all records | Yes (clearly substantial) |
| Scientific research reproduction (EU) | No (privileged use exception) |

### Sui generis jurisdiction
EU-only right. Protects databases created by EU nationals/residents/companies. A US company has no sui generis protection in the US (no equivalent law), but can claim it in the EU if they meet the investment threshold. The right exists automatically, no registration needed.

## Worked Example

### FAIR category assignment

"Released with a clear and accessible data usage license" → Reusable. A license tells others how they can reuse the data.

"Assigned a globally unique and persistent identifier" → Findable. You cannot find data without a stable identifier.

"Use commonly adopted, accessible, and preferably open standards and formats" → Interoperable. Standards let different systems work with the same data.

"Metadata remain accessible even when the data are no longer available" → Accessible. The metadata survives the data.

### Legal framework matching

A spreadsheet with personal information about identifiable living individuals → GDPR. Personal data of EU residents requires consent and anonymization.

A company keeps its customer list confidential using NDAs → Trade secret protection. NDAs are the mechanism.

A research article reproduces an original figure from a textbook → Copyright. The figure is a copyrightable creative work.

A database of publicly available weather measurements → None of the above. No personal data (no GDPR), no creative expression (no copyright), no confidential info (no trade secret), and weather data is not inherently protected unless substantial investment in compilation (sui generis).

### Why BHB lost

The British Horse Racing Board organized races and selected participants. It argued its database of racing data deserved sui generis protection. The European Court of Justice disagreed: the data was created as part of BHB's normal business activity. The sui generis right protects investment in *obtaining existing data* from external sources, not in *generating new data* through your own operations. Since BHB created the data rather than collecting it, the investment was in data creation, not data obtaining.

## Common Pitfalls

**"FAIR means open access."** No. FAIR means findable and accessible with a clear protocol. Data can be FAIR and restricted behind authentication. The protocol must be open and standardized, but the data itself can be access-controlled.

**"Copyright protects datasets of facts."** No. Facts are not copyrightable. A dataset of temperature measurements has no copyright protection. But the *selection or arrangement* of those facts might qualify for the sui generis database right in the EU, if substantial investment was made in compiling them.

**"The sui generis right protects any database."** No. It protects databases where substantial investment was made in *obtaining, verifying, or presenting* existing data. If you *created* the data yourself (like BHB organizing races), the right does not apply. The distinction is collection vs. creation.

**"A trivial schema is copyrightable."** No. A two-column schema (firstName, lastName) is too obvious to have the originality required for copyright. A novel partitioning of Germany into 1,860 carefully crafted regions would be copyrightable because it reflects creative intellectual effort.

**"US companies get sui generis protection in the US."** No. The sui generis database right is EU-only. The US has no equivalent. A US company can claim protection *in the EU* if they meet the investment threshold, but not at home.

**"Computational agents are not FAIR stakeholders."** Wrong. The inclusion of computational agents as stakeholders is what distinguishes FAIR from earlier data management guidelines. FAIR is designed for machine-actionable data.

## Connections

[[reproducibility-engineering-lecture-10]]: Lecture 10 covers artifact packaging and workflow provenance, which are the practical mechanisms that make data FAIR.

[[artifact-availability]]: Artifact availability (ACM badging) is the publishing-side counterpart to FAIR principles. FAIR is the data management framework; ACM badges certify specific artifacts.

[[data-provenance]]: Provenance is a FAIR Reusable requirement. Detailed provenance makes data reusable because others can trace its origins and transformations.

[[reproducible-builds]]: Reproducible builds ensure the software side of FAIR. FAIR data needs reproducible software to be useful.

[[reproducibility-crisis]]: FAIR principles are a direct response to the reproducibility crisis. If data is not findable or accessible, reproduction is impossible.

## Open Questions

- How will the e-Privacy Regulation (still in draft) affect IoT data sharing under FAIR?
- Can FAIR compliance be automatically audited, or is it inherently subjective?
- How do you enforce data retention policies when data has been replicated across multiple cloud services?
- Is there a standard format for recording FAIR metadata that the community has converged on?
