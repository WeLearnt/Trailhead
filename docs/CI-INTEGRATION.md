# CI integration — additive one-liner

Trailhead does **not** add a new GitHub Actions workflow in v1. Your existing CI (Ruff, coverage, full pytest) stays canonical.

## Optional: call Trailhead in existing CI

Add to your current lint/test job:

```bash
pip install -r requirements-dev.txt
python scripts/trailhead-check.py --verify-manifest examples/pandas-standin/
```

This enforces library-specific checks for **all contributors**, including non-Cursor editors.

## Division of labor

| Check | Owner |
|-------|-------|
| Wildcard imports, style, complexity | **Your CI (Ruff)** |
| Deprecated APIs, test mirror, collect-only | **trailhead-check.py** |
| Coverage threshold | **Your CI** |
| Weak test quality | **QA skill + human review** |

## When Trailhead passes but CI fails

1. Read CI log — usually Ruff or coverage
2. Fix in branch; `make check` does not duplicate Ruff
3. See triage section in [MAINTAINING-TRAILHEAD.md](MAINTAINING-TRAILHEAD.md)

## Bugbot

Optional pre-push `/review` on Teams — not a CI replacement.
