# Prevue Live Demo — Presenter Guide

Audience: data engineering teammates. Repo: `Doki064/test-sandbox-repo`.

## Before the room

1. Confirm `CURSOR_API_KEY` is set under **Settings → Secrets → Actions**.
2. Open all demo PRs in browser tabs (see README catalog).
3. Optional: branch protection on `main` requiring check `prevue/review` — shows merge gate on PR #2.

## Story arc (≈15 min)

### 1. Problem framing (1 min)

Full-context AI review burns tokens loading irrelevant guidelines. Prevue classifies the diff, loads **only** matching skill bundles, posts sticky summary + inline comments + a pass/fail check.

### 2. Automatic review — data PR (#1)

**Open:** PR titled *Demo: Data classification — unsafe SQL migration*

**Show:**

- Actions run on `pull_request` (opened / synchronize / ready_for_review).
- Sticky comment **Metadata** section: label `data`, matched glob `**/migrations/**`.
- Inline comments from built-in skills `sql-safety`, `migrations`.
- **Coverage** section if partial (usually full for this small PR).
- Check run `prevue/review` — neutral or failure depending on findings.

**Say:** Deterministic classifier matched `migrations/001_add_events_table.sql` at **zero classification tokens**. Router loaded the `data` bundle only — not frontend, not infra.

**Intentional issues in diff:**

- `ALTER TABLE ... ADD COLUMN ... NOT NULL` without default/backfill (migration lock risk).
- `DELETE FROM staging_events` without `WHERE` (destructive SQL).

### 3. Security gate (#2)

**Open:** PR *Demo: Security classification — committed credentials*

**Show:**

- Metadata label `security` (paths under `config/` or `.env`).
- Inline at **error** severity for hardcoded API key / connection string.
- Check `prevue/review` → **failure** because `min_severity_to_fail: error` in `.github/prevue.yml`.

**Say:** Same pipeline, different bundle. Security skills always pack first (canonical label order).

### 4. Multi-label union (#3)

**Open:** PR *Demo: Multi-label routing — SQL migration + Terraform*

**Show:**

- Metadata lists **both** `data` and `infra` with their matched globs.
- Findings span SQL safety and IaC (public S3 ACL, open security group).

**Say:** Prevue does not pick a single “dominant” label. Multi-domain PRs get the **union** of skill bundles (D-01).

### 5. Backend Python ETL (#4)

**Open:** PR *Demo: Backend classification — Python ETL with SQL injection*

**Show:**

- `backend` label on `pipelines/*.py`.
- String-built SQL with user input flagged.

**Say:** `.py` files route to backend bundle; overlap with `data` globs on `pipelines/**` can also apply `data` skills where `applies-to` matches.

### 6. Custom consumer skill (#5)

**Open:** PR *Demo: Custom skill — pipeline standards*

**Show:**

- Finding about missing `owner` / `sla_hours` docstring from `.github/prevue/skills/data/pipeline-standards.md`.
- Sticky **Skills** section lists consumer skill loaded.

**Say:** Teams add `SKILL.md` files under `.github/prevue/skills/`. Same bundle/filename replaces a built-in; new filenames add alongside.

### 7. Infra-only (#6)

**Open:** PR *Demo: Infra classification — Terraform and GitHub Actions*

**Show:**

- `infra` label for `*.tf` and `.github/workflows/**`.
- `iac-safety` + `ci-workflow-hardening` findings.

### 8. Skip policy (#7)

**Open:** PR *Demo: Skip review — label and title patterns* (has `skip-review` label)

**Show:**

- Neutral `prevue/review` check with skip reason in sticky comment.
- No Copilot/engine run in logs.

**Alternative:** PR title starting with `[skip prevue]` hits `skip_title_patterns`.

### 9. Incremental lifecycle (live, on PR #1)

1. Merge or fix one issue on PR #1 branch; push.
2. Second Actions run reviews **only files changed since last sticky head SHA** (incremental).
3. Outdated inline threads auto-resolve when `resolve_outdated: true`.
4. Comment `/prevue review` on the PR → forced full re-review (command workflow).

### 10. `/prevue` commands (live)

| Command | Demo action |
|---------|-------------|
| `/prevue review` | Force full re-review after incremental |
| `/prevue dismiss <id> reason: …` | Dismiss false positive; `reason:` required for errors |
| `/prevue resolve <id>` | Collapse outdated thread |
| `/prevue status` | Show sticky state (no engine) |

Requires **write** access; fork PRs refused.

## Config highlights to mention

From `.github/prevue.yml`:

```yaml
review:
  min_severity_to_fail: error   # PR #2 fails the check
  incremental: true
  resolve_outdated: true

classification:
  fallback:
    enabled: true               # LLM only for unmatched paths in packed set

skip:
  skip_labels: [skip-review]
  skip_title_patterns: ["^\\[skip prevue\\]"]
```

## FAQ prep

| Question | Answer |
|----------|--------|
| Fork PRs? | Skipped in v1 (untrusted head). |
| Token cost on clear SQL PR? | Zero for classification; engine only for review. |
| Custom rules without code? | `labels` + `ignore` globs in `prevue.yml`. |
| Required check name? | `prevue/review` (not the Actions job name). |
| Engine options? | `copilot-cli`, `claude-code-cli`, `cursor-cli` via workflow input. |

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| Workflow does not run | Draft PR — mark ready for review |
| Review skipped instantly | Bot author, `skip-review` label, or fork |
| No findings | Check Actions logs; confirm `CURSOR_API_KEY` |
| Config ignored | `prevue.yml` must be on **base** branch, not PR head only |

## Links

- Prevue repo: https://github.com/Doki064/prevue
- Consumer setup: https://github.com/Doki064/prevue/blob/main/docs/consumer-setup.md
- Configuration reference: https://github.com/Doki064/prevue/blob/main/docs/configuration.md
