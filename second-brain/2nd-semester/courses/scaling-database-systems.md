---
title: "Scaling Database Systems"
tags: [course, semester-2, scaling-database-systems]
professor: "Prof. Dr.-Ing. Stefanie Scherzinger"
semester: "WS 2026/27"
exam_date: "TBD"
credits: "TBD"
language: "not stated in the ingested sheets"
source_count: 4
status: active
last_updated: 2026-10-20
prerequisites: []
---

## One-line Summary
A project course in which students build miniHive, a minimalistic version of Hive, on the command line in Python, test it in a Docker container, and hand in milestones through Praktomat.

## Course Information

- **Chair:** Scalable Database Systems, University of Passau
- **Instructor:** Prof. Dr.-Ing. Stefanie Scherzinger
- **Teaching staff:** Stefan Klessinger, Christoph Koehnen
- **Term:** Winter Term 2026/27, language English
- **Platforms:** Stud.IP for news, sheets, and the forum; Praktomat for submissions; Docker for testing
- **Exam date, credit points:** not stated in the ingested material

The four ingested sources are organisational: prerequisites, exercise scheduling, Docker server instructions, and Praktomat. The `raw/lectures/Scaling Database Systems/Vorlesung/` directory exists but is empty, so no lecture slides have been ingested — only `Ubung/` material. The technical content of the course — what "scaling database systems" means here — is therefore not in the vault.

## Exercise Organisation

Three groups, each covering the same content, starting 21/22 October 2026.

| Day | Time | Room |
|-----|------|------|
| Wednesday | 12:15 – 13:45 | (ITZ) SR 004 |
| Thursday | 14:15 – 15:45 | (ITZ) SR 001 |
| Thursday | 16:00 – 17:30 | (ITZ) SR 004 |

- Students assign themselves to one group; sign-ups open from 16 October 2026 at 14:00 and close 20 October 2026 at 23:59.
- Each group is capped at 30 students.
- Bring your own device to the sessions.
- The first sheet appears in Stud.IP on 20 October at 18:00 and is worked on *during* the first session.
- From the second sheet on, the material appears in Stud.IP at 18:00 on the Friday before, and is worked on *before* the session.
- Questions outside sessions go to the Stud.IP forum, so all students benefit from the answer.

## The Project - miniHive

The prerequisites sheet states the following, and nothing else:

- The course builds **miniHive**, a minimalistic version of Hive.
- The work makes extensive use of the command line (terminal) and Python.
- A Docker container is provided to test the implementation.
- Required skills: basic Bash command line usage, concept and basic usage of Git, basic usage of SSH.
- The Bash requirement is not optional: the miniHive container has **no graphical user interface**.
- Recommended hardware: at least 8 GiB of main memory to run the miniHive Docker container.
- Reference material given in the sheet: a Bash playlist, the Udacity *Version Control with Git* course, and the Passau FIM page on SSH.
- Technical problems on your own device get limited support, because every machine has a different environment, operating system, and installed applications. Questions go to the Stud.IP course forum; check for an existing answer first, and state your operating system and the failed command.

Milestones are submitted through Praktomat and must not be made public: no milestone code in the Stud.IP forum, no upload into a public GitHub repository. Plagiarism affects the creator and the one who copies.

What miniHive contains internally, how it interfaces, and how the milestones break down is lecture material, not yet ingested.

## Tooling and Submission

**Docker.** A container is provided to test milestone implementations. Either install Docker locally per <https://docs.docker.com/get-docker/> and verify with the hello-world image, or use the course server — which requires an access application.

**The server, narrow-sea.** Purpose: an identical setup for all participants regardless of local OS. It requires a FIM account, different from the ZIM account used for Stud.IP; create it via the Passau FIM accounts page, which may itself require a VPN. Send your FIM account name from your university email to `sds-tutorials@uni-passau.de` with the subject "Docker Server Access" by 19 October 2026. The server is reachable only from within the university network, so from home you need a VPN.

- FQDN: `narrow-sea.sdbs.fim.uni-passau.de`
- Fingerprint: `SHA256:wLGEIY3qWqGa5va/OEDCizygRctc5Evrflwx3X7XCwQ`
- Command: `ssh <FIM-account-name>@narrow-sea.sdbs.fim.uni-passau.de`

Client-side notes: Windows users may have to activate the OpenSSH feature; Linux and macOS users may have to install `openssh`; do not forget the `sdbs` subdomain; FIM accounts expire and may need reactivation. On the server, Docker is pre-installed in rootless mode — each user has their own daemon — and you must run `systemctl --user start docker` on every connection. The FIM terms apply on narrow-sea as well. Because hardware is shared, execution times vary with load: postpone work to a quieter time, but keep the deadlines; coordinating your work is your own responsibility.

**Praktomat.** All submissions, milestones included, go through Praktomat, reachable only from inside the Passau network (VPN from outside) at <https://praktomat.sdbs.fim.uni-passau.de>. Select the course "Scaling Database Systems" in "Wintersemester 26/27". Praktomat is not integrated with university authentication, so a separate account is needed, and each instance has its own accounts: register again for this instance even if you had an older one. Registration requires username, first name, last name, email address, matriculation number, password, and password confirmation — all mandatory. Only email addresses of the form `ZIM-name@ads.uni-passau.de` are accepted. A confirmation email with an activation link is sent; on first login you accept a disclaimer with the declaration of authenticity and the data privacy statement.

Each exercise shows its deadline; after it, submission is impossible, and email or paper submissions are not accepted. Praktomat checks submissions automatically but assigns no grades, so ignore the Result Overview. On the exercise detail page, My Solutions shows previous submissions and accepts a new one. Use the exact filename the exercise description specifies — a wrong filename is a rejection reason. You may submit as often as you like before the deadline; the Final Solution is your most recent submission that passed all required tests, and a later failing submission does not replace a previously accepted one.

## Lecture Index

| # | Sheet | Source file | Status |
|---|-------|-------------|--------|
| 1 | Prerequisites | `prerequisites.txt` | ingested |
| 2 | Exercise Sessions (Kickoff) | `sds_kickoff_exercises.txt` | ingested |
| 3 | Docker Server Instructions | `docker_server_instructions.txt` | ingested |
| 4 | Praktomat | `praktomat.txt` | ingested |

No lecture slides have been ingested for this course; `raw/lectures/Scaling Database Systems/Vorlesung/` is empty, and only `Ubung/` material exists. The four sheets above are organisational, and the concept pages built on them cover structure, tooling, and workflow.

## Open Questions

- Exam date, exam format, credit points, and grading scheme are not in the ingested material. Nothing is guessed; the frontmatter fields stay at "TBD".
- The milestone list, its structure, and how milestones contribute to the grade are likewise absent.
- No lecture content has been ingested. Nothing about sharding, replication, query processing, consistency, or any other database topic appears in the source, and none is asserted on the linked pages.
- It is unknown whether the first sheet was worked on in the session of 21/22 October.
- The contents of the sheets are unknown: they arrive through Stud.IP at fixed times, and only their publication schedule and role are known here.
- Whether students collaborate on a milestone, and how Git is used across a group, is not stated.
