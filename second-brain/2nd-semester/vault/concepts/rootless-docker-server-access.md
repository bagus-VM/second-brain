---
title: "Rootless Docker and the narrow-sea Server"
tags: [concept, scaling-database-systems, semester-2, infrastructure, docker]
course: "Scaling Database Systems"
source_count: 1
status: current
last_updated: 2026-10-20
prerequisites: ["[[scaling-database-systems]]"]
---

## One-line Summary
narrow-sea is the course's shared Docker host, reachable only from inside the university network, where each student runs their own rootless Docker daemon instead of installing Docker locally.

## Core Intuition

The security argument is implicit in the sheet and worth making explicit, because it is what makes
the fingerprint load-bearing.

**The fingerprint exists because the server is a shared, privileged resource.** narrow-sea is a
multi-user machine, reachable by every student in the course, sitting inside the university
network. The SSH host key is the only thing binding your client to *that* machine. A
man-in-the-middle on a shared network path could present a key of its own and receive your
credentials, your uploads, and your milestone code. The SHA256 fingerprint is quoted in the sheet
so that the first connection can be checked against a value published out of band, rather than
trusted because the client proposed it. A client that accepts the first key it is offered has no
security property at all; it has convenience.

**Rootless is what keeps students apart.** Docker is pre-installed in rootless mode, and the sheet
states: "Each user has their own Docker daemon." Your containers run under your own account, in
your own namespace, with your own storage and network stack. One student's container cannot see
another's filesystem, cannot join another's network namespace, and cannot stop another's daemon,
because it does not run as root and does not control the other daemon. With one root-owned
daemon, every student would share a container runtime, a set of networks, and a set of privileges -
isolation would be a convention rather than a mechanism. Rootless turns isolation from policy into
a property the operating system enforces.

This also explains the per-connection step. `systemctl --user start docker` starts *your* daemon,
in *your* session, as *your* user - and it has to run every time, because a user-level daemon is
scoped to your login session and does not survive it. The command is not a workaround; it is the
design.

## Formal Definition / Statement

The mechanics as stated by the Docker Server Instructions sheet, in the sheet's own order:

- **Purpose.** Docker ensures "that all participants have an identical setup, regardless of their
  local operating system and environment." Run it locally and you can ignore this sheet; otherwise
  narrow-sea is provided, with Docker pre-installed.
- **Shared hardware.** "As hardware resources are shared, execution times may vary." Postpone a
  slow run until the load is lower - but "keep the deadlines in mind", because coordinating your
  work to meet the project deadlines is "your own responsibility".
- **Terms.** "The terms and conditions you signed for your FIM account also apply on narrow-sea."
- **Account requirement.** You need a FIM account, and "the FIM account is different from your ZIM
  account, which is used, e.g., for Stud.IP." It is created via the FIM accounts page, and VPN may
  be required to access that page.
- **Access application.** "Send your FIM account name from your university email address to
  sds-tutorials@uni-passau.de with the subject 'Docker Server Access' by October 19, 2026."
- **Reachability.** "The Docker server can only be accessed from within the university network. To
  access the server from your home, you need to setup a VPN connection."
- **Identity check.** "For security reasons, please confirm that your connection matches the
  following data": FQDN `narrow-sea.sdbs.fim.uni-passau.de`, fingerprint
  `SHA256:wLGEIY3qWqGa5va/OEDCizygRctc5Evrflwx3X7XCwQ`.
- **Connection command.** `ssh <FIM-account-name>@narrow-sea.sdbs.fim.uni-passau.de`.
- **Client-side notes.** Windows users need to activate the OpenSSH feature if the command fails in
  the Windows terminal; Linux and macOS users may need the `openssh` package if `ssh` is
  unrecognized. FIM accounts expire after some time and may need reactivation via FIM AMS. If you
  still cannot connect, check the FQDN - "do not forget the sdbs subdomain in the FQDN".
- **Rootless model.** "Docker is pre-installed on narrow-sea in rootless mode. Each user has their
  own Docker daemon. Once connected to the server, you need to activate the Docker daemon."
- **Activation.** "Execute the following command to spawn the Docker service every time you connect
  to the server:"
  `systemctl --user start docker`
- **Verification.** "To confirm that the environment is set up correctly, run the hello-world image
  as described in the Docker documentation."

## Key Properties

- **A shared machine, not a dedicated one.** Hardware is pooled, so execution time depends on the
  load from other students. That is a property of the resource, not a defect to be reported.
- **The FIM account is a second identity.** Not the ZIM account used for Stud.IP, created
  separately, possibly needing VPN to reach its own page, and expiring.
- **Access is granted by a manual application** sent from a university email address, with a
  specified subject line and a stated deadline. The server does not grant access on account
  creation.
- **Network-local by design.** From home, VPN is not optional.
- **The host identity is published and checkable.** FQDN plus SHA256 fingerprint, so the client can
  be bound to a specific host.
- **Verification is a single command.** hello-world confirms the environment end to end.

## Worked Example

