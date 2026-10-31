#!/usr/bin/env python3
"""Build the course Markdown pages, README tables, and combined JSON.

Usage:
    python scripts/build.py

Reads:
    data/catalog.json          # normalized ExploreCourses data
    data/courses/*.json        # hand-written course notes
    data/more_courses.json     # additional related courses (table only)

Writes:
    courses/<slug>.md
    data/courses.json
    README.md                  # replaces the marked table blocks
"""

from __future__ import annotations

import json
import re
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COURSES_DIR = ROOT / "courses"
DATA_DIR = ROOT / "data"
README = ROOT / "README.md"

CATEGORY_ORDER = [
    "基础核心",
    "LLM 与 Agent",
    "ML 系统与硬件",
    "视觉、图形与生成",
    "机器人、具身智能",
    "AI for Science 与医疗",
    "产品、伦理与设计",
    "统计与优化",
]

TERM_CN = {
    "2026-2027 Autumn": "2026 秋",
    "2026-2027 Winter": "2027 冬",
    "2026-2027 Spring": "2027 春",
    "2026-2027 Summer": "2027 夏",
}

TERM_ORDER = {
    "2026-2027 Autumn": 0,
    "2026-2027 Winter": 1,
    "2026-2027 Spring": 2,
    "2026-2027 Summer": 3,
}


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def cross_listed(title: str, own_id: str) -> str:
    m = re.search(r"\(([^()]*)\)\s*$", title)
    if not m:
        return ""
    parts = [p.strip() for p in m.group(1).split(",")]
    parts = [p for p in parts if p and p != own_id]
    return "、".join(parts)


def terms_cn(terms: list[str]) -> str:
    if not terms:
        return "2026–27 未排课"
    ordered = sorted(terms, key=lambda t: TERM_ORDER.get(t, 99))
    return " / ".join(TERM_CN.get(t, t) for t in ordered)


def units(course: dict) -> str:
    lo, hi = course.get("units_min", ""), course.get("units_max", "")
    if not lo:
        return "—"
    return lo if lo == hi else f"{lo}–{hi}"


def stars(level: int) -> str:
    level = max(1, min(5, int(level)))
    return "★" * level + "☆" * (5 - level)


def instructor_line(course: dict) -> str:
    names = course.get("instructors_pi") or course.get("instructors") or []
    if not names:
        return "TBA"
    shown = names[:4]
    suffix = " 等" if len(names) > 4 else ""
    return "、".join(shown) + suffix


def explorecourses_url(course_id: str) -> str:
    q = urllib.parse.quote_plus(course_id)
    return (
        "https://explorecourses.stanford.edu/search?view=catalog"
        f"&academicYear=20262027&q={q}"
    )


def render_doc(course: dict, catalog: dict, slug_to_title: dict) -> str:
    cid = course["id"]
    cat = catalog[cid]
    cross = cross_listed(cat["title"], cid)
    cross_line = f"<br>同时列于：{cross}" if cross else ""

    topics = "\n".join(f"- {t}" for t in course["topics"])

    related_lines = []
    for rid in course.get("related", []):
        if rid in slug_to_title:
            slug, title = slug_to_title[rid]
            related_lines.append(f"- [{rid} · {title}]({slug}.md)")
        else:
            related_lines.append(f"- {rid}")
    related = "\n".join(related_lines) or "—"

    links = [f"- [ExploreCourses]({explorecourses_url(cid)})"]
    for label, url in course.get("links", []):
        links.append(f"- [{label}]({url})")
    links_md = "\n".join(links)

    note = course.get("note", "").strip()
    note_md = f"\n> **备注**：{note}\n" if note else ""

    return f"""# {cid} · {course['zh']}

> {course['one']}

| 项目 | 内容 |
| --- | --- |
| **课程编号** | {cid}{cross_line} |
| **英文名称** | {cat['title']} |
| **学期** | {terms_cn(cat['terms'])} |
| **学分** | {units(cat)} |
| **评分** | {cat['grading'] or '—'} |
| **授课** | {instructor_line(cat)} |
| **先修** | {course['prereq']} |
| **难度** | {stars(course['difficulty'])}（主观） |
| **标签** | {' · '.join('`' + t + '`' for t in course['tags'])} |
{note_md}
## 课程定位

{course['pos']}

## 主要内容

{topics}

## 考核与工作量

{course['assess']}

## 适合谁

{course['who']}

## 学习建议

{course['tips']}

## 相关课程

{related}

## 资源

{links_md}

<details>
<summary>官方课程描述（英文原文）</summary>

> {cat['description']}

</details>

---

<sub>信息整理自 Stanford ExploreCourses（2026–27）与课程官网，最后更新 2026-10-30。课程安排、考核比例以官方为准。</sub>
"""


