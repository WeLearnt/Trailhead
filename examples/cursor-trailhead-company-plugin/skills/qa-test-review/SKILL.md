---
name: qa-test-review
description: Review test coverage and quality for a change. Identifies gaps, edge cases, and regression risks. Use during code review or before merge.
disable-model-invocation: true
---

# QA — Test Review

Analyze test coverage and quality for a pending change. Produce actionable feedback for the engineer.

## Step 1: Identify the Change Scope

Determine which files were modified:
```bash
git diff --name-only main...HEAD
```

Or ask the user which files/PR to review.

## Step 2: Map Source to Tests

For each modified source file under `examples/pandas-standin/pandas/core/`:
- Expected test: `pandas/tests/core/<same-path>/test_<module>.py`
- Check if test file exists and was updated

## Step 3: Coverage Gap Analysis

For each new or modified public function, verify:

| Requirement | Present? | Notes |
|-------------|----------|-------|
| Happy-path test | ✅/❌ | Normal input → expected output |
| Edge case test | ✅/❌ | Empty, single element, boundary values |
| Error case test | ✅/❌ | Invalid input → correct exception |
| Parametrize variants | ✅/❌ | Multiple input types tested |

## Step 4: Regression Risk Assessment

Check:
- [ ] Existing tests still pass (`make test-standin`)
- [ ] No tests were deleted without justification
- [ ] Changed behavior has updated assertions (not just added tests)
- [ ] Deprecated API usage in tests (tests should use current APIs)

## Step 5: Generate Review Report

```markdown
## Test Review: <PR title or file scope>

### Coverage Summary
- Functions reviewed: N
- Fully covered: N
- Gaps found: N

### Gaps (must fix before merge)
1. `<function_name>` in `<file>` — missing edge case for <scenario>
2. `<function_name>` in `<file>` — no error case for <invalid input>

### Suggestions (nice to have)
1. Consider parametrizing <test> over <variants>
2. Add regression test for <related scenario>

### Regression Risks
- <any concerns about existing behavior changing>

### Verdict: PASS / NEEDS WORK
```

## QA Does Not Need To

- Write the tests (unless asked)
- Understand implementation details
- Run the full test suite manually (use `make test-standin`)
