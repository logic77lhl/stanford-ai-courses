# 高校课程地图 · AI 复现手册（Playbook）

> 目标：把这份文档 + 一段项目 Brief 交给 AI（Claude Code / OpenCode / Codex / Cursor 均可），让它在一台干净机器上复现一个同构的「课程地图」站点。
>
> 本文档以 `stanford-ai-courses` 为参考实现，但所有学校名、课程名、分类、配色都可替换。

---

## 0. 这份文档怎么用

有三种用法，按你的投入程度选：

| 用法 | 做法 | 适合 |
|---|---|---|
| **A. 一把梭** | 填好第 1 节的 Brief，连同第 11 节的 Master Prompt 一起发给 AI | 想快速看到成品 |
| **B. 分阶段** | 按第 3 节的 Phase 0–7 逐段推进，每段验收后再继续 | 想要质量可控 |
| **C. 只抄骨架** | 只读第 4 节数据契约 + 第 5 节信息架构，自己写生成器 | 有开发经验，只想复用设计 |

**最关键的一句话**：这类项目不是「让 AI 写 125 个 HTML 页面」，而是「让 AI 建一条数据 → 页面 → 校验的流水线」。只要数据契约和验收标准写清楚，复现就稳定；否则 AI 会产出一堆风格不一致、链接靠编的页面。

---

## 1. 项目 Brief（先填这张表）

把下面这段复制出来，替换尖括号内容。**这是唯一需要你手写的东西**。

```yaml
project:
  name: "<项目名，例如：MIT AI 课程地图>"
  institution: "<学校，例如：MIT>"
  domain: "<领域，例如：AI / ML / Agent>"
  scope: "<范围，例如：EECS 与 Sloan 的 AI 相关课程>"
  academic_year: "<学年，例如：2026–27>"
  language: "zh-CN"            # 站点主语言
  keep_english: true           # 是否保留官方英文描述

scale:
  core_courses: 55             # 完整详情页
  extended_courses: 70         # 精简档案页
  lecture_outlines: 27         # 有逐讲大纲的课程数
  bilibili_courses: 15         # 有第三方视频的课程数

data_sources:
  catalog: "<课程目录 URL，例如 ExploreCourses>"
  official_sites: "<课程官网的查找方式>"
  video: "<B站 / YouTube / OCW 等>"

output:
  site: "github-pages"         # github-pages | vercel | netlify | local
  repo: "<owner/repo>"
  base_path: "/<repo>/"        # 用户主页仓库设为 "/"
  visual_style: "dark-cinema"  # dark-cinema | clean-light | editorial
  pages:
    - index
    - paths
    - semester
    - prereqs
    - bilibili
    - course
    - "404"
```

填完后，用一句话回答这 5 个问题，AI 会少问很多：

1. **读者是谁？** 本校选课学生 / 自学者 / 转专业的人 / 招生宣传？
2. **最重要的动作是什么？** 找一门课 / 按方向选课 / 按学期排课 / 看先修顺序？
3. **内容深度到哪？** 只要官方档案，还是要中文定位、考核、避坑建议？
4. **视频资源收不收？** 收的话，是否接受第三方搬运并标注风险？
5. **你愿意维护到什么程度？** 一学期更新一次 / 每月 / 想自动巡检？

---

## 2. 系统全貌

```text
ExploreCourses / 官网 / 视频站
        │
        ▼
data/catalog.json            原始课程目录（机械抓取，可重复）
        │
        ├── data/courses/*.json      55 门核心课（人工/AI 精修）
        ├── data/more_courses.json   70 门延伸课（轻量）
        ├── data/lectures/*.json     27 门逐讲大纲 + 课件 + B站
        ├── data/resources.json      视频 / 代码 / 工具
        ├── data/prereqs.json        先修关系图
        └── data/search_aliases.json 搜索术语别名
        │
        ▼
scripts/build.py             → courses/*.md + data/courses.json + README 表格
scripts/build_site.py        → docs/*.html + docs/assets/courses.js
scripts/check.py             → 页面数 / 站内链接 / README 链接 / 数据完整性
        │
        ▼
GitHub Actions（重建 + 校验 + 提交一致性） → GitHub Pages
```

**三条设计原则：**

