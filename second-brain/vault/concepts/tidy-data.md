---
title: "Tidy Data"
tags: [concept, reproducibility-engineering, semester-1, data-wrangling, data-organization]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-06-19
prerequisites: ["[[reproducibility-engineering-lecture-7]]"]
---

## One-line Summary
Data organized so each variable is a column, each observation is a row, each value is a cell.

## Core Intuition
Tidy data is the "normal form" for tabular data — a structural invariant that makes every downstream operation (filtering, grouping, joining, visualising) composable and tool-agnostic. If your data is tidy, you can pipe it through a standard toolkit (SQL, dplyr, pandas) without ad-hoc reshaping at every step. If it's untidy, every analysis requires custom code to first make the data usable.

The concept was formalised by Hadley Wickham in his 2014 paper "Tidy Data" (Journal of Statistical Software). The three rules are simple; the hard part is recognising untidy data and knowing how to reshape it.

## Formal Definition / Statement
A dataset is **tidy** if and only if:
1. **Each variable forms a column** — no two variables packed into one column (e.g., "height: 180cm" is two variables: type and value)
2. **Each observation forms a row** — no observation split across multiple rows (e.g., a patient's vitals on separate rows)
3. **Each value forms a cell** — one value per (row, column) intersection; no multi-valued cells

A dataset satisfying all three rules is in "tidy form." A dataset violating any rule is "untidy."

## Key Properties

### Wickham's three rules
1. Each variable = one column
2. Each observation = one row
3. Each value = one cell

These rules are necessary and sufficient for tidy data. All three must hold simultaneously.

### Why it matters: enables tools that operate on uniform tabular structure
- **Composability**: tidy data can be piped through a sequence of standard operations (filter → group → aggregate → join → visualise) without custom reshaping.
- **Tool support**: most statistical and visualisation tools (ggplot2, dplyr, pandas, SQL, R, Python) assume tidy input. Untidy data requires custom code.
- **Testability**: a tidy dataset has a known structure. You can write assertions (e.g., "every row has exactly one value per column") and check them automatically.
- **Reproducibility**: tidy data makes the transformation history explicit. You can trace every value back to its source.

### Common untidy patterns
- **Cross-tabulations / contingency tables**: values of one variable become column headers (e.g., columns `male`, `female` with counts). The column headers *are* data, not variable names.
- **Multiple variables in one column**: e.g., a column `measurement` containing "height: 180cm" — two variables (type and value) packed together.
- **Variables in both rows and columns**: e.g., a table where rows are patients, columns are dates, and cells are temperatures — the date is a variable encoded as a column header.
- **Multiple observation types in one table**: e.g., a table mixing patient demographics and lab results in the same rows.
- **One variable spread across multiple columns**: e.g., `first_name`, `last_name` as separate columns when they should be a single `name` variable (or vice versa — depends on the analysis).

### Pivoting and unpivoting
- **Unpivoting (wide → tall)**: transform a wide table (many columns for the same variable at different levels) into a tall table (one column for the variable, one column for the level). Example: columns `mag_1995`, `mag_1996`, ..., `mag_2024` → columns `year`, `magnitude`.
- **Pivoting (tall → wide)**: the reverse. Use `GROUP BY` with conditional aggregation (`CASE WHEN`).

### Connection to reproducibility: tidy data is a prerequisite for reproducible analysis pipelines
- **Reproducible pipelines assume tidy input**: if the input is untidy, every step requires custom reshaping code — code that is hard to test, hard to reuse, and hard to reproduce.
- **Tidy data makes the transformation history explicit**: you can log every reshaping step and reproduce the entire pipeline.
- **Untidy data hides errors**: a misaligned pivot produces plausible-looking but wrong results. Tidy data makes errors visible (e.g., a missing value is an empty cell, not a misaligned column).

## Worked Example

**Untidy data** (cross-tabulation):
| region | mag_1995 | mag_1996 | mag_1997 |
|--------|----------|----------|----------|
| Pacific | 6.2 | 5.8 | 7.1 |
| Atlantic | 4.1 | 4.5 | 3.9 |

**Problem**: `year` is a variable, but it's encoded as column headers. This violates Rule 1 (each variable = column).

**Tidy data** (unpivoted):
| region | year | magnitude |
|--------|------|-----------|
| Pacific | 1995 | 6.2 |
| Pacific | 1996 | 5.8 |
| Pacific | 1997 | 7.1 |
| Atlantic | 1995 | 4.1 |
| Atlantic | 1996 | 4.5 |
| Atlantic | 1997 | 3.9 |

Now `region`, `year`, and `magnitude` are each a column. Each row is one observation (one region-year measurement). Each cell is one value. Tidy.

## Common Pitfalls

- **Confusing "wide" with "untidy"**: wide data is not always untidy. A dataset with columns `name`, `height_cm`, `weight_kg` is wide *and* tidy — each column is a distinct variable.
- **Confusing "long" with "tidy"**: long data is not always tidy. A dataset with columns `variable`, `value` where `variable` encodes multiple things (e.g., "height_cm", "weight_kg") is long but untidy — the variable name contains two pieces of information (measurement type and unit).
- **Thinking tidy data is always the goal**: tidy data is the goal for *analysis*. For *presentation* (e.g., a summary table in a paper), wide/pivoted data is often more readable. Tidy data is the intermediate form, not the final form.
- **Forgetting that "observation" depends on the analysis**: the same dataset can be tidy for one analysis and untidy for another. An "observation" is defined by the unit of analysis (e.g., a patient, a day, a region-year).
- **Pivoting without a key**: when pivoting tall→wide, you need a `GROUP BY` key. Without it, you collapse all rows into one.

## Connections
- [[reproducibility-engineering-lecture-7]] — the lecture that introduces tidy data
- [[data-provenance]] — tidy data transformations should be logged for provenance
- [[workflow-reproducibility]] — data cleaning is a workflow; tidy data is the starting point
- [[json-schema]] — validates structure, analogous to tidy data's structural invariant
- [[hdf5]] — hierarchical data can also be tidy (each dataset = one variable)
- [[sqlite-architecture]] — SQL is a natural tool for reshaping data to/from tidy form

## Open Questions
- Is there a formal definition of "tidy" beyond Wickham's three rules? (E.g., a normal form for data, analogous to database normal forms?)
- How do you tidy data that is inherently multi-dimensional (e.g., a tensor of sensor readings over time, space, and frequency)?
- What is the relationship between tidy data and database normal forms (1NF, 2NF, 3NF)?
- Can you automatically detect untidy data? (E.g., a linter for tabular data?)
