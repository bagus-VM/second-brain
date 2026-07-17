---
title: "In-Class Exercise Sheet 11: FAIR Principles & Legal Aspects of Research Data"
tags: [practice, reproducibility-engineering, semester-1]
course: "Reproducibility Engineering"
status: current
last_updated: 2026-07-17
---

# In-Class Exercise Sheet 11: FAIR Principles & Legal Aspects of Research Data

Based on:
- Wilkinson, M.D. et al. "The FAIR Guiding Principles for scientific data management and stewardship" (Nature, 2016)
- Beurskens, M. & Scherzinger, S. "Legal Perspectives on Research Data Storage" (Datenbank-Spektrum, 2023)
- Beurskens, M. & Scherzinger, S. "Datenbankherstellerrecht und Datenbankforschung" (Datenbank-Spektrum, 2024)

## 1 FAIR Scope

> [!note]- Solution
> The FAIR Guiding Principles apply to:
> - **Research data** -- yes, this is the primary target
> - **Algorithms used to process or analyze the data** -- yes
> - **Software tools used in the research process** -- yes
> - **Workflows that led to the data** -- yes
> - **Physical laboratory equipment** -- no. FAIR applies to *digital* research artefacts, not physical equipment.
>
> The principles explicitly target "digital research objects" -- data, algorithms, tools, and workflows all qualify.

## 2 FAIR Stakeholders

> [!note]- Solution
> All of the listed options are stakeholders:
> - **Researchers who conducted the original work** -- they produce and describe the data
> - **Researchers who want to reuse each other's data** -- they are consumers of FAIR data
> - **Professional data publishers** -- they make data discoverable and accessible
> - **Funding agencies** -- they increasingly mandate FAIR compliance
> - **Computational agents that discover and process data** -- this is a key design goal of FAIR: machines should be able to autonomously find, access, and reuse data without human intervention
>
> The inclusion of computational agents as stakeholders is what distinguishes FAIR from earlier data management guidelines. FAIR is designed for *machine-actionable* data.

## 3 Central Goal of FAIR

> [!note]- Solution
> A central goal of the FAIR Guiding Principles is that digital objects should be **machine-actionable**, enabling **computational agents** to autonomously discover, interpret, access, and reuse data.
>
> The word "autonomously" is key -- FAIR doesn't just make data human-readable, it makes data machine-readable with minimal human intervention.

## 4 Data Stewardship Strategy

> [!note]- Solution
> **Adopt general-purpose, open interoperability standards.**
>
> The other options are wrong because:
> - Bespoke parsers create fragmentation, not interoperability
> - Restricting repository types reduces accessibility
> - Requiring every tool to support every format is impractical
>
> FAIR emphasizes that (meta)data should use "a formal, accessible, shared, and broadly applicable language for knowledge representation" -- that's the open standards approach.

## 5 The Four FAIR Categories

> [!note]- Solution
> **(a) To be Findable:**
> - (Meta)data are assigned a globally unique and persistent identifier
> - Data are described with rich metadata
> - Metadata clearly and explicitly include the identifier of the data they describe
> - (Meta)data are registered or indexed in a searchable resource
>
> **(b) To be Accessible:**
> - (Meta)data are retrievable by their identifier using a standardized communications protocol
> - The protocol is open, free, and universally implementable
> - The protocol allows for authentication and authorization where necessary
> - Metadata remain accessible even when the data are no longer available
>
> **(c) To be Interoperable:**
> - (Meta)data use a formal, accessible, shared, and broadly applicable language for knowledge representation
> - (Meta)data use vocabularies that themselves follow the FAIR principles
> - (Meta)data include qualified references to other (meta)data
>
> **(d) To be Reusable:**
> - (Meta)data are richly described with accurate and relevant attributes
> - (Meta)data are released with a clear and accessible data usage license
> - (Meta)data are associated with detailed provenance
> - (Meta)data meet domain-relevant community standards

## 6 FAIR Category Assignment

