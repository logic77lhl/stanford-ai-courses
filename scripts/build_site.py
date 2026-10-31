#!/usr/bin/env python3
"""Build the GitHub Pages site under docs/.

Usage:
    python scripts/build_site.py

Reads:
    data/catalog.json
    data/courses.json
    data/more_courses.json
    data/resources.json
Writes:
    docs/index.html
    docs/paths.html
    docs/courses/*.html
    docs/assets/courses.js
    docs/404.html
    docs/.nojekyll
"""

from __future__ import annotations

import html
import json
import re
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "docs"
COURSES_OUT = SITE / "courses"
ASSETS = SITE / "assets"

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

CATEGORY_BLURB = {
    "基础核心": "ML 的地基：概率、优化、监督/无监督、生成模型与图学习。",
    "LLM 与 Agent": "从 Transformer 到 agent 工程：训练、对齐、RAG、eval、长程任务。",
    "ML 系统与硬件": "训练/推理基础设施、GPU 集群、编译器和 AI 芯片。",
    "视觉、图形与生成": "识别、3D、神经渲染、扩散模型与计算成像。",
    "机器人、具身智能": "运动学、SLAM、操作、模仿学习与 embodied AI。",
    "AI for Science 与医疗": "基因组、蛋白、医疗 FM、神经科学与科学发现。",
    "产品、伦理与设计": "AI 产品、人机交互、公平、可解释与治理。",
    "统计与优化": "统计学习、因果、安全约束、生成模型效率。",
}

TECH_BY_CAT = {
    "基础核心": ["Python", "NumPy", "PyTorch", "scikit-learn"],
    "LLM 与 Agent": ["Python", "PyTorch", "Hugging Face", "DSPy", "LLM API"],
    "ML 系统与硬件": ["Python", "C++", "CUDA", "Triton", "PyTorch"],
    "视觉、图形与生成": ["Python", "PyTorch", "OpenCV", "CUDA"],
    "机器人、具身智能": ["Python", "C++", "ROS", "PyTorch"],
    "AI for Science 与医疗": ["Python", "PyTorch", "Biopython", "RDKit"],
    "产品、伦理与设计": ["Python", "LLM API", "Eval", "Figma"],
    "统计与优化": ["Python", "R", "scikit-learn", "CVXPY"],
}

FEATURED = ["CS 229", "CS 224N", "CS 231N", "CS 336", "CS 224V", "CS 329Z", "EE 292R", "CS 223A"]

PATHS = [
    {
        "name": "LLM / Agent 工程",
        "short": "做 AI engineer、agent 产品、LLM 应用",
        "desc": "从 NLP 地基到 agent 工程，再到从零训练语言模型。重点是 eval，而不是只搭 demo。",
        "steps": ["CS 224N", "CS 329Z", "CS 224V", "CS 336"],
        "also": ["CS 329H", "CS 329T", "CS 224G", "CS 25", "MS&E 203"],
    },
    {
        "name": "ML 研究 / 读博",
        "short": "读博、做 ML theory / 生成模型 / RL",
        "desc": "先把监督学习、无监督学习和学习理论打通，再选一个方向做深。",
        "steps": ["CS 229", "CS 229M", "CS 236", "CS 234"],
        "also": ["STATS 315A", "CS 228", "CS 330", "CS 332"],
    },
    {
        "name": "CV / 生成 / 3D",
        "short": "视觉、3D 生成、图形",
        "desc": "识别 → 生成模型 → 3D 表示/渲染，形成完整的视觉与图形栈。",
        "steps": ["CS 231N", "CS 236", "CS 348N", "CS 468"],
        "also": ["CS 231A", "CS 236G", "CS 348I", "CS 448I"],
    },
    {
        "name": "机器人 / 具身",
        "short": "机器人、具身智能、自动驾驶",
        "desc": "运动学与控制 → 自主系统 → 学习与操作 → 具身研究。",
        "steps": ["CS 223A", "CS 237A", "CS 237B", "CS 381"],
        "also": ["CS 225A", "CS 227A", "CS 234", "CS 231N"],
    },
    {
        "name": "MLSys / 推理",
        "short": "训练/推理基础设施、AI 芯片",
        "desc": "从 ML 系统设计到推理 serving，再到加速器与网络。",
        "steps": ["CS 229S", "CS 349D", "CS 349E", "CS 217"],
        "also": ["CS 329S", "CS 349F", "CS 149", "MS&E 319"],
    },
    {
        "name": "AI4Science / 医疗",
        "short": "计算生物、医疗 AI、科学发现",
        "desc": "ML 基础 → 领域数据 → 医疗/生物 FM → 前沿讲座。",
        "steps": ["CS 229", "CS 273B", "CS 277", "EE 292R"],
        "also": ["CS 279", "CS 287", "CS 375", "CS 286"],
    },
]

