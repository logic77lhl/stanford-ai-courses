#!/usr/bin/env python3
"""Build the full English site under docs/en/.

Reads:
    data/courses.en.json       # 55 core + 70 related, built by build_i18n.py
    data/i18n/ui.en.json       # nav, sections, categories, table labels
    data/i18n/pages.en.json    # page copy for paths / semester / prereqs / bilibili
    data/i18n/paths.en.json    # six learning paths
    data/i18n/prereqs.en.json  # prerequisite graph
    data/lectures/*.json       # lecture outlines + Bilibili links
    data/resources.json        # videos / code / tech

Writes:
    docs/en/index.html
    docs/en/paths.html
    docs/en/semester.html
    docs/en/prereqs.html
    docs/en/bilibili.html
    docs/en/404.html
    docs/en/courses/<slug>.html   (125 pages)
"""

from __future__ import annotations

import html
import json
import re
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
SITE = ROOT / "docs"
OUT = SITE / "en"
COURSES_OUT = OUT / "courses"

LINK_LABELS = {
    "课程官网": "Course site",
    "课程主页": "Course page",
    "官方页面": "Official page",
    "课程视频": "Course videos",
    "视频": "Videos",
    "代码": "Code",
    "讲义": "Slides",
}

FAVICON = (
    "data:image/svg+xml,"
    "%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E"
    "%3Crect width='64' height='64' rx='14' fill='%2309090b'/%3E"
    "%3Ccircle cx='32' cy='32' r='15' fill='none' stroke='%23d4b176' stroke-width='4'/%3E"
    "%3Ccircle cx='32' cy='32' r='4' fill='%23d4b176'/%3E%3C/svg%3E"
)


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def esc(value: object) -> str:
    return html.escape(str(value if value is not None else ""))


def md(value: str) -> str:
    text = esc(value)
    text = text.replace("**", "\x00")
    parts = text.split("\x00")
    out = []
    for i, part in enumerate(parts):
        out.append(f"<strong>{part}</strong>" if i % 2 else part)
    return "".join(out).replace("`", "")


def stars(level) -> str:
    if not level:
        return "—"
    level = max(1, min(5, int(level)))
    return "★" * level + "☆" * (5 - level)


def link_label(label: str) -> str:
    if re.search(r"[\u4e00-\u9fff]", label or ""):
        return "Bilibili mirror"
    return label


def bili_report_url(cid: str, links: list) -> str:
    title = urllib.parse.quote(f"[Bilibili] dead link: {cid}")
    body = urllib.parse.quote("\n".join(f"- {label}: {url}" for label, url in links))
    return (
        "https://github.com/logic77lhl/stanford-ai-courses/issues/new"
        f"?title={title}&body={body}"
    )


def load_lectures() -> dict:
    merged = {}
    folder = DATA / "lectures"
    if folder.exists():
        for path in sorted(folder.glob("*.json")):
            merged.update(load_json(path))
    legacy = DATA / "lectures.json"
    if legacy.exists():
        merged.update(load_json(legacy))
    return merged


def shell(
    title: str,
    desc: str,
    body: str,
    base: str = "",
    active: str = "",
    zh_link: str = "",
    alt_zh: str = "",
    alt_en: str = "",
    extra_scripts: str = "",
) -> str:
    nav = [
        ("map", "Map", f"{base}index.html#map"),
        ("courses", "Courses", f"{base}index.html#courses"),
        ("paths", "Paths", f"{base}paths.html"),
        ("semester", "Semester", f"{base}semester.html"),
        ("prereqs", "Prereqs", f"{base}prereqs.html"),
        ("bilibili", "Bilibili", f"{base}bilibili.html"),
        ("about", "About", f"{base}index.html#about"),
    ]
    nav_html = ""
    for key, label, href in nav:
        cls = ' class="on"' if key == active else ""
        nav_html += f'<a href="{href}"{cls}>{label}</a>'
    zh_link = zh_link or f"{base}../index.html"
    asset_base = f"{base}../"
    alt_en = alt_en or "https://logic77lhl.github.io/stanford-ai-courses/en/"
    alt_zh = alt_zh or "https://logic77lhl.github.io/stanford-ai-courses/"
    html_text = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="theme-color" content="#09090b">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:type" content="website">
