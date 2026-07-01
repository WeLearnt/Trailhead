---
name: pre-push-quality-gate
description: Run all quality checks before pushing code. Catches deprecated APIs, missing tests, and convention gaps. Use before git push or when the user asks to validate their changes.
---

# Pre-Push Quality Gate

Run this before every `git push`. Three gates: Cursor while coding → Trailhead before push → customer CI on the PR.

## Step 1: Library-specific checks

```bash
make check
```

`trailhead-check.py` enforces:
- Deprecated API usage (`scripts/deprecated-apis.json`)
- Mirrored test files for modules with public functions
- `pytest --collect-only` smoke

Generic style (wildcard imports, etc.) is enforced by **their CI (Ruff)** — not duplicated here.

## Step 2: Run tests

```bash
make test-standin
```

All stand-in tests must pass.

## Step 3: Convention review

- [ ] PR title has correct prefix (`ENH:`, `BUG:`, etc.)
- [ ] New public functions have type annotations and docstrings
- [ ] Test file mirrors source path
- [ ] No deprecated APIs
- [ ] Tests assert real behavior (not just `is not None`)

## Step 4: Bugbot review (optional, Teams)

If available, run `/review` and fix findings before push.

## Step 5: Report

```
Quality Gate Results
────────────────────
✅/❌ make check (trailhead-check.py)
✅/❌ make test-standin
✅/❌ convention review
✅/❌ Bugbot (if run)

Ready to push: YES/NO
```

Push hooks also run `make check` — failures block `git push` in a trusted workspace.