FAVICON = (
    "data:image/svg+xml,"
    "%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E"
    "%3Crect width='64' height='64' rx='14' fill='%2309090b'/%3E"
    "%3Ccircle cx='32' cy='32' r='15' fill='none' stroke='%23d4b176' stroke-width='4'/%3E"
    "%3Ccircle cx='32' cy='32' r='4' fill='%23d4b176'/%3E%3C/svg%3E"
)


def esc(value: object) -> str:
    return html.escape(str(value or ""), quote=True)


def md(value: str) -> str:
    return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", esc(value))


def slugify(value: str) -> str:
    value = value.lower().replace("&", "")
    return re.sub(r"[^a-z0-9]+", "-", value).strip("-")


def stars(level: int | None) -> str:
    if level is None:
        return "—"
    level = max(1, min(5, int(level)))
    return "★" * level + "☆" * (5 - level)


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_site_data():
    catalog = {c["id"]: c for c in load_json(ROOT / "data" / "catalog.json")}
    core = load_json(ROOT / "data" / "courses.json")
    more = load_json(ROOT / "data" / "more_courses.json")
    resources = load_json(ROOT / "data" / "resources.json") if (ROOT / "data" / "resources.json").exists() else {}

    items = []
    for c in core:
        items.append({**c, "type": "core", "title_en": c["title"], "card_desc": c["one"], "search": " ".join(
            [c["id"], c["zh"], c["title"], c["one"], " ".join(c.get("tags", []))]
        )})

    for m in more:
        cid = m["id"]
        if cid not in catalog:
            continue
        cat = catalog[cid]
        title = cat["title"]
        slug = slugify(f"{cid} {title}")
        items.append({
            "id": cid,
            "slug": slug,
            "zh": m.get("tag", title),
            "cat": m.get("cat", "基础核心"),
            "type": "ext",
            "difficulty": None,
            "one": f"延伸课程 · {m.get('tag', '')}。本页保留官方档案与入口，详细内容见官方描述。",
            "card_desc": title,
            "pos": f"{title} 是与「{m.get('tag', '')}」相关的延伸课程。当前版本只整理官方档案与入口，中文速览待补充；先读官方描述和课程官网。",
            "prereq": "见官方描述（延伸课程暂未单独整理先修）。",
            "assessment": "以当季官网为准（延伸课程暂未单独整理考核）。",
            "who": f"对「{m.get('tag', '')}」方向感兴趣的人。",
            "tips": "先读官方描述和课程官网，再判断是否适合自己。",
            "title": title,
            "title_en": title,
            "description": cat["description"],
            "units": cat["units_min"] if cat["units_min"] == cat["units_max"] else f"{cat['units_min']}–{cat['units_max']}",
            "grading": cat["grading"],
            "terms": terms_cn(cat["terms"]),
            "instructors": ", ".join((cat.get("instructors_pi") or cat.get("instructors") or [])[:4]) or "TBA",
            "tags": [m.get("tag", "延伸")],
            "search": " ".join([cid, title, m.get("tag", ""), cat["description"]]),
        })

    items.sort(key=lambda c: (CATEGORY_ORDER.index(c["cat"]) if c["cat"] in CATEGORY_ORDER else 99, c["id"]))
    return items, resources, catalog


def terms_cn(terms: list[str]) -> str:
    if not terms:
        return "2026–27 未排课"
    mapping = {
        "2026-2027 Autumn": (0, "2026 秋"),
        "2026-2027 Winter": (1, "2027 冬"),
        "2026-2027 Spring": (2, "2027 春"),
        "2026-2027 Summer": (3, "2027 夏"),
    }
    ordered = sorted(terms, key=lambda t: mapping.get(t, (99, t))[0])
    return " / ".join(mapping.get(t, (99, t))[1] for t in ordered)


def ec_url(cid: str) -> str:
    return "https://explorecourses.stanford.edu/search?view=catalog&academicYear=20262027&q=" + urllib.parse.quote_plus(cid)


