# Trailhead — Agent Context (pandas stand-in app repo)

This repository is **WeLearnt/Trailhead** — the app-repo layer of Trailhead onboarding.

Stand-in library: [pandas](https://github.com/pandas-dev/pandas) (demo slice in `examples/pandas-standin/`).

**Org repo:** https://github.com/WeLearnt/Trailhead

## Three layers (Cursor-native)

| Layer | Source | What it provides |
|-------|--------|------------------|
| **Team Rules** | Cursor dashboard (enforced) | 2–3 non-negotiable bullets |
| **Required plugin** | `org-trailhead` via Team Marketplace | Company Python + security rules; `/welcome-onboard`, `/pm-plan-change`, `/qa-test-review` |
| **App repo** | This git repo | Repo rules, `/scaffold-first-contribution`, `/pre-push-quality-gate`, `trailhead-check.py`, hooks |

Precedence: Team Rules → plugin rules → `.cursor/rules/repo-*.mdc`.

Pin plugin version in `trailhead-manifest.json` for MR visibility.

## Layout

```
examples/pandas-standin/              # Demo library slice
examples/cursor-trailhead-company-plugin/  # Import to Team Marketplace
.cursor/rules/repo-*.mdc              # Library-specific conventions
.cursor/skills/                       # App-repo workflows
scripts/trailhead-check.py            # Library-specific deterministic gate
trailhead-manifest.json               # company_plugin version pin
docs/                                 # Runbooks and demo guides
```

## Contribution workflow (summary)

1. Fork WeLearnt repo (`WeLearnt/Trailhead`); add `upstream` remote
2. `make setup` (local) or Cloud Dev Environment (see `docs/CLOUD-ONBOARDING.md`)
3. Feature branch from synced `main`
4. `/scaffold-first-contribution` → code + mirrored tests
5. `make check` → `/pre-push-quality-gate` → `git push` (hook re-runs check)
6. Open PR to `upstream` — **their CI unchanged** (Ruff, coverage, full pytest)

Full process: [docs/CONTRIBUTION-WORKFLOW.md](docs/CONTRIBUTION-WORKFLOW.md).

## Three pre-review gates

1. **Cursor while coding** — rules + skills
2. **Trailhead before push** — `trailhead-check.py` + push hook
3. **Their CI on PR** — Ruff, coverage, full test suite

## Maintaining Trailhead

Platform team owns rules, skills, `deprecated-apis.json`, and manifest bumps. See [docs/MAINTAINING-TRAILHEAD.md](docs/MAINTAINING-TRAILHEAD.md). Run `make test` before merging Trailhead changes.

## Security

- Approved packages: `scripts/approved-packages.txt`
- No external code ingestion (Team Rules + company plugin)
- Push hooks require **trusted workspace**
