# 00 · 通用骨架（Universal Skeleton）

> 任何「一批条目 + 详情页 + 关系/时间线/对比」的策展型站点，都可以套这份骨架。
>
> 先用它定结构，再用领域模板（01–10）填字段。

---

## 1. 适用与不适用

**适用**：
- 条目数量 30–500，人工可审。
- 每个条目有稳定的身份（课号、DOI、repo、法规号、地点 ID）。
- 用户的核心动作是「找、比、按顺序看」。
- 信息会变，但变化可核验。

**不适用**：
- 实时数据流（股票、天气）——需要后端与推送，不是静态站。
- 用户生成内容为主（论坛、评论）——需要账号、审核、数据库。
- 一条数据就要复杂交互（地图导航、代码运行）——需要专门应用。

---

## 2. 六个核心概念

| 概念 | 作用 | 例子 |
|---|---|---|
| **Item** | 被策展的条目 | 课程、论文、工具、法规 |
| **Facet** | 可比较的属性 | 难度、许可证、截止日期 |
| **Relation** | 条目之间的关系 | 先修、引用、替代、管辖 |
| **Artifact** | 条目关联的外部产物 | 课件、代码、PDF、官网 |
| **Source** | 信息来源与抓取时间 | ExploreCourses、arXiv |
| **Snapshot** | 某一时刻的状态 | 2026 秋课表、2026 榜单 |

**关键**：Item 是主键；Facet 用来排序和筛选；Relation 用来画图；Artifact 用来给用户「下一步」；Source/Snapshot 用来维持可信度。

---

## 3. 目录结构

```text
.
├── README.md
├── BRIEF.md                    # 项目边界与收录标准
├── data/
│   ├── catalog.json            # 机械抓取，可重跑
│   ├── items/                  # 策展数据，按分类分文件
│   │   ├── 01-*.json
│   │   └── ...
│   ├── relations.json          # 关系边表
│   ├── artifacts.json          # 外部产物（可选）
│   ├── aliases.json            # 搜索别名
│   └── snapshots/              # 时间敏感数据快照
├── content/                    # 生成的 Markdown（可选）
├── docs/                       # 静态站点
│   ├── index.html
│   ├── items/*.html
│   ├── graph.html
│   ├── timeline.html
│   ├── compare.html
│   └── assets/{style.css,app.js,items.js}
└── scripts/
    ├── fetch_catalog.py
    ├── build.py
    ├── build_site.py
    └── check.py
```

**原则**：`catalog` 可以随时重抓；`items` 是人工成果，不能被抓取覆盖；`snapshots` 只追加，不修改历史。

---

## 4. 数据契约

### 4.1 Item

```json
{
  "id": "ARXIV:1706.03762",
  "slug": "attention-is-all-you-need",
  "name": "Attention Is All You Need",
  "name_en": "Attention Is All You Need",
  "category": "Transformer",
  "summary": "提出 Transformer，用自注意力替代循环结构。",
  "facets": {
    "year": 2017,
    "venue": "NeurIPS",
    "difficulty": 3,
    "status": "foundational"
  },
  "tags": ["Transformer", "attention", "NLP"],
  "links": [
    { "label": "arXiv", "url": "https://arxiv.org/abs/1706.03762", "type": "official" },
    { "label": "代码", "url": "https://github.com/...", "type": "code" }
  ],
  "relations": [
    { "type": "extends", "target": "ARXIV:1409.0473" }
  ],
  "artifacts": [
    { "type": "pdf", "label": "论文 PDF", "url": "https://...", "access": "public" }
  ],
  "sources": [
    { "label": "arXiv", "url": "https://arxiv.org/abs/1706.03762", "retrieved_at": "2026-10-31" }
  ],
  "freshness": {
    "checked_at": "2026-10-31",
    "volatile": ["citation_count", "code_link"]
  },
  "notes": "引用数会变；以 Semantic Scholar 为准。"
}
```

必填：`id, slug, name, category, summary, facets, tags, links, sources, freshness`。
可选：`name_en, relations, artifacts, notes`。

### 4.2 Relation

```json
{
  "from": "CS 229",
  "to": "CS 230",
  "type": "prereq",
  "strength": "recommended",
  "note": "CS 230 假设已掌握监督学习基础。",
  "source": "https://cs230.stanford.edu/"
}
```

`type` 的取值由领域决定：

| 领域 | 常见 type |
|---|---|
| 课程 | `prereq`, `related`, `cross_listed` |
| 论文 | `cites`, `extends`, `contradicts`, `reproduces` |
| 工具 | `alternative`, `depends_on`, `integrates` |
| 会议 | `same_series`, `co_located`, `sister` |
| 法规 | `amends`, `implements`, `supersedes` |
| 公司 | `competitor`, `supplier`, `customer` |

**规则**：每条边必须有 `source` 或 `note`，否则不画。

### 4.3 Snapshot

