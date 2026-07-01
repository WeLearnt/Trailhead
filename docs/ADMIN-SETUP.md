# Admin setup — Team Marketplace + Team Rules

One-time setup for Priya's platform team. Requires **Cursor Teams** (Jack's demo: 2 Standard seats, $80/mo).

## Prerequisites

- Team admin access (Seat 1 or Unpaid Admin)
- GitHub repo containing `examples/cursor-trailhead-company-plugin/` (or dedicated `meridian-systems/cursor-trailhead-company-plugin` repo)
- Cursor GitHub App installed on the org (for marketplace auto-refresh on push)

## Step 1: Import team marketplace

1. Cursor Dashboard → **Settings** → **Plugins** → **Team Marketplaces**
2. **Import** → paste GitHub repo URL
3. Review parsed plugins (`org-trailhead` from `.cursor-plugin/marketplace.json`)
4. Save marketplace

## Step 2: Mark plugin Required

1. Open imported marketplace → `org-trailhead`
2. Enable **Required** so every team member receives rules/skills automatically
3. Optional: set **Team Access** groups for staged rollout

## Step 3: Team Rules (enforce-only)

Dashboard → **Team Rules** → add 2–3 bullets, enable **enforce**:

- Never copy code from external sources (Stack Overflow, gists, unknown repos)
- Use only approved packages per app repo `scripts/approved-packages.txt`
- Do not commit secrets or credentials

Keep the full style guide in the plugin — not in Team Rules.

## Step 4: App repo per library

For each library repo:

1. Add Trailhead app config (rules, skills, hooks, `trailhead-check.py`, manifest)
2. Set `trailhead-manifest.json` → `company_plugin.version` matching published plugin
3. Document fork workflow in `docs/CONTRIBUTION-WORKFLOW.md`

## Step 5: Verify (Seat 2 / new engineer)

1. Fresh Cursor login on team
2. Customize → Plugins → confirm `org-trailhead` installed (Required)
3. Clone app repo → `make setup`
4. `/welcome-onboard`

## Jack's two-seat demo

| Seat | Role |
|------|------|
| Seat 1 / Unpaid Admin | Steps 1–3 above |
| Seat 2 | Step 5 — live zero-install proof for Priya |

## Updating company standards

1. PR in plugin repo → release new semver (e.g. `1.3.0`)
2. App repo PR bumps `trailhead-manifest.json` version pin
3. Marketplace auto-refresh picks up plugin push (if GitHub App configured)

See [RULE-LAYERING.md](RULE-LAYERING.md) and [MAINTAINING-TRAILHEAD.md](MAINTAINING-TRAILHEAD.md).
