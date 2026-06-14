---
title: "PostgreSQL Foreign Tables"
tags: [concept, reproducibility-engineering, semester-1, postgresql, foreign-table, file-fdw]
course: "Reproducibility Engineering"
source_count: 2
status: current
last_updated: 2026-06-14
prerequisites: ["[[client-server-db-architecture]]", "[[sqlite-architecture]]"]
---

## One-line Summary
A PostgreSQL foreign table is a table-like object whose rows are *not* stored inside the database — they are read on demand from an external source (a file on disk, a remote database, a web service) through a Foreign Data Wrapper (FDW) — useful for querying logs, CSVs, or other databases as if they were SQL tables, but with sharp performance and reproducibility caveats.

## Core Intuition
The lecture's example (Sheet 6, task 6) shows the canonical use case: read `/proc/meminfo` as if it were a SQL table.

```sql
CREATE FOREIGN TABLE experiment_meminfo (
    key   text,
    value text
)
SERVER local_files
OPTIONS (
    filename '/proc/meminfo',
    format 'csv',
    delimiter ':'
);

SELECT * FROM experiment_meminfo WHERE key = 'MemTotal';
```

PostgreSQL doesn't *store* the contents of `/proc/meminfo`. It *queries* it on demand, parses the file with the `file_fdw` extension, and returns rows. The file is read every time the foreign table is queried.

The lecture's trap question: "Which conclusion is justified when the `CREATE FOREIGN TABLE` statement succeeds?"

```
⃝ PostgreSQL has verified that /proc/meminfo exists.
⃝ PostgreSQL has verified that the file can be read by the server process.
⃝ PostgreSQL has verified that every line can be parsed into two columns.
⃝ None of these options.
```

**Answer: None of these.** The `CREATE FOREIGN TABLE` statement only registers the table's *definition* — the file path, the format, the column types. The actual file is *not* read until a query is run against the table. The verification happens lazily, at query time. This is a classic source of "the table works, the query fails" surprises.

## Formal Definition / Statement

### Anatomy of a foreign table
```sql
CREATE FOREIGN TABLE table_name (
    column1 type1,
    column2 type2,
    ...
)
SERVER server_name
[ OPTIONS ( option 'value', ... ) ]
```

- **server_name**: a `SERVER` object that points to an FDW (Foreign Data Wrapper). The FDW is the plugin that knows how to read the external source.
- **OPTIONS**: FDW-specific options. For `file_fdw`: `filename`, `format`, `delimiter`, `header`, `quote`, `escape`, `null`.

### Common FDWs
- **`file_fdw`**: read CSV/TSV files. Shipped with PostgreSQL.
- **`postgres_fdw`**: query another PostgreSQL server. Shipped.
- **`mysql_fdw`**: query MySQL. Third-party.
- **`mongodb_fdw`**: query MongoDB. Third-party.
- **`http_fdw`**: query HTTP endpoints. Third-party.

### How a query is executed
1. The planner recognises the table as foreign.
2. The planner pushes down predicates to the FDW where possible (e.g., `WHERE key = 'MemTotal'` can be evaluated by `file_fdw` *only if* the file is indexed — for plain CSV files, no pushdown is possible).
3. The FDW opens the external source, reads the rows, applies any local predicates, returns the result.
4. The result is presented to the client as a normal PostgreSQL result set.

### Performance characteristics
- **No statistics by default**: the planner doesn't know the row count, so it can't optimise joins.
- **No indexes (in general)**: a CSV file has no index. Every query reads the whole file.
- **No pushdown (in general)**: predicates are evaluated *after* the file is read.
- **Latency dominated by I/O**: reading `/proc/meminfo` is cheap; reading a 100 GB CSV is slow.

## Key Properties

### Strengths
- **No data movement**: query the external source in place. No ETL, no staging table.
- **Standard SQL interface**: the foreign table looks like a regular table. Existing tools (psql, BI tools, ORM) work without modification.
- **Schema on read**: the column types are declared at `CREATE FOREIGN TABLE` time, but the data isn't validated until query time.
- **Composable**: you can JOIN a foreign table with local tables, aggregate it, filter it — anything that works on a local table.

### Weaknesses
- **No pushdown in the basic case**: the FDW reads the *entire* file, then PostgreSQL filters. For large files, this is slow.
- **No transactions across local + foreign**: a `BEGIN; SELECT from local; SELECT from foreign; COMMIT;` doesn't give you a consistent snapshot of the foreign source.
- **No writes (in the basic case)**: most FDWs are read-only. Some support INSERT/UPDATE/DELETE (e.g., `postgres_fdw` with `mutable` option).
- **No statistics**: the planner assumes the foreign table has 1000 rows (default `fdw_startup_cost`, `fdw_tuple_cost`). Bad plans for large foreign tables.
- **Lazy validation**: as the lecture's trap question shows, `CREATE FOREIGN TABLE` is no guarantee that the source is usable. Errors surface at query time.

