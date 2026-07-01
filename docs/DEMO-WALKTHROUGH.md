# Demo walkthrough — ~15 minutes (Teams two-seat)

**Audience:** Priya Nair, Platform Engineering Lead, **WeLearnt**.

**Act 1** can be pre-done; **Act 2** is the live engineer story on Seat 2.

## Act 1 — Admin (Seat 1, ~2 min)

1. Team Marketplace → `org-trailhead` imported, **Required**
2. Team Rules → 2–3 enforced bullets
3. One line: "Engineers get this automatically — I'll log in as a new hire."

## Act 2 — New engineer (Seat 2)

### 1. Fresh login (30 sec)

- Customize → Plugins → `org-trailhead` already installed
- No manual plugin install

### 2. Setup (2 min)

```bash
git clone https://github.com/WeLearnt/Trailhead.git
cd Trailhead
make setup
```

- `/welcome-onboard` — what happened, what's next

### 3. The problem (1 min)

- Stand-in library has docs; engineers still drift on conventions
- Three gates: Cursor → Trailhead → their CI

### 4. Scaffold (4 min)

- `/scaffold-first-contribution`
- Show fork check (step 0), branch, code + mirrored tests under `examples/pandas-standin/`

### 5. Catch a mistake (2 min)

- Introduce deprecated `legacy_normalize` call OR omit test file
- `make check` → fails with clear message
- Fix → `make check` passes

### 6. Pre-push + hook (2 min)

- `/pre-push-quality-gate`
- Optional Bugbot `/review`
- `git push` → hook runs `make check` (trusted workspace)

### 7. Hand off to their process (1 min)

- Open PR — **CI unchanged** (Ruff, coverage, pytest)
- `make test` — Trailhead strength test

### 8. Maintainability (1 min)

- `trailhead-manifest.json` pin
- `docs/MAINTAINING-TRAILHEAD.md` — platform owns without Jack

### 9. What we did NOT touch (30 sec)

- No CI workflow rebuild
- No deploy pipeline
- No Enterprise requirement

## Closing line

> Your docs stay canonical. Trailhead makes them executable. Company standards ship via Required plugin — I'll show you the manifest bump path for version control in MRs.