<link rel="alternate" hreflang="en" href="{esc(alt_en)}">
<link rel="alternate" hreflang="zh-CN" href="{esc(alt_zh)}">
<link rel="alternate" hreflang="x-default" href="{esc(alt_zh)}">
<link rel="icon" href="{FAVICON}">
<link rel="stylesheet" href="{asset_base}assets/style.css">
</head>
<body>
<header class="top">
  <div class="wrap topin">
    <a class="brand" href="{base}index.html">Stanford AI <span>Course Map</span></a>
    <nav class="nav" id="nav">{nav_html}</nav>
    <a class="lang" href="{esc(zh_link)}">中文</a>
    <a class="gh" href="https://github.com/logic77lhl/stanford-ai-courses" target="_blank" rel="noopener">GitHub ↗</a>
    <button class="menu" id="menuBtn" aria-label="Menu">☰</button>
  </div>
</header>
<main>
{body}
</main>
<footer class="foot">
  <div class="wrap">
    <p class="footbrand">Stanford AI · Course Map</p>
    <p>2026–27 · Unofficial. Course information is based on <a href="https://explorecourses.stanford.edu/" target="_blank" rel="noopener">ExploreCourses</a>; always check the official syllabus.</p>
    <p><a href="{base}index.html#about">About this edition</a> · <a href="{esc(zh_link)}">中文完整版</a></p>
  </div>
</footer>
<script src="{asset_base}assets/app.js"></script>
{extra_scripts}
</body>
</html>"""
    return "\n".join(line.rstrip() for line in html_text.splitlines()) + "\n"


def course_card(c: dict, base: str = "") -> str:
    badge = "Core" if c["type"] == "core" else "Related"
    tags = "".join(f"<span>{esc(t)}</span>" for t in c.get("tags", [])[:3])
    search = " ".join(
        [c["id"], c["title"], c.get("zh", ""), c["one"], " ".join(c.get("tags", []))]
    ).lower()
    return f"""<a class="ccard" href="{base}courses/{esc(c['slug'])}.html" data-type="{c['type']}" data-cat="{esc(c['cat'])}" data-code="{esc(c['id'])}" data-diff="{c.get('difficulty') or 0}" data-search="{esc(search)}">
  <div class="ccard-top"><span class="ccard-code">{esc(c['id'])}</span><span class="ccard-badge {'ext' if c['type'] == 'ext' else ''}">{badge}</span></div>
  <h3>{esc(c['title'])}</h3>
  <p>{esc(c['one'])}</p>
  <div class="ccard-meta"><span>{esc(c['terms'])}</span><span class="stars">{stars(c.get('difficulty'))}</span></div>
  <div class="ccard-tags">{tags}</div>
