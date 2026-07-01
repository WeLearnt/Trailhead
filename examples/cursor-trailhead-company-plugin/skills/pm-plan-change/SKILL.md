---
name: pm-plan-change
description: Help PMs plan a library change with acceptance criteria, test requirements, and risk assessment. Use when planning features, writing issues, or scoping work for engineering.
disable-model-invocation: true
---

# PM — Plan a Change

Help the PM write a clear, actionable issue that engineering can pick up without back-and-forth.

## Step 1: Gather Context

Ask the PM:
1. What user problem does this solve?
2. Who is affected? (internal teams, external users, specific workflows)
3. Is this a new feature, bug fix, or improvement to existing behavior?
4. Any deadline or dependency?

## Step 2: Classify the Change

Map to a PR prefix:
| Type | Prefix | Example |
|------|--------|---------|
| New feature | `ENH:` | `ENH: Add rolling window aggregation` |
| Bug fix | `BUG:` | `BUG: Fix off-by-one in date range filter` |
| Documentation | `DOC:` | `DOC: Update migration guide for v3` |
| Test improvement | `TST:` | `TST: Add edge case tests for null handling` |
| Performance | `PERF:` | `PERF: Vectorize groupby aggregation` |
| Type annotations | `TYP:` | `TYP: Add stubs for io module` |
| Code cleanup | `CLN:` | `CLN: Remove deprecated ix accessor` |

## Step 3: Generate Issue Template

```markdown
## Problem
<user-facing problem statement>

## Proposed Solution
<high-level approach — NOT implementation details>

## Acceptance Criteria
- [ ] <criterion 1 — testable>
- [ ] <criterion 2 — testable>
- [ ] <criterion 3 — testable>

## Test Requirements
Engineering must include:
- [ ] Happy-path test for <scenario>
- [ ] Edge case: <boundary condition>
- [ ] Error case: <invalid input behavior>

## Risk Assessment
- Breaking change: YES/NO
- Deprecation needed: YES/NO
- Affects public API: YES/NO
- Requires new dependency: YES/NO (must be approved by platform team)

## Suggested PR Title
`<PREFIX>: <concise description>`

## Out of Scope
- <what this issue does NOT cover>
```

## Step 4: Flag Risks

Alert the PM if:
- The change requires a new dependency (needs platform approval)
- The change deprecates existing API (needs migration guide)
- The change affects a core module many teams depend on (needs extra review)

## PM Does Not Need To

- Understand Python or the codebase structure
- Write tests or code
- Know which files to modify

Engineering uses `/scaffold-first-contribution` to implement from this issue.
