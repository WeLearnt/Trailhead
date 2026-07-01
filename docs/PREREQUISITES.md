# Prerequisites — Jack's demo checklist

## Cursor license (locked: Tier C)

| Item | Cost |
|------|------|
| Teams Standard × 2 | **$80/mo** ($64/mo annual) |
| Enterprise | **Not required** |

**Seat 1** (or Unpaid Admin): marketplace + Team Rules setup  
**Seat 2**: fresh engineer login for live demo

Set team spending limit **$0–$20** for on-demand usage safety.

## Accounts

- [ ] GitHub account #1 — hosts demo app repo
- [ ] GitHub account #2 — engineer fork for PR flow
- [ ] Cursor Teams org with both seats invited

## Before sitting with Priya

- [ ] Plugin imported + **Required** (`docs/ADMIN-SETUP.md`)
- [ ] Team Rules: 2–3 enforced bullets
- [ ] Seat 2 never manually installed plugin
- [ ] Engineer fork + `upstream` remote on Seat 2
- [ ] `TRAILHEAD_SKIP_FORK_CHECK=1` only for local dev without fork
- [ ] `make setup` green on Seat 2
- [ ] `make test` green
- [ ] Trusted workspace enabled on Seat 2 (for push hooks)
- [ ] Deliberate violation staged for `make check` demo (deprecated API or missing test)
- [ ] `docs/APPROACH.md` open for judgment conversation

## Cursor version

- Cursor 3.7+ recommended (Bugbot `/review` optional in pre-push skill)
- Project hooks require **trusted workspace**

## Windows note

Project hooks use bash. Windows teams should use **WSL** for reliable hook behavior.

## Simulated path (not Jack's tier)

Pro ($20/mo) can run app-repo rules/skills/hooks but must simulate company layer from `examples/cursor-trailhead-company-plugin/`. Jack's demo uses live Teams — no simulation.
