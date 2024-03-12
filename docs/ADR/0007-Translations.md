# 20. Translations

Date: 2024-03-12

## Status

Accepted

## Context

The code language is English.

## Decision

We will translate all user interface relevant names (models, field_names, templates) into German inside the project.
User inputs will not be translatable for now and are entered in German.
The projects interface language is German.

## Consequences

* All the code is in English.
* We translate all relevant names through .po files using Django's internal i18n system (instructions in the README).
* User inputs are by convention in German.
