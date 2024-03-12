# 4. Django

Date: 2024-03-12

## Status

Accepted

## Context

We decided to use a batteries-inluded-Web-Framework in ADR 0003. Therefore we had to decide which framework should be
used to implement the storing of the data.

We compared different batteries-included Frameworks written in Python, PHP, Ruby, Java, Groovy.

## Decision

Django came out on top for these reasons:
* admin functionality
* very active community since 2005
* Python is a [very common and loved language](https://insights.stackoverflow.com/survey/2019#technology)
* many third-party-plugins
* mature ORM

As one teammember was an experienced Django-developer and it was on top of the comparison we decided to write a
Proof of concept (PoC).

As the requirements were met by the Django-PoC, we decided to go with the Django framework.

## Consequences

* We will use a Python CRUD-Framework and the Python language in the project. It's the brain of the project and will be
time-consuming to change.
* We use the Django project structure which means to group models into apps and use dedicated files for different
functionaliy, e.g. models.py for models, admin.py for admin interface, etc..
