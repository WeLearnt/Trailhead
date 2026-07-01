#!/usr/bin/env bash
# Trailhead one-command local onboarding (Phase A–D).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

PLUGIN_NAME="org-trailhead"
PLUGIN_VERSION="1.2.0"

echo "=== Trailhead setup ==="

# Phase A — fork / remotes
if [[ "${TRAILHEAD_SKIP_FORK_CHECK:-}" != "1" ]]; then
  if ! git remote get-url upstream >/dev/null 2>&1; then
    echo "Phase A FAILED: missing 'upstream' remote (fork workflow not configured)."
    echo
    echo "Expected workflow:"
    echo "  1. Fork this repository on GitHub (engineer account)."
    echo "  2. git clone https://github.com/<you>/trailhead.git"
    echo "  3. git remote add upstream https://github.com/WeLearnt/Trailhead.git"
    echo "  4. git fetch upstream"
    echo
    echo "Re-run after remotes are configured, or set TRAILHEAD_SKIP_FORK_CHECK=1 for local-only dev."
    exit 1
  fi
  echo "Phase A: upstream remote present"
else
  echo "Phase A: skipped (TRAILHEAD_SKIP_FORK_CHECK=1)"
fi

# Phase B — toolchain
echo "Phase B: installing Python dependencies"
python3 -m pip install -q -r requirements-dev.txt

# Phase C — Trailhead self-test
echo "Phase C: running Trailhead strength test"
make test

# Phase D — Cursor team layer reminders
echo
echo "Phase D: Cursor team layer"
echo "  - Required plugin: ${PLUGIN_NAME} v${PLUGIN_VERSION}"
echo "    Verify in Cursor → Customize → Plugins (should be auto-installed on Teams)."
echo "  - Team Rules: enforced org policies apply automatically on Teams."
echo "  - Trusted workspace: enable for this repo so project hooks run on git push."
echo
echo "=== Trailhead setup complete ==="
