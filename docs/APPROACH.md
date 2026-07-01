# Trailhead Approach — Response to Priya

**Demo customer:** **Meridian Systems** — fictional B2B data platform company (~800 engineers). **Priya Nair**, Platform Engineering Lead, owns onboarding for convention-heavy internal Python libraries.

## The problem worth solving first

**Time to a correct first PR** — not "learn the entire library." If the first PR is wrong, review cycles multiply. Trailhead targets **days, not weeks**, for convention-compliant first contributions.

## What we built first vs skipped

### Built (this repo)

| Priority | Component | Why |
|----------|-----------|-----|
| 1 | Required plugin + Team Rules | Zero-install company standards (Teams) |
| 2 | `/scaffold-first-contribution` | Guided first PR through fork → branch → tests |
| 3 | `trailhead-check.py` + push hook | Library-specific mistakes before review |
| 4 | `make setup` + cloud golden image | Day-1 friction: fail fast on fork, same stack everywhere |
| 5 | `MAINTAINING-TRAILHEAD.md` + `make test` | Priya's team owns it without Jack |

### Skipped (conscious)

| Item | Why |
|------|-----|
| New CI workflow YAML | Additive one-liner only — see `docs/CI-INTEGRATION.md` |
| Auto-fork | Org policy / identity — fail with instructions |
| `company-simulated.mdc` | Jack uses live Teams two-seat demo |
| Coverage % in Trailhead | Their CI owns it |
| Enterprise features | Teams is sufficient |

## Architecture

Three layers: **Team Rules** → **Required plugin** → **app repo** (rules, skills, check script, hooks). ~80% config, one ~80-line check script.

## Three pre-review gates

1. Cursor rules/skills while coding  
2. `trailhead-check.py` + hook before push  
3. Their CI on PR (Ruff, coverage, full pytest) — **unchanged**

## Expected impact (estimates — validate in pilot)

| Metric | Before | Target |
|--------|--------|--------|
| Days to first merged PR | 2–4 weeks | 3–5 days |
| Review rounds on first PR | 3–5 | 1–2 |
| Convention issues pre-review | ~10% | ~80% |

Measure with [docs/METRICS.md](METRICS.md) + [docs/PILOT-PLAYBOOK.md](PILOT-PLAYBOOK.md).

## What we tried, ruled out, stuck on

| Tried | Ruled out | Stuck on / open |
|-------|-----------|-----------------|
| Rules + skills + thin check script | Rebuilding CI/CD | Windows hook reliability (WSL) |
| Cloud golden image | Cloud-only bypassing PR | Org git token policy for cloud push |
| Manifest plugin version pin | Copying company rules into every app repo | Rolling manifest across N repos (manual v1) |
| Required Team Marketplace plugin | Dashboard-only rules for versioning | — |

## Demo tier (Jack)

**Teams Standard × 2 — $80/mo.** Seat 2 logs in fresh; Required plugin already present. See [docs/PREREQUISITES.md](PREREQUISITES.md).

## Honesty line

> I'll show this the way your engineers experience it — second account, company standards already there, no CI rebuild, platform team maintains via `make test`.

## Docs coexistence

[docs/DOCS-MAP.md](DOCS-MAP.md) — wiki stays canonical; Trailhead encodes guardrails at edit time.
