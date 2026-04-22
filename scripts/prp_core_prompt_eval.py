"""Deterministic prompt-contract evaluator for prp-core.

Checks shipped skills, agents, and hooks for required contract strings,
and verifies that shipped plugin files match their .claude/ mirror copies.

Usage:
    uv run python scripts/prp_core_prompt_eval.py --list
    uv run python scripts/prp_core_prompt_eval.py --case plan
    uv run python scripts/prp_core_prompt_eval.py --case implement
    uv run python scripts/prp_core_prompt_eval.py --case review
    uv run python scripts/prp_core_prompt_eval.py --case issue-fix
    uv run python scripts/prp_core_prompt_eval.py --case mirror-parity
    uv run python scripts/prp_core_prompt_eval.py --case research-team-hook-schema
    uv run python scripts/prp_core_prompt_eval.py --all

Exit code 0 means all checks pass. Exit code 1 means one or more checks failed.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

CASES_PATH = Path("tests/prp-core/prompt-cases.json")
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"
BOLD = "\033[1m"


def load_cases(path: Path) -> list[dict]:
    if not path.exists():
        print(f"{RED}ERROR: cases file not found: {path}{RESET}", file=sys.stderr)
        sys.exit(1)
    return json.loads(path.read_text())


def evaluate_must_contain(case: dict) -> list[str]:
    """Check that each target file contains all required strings."""
    failures: list[str] = []
    targets = case.get("targets", [])
    needles = case.get("must_contain", [])
    for target in targets:
        p = Path(target)
        if not p.exists():
            failures.append(f"  {RED}MISSING FILE{RESET}: {target}")
            continue
        text = p.read_text()
        for needle in needles:
            if needle not in text:
                failures.append(
                    f"  {RED}MISSING CONTRACT{RESET}: '{needle}' not found in {target}"
                )
    return failures


def evaluate_mirror_parity(case: dict) -> list[str]:
    """Check that each (shipped, mirror) pair is identical."""
    failures: list[str] = []
    for pair in case.get("mirror_pairs", []):
        left_path, right_path = Path(pair[0]), Path(pair[1])
        if not left_path.exists():
            failures.append(f"  {RED}MISSING{RESET}: shipped file not found: {left_path}")
            continue
        if not right_path.exists():
            failures.append(f"  {RED}MISSING{RESET}: mirror file not found: {right_path}")
            continue
        if left_path.read_text() != right_path.read_text():
            failures.append(f"  {RED}DRIFT{RESET}: {left_path} != {right_path}")
    return failures


def run_case(case: dict) -> tuple[int, int]:
    """Run one case. Returns (pass_count, fail_count)."""
    case_id = case["id"]
    description = case.get("description", "")
    print(f"\n{BOLD}Case: {case_id}{RESET}  {description}")

    if case_id == "mirror-parity":
        failures = evaluate_mirror_parity(case)
    else:
        failures = evaluate_must_contain(case)

    if failures:
        for f in failures:
            print(f)
        print(f"  {RED}FAIL{RESET} [{case_id}]: {len(failures)} check(s) failed")
        return 0, len(failures)
    else:
        print(f"  {GREEN}PASS{RESET} [{case_id}]")
        return 1, 0


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Deterministic prompt-contract evaluator for prp-core."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--list", action="store_true", help="List available case IDs")
    group.add_argument("--case", metavar="ID", help="Run a specific case by ID")
    group.add_argument("--all", action="store_true", help="Run all cases")
    args = parser.parse_args()

    cases = load_cases(CASES_PATH)

    if args.list:
        print(f"{BOLD}Available prompt-eval cases:{RESET}")
        for case in cases:
            print(f"  {case['id']:30s}  {case.get('description', '')}")
        print(f"\nRun with: uv run python scripts/prp_core_prompt_eval.py --case <id>")
        print(f"Docs:      docs/prp-core-prompt-evals.md")
        return

    if args.all:
        total_pass = total_fail = 0
        for case in cases:
            p, f = run_case(case)
            total_pass += p
            total_fail += f
        print(f"\n{BOLD}Results:{RESET} {total_pass} passed, {total_fail} failed")
        if total_fail > 0:
            sys.exit(1)
        return

    case_map = {c["id"]: c for c in cases}
    if args.case not in case_map:
        available = ", ".join(case_map)
        print(f"{RED}ERROR{RESET}: unknown case '{args.case}'. Available: {available}", file=sys.stderr)
        sys.exit(1)

    p, f = run_case(case_map[args.case])
    if f > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