1. **数据与模板分离**：改内容只动 `data/`，不动 HTML。
2. **目录与策展分离**：`catalog.json` 是机械结果；核心课的精修内容单独存放，避免抓取覆盖人工成果。
3. **每次生成都可校验**：页面数量、链接、数据条数都硬编码进 `check.py`，防止「看起来生成了，其实少了一半」。

---

## 3. 分阶段执行（AI 按这个顺序做）

### Phase 0 · 立项与边界（30 分钟）

**产物**：`BRIEF.md`（第 1 节内容）+ 一张课程分类表。

**要做**：
- 确定 6–8 个方向分类（参考：基础核心 / LLM 与 Agent / 系统与硬件 / 视觉与生成 / 机器人与具身 / AI4Science 与医疗 / 产品伦理 / 统计与优化）。
- 确定「核心」和「延伸」的判定标准。
- 确定不收录什么（纯编程入门、纯数学、纯政策等）。

**验收**：每个分类能说出 3 门代表课；核心课数量在 30–80 之间（太少不值得做站，太多写不完）。

---

### Phase 1 · 抓课程目录（1–2 小时）

**产物**：`data/catalog.json`、`data/raw/`（缓存，不进仓库）。

**要做**：
- 找到目录的稳定入口（Stanford 用 ExploreCourses 的 subject 页面）。
- 抓取字段：`subject, code, title, description, grading, units_min, units_max, terms, instructors, instructors_pi, course_id, id, slug`。
- 按 subject 分批抓，带 1–2 秒延迟，缓存原始 HTML/JSON。
- 统一 `id` 格式：`"CS 229"`（学科 + 空格 + 编号）。

**验收**：
- 条目数 > 1000（Stanford 参考值 1904）。
- 每门课都有 `title`、`description`、`terms`。
- 重复运行结果一致（幂等）。

**常见错误**：把 `&` 直接塞进 slug（`MS&E` → `ms-and-e`）。正确做法是先删 `&` 再 slugify → `mse-319`。

---

### Phase 2 · 核心课数据（最花时间，2–5 天）

**产物**：`data/courses/01-foundations.json` … `08-stats.json`，共 55 门。

**做法**：
- 按分类分文件，每文件 5–10 门，方便 review。
- 每门课先填「硬信息」（编号、学期、学分、教师），再写「判断信息」（难度、定位、适合谁、建议）。
- 一次只写一个分类，写完让 AI 自查字段完整性。

**验收**：每门课至少包含第 4.2 节的全部必填字段；`one` ≤ 60 字；`topics` 5–8 条。

---

### Phase 3 · Markdown 与 README（半天）

**产物**：`courses/*.md`、`data/courses.json`、README 课程总表。

**要做**：
- `build.py` 读核心课数据，生成每门课的 Markdown 速览。
- 同时生成机器可读的 `data/courses.json`（供站点使用）。
- README 表格用 `<!-- BEGIN:COURSE_TABLE -->` 标记包裹，方便重复生成。

**验收**：55 个 `.md`；每篇都有固定小节（课程定位 / 主要内容 / 考核与工作量 / 适合谁 / 学习建议 / 相关课程 / 资源）；README 表格链接全部可点。

---

### Phase 4 · 站点生成（1–2 天）

**产物**：`docs/index.html`、`docs/courses/*.html`、`docs/assets/{style.css,app.js,courses.js}`。

**要做**：
- 先写 `shell()`（head / header / footer），保证所有页面共享骨架。
- 再写页面函数：`index_page`、`course_page`、`paths_page`、`semester_page`、`prereqs_page`、`bilibili_page`、`not_found`。
- 课程卡片由 `courses.js` + `app.js` 客户端渲染，支持搜索/筛选/排序。
- 首页只放 8 门旗舰课，不要把所有课程堆在首屏。

**验收**：
- 125 个课程页（55 + 70）。
- 首页卡片数 = 课程总数。
- 搜索能命中课程编号、名称、标签、讲次术语。
- 移动端 390px 无横向滚动。

---

### Phase 5 · 逐讲与资源（1–3 天，可增量）

**产物**：`data/lectures/*.json`、`data/resources.json`、`data/search_aliases.json`、`data/prereqs.json`。

**要做**：
- 只给旗舰课做逐讲大纲，不要 125 门全做。
- 每门课一个 JSON，字段见 4.4。
- 官方有 slides 就直链；只在 Canvas 的就只写 schedule，不伪造 PDF。
- B站/YouTube 链接必须逐条核验，标注「第三方、可能失效」。
- 先修图用手工边表，不要假装从目录里能抓到完整先修。