def yt_search(cid: str, title: str) -> str:
    return "https://www.youtube.com/results?search_query=" + urllib.parse.quote_plus(f"Stanford {cid} {title}")


def gh_search(cid: str) -> str:
    return "https://github.com/search?q=" + urllib.parse.quote_plus(f"Stanford {cid}") + "&type=repositories"


def header(base: str = "", active: str = "") -> str:
    def cls(key: str) -> str:
        return " class=\"on\"" if active == key else ""

    return f"""<header class="top">
  <div class="wrap topin">
    <a class="brand" href="{base}index.html">Stanford AI <span>课程地图</span></a>
    <nav class="nav" id="nav">
      <a href="{base}index.html#map"{cls("map")}>地图</a>
      <a href="{base}index.html#courses"{cls("courses")}>课程</a>
      <a href="{base}paths.html"{cls("paths")}>路径</a>
      <a href="{base}bilibili.html"{cls("bili")}>B站</a>
      <a href="{base}index.html#about"{cls("about")}>关于</a>
    </nav>
    <a class="gh" href="https://github.com/logic77lhl/stanford-ai-courses" target="_blank" rel="noopener">GitHub ↗</a>
    <button class="menu" id="menuBtn" aria-label="菜单">☰</button>
  </div>
</header>"""


def footer(base: str = "") -> str:
    return f"""<footer class="foot">
  <div class="wrap footin">
    <div>
      <p class="footbrand">Stanford AI · 课程地图</p>
      <p>2026–27 学年 · 非官方整理 · 课程信息以 <a href="https://explorecourses.stanford.edu/" target="_blank" rel="noopener">ExploreCourses</a> 为准。</p>
    </div>
    <div class="footlinks">
      <a href="{base}index.html#map">课程地图</a>
      <a href="{base}index.html#courses">全部课程</a>
      <a href="{base}paths.html">学习路径</a>
      <a href="https://github.com/logic77lhl/stanford-ai-courses" target="_blank" rel="noopener">GitHub</a>
    </div>
  </div>
</footer>"""


def shell(title: str, desc: str, body: str, base: str = "", active: str = "", extra_scripts: str = "") -> str:
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="theme-color" content="#09090b">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:type" content="website">
<link rel="icon" href="{FAVICON}">
<link rel="stylesheet" href="{base}assets/style.css">
</head>
<body>
{header(base, active)}
<main>
{body}
</main>
{footer(base)}
{extra_scripts}
<script src="{base}assets/app.js"></script>
</body>
</html>
"""


def course_card(c: dict, base: str = "") -> str:
    badge = "核心" if c["type"] == "core" else "延伸"
    tags = "".join(f"<span>{esc(t)}</span>" for t in c.get("tags", [])[:3])
    return f"""<a class="ccard" href="{base}courses/{c['slug']}.html"
   data-cat="{esc(c['cat'])}" data-type="{c['type']}" data-search="{esc(c['search'])}"
   data-diff="{c.get('difficulty') or 0}" data-code="{esc(c['id'])}">
  <div class="ccard-top">
    <span class="ccard-code">{esc(c['id'])}</span>
    <span class="ccard-badge {'ext' if c['type'] == 'ext' else ''}">{badge}</span>
  </div>
  <h3>{esc(c['zh'])}</h3>
  <p>{esc(c.get('card_desc', c['one']))}</p>
  <div class="ccard-meta">
    <span>{esc(c['terms'])}</span>
    <span class="stars">{stars(c.get('difficulty'))}</span>
  </div>
  <div class="ccard-tags">{tags}</div>
</a>"""


def poster_card(c: dict, base: str = "") -> str:
    return f"""<a class="poster-card" href="{base}courses/{c['slug']}.html">
  <div class="poster-art">
    <span class="poster-kicker">{esc(c['cat'])}</span>
    <span class="poster-code">{esc(c['id'])}</span>
    <span class="poster-line"></span>
  </div>
  <div class="poster-body">
    <h3>{esc(c['zh'])}</h3>
    <p>{esc(c['one'])}</p>
    <span class="poster-more">查看课程 →</span>
  </div>
</a>"""


def track_card(cat: str, index: int, courses: list[dict]) -> str:
    group = [x for x in courses if x["cat"] == cat]
    codes = " · ".join(x["id"] for x in group[:3])
    return f"""<button class="track" data-filter="{esc(cat)}">
  <span class="track-no">{index:02d}</span>
  <h3>{esc(cat)}</h3>
  <p>{esc(CATEGORY_BLURB.get(cat, ""))}</p>
  <div class="track-foot"><span>{len(group)} 门</span><span>{esc(codes)}</span></div>
