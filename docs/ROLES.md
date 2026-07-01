# Roles — Trailhead entry points

One toolkit; role-specific skills. Engineers are primary; PM/QA are lightweight.

| Role | Skill | Location | What it does |
|------|-------|----------|--------------|
| **New engineer** | `/welcome-onboard` | Company plugin | Day-1 orientation after setup |
| **Engineer** | `/scaffold-first-contribution` | App repo | Fork → branch → code → tests |
| **Engineer** | `/pre-push-quality-gate` | App repo | `make check` + convention checklist |
| **PM** | `/pm-plan-change` | Company plugin | Issue template with acceptance criteria |
| **QA** | `/qa-test-review` | Company plugin | Coverage gaps, weak tests |
| **Anyone** | `/devops-deploy-check` | App repo | Read-only pre-merge checklist (no CI edits) |

## Engineer path (P0)

```
make setup → /welcome-onboard → /scaffold-first-contribution → make check → /pre-push-quality-gate → PR
```

## PM / QA (secondary)

Output is markdown for Jira/GitHub — not a new PM or QA tool. QA catches **weak tests** that `trailhead-check.py` does not AST-enforce.

## Admin (platform)

[docs/ADMIN-SETUP.md](ADMIN-SETUP.md) — marketplace, Required plugin, Team Rules.
