# Demo Setup Checklist

Complete these once before the live demo. Reviews will fail at engine install without the Copilot token.

## 1. Add repository secret

**Settings → Secrets and variables → Actions → New repository secret**

| Name | Value |
|------|-------|
| `COPILOT_GITHUB_TOKEN` | Fine-grained **user** PAT (`github_pat_…`) with **Copilot Requests** permission |

Do not use the default `GITHUB_TOKEN` — Copilot CLI requires a user-owned PAT.

## 2. Re-run failed workflow jobs

After adding the secret:

```bash
gh run list --repo Doki064/test-sandbox-repo --workflow "Prevue Review" --limit 10
gh run rerun <run-id> --repo Doki064/test-sandbox-repo --failed
```

Or close/reopen each demo PR, or push an empty commit to trigger `synchronize`.

## 3. Optional — branch protection demo

To show PR #2 blocking merge:

1. **Settings → Branches → Add rule** on `main`
2. Require status check: `prevue/review` (not `prevue / review` job name)
3. PR #2 (security) should remain unmergeable until credentials are removed

## 4. Optional — `skip-review` label

Create label for PR #7 dual-trigger demo:

```bash
gh label create skip-review \
  --repo Doki064/test-sandbox-repo \
  --color BFD4F2 \
  --description "Skip Prevue AI review"
gh pr edit 7 --repo Doki064/test-sandbox-repo --add-label skip-review
```

PR #7 already skips via title `[skip prevue]` even without the label.

## 5. Presenter doc

Walkthrough script: [DEMO.md](./DEMO.md)