</button>"""


def resource_items(c: dict, resources: dict) -> tuple[list[str], list[str], list[str], list[str], bool]:
    r = resources.get(c["id"], {})
    videos = list(r.get("videos", []))
    code = list(r.get("code", []))
    extra = list(r.get("extra", []))
    tech = r.get("tech") or TECH_BY_CAT.get(c["cat"], [])
    curated = bool(videos or code or extra)
    return videos, code, extra, tech, curated


def lecture_section(c: dict, lectures: dict) -> str:
    data = lectures.get(c["id"], {})
    schedule = data.get("schedule")
    slides = data.get("slides", [])
    rows = data.get("lectures", [])
    bili = data.get("bilibili", [])
    if not (schedule or slides or rows or bili):
        return ""

    tools = []
    if schedule:
        tools.append(f'<a class="ltool" href="{esc(schedule[1])}" target="_blank" rel="noopener">{esc(schedule[0])} ↗</a>')
    for label, url in slides:
        tools.append(f'<a class="ltool" href="{esc(url)}" target="_blank" rel="noopener">{esc(label)} ↗</a>')
    for label, url in bili:
        tools.append(f'<a class="ltool bili" href="{esc(url)}" target="_blank" rel="noopener">B站 · {esc(label)} ↗</a>')

    if rows:
        head = '<div class="lecture-row head"><span>#</span><span>主题 / 讲者</span></div>'
        body = "".join(
            f'<div class="lecture-row"><span class="ln">{int(r.get("n", i + 1)):02d}</span><span>{esc(r.get("title", ""))}</span></div>'
            for i, r in enumerate(rows)
        )
        table = f'<div class="lecture-table">{head}{body}</div>'
    else:
        table = '<p class="muted">逐讲大纲暂未整理；官方 schedule / slides 见上方入口。</p>'

    note = data.get("note", "")
    note_html = f'<p class="lecture-note">{esc(note)}</p>' if note else ""

    return f"""<section class="prose">
  <h2>课程大纲 / 课件</h2>
  <div class="lecture-tools">{''.join(tools)}</div>
  {table}
  {note_html}
</section>"""


def resource_block(c: dict, resources: dict, lectures: dict) -> str:
    videos, code, extra, tech, curated = resource_items(c, resources)

    def links(items, cls="res"):
        return "".join(
            f'<a class="{cls}" href="{esc(url)}" target="_blank" rel="noopener"><span>{esc(label)}</span><b>↗</b></a>'
            for label, url in items
        )

    official = "".join(
        f'<a class="res" href="{esc(url)}" target="_blank" rel="noopener"><span>{esc(label)}</span><b>↗</b></a>'
        for label, url in c.get("links", [])
    )
    ec = f'<a class="res" href="{esc(ec_url(c["id"]))}" target="_blank" rel="noopener"><span>ExploreCourses</span><b>↗</b></a>'

    blocks = [f'<div class="resgroup"><h4>官方入口</h4>{official}{ec}</div>']

    if videos:
        blocks.append(f'<div class="resgroup"><h4>视频</h4>{links(videos)}</div>')
    if code:
        blocks.append(f'<div class="resgroup"><h4>代码 / 仓库</h4>{links(code)}</div>')
    if extra:
        blocks.append(f'<div class="resgroup"><h4>延伸阅读</h4>{links(extra)}</div>')
    bili = lectures.get(c["id"], {}).get("bilibili", [])
    if bili:
        blocks.append(f'<div class="resgroup"><h4>B站视频</h4>{links(bili, "res bili")}</div>')

    if not curated:
        blocks.append(
            f'<div class="resgroup"><h4>搜索入口</h4>'
            f'<a class="res" href="{esc(yt_search(c["id"], c["title"]))}" target="_blank" rel="noopener"><span>YouTube 搜索</span><b>↗</b></a>'
            f'<a class="res" href="{esc(gh_search(c["id"]))}" target="_blank" rel="noopener"><span>GitHub 搜索</span><b>↗</b></a>'
            f'</div>'
        )

    tech_html = "".join(f"<span>{esc(t)}</span>" for t in tech)
    badge = '<span class="resbadge on">已核验</span>' if curated else '<span class="resbadge">官方入口</span>'

    return f"""<div class="aside-card">
  <div class="aside-head"><h3>资源</h3>{badge}</div>
  {''.join(blocks)}
  <div class="resgroup"><h4>常见工具</h4><div class="tech">{tech_html}</div></div>
