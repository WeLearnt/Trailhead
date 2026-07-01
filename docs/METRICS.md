# Metrics — measuring onboarding impact

Trailhead v1 does not ship an analytics dashboard. Priya's team measures impact with a spreadsheet during pilot.

## Toolkit proof (technical)

```bash
make test   # must pass before rollout and after Trailhead changes
```

## People proof (pilot)

Use during 4-week pilot with 5–8 engineers. See [PILOT-PLAYBOOK.md](PILOT-PLAYBOOK.md).

## Baseline worksheet (fill before pilot)

| Metric | Baseline (Meridian Systems) | Target after 4 weeks |
|--------|---------------------|----------------------|
| Days to first merged PR | | |
| Review rounds on first PR | | |
| Convention issues caught pre-review | | |
| % first PRs needing style-only rework | | |

## Per-engineer log (weekly)

| Engineer | Week | First PR opened? | `make check` used? | Review rounds | Notes |
|----------|------|------------------|--------------------|---------------|-------|
| | | | | | |

## Success criteria (suggested)

- Median time to first merged PR ↓ 50%+
- First PR review rounds ≤ 2 for ≥ 70% of pilot cohort
- Platform team can merge Trailhead config change without vendor help (`make test` green)

## What we do not measure in v1

- Cursor usage analytics API automation
- Per-rule effectiveness scores
- Automated GitHub API reporting