</a>"""


def course_page(c: dict, all_courses: list[dict], ui: dict, pages: dict) -> str:
    related = []
    by_id = {x["id"]: x for x in all_courses}
    for rid in c.get("related", [])[:3]:
        found = by_id.get(rid)
        if found:
            related.append(found)
    if not related:
        related = [x for x in all_courses if x["cat"] == c["cat"] and x["id"] != c["id"]][:3]
    related_html = "".join(
        f'<a class="relcard" href="{esc(x["slug"])}.html"><span>{esc(x["id"])}</span><b>{esc(x["title"])}</b></a>'
        for x in related
    )

    topics = c.get("topics", [])
    if topics:
        topics_html = '<ol class="topic-list">' + "".join(f"<li>{md(t)}</li>" for t in topics) + "</ol>"
    else:
        topics_html = '<p class="muted">This is a related-course page: the official description below is the main content.</p>'

    links = [
        f'<a class="res" href="https://explorecourses.stanford.edu/search?view=catalog&academicYear=20262027&q={esc(c["id"]).replace(" ", "+")}" target="_blank" rel="noopener"><span>ExploreCourses</span><b>↗</b></a>'
    ]
    for label, url in c.get("links", []):
        links.append(
            f'<a class="res" href="{esc(url)}" target="_blank" rel="noopener"><span>{esc(LINK_LABELS.get(label, "Link"))}</span><b>↗</b></a>'
        )

    zh_page = SITE / "courses" / f"{c['slug']}.html"
    zh_aside = (
        f'<a class="res" href="../../courses/{esc(c["slug"])}.html"><span>Read this page in Chinese</span><b>↗</b></a>'
        if zh_page.exists()
        else ""
    )
    md_link = (
        f'<a class="res" href="https://github.com/logic77lhl/stanford-ai-courses/blob/main/courses/en/{esc(c["slug"])}.md" target="_blank" rel="noopener"><span>Markdown on GitHub</span><b>↗</b></a>'
        if c["type"] == "core"
        else ""
    )
    status_note = (
        '<p class="note-inline">Draft translation: official facts are checked; wording may change after native review.</p>'
        if c.get("status") != "reviewed"
        else ""
    )
    note_html = f'<p class="note-inline">{esc(c["note"])}</p>' if c.get("note") else ""
    badge = pages["common"]["core"] if c["type"] == "core" else pages["common"]["ext"]

    body = f"""<div class="wrap">
  <a class="back" href="../index.html#courses">← Back to the course map</a>

  <section class="course-hero">
    <div class="course-poster">
      <span class="cp-kicker">Stanford · 2026—27</span>
      <span class="cp-code">{esc(c['id'])}</span>
      <span class="cp-cat">{esc(c['cat_en'])}</span>
      <span class="cp-stars">{stars(c.get('difficulty'))}</span>
    </div>
    <div class="course-head">
      <p class="kicker">{esc(badge)} · {esc(c['cat_en'])}</p>
      <h1>{esc(c['title'])}</h1>
      <p class="course-en">中文：{esc(c['zh'])}</p>
      <p class="course-one">{esc(c['one'])}</p>
      {status_note}
      {note_html}
      <div class="meta-chips">
        <span>{esc(c['units'])} units</span>
        <span>{esc(c['terms'])}</span>
        <span>{esc(c['grading'])}</span>
        <span>{stars(c.get('difficulty'))}</span>
      </div>
      <div class="tagrow">{''.join(f'<span>{esc(t)}</span>' for t in c.get('tags', []))}</div>
    </div>
  </section>

  <div class="course-layout">
    <article class="course-main">
      <section class="prose">
        <h2>{esc(ui['sections']['positioning'])}</h2>
        <p>{esc(c['pos'])}</p>
      </section>

      <section class="prose">
        <h2>{esc(ui['sections']['topics'])}</h2>
        {topics_html}
      </section>

      <section class="prose two">
        <div><h2>{esc(ui['sections']['prereq'])}</h2><p>{esc(c['prereq'])}</p></div>
        <div><h2>{esc(ui['sections']['assessment'])}</h2><p>{esc(c['assessment'])}</p></div>
      </section>

      <section class="prose two">
        <div><h2>{esc(ui['sections']['who'])}</h2><p>{esc(c['who'])}</p></div>
        <div><h2>{esc(ui['sections']['tips'])}</h2><p>{esc(c['tips'])}</p></div>
      </section>

      <section class="prose">
        <h2>{esc(ui['sections']['related'])}</h2>
        <div class="related-grid">{related_html}</div>
      </section>

      <section class="prose">
        <details class="official">
          <summary>{esc(ui['sections']['official'])}</summary>
          <p>{esc(c.get('description', ''))}</p>
        </details>
      </section>
    </article>

    <aside class="course-aside">
      <div class="aside-card">
        <div class="aside-head"><h3>{esc(ui['sections']['facts'])}</h3></div>
        <dl class="facts">
          <div><dt>Course</dt><dd>{esc(c['id'])}</dd></div>
          <div><dt>Term</dt><dd>{esc(c['terms'])}</dd></div>
          <div><dt>Units</dt><dd>{esc(c['units'])}</dd></div>
          <div><dt>Grading</dt><dd>{esc(c['grading'])}</dd></div>
          <div><dt>Instructors</dt><dd>{esc(c['instructors'])}</dd></div>
          <div><dt>Difficulty</dt><dd>{stars(c.get('difficulty'))}</dd></div>
        </dl>
      </div>
      <div class="aside-card">
        <div class="aside-head"><h3>{esc(ui['sections']['resources'])}</h3></div>
        {''.join(links)}
        {zh_aside}
        {md_link}
      </div>
    </aside>
  </div>