</div>"""


def course_page(c: dict, all_courses: list[dict], resources: dict, lectures: dict) -> str:
    idx = all_courses.index(c)
    prev_c = all_courses[idx - 1] if idx > 0 else None
    next_c = all_courses[idx + 1] if idx < len(all_courses) - 1 else None

    related = []
    for rid in c.get("related", [])[:3]:
        found = next((x for x in all_courses if x["id"] == rid), None)
        if found:
            related.append(found)
    if not related:
        related = [x for x in all_courses if x["cat"] == c["cat"] and x["id"] != c["id"]][:3]

    related_html = "".join(
        f'<a class="relcard" href="{x["slug"]}.html"><span>{esc(x["id"])}</span><b>{esc(x["zh"])}</b></a>'
        for x in related
    )

    topics = c.get("topics", [])
    if topics:
        topics_html = '<ol class="topic-list">' + "".join(f"<li>{md(t)}</li>" for t in topics) + "</ol>"
    else:
        topics_html = '<p class="muted">本页为延伸课程速览，主要内容见下方官方描述。</p>'

    note = c.get("note", "")
    note_html = f'<p class="note-inline">{esc(note)}</p>' if note else ""

    prereq = c.get("prereq") or "见官方描述"
    assessment = c.get("assessment") or "以当季官网为准"
    who = c.get("who") or f"对「{c['one']}」感兴趣的人"
    tips = c.get("tips") or "先读官方描述和课程官网，再决定是否投入。"
    pos = c.get("pos") or c.get("description", "")

    pager = ""
    if prev_c:
        pager += f'<a class="pager prev" href="{prev_c["slug"]}.html"><small>上一门</small><b>{esc(prev_c["id"])} · {esc(prev_c["zh"])}</b></a>'
    if next_c:
        pager += f'<a class="pager next" href="{next_c["slug"]}.html"><small>下一门</small><b>{esc(next_c["id"])} · {esc(next_c["zh"])}</b></a>'

    badge = "核心课程" if c["type"] == "core" else "延伸课程"
    body = f"""<div class="wrap">
  <a class="back" href="../index.html#courses">← 返回课程地图</a>

  <section class="course-hero">
    <div class="course-poster">
      <span class="cp-kicker">Stanford · 2026—27</span>
      <span class="cp-code">{esc(c['id'])}</span>
      <span class="cp-cat">{esc(c['cat'])}</span>
      <span class="cp-stars">{stars(c.get('difficulty'))}</span>
    </div>
    <div class="course-head">
      <p class="kicker">{badge} · {esc(c['cat'])}</p>
      <h1>{esc(c['zh'])}</h1>
      <p class="course-en">{esc(c['title'])}</p>
      <p class="course-one">{esc(c['one'])}</p>
      <div class="meta-chips">
        <span>{esc(c['units'])} 学分</span>
        <span>{esc(c['terms'])}</span>
        <span>{esc(c['grading'])}</span>
        <span>{stars(c.get('difficulty'))}</span>
      </div>
      <div class="tagrow">{''.join(f'<span>{esc(t)}</span>' for t in c.get('tags', []))}</div>
      {note_html}
    </div>
  </section>

  <div class="course-layout">
    <article class="course-main">
      <section class="prose">
        <h2>课程定位</h2>
        <p>{esc(pos)}</p>
      </section>

      <section class="prose">
        <h2>主要内容</h2>
        {topics_html}
      </section>

      {lecture_section(c, lectures)}

      <section class="prose two">
        <div><h2>先修</h2><p>{esc(prereq)}</p></div>
        <div><h2>考核与工作量</h2><p>{esc(assessment)}</p></div>
      </section>

      <section class="prose two">
        <div><h2>适合谁</h2><p>{esc(who)}</p></div>
        <div><h2>学习建议</h2><p>{esc(tips)}</p></div>
      </section>

      <section class="prose">
        <h2>相关课程</h2>
        <div class="related-grid">{related_html}</div>
      </section>

      <section class="prose">
        <details class="official">
          <summary>官方课程描述（英文原文）</summary>
          <p>{esc(c.get('description', ''))}</p>
        </details>
      </section>
    </article>

    <aside class="course-aside">
      <div class="aside-card">
        <div class="aside-head"><h3>快速档案</h3></div>
        <dl class="facts">
          <div><dt>课程编号</dt><dd>{esc(c['id'])}</dd></div>
          <div><dt>学期</dt><dd>{esc(c['terms'])}</dd></div>
          <div><dt>学分</dt><dd>{esc(c['units'])}</dd></div>
          <div><dt>评分</dt><dd>{esc(c['grading'])}</dd></div>
          <div><dt>授课</dt><dd>{esc(c['instructors'])}</dd></div>
          <div><dt>难度</dt><dd>{stars(c.get('difficulty'))}</dd></div>
        </dl>
      </div>
      {resource_block(c, resources, lectures)}
      {f'<div class="aside-card"><div class="aside-head"><h3>Markdown</h3></div><a class="res" href="https://github.com/logic77lhl/stanford-ai-courses/blob/main/courses/{esc(c["slug"])}.md" target="_blank" rel="noopener"><span>在 GitHub 查看课程速览</span><b>↗</b></a></div>' if c['type'] == 'core' else ''}
    </aside>
  </div>

  <div class="pagerrow">{pager}</div>
