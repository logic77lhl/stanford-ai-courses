[中文](README.md) | **English**

# Stanford AI / ML / Agent Course Map

> 2026–27 academic year · 55 core courses · 70 related courses · a Chinese overview for every core course

**Live site**: <https://logic77lhl.github.io/stanford-ai-courses/>

**Full English site**: 125 course pages + paths / semester / prerequisites / Bilibili · [English site](https://logic77lhl.github.io/stanford-ai-courses/en/)

Stanford's AI courses are spread across CS, EE, STATS, MS&E, CME, AA, PSYCH, and SymSys, numbered from CS 25 to CS 528, plus a pile of 1-unit seminars. This repo turns them into a map: **one Markdown overview per core course**, plus a full course table, learning paths, and related courses. `docs/` is a browsable GitHub Pages site.

[![Site preview](docs/assets/preview.png)](https://logic77lhl.github.io/stanford-ai-courses/)

**Who it's for**: Stanford students picking courses; self-taught learners following Stanford's curriculum; anyone who wants the course landscape for one area (LLM/agents, CV, robotics, MLSys, AI4Science) at a glance.

> Want the same structure for another school or field? See **[PLAYBOOK.md](PLAYBOOK.md)** — a reproduction manual you can hand to an AI (data contract, staged workflow, master prompt, acceptance checklist).
>
> For papers, tools, conferences, datasets, reading lists, companies, or regulations, see **[playbooks/](playbooks/README.md)** — 10 domain templates plus a generic skeleton.

---

## Layout

```text
.
├── README.md                 # full table + learning paths + related courses
├── PLAYBOOK.md               # AI-facing reproduction manual
├── playbooks/                # 10 domain templates + skeleton + master prompt
├── courses/                  # 55 core courses, one overview each
├── courses/en/               # English overviews (55 core courses)
├── docs/                     # GitHub Pages site (index + 125 course pages)
├── docs/en/                  # English site (125 course pages + 5 top-level pages)
├── docs/learning-paths.md    # the six learning paths in detail
├── data/
│   ├── courses.json          # machine-readable course data
│   ├── catalog.json          # normalised ExploreCourses dump
│   ├── courses/              # hand-written source data, split by area
│   ├── i18n/                 # English translation layer (ui.en.json / glossary.json / en/*.json)
│   ├── resources.json        # videos / code / tools
│   ├── lectures/             # per-course JSON: lecture outline / slides / Bilibili link
│   ├── prereqs.json          # prerequisite graph
│   └── more_courses.json     # related-course list, one Chinese line each
└── scripts/
    ├── fetch_catalog.py      # pull from ExploreCourses
    ├── build.py              # generate courses/*.md and the README tables
    ├── build_site.py         # generate the docs/ site
    └── verify_bilibili.py    # weekly CI check for dead Bilibili links
```

## How to use it

1. **Start from a learning path** — if you already know your direction, jump to [learning paths](#learning-paths) and pick courses along a route.
2. **Then the master table** — browse by area and open a course page.
3. **Then the course page** — positioning, main content, **lecture outline / slides**, prerequisites, assessment, who it suits, study advice, related courses, resources.

The site also provides:

- **125 course pages** — 55 core + 70 related, filterable by area, core/related, and keyword; keywords also match individual lecture titles (e.g. PPO, AlphaFold).
- **Lecture outlines / slides** — per-lecture topics, official slides and notes, and mirror links for 27 courses.
- **Bilibili resources page** — 15 courses, 23 mirrored or Chinese-dubbed versions, marked "third-party, may break", with a one-click dead-link report.
- **By-quarter page** — the 55 core courses split across Autumn 2026 / Winter 2027 / Spring 2027, plus courses not offered this year.
- **Prerequisite page** — a graph for 27 courses plus the official prerequisite text.

## What's included

- **Time base**: 2026–27, per [Stanford ExploreCourses](https://explorecourses.stanford.edu/).
- **55 core courses**: AI/ML/agents as the core method or core application, with reasonably complete public information.
- **Related courses**: more specialised, more cross-disciplinary, or 1-unit seminars; the site still generates a compact page (official record + entry point).
- **Excluded**: pure programming intro, pure math/statistics foundations, pure policy/ethics (unless tightly coupled to AI technology).
- **Not offered**: some courses aren't scheduled in 2026–27; their pages say so and use the most recent offering.
- **Subjective parts**: difficulty stars, study advice, and "who it suits" are the maintainer's judgement, not official.
- **Third-party video**: Bilibili links are uploads by others; they may break, miss episodes, or lag the current version. Prefer the official course site and Stanford Online.

## Course tables

The full table (course number, title, units, quarter, difficulty, overview link) lives in the Chinese README and on the site. Keeping 125 rows duplicated in two languages would drift; the numbered table in [README.md](README.md) and the filterable site are the single sources.

Browse the site: <https://logic77lhl.github.io/stanford-ai-courses/>

## English edition

The English site is a full mirror: **125 course pages** (55 core + 70 related) plus **paths, semester, prerequisites, and Bilibili** pages. Every Chinese page has a language link to its English counterpart.

- The Chinese notes in `data/courses/*.json` remain the source of truth.
- Core translations live in `data/i18n/en/<slug>.json`; related-course one-liners in `data/i18n/more_courses.en.json`.
- Page copy is in `data/i18n/ui.en.json`, `pages.en.json`, `paths.en.json`, and `prereqs.en.json`.
- Official facts (title, description, units, terms, instructors) are read from `data/catalog.json`, never retyped.
- `scripts/i18n_check.py --strict` fails on missing courses, dropped topic bullets, or Chinese characters leaking into English.
- All English pages are `draft`: structurally checked, awaiting native review.

The full course table is intentionally not duplicated in English — it would drift. Use the Chinese table or the filterable English site.

## Learning paths

Six routes — foundations, LLM/agents, CV, robotics, MLSys, AI4Science — each with an ordered course list and a note on what the route leaves out. Details in [docs/learning-paths.md](docs/learning-paths.md).

## Data and regeneration

```bash
python scripts/fetch_catalog.py     # refresh from ExploreCourses
python scripts/build.py             # regenerate course pages and tables
python scripts/build_site.py        # regenerate docs/
python scripts/build_i18n.py        # build English Markdown + data/courses.en.json
python scripts/build_site_en.py     # regenerate docs/en/
python scripts/i18n_check.py        # validate the translation layer
python scripts/verify_bilibili.py   # check third-party video links
```

CI runs the build and the Bilibili check; a broken link opens a report rather than failing silently.

## Known limits

- Course information reflects the 2026–27 catalogue; schedules change every year.
- Difficulty ratings and study advice are opinions.
- Third-party video links rot; the weekly check only detects "unreachable", not "replaced by a different course".
- Related-course pages are intentionally thin — they exist to be found, not to be complete.

## License

[MIT](LICENSE). Course descriptions, syllabi, and slides belong to Stanford and the respective instructors.
