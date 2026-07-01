---
name: devops-deploy-check
description: Read-only pre-merge checklist for engineers — does not modify CI/CD. Use before asking for merge or when validating release readiness.
disable-model-invocation: true
---

# DevOps Pre-Merge Checklist (read-only)

Trailhead does **not** modify deploy pipelines or CI workflows. This skill is a lightweight checklist before merge.

## Before requesting merge

- [ ] `make check` passes locally
- [ ] `make test-standin` passes
- [ ] PR opened against `upstream` (not direct push to org `main`)
- [ ] Customer CI on the PR is green (Ruff, coverage, full pytest)
- [ ] `trailhead-manifest.json` bumped if `company_plugin.version` changed
- [ ] Release notes / changelog updated if the library ships versioned releases

## What Trailhead does not do

- No deploy triggers
- No merge queue changes
- No new GitHub Actions workflows in this demo

See `docs/CI-INTEGRATION.md` for optional one-liner to call `trailhead-check.py` from existing CI.