</div>"""
    return shell(f"{c['id']} · {c['zh']} | Stanford AI 课程地图", c["one"], body, base="../", active="courses")


def bili_card(c: dict, lectures: dict) -> str:
    links = lectures.get(c["id"], {}).get("bilibili", [])
    if not links:
        return ""
    label, url = links[0]
    return f"""<a class="bili-card" href="courses/{c['slug']}.html">
  <span class="bili-code">{esc(c['id'])}</span>
  <b>{esc(c['zh'])}</b>
  <p>{esc(label)}</p>
  <span class="bili-go">课程页 · B站链接 →</span>
</a>"""


def index_page(courses: list[dict], resources: dict, lectures: dict) -> str:
    core = [c for c in courses if c["type"] == "core"]
    ext = [c for c in courses if c["type"] == "ext"]
    featured = [next(c for c in courses if c["id"] == fid) for fid in FEATURED if any(x["id"] == fid for x in courses)]

    tracks = "".join(track_card(cat, i + 1, courses) for i, cat in enumerate(CATEGORY_ORDER))
    posters = "".join(poster_card(c) for c in featured)

    paths_html = "".join(
        f"""<article class="path-card">
  <div class="path-head"><h3>{esc(p['name'])}</h3><span>{esc(p['short'])}</span></div>
  <p>{esc(p['desc'])}</p>
  <div class="path-steps">{''.join(f'<span>{esc(s)}</span>' for s in p['steps'])}</div>
</article>"""
        for p in PATHS
    )

    bili_courses = [c for c in courses if lectures.get(c["id"], {}).get("bilibili")]
    bili_html = "".join(bili_card(c, lectures) for c in bili_courses[:8])

    body = f"""<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <p class="kicker">Stanford University · 2026—27</p>
      <h1>AI / ML / Agent<br><em>课程地图</em></h1>
      <p class="hero-lede">把 Stanford 分散在 CS、EE、STATS、MS&amp;E、CME、AA、PSYCH、SymSys 的 AI 课程，整理成一张可浏览的地图。{len(core)} 门核心课深度速览，{len(ext)} 门延伸课，6 条学习路径。</p>
      <div class="hero-actions">
        <a class="btn gold" href="#courses">浏览全部课程</a>
        <a class="btn" href="paths.html">按学习路径看</a>
      </div>
    </div>
    <div class="hero-side">
      <div class="hero-mark">2026</div>
      <p>“选课不是集邮。<br>先看地图，再选路径。”</p>
    </div>
  </div>
  <div class="wrap">
    <div class="stats">
      <div class="stat gold"><b>{len(core)}</b><span>核心课程</span></div>
      <div class="stat"><b>{len(ext)}</b><span>延伸课程</span></div>
      <div class="stat"><b>{len(CATEGORY_ORDER)}</b><span>方向</span></div>
      <div class="stat"><b>{len(PATHS)}</b><span>学习路径</span></div>
      <div class="stat"><b>{len(courses)}</b><span>课程总数</span></div>
      <div class="stat"><b>26—27</b><span>学年</span></div>
    </div>
  </div>
</section>

