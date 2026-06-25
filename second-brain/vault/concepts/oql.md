---
title: "OQL (Object Query Language)"
tags: [concept, multimedia-databases, semester-1, query-languages, oql, odmg]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-25
prerequisites: ["[[object-relational-databases]]", "[[multimedia-query-languages]]"]
---

## One-line Summary
A query language for object databases, similar to SQL 92 but built around objects, identity, and path expressions instead of flat tables.

## Core Intuition
SQL was designed for rows in tables. Object oriented databases store complex objects with identity, inheritance, and methods, none of which fit neatly into SQL's flat projection model. OQL answers this by keeping the familiar select from where shape but making every operand an object or a query that returns objects. You can navigate from an object to its related objects through path expressions, call methods in the query, and rely on late binding so the right method runs for the actual object type.

The practical reason OQL matters here is that it is the base MOQL extends. The multimedia extensions are bolted onto OQL's WHERE clause, so understanding OQL's basic construct is a prerequisite for reading MOQL queries. OQL is based on the ODMG object model and is usually embedded inside programming languages rather than used as a standalone shell.

## Formal Definition / Statement

OQL is based on the ODMG object model. It is similar to SQL 92 with object oriented extensions:
- complex objects
- object identity
- path expressions
- polymorphisms
- function calls
- late binding

It is embedded in programming languages.

**Basic query construct**:
```
select [ distinct ] projection_attributes
from   query [ [ as ] identifier ] { , query [ [ as ] identifier ] }
where  query
```

Key points about the construct:
- The `from` clause takes *queries*, not just table names. Each query can be bound to an identifier with `as`.
- `projection_attributes` can include path expressions that navigate object references and methods.
- `distinct` removes duplicates, as in SQL.
- The `where` clause is itself a query (a boolean valued expression), which may call methods and traverse paths.

## Key Properties / Complexity

### Object oriented features that distinguish OQL from SQL 92
- **Object identity**: two objects with identical attribute values are still distinct if they have different identities. Comparisons can be by identity, not only by value.
- **Path expressions**: a query can write `student.advisor.department.name` to navigate from a student object through its advisor to the department and its name. SQL needs joins for the same navigation.
- **Polymorphism and late binding**: when a query calls a method on an object, the method that runs is determined by the object's actual type at runtime, not the declared type. A `draw()` call on a Shape variable runs Circle.draw or Square.draw depending on the real object.
- **Function calls**: methods and functions can appear in projection and predicate positions, so computation can live in the query rather than only in the application.

### From clause as query, not table
- Because `from` accepts queries, subqueries can generate the collections being iterated over without a separate subselect syntax.
- Each entry in the from list can be aliased, and multiple entries produce a Cartesian product filtered by the where clause, as in SQL.

### Embedding
- OQL is typically embedded in a host language (C++, Smalltalk, Java in the ODMG world). Objects returned by a query are native language objects, so there is no object relational impedance mismatch on the way out.

## Worked Example

A simple OQL query over a university object model:
```
select distinct s.name, s.advisor.department.name
from   students s
where  s.advisor.department.name = "Computer Science"
```

Step by step:
1. `students s` binds s to each object in the students collection.
2. `s.advisor.department.name` is a path expression. It navigates from the student to the advisor object, then to that advisor's department object, then to the department's name attribute. No joins are written.
3. The WHERE clause uses the same path expression to keep only students whose advisor is in Computer Science.
4. `distinct` removes duplicate name pairs if a student and advisor share a name across departments.

A query whose from clause is itself a query:
```
select c.name
from   (select d from departments d where d.budget > 1000000) as d
where  d.college.name = "Engineering"
```
Here the from clause runs an inner query that filters departments by budget, binds the result to d, and the outer where filters by college. This nesting is natural in OQL because every from entry is a query.

## Common Pitfalls
- **Reading OQL as if it were SQL 92**: the syntax looks similar, but the from clause takes queries and objects, not tables. Assuming table semantics leads to wrong mental models of what path expressions return.
- **Forgetting late binding**: a method call in a query runs the subclass implementation, not the declared type's. Tests on a single subtype can pass while a polymorphic query returns unexpected results.
- **Assuming OQL is standalone**: it is embedded in a host language. Treating it like a SQL shell that prints rows misses that results come back as native objects.
- **Confusing OQL with SQL/MM**: OQL is the object query language from ODMG. SQL/MM is the SQL multimedia standard. MOQL extends OQL, while SQL/MM extends SQL. They are different extension lineages.
- **Ignoring object identity**: comparing objects with `=` may compare identity, not value. Use explicit attribute comparisons when you need value equality.

## Connections
[[moql]]: MOQL extends OQL's WHERE clause with spatial, temporal, contains, and presentation constructs.
[[multimedia-query-languages]]: OQL is the base of the extension category that produced MOQL.
[[object-relational-databases]]: the ODMG object model OQL queries sits in the object oriented side of the object relational landscape.
[[sql-mm]]: the SQL 99 multimedia extension, the parallel to MOQL on the SQL side.
[[feature-vector]]: object identity and path expressions let an OQL query navigate from a media object to its stored feature descriptors.

## Open Questions
- Why did OQL and the ODMG model lose traction to object relational SQL extensions? Was it the embedding model, vendor support, or the dominance of SQL?
- Could path expressions be added to modern graph or document query languages, given OQL already had them decades ago?
- How would OQL's late binding interact with a machine learning model exposed as a method on a media object?
