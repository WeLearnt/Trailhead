# Maintaining Trailhead — platform team runbook

Your team owns Trailhead without vendor tickets. Everything is plain text in git + one thin Python script.

## Ownership

| Artifact | Owner | Update when |
|----------|-------|-------------|
| Team Rules bullets | Security + platform | Policy change |
| `org-trailhead` plugin | Platform eng | Company-wide convention change |
| App repo `repo-*.mdc` | Platform eng | Library-specific convention |
| `scripts/deprecated-apis.json` | Platform eng | API deprecated |
| `scripts/approved-packages.txt` | Security | Dependency policy |
| `trailhead-manifest.json` | App repo PR | Adopt new plugin version |
| `trailhead-check.py` | Platform eng | New library-specific check |

## Change-mapping table

| Library change | Update | Verify |
|----------------|--------|--------|
| New coding convention | `.cursor/rules/repo-*.mdc` or plugin rule | Agent test + `make check` |
| API deprecated | `scripts/deprecated-apis.json` | `make test` |
| New approved dependency | `scripts/approved-packages.txt` | `make check` |
| PR/branch process | `docs/CONTRIBUTION-WORKFLOW.md` + scaffold skill | Demo walkthrough |
| New deterministic check | `trailhead-check.py` + `tests/test_trailhead.py` | `make test` |
| New role workflow | plugin or app `SKILL.md` | Manual skill invoke |
| Company-wide skill | plugin repo | Marketplace release + manifest bump |

## Extension patterns

- **Add convention:** edit `.mdc` rule or add under plugin `rules/`
- **Add check:** extend `trailhead-check.py` + strength test case
- **Add workflow:** new `SKILL.md` — no compiled code

**Never duplicate:** rules describe intent; JSON + script enforce.

## First time maintaining (30 min)

1. Clone app repo + plugin repo
2. Edit one rule; run `make test`
3. Bump `trailhead-manifest.json` after plugin release
4. Open PR with template checklist

## Rollback bad plugin version

1. Revert plugin repo release or pin app manifest to last good `company_plugin.version`
2. `make setup` reminds engineers to verify plugin version in Customize

## When Trailhead passes but CI fails

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| Ruff failure | Style/import rule | Fix locally; not in trailhead-check |
| Coverage drop | Missing tests | Add tests; Trailhead only checks mirror + collect |
| pytest failure | Logic bug | Fix code |
| Manifest failure | Version below minimum | Bump manifest or lower floor |

## Non-Cursor engineers

Rules/skills/hooks are Cursor-only. `trailhead-check.py` in CI works for everyone — document in [CI-INTEGRATION.md](CI-INTEGRATION.md).
