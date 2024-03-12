# 6. Postgres

Date: 2024-03-12

## Status

Accepted

## Context

We decided in ADR 0002/0003/0004 to use Django as a Web framework. A Web framework abstracts the database interaction
so that it is not necessary to write native SQL code. Nonetheless it is necessary to install and use a database in the
back. We do not have any special requirements for the database and it's enough to have standard SQL functionality.

The default database for projects with Django is SQLite. It is easy to setup and can be used directly. It was also
used in the Proof of concept for this project. However SQLite is not a client-server database engine and is especially
used for client/local storage in applications. Our application is a client-server application and therefore needs
another database. Postgres is the standard for such setups.
Furthermore:
* Postgres is recommended by Django as production-database.
* Postgres is widely used in production environments in various industries
* Postgres has been on the market since 1996. A lot of development (performance optimizations, security, etc.) has
already gone into it.

## Decision

We decide to use a Postgres Database. We manipulate the structure and the data of the database through Django.

## Consequences

* We depend on the Postgres database to store the data. It is possible to change the underlying
database, but it is associated with significant effort (migrations).
* We use the backup functionality of Postgres databases to back up the valuable data.
* Every developer needs a local instance of Postgres to develop.