**验收**：每门有逐讲的课 ≥ 8 讲；所有外链可访问（或明确标注需登录）；B站链接有失效报告入口。

---

### Phase 6 · 校验与 CI（半天）

**产物**：`scripts/check.py`、`.github/workflows/build.yml`、`.github/workflows/bilibili.yml`。

**要做**：
- `check.py` 硬校验：课程页数量、每个页面内部链接、README 相对链接、数据文件数量。
- CI 顺序固定：`build.py → build_site.py → check.py → git diff --exit-code`。
- 第三方链接单独一个 weekly workflow，失败只报警不阻塞主站。

**验收**：本地 `errors: 0`；CI 绿色；故意改坏一个链接时 `check.py` 必须报错。

---

### Phase 7 · 部署与验收（半天）

**产物**：线上站点 + README 预览图 + 仓库 topics/homepage。

**要做**：
- GitHub Pages 从 `main` 的 `/docs` 部署。
- 用 Playwright 做线上冒烟：首页卡片数、课程页逐讲行数、B站链接数、console 无报错。
- README 加线上地址、预览图、构建命令。

**验收**：第 8 节的 Definition of Done 全部通过。

---

## 4. 数据契约（AI 必须严格遵守）

### 4.1 `data/catalog.json`

数组，每项：

```json
{
  "subject": "CS",
  "code": "229",
  "title": "Machine Learning",
  "description": "This course provides a broad introduction...",
  "grading": "Letter or Credit/No Credit",
  "units_min": "3",
  "units_max": "4",
  "terms": ["2026-2027 Winter", "2026-2027 Spring"],
  "instructors": ["Ng, A."],
  "instructors_pi": ["Ng, A."],
  "course_id": "104746",
  "id": "CS 229",
  "slug": "cs-229"
}
```

规则：
- `terms` 用固定英文枚举：`2026-2027 Autumn|Winter|Spring|Summer`。
- `units_min/max` 用字符串，避免 `3.0` 与 `3` 混用。
- `id` 全局唯一；跨院系同编号课程加后缀（如 `CS 229M`）。

### 4.2 `data/courses/*.json`（核心课，最重要）

```json
{
  "id": "CS 229",
  "slug": "cs229-machine-learning",
  "zh": "机器学习",
  "cat": "基础核心",
  "difficulty": 4,
  "one": "一门把监督学习、无监督学习、学习理论和 RL 串起来的 ML 总课。",
  "pos": "CS 229 是 Stanford ML 方向的地基课……",
  "topics": [
    "**监督学习**：线性/逻辑回归、GLM、SVM、树集成",
    "**无监督学习**：k-means、GMM、EM、PCA、ICA",
    "**学习理论**：偏差-方差、正则化、模型选择",
    "**强化学习**：MDP、值迭代、Q-learning、策略搜索"
  ],
  "prereq": "概率、线性代数、多元微积分；编程能力至少 CS 106B。",
  "assess": "5 次作业 + 期中 + 期末 + 一个开放项目；workload 偏重。",
  "who": "想系统补 ML 基础、准备读博或做 ML 工程的人。",
  "tips": "先补 CS 109 和线代；作业不要只看答案，推导要自己写一遍。",
  "tags": ["ML", "监督学习", "无监督学习", "RL"],
  "links": [["课程官网", "https://cs229.stanford.edu/"]],
  "related": ["CS 230", "CS 229M", "CS 234"],
  "note": ""
}
```

字段规则：

| 字段 | 必填 | 类型 | 约束 |
|---|---|---|---|
| `id` | 是 | string | 必须存在于 catalog |
| `slug` | 是 | string | 小写、连字符、全局唯一 |
| `zh` | 是 | string | 中文课程名，≤ 20 字 |
| `cat` | 是 | string | 必须在分类表里 |
| `difficulty` | 是 | int 1–5 | 见 6.3 rubric |
| `one` | 是 | string | 一句话定位，≤ 60 字 |
| `pos` | 是 | string | 100–200 字，讲清在课程体系里的位置 |
| `topics` | 是 | string[] | 5–8 条，可用 `**粗体**` |
| `prereq` | 是 | string | 具体到课号；不确定写「见官方」 |
| `assess` | 是 | string | 作业/考试/项目/工作量 |
| `who` | 是 | string | 适合谁，不要写「所有人」 |
| `tips` | 是 | string | 可执行的建议，不要空话 |
| `tags` | 是 | string[] | 2–4 个 |
| `links` | 是 | [label,url][] | 只放官方链接 |
| `related` | 否 | string[] | 2–3 个课号 |
| `note` | 否 | string | 未排课、改名、跨院系说明 |

