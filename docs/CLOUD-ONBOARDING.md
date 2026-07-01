# Cloud onboarding — golden image path

Parallel to local `make setup`. Same Trailhead stack; faster boot on a fresh machine.

## Configuration

- [`.cursor/environment.json`](../.cursor/environment.json) — Dockerfile + install command
- [`.cursor/Dockerfile`](../.cursor/Dockerfile) — Python 3 + git + sudo

`install` runs:

```bash
pip install -r requirements-dev.txt && TRAILHEAD_SKIP_FORK_CHECK=1 make test
```

Fork check is skipped in cloud bootstrap; engineer still needs fork for real PR flow.

## Starting a cloud agent

1. Open repo in Cursor (Teams)
2. Start cloud agent on branch with committed `environment.json`
3. Do **not** rely on dashboard snapshot wizard if you want Dockerfile mode — commit config and start a normal cloud agent
4. Optional: `/welcome-onboard` after boot

## Git push from cloud

Requires Cursor Secrets for git credentials and org approval. If not configured, demo **local push** from Seat 2 instead.

## Snapshot expiry

If a saved dashboard snapshot overrides Dockerfile, delete old environments: Dashboard → Cloud Agents → Environments → Delete. Next agent rebuilds from repo Dockerfile.

## Demo talking point

> Cloud and local hit the same three gates — rules while coding, `make check` before push, your CI on the PR.