<section class="section" id="map">
  <div class="wrap">
    <div class="section-head"><h2>课程地图</h2><small>8 个方向</small><span class="line"></span><a href="#courses">查看全部 →</a></div>
    <div class="track-grid">{tracks}</div>
  </div>
</section>

<section class="section" id="featured">
  <div class="wrap">
    <div class="section-head"><h2>旗舰课程</h2><small>如果只挑几门</small><span class="line"></span></div>
    <div class="poster-grid">{posters}</div>
  </div>
</section>

<section class="section" id="courses">
  <div class="wrap">
    <div class="section-head"><h2>全部课程</h2><small>搜索 / 筛选 / 排序</small><span class="line"></span><span class="count" id="courseCount"></span></div>
    <div class="toolbar">
      <input type="search" id="courseSearch" placeholder="搜课程编号、名称、标签…" autocomplete="off">
      <div class="seg" id="typeSeg">
        <button class="on" data-type="all">全部</button>
        <button data-type="core">核心</button>
        <button data-type="ext">延伸</button>
      </div>
      <select id="courseSort" aria-label="排序">
        <option value="code">按课程编号</option>
        <option value="diff">按难度</option>
        <option value="name">按名称</option>
      </select>
    </div>
    <div class="chips" id="catChips">
      <button class="chip on" data-cat="all">全部方向</button>
      {''.join(f'<button class="chip" data-cat="{esc(cat)}">{esc(cat)}</button>' for cat in CATEGORY_ORDER)}
    </div>
    <div class="course-grid" id="courseGrid"></div>
    <p class="empty" id="courseEmpty" hidden>没有匹配的课程。</p>
  </div>
</section>

<section class="section" id="paths">
  <div class="wrap">
    <div class="section-head"><h2>学习路径</h2><small>按目标选，不按热度选</small><span class="line"></span><a href="paths.html">展开 →</a></div>
    <div class="path-grid">{paths_html}</div>
  </div>
</section>

<section class="section" id="bilibili">
  <div class="wrap">
    <div class="section-head"><h2>B站资源</h2><small>第三方搬运 · 可能失效</small><span class="line"></span><a href="bilibili.html">全部 →</a></div>
    <div class="bili-grid">{bili_html}</div>
  </div>
</section>

<section class="section about" id="about">
  <div class="wrap about-grid">
    <div>
      <p class="kicker">About</p>
      <h2>这张地图怎么用</h2>
      <p>先看方向，再选路径，最后点进课程页。每门核心课有定位、主要内容、课程大纲/课件、先修、考核、适合谁、学习建议和资源入口；延伸课保留官方档案与链接。</p>
    </div>
    <div class="about-note">
      <p><b>信息基准</b>：2026–27 学年，课程数据来自 Stanford ExploreCourses 与课程官网。</p>
      <p><b>非官方</b>：难度、建议、适合谁是整理者判断，选课以官方为准。</p>
      <p><b>更新</b>：修改 <code>data/</code> 后运行 <code>python scripts/build_site.py</code>。</p>
    </div>
  </div>
</section>"""
    return shell("Stanford AI / ML / Agent 课程地图", "Stanford 2026–27 AI/ML/Agent 课程地图：55 门核心课深度速览、70 门延伸课、6 条学习路径。", body, active="map", extra_scripts='<script src="assets/courses.js"></script>')


def paths_page(courses: list[dict]) -> str:
    by_id = {c["id"]: c for c in courses}
    blocks = []
    for i, p in enumerate(PATHS, 1):
        steps = "".join(
            f'<a class="step" href="courses/{by_id[sid]["slug"]}.html"><span>{n:02d}</span><b>{esc(sid)}</b><small>{esc(by_id[sid]["zh"])}</small></a>'
            for n, sid in enumerate(p["steps"], 1) if sid in by_id
        )
        also = "".join(
            f'<a class="also" href="courses/{by_id[sid]["slug"]}.html">{esc(sid)}</a>'
            for sid in p["also"] if sid in by_id
        )
        blocks.append(f"""<section class="path-detail">
  <div class="path-detail-head">
    <span class="path-index">{i:02d}</span>
    <div><h2>{esc(p['name'])}</h2><p>{esc(p['desc'])}</p></div>
  </div>
  <div class="steps">{steps}</div>
  <div class="also-row"><span>还可以搭配</span>{also}</div>
