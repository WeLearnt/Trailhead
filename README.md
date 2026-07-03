# Trailhead

**Canonical repo:** https://github.com/WeLearnt/Trailhead

Trailhead is **WeLearnt's Cursor environment toolkit** — configuration, runbooks, and reusable patterns for onboarding engineers onto convention-heavy internal libraries. **Platform and Cursor admins are the primary audience for this repository.** End-user developers do not clone or contribute here; they work in their **library app repos**, where the same Trailhead layers are already applied.

## Who uses what

| Audience | Where they work | What they get automatically |
|----------|-----------------|----------------------------|
| **Cursor / platform admins** | This repo + Cursor dashboard | Setup, publish plugin, Team Rules, roll out to library repos |
| **Library maintainers** | Their library repo (+ PRs here for shared templates) | App-repo rules, skills, hooks, check script |
| **Engineers** | Forked **library repo** only | Required plugin, Team Rules, app-repo skills — zero manual install on Teams |

Engineer day-1 flow lives in the library repo: `make setup` → `/welcome-onboard` → `/scaffold-first-contribution` → `make check` → PR. See [docs/CONTRIBUTION-WORKFLOW.md](docs/CONTRIBUTION-WORKFLOW.md).

## Problem Trailhead solves

Contribution docs exist, but engineers still ship wrong first PRs — deprecated APIs, wrong test layout, avoidable review churn. Trailhead makes standards **executable at edit time** without replacing existing CI.

Three pre-review gates:

1. **Cursor while coding** — rules and skills
2. **Trailhead before push** — deterministic checks and a git push hook
3. **CI on the PR** — unchanged (Ruff, coverage, full pytest)

## Cursor-native features

| Feature | Role at WeLearnt |
|---------|------------------|
| **Team Rules** | Enforced org policies in the dashboard (short non-negotiable bullets) |
| **Team Marketplace** | Distribute the company plugin from a GitHub repo |
| **Required plugin** (`org-trailhead`) | Company-wide rules and skills — auto-installed for every team member |
| **Rules** (`.mdc`) | Company and library conventions injected while coding |
| **Agent skills** | Guided workflows invoked with `/skill-name` in chat |
| **Hooks** (`beforeShellExecution`) | Block `git push` when checks fail (requires trusted workspace) |
| **Cloud Dev Environment** | Optional golden image via `.cursor/environment.json` |

Plugin source to publish: `examples/cursor-trailhead-company-plugin/` → `WeLearnt/cursor-trailhead-company-plugin`.

### Skills by layer

| Skill | Layer | Used by |
|-------|-------|---------|
| `/welcome-onboard` | Company plugin | Engineers — day-1 orientation |
| `/pm-plan-change` | Company plugin | PMs — change planning |
| `/qa-test-review` | Company plugin | QA — test quality review |
| `/scaffold-first-contribution` | App repo (per library) | Engineers — guided first PR |
| `/pre-push-quality-gate` | App repo (per library) | Engineers — pre-push checklist |

## Custom components (not Cursor platform)

| Component | Purpose |
|-----------|---------|
| `scripts/trailhead-check.py` | Library-specific gate — deprecated APIs, mirrored tests, pytest smoke |
| `scripts/deprecated-apis.json` | Machine-readable deprecation policy |
| `scripts/approved-packages.txt` | Package allowlist referenced by Team Rules and plugin |
| `trailhead-manifest.json` | Pins company plugin version for MR visibility |
| `make setup` / `Makefile` | Rollout validation and app-repo health checks |
| `.cursor/hooks/gate-push.sh` | Runs `make check` before push |

Admins copy these into each library repo. Engineers interact with the outcomes, not this canonical repo.

## Architecture

```
Team Rules → Required plugin → App repo config → trailhead-check.py
```

| Layer | Location | Owner |
|-------|----------|-------|
| Team Rules | Cursor dashboard | Platform admin |
| Company plugin | Team Marketplace | Platform team |
| App repo layer | Per-library git repo | Library maintainers |
| Deterministic gate | `trailhead-check.py` in each library | Platform + library owners |

Precedence: Team Rules → plugin rules → app-repo rules. See [docs/RULE-LAYERING.md](docs/RULE-LAYERING.md).

## Admin quick start

1. [docs/ORG-SETUP.md](docs/ORG-SETUP.md) — WeLearnt GitHub org and plugin repo
2. [docs/ADMIN-SETUP.md](docs/ADMIN-SETUP.md) — import marketplace, mark plugin **Required**, set Team Rules
3. [docs/MAINTAINING-TRAILHEAD.md](docs/MAINTAINING-TRAILHEAD.md) — ongoing ownership
4. Roll out app-repo config (`.cursor/rules/`, `.cursor/skills/`, hooks, check script, manifest) to each library repo

Validate this template before rollout:

```bash
TRAILHEAD_SKIP_FORK_CHECK=1 make setup
make check
make test
```

## Documentation

| Doc | Audience |
|-----|----------|
| [docs/ADMIN-SETUP.md](docs/ADMIN-SETUP.md) | Cursor admins — one-time Teams setup |
| [docs/ORG-SETUP.md](docs/ORG-SETUP.md) | GitHub org and plugin publish |
| [docs/MAINTAINING-TRAILHEAD.md](docs/MAINTAINING-TRAILHEAD.md) | Platform team runbook |
| [docs/APPROACH.md](docs/APPROACH.md) | Strategy, scope, and what we skipped |
| [docs/CONTRIBUTION-WORKFLOW.md](docs/CONTRIBUTION-WORKFLOW.md) | Engineer fork workflow (for library repos) |
| [docs/DOCS-MAP.md](docs/DOCS-MAP.md) | Wiki vs Trailhead coexistence |
| [docs/DEMO-WALKTHROUGH.md](docs/DEMO-WALKTHROUGH.md) | Live demo script |

## What Trailhead does not do

- No new CI workflow YAML (optional one-liner in [docs/CI-INTEGRATION.md](docs/CI-INTEGRATION.md))
- No deploy pipeline changes
- No auto-fork — library repos fail with instructions if fork workflow is missing