### 4.3 `data/more_courses.json`（延伸课）

```json
{
  "id": "CS 525",
  "tag": "Data for AI",
  "cat": "AI for Science 与医疗",
  "zh_one": "训练数据的筛选、去重、合成、归因与版权。"
}
```

规则：`id` 必须在 catalog；`tag` 是中文短标签；`zh_one` 是一句话，不要复制英文描述。

### 4.4 `data/lectures/*.json`（逐讲，一门课一个文件）

```json
{
  "CS 229": {
    "schedule": ["课程 syllabus", "https://cs229.stanford.edu/"],
    "slides": [
      ["Lecture Notes（官方 PDF）", "https://cs229.stanford.edu/main_notes.pdf"]
    ],
    "lectures": [
      { "n": 1, "title": "Introduction and Basic Concepts" },
      { "n": 2, "title": "Supervised Learning Setup; Linear Regression" }
    ],
    "bilibili": [
      ["2026 春 · 中英双语（第三方）", "https://www.bilibili.com/video/BV..."]
    ],
    "note": "以 Fall 2018 公开 syllabus 整理；官方讲义以 main_notes.pdf 为准。"
  }
}
```

规则：
- `schedule` 和 `slides` 都是 `[label, url]`。
- `lectures[].n` 从 1 连续编号；标题保留官方英文。
- `bilibili` 必须人工核验，label 里写年份 + 语言 + `（第三方）`。
- `note` 必须说明数据来自哪个学期/版本。

### 4.5 `data/resources.json`

```json
{
  "CS 229": {
    "videos": [["Stanford Online（YouTube）", "https://..." ]],
    "code": [["官方作业仓库", "https://github.com/..."]],
    "extra": [["课程笔记", "https://..."]],
    "tech": ["Python", "NumPy", "PyTorch"]
  }
}
```

### 4.6 `data/prereqs.json`

```json
{
  "note": "粗粒度建议，不是官方先修要求。",
  "levels": [
    { "name": "起点 · 基础", "courses": ["CS 229", "CS 221"] },
    { "name": "核心 ML", "courses": ["CS 230", "CS 231N"] }
  ],
  "edges": [["CS 229", "CS 230"], ["CS 229", "CS 231N"]]
}
```

规则：只放你愿意背书的边；不要为了图好看硬连。

### 4.7 `data/search_aliases.json`

```json
{
  "CS 224R": ["PPO", "SAC", "DQN", "offline RL", "RLHF"],
  "MS&E 319": ["MoE", "KV cache", "quantization"]
}
```

作用：让搜索 `PPO` 能命中 CS 224R，而不是命中 `support` 里的子串。

### 4.8 命名规则

- 课程页 slug：`slugify(f"{id} {title}")`，先删 `&`，再 `[^a-z0-9]+ → -`。
- 逐讲文件名：`slugify(id)`，如 `cs-229.json`、`mse-319.json`。
- 分类文件名：`01-foundations.json` … `08-stats.json`，数字保证顺序。

---

## 5. 站点信息架构

| 页面 | 作用 | 核心区块 |
|---|---|---|
| `index.html` | 入口 | Hero、统计、8 方向地图、8 门旗舰、全部课程（搜索/筛选/排序）、学习路径、B站、About |
| `paths.html` | 按目标选课 | 6 条路径，每条：目标 → 核心序列 → 可搭配 |
| `semester.html` | 按学期选课 | 秋/冬/春/夏 + 未排课，核心/延伸标记 |
| `prereqs.html` | 先修关系 | SVG DAG + 核心课先修原文 |
| `bilibili.html` | 第三方视频 | 按方向分组、失效报告入口、风险提示 |
| `courses/*.html` | 课程详情 | 海报头、定位、主要内容、逐讲大纲、先修/考核、适合谁/建议、相关课程、官方英文描述、侧栏资源 |
| `404.html` | 兜底 | 返回课程地图 |

导航顺序固定：**地图 / 课程 / 路径 / 学期 / 先修 / B站 / 关于**。移动端折叠为菜单。

