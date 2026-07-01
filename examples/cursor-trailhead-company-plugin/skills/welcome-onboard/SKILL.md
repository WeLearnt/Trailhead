---
name: welcome-onboard
description: Orient a new engineer after setup — what Trailhead configured and what to do next. Use on day 1 or when the user asks how to get started.
---

# Welcome Onboard

Greet the engineer and confirm they are on the **app repo** with Trailhead enabled.

## What already happened (zero install on Teams)

- **Required plugin `org-trailhead`** — company Python + security rules (Customize → Plugins)
- **Team Rules** — enforced org policies (no external code, approved packages)
- **App repo** — library-specific rules, scaffold skill, local check script, hooks

## What they should do now

1. Confirm fork + `upstream` remote (see `docs/CONTRIBUTION-WORKFLOW.md`)
2. Run `make setup` (or use Cloud Dev Environment — see `docs/CLOUD-ONBOARDING.md`)
3. Enable **trusted workspace** so push hooks run
4. Run `/scaffold-first-contribution` for their first change
5. Before push: `make check` or `/pre-push-quality-gate`

## Key commands

| Command | Purpose |
|---------|---------|
| `make setup` | One-time local onboarding |
| `make check` | Library-specific pre-push checks |
| `make test` | Trailhead strength test + stand-in tests |
| `/scaffold-first-contribution` | Guided first PR |
| `/pre-push-quality-gate` | Full pre-review checklist |

## Docs map

- Process: `docs/CONTRIBUTION-WORKFLOW.md`
- Cloud path: `docs/CLOUD-ONBOARDING.md`
- Maintaining Trailhead: `docs/MAINTAINING-TRAILHEAD.md`
