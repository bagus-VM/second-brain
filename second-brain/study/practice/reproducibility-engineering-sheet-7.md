---
title: "Exercise Sheet 7 — BenchBase Lab: SQLite vs PostgreSQL"
tags:
  - practice
  - reproducibility-engineering
  - semester-1
  - benchmarking
  - docker-compose
  - sqlite
  - postgresql
course: "Reproducibility Engineering"
status: current
last_updated: 2026-06-19
---

# Exercise Sheet 7 — BenchBase Lab: SQLite vs PostgreSQL

## Overview
The task is to compare the performance of an embedded DBMS ([[sqlite-architecture|SQLite]]) vs a client-server DBMS (PostgreSQL) using the BenchBase benchmarking framework (a Java port of YCSB — Yahoo! Cloud Serving Benchmark). The exercise explores how deployment architecture affects throughput, and how Docker can be used to make the comparison reproducible.

## Tasks

### 1. BenchBase with SQLite (embedded)

**Setup**: Build a Docker image for BenchBase with SQLite support. The image includes the BenchBase JAR, the SQLite JDBC driver, and a workload configuration.

**Dockerfile** (simplified):
```dockerfile
FROM maven:3.9-eclipse-temurin-21 AS build
WORKDIR /app
RUN git clone https://github.com/benchbase-io/benchbase.git .
RUN mvn -q -pl sqlite -am package -DskipTests

FROM eclipse-temurin:21-jre
COPY --from=build /app/sqlite/target/benchbase-sqlite.jar /benchbase.jar
COPY config/sqlite /config
WORKDIR /results
ENTRYPOINT ["java", "-jar", "/benchbase.jar"]
```

**Running the benchmark**:
```bash
docker build -t benchbase-sqlite .
docker run --rm -v $(pwd)/results:/results benchbase-sqlite \
  -b ycsb -c /config/workloada.properties -d /results
```

**Workload configurations** (YCSB workloads):
- **Workload A (read-only)**: 50% reads, 50% updates
- **Workload B (mixed)**: 95% reads, 5% updates
- **Workload C (write-only)**: 100% inserts

Actually, the sheet uses:
- **read-only**: 100% reads
- **mixed**: 50% reads, 50% updates
- **write-only**: 100% inserts

### 2. BenchBase with PostgreSQL (client-server)

**Setup**: Use Docker Compose to run a PostgreSQL server and a BenchBase client. The client connects to the server over the Docker network.

**compose.yaml**:
```yaml
services:
  db:
    image: postgres:16
    environment:
      POSTGRES_DB: benchbase
      POSTGRES_USER: benchbase
      POSTGRES_PASSWORD: benchbase
    ports: ["5433:5432"]
    volumes: [pgdata:/var/lib/postgresql/data]
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U benchbase"]
      interval: 2s
      timeout: 5s
      retries: 10

  bench:
    image: benchbase-postgres
    depends_on:
      db:
        condition: service_healthy
    environment:
      BENCHBASE_DB_URL: jdbc:postgresql://db:5432/benchbase
      BENCHBASE_DB_USER: benchbase
      BENCHBASE_DB_PASSWORD: benchbase
    volumes: [results:/results]
    command: ["-b", "ycsb", "-c", "/config/workloada.properties", "-d", "/results"]

volumes:
  pgdata:
  results:
```

**Key difference**: the PostgreSQL setup uses two containers (server + client) connected over a Docker network. The SQLite setup uses a single container (embedded). This is the [[client-server-db-architecture]] vs embedded architecture comparison.

### 3. Throughput Comparison

**Results** (operations per second, from the exercise sheet):

| Workload | SQLite (embedded) | PostgreSQL (client-server) | Ratio (PG/SQLite) |
|----------|-------------------|----------------------------|-------------------|
| read-only | 2110.7 ops/s | 4016.8 ops/s | 1.9× |
| mixed | 1114.5 ops/s | 2705.5 ops/s | 2.4× |
| write-only | 10000.1 ops/s | 10000.7 ops/s | 1.0× |