课程页侧栏固定三块：快速档案、资源（官方入口/视频/代码/延伸阅读/工具）、Markdown 入口（仅核心课）。

---

## 6. 设计系统（dark-cinema）

### 6.1 Design tokens

```css
:root {
  --bg: #09090b;
  --panel: #121216;
  --text: #e9e5dd;
  --muted: #8d94a1;
  --dim: #606774;
  --gold: #d4b176;
  --gold2: #f1d9a7;
  --line: rgba(255,255,255,.08);
  --blue: #8fa6b8;
  --red: #c96b5a;
  --serif: "Noto Serif SC", "Songti SC", serif;
  --sans: -apple-system, "PingFang SC", "Microsoft YaHei", sans-serif;
}
```

### 6.2 版式

- 最大宽度 1240px，左右 padding 26px（移动端 16px）。
- 标题用衬线体，正文用无衬线；数字/课号用衬线体强调。
- 首页 Hero 标题 `clamp(40px, 6vw, 72px)`。
- 卡片圆角 5–6px，边框 1px `--line`，hover 时边框变金色。
- 不使用大面积纯白；暗色底 + 金色点缀 + 蓝色表示第三方/链接。

### 6.3 难度 rubric

| 星级 | 含义 |
|---|---|
| ★☆☆☆☆ | 1 学分讲座 / 无需背景 |
| ★★☆☆☆ | 本科入门，作业轻 |
| ★★★☆☆ | 需要 ML 基础，工作量中等 |
| ★★★★☆ | 研究生核心课，数学/编程要求高 |
| ★★★★★ | 博士级 / 从零造系统 / workload 极大 |

### 6.4 组件清单

- `course-card`：课号、中文名、一句话、学期、难度、标签。
- `poster-card`：旗舰课海报（方向、课号、大标题）。
- `track-card`：8 个方向入口。
- `lecture-table`：`# / 主题` 两列。
- `resgroup`：侧栏资源分组。
- `bili-item`：课程 + 多个视频链接 + 失效报告。
- `term-row`：课号 / 名称 / 核心或延伸。
- `pnode` + `pg-edge`：先修 SVG。

---

## 7. 内容生产规则

### 7.1 来源优先级

1. 当季 ExploreCourses / 官方课程页
2. 官方 syllabus / schedule / slides
3. 官方 GitHub / 教材
4. 往期公开课程页（必须注明学期）
5. 第三方视频（必须注明「第三方、可能失效」）

**绝不**：编造 PDF 链接、把 Canvas 内部链接当公开链接、把往期当当前。

### 7.2 中文一句话公式

`这门课在体系里是什么 + 最有辨识度的内容 + 适合谁`

例：
- CS 336：「从 tokenizer、Transformer、GPU 到 scaling law，把 LLM 从零造一遍。」
- CS 329H：「用 Bradley–Terry、RLHF、DPO 和 bandit，把『人类偏好』变成可优化目标。」

### 7.3 写作语气

- 用陈述句，不用营销词（「顶级」「必学」「神器」）。
- 可以写判断，但要给理由：「workload 大，因为 5 次作业 + 项目」。
- 不确定就写「以当季官网为准」，不要猜。

### 7.4 第三方视频

- label 必须含：年份、语言/配音、`（第三方）`。
- 页面必须有一句风险提示。
- 必须提供失效报告入口（GitHub Issue 预填课程号 + 链接）。

---

## 8. 校验与 CI

### 8.1 `check.py` 必须检查

- 课程页数量 == 核心 + 延伸（参考 125）。
- 每个页面的 `href/src` 相对路径存在。
- README 里所有相对链接存在。
- 每个核心课有对应 Markdown。
- Markdown 含固定小节。
- 逐讲文件数量、总讲数、B站链接数符合预期。
- 未知课程 ID 报错。

### 8.2 GitHub Actions

```yaml
# build.yml
on: [push, pull_request]
steps:
  - checkout
  - setup-python 3.12
  - pip install -r requirements.txt
  - python scripts/build.py
  - python scripts/build_site.py
  - python scripts/check.py
  - git diff --exit-code
```

```yaml
# bilibili.yml（或 video-links.yml）
on:
  schedule: [{ cron: "0 3 * * 1" }]
  workflow_dispatch:
steps:
  - checkout
  - setup-python
  - python scripts/verify_bilibili.py
```

