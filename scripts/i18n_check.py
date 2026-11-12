#!/usr/bin/env python3
"""Validate the English translation layer.

Usage:
    python scripts/i18n_check.py            # report coverage, fail on bad files
    python scripts/i18n_check.py --strict   # also fail if any core course is untranslated

Checks:
  * every data/i18n/en/<slug>.json points at a real course
  * required fields are present and non-empty
  * topic count matches the Chinese source (no dropped or invented bullets)
  * no Chinese characters leak into English fields
  * status is draft | reviewed
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
I18N_DIR = DATA_DIR / "i18n"
EN_DIR = I18N_DIR / "en"

REQUIRED = ("one", "pos", "topics", "prereq", "assess", "who", "tips")
CJK = re.compile(r"[\u4e00-\u9fff]")
STATUSES = {"draft", "reviewed"}


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def walk_strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from walk_strings(item)
    elif isinstance(value, dict):
        for item in value.values():
            yield from walk_strings(item)


def main() -> None:
    strict = "--strict" in sys.argv
    ui = load_json(I18N_DIR / "ui.en.json")
    courses = []
    for path in sorted((DATA_DIR / "courses").glob("*.json")):
        courses.extend(load_json(path))
    by_slug = {c["slug"]: c for c in courses}

    errors = []
    warnings = []
    translated = 0

    for path in sorted(EN_DIR.glob("*.json")):
        doc = load_json(path)
        slug = doc.get("slug") or path.stem
        course = by_slug.get(slug)
        if not course:
            errors.append(f"{path.name}: slug {slug!r} is not in data/courses/*.json")
            continue

        missing = [k for k in REQUIRED if not doc.get(k)]
        if missing:
            errors.append(f"{slug}: missing {missing}")

        status = doc.get("status", "draft")
        if status not in STATUSES:
            errors.append(f"{slug}: status must be one of {sorted(STATUSES)}, got {status!r}")

        topics = doc.get("topics") or []
        if len(topics) != len(course.get("topics") or []):
            errors.append(
                f"{slug}: {len(topics)} English topics vs {len(course.get('topics') or [])} Chinese topics"
            )

        for field in REQUIRED:
            value = doc.get(field)
            if isinstance(value, str) and CJK.search(value):
                errors.append(f"{slug}.{field}: Chinese characters in English text")
            if isinstance(value, list):
                for i, item in enumerate(value):
                    if CJK.search(str(item)):
                        errors.append(f"{slug}.{field}[{i}]: Chinese characters in English text")

        for text in walk_strings(doc):
            if CJK.search(text):
                errors.append(f"{slug}: Chinese characters in English text: {text[:60]!r}")

        if not doc.get("updated"):
            warnings.append(f"{slug}: missing updated date")

        translated += 1

    cats = {c["cat"] for c in courses}
    missing_cats = sorted(cats - set(ui.get("categories", {})))
    if missing_cats:
        errors.append(f"ui.en.json: missing category translations {missing_cats}")

    more = load_json(DATA_DIR / "more_courses.json") if (DATA_DIR / "more_courses.json").exists() else []
    more_en = load_json(I18N_DIR / "more_courses.en.json") if (I18N_DIR / "more_courses.en.json").exists() else {}
    related_ok = 0
    for m in more:
        tr = more_en.get(m["id"])
        if not tr:
            errors.append(f"more_courses.en.json: missing {m['id']}")
            continue
        for key in ("tag", "one"):
            value = tr.get(key, "")
            if not value:
                errors.append(f"more_courses.en.json: {m['id']} missing {key}")
            elif CJK.search(value):
                errors.append(f"more_courses.en.json: {m['id']}.{key} has Chinese characters")
        related_ok += 1

    for name in ("paths.en.json", "pages.en.json", "prereqs.en.json"):
        path = I18N_DIR / name
        if not path.exists():
            errors.append(f"{name}: missing")
            continue
        for text in walk_strings(load_json(path)):
            if CJK.search(text):
                errors.append(f"{name}: Chinese characters in English text: {text[:60]!r}")

    total = len(courses)
    print(f"coverage: {translated}/{total} core courses, {related_ok}/{len(more)} related courses")
    if translated < total and strict:
        errors.append(f"{total - translated} core courses still have no English overview")
    if translated < total and not strict:
        print("  (use --strict in CI once the translation is complete)")

    for warning in warnings:
        print(f"  warn: {warning}")
    for error in errors:
        print(f"  error: {error}")

    if errors:
        sys.exit(1)
    print("i18n check passed")


if __name__ == "__main__":
    main()
