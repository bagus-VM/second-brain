---
title: "Reproducibility Engineering Sheet 7 — BenchBase Lab Flashcards"
tags:
  - flashcards
  - reproducibility-engineering
  - semester-1
  - benchmarking
  - docker-compose
course: "Reproducibility Engineering"
status: current
last_updated: 2026-06-19
---

# Flashcards — Exercise Sheet 7 (BenchBase Lab: SQLite vs PostgreSQL)

> [!question]- What is BenchBase, and what is it a port of?
> [!answer]- BenchBase is a Java-based benchmarking framework for database systems. It is a port of YCSB (Yahoo! Cloud Serving Benchmark), which was originally written in Java and targeted at NoSQL databases. BenchBase extends YCSB to support SQL databases (SQLite, PostgreSQL, MySQL/MariaDB, etc.).

> [!question]- What are the three YCSB workloads used in the exercise, and what do they measure?
> [!answer]- **Read-only**: 100% reads — measures read throughput. **Mixed**: 50% reads, 50% updates — measures mixed read/write throughput. **Write-only**: 100% inserts — measures write throughput. These workloads stress different aspects of the DBMS: caching (read-only), concurrency control (mixed), and disk I/O (write-only).

> [!question]- In the throughput comparison, why is PostgreSQL faster than SQLite for read-only and mixed workloads, but the same for write-only?
> [!answer]- **Read-only**: PostgreSQL has a more sophisticated buffer pool and query optimizer, giving it ~1.9× faster read throughput. **Mixed**: PostgreSQL's MVCC (multi-version concurrency control) handles concurrent reads and writes better, giving it ~2.4× faster mixed throughput. **Write-only**: both DBMS hit the same ~10,000 ops/s limit, suggesting the bottleneck is disk I/O, not the DBMS.

> [!question]- What is a multi-stage Docker build, and why is it used in the BenchBase Dockerfile?
> [!answer]- A multi-stage build uses multiple `FROM` instructions in a Dockerfile. Each stage can copy artifacts from previous stages. In the BenchBase Dockerfile, the first stage (maven:3.9-eclipse-temurin-21, ~800 MB) compiles the JAR. The second stage (eclipse-temurin:21-jre, ~200 MB) copies only the JAR. This reduces the final image size from ~800 MB to ~200 MB, making it faster to pull, smaller to store, and more secure (fewer attack surfaces).

> [!question]- What is the difference between the SQLite and PostgreSQL Docker setups in the exercise?
> [!answer]- **SQLite**: a single container runs the BenchBase client, which links the SQLite library and reads/writes a local file. No server process. **PostgreSQL**: two containers — a PostgreSQL server and a BenchBase client — connected over a Docker network. The client connects to the server via JDBC. This is the [[sqlite-architecture|embedded]] vs [[client-server-db-architecture|client-server]] architecture comparison.

> [!question]- Why does the PostgreSQL Docker Compose file use a `healthcheck` and `depends_on: condition: service_healthy`?
> [!answer]- The `healthcheck` runs `pg_isready` every 2 seconds to check if PostgreSQL is ready to accept connections. The `depends_on: condition: service_healthy` ensures the BenchBase client waits for PostgreSQL to be *ready*, not just *started*. Without this, the client might try to connect before PostgreSQL is ready, causing a connection error.

> [!question]- What is a PostgreSQL foreign table, and when is the source file actually read?
> [!answer]- A foreign table is a table-like object whose rows are read on demand from an external source (a file, a remote DB, a web service) through a Foreign Data Wrapper (FDW). The source file is *not* read at `CREATE FOREIGN TABLE` time — only when a query is run against the table. This lazy validation is by design (the file might appear later) but can surprise new users who expect the table creation to fail if the file doesn't exist.

> [!question]- What makes a SQL query non-reproducible, and how do you fix it?
> [!answer]- A query is non-reproducible if it can return different results on the same data. Common causes: `ORDER BY RANDOM()` (different order each time), `LIMIT` without `ORDER BY` (arbitrary row selection), `NOW()` or `CURRENT_TIMESTAMP` (time-dependent), non-deterministic functions (e.g., `UUID_GENERATE_V4()`). Fix: use deterministic queries — explicit `ORDER BY` on a unique key, no time-dependent functions, no random ordering.

> [!question]- What is MVCC, and why does it give PostgreSQL an advantage in mixed workloads?
> [!answer]- MVCC (Multi-Version Concurrency Control) is a concurrency control method where each transaction sees a snapshot of the database at a point in time. Readers don't block writers, and writers don't block readers. PostgreSQL uses MVCC, so read-heavy and mixed workloads can proceed concurrently without locking. SQLite uses file-level locking, so readers and writers can block each other, reducing throughput in mixed workloads.

> [!question]- Why is the write-only throughput the same for SQLite and PostgreSQL (~10,000 ops/s)?
> [!answer]- The write-only throughput is bounded by disk I/O, not the DBMS. Both SQLite and PostgreSQL are writing to disk at the same rate, so they hit the same limit. The bottleneck is the disk, not the DBMS. To increase write throughput, you would need faster storage (SSD, NVMe) or a different benchmark configuration (e.g., batch inserts, asynchronous commits).
