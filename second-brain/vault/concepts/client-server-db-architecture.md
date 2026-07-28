---
title: "Client-Server Database Architecture"
tags: [concept, reproducibility-engineering, semester-1, database, client-server, architecture]
course: "Reproducibility Engineering"
source_count: 2
status: current
last_updated: 2026-06-14
prerequisites: ["[[reproducibility-engineering-lecture-6]]", "[[sqlite-architecture]]", "[[docker-compose]]"]
---

## One-line Summary
A client-server database architecture separates the database server (which manages data, accepts queries, and enforces transactions) from the database client (which sends queries and receives results) — typically running on different hosts connected by a network — the dominant model for production databases (PostgreSQL, MySQL, Oracle, SQL Server) and the explicit contrast to SQLite's serverless, file-based model.

## Core Intuition
The lecture's figure (Sheet 6, task 1) labels the two architectures:

**Architecture (a) — File-based (SQLite):**
```
┌─────────────────────────────┐
│      User Application       │
│  ┌─────────────────────┐    │
│  │   SQLite library    │    │
│  └──────────┬──────────┘    │
└─────────────┼───────────────┘
              │ direct file I/O
              ▼
        SQLite file(s)  ← file on disk
```

**Architecture (b) — Client-server (PostgreSQL, MySQL, etc.):**
```
┌──────────────┐    network    ┌─────────────────┐
│ Client host  │◄─────────────►│  Database server│
│  ┌────────┐  │               │  ┌───────────┐  │
│  │  App   │  │               │  │  RDBMS    │  │
│  │+ Client│  │               │  │  process  │  │
│  │  lib   │  │               │  └─────┬─────┘  │
│  └────────┘  │               │        │        │
└──────────────┘               │        ▼        │
                               │  DB file(s)     │
                               └─────────────────┘
```

The key difference: in (a), the application links the DB library and reads/writes the file directly. In (b), a separate server process mediates all access; clients send queries over a network protocol.

## Formal Definition / Statement

### Components
- **DB client library**: the client-side API (e.g., `libpq` for PostgreSQL, `libmysqlclient` for MySQL). Handles connection, query serialisation, result deserialisation.
- **User application**: the program that uses the DB client library. Runs in the client host's process.
- **Network**: TCP/IP (typically) between client and server. The protocol is database-specific (PostgreSQL wire protocol, MySQL protocol).
- **RDBMS (server)**: the database management system process. Manages connections, parses queries, plans execution, manages transactions, enforces ACID, writes to disk.
- **DB file(s)**: the on-disk storage. The server is the only process that touches them directly.

### Communication pattern
1. Client opens a connection to the server (handshake, authentication).
2. Client sends a query (SQL text or prepared statement).
3. Server parses, optimises, executes the query.
4. Server returns results (rows, status, errors).
5. Client processes the results.
6. (For transactions) client sends `BEGIN` / `COMMIT` / `ROLLBACK`.
7. Connection is closed or pooled for reuse.

### The lecture's Docker Compose example
```yaml
services:
  db:
    image: postgres:16
    environment:
      POSTGRES_DB: benchdb
      POSTGRES_USER: lab
      POSTGRES_PASSWORD: labpw
    ports:
      - "5433:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data
  bench:
    image: postgres:16        # same image, used as a client
    depends_on:
      - db
    environment:
      PGPASSWORD: labpw
    command: bash -c "pgbench -i -h db -U lab benchdb && pgbench -h db -U lab -T 30 benchdb"
volumes:
  pgdata:
```