</div>"""
    return shell(
        f"{c['id']} · {c['title']} | Stanford AI Course Map",
        c["one"],
        body,
        base="../",
        active="courses",
        zh_link=f"../../courses/{c['slug']}.html" if zh_page.exists() else "../../index.html",
        alt_zh=(
            f"https://logic77lhl.github.io/stanford-ai-courses/courses/{c['slug']}.html"
            if zh_page.exists()
            else "https://logic77lhl.github.io/stanford-ai-courses/"
        ),
        alt_en=f"https://logic77lhl.github.io/stanford-ai-courses/en/courses/{c['slug']}.html",
    )


def index_page(items: list[dict], ui: dict, pages: dict, total_core: int, total_ext: int) -> str:
    cat_order = list(ui["categories"].keys())
    items_sorted = sorted(
        items,
        key=lambda c: (
            cat_order.index(c["cat"]) if c["cat"] in cat_order else 99,
            0 if c["type"] == "core" else 1,
            c["id"],
        ),
    )
    cards = "".join(course_card(c) for c in items_sorted)
    chips = '<button class="chip on" data-cat="all">All</button>' + "".join(
        f'<button class="chip" data-cat="{esc(key)}">{esc(label)}</button>'
        for key, label in ui["categories"].items()
    )
    body = f"""<div class="wrap">
  <section class="hero" id="map">
    <p class="kicker">{esc(ui['index']['kicker'])}</p>
    <h1>{ui['index']['title']}</h1>
    <p class="hero-lede">{esc(ui['index']['lede'])}</p>
    <p class="hero-lede" style="color:var(--gold)">{esc(ui['index']['pilot'].format(n=len(items), total=total_core))}</p>
    <div class="hero-actions">
      <a class="btn gold" href="#courses">Browse all courses</a>
      <a class="btn" href="../index.html">{esc(ui['index']['browse'])}</a>
    </div>
    <div class="stats" style="grid-template-columns:repeat(3,1fr)">
      <div class="stat gold"><b>{total_core}</b><span>Core courses</span></div>
      <div class="stat"><b>{total_ext}</b><span>Related courses</span></div>
      <div class="stat"><b>{len(items)}</b><span>Total course pages</span></div>
    </div>
  </section>

  <section class="section" id="courses">
    <div class="section-head"><h2>All courses</h2><small>Search / filter / sort</small><span class="line"></span><span class="count" id="courseCount"></span></div>
    <div class="toolbar">
      <input type="search" id="courseSearch" placeholder="Search course code, title, tag…" autocomplete="off">
      <div class="seg" id="typeSeg">
        <button class="on" data-type="all">All</button>
        <button data-type="core">Core</button>
        <button data-type="ext">Related</button>
      </div>
      <select id="courseSort">
        <option value="code">By course code</option>
        <option value="name">By title</option>
        <option value="diff">By difficulty</option>
      </select>
    </div>
    <div class="chips" id="catChips">{chips}</div>
    <div class="course-grid" id="courseGrid">{cards}</div>
    <p class="empty" id="courseEmpty" hidden>No matching courses.</p>
  </section>

  <section class="section" id="about">
    <div class="section-head"><h2>About this edition</h2><span class="line"></span></div>
    <p class="muted">{esc(ui['index']['about_body'])}</p>
    <p class="muted">{esc(ui['index']['footnote'])}</p>
  </section>
