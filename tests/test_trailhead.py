"""Strength tests for scripts/trailhead-check.py."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
CHECK = ROOT / "scripts" / "trailhead-check.py"
STANDIN = ROOT / "examples" / "pandas-standin"


def run_check(*args: str) -> subprocess.CompletedProcess[str]:
  return subprocess.run(
    [sys.executable, str(CHECK), *args],
    cwd=ROOT,
    capture_output=True,
    text=True,
  )


def test_check_passes_on_clean_standin():
  result = run_check(str(STANDIN))
  assert result.returncode == 0, result.stderr
  assert "OK" in result.stdout


def test_check_fails_on_deprecated_api(tmp_path: Path):
  core = tmp_path / "pandas" / "core" / "ops"
  core.mkdir(parents=True)
  (core / "bad.py").write_text(
    "import numpy as np\n\n"
    "def use_old(values):\n"
    "    return legacy_normalize(values)\n",
    encoding="utf-8",
  )
  result = run_check(str(tmp_path))
  assert result.returncode == 1
  assert "legacy_normalize" in result.stderr


def test_check_fails_on_missing_test_mirror(tmp_path: Path):
  core = tmp_path / "pandas" / "core" / "ops"
  core.mkdir(parents=True)
  (core / "widget.py").write_text(
    "def widget():\n    return 1\n",
    encoding="utf-8",
  )
  result = run_check(str(tmp_path))
  assert result.returncode == 1
  assert "missing mirrored test" in result.stderr


def test_verify_manifest_below_minimum():
  manifest = ROOT / "trailhead-manifest.json"
  original = manifest.read_text(encoding="utf-8")
  try:
    manifest.write_text(
      json.dumps({"company_plugin": {"version": "0.1.0", "minimum_version": "1.0.0"}}),
      encoding="utf-8",
    )
    result = run_check("--verify-manifest", str(STANDIN))
    assert result.returncode == 1
    assert "below minimum_version" in result.stderr
  finally:
    manifest.write_text(original, encoding="utf-8")
