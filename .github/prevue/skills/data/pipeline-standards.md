---
name: Data Pipeline Standards
description: Team conventions for batch ETL jobs and warehouse loads.
applies-to:
  - "pipelines/**"
  - "dbt/**"
---
- Every pipeline module must declare `owner` and `sla_hours` in a module docstring.
- Batch jobs must log row counts on read and write; flag loads with no metrics.
- Idempotent loads only — no blind `INSERT` without dedupe key or merge strategy.
- Partition columns must be explicit in load SQL; flag implicit full-table scans on fact tables.