</div>
<script>
(function () {{
  var grid = document.getElementById('courseGrid');
  var cards = Array.prototype.slice.call(grid.querySelectorAll('.ccard'));
  var q = document.getElementById('courseSearch');
  var sort = document.getElementById('courseSort');
  var count = document.getElementById('courseCount');
  var empty = document.getElementById('courseEmpty');
  var chips = Array.prototype.slice.call(document.querySelectorAll('#catChips .chip'));
  var types = Array.prototype.slice.call(document.querySelectorAll('#typeSeg button'));
  var state = {{ cat: 'all', type: 'all', text: '' }};
  function apply() {{
    var list = cards.filter(function (c) {{
      if (state.type !== 'all' && c.dataset.type !== state.type) return false;
      if (state.cat !== 'all' && c.dataset.cat !== state.cat) return false;
      if (state.text && c.dataset.search.indexOf(state.text) === -1) return false;
      return true;
    }});
    if (sort.value === 'name') {{
      list.sort(function (a, b) {{ return a.querySelector('h3').textContent.localeCompare(b.querySelector('h3').textContent, 'en'); }});
    }} else if (sort.value === 'diff') {{
      list.sort(function (a, b) {{ return Number(b.dataset.diff) - Number(a.dataset.diff) || a.dataset.code.localeCompare(b.dataset.code, 'en', {{ numeric: true }}); }});
    }} else {{
      list.sort(function (a, b) {{ return a.dataset.code.localeCompare(b.dataset.code, 'en', {{ numeric: true }}); }});
    }}
    grid.innerHTML = '';
    list.forEach(function (c) {{ grid.appendChild(c); }});
    count.textContent = list.length + ' courses';
    empty.hidden = list.length !== 0;
  }}
  q.addEventListener('input', function () {{ state.text = q.value.trim().toLowerCase(); apply(); }});
  sort.addEventListener('change', apply);
  chips.forEach(function (ch) {{
    ch.addEventListener('click', function () {{
      state.cat = ch.dataset.cat;
      chips.forEach(function (x) {{ x.classList.toggle('on', x === ch); }});
      apply();
    }});
  }});
  types.forEach(function (btn) {{
    btn.addEventListener('click', function () {{
      state.type = btn.dataset.type;
      types.forEach(function (x) {{ x.classList.toggle('on', x === btn); }});
      apply();
    }});
  }});
  apply();
}})();
</script>"""
    return shell(
        "Stanford AI Course Map · English",
        ui["index"]["lede"],
        body,
        active="map",
        zh_link="../index.html",
        alt_zh="https://logic77lhl.github.io/stanford-ai-courses/",
        alt_en="https://logic77lhl.github.io/stanford-ai-courses/en/",
    )


def paths_page(items: list[dict], paths: list[dict], pages: dict) -> str:
    by_id = {c["id"]: c for c in items}
    blocks = []
    for i, p in enumerate(paths, 1):
        steps = "".join(
            f'<a class="step" href="courses/{by_id[sid]["slug"]}.html"><span>{n:02d}</span><b>{esc(sid)}</b><small>{esc(by_id[sid]["title"])}</small></a>'
            for n, sid in enumerate(p["steps"], 1)
            if sid in by_id
        )
        also = "".join(
            f'<a class="also" href="courses/{by_id[sid]["slug"]}.html">{esc(sid)}</a>'
            for sid in p["also"]
            if sid in by_id
        )
        blocks.append(f"""<section class="path-detail">
  <div class="path-detail-head">
    <span class="path-index">{i:02d}</span>
    <div><h2>{esc(p['name'])}</h2><p>{esc(p['desc'])}</p></div>
  </div>
  <div class="steps">{steps}</div>
  <div class="also-row"><span>{esc(pages['paths']['also'])}</span>{also}</div>
</section>""")
    body = f"""<div class="wrap">
  <a class="back" href="index.html">{esc(pages['common']['backHome'])}</a>
  <section class="page-hero">
    <p class="kicker">{esc(pages['paths']['kicker'])}</p>
    <h1>{esc(pages['paths']['title'])}</h1>
    <p>{esc(pages['paths']['lede'])}</p>
  </section>
  {''.join(blocks)}
