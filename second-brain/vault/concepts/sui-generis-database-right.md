---
title: "Sui Generis Database Right"
tags: [concept, reproducibility-engineering, semester-1, law, databases, eu-law]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-07-17
prerequisites: ["[[legal-frameworks-research-data]]"]
---

## One-line Summary
An EU-specific right that protects the substantial investment in compiling a database, separate from copyright.

## Core Intuition
Copyright protects creative expression -- but what about a database that required enormous effort to compile but isn't "creative" in the copyright sense? A phone directory, a collection of weather measurements, or a genomic database might involve years of work and millions of euros, yet the individual entries are facts (not copyrightable). The EU Database Directive (96/9/EC) created the **sui generis database right** specifically to fill this gap: it protects the *investment* in obtaining, verifying, or presenting the contents, regardless of whether the database is creative.

## Formal Definition / Statement
The sui generis database right (EU Directive 96/9/EC, Article 7) prohibits:
- **Extraction** -- transferring the whole or a substantial part of the contents to another medium by any means
- **Reutilization** -- making the whole or a substantial part available to the public by any means

The right applies when there has been a "qualitatively and/or quantitatively a substantial investment in either the obtaining, verification or presentation of the contents."

## Key Properties / Complexity

### What counts as "substantial investment"
- **Obtaining**: collecting existing data from scattered sources (e.g., compiling weather stations' readings into one database)
- **Verification**: checking data for accuracy and consistency
- **Presentation**: organizing data for efficient access

The investment must be in the *data itself*, not in *creating* the data. This is the most contested boundary.

### Creation vs. obtaining (the BHB rule)
The European Court of Justice ruled in **BHB v. William Hill** (2004) that creating data is not "obtaining" it. The British Horseracing Board created racing information (runners, riders, dates) as part of its normal business. William Hill copied this data for betting. The ECJ ruled the database was *not* protected because the investment was in *creating* the data, not in *collecting existing* data.

This rule has major implications for research: if you generate data through experiments (like running a simulation), the sui generis right may not protect it. If you collect and compile existing data (like a literature database), it likely does.

### Automatic protection, no registration
Unlike patents or trademarks, the sui generis right arises automatically when the investment threshold is met. No registration, no formalities. But the right can be lost if the database is published without access restrictions -- in that case, extraction for research purposes is a privileged use.

### Research exception
Article 9(b) of the Directive allows extraction for research purposes:
- Extraction of a non-substantial part is always allowed
- Extraction of a substantial part for non-commercial research is allowed
- This exception cannot be overridden by contract

### Who owns the right?
The maker of the database is the person or entity that took the initiative and risk of the investment. For university research databases, this is typically the university (the employer), not the individual researchers -- because the university financed the infrastructure and employed the researchers.

### Jurisdiction
The sui generis right is EU-only. There is no equivalent in US law (the US relies on contract law and trade secrets instead). A US company's database is not protected by sui generis rights unless the company is registered in the EU or the database was created in the EU.

## Worked Example

**Case: Toll Collect**
The German Toll Collect GmbH collected truck toll records as a byproduct of operating the toll system. These records were supplied to a payment-service provider, which reused them. The BGH ruled the database was *not* protected because the toll records were generated automatically by the system's operation -- there was no separate "substantial investment" in obtaining the data. The data creation was an automatic consequence of running the toll system.

**Contrast with a weather database:**
If a research institute employs staff to manually collect, clean, and organise weather measurements from hundreds of stations, that *is* a substantial investment in "obtaining" existing data. The database would be protected.

## Common Pitfalls
- **Confusing sui generis with copyright.** Copyright protects creative expression; sui generis protects investment. A database can have both, one, or neither.
- **Assuming all databases are protected.** Only databases with a "substantial investment" qualify. Trivial collections don't.
- **Forgetting the creation/obtaining distinction.** Data you *generate* (through experiments, simulations) may not be protected. Data you *collect* (from existing sources) likely is.
- **Ignoring the research exception.** Non-commercial research extraction is a privileged use that cannot be contractually waived.
- **Thinking it's international.** The sui generis right is EU-only. No US, no Chinese, no Japanese equivalent.

## Connections
- [[legal-frameworks-research-data]] -- the overview of all legal frameworks for research data
- [[fair-data-principles]] -- FAIR's licensing requirement (R1.1) interacts with database rights
- [[hdf5]] -- HDF5 files are databases in the legal sense; their compilation may be protected
- [[data-provenance]] -- documenting who compiled the data supports ownership claims
- [[reproducibility-engineering-sheet-11]] -- IC_11 exercises on sui generis rights (Q10)

## Open Questions
- Does the creation/obtaining distinction survive in the age of automated data collection? (Sensor networks *create* data but also *obtain* measurements from the physical world.)
- How does the proposed EU Data Act (2024) change the landscape for research databases?
- Can a machine learning training dataset claim sui generis protection?