> [!note]- Solution
> **(a)** "Released with a clear and accessible data usage license" -> **Reusable**
> (A license tells others *how* they can reuse the data.)
>
> **(b)** "Assigned a globally unique and persistent identifier" -> **Findable**
> (You can't find data without a stable identifier to look up.)
>
> **(c)** "Use commonly adopted, accessible, and preferably open standards and formats" -> **Interoperable**
> (Standards enable different systems to work with the same data.)
>
> **(d)** "Metadata remain accessible even when the data are no longer available" -> **Accessible**
> (Accessibility persists even when the data itself is gone -- the metadata survives.)

## 7 Legal Framework Matching

> [!note]- Solution
> - **(a) Data protection (GDPR)** -> **(d)** A spreadsheet contains personal information about identifiable living individuals
> - **(b) Company keeps customer list confidential using NDAs** -> **(e) Trade secret protection** -- NDAs and access restrictions are the classic mechanism for protecting trade secrets
> - **(c) Copyright** -> **(f)** A research article reproduces an original figure published in a textbook -- the figure is a copyrightable creative work
> - **(d) None of the above** -> **(h)** A database contains only publicly available weather measurements -- no personal data (no GDPR), no creative expression (no copyright), no confidential information (no trade secret), and weather data isn't inherently protected
>
> Note: (g) is not a scenario but a category option. The remaining scenario is (b) the NDA/customer list case, matched to trade secret protection.

## 8 Copyright Protection for Database Artifacts

> [!note]- Solution
> **(a) Database schema (sufficiently original)** -> **Copyright**
> A schema can be a creative literary work if it reflects original choices in structuring data.
>
> **(b) Complex stored procedure or UDF** -> **Copyright**
> Software source code is protected by copyright as a literary work.
>
> **(c) Original graphical user interface (GUI)** -> **Copyright**
> An original GUI is a creative work (visual art + code).
>
> **(d) Original web API** -> **Copyright**
> An API design involves creative choices in interface structure (though this is legally debated -- see Oracle v. Google).
>
> **(e) Image of Bart Simpson stored as BLOB** -> **Copyright**
> The image is a copyrighted artistic work (owned by its creator/Fox). Storing it in a database doesn't change its copyright status.

## 9 Database Schema Copyright

> [!note]- Solution
> **(a)** Two attributes `firstName` and `lastName` -> **No**
> This is a trivial, obvious way to store names. It lacks the "originality" required for copyright protection. Any developer would design it the same way.
>
> **(b)** Novel schema partitioning Germany into 1,860 carefully crafted geographical regions -> **Yes**
> The deliberate, creative partitioning of Germany into 1,860 specific regions reflects original intellectual effort. This is not a trivial or obvious design choice -- it required domain expertise and creative judgment.

## 10 Sui Generis Database Right

> [!note]- Solution
> This right is called the **sui generis database right** (EU Database Directive 96/9/EC).
>
> It protects the *investment* in obtaining, verifying, or presenting the contents of a database -- not the creative expression (that's copyright) but the substantial effort and expense of compiling the data.
>
> **(a) BHB v. William Hill** -> **The database was NOT protected.**
> The European Court of Justice ruled that the *creation* of data (organizing horse races, selecting participants) is not "obtaining" existing data. The BHB created the data as part of its normal business activity. The sui generis right protects investment in *collecting existing data*, not in *generating new data*.
>
> **(b) Toll Collect** -> **The database was NOT protected.**
> The BGH ruled that the toll records were generated as a byproduct of the toll system's operation, not obtained through substantial separate investment. The data creation was an automatic consequence of running the system.
>
> **(c) University research database** -> **The university, because it made the substantial investment.**
> The sui generis right belongs to the party that made the substantial investment in obtaining/verifying/presenting the data -- in this case, the university that financed the infrastructure and employed the researchers.
>
> **(d) Actions that can violate the right:**
> - Extracting a single record -> **No** (not a "substantial part")
> - Repeatedly extracting individual records until effectively copied -> **Yes** (systematic extraction constitutes a substantial part)
> - Extracting all records -> **Yes** (clearly a substantial part)
>
> The key: individual extraction is fine; systematic or bulk extraction violates the right.
>
> **(e) US company, no license agreement** -> **Yes, can claim protection.**
> The sui generis right applies to databases created by EU nationals/residents or companies registered in the EU. But the question says a US company -- the sui generis right is an EU right. However, the US company could claim protection *in the EU* if they made a substantial investment. The lack of a license agreement doesn't waive the right (unlike copyright, the sui generis right exists automatically).
>
> Wait -- re-reading: a US company that puts a database on their website. The sui generis right is EU-only. In the US, there is no equivalent. So: **Yes** if claiming in the EU (if they meet the investment threshold), but the right is limited to EU jurisdictions.
>
> **(f) German institution, US company copies** -> **Yes.**
> The German institution made the substantial investment. The sui generis right is an EU right that protects against unauthorized extraction/reutilization. The fact that the copier is in the US doesn't matter -- the database was created in the EU and the right applies. The lack of a license agreement doesn't waive the right.
>
> **(g) French research team reproduces for comparison** -> **No risk of violation.**
> The Database Directive includes exceptions for research and educational use. Extracting data for scientific research purposes (reproduction for comparison) falls under the privileged use exception. The French team's use is non-commercial and for scientific purposes.

## 11 Label the Overview Chart

> [!note]- Solution
> The chart shows stakeholders in research data storage: Data Providers, Researchers, Data Repositories, Interested Third Parties.
>
> **Stakeholder roles:**
> - **Data Providers** -- individuals who supply personal data (health records, survey responses)
> - **Researchers** -- the team conducting the study
> - **Data Repositories** -- institutional or third-party storage services
> - **Interested Third Parties** -- other researchers, funding agencies, the public
>
> **Labels for the relationship framework:**
> - Between Data Providers and Researchers: **Consent or License** / **Privacy** (GDPR applies to personal data)
> - Between Researchers and Data Repositories: **Contract Terms** / **Terms of Use**
> - Across all stakeholders: **Attribution** / **Restricted Use** / **Privileged Use**
> - Researchers own the **Copyright in Structure** (database schema) and **Copyright in Software**
> - Data Providers retain **Privacy** rights (GDPR)
> - The database contents may have **sui generis rights**
> - **Trade Secrecy** may apply to proprietary datasets
> - **IP Rights** cover the overall intellectual property landscape
> - **Cross-Cutting Concerns: Security, Compliance, Availability** apply horizontally
>
> The key insight: research institutions sit at the center, contracting with repository providers and managing consent/licenses with data providers. Legal protection is layered -- copyright for creative elements, sui generis for the database investment, GDPR for personal data, trade secrecy for confidential business data.

## Related Lectures
- [[reproducibility-engineering-lecture-8]] -- HDF5 and data formats (data interoperability connects to FAIR)
- [[reproducibility-engineering-lecture-10]] -- artifact packaging (FAIR applies to research artifacts)
- [[fair-data-principles]] -- concept page for FAIR
- [[legal-frameworks-research-data]] -- concept page for legal frameworks
- [[sui-generis-database-right]] -- concept page for the EU database right
