# 贡献指南

感谢你愿意完善这份课程地图。所有课程信息都应以官方来源为准。

## 新增一门核心课程

1. 在 `data/courses/` 里找到对应方向的 JSON 文件（没有就新建）。
2. 复制一个现有条目，填写字段：

| 字段 | 说明 |
| --- | --- |
| `id` | 课程编号，必须与 ExploreCourses 一致，如 `CS 229` |
| `slug` | 文件名，建议 `cs229-machine-learning` |
| `zh` | 中文课程名 |
| `cat` | 必须属于 `scripts/build.py` 里的 `CATEGORY_ORDER` |
| `difficulty` | 1–5，主观难度 |
| `one` | 一句话定位，会显示在课程页开头 |
| `pos` | 课程定位，2–4 句 |
| `topics` | 主要内容 bullet，支持 `**加粗**` |
| `prereq` | 先修要求 |
| `assess` | 考核与工作量 |
| `who` | 适合谁 |
| `tips` | 学习建议 |
| `tags` | 标签数组 |
| `links` | `[["课程官网", "https://..."]]`，只放验证过的链接 |
| `related` | 相关课程 ID 数组 |
| `note` | 可选备注，如“2026–27 未排课” |

3. 运行 `python scripts/build.py`，会生成 `courses/<slug>.md` 并更新 README 表格。
4. 提交 `data/courses/*.json`、`courses/*.md`、`README.md`。

## 新增一门延伸课程

在 `data/more_courses.json` 里加 `{ "id": "CS 999", "tag": "方向/备注" }`，然后重新构建。延伸课程只进 README 表格，不生成单独页面。

## 修正信息

- 课程名称、学期、学分、教师：以 ExploreCourses 为准。
- 考核比例、先修：以课程官网当季 syllabus 为准；不确定就写“以当季官网为准”。
- 主观判断（难度、适合谁、建议）允许不同意见，但请在 PR 里说明理由。

## 不要做的事

- 不要直接改 `courses/*.md`（它们是生成文件）。
- 不要提交 `data/raw/`（大文件，已在 `.gitignore`）。
- 不要编造课程官网链接；没有就留空，只放 ExploreCourses。
- 不要大段复制课程官网原文；官方描述会以 `<details>` 引用，正文请用自己的话总结。
