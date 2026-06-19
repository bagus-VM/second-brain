---
title: "Lecture 7: Tidy Data"
tags: [topic, reproducibility-engineering, semester-1, tidy-data, data-wrangling, sql, metadata]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-06-19
prerequisites: ["[[reproducibility-engineering-lecture-6]]", "[[data-provenance]]", "[[workflow-reproducibility]]"]
sources: ["raw/lectures/reproducibility_engineering/Vorlesung/SoSe_2026_RepEng_IC_7___Tidy_Data.pdf"]
---

## One-line Summary
Data is "tidy" when each variable is a column, each observation is a row, and each value is a cell — and this structural invariant is a prerequisite for reproducible analysis pipelines, because tools that operate on uniform tabular data can be composed, tested, and re-run without ad-hoc reshaping.

## Core Intuition
Most real-world data arrives *untidy*: cross-tabulations, pivot tables, multi-variable columns, header rows that encode values. The lecture's central claim is that **tidying is not optional cleanup** — it is the foundational step that makes every downstream operation (filtering, grouping, joining, visualising) composable and reproducible.

Hadley Wickham's three rules are deceptively simple, but the hard part is *recognising* untidy data and knowing how to reshape it. The lecture covers this through SQL: pivoting (wide→tall) and unpivoting (tall→wide) using `CREATE TABLE AS ... CASE`, `GROUP BY`, and `UNION ALL`. The earthquakes example — a wide table with columns `mag_1995`, `mag_1996`, ..., `mag_2024` — is the canonical untidy→tidy transformation.

The lecture also introduces **metadata as a first-class concern**: data exploration and cleaning are workflows, and every transformation should be either *reversible* (so you can undo mistakes) or *destructive-but-logged* (so you can trace provenance). This connects directly to [[data-provenance]] and [[workflow-reproducibility]].

## Key Concepts