A student's first session, in the order the sheet imposes.

**Step 1 - get the account and the access.** The student already has a ZIM account for Stud.IP.
That account is the wrong one here, so they open the FIM accounts page - VPN may be required even
for this, since the page may sit outside the direct network path - and create a FIM account. From
their university email address they then write to `sds-tutorials@uni-passau.de` with the subject
"Docker Server Access" and state the account name. The deadline is 19 October 2026, one day before
the exercise group sign-up closes and before the first session on 21/22 October. A late application
risks not having access when the first exercise session happens. On Windows the client also needs
the OpenSSH feature active; on Linux or macOS, an unrecognized `ssh` means the `openssh` package is
missing.

**Step 2 - connect from inside the network.** On campus, the student runs
`ssh <FIM-account-name>@narrow-sea.sdbs.fim.uni-passau.de`. Dropping the `sdbs` subdomain produces
a name that does not resolve, and the sheet names that specific mistake. On the first connection
the client presents a host key, and the student checks it against the published fingerprint
`SHA256:wLGEIY3qWqGa5va/OEDCizygRctc5Evrflwx3X7XCwQ`. Match: proceed. Mismatch: stop - the sheet's
"for security reasons, please confirm" is not decorative. From home, the student brings up the
university VPN first; without it the host is unreachable.

**Step 3 - start the daemon and verify.** Immediately after connecting, the student runs
`systemctl --user start docker`, then the hello-world image. The output confirms the daemon is up,
the image pull path works, and the runtime is functioning. Only now is the environment usable for
the miniHive test container described in [[minihive-project-structure]].

**Step 4 - work under load.** The server is busy; a build that took a minute on a laptop takes
several. The student's response, per the sheet, is to postpone that particular run until the load
is lower - and to keep the deadline in view while doing so. Months later the FIM account expires
and access fails with an authentication error rather than a network error; the student reactivates
the account via FIM AMS and connects again.
## Common Pitfalls

- **Confusing the FIM account with the ZIM account.** They are different credentials. The ZIM
  account serves Stud.IP; the FIM account serves narrow-sea. Using the wrong one fails
  authentication and looks like a server problem, and the account also expires after some time and
  may need reactivation by you via FIM AMS.
- **Getting the host name wrong.** `narrow-sea.fim.uni-passau.de` is not the host - the `sdbs`
  subdomain is required, and the sheet names that as a first thing to check when the connection
  fails. From home the server is also unreachable without VPN, so the attempt fails at the network
  layer rather than at authentication.
- **Forgetting `systemctl --user start docker`.** A fresh session has no daemon, and the failure
  that follows is a Docker client error about not being able to reach the daemon. It looks like a
  broken server; it is a service that was never started. Skipping hello-world is the same mistake
  one step later: the check costs seconds and localises a broken environment immediately.
- **Skipping the fingerprint check.** The only thing binding you to the real narrow-sea is the
  host key. Accepting whatever key is offered makes the SSH layer decorative.
- **Late access application.** The deadline is 19 October 2026 and the first session is 21/22
  October. No turnaround time is stated, so the buffer is thin.
- **Treating a slow run as a broken build.** Execution times vary with shared load. Postpone the
  run; do not hunt for a bug that is queueing. The deadline does not move with the load - the sheet
  places that coordination on you. The FIM terms also apply on the server, not merely on the
  account itself.
## Connections

- [[scaling-database-systems]] - the course page; this infrastructure exists for its milestones.
- [[minihive-project-structure]] - the project whose implementation is tested in the container.
- [[praktomat-submission-workflow]] - where tested milestone code is submitted; also university-network-bound.
- [[containerization-for-builds]] - the general practice the course's test container instantiates.
- [[multi-stage-docker-build]] - how a test image is assembled from several layers.
- [[reproducible-builds]] - the reason a fixed shared environment is worth the access procedure.

## Open Questions

- **The server's hardware is unspecified.** Nothing states CPU model, core count, RAM, storage type,
  or how many students are expected to share it. Only that hardware resources are shared.
- **The rootless implementation details are unstated.** The sheet names "rootless mode" and "each
  user has their own Docker daemon" but does not name the mechanism (rootless Docker, Podman, or a
  user-namespace wrapper), the `systemd` user unit details, or the storage driver. Nor is it stated
  whether ingress or privileged containers are available - which determines whether a milestone can
  bind a port or mount a volume.
- **The FIM account expiry period is unknown.** The sheet says accounts "expire after some time"
  without a duration or reactivation interval, and does not say whether the FIM accounts page always
  needs VPN or only from outside the network. The access-granting procedure after the email is also
  unstated: automatic, by reply, or by a manual list update, and with what turnaround time.
- **Whether a quota or resource limit applies per user** (CPU time, memory, container count) is not
  stated, though the rootless model suggests per-user limits exist.
- **Whether a local-Docker student and a narrow-sea student can exchange artefacts** is not
  addressed, and it bears on whether "identical setup" really holds across both paths. What happens
  to stored containers and images after the term is also unstated.
