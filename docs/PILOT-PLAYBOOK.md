# Pilot playbook — 4 weeks, 5–8 engineers

Prove people impact after toolkit proof (`make test`).

## Week 0 — prep

- [ ] Teams marketplace + Required plugin live ([ADMIN-SETUP.md](ADMIN-SETUP.md))
- [ ] App repo Trailhead merged to `main`
- [ ] Baseline worksheet in [METRICS.md](METRICS.md)
- [ ] Pick 5–8 engineers (mix of junior + mid)
- [ ] Assign platform buddy for fork/remote questions

## Week 1 — orientation

- Engineers: `make setup`, `/welcome-onboard`, read [CONTRIBUTION-WORKFLOW.md](CONTRIBUTION-WORKFLOW.md)
- Goal: everyone has fork + feature branch ready
- Log blockers (fork policy, Windows hooks, cloud secrets)

## Week 2 — first PR

- Engineers: `/scaffold-first-contribution` → first PR to stand-in or real library
- Track: `make check` failures caught before push vs in review
- Platform: no Trailhead changes unless `make test` fails

## Week 3 — tighten

- Optional: `/qa-test-review` on first PRs
- Compare review comments — style vs logic
- Bump plugin only if company rule gap found

## Week 4 — retrospective

- Fill metrics spreadsheet
- Decision: expand cohort, adjust rules, or pin manifest
- Document stuck items for IT (SSO, secrets, Windows)

## Escalation

| Blocker | Owner |
|---------|-------|
| Fork policy | IT / GitHub admin |
| Teams license | Procurement |
| Hook on Windows | WSL mandate or defer hooks |
| Cloud git push | Cursor Secrets + security review |
