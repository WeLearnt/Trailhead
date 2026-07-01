# Docs map — Trailhead vs existing documentation

**Rule for Priya:** Docs stay canonical for narrative. Trailhead makes them **executable at edit time**.

| Trailhead artifact | Replaces wiki? | Maps to (pandas example) |
|--------------------|----------------|--------------------------|
| `python-base.mdc` (plugin) | No | Contributing guide — style section |
| `repo-core-conventions.mdc` | No | PR prefixes, test layout |
| `CONTRIBUTION-WORKFLOW.md` | No | "Submitting a pull request" |
| `deprecated-apis.json` | No | Deprecation policy (machine-readable) |
| `/welcome-onboard` | No | Dev Slack / mailing list orientation |
| `/scaffold-first-contribution` | No | First contribution tutorial |
| `trailhead-check.py` | No | CI lint + deprecation (partial overlap) |
| Team Rules bullets | No | Security policy summary |

## For engineers

> Read the wiki for *why*. Cursor rules and skills enforce *how* while you code. CI still runs on the PR.

## For platform team

When wiki changes:
1. Update canonical doc (unchanged process)
2. Update matching rule/skill/JSON if behavior should change at edit time
3. Run `make test`

## Duplication policy

- **Do not** paste entire wiki into rules — link in skill prose instead
- **Do** encode checkable items in `trailhead-check.py` and JSON configs
