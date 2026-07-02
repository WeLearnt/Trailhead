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

## Cursor Cloud specific instructions

Pure-Python tooling repo — no server, web app, or long-running services. Dependencies are just `numpy` + `pytest` (`requirements-dev.txt`). The cloud environment is defined by `.cursor/environment.json` (builds `.cursor/Dockerfile`), so environment changes belong in those files, not a snapshot.

- Run everything via the root `Makefile`: `make check` (deterministic gate = this repo's "lint"), `make test-standin`, `make test-trailhead`, and `make test` (all three). See README/Makefile for the exact commands.
- There is no Ruff/other linter in this repo; generic style is enforced only by upstream CI. `make check` (`scripts/trailhead-check.py`) is the local gate.
- `make setup` (and only that target) hard-fails without a git `upstream` remote. Use `TRAILHEAD_SKIP_FORK_CHECK=1` for local/cloud dev. Plain `make test`/`make check` do not need the remote.
- Stand-in tests import an in-place `pandas` package with no install step; the Makefile already sets `PYTHONPATH=.` for `test-standin`. Replicate that if running pytest by hand from `examples/pandas-standin/`.
- `pip install` places the `pytest` console script in `~/.local/bin` (not on PATH); invoke as `python3 -m pytest` (the Makefile already does).
