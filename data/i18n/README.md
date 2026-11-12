# English translation layer

The Chinese notes in `data/courses/*.json` are the source of truth. English
lives here, in one file per course, so translation PRs never touch the Chinese
data and a missing translation is visible instead of silently falling back to
machine output.

## Files

```text
data/i18n/
├── ui.en.json                 # UI strings, category names, section headings
├── pages.en.json              # paths / semester / prereqs / bilibili copy
├── paths.en.json              # six learning paths
├── prereqs.en.json            # prerequisite graph labels
├── more_courses.en.json       # 70 related courses: English tag + one-liner
├── glossary.json              # termbase + things to keep as-is
├── en/
│   ├── cs221-artificial-intelligence.json
│   └── ...                    # 55 core courses
├── queue/                     # local translation packets (gitignored)
└── README.md
```

## One course file

```json
{
  "slug": "cs221-artificial-intelligence",
  "status": "reviewed",
  "updated": "2026-11-12",
  "one": "One-sentence summary.",
  "pos": "Course positioning paragraph.",
  "topics": ["**Bold label**: detail", "..."],
  "prereq": "Prerequisites.",
  "assess": "Assessment and workload.",
  "who": "Who it is for.",
  "tips": "Study advice.",
  "tags": ["AI", "Foundations", "Search", "Probability"]
}
```

`status` is `draft` or `reviewed`. The English index lists both; flip a file to
`reviewed` after a native-language review.

## Rules

- **Official facts come from `data/catalog.json`**, not from translation:
  title, description, units, terms, grading, instructors. Do not retype them.
- **Keep course codes, people, libraries, and acronyms unchanged** — see
  `glossary.json` → `keep_as_is`.
- **Do not invent facts.** If the Chinese says "usually", keep the hedge. If a
  number is not in the source, do not add it.
- **Topic count must match** the Chinese source. `i18n_check.py` fails if a
  bullet is dropped or invented.
- **No Chinese characters in English fields.** The checker rejects CJK text.
- Keep Markdown bold labels (`**...**`) in `topics`; they become `<strong>`.

## Workflow

1. For a new core course, run `python scripts/i18n_packet.py --limit 8`; each
   packet separates `official` (reuse) from `editorial_zh` (translate).
2. For a related course, add its English `tag` and `one` to
   `more_courses.en.json`.
3. Run:
   ```bash
   python scripts/build_i18n.py
   python scripts/i18n_check.py --strict
   python scripts/build_site_en.py
   ```
4. Commit the source JSON **and** the generated `courses/en/*.md`,
   `data/courses.en.json`, and `docs/en/**`.

`python scripts/i18n_check.py --strict` fails if any core or related course is
missing. CI runs it on every change under `data/i18n/`.

## Coverage

Full site: **55 / 55** core courses, **70 / 70** related courses, and 5
top-level pages (index, paths, semester, prerequisites, Bilibili). All English
pages are `draft` (facts checked, awaiting native review).
