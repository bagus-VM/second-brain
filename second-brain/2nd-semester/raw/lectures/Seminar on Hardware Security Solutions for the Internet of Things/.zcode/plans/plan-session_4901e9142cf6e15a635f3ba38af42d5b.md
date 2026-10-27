# Content Plan: Sections II–VI (pages 2–6)

All facts below were verified against primary sources this session. Style: succinct, humanizer-clean (no em dashes, no inflation words, plain verbs), every claim cited. Budget: ~5.5 pages of content + references, landing at 6 pages after float spacing.

## Section II — Background (~0.95 page)

**II-A Zero-day fundamentals (~0.3 p).** Definition and lifecycle (private discovery → exploitation → disclosure → patch → value decay), citing NIST CSRC and Ablon & Bogart's RAND study of 200+ zero-day lifespans. Disclosure norms: Project Zero's 90-day deadline (7-day for in-the-wild). Why mobile is special: zero-click delivery and multi-bug chains — GTIG found ~90% of multi-zero-day chains targeted mobile devices.

**II-B Android security architecture (~0.35 p).** AOSP + OEM model: monthly bulletins since Aug 2015 with security patch levels, but OEM adoption optional [source.android.com]. Fragmentation costs: Jones et al. (CCS 2020) measured median 24-day manufacturer/carrier latency; Zhang et al. (USENIX Sec 2021) on kernel patch propagation. Google's countermeasures: Treble (2017), Mainline/modular system components (Android 10, 2019) delivering some fixes via Google Play. Hardware layer: verified boot, TrustZone TEEs, hardware-backed keystore/StrongBox, Titan M chip (blog.google, 2018). Support reality: Pixel 8's 7-year commitment (Oct 2023) vs. the rest of the ecosystem.

**II-C iOS security architecture (~0.3 p).** Vertical integration: single vendor, App Store review, direct OTA updates to all supported devices [Apple Platform Security]. Exploit mitigations: BlastDoor sandbox for Messages (iOS 14, documented by Project Zero + Apple Platform Security), Lockdown Mode (iOS 16, 2022, Apple newsroom), Rapid Security Responses (iOS 16.4, 2023). Hardware layer: boot ROM root of trust, Secure Enclave, PAC (A12, 2018), PPL kernel integrity (iOS 16; superseded by SPTM/TXM on iOS 17).

## Section III — Related Work (~0.6 page)

Three clusters, one sentence of relevance each:
1. **Empirical zero-day studies:** Bilge & Dumitras (CCS 2012, zero-days exploited long before disclosure); Ablon & Bogart (RAND 2017, markets/lifespans); GTIG annual reviews + P0 "0day In the Wild" tracker (a new in-the-wild exploit found every 17 days on average) as the industry corpus.
2. **Platform security:** Faruki et al. (IEEE COMST 2015, Android survey); **Garg & Baliyan (Computer Science Review 2021 — the closest prior work**, a general Android-vs-iOS comparison concluding Android more vulnerable due to fragmented patching).
3. **Hardware/TEE and spyware cases:** Pinto & Santos (ACM CSUR 2019, TrustZone survey); Cerdeira et al. (IEEE S&P 2020, TEE vulnerability SoK); Citizen Lab forensic reports (FORCEDENTRY 2021, Graphite 2025).

Closing differentiation paragraph: Garg & Baliyan's comparison pre-dates 2022–2026 developments (Lockdown Mode, PPL, Mainline maturity, the CSV escalation GTIG documented) and does not quantify in-the-wild exploitation. This paper differs by focusing on zero-days specifically, using post-2022 exploitation data, and adding the hardware-backed-defense dimension.

## Section IV — Implementation: Comparative Framework (~1.0 page)

**IV-A Method (~0.35 p).** Literature meta-analysis protocol: sources (GTIG annual reviews 2023–2026, P0 tracker, Citizen Lab forensic reports, AOSP bulletins, Apple security releases, peer-reviewed studies), window 2019–2026, inclusion criteria (in-the-wild confirmed, or zero-day-relevant empirical finding), extraction schema (CVE, platform, vector, fix version/date, patch reach, hardware involvement).

