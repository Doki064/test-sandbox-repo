# Prevue Demo Sandbox

Sandbox repo for live demos of [Prevue](https://github.com/Doki064/prevue) — token-efficient AI PR review for data engineering teams.

## What is wired up

| Component | Path |
|-----------|------|
| Automatic review on PR open/sync | `.github/workflows/prevue-review.yml` |
| `/prevue` comment commands | `.github/workflows/prevue-command.yml` + `prevue-command-run.yml` |
| Consumer config | `.github/prevue.yml` |
| Custom data skill | `.github/prevue/skills/data/pipeline-standards.md` |

**Prerequisite:** repo secret `COPILOT_GITHUB_TOKEN` (fine-grained user PAT with Copilot Requests).

## Demo PR catalog

Open PRs are numbered for the walkthrough. Each PR title states the feature being shown.

| PR | Feature demonstrated |
|----|----------------------|
| **#1 Data: SQL migration review** | Zero-token `data` label → `sql-safety` + `migrations` skills |
| **#2 Security: committed secrets** | `security` label, error-severity inline, `prevue/review` check fails |
| **#3 Multi-label: data + infra** | Union routing — SQL + Terraform load both skill bundles |
| **#4 Backend: Python ETL** | `backend` label on `.py` pipelines; SQL injection flagged |
| **#5 Custom consumer skill** | Team `pipeline-standards` skill catches missing `owner`/`sla_hours` |
| **#6 Infra: Terraform + CI** | `infra` label → `iac-safety` + `ci-workflow-hardening` |
| **#7 Skip review** | `skip-review` label / `[skip prevue]` title — neutral check, no engine spend |

## Live demo script

Full presenter notes: [docs/DEMO.md](docs/DEMO.md)

### 5-minute arc

1. Open **PR #1** — show sticky summary Metadata (labels + matched globs), inline SQL findings, `prevue/review` check.
2. Open **PR #2** — security finding at error severity; check fails (`min_severity_to_fail: error`).
3. Open **PR #3** — Metadata shows `data` **and** `infra` labels (multi-label union).
4. On **PR #1**, push a small fix → incremental re-review (delta only). Comment `/prevue review` for full re-run.
5. On a finding, comment `/prevue dismiss <fingerprint> reason: demo` then `/prevue resolve <id>`.

### Pipeline (remind audience)

```
PR submit → fetch diff → classify → route → load skills → review → sticky + inline + check
```

Classification is deterministic-first (zero tokens for clear-cut paths). Ambiguous files can use LLM fallback (`classification.fallback.enabled`).

## Project layout (fictional warehouse)

```
pipelines/          # Python ETL jobs
migrations/         # Flyway-style SQL
terraform/          # AWS infra for the lakehouse
dbt/                # dbt models (placeholder)
```

This is demo scaffolding — not production code.