**Analysis**:
- **Read-only**: PostgreSQL is ~1.9× faster. This is expected — PostgreSQL has a more sophisticated buffer pool and query optimizer.
- **Mixed**: PostgreSQL is ~2.4× faster. The gap widens because PostgreSQL handles concurrent reads and writes better (MVCC — multi-version concurrency control).
- **Write-only**: Both are ~10,000 ops/s. This is the insert rate limit, likely bounded by the disk I/O or the benchmark configuration (not the DBMS).

**Why SQLite is slower for reads**: SQLite reads from a single file. PostgreSQL uses a buffer pool and can cache frequently accessed pages in memory. For read-heavy workloads, PostgreSQL's caching gives it an advantage.

**Why write-only is the same**: both DBMS are writing to disk at the same rate. The write bottleneck is disk I/O, not the DBMS.

### 4. Image Size Comparison

**Build image vs prebuilt runtime**:
- **Build image** (maven:3.9-eclipse-temurin-21): ~800 MB (includes JDK, Maven, build tools)
- **Runtime image** (eclipse-temurin:21-jre): ~200 MB (includes only JRE, no build tools)
- **Multi-stage build**: the Dockerfile uses a multi-stage build — the build stage compiles the JAR, the runtime stage copies only the JAR. This reduces the final image size from ~800 MB to ~200 MB.

**Reproducibility implication**: the multi-stage build ensures the runtime image is minimal and contains only the artifacts needed to run the benchmark. This reduces the attack surface, speeds up container startup, and makes the image more portable.

### 5. Multiple Choice Questions

**5a. Foreign tables in PostgreSQL**:
- A foreign table is a table-like object whose rows are read on demand from an external source (a file, a remote DB, a web service) through a Foreign Data Wrapper (FDW).
- The file is *not* read at `CREATE FOREIGN TABLE` time — only when a query is run against the table.
- **Answer**: Foreign tables are lazy — they don't validate the source at creation time.

**5b. MariaDB benchmarking**:
- MariaDB is a fork of MySQL. BenchBase supports MariaDB through the MySQL JDBC driver.
- The benchmark setup is similar to PostgreSQL: a server container + a client container.
- **Answer**: MariaDB can be benchmarked with BenchBase using the same workflow as PostgreSQL.

**5c. Query reproducibility**:
- A query is reproducible if it produces the same result on the same data, regardless of when or where it is run.
- Non-deterministic queries (e.g., `ORDER BY RANDOM()`, `LIMIT` without `ORDER BY`) are not reproducible.
- **Answer**: To ensure reproducibility, always use deterministic queries (explicit `ORDER BY`, no `RANDOM()`).

## Key Takeaways

1. **Deployment architecture affects performance**: embedded (SQLite) is simpler but slower for read-heavy workloads. Client-server (PostgreSQL) is more complex but faster for concurrent workloads.
2. **Docker makes benchmarking reproducible**: the same Docker image on any machine produces the same setup. The `compose.yaml` file pins versions, configuration, and network setup.
3. **Multi-stage builds reduce image size**: the build stage compiles the JAR, the runtime stage copies only the JAR. This is a best practice for Docker images.
4. **Write-only workloads are I/O-bound**: both SQLite and PostgreSQL hit the same write limit, suggesting the bottleneck is disk I/O, not the DBMS.
5. **Foreign tables are lazy**: they don't validate the source at creation time. This is by design but can surprise new users.

## Related Lectures
- [[reproducibility-engineering-lecture-6]] — database architectures
- [[reproducibility-engineering-lecture-7]] — tidy data (data cleaning for benchmark results)
- [[client-server-db-architecture]] — the PostgreSQL architecture
- [[sqlite-architecture]] — the SQLite architecture
- [[docker-compose]] — the standard for multi-service reproducible setups
- [[foreign-tables-postgresql]] — for capturing experiment metadata
