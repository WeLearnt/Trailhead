# WeLearnt GitHub org — setup checklist

**Canonical app repo:** https://github.com/WeLearnt/Trailhead

Priya's company org: **https://github.com/WeLearnt**

## Publish app repo to WeLearnt

If `WeLearnt/Trailhead` is empty or new, push from a machine with org access:

```bash
git clone https://github.com/WeLearnt/Trailhead.git
cd Trailhead
# If empty repo, pull latest from jackbrad mirror once (then delete jackbrad copy):
git remote add mirror https://github.com/jackbrad/Trailhead.git
git fetch mirror main
git merge mirror/main --allow-unrelated-histories   # only if WeLearnt repo has README init
git remote remove mirror
git push -u origin main
```

Or if you already have this workspace locally with `origin` → `WeLearnt/Trailhead`:

```bash
git remote set-url origin https://github.com/WeLearnt/Trailhead.git
git push -u origin main
```

After push succeeds, archive or delete `jackbrad/Trailhead` (no longer canonical).

## Repos

| Repo | Purpose | Status |
|------|---------|--------|
| [`WeLearnt/Trailhead`](https://github.com/WeLearnt/Trailhead) | App repo — rules, skills, hooks, stand-in, docs | **Primary** |
| `WeLearnt/cursor-trailhead-company-plugin` | Required Team Marketplace plugin | Create next — copy `examples/cursor-trailhead-company-plugin/` |

## Clone (engineers)

Fork `WeLearnt/Trailhead` on GitHub, then:

```bash
git clone https://github.com/<you>/Trailhead.git
cd Trailhead
git remote add upstream https://github.com/WeLearnt/Trailhead.git
git fetch upstream
make setup
```

## Cursor Team Marketplace (Seat 1 / admin)

1. Dashboard → Settings → Plugins → Team Marketplaces → **Import**
2. URL: `https://github.com/WeLearnt/cursor-trailhead-company-plugin` (after plugin repo exists)
3. Mark `org-trailhead` **Required**
4. Install Cursor GitHub App on **WeLearnt** org

See [ADMIN-SETUP.md](ADMIN-SETUP.md).

## Remotes

```bash
git remote -v
# origin   → your fork (Seat 2) or WeLearnt/Trailhead (admin clone)
# upstream → https://github.com/WeLearnt/Trailhead.git
```

## Demo dry run

[PREREQUISITES.md](PREREQUISITES.md) → [DEMO-CHECKLIST.md](DEMO-CHECKLIST.md) → [DEMO-WALKTHROUGH.md](DEMO-WALKTHROUGH.md)
