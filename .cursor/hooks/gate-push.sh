#!/usr/bin/env bash
# Block git push when Trailhead library-specific checks fail.
set -euo pipefail

input="$(cat)"
command="$(echo "$input" | jq -r '.command // empty')"

if echo "$command" | grep -qE '(^|[;&|]\s*)git\s+push\b'; then
  repo_root="$(echo "$input" | jq -r '.workspace_roots[0] // empty')"
  if [[ -z "$repo_root" ]]; then
    repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
  fi

  if ! (cd "$repo_root" && make check >/tmp/trailhead-hook.log 2>&1); then
    log="$(tail -n 20 /tmp/trailhead-hook.log | tr '\n' ' ')"
    jq -n \
      --arg msg "git push blocked: Trailhead checks failed. Run 'make check' and fix issues." \
      --arg agent "Push blocked. Run 'make check' in the repo root. Details: $log" \
      '{continue: true, permission: "deny", user_message: $msg, agent_message: $agent}'
    exit 0
  fi
fi

jq -n '{continue: true, permission: "allow"}'