**IV-B The five-dimension framework (~0.65 p).** Each dimension defined with its measurable indicator. **Table I** (booktabs, ~13 rows): dimension | Android indicator | iOS indicator.

## Section V — Evaluation (~1.15 pages incl. chart)

**V-A In-the-wild exploitation (~0.45 p).** **Table II**: counts by year 2023–2025 — total (97 / 75 / 90, as first reported; footnote: revised to 100 / 78 by later attribution), mobile (17 / 9 / 15), Android (7 / 7), Apple (~6 / 5). **One pgfplots bar chart**: mobile zero-days by year, stacked or grouped Android/Apple where known. Findings: mobile is a minority of totals but the target of nearly all multi-bug chains; iOS draws the most documented mobile exploitation (CSV zero-click); Android's zero-days skew to third-party components (5 of 7 in 2023, 3 of 7 in 2024); 2025 milestone: CSVs attributed more zero-days than state-sponsored groups for the first time; CSVs behind 75% (13 of 17) of Google/Android-ecosystem zero-days in 2023. Case vignettes woven in (2–3 sentences each): FORCEDENTRY (CVE-2021-30860, bypassed BlastDoor, fixed iOS 14.8), Graphite (CVE-2025-43200, fixed iOS 18.3.1), Pixel 9 research chain (CVE-2025-54957, third-party Dolby decoder).

**V-B Applying the framework (~0.45 p).** **Table III**: five dimensions × Android/iOS with qualitative verdicts and the quantitative anchors (24-day median latency vs. direct RSR pushes; optional StrongBox vs. universal Secure Enclave; etc.). Key synthesis: Apple converts patches to protection faster; Android's exposure is dominated by reach (fragmentation) rather than absence of defenses; hardware anchors now exist on both, differing in universality.

**V-C Threats to validity (~0.25 p).** Detection bias (counts = detected exploits only), attribution uncertainty, retroactive count revision, vendor transparency asymmetry, scope limits (mobile OS, not browsers).

## Section VI — Conclusion and Future Work (~0.3 page)

Three findings restated in three sentences; one line of limitations; future work: MTE rollout effects, regulation (EU Cyber Resilience Act) as an update-forcing mechanism, extending comparison to other mobile OSes.

## Bibliography additions (~14 new entries → ~26 total)

bilge2012 (CCS), ablon2017 (RAND RR1751), faruki2015 (COMST 17(2):998–1022), garg2021 (Comput. Sci. Rev. 41:100372), jones2020 (CCS), zhang2021 (USENIX Sec), pinto2019 (CSUR 51(6):130), cerdeira2020 (S&P pp. 1416–1432), marczak2021forcedentry (CL Rep. 143), silvanovich2021blastdoor (P0 blog), gtig2024review (blog.google 2023 review, 97 total), p0tracker (projectzero.google/0day.html), lockdown2022 (support.apple.com/en-us/105120 + newsroom), ppl2024 (Apple "Operating system integrity" page), mainline2019 (developer.android.com / source.android.com), titanm2018 (blog.google Oct 2018), pixel2023support (blog.google 7-years post). Verify-at-write-time: Jones first author name ("Kailani R. Jones" per CCS program — recheck on ACM DL), Bilge & Dumitras headline number (avg ~312 days undetected), Faruki full author list, PAC official Apple source.

## Consistency fix during writing

Introduction currently says "98" for 2023; the 2023 review itself says 97 (each year's own report is the citable number). Change intro to 97 and explain the revision footnote in V-A.

## Implementation steps

1. Add ~14 verified entries to `references.bib` (with the 4 write-time re-verifications via search).
2. Write Section II, compile, check float behavior.
3. Write Sections III + IV with Table I, compile.
4. Write Section V with Table II, Table III, and the pgfplots chart; add `\usepackage{pgfplots}`; compile (MiKTeX auto-installs).
5. Write Section VI; fix intro 97; full recompile.
6. Page-balance pass: target 5.75–6.0 pages; trim order if over: II mitigation lists → vignette lengths → Table III row merge. Expand order if under: vignettes → V-C.
7. Final checks: zero undefined citations, zero overfull boxes, visual pass on all 6 pages, no template boilerplate left.