注意：CI runner 的 IP 可能被视频站限流。脚本要把「网络错误/限流」标为 `unknown`，只有明确 `404` 才判死，否则每周都会红。

### 8.3 Definition of Done

- [ ] 首页卡片数 == 课程总数
- [ ] 课程页数 == 核心 + 延伸
- [ ] 所有课程页有标题、一句话、学期、难度
- [ ] 逐讲课 ≥ 8 讲，且讲次连续
- [ ] 外链抽查 20 条全部可访问
- [ ] 移动端 390px 无横向滚动
- [ ] 搜索能命中课号、名称、术语
- [ ] `check.py` 输出 `errors: 0`
- [ ] CI 绿色、Pages 部署成功
- [ ] README 有线上地址和预览图

---

## 9. 常见坑（这个项目踩过的）

| 坑 | 表现 | 解法 |
|---|---|---|
| slug 里的 `&` | `MS&E` 变成 `ms-and-e-319` | 先 `replace("&","")` 再 slugify |
| 学期中英文映射 | 2027 冬 显示成 2027 Spring | 固定枚举映射表，不靠字符串猜 |
| 未排课课程 | 页面空白或 404 | `terms=[]` → 统一显示「2026–27 未排课」+ note |
| 伪造 PPT | 链接 404 | 只链官方；没有就写「slides 在 Canvas」 |
| B站失效 | 页面还在，视频没了 | 每周巡检 + 失效报告 Issue |
| CI 被视频站限流 | 每周 workflow 红 | `unknown` 不算死，只有 404 才失败 |
| PowerShell 中文乱码 | 终端显示 `??`，文件其实正常 | 用 UTF-8 读写，验证用浏览器/Python |
| 页面数写死 | 加课后 check 失败 | 数量校验与数据长度同步更新 |
| API 推送限制 | 大仓库 push 失败 | 分批/用 API 建 tree，或改用 SSH |
| 搜索子串误命中 | 搜 PPO 命中 `support` | 加 `search_aliases` + 相关性排序 |
| 课程跨学期 | 同一门出现在秋和春 | 允许重复，页面注明「可能跨学期开设」 |

---

## 10. 变体：换学校 / 换领域怎么改

### 10.1 换学校

只改三处：
1. `scripts/fetch_catalog.py` 的抓取入口与字段映射。
2. `data/courses/*.json` 的课程内容。
3. 文案里的学校名、学期枚举、部署地址。

信息架构、CSS、校验逻辑可以原样复用。

### 10.2 换领域（不一定是课程）

同一套骨架可以套：
- **论文地图**：`catalog` = arXiv/DBLP，`core` = 50 篇必读，`lectures` = 按主题分组。
- **工具地图**：`catalog` = GitHub topics，`core` = 30 个工具，`resources` = 文档/教程。
- **会议地图**：`catalog` = 会议列表，`core` = 主会/workshop，`paths` = 投稿路线。

把「课程」替换成「条目」，把「逐讲」替换成「章节/主题」，其余不变。

### 10.3 最小可行版（半天）

如果只想先看效果：

1. 只做 20 门核心课，不做延伸课。
2. 跳过逐讲、B站、先修图。
3. 页面只保留：首页 + 课程页 + 404。
4. 先本地 `python -m http.server` 预览，满意后再上 Pages。

MVP 的验收只有三条：卡片能点、课程页有内容、手机能看。

---

## 11. Master Prompt（复制给 AI）

> 使用说明：把第 1 节填好的 Brief 放在本段后面一起发送。建议一次只让它做 Phase 0–2，验收后再继续。