时间敏感字段不要直接写在 Item 上，放快照：

```json
{
  "snapshot_id": "2026-10-31",
  "item_id": "NEURIPS-2026",
  "fields": {
    "abstract_deadline": "2026-05-15T23:59:00-12:00",
    "paper_deadline": "2026-05-22T23:59:00-12:00",
    "acceptance_rate": 0.26
  },
  "source": "https://neurips.cc/"
}
```

好处：可以显示「截至 2026-10-31」，也能保留历史。

---

## 5. 页面类型

| 页面 | 必需 | 内容 |
|---|---|---|
| `index.html` | 是 | Hero、统计、分类入口、精选、全部条目（搜索/筛选/排序） |
| `items/*.html` | 是 | 头部、摘要、属性表、关系、外部产物、来源、相关条目 |
| `graph.html` | 可选 | 关系图（SVG/D3），支持按类型过滤 |
| `timeline.html` | 可选 | 按时间排序的条目/事件 |
| `compare.html` | 可选 | 3–5 个条目横向对比 |
| `category.html` | 可选 | 单分类聚合页 |
| `about.html` | 可选 | 方法、来源、免责声明、更新日志 |
| `404.html` | 是 | 返回首页 |

**导航不超过 7 项**：首页 / 全部 / 关系 / 时间线 / 对比 / 关于。

---

## 6. 生成流水线

```text
fetch_catalog.py
  → data/catalog.json
build.py
  → data/items.json（合并）
  → content/*.md（可选）
  → README 表格
build_site.py
  → docs/*.html
  → docs/assets/items.js
check.py
  → 数量 / 链接 / 字段 / 关系完整性
```

### 每步的幂等要求

- 同一份输入，重复运行输出一致。
- 生成文件必须可被 `git diff --exit-code` 检查。
- 删除条目后，旧的详情页必须被清理（构建前删除 `docs/items/*.html`）。

---

## 7. 校验清单（check.py）

```text
[ ] 详情页数量 == Item 数量
[ ] 每个 Item 有 slug 且唯一
[ ] 每个 Item 的 category 在分类表里
[ ] 每个必填 facet 存在
[ ] 每个 relation 的 from/to 都存在
[ ] 每个页面内部链接存在
[ ] README 相对链接存在
[ ] 每个 Item 至少 1 个 source
[ ] 时间敏感字段有 checked_at
[ ] 第三方链接有 access/risk 标记
```

建议把预期数量写成常量，例如：

```python
EXPECTED_ITEMS = 125
EXPECTED_PAGES = 125
```

新增条目时同步更新，强制自己面对「数量变化」。

---

## 8. 时间敏感数据的处理

| 数据 | 易变性 | 策略 |
|---|---|---|
| 课程学期 | 每学年 | 每学期重抓，页面标学年 |
| 论文引用数 | 每天 | 快照 + 「截至日期」 |
| 会议 deadline | 每年 | 存时区 + AoE，过期后归档 |
| 工具 star | 每天 | 快照，不要实时 |
| 数据集榜单 | 每周 | 快照 + 来源链接 |
| 法规状态 | 不定期 | 存生效日期 + 修订号 |
| 营业时间/价格 | 不定期 | 标「最后核验」，提供官方链接 |

**原则**：宁可显示「截至 2026-10-31，可能已变」，也不要假装实时。

---

## 9. 排序与评分

不要用一个模糊的「总分」。至少拆成两个维度：

- **Quality**：内容质量、权威性、维护状态。
- **Fit**：对目标读者的匹配度。

每个维度用 1–5 分，并写锚点：

```text
5 = 领域公认必读/必用，长期维护
4 = 高质量，适合系统学习
3 = 合格，适合特定场景
2 = 有更好替代
1 = 仅作存档
```

页面上显示「为什么是这个分」，而不是只显示星星。

---

## 10. 给 AI 的执行约束

把下面这段附在 Master Prompt 后面：

```text
你必须：
1. 先读通用骨架和领域模板，再动手。
2. 先输出 BRIEF 确认与分类表，等我确认后再抓数据。
3. 先做 20–30 个条目的垂直切片（catalog + items + 3 个页面），验收后再扩。
4. 所有页面由数据生成，不手写 HTML。
5. 不伪造链接；不确定的字段写 null 并注明「待核验」。
6. 每完成一个阶段，报告：改了哪些文件、跑了哪些命令、验收数字。
7. 任何数量变化，同步更新 check.py 的预期值。
```

---

## 11. 最小可信版本（MVP）

```text
20–30 个条目
1 个分类（或 3 个小分类）
3 个页面：index / item detail / 404
无关系图、无时间线、无对比
1 个 check.py：条目数 + 链接
```

MVP 的验收只有三条：

1. 每个条目字段完整。
2. 每个链接可访问。
3. 手机能看。

先做到这三条，再谈「500 条」和「关系图」。
