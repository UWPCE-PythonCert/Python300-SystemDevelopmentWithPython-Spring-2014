
.. No SQL DataBases slides file, created by
   hieroglyph-quickstart on Sat Apr 12 15:26:42 2014.

================
No SQL Databases
================

Some other options for storing/retrieving data.

What is a Database?
====================

  "A database is an organized collection of data. The data are typically organized to model relevant aspects of reality in a way that supports processes requiring this information.

Usually a way to persist and recover that organised data.

These days, when you say "Database" almost everyone thinks "Relational Database", and SQL is the standard way to do that.

SQL RDBMS systems are robust, powerful, scalable and very well optimised.

But: They require you to adapt the relational data model. 

Non RDBMS options:
==================

A key buzzword these days is "NOSQL"

OK: They don't use SQL -- but what are they?

Not one thing, but key features are mostly shared:
 * "schema less"
   - Document oriented
 * Map/Reduce

Easier to distribute/paralelize:
  * Highly Scalable


Database Schema
===============

Schema:
  A database schema is the organization of data, and description of how a database is constructed: Divided into database tables, and relationships: foreign keys, etc...

  Includes what fields in what tables, what data tyeps each fiels is, normalization of shared data, etc.

This requires a fair bit of work up-front, and can be hard to adapt as the system requirements change.

It also can be a bit ugly to map your programming data model to the schema.

Schemaless
==========

Schemaless databases generally follow a "document model".

Each entry in the database is a "document":
 * essentially an arbitraty collection of fields.
 * often looks like a Python dict.

Not every entry has to have exactly the same struture.

Maps well to dynamic programming languages.

Adapts well as the system changes.

NoSQL in Python:
================

Three Categories:

1. Simple key-value object store:
   - shelve
   - anydbm
   (we talked about these last fall...)
   - Can store (almost) any Python object
   - Only provides storage and retrieval 

2. External NOSQL system:
  - Python bindings to external NOSQL system
  - Doesn't store full Python objects
  - Generally stores arbitrary collections of data (but not classes)
  - Provides in-database searching, etc.

3. Python object database:
  - Stores and retrieves arbitrary Python objects.
  - Provides some in-database searching, etc.
  - ZODB is the only robust maintained system (I know of)





