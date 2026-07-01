# WeLearnt GitHub org — setup checklist

Priya's company org is live: **https://github.com/WeLearnt**

Use this after the org exists and before the two-seat Teams demo.

## 1. Create org repos

| Repo | Purpose | Source |
|------|---------|--------|
| `WeLearnt/Trailhead` | App repo (this toolkit + pandas stand-in) | Transfer from `jackbrad/Trailhead` or push `main` + PR branch |
| `WeLearnt/cursor-trailhead-company-plugin` | Required Team Marketplace plugin | Copy `examples/cursor-trailhead-company-plugin/` from Trailhead |

**Plugin repo layout:** root contains `.cursor-plugin/`, `rules/`, `skills/` — see `examples/cursor-trailhead-company-plugin/README.md`.

## 2. Transfer or publish Trailhead app repo

Option A — **Transfer** (keeps PR history):

1. GitHub → `jackbrad/Trailhead` → Settings → Transfer ownership → `WeLearnt`
2. Update local remote: `git remote set-url origin https://github.com/WeLearnt/Trailhead.git`

Option B — **New repo** under org:

```bash
gh repo create WeLearnt/Trailhead --public --source=. --remote=welearnt --push
```

## 3. Engineer fork (Seat 2 demo account)

On the **engineer** GitHub account (not admin):

```bash
# Fork WeLearnt/Trailhead in GitHub UI, then:
git clone https://github.com/<engineer-user>/Trailhead.git
cd Trailhead
git remote add upstream https://github.com/WeLearnt/Trailhead.git
git fetch upstream
make setup
```

## 4. Cursor Team Marketplace

1. Dashboard → Settings → Plugins → Team Marketplaces → **Import**
2. URL: `https://github.com/WeLearnt/cursor-trailhead-company-plugin`
3. Mark `org-trailhead` **Required**
4. Install Cursor GitHub App on **WeLearnt** org (for auto-refresh on plugin push)

See [ADMIN-SETUP.md](ADMIN-SETUP.md).

## 5. Verify remotes

```bash
git remote -v
# origin  → engineer fork (Seat 2) OR WeLearnt/Trailhead (admin)
# upstream → https://github.com/WeLearnt/Trailhead.git
```

## 6. Demo dry run

[PREREQUISITES.md](PREREQUISITES.md) → [DEMO-CHECKLIST.md](DEMO-CHECKLIST.md) → [DEMO-WALKTHROUGH.md](DEMO-WALKTHROUGH.md)
