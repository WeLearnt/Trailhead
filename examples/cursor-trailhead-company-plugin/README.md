# org-trailhead — Company plugin package

Import this directory (or a dedicated repo with the same layout) to **Cursor Team Marketplace**. Mark **Required** for zero-install company standards.

## Contents

| Path | Purpose |
|------|---------|
| `.cursor-plugin/plugin.json` | Plugin manifest (`org-trailhead` v1.2.0) |
| `.cursor-plugin/marketplace.json` | Multi-plugin marketplace root (if single repo) |
| `rules/python-base.mdc` | Company Python conventions |
| `rules/security-base.mdc` | Security boundaries |
| `skills/welcome-onboard/` | Day-1 orientation |
| `skills/pm-plan-change/` | PM issue scaffolding |
| `skills/qa-test-review/` | QA test review |

## App repos pin this version

```json
{
  "company_plugin": {
    "name": "org-trailhead",
    "version": "1.2.0"
  }
}
```

In `trailhead-manifest.json` at the library repo root.

## Admin steps

See [../../docs/ADMIN-SETUP.md](../../docs/ADMIN-SETUP.md).

## Versioning

1. PR in plugin repo → release semver  
2. App repos bump manifest pin  
3. Marketplace auto-refresh on push (GitHub App required)