```text
你是一名资深数据工程师 + 前端工程师 + 技术编辑。请为我复现一个「课程地图」静态站点项目。

【输入】
我会在下面附上 PROJECT BRIEF（YAML）和 PLAYBOOK（本对话已提供）。请严格遵守 PLAYBOOK 中的数据契约、页面结构、设计 tokens 和验收标准。

【目标】
在一台干净机器上，从零建立：
1. data/catalog.json（机械抓取的课程目录）
2. data/courses/*.json（核心课精修数据）
3. data/more_courses.json（延伸课）
4. data/lectures/*.json（逐讲大纲，可后补）
5. scripts/build.py、build_site.py、check.py
6. docs/ 静态站点（index / paths / semester / prereqs / bilibili / courses / 404）
7. .github/workflows/build.yml
8. README.md（线上地址、预览图、构建命令）

【硬性规则】
- 不要手写 100+ 个 HTML 页面；所有页面必须由数据生成。
- 不要编造任何 URL。找不到官方资源就留官方入口，并写「以当季官网为准」。
- 第三方视频必须标注「第三方、可能失效」，并提供失效报告入口。
- 每个课程页必须有：标题、英文名、一句话、学期、学分、难度、先修、考核、适合谁、建议、资源。
- 所有相对链接必须能通过 check.py。
- 移动端 390px 不得横向滚动。
- 先完成 Phase 0–2 并让我验收，不要一次做完所有阶段。

【执行顺序】
Phase 0：输出 BRIEF 确认 + 6–8 个分类 + 核心/延伸判定标准。
Phase 1：实现抓取脚本，产出 catalog.json，报告条目数与字段完整率。
Phase 2：按分类生成核心课 JSON，每完成一个分类就停下来让我 review。
Phase 3：实现 build.py，生成 Markdown 与 README 表格。
Phase 4：实现 build_site.py，生成站点与课程页。
Phase 5：补逐讲/资源/先修/搜索别名（可增量）。
Phase 6：实现 check.py 与 CI，确保 errors: 0。
Phase 7：部署说明 + 线上冒烟清单。

【每阶段输出】
- 改了哪些文件
- 运行了哪些命令
- 验收结果（数字，不要只说「完成了」）
- 下一阶段需要我确认的 1–3 个问题

【开始前】
先问我最多 5 个必要问题；如果信息足够，直接开始 Phase 0。

PROJECT BRIEF:
<把第 1 节的 YAML 粘贴在这里>
```

---

## 附录 A · 参考文件树

```text
.
├── README.md
├── PLAYBOOK.md
├── requirements.txt
├── courses/                    # 生成的 Markdown（55）
├── docs/                       # GitHub Pages
│   ├── index.html
│   ├── paths.html
│   ├── semester.html
│   ├── prereqs.html
│   ├── bilibili.html
│   ├── 404.html
│   ├── assets/{style.css,app.js,courses.js,preview.png}
│   └── courses/*.html          # 125
├── data/
│   ├── catalog.json
│   ├── courses.json
│   ├── courses/*.json          # 手写核心课
│   ├── more_courses.json
│   ├── lectures/*.json         # 一门课一个
│   ├── resources.json
│   ├── prereqs.json
│   └── search_aliases.json
└── scripts/
    ├── fetch_catalog.py
    ├── build.py
    ├── build_site.py
    ├── check.py
    └── verify_bilibili.py
```

## 附录 B · 构建命令

```bash
pip install -r requirements.txt
python scripts/fetch_catalog.py
python scripts/build.py
python scripts/build_site.py
python scripts/check.py
```

本地预览：

```bash
python -m http.server 8000 --directory docs
```

## 附录 C · 一页纸检查表

```text
[ ] Brief 填完，5 个问题有答案
[ ] 分类 6–8 个，每类 3 门代表课
[ ] catalog.json 条目 > 1000，字段完整
[ ] 核心课 30–80 门，字段齐全
[ ] 延伸课有中文一句话
[ ] 逐讲课 ≥ 8 讲，讲次连续
[ ] 官方链接可访问，无伪造
[ ] 第三方视频有标注 + 失效报告
[ ] 首页卡片数 == 课程总数
[ ] 课程页数 == 核心 + 延伸
[ ] 搜索命中课号/名称/术语
[ ] 390px 无横向滚动
[ ] check.py errors: 0
[ ] CI 绿色，Pages 成功
[ ] README 有线上地址和预览图
```

---

**最后一句**：这份文档的价值不在「步骤」，而在**数据契约 + 验收标准**。只要这两部分不变，换学校、换领域、换 AI 工具，都能复现出同一水准的项目。

---

## 想扩展到别的领域？

本手册是「课程地图」的完整实现。如果你要做论文、工具、会议、数据集、学者、书单、公司、法规、城市指南等方向，见：

- **[playbooks/README.md](playbooks/README.md)**：10 个领域模板索引 + 20 个具体选题 + 模板选择决策表
- **[playbooks/00-universal-skeleton.md](playbooks/00-universal-skeleton.md)**：跨领域通用数据模型与流水线
- **[playbooks/MASTER-PROMPT.md](playbooks/MASTER-PROMPT.md)**：通用主提示词（支持单模板与组合模板）
