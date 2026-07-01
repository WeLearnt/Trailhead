# Trailhead

**Trailhead** is a demo/reference implementation of Cursor-native engineer onboarding for convention-heavy internal libraries. It encodes standards into rules, skills, hooks, and a thin check script — without rebuilding CI/CD.

This repo uses a **pandas stand-in** (`examples/pandas-standin/`) so you can demo first contributions without cloning 3,500 files.

## Quick start

```bash
# After fork + upstream remote are configured (see docs/CONTRIBUTION-WORKFLOW.md)
make setup          # one-command onboarding (set TRAILHEAD_SKIP_FORK_CHECK=1 for local-only)
make check          # library-specific pre-push checks
make test           # strength test + stand-in pytest
```

In Cursor:
- `/welcome-onboard` — day-1 orientation (company plugin)
- `/scaffold-first-contribution` — guided first PR (app repo)
- `/pre-push-quality-gate` — pre-push checklist

## Architecture

```
Team Rules (enforce) + Required plugin (company) + app repo config + trailhead-check.py
```

| Layer | Location |
|-------|----------|
| Company plugin | `examples/cursor-trailhead-company-plugin/` → Team Marketplace |
| App repo rules/skills | `.cursor/rules/repo-*.mdc`, `.cursor/skills/` |
| Deterministic gate | `scripts/trailhead-check.py` |
| Version pin | `trailhead-manifest.json` |

See [docs/RULE-LAYERING.md](docs/RULE-LAYERING.md) and [docs/APPROACH.md](docs/APPROACH.md).

## Demo customer

**WeLearnt** — B2B data platform company. **Priya Nair** (Platform Engineering Lead) is the buyer persona. GitHub org: [`WeLearnt`](https://github.com/WeLearnt). Setup: [docs/ORG-SETUP.md](docs/ORG-SETUP.md).

## Demo with Priya (Teams × 2 seats)

Jack's locked demo tier: **$80/mo** for two Teams Standard seats — admin setup + fresh engineer login. See [docs/PREREQUISITES.md](docs/PREREQUISITES.md) and [docs/DEMO-WALKTHROUGH.md](docs/DEMO-WALKTHROUGH.md).

## Docs

| Doc | Purpose |
|-----|---------|
| [docs/APPROACH.md](docs/APPROACH.md) | Strategy for Priya |
| [docs/DEMO-WALKTHROUGH.md](docs/DEMO-WALKTHROUGH.md) | Live demo script |
| [docs/ADMIN-SETUP.md](docs/ADMIN-SETUP.md) | One-time Teams admin setup |
| [docs/MAINTAINING-TRAILHEAD.md](docs/MAINTAINING-TRAILHEAD.md) | Platform team runbook |
| [docs/DOCS-MAP.md](docs/DOCS-MAP.md) | Coexistence with existing wiki docs |

## What Trailhead does not do

- No new CI workflow YAML (optional one-liner documented)
- No deploy pipeline changes
- No auto-fork (fails with instructions if fork missing)
