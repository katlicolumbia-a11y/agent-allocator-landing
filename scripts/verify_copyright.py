#!/usr/bin/env python3
"""Fail CI when Katrina Li's ownership records are removed or altered."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {
    "index.html": [
        'meta name="author" content="Katrina Li"',
        'meta name="copyright" content="Copyright © 2026 Katrina Li.',
        "© 2026 Katrina Li",
    ],
    "COPYRIGHT.md": ["Copyright © 2026 Katrina Li", "All rights reserved"],
    "NOTICE": ["Katrina Li", "katlicolumbia-a11y"],
    ".github/CODEOWNERS": ["* @katlicolumbia-a11y"],
}

errors = []
for relative_path, markers in REQUIRED.items():
    path = ROOT / relative_path
    if not path.is_file():
        errors.append(f"missing required ownership file: {relative_path}")
        continue
    text = path.read_text(encoding="utf-8")
    for marker in markers:
        if marker not in text:
            errors.append(f"missing ownership marker in {relative_path}: {marker}")

if errors:
    raise SystemExit("COPYRIGHT GUARD FAILED\n" + "\n".join(f"- {e}" for e in errors))

print("Copyright and attribution records verified for Katrina Li.")