- `db` is the **server** service: `postgres:16` image, port 5432, persistent volume.
- `bench` is the **client** service: same image (reused for `pgbench` binary), connects to `db:5432` (Docker DNS resolves `db` to the server's IP), runs the benchmark.
- The host port mapping `5433:5432` lets the *host machine* connect to the server (on 5433); other containers on the Compose network connect to `db:5432` directly.

## Key Properties / Complexity

### Strengths
- **Centralised data**: one server, one source of truth. Multiple clients can read/write the same data.
- **Concurrent access**: the server manages locking, transactions, isolation. Many clients can write simultaneously (with appropriate isolation).
- **Network access**: clients can be on different machines. The database is a shared resource.
- **Server-side computation**: the server can execute stored procedures, triggers, user-defined functions. Reduces data movement.
- **Authentication and authorisation**: the server can enforce who connects, what they can do. Granular permissions.
- **Backup and recovery**: the server is the natural place to implement backups (consistent snapshots, WAL shipping, point-in-time recovery).

### Weaknesses
- **Operational complexity**: server must be installed, configured, monitored, patched, backed up. Requires a DBA or at least ops expertise.
- **Single point of failure**: if the server goes down, all clients lose access. Mitigated by replication, failover, clustering.
- **Network latency**: every query crosses the network. For high-throughput, low-latency workloads, this is a bottleneck.
- **Configuration drift**: server config, client config, network config — three places where things can go wrong. Reproducibility story is harder than SQLite.
- **Version skew**: client and server must speak the same protocol. Major-version upgrades may break compatibility.

### When to use client-server
- **Production web applications**: many users, many concurrent connections, central data.
- **Multi-user OLTP**: transactions across users.
- **Analytics on shared data**: the server is the natural place to enforce read consistency.
- **Regulatory requirements**: data must be controlled at a central location (audit, encryption, access control).
- **Big data**: server-side parallelism (parallel queries, partitioning, sharding).

### When to use SQLite instead
- **Embedded applications**: mobile apps, IoT devices, desktop apps.
- **Single-user data analysis**: the analyst's local file.
- **Reproducible research**: one file, one source, no configuration.
- **Test fixtures**: fast to spin up, easy to throw away.
- **Application file format**: Firefox, Chrome, macOS use SQLite as their file format.

## Worked Example

A simple client-server database experiment:

```bash
# On the server host (or as a Docker container):
$ postgres -D /var/lib/postgresql/data
# Listens on port 5432
# Ready to accept connections

# On the client host:
$ psql -h db.example.com -U alice -d mydb
Password: ******
mydb=> SELECT count(*) FROM measurements;
 count
-------
  1000
(1 row)
```

The client (`psql`) connected to the server (running on `db.example.com`, port 5432), authenticated as `alice`, ran a query, got a result. The server did all the parsing, planning, execution, and disk I/O.

To make this reproducible, you need to pin:
- The server version (`postgres:16` vs `postgres:15`)
- The server configuration (postgresql.conf)
- The client version (libpq)
- The schema (DDL)
- The data (dumps or replication)

Compare to SQLite: the *file* is the entire reproducibility artifact.

## Common Pitfalls
- **"The network is fast, so client-server is as fast as SQLite"**: the network latency is a constant overhead, not bandwidth. Even a localhost connection has microsecond-scale overhead that SQLite's direct file I/O avoids.
- **Forgetting the server is stateful**: closing a connection doesn't lose data, but restarting the server with the wrong config can. Always back up before config changes.
- **Confusing "client library" with "client application"**: the client library is the *API* (e.g., `libpq`); the client application is the *user* of that API. The lecture's `pgbench` is an application that uses `libpq`.
- **Connection pooling mistakes**: opening a new connection per query is expensive. Use a pooler (pgbouncer, pgpool, application-side pool). Connection leaks bring the server down.
- **Version skew**: client `libpq` 14 can't talk to server `postgres:16` for some advanced features. Pin both sides.
- **Reusing the same Docker image for server and client**: the lecture does this (both services use `postgres:16`). It works because the `pgbench` binary is in the image. In a real architecture, the client and server might run on different bases.

## Connections
- [[reproducibility-engineering-lecture-6]] — the lecture
- [[sqlite-architecture]] — the contrast
- [[docker-compose]] — the standard way to deploy multi-service DB setups
- [[foreign-tables-postgresql]] — a server-side integration technique
- [[reproducibility-engineering-lecture-6]] — the architecture overview

## Open Questions
- For very high-throughput workloads, can client-server match the latency of in-process databases? (Yes, with prepared statements, binary protocols, and connection pooling. SQLite still wins for single-process scenarios.)
- How do you make a client-server DB setup *reproducible* across machines? (Pin the server version, the config, the schema, the data. Use infrastructure-as-code: Terraform, Ansible, Pulumi. Version the config.)
- For serverless deployments (Lambda, Cloud Functions), is the client-server model still right? (Yes — the function connects to a managed serverless DB like Aurora Serverless. The "server" is invisible but still there.)