### Wickham's three rules of tidy data
1. **Each variable forms a column** — no two variables in one column (e.g., "date" and "time" merged as a string)
2. **Each observation forms a row** — no observation split across rows (e.g., a patient's vitals on multiple rows)
3. **Each value forms a cell** — one value per (row, column) intersection

A dataset is tidy if and only if all three rules hold simultaneously.

### Common untidy patterns
- **Cross-tabulations / contingency tables**: values of one variable become column headers (e.g., columns `male`, `female` with counts). The column headers *are* data, not variable names.
- **Multiple variables in one column**: e.g., a column `measurement` containing "height: 180cm" — two variables (type and value) packed together.
- **Variables in both rows and columns**: e.g., a table where rows are patients, columns are dates, and cells are temperatures — the date is a variable encoded as a column header.
- **Multiple types in one table**: e.g., a table mixing patient demographics and lab results in the same rows.
- **One variable spread across multiple columns**: e.g., `first_name`, `last_name` as separate columns when they should be a single `name` variable (or vice versa — depends on the analysis).

### Pivoting and unpivoting in SQL
**Unpivoting (wide → tall)**: Transform a wide table (many columns for the same variable at different levels) into a tall table (one column for the variable, one column for the level).

The earthquakes example:
```sql
-- Wide: columns mag_1995, mag_1996, ..., mag_2024
-- Tall: columns year, magnitude

CREATE TABLE earthquakes_tall AS
SELECT 1995 AS year, mag_1995 AS magnitude FROM earthquakes_wide
UNION ALL
SELECT 1996 AS year, mag_1996 AS magnitude FROM earthquakes_wide
UNION ALL
...
SELECT 2024 AS year, mag_2024 AS magnitude FROM earthquakes_wide;
```

**Pivoting (tall → wide)**: The reverse. Use `GROUP BY` with conditional aggregation:
```sql
CREATE TABLE earthquakes_wide AS
SELECT
  MAX(CASE WHEN year = 1995 THEN magnitude END) AS mag_1995,
  MAX(CASE WHEN year = 1996 THEN magnitude END) AS mag_1996,
  ...
  MAX(CASE WHEN year = 2024 THEN magnitude END) AS mag_2024
FROM earthquakes_tall
GROUP BY <some_key>;
```

### Metadata: data exploration as workflow
- **Data cleaning is a workflow**, not a one-shot action. Each step (filter, reshape, impute, aggregate) transforms the data.
- **Destructive vs reversible actions**:
  - *Reversible*: filtering (you can undo by removing the filter), renaming columns, reshaping — you can always get back to the original.
  - *Destructive*: dropping rows, aggregating, imputing missing values — you lose information. Once you drop rows, you can't get them back from the filtered dataset.
- **The provenance chain**: every transformation should be recorded (in a script, a notebook, or a migration log) so the workflow is reproducible. This is [[data-provenance]] applied to data wrangling.

### Odds ratios and contingency table analysis in SQL
A contingency table (cross-tabulation) is inherently untidy — it encodes one variable's values as column headers. To compute an odds ratio:

```sql
-- Contingency table: treatment (A/B) × outcome (success/failure)
-- Untidy: columns A_success, A_failure, B_success, B_failure
-- Tidy: columns treatment, outcome, count

-- Odds ratio = (A_success / A_failure) / (B_success / B_failure)
SELECT
  (SUM(CASE WHEN treatment='A' AND outcome='success' THEN count ELSE 0 END) *
   SUM(CASE WHEN treatment='B' AND outcome='failure' THEN count ELSE 0 END)) /
  (SUM(CASE WHEN treatment='A' AND outcome='failure' THEN count ELSE 0 END) *
   SUM(CASE WHEN treatment='B' AND outcome='success' THEN count ELSE 0 END))
  AS odds_ratio
FROM tidy_contingency;
```

The key insight: you must *first* tidy the contingency table before you can compute statistics on it. The tidy form is the prerequisite for analysis.

## Key Properties

### Why tidy data matters for reproducibility
- **Composability**: tidy data can be piped through a sequence of transformations (filter → group → aggregate → join) without ad-hoc reshaping at each step.
- **Tool support**: most statistical and visualisation tools (ggplot2, dplyr, pandas, SQL) assume tidy input. Untidy data requires custom code for every analysis.
- **Testability**: a tidy dataset has a known structure. You can write assertions (e.g., "every row has exactly one value per column") and check them automatically.
- **Provenance**: tidy data makes the transformation history explicit. You can trace every value back to its source.

### The cost of untidy data
- Every analysis requires custom reshaping code — code that is hard to test, hard to reuse, and hard to reproduce.
- Errors in reshaping are silent: a misaligned pivot produces plausible-looking but wrong results.
- Collaboration breaks down: two analysts reshape the same data differently and get different answers.

### SQL as a reshaping tool
- SQL's `CASE`, `GROUP BY`, `UNION ALL`, and `PIVOT`/`UNPIVOT` (in some dialects) are the workhorses for tidy↔untidy transformations.
- `CREATE TABLE AS` materialises the reshaped data — a destructive action that should be logged.
- Views (`CREATE VIEW AS`) are the reversible alternative — the original data is untouched.

## Worked Example: Earthquakes Wide → Tall

**Wide table** (untidy):
| region | mag_1995 | mag_1996 | mag_1997 |
|--------|----------|----------|----------|
| Pacific | 6.2 | 5.8 | 7.1 |
| Atlantic | 4.1 | 4.5 | 3.9 |

**Problem**: `year` is a variable, but it's encoded as column headers. This violates Rule 1 (each variable = column).

**Unpivot to tidy**:
```sql
CREATE TABLE earthquakes_tidy AS
SELECT region, 1995 AS year, mag_1995 AS magnitude FROM earthquakes_wide
UNION ALL
SELECT region, 1996 AS year, mag_1996 AS magnitude FROM earthquakes_wide
UNION ALL
SELECT region, 1997 AS year, mag_1997 AS magnitude FROM earthquakes_wide;
```

**Tidy table**:
| region | year | magnitude |
|--------|------|-----------|
| Pacific | 1995 | 6.2 |
| Pacific | 1996 | 5.8 |
| Pacific | 1997 | 7.1 |
| Atlantic | 1995 | 4.1 |
| Atlantic | 1996 | 4.5 |
| Atlantic | 1997 | 3.9 |

Now `region`, `year`, and `magnitude` are each a column. Each row is one observation (one region-year measurement). Each cell is one value. Tidy.

**Pivot back** (if needed):
```sql
CREATE TABLE earthquakes_repivoted AS
SELECT
  region,
  MAX(CASE WHEN year = 1995 THEN magnitude END) AS mag_1995,
  MAX(CASE WHEN year = 1996 THEN magnitude END) AS mag_1996,
  MAX(CASE WHEN year = 1997 THEN magnitude END) AS mag_1997
FROM earthquakes_tidy
GROUP BY region;
```

## Common Pitfalls

- **Confusing "wide" with "untidy"**: wide data is not always untidy. A dataset with columns `name`, `height_cm`, `weight_kg` is wide *and* tidy — each column is a distinct variable.
- **Confusing "long" with "tidy"**: long data is not always tidy. A dataset with columns `variable`, `value` where `variable` encodes multiple things (e.g., "height_cm", "weight_kg") is long but untidy — the variable name contains two pieces of information (measurement type and unit).
- **Pivoting without a key**: when pivoting tall→wide, you need a `GROUP BY` key. Without it, you collapse all rows into one.
- **`CREATE TABLE AS` is destructive**: it materialises the result and discards the original. Use `CREATE VIEW AS` if you want to keep the original.
- **Odds ratio direction matters**: (A/B) is the inverse of (B/A). Always state which direction you're computing.
- **Contingency tables are untidy by definition**: the column headers *are* data. You must unpivot before analysis.
- **The lecture's focus is reproducibility, not SQL syntax**: the SQL is a means to an end. The end is a reproducible data transformation pipeline.

## Connections
- [[data-provenance]] — tidy data transformations should be logged for provenance
- [[workflow-reproducibility]] — data cleaning is a workflow; every step must be reproducible
- [[client-server-db-architecture]] — SQL reshaping works the same in SQLite and PostgreSQL
- [[sqlite-architecture]] — the single-file DB is ideal for archiving tidy datasets
- [[tidy-data]] — the concept page
- [[json-schema]] — validates structure, analogous to tidy data's structural invariant
- [[hdf5]] — hierarchical data can also be tidy (each dataset = one variable)

## Open Questions
- Is there a formal definition of "tidy" beyond Wickham's three rules? (E.g., a normal form for data?)
- How do you tidy data that is inherently multi-dimensional (e.g., a tensor of sensor readings over time, space, and frequency)?
- What is the relationship between tidy data and database normal forms (1NF, 2NF, 3NF)?
- Can you automatically detect untidy data? (E.g., a linter for tabular data?)
- How do you handle tidy data in non-tabular formats (JSON, HDF5)?