### When to use foreign tables
- **One-off exploration**: query a log file or CSV without loading it into PostgreSQL.
- **Cross-database queries**: read from another PostgreSQL or MySQL instance.
- **Web service integration**: query an HTTP API as a table.
- **Light ETL**: read a file, transform in SQL, write to a local table.

### When NOT to use foreign tables
- **Production analytics on large data**: use a proper ETL pipeline to load the data first.
- **High-frequency queries**: the I/O cost of reading the external source on every query is too high.
- **Transactional consistency**: foreign tables are typically not part of the local transaction.

## Worked Example

The lecture's full task 6:

```sql
-- Create the foreign table
CREATE FOREIGN TABLE experiment_meminfo (
    key   text,
    value text
)
SERVER local_files
OPTIONS (
    filename '/proc/meminfo',
    format 'csv',
    delimiter ':'
);
```

Multi-choice questions:
1. Which conclusion is justified when `CREATE FOREIGN TABLE` succeeds?
   → **None.** The statement is metadata; the file is not read.

2. Which statements are true? (check all that apply)
   - ✓ Problems such as unreadable files or unexpected file format may only become visible when the table is queried.
   - ✓ A query such as `SELECT * FROM experiment_meminfo` reads and parses the external file.
   - ✗ Evaluating a selection such as `WHERE key = 'MemTotal'` can use an index on /proc/meminfo. (No index exists; the file is scanned.)
   - ✓ For this example, scanning the complete source is usually cheap, because /proc/meminfo is small.
   - ✗ For a very large CSV file, highly selective predicates in the WHERE-clause are guaranteed to make access efficient. (No, predicates are evaluated after the file is read.)
   - ✗ Joining experiment_meminfo with PostgreSQL-internal base tables is possible and also carried out very efficiently. (Joins are *possible*, but not *efficient* — no statistics, no index.)

3. For a large CSV foreign table `measurements`, which queries require scanning the entire file?
   - ✓ `SELECT * FROM measurements;` (full scan to return all rows)
   - ✗ `SELECT * FROM measurements WHERE run_id = 42;` (also full scan — no index, no pushdown)
   - ✓ `SELECT COUNT(*) FROM measurements;` (full scan to count)

**Key takeaway:** for foreign tables, *every* query is effectively a full scan unless the FDW provides index/pushdown support. "Efficient" access via WHERE clauses is a property of the *local* planner; foreign tables are typically scan-only.

## Common Pitfalls
- **Assuming the file exists at create time**: the `CREATE FOREIGN TABLE` doesn't check. The error surfaces at query time.
- **Assuming predicates are pushed down**: for `file_fdw`, they're not. The whole file is read, then filtered.
- **Assuming cost-based optimisation works**: the planner uses default cost estimates (1000 rows) for foreign tables. Run `ANALYZE foreign_table` after loading data, or the planner will make bad decisions on joins.
- **Forgetting permissions**: the FDW runs *as the server process*. If the file is owned by `alice` and the server runs as `postgres`, the read fails. Permissions matter.
- **Confusing foreign tables with `COPY ... FROM`**: `COPY` loads the data into a local table (storing it). Foreign tables leave the data in place. Use `COPY` for ETL; use foreign tables for ad-hoc queries.
- **Trying to do transactions across local + foreign**: the foreign source is typically not transactional. Your local transaction is fine, but the foreign snapshot is not coordinated with it.

## Connections
- [[reproducibility-engineering-lecture-6]] — the lecture
- [[client-server-db-architecture]] — the server-side context
- [[sqlite-architecture]] — a different approach to "external data": just read the file directly
- [[reproducibility-engineering-lecture-6]] — the broader lecture

## Open Questions
- For frequently-queried foreign tables, should you materialise them into local tables? (Yes, if the data changes infrequently and queries are expensive. Use a scheduled `INSERT INTO local SELECT * FROM foreign`.)
- For real-time foreign data (e.g., Kafka, web APIs), are foreign tables the right abstraction? (Probably not — there's a latency, pushdown, and consistency story that doesn't fit the table model. Use a streaming SQL engine instead.)
- Can a foreign table be made indexable? (In PostgreSQL 15+, no — but you can create a local covering index on a materialised view that copies the foreign data.)