</section>""")

    body = f"""<div class="wrap">
  <a class="back" href="index.html">← 返回首页</a>
  <section class="page-hero">
    <p class="kicker">Learning Paths</p>
    <h1>六条学习路径</h1>
    <p>按目标而不是按课程编号选课。每条路径给出核心序列和可搭配课程；先修关系与避坑说明见 <a href="https://github.com/logic77lhl/stanford-ai-courses/blob/main/docs/learning-paths.md" target="_blank" rel="noopener">learning-paths.md</a>。</p>
  </section>
  {''.join(blocks)}
</div>"""
    return shell("学习路径 | Stanford AI 课程地图", "六条 Stanford AI/ML/Agent 学习路径：LLM/Agent、ML 研究、CV/生成、机器人、MLSys、AI4Science。", body, active="paths")


def bilibili_page(courses: list[dict], lectures: dict) -> str:
    groups = []
    for cat in CATEGORY_ORDER:
        items = [c for c in courses if c["cat"] == cat and lectures.get(c["id"], {}).get("bilibili")]
        if not items:
            continue
        cards = []
        for c in items:
            links = "".join(
                f'<a class="bili-link" href="{esc(url)}" target="_blank" rel="noopener">{esc(label)} ↗</a>'
                for label, url in lectures[c["id"]]["bilibili"]
            )
            cards.append(
                f'<div class="bili-item"><div><span class="bili-code">{esc(c["id"])}</span>'
                f'<a class="bili-title" href="courses/{c["slug"]}.html">{esc(c["zh"])}</a></div>'
                f'<div class="bili-links">{links}</div></div>'
            )
        groups.append(f'<section class="bili-group"><h2>{esc(cat)}</h2>{ "".join(cards) }</section>')

    body = f"""<div class="wrap">
  <a class="back" href="index.html">← 返回首页</a>
  <section class="page-hero">
    <p class="kicker">Bilibili</p>
    <h1>B站课程资源</h1>
    <p>这里汇总 B 站上可找到的 Stanford AI/ML 课程搬运与中配版本。<b>均为第三方上传</b>，可能失效、缺集或与最新版本不一致；优先看官方课程站和 Stanford Online 的 YouTube 录像。</p>
  </section>
  {''.join(groups)}
</div>"""
    return shell("B站资源 | Stanford AI 课程地图", "Stanford AI/ML/Agent 课程的 B 站搬运与中配资源汇总。", body, active="bili")


def not_found() -> str:
    body = """<div class="wrap"><section class="page-hero"><p class="kicker">404</p><h1>这门课不在地图上</h1><p>链接可能变了。回到 <a href="index.html">课程地图</a> 重新找。</p></section></div>"""
    return shell("404 | Stanford AI 课程地图", "页面不存在", body)


def main() -> None:
    courses, resources, _ = load_site_data()
    lectures_path = ROOT / "data" / "lectures.json"
    lectures = load_json(lectures_path) if lectures_path.exists() else {}
    COURSES_OUT.mkdir(parents=True, exist_ok=True)
    ASSETS.mkdir(parents=True, exist_ok=True)

    for stale in COURSES_OUT.glob("*.html"):
        stale.unlink()

    for c in courses:
        (COURSES_OUT / f"{c['slug']}.html").write_text(course_page(c, courses, resources, lectures), encoding="utf-8", newline="\n")

    (SITE / "index.html").write_text(index_page(courses, resources, lectures), encoding="utf-8", newline="\n")
    (SITE / "paths.html").write_text(paths_page(courses), encoding="utf-8", newline="\n")
    (SITE / "bilibili.html").write_text(bilibili_page(courses, lectures), encoding="utf-8", newline="\n")
    (SITE / "404.html").write_text(not_found(), encoding="utf-8", newline="\n")
    (SITE / ".nojekyll").write_text("", encoding="utf-8", newline="\n")

    site_data = [{
        "id": c["id"], "slug": c["slug"], "zh": c["zh"], "cat": c["cat"], "type": c["type"],
        "one": c["one"], "card_desc": c.get("card_desc", c["one"]), "tags": c.get("tags", []), "difficulty": c.get("difficulty"),
        "terms": c["terms"], "units": c["units"], "search": c["search"],
    } for c in courses]
    (ASSETS / "courses.js").write_text(
        "window.COURSES = " + json.dumps(site_data, ensure_ascii=False) + ";\n",
        encoding="utf-8", newline="\n",
    )

    print(f"built {len(courses)} course pages")
    print(f"site: {SITE}")


if __name__ == "__main__":
    main()
