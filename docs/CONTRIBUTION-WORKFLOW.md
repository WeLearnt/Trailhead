# Contribution workflow — fork, branch, PR

Trailhead **encodes** your existing process; it does not replace merge queues, CODEOWNERS, or CI.

## Standard flow

1. **Fork** the org repo to your GitHub account
2. **Clone your fork**
   ```bash
   git clone https://github.com/<you>/trailhead.git
   cd trailhead
   git remote add upstream https://github.com/welearnt/trailhead.git
   git fetch upstream
   ```
3. **Sync main**
   ```bash
   git checkout main
   git pull upstream main --ff-only
   ```
4. **Feature branch** — one logical change
   ```bash
   git checkout -b enh/my-first-contribution
   ```
5. **Worktree (optional)** for parallel work
   ```bash
   git worktree add ../enh-my-first-contribution enh/my-first-contribution
   ```
6. **Develop** — use `/scaffold-first-contribution`; edit under `examples/pandas-standin/`
7. **Validate**
   ```bash
   make check
   make test-standin
   ```
8. **Push to fork** (never push to `upstream/main`)
   ```bash
   git push origin enh/my-first-contribution
   ```
   Push hook runs `make check` in trusted workspaces.
9. **Open PR** to `upstream` via GitHub UI or `gh pr create`
10. **Review + merge** — existing CODEOWNERS and CI unchanged

## If fork is missing

`make setup` **fails fast** with exact `git remote add upstream` instructions. Trailhead does not auto-fork (org policy / GitHub identity).

For local-only development without a fork:

```bash
export TRAILHEAD_SKIP_FORK_CHECK=1
make setup
```

## Cloud agents

Cloud agents use the same rules, skills, and checks. Git push from cloud requires org-approved secrets — see [CLOUD-ONBOARDING.md](CLOUD-ONBOARDING.md).

## Hook limitations

Hooks fire for agent/terminal push in Cursor. Commits via GitHub web UI bypass hooks — their CI is the backstop.
