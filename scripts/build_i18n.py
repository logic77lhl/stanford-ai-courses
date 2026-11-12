#!/usr/bin/env python3
"""Build the English layer for the course map.

The Chinese notes in ``data/courses/*.json`` stay untouched. Translations live
in ``data/i18n/en/<slug>.json``; this script merges them with the official
English facts from ``data/catalog.json`` and writes:

    courses/en/<slug>.md       English Markdown overview
    data/courses.en.json       English data for the site builder

Usage:
    python scripts/build_i18n.py

Add a course by dropping ``data/i18n/en/<slug>.json`` next to the others.
Missing translations are skipped, not machine-translated at build time.
"""

from __future__ import annotations

import json
import re
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COURSES_DIR = ROOT / "courses" / "en"
DATA_DIR = ROOT / "data"
I18N_DIR = DATA_DIR / "i18n"
EN_DIR = I18N_DIR / "en"

REQUIRED = ("one", "pos", "topics", "prereq", "assess", "who", "tips")

TERM_ORDER = {
    "2026-2027 Autumn": 0,
    "2026-2027 Winter": 1,
    "2026-2027 Spring": 2,
    "2026-2027 Summer": 3,
}

LINK_LABELS = {
    "课程官网": "Course site",
    "课程主页": "Course page",
    "官方页面": "Official page",
    "课程视频": "Course videos",
    "视频": "Videos",
    "代码": "Code",
    "讲义": "Slides",
}


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def cross_listed(title: str, own_id: str) -> str:
    m = re.search(r"\(([^()]*)\)\s*$", title)
    if not m:
        return ""
    parts = [p.strip() for p in m.group(1).split(",")]
    parts = [p for p in parts if p and p != own_id]
    return ", ".join(parts)


def units(course: dict) -> str:
    lo, hi = course.get("units_min", ""), course.get("units_max", "")
    if not lo:
        return "—"
    return lo if lo == hi else f"{lo}–{hi}"


def stars(level: int | None) -> str:
    level = max(1, min(5, int(level or 0)))
    return "★" * level + "☆" * (5 - level)


def instructor_line(course: dict) -> str:
    names = course.get("instructors_pi") or course.get("instructors") or []
    if not names:
        return "TBA"
    shown = names[:4]
    suffix = ", et al." if len(names) > 4 else ""
    return "; ".join(shown) + suffix


def terms_en(terms: list[str], ui: dict) -> str:
    ordered = sorted(terms or [], key=lambda t: TERM_ORDER.get(t, 99))
    return ", ".join(ui["terms"].get(t, t) for t in ordered) or ui["terms"]["none"]


def explorecourses_url(course_id: str) -> str:
    q = urllib.parse.quote_plus(course_id)
    return (
        "https://explorecourses.stanford.edu/search?view=catalog"
        f"&academicYear=20262027&q={q}"
    )


def slugify(value: str) -> str:
    value = value.lower().replace("&", "")
    return re.sub(r"[^a-z0-9]+", "-", value).strip("-")


def render_doc_en(course: dict, cat: dict, en: dict, slug_to_title: dict, ui: dict) -> str:
    cid = course["id"]
    cross = cross_listed(cat["title"], cid)
    cross_line = f"<br>Cross-listed: {cross}" if cross else ""
    terms = terms_en(cat.get("terms") or [], ui)

    topics = "\n".join(f"- {t}" for t in en["topics"])

    related_lines = []
    for rid in course.get("related", []):
        if rid in slug_to_title:
            slug, title, has_en = slug_to_title[rid]
            if has_en:
                related_lines.append(f"- [{rid} · {title}]({slug}.md)")
            else:
                related_lines.append(f"- {rid} · {title}")
        else:
            related_lines.append(f"- {rid}")
    related = "\n".join(related_lines) or "—"

    links = [f"- [ExploreCourses]({explorecourses_url(cid)})"]
    for label, url in course.get("links", []):
        links.append(f"- [{LINK_LABELS.get(label, 'Link')}]({url})")
    links_md = "\n".join(links)

    tags = en.get("tags") or course.get("tags", [])
    updated = en.get("updated", "2026-11-12")
    note_md = f"\n> **Note**: {en['note']}\n" if en.get("note") else ""

    return f"""# {cid} · {cat['title']}

> {en['one']}

| {ui['table']['item']} | {ui['table']['detail']} |
| --- | --- |
| **{ui['table']['course']}** | {cid}{cross_line} |
| **{ui['table']['units']}** | {units(cat)} |
| **{ui['table']['terms']}** | {terms} |
| **{ui['table']['grading']}** | {cat['grading'] or '—'} |
| **{ui['table']['instructors']}** | {instructor_line(cat)} |
| **{ui['table']['prereq']}** | {en['prereq']} |
| **{ui['table']['difficulty']}** | {stars(course['difficulty'])} (subjective) |
| **{ui['table']['tags']}** | {' · '.join('`' + t + '`' for t in tags)} |
{note_md}
## {ui['sections']['positioning']}

{en['pos']}

## {ui['sections']['topics']}

{topics}

## {ui['sections']['assessment']}

{en['assess']}

## {ui['sections']['who']}

{en['who']}

## {ui['sections']['tips']}

{en['tips']}

## {ui['sections']['related']}

{related}

## {ui['sections']['resources']}

{links_md}

<details>
<summary>{ui['sections']['official']}</summary>

> {cat['description']}

</details>

---

<sub>Compiled from Stanford ExploreCourses (2026–27) and course sites. Last updated {updated}. Course offerings and grading are subject to the official syllabus.</sub>
"""