</div>"""
    return shell(
        "Learning Paths | Stanford AI Course Map",
        pages["paths"]["lede"],
        body,
        active="paths",
        zh_link="../paths.html",
        alt_zh="https://logic77lhl.github.io/stanford-ai-courses/paths.html",
        alt_en="https://logic77lhl.github.io/stanford-ai-courses/en/paths.html",
    )


def semester_page(items: list[dict], pages: dict) -> str:
    terms = ["Autumn 2026", "Winter 2027", "Spring 2027", "Summer 2027"]
    groups = {t: [] for t in terms}
    other = []
    for c in items:
        hit = [t for t in terms if t in str(c.get("terms", ""))]
        if not hit:
            other.append(c)
        for t in hit:
            groups[t].append(c)

    def ordered(rows):
        return sorted(rows, key=lambda c: (0 if c["type"] == "core" else 1, c["id"]))

    def rows_html(rows):
        out = ""
        for c in rows:
            kind = pages["semester"]["core"] if c["type"] == "core" else pages["semester"]["ext"]
            out += (
                f'<a class="term-row" href="courses/{c["slug"]}.html">'
                f'<span class="term-code">{esc(c["id"])}</span>'
                f'<span class="term-name">{esc(c["title"])}</span>'
                f'<span class="term-type {c["type"]}">{kind}</span>'
                f"</a>"
            )
        return out

    core_total = sum(1 for c in items if c["type"] == "core")
    blocks = []
    for t in terms:
        group = ordered(groups[t])
        if not group:
            continue
        core_n = sum(1 for c in group if c["type"] == "core")
        blocks.append(f"""<section class="term-block">
  <div class="term-head"><h2>{esc(t)}</h2><span>{core_n} core · {len(group) - core_n} related</span></div>
  <div class="term-list">{rows_html(group)}</div>
</section>""")

    other_rows = ordered(other)
    blocks.append(f"""<section class="term-block">
  <div class="term-head"><h2>{esc(pages['semester']['notOffered'])}</h2><span>{len(other_rows)} courses</span></div>
  <p class="muted">{esc(pages['semester']['notOfferedNote'])}</p>
  <div class="term-list">{rows_html(other_rows)}</div>
</section>""")

    body = f"""<div class="wrap">
  <a class="back" href="index.html">{esc(pages['common']['backHome'])}</a>
  <section class="page-hero">
    <p class="kicker">{esc(pages['semester']['kicker'])}</p>
    <h1>{esc(pages['semester']['title'])}</h1>
    <p>{esc(pages['semester']['lede'])}</p>
  </section>
  {''.join(blocks)}
