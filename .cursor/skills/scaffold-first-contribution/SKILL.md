---
name: scaffold-first-contribution
description: Guide a new engineer through scaffolding a correct first contribution following library conventions. Use when onboarding, starting a first PR, or when the user asks how to contribute.
---

# Scaffold First Contribution

Walk the engineer through a convention-compliant first change without requiring them to read the whole codebase.

## Step 0: Verify fork and remotes

Before editing code, confirm the engineer workflow:

```bash
git remote -v
```

Required:
- `origin` → engineer's fork
- `upstream` → WeLearnt canonical repo (`WeLearnt/Trailhead`)

If `upstream` is missing, stop and show:

```bash
git remote add upstream https://github.com/WeLearnt/Trailhead.git
git fetch upstream
git checkout main
git pull upstream main --ff-only
```

See `docs/CONTRIBUTION-WORKFLOW.md` for the full fork → branch → PR path.

## Step 1: Understand the change

Ask the user:
1. What type of change? (`ENH`, `BUG`, `DOC`, `TST`, `PERF`, `TYP`, `CLN`)
2. What area of the library? (ops, dtypes, indexing, io, etc.)
3. Is there a linked GitHub issue?

Map their answer to a PR title prefix and target directory under `examples/pandas-standin/pandas/`.

## Step 2: Find the right location

Search the stand-in codebase for similar existing code:

```
examples/pandas-standin/pandas/core/<area>/
```

Read 1–2 neighboring modules to understand patterns. Do NOT read the entire tree.

## Step 3: Scaffold source + tests together

For every new public function:
1. Add the function to the appropriate source file
2. Create or update the mirrored test file:
   - Source: `pandas/core/<area>/<module>.py`
   - Test: `pandas/tests/core/<area>/test_<module>.py`
3. Include type annotations and NumPy-style docstring
4. Write happy-path, edge-case, and error-case tests

## Step 4: Validate before presenting

```bash
make check
make test-standin
```

Fix any failures before presenting the change.

## Step 5: Prepare PR metadata

Present to the user:
- **PR title**: `<PREFIX>: <concise description>`
- **PR description** using the repo template (`.github/PULL_REQUEST_TEMPLATE.md`)

## Do not

- Create files outside `examples/pandas-standin/pandas/`
- Use deprecated APIs from `scripts/deprecated-apis.json`
- Skip tests for new public functions
- Copy code from external sources