def main() -> None:
    ui = load_json(I18N_DIR / "ui.en.json")
    catalog = {c["id"]: c for c in load_json(DATA_DIR / "catalog.json")}

    courses: list[dict] = []
    for path in sorted((DATA_DIR / "courses").glob("*.json")):
        courses.extend(load_json(path))

    en_by_slug = {}
    for path in sorted(EN_DIR.glob("*.json")):
        doc = load_json(path)
        slug = doc.get("slug") or path.stem
        en_by_slug[slug] = doc

    # English titles are official; related links can point at any translated course.
    slug_to_title = {}
    for c in courses:
        slug_to_title[c["id"]] = (c["slug"], catalog[c["id"]]["title"], c["slug"] in en_by_slug)

    COURSES_DIR.mkdir(parents=True, exist_ok=True)
    exported = []
    for c in courses:
        en = en_by_slug.get(c["slug"])
        if not en:
            continue
        missing = [k for k in REQUIRED if not en.get(k)]
        if missing:
            raise SystemExit(f"{c['slug']}: missing English fields {missing}")

        cat = catalog[c["id"]]
        (COURSES_DIR / f"{c['slug']}.md").write_text(
            render_doc_en(c, cat, en, slug_to_title, ui), encoding="utf-8", newline="\n"
        )
        exported.append({
            "id": c["id"],
            "slug": c["slug"],
            "zh": c["zh"],
            "title": cat["title"],
            "cat": c["cat"],
            "cat_en": ui["categories"].get(c["cat"], c["cat"]),
            "type": "core",
            "difficulty": c["difficulty"],
            "one": en["one"],
            "pos": en["pos"],
            "topics": en["topics"],
            "prereq": en["prereq"],
            "assessment": en["assess"],
            "who": en["who"],
            "tips": en["tips"],
            "tags": en.get("tags") or c.get("tags", []),
            "description": cat["description"],
            "units": units(cat),
            "terms": terms_en(cat.get("terms") or [], ui),
            "grading": cat["grading"],
            "instructors": instructor_line(cat),
            "related": c.get("related", []),
            "links": c.get("links", []),
            "doc": f"courses/en/{c['slug']}.md",
            "status": en.get("status", "draft"),
            "updated": en.get("updated", ""),
            "note": en.get("note", ""),
        })

    more = load_json(DATA_DIR / "more_courses.json") if (DATA_DIR / "more_courses.json").exists() else []
    more_en = load_json(I18N_DIR / "more_courses.en.json") if (I18N_DIR / "more_courses.en.json").exists() else {}
    for m in more:
        cid = m["id"]
        if cid not in catalog:
            continue
        tr = more_en.get(cid)
        if not tr:
            continue
        cat = catalog[cid]
        cat_zh = m.get("cat", "基础核心")
        exported.append({
            "id": cid,
            "slug": slugify(f"{cid} {cat['title']}"),
            "zh": m.get("tag", cat["title"]),
            "title": cat["title"],
            "cat": cat_zh,
            "cat_en": ui["categories"].get(cat_zh, cat_zh),
            "type": "ext",
            "difficulty": None,
            "one": tr["one"],
            "pos": f"{tr['one']} This page keeps the official record and entry points; check the current syllabus for details.",
            "topics": [],
            "prereq": "See the official description (related courses do not have a separate prerequisite write-up).",
            "assessment": "Check the current syllabus.",
            "who": f"Anyone interested in {tr['tag']}.",
            "tips": "Read the official description and course site before deciding.",
            "tags": [tr["tag"]],
            "description": cat.get("description", ""),
            "units": units(cat),
            "terms": terms_en(cat.get("terms") or [], ui),
            "grading": cat.get("grading", ""),
            "instructors": instructor_line(cat),
            "related": [],
            "links": [],
            "doc": "",
            "status": "draft",
            "updated": "2026-11-12",
            "note": "",
        })

    (DATA_DIR / "courses.en.json").write_text(
        json.dumps(exported, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n"
    )
    core_n = sum(1 for c in exported if c["type"] == "core")
    print(f"English overviews: {core_n}/{len(courses)} core + {len(exported) - core_n} related courses")
    for c in exported:
        print(f"  {c['id']:8} {c['slug']}  [{c['status']}]")


if __name__ == "__main__":
    main()