</div>"""
    return shell(
        "Courses by Term | Stanford AI Course Map",
        pages["semester"]["lede"],
        body,
        active="semester",
        zh_link="../semester.html",
        alt_zh="https://logic77lhl.github.io/stanford-ai-courses/semester.html",
        alt_en="https://logic77lhl.github.io/stanford-ai-courses/en/semester.html",
    )


def prereq_svg(items: list[dict], prereqs: dict) -> str:
    by_id = {c["id"]: c for c in items}
    levels = prereqs.get("levels", [])
    edges = prereqs.get("edges", [])
    node_w, node_h = 178, 50
    gap_x, gap_y, top = 270, 68, 66
    max_n = max((len(l["courses"]) for l in levels), default=1)
    width = 40 + (len(levels) - 1) * gap_x + node_w + 40
    height = top + (max_n - 1) * gap_y + node_h + 26
    pos = {}
    for li, level in enumerate(levels):
        n = len(level["courses"])
        start_y = top + (max_n - n) * gap_y / 2
        for j, cid in enumerate(level["courses"]):
            pos[cid] = (40 + li * gap_x, start_y + j * gap_y)

    parts = [
        f'<svg class="prereq-svg" viewBox="0 0 {width} {height}" role="img" aria-label="Course prerequisite graph">',
        '<defs><marker id="pg-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
        '<path d="M 0 0 L 10 5 L 0 10 z" fill="rgba(255,255,255,.28)"></path></marker></defs>',
    ]
    for li, level in enumerate(levels):
        x = 40 + li * gap_x
        parts.append(f'<text class="pg-level" x="{x}" y="30">{esc(level["name"])}</text>')
    for a, b in edges:
        if a not in pos or b not in pos:
            continue
        x1, y1 = pos[a]
        x2, y2 = pos[b]
        sx, sy = x1 + node_w, y1 + node_h / 2
        ex, ey = x2, y2 + node_h / 2
        mx = (sx + ex) / 2
        parts.append(
            f'<path class="pg-edge" d="M{sx:.0f},{sy:.0f} C{mx:.0f},{sy:.0f} {mx:.0f},{ey:.0f} {ex:.0f},{ey:.0f}" marker-end="url(#pg-arrow)"></path>'
        )
    for cid, (x, y) in pos.items():
        c = by_id.get(cid)
        if not c:
            continue
        cls = "core" if c["type"] == "core" else "ext"
        name = c["title"] if len(c["title"]) <= 28 else c["title"][:27] + "…"
        parts.append(
            f'<g class="pnode {cls}" transform="translate({x:.0f},{y:.0f})">'
            f"<title>{esc(cid)} · {esc(c['title'])}</title>"
            f'<rect width="{node_w}" height="{node_h}" rx="6"></rect>'
            f'<text class="pcode" x="12" y="21">{esc(cid)}</text>'
            f'<text class="pname" x="12" y="38">{esc(name)}</text>'
            f"</g>"
        )
    parts.append("</svg>")
    return "".join(parts)


def prereqs_page(items: list[dict], prereqs: dict, pages: dict) -> str:
    by_id = {c["id"]: c for c in items}
    graph_ids = [cid for level in prereqs.get("levels", []) for cid in level["courses"] if cid in by_id]
    rows = "".join(
        f'<div class="prereq-item"><a class="prereq-code" href="courses/{by_id[cid]["slug"]}.html">{esc(cid)}</a>'
        f'<b>{esc(by_id[cid]["title"])}</b><p>{esc(by_id[cid].get("prereq") or "See the official description.")}</p></div>'
        for cid in sorted(graph_ids, key=lambda x: (0 if by_id[x]["type"] == "core" else 1, x))
    )
    body = f"""<div class="wrap">
  <a class="back" href="index.html">{esc(pages['common']['backHome'])}</a>
  <section class="page-hero">
    <p class="kicker">{esc(pages['prereqs']['kicker'])}</p>
    <h1>{esc(pages['prereqs']['title'])}</h1>
    <p>{esc(prereqs.get('note', ''))}</p>
  </section>
  <section class="prereq-wrap">
    <div class="prereq-legend">
      <span><i class="dot core"></i>{esc(pages['prereqs']['legendCore'])}</span>
      <span><i class="dot ext"></i>{esc(pages['prereqs']['legendExt'])}</span>
      <span>{esc(pages['prereqs']['legendArrow'])}</span>
    </div>
    <div class="prereq-scroll">{prereq_svg(items, prereqs)}</div>
  </section>
  <section class="prereq-list">
    <div class="section-head"><h2>{esc(pages['prereqs']['listTitle'])}</h2><small>{esc(pages['prereqs']['listNote'])}</small><span class="line"></span></div>
    <div class="prereq-grid">{rows}</div>
  </section>