def table_for(courses: list[dict], catalog: dict) -> str:
    lines = [
        "| 课程 | 名称 | 学分 | 学期 | 难度 | 速览 |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for c in courses:
        cat = catalog[c["id"]]
        lines.append(
            f"| **{c['id']}** | {c['zh']} | {units(cat)} | {terms_cn(cat['terms'])} "
            f"| {stars(c['difficulty'])} | [打开](courses/{c['slug']}.md) |"
        )
    return "\n".join(lines)


def more_table(more: list[dict], catalog: dict) -> str:
    lines = [
        "| 课程 | 名称 | 学分 | 学期 | 方向/备注 |",
        "| --- | --- | --- | --- | --- |",
    ]
    for m in more:
        cid = m["id"]
        if cid not in catalog:
            continue
        cat = catalog[cid]
        lines.append(
            f"| **{cid}** | {cat['title']} | {units(cat)} | {terms_cn(cat['terms'])} "
            f"| {m.get('tag', '')} |"
        )
    return "\n".join(lines)


def replace_block(text: str, marker: str, content: str) -> str:
    begin = f"<!-- BEGIN:{marker} -->"
    end = f"<!-- END:{marker} -->"
    pattern = re.compile(re.escape(begin) + r".*?" + re.escape(end), re.S)
    replacement = f"{begin}\n\n{content}\n\n{end}"
    if not pattern.search(text):
        raise SystemExit(f"marker not found in README: {marker}")
    return pattern.sub(replacement, text)


def main() -> None:
    catalog_list = load_json(DATA_DIR / "catalog.json")
    catalog = {c["id"]: c for c in catalog_list}

    courses: list[dict] = []
    for path in sorted((DATA_DIR / "courses").glob("*.json")):
        courses.extend(load_json(path))

    ids = [c["id"] for c in courses]
    dupes = {i for i in ids if ids.count(i) > 1}
    if dupes:
        raise SystemExit(f"duplicate course ids: {sorted(dupes)}")
    missing = [i for i in ids if i not in catalog]
    if missing:
        raise SystemExit(f"course ids not found in catalog: {missing}")

    order = {c: i for i, c in enumerate(CATEGORY_ORDER)}
    courses.sort(key=lambda c: (order.get(c["cat"], 99), c["id"]))

    slug_to_title = {c["id"]: (c["slug"], c["zh"]) for c in courses}

    COURSES_DIR.mkdir(exist_ok=True)
    for c in courses:
        (COURSES_DIR / f"{c['slug']}.md").write_text(
            render_doc(c, catalog, slug_to_title), encoding="utf-8", newline="\n"
        )

    combined = []
    for c in courses:
        cat = catalog[c["id"]]
        combined.append({
            **{k: c[k] for k in ("id", "slug", "zh", "cat", "difficulty", "one", "tags")},
            "title": cat["title"],
            "description": cat["description"],
            "units": units(cat),
            "grading": cat["grading"],
            "terms": terms_cn(cat["terms"]),
            "instructors": instructor_line(cat),
            "prereq": c["prereq"],
            "pos": c["pos"],
            "topics": c["topics"],
            "assessment": c["assess"],
            "who": c["who"],
            "tips": c["tips"],
            "related": c.get("related", []),
            "links": c.get("links", []),
            "note": c.get("note", ""),
            "doc": f"courses/{c['slug']}.md",
        })
    (DATA_DIR / "courses.json").write_text(
        json.dumps(combined, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n"
    )

    more = load_json(DATA_DIR / "more_courses.json") if (DATA_DIR / "more_courses.json").exists() else []

    readme = README.read_text(encoding="utf-8")
    sections = []
    for cat_name in CATEGORY_ORDER:
        group = [c for c in courses if c["cat"] == cat_name]
        if not group:
            continue
        sections.append(f"### {cat_name}\n\n{table_for(group, catalog)}")
    readme = replace_block(readme, "COURSE_TABLE", "\n\n".join(sections))
    readme = replace_block(readme, "MORE_TABLE", more_table(more, catalog))
    README.write_text(readme, encoding="utf-8", newline="\n")

    print(f"built {len(courses)} course docs")
    print(f"wrote {DATA_DIR / 'courses.json'}")
    print(f"updated {README}")


if __name__ == "__main__":
    main()
