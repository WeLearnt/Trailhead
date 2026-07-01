#!/usr/bin/env python3
"""Trailhead local quality gate — library-specific checks only.

Assumes generic anti-patterns (wildcard imports, style) are enforced by the
customer's existing CI (e.g. Ruff). This script checks:
  1. Deprecated API usage (scripts/deprecated-apis.json)
  2. Mirrored test files for modules with public functions
  3. pytest --collect-only smoke on the stand-in test suite
"""

from __future__ import annotations

import argparse
import ast
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STANDIN = ROOT / "examples" / "pandas-standin"
MANIFEST = ROOT / "trailhead-manifest.json"
DEPRECATED = ROOT / "scripts" / "deprecated-apis.json"


def load_json(path: Path) -> dict:
  with path.open(encoding="utf-8") as handle:
    return json.load(handle)


def display_path(path: Path) -> str:
  try:
    return str(path.relative_to(ROOT))
  except ValueError:
    return str(path)


def check_deprecated(target: Path, api_names: list[str]) -> list[str]:
  errors: list[str] = []
  for path in sorted(target.rglob("*.py")):
    if "tests" in path.parts:
      continue
    tree = ast.parse(path.read_text(encoding="utf-8"))
    defined = {
      node.name
      for node in tree.body
      if isinstance(node, ast.FunctionDef)
    }
    for node in ast.walk(tree):
      if not isinstance(node, ast.Call):
        continue
      func = node.func
      if isinstance(func, ast.Name) and func.id in api_names and func.id not in defined:
        errors.append(
          f"{display_path(path)}:{node.lineno}: calls deprecated API '{func.id}'"
        )
  return errors


def mirrored_test_path(source: Path) -> Path | None:
  try:
    rel = source.relative_to(STANDIN / "pandas")
  except ValueError:
    return None
  if not rel.parts or rel.parts[0] != "core":
    return None
  test_parts = ("tests", "core", *rel.parts[1:-1], f"test_{rel.stem}.py")
  return STANDIN / "pandas" / Path(*test_parts)


def public_functions(path: Path) -> list[str]:
  tree = ast.parse(path.read_text(encoding="utf-8"))
  return [
    node.name
    for node in tree.body
    if isinstance(node, ast.FunctionDef) and not node.name.startswith("_")
  ]


def check_test_mirrors(target: Path) -> list[str]:
  errors: list[str] = []
  for source in sorted((target / "pandas" / "core").rglob("*.py")):
    if source.name == "__init__.py":
      continue
    if not public_functions(source):
      continue
    test_path = mirrored_test_path(source)
    if test_path is None or not test_path.is_file():
      rel = display_path(source)
      expected = display_path(test_path) if test_path else "unknown"
      errors.append(f"{rel}: missing mirrored test file (expected {expected})")
  return errors


def check_pytest_collect(target: Path) -> list[str]:
  tests_dir = target / "pandas" / "tests"
  if not tests_dir.is_dir():
    return []
  result = subprocess.run(
    [sys.executable, "-m", "pytest", "pandas/tests/", "--collect-only", "-q"],
    cwd=target,
    capture_output=True,
    text=True,
  )
  if result.returncode != 0:
    detail = (result.stdout + result.stderr).strip() or "pytest collect failed"
    return [f"pytest --collect-only failed: {detail}"]
  return []


def parse_version(version: str) -> tuple[int, ...]:
  match = re.match(r"^(\d+(?:\.\d+)*)", version)
  if not match:
    raise ValueError(f"invalid version: {version}")
  return tuple(int(part) for part in match.group(1).split("."))


def check_manifest() -> list[str]:
  if not MANIFEST.is_file():
    return ["trailhead-manifest.json: missing"]
  data = load_json(MANIFEST)
  plugin = data.get("company_plugin", {})
  version = plugin.get("version")
  minimum = plugin.get("minimum_version")
  if not version:
    return ["trailhead-manifest.json: company_plugin.version is required"]
  if minimum and parse_version(version) < parse_version(minimum):
    return [
      f"trailhead-manifest.json: company_plugin.version {version} "
      f"is below minimum_version {minimum}"
    ]
  return []


def main() -> int:
  parser = argparse.ArgumentParser(description="Trailhead library-specific checks")
  parser.add_argument(
    "target",
    nargs="?",
    default=str(STANDIN),
    help="Path to library tree (default: examples/pandas-standin)",
  )
  parser.add_argument(
    "--verify-manifest",
    action="store_true",
    help="Validate trailhead-manifest.json company_plugin pin",
  )
  args = parser.parse_args()
  target = Path(args.target).resolve()

  errors: list[str] = []
  if args.verify_manifest:
    errors.extend(check_manifest())

  deprecated = load_json(DEPRECATED)
  api_names = [entry["name"] for entry in deprecated.get("deprecated_apis", [])]
  errors.extend(check_deprecated(target, api_names))
  errors.extend(check_test_mirrors(target))
  errors.extend(check_pytest_collect(target))

  if errors:
    print("trailhead-check: FAILED", file=sys.stderr)
    for error in errors:
      print(f"  - {error}", file=sys.stderr)
    return 1

  print("trailhead-check: OK")
  return 0


if __name__ == "__main__":
  sys.exit(main())