</div>"""
    return shell(
        "Prerequisites | Stanford AI Course Map",
        "Prerequisite graph and prerequisite text for Stanford AI/ML/Agent courses.",
        body,
        active="prereqs",
        zh_link="../prereqs.html",
        alt_zh="https://logic77lhl.github.io/stanford-ai-courses/prereqs.html",
        alt_en="https://logic77lhl.github.io/stanford-ai-courses/en/prereqs.html",
    )


def bilibili_page(items: list[dict], lectures: dict, pages: dict) -> str:
    grouped: dict[str, list] = {}
    for c in items:
        links = lectures.get(c["id"], {}).get("bilibili") or []
        if not links:
            continue
        grouped.setdefault(c["cat_en"], []).append((c, links))

    blocks = []
    for cat, entries in grouped.items():
        cards = ""
        for c, links in entries:
            link_html = "".join(
                f'<a class="bili-link" href="{esc(url)}" target="_blank" rel="noopener">{esc(link_label(label))} ↗</a>'
                for label, url in links
            )
            link_html += (
                f'<a class="bili-report" href="{esc(bili_report_url(c["id"], links))}" target="_blank" rel="noopener">{esc(pages["bilibili"]["report"])} ↗</a>'
            )
            cards += (
                f'<div class="bili-item"><div><span class="bili-code">{esc(c["id"])}</span>'
                f'<a class="bili-title" href="courses/{c["slug"]}.html">{esc(c["title"])}</a></div>'
                f'<div class="bili-links">{link_html}</div></div>'
            )
        blocks.append(f'<section class="bili-group"><h2>{esc(cat)}</h2>{cards}</section>')

    body = f"""<div class="wrap">
  <a class="back" href="index.html">{esc(pages['common']['backHome'])}</a>
  <section class="page-hero">
    <p class="kicker">{esc(pages['bilibili']['kicker'])}</p>
    <h1>{esc(pages['bilibili']['title'])}</h1>
    <p>{esc(pages['bilibili']['lede'])}</p>
  </section>
  {''.join(blocks)}
</div>"""
    return shell(
        "Bilibili Resources | Stanford AI Course Map",
        pages["bilibili"]["lede"],
        body,
        active="bilibili",
        zh_link="../bilibili.html",
        alt_zh="https://logic77lhl.github.io/stanford-ai-courses/bilibili.html",
        alt_en="https://logic77lhl.github.io/stanford-ai-courses/en/bilibili.html",
    )


def not_found(pages: dict) -> str:
    body = f"""<div class="wrap"><section class="page-hero"><p class="kicker">404</p><h1>This course is not on the map</h1><p>The link may have changed. Go back to the <a href="index.html">course map</a>.</p></section></div>"""
    return shell("404 | Stanford AI Course Map", "Page not found", body, zh_link="../index.html")


def main() -> None:
    items = load_json(DATA / "courses.en.json")
    ui = load_json(DATA / "i18n" / "ui.en.json")
    pages = load_json(DATA / "i18n" / "pages.en.json")
    paths = load_json(DATA / "i18n" / "paths.en.json")
    prereqs = load_json(DATA / "i18n" / "prereqs.en.json")
    lectures = load_lectures()

    OUT.mkdir(parents=True, exist_ok=True)
    COURSES_OUT.mkdir(parents=True, exist_ok=True)
    for old in COURSES_OUT.glob("*.html"):
        old.unlink()

    for c in items:
        (COURSES_OUT / f"{c['slug']}.html").write_text(
            course_page(c, items, ui, pages), encoding="utf-8", newline="\n"
        )

    core_n = sum(1 for c in items if c["type"] == "core")
    ext_n = sum(1 for c in items if c["type"] == "ext")
    (OUT / "index.html").write_text(
        index_page(items, ui, pages, core_n, ext_n), encoding="utf-8", newline="\n"
    )
    (OUT / "paths.html").write_text(paths_page(items, paths, pages), encoding="utf-8", newline="\n")
    (OUT / "semester.html").write_text(semester_page(items, pages), encoding="utf-8", newline="\n")
    (OUT / "prereqs.html").write_text(prereqs_page(items, prereqs, pages), encoding="utf-8", newline="\n")
    (OUT / "bilibili.html").write_text(bilibili_page(items, lectures, pages), encoding="utf-8", newline="\n")
    (OUT / "404.html").write_text(not_found(pages), encoding="utf-8", newline="\n")
    print(f"English site: {core_n} core + {ext_n} related course pages, 5 top-level pages")


if __name__ == "__main__":
    main()
