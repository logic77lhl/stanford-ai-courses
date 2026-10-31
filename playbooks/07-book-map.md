# 07 · 书单与阅读路径（Book / Reading Map）

> 把某个主题的书整理成「难度分级 + 先读关系 + 主题路径 + 版本信息」。
>
> 适合：自学路线、课程参考书、团队读书会、领域入门书单。

---

## 与通用骨架的差异

| 维度 | 课程地图 | 书单 |
|---|---|---|
| 主键 | 课号 | ISBN / 书名 + 版次 |
| 时间 | 学期 | 出版年 + 版次 |
| 关系 | 先修 | 先读、同主题、替代 |
| 质量信号 | 难度 | 难度 + 时效性 + 可读性 |
| 最大坑 | 课件权限 | 版本、翻译质量、过时 |

---

## 数据源

| 数据 | 来源 | 备注 |
|---|---|---|
| 元数据 | 出版社 / ISBNdb / Open Library | 书名、作者、版次 |
| 目录 | 出版社 / 豆瓣 | 章节结构 |
| 评价 | 豆瓣 / Goodreads | 只作参考 |
| 电子版 | 作者主页 / 出版社 | 区分免费/付费 |
| 课程采用 | 课程 syllabus | 可选 |

---

## 实体字段

```json
{
  "id": "ISBN:9780262046305",
  "slug": "deep-learning-goodfellow",
  "name": "深度学习",
  "name_en": "Deep Learning",
  "category": "深度学习",
  "summary": "从线性代数到生成模型的系统教材，偏理论。",
  "facets": {
    "authors": ["Ian Goodfellow", "Yoshua Bengio", "Aaron Courville"],
    "year": 2016,
    "edition": "1st",
    "publisher": "MIT Press",
    "pages": 800,
    "difficulty": 4,
    "language": "en/zh",
    "status": "classic-but-dated"
  },
  "tags": ["deep learning", "textbook", "theory"],
  "links": [
    { "label": "出版社", "url": "https://mitpress.mit.edu/...", "type": "official" },
    { "label": "免费在线版", "url": "https://www.deeplearningbook.org/", "type": "free" }
  ],
  "relations": [
    { "type": "prereq", "target": "ISBN:...", "note": "先读线性代数" }
  ],
  "artifacts": [
    { "type": "toc", "label": "目录", "url": "https://...", "access": "public" }
  ],
  "sources": [
    { "label": "出版社", "url": "https://mitpress.mit.edu/...", "retrieved_at": "2026-10-31" }
  ],
  "freshness": {
    "checked_at": "2026-10-31",
    "volatile": ["edition", "price", "availability"]
  }
}
```

**领域必填 facet**：`authors`, `year`, `edition`, `pages`, `difficulty`, `language`。
**领域必填内容**：`why_read`, `prereq`, `toc_summary`, `caveats`, `companion`.

---

## 难度分级

| 星 | 锚点 |
|---|---|
| 1 | 科普，无需背景 |
| 2 | 本科低年级可读 |
| 3 | 需要基础数学/编程 |
| 4 | 研究生教材，推导多 |
| 5 | 参考手册/研究专著 |

---

## 页面结构

| 页面 | 内容 |
|---|---|
| `index` | 主题入口 + 入门/进阶/参考三层 |
| `book detail` | 定位、目录、先修、优缺点、版本、配套 |
| `reading-path` | 从入门到研究的 6–10 本顺序 |
| `compare` | 同主题 3 本书对比 |
| `topic` | 单主题书单 |

---

## 关键判断规则

1. **版次必须写**：同一本书 1st/2nd 内容差很多。
2. **区分原版与翻译**：翻译质量、术语一致性要提示。
3. **标注时效性**：2016 的 DL 教材在 2026 年仍可读，但缺 LLM。
4. **免费版优先给官方链接**，不要给盗版。
5. **不写「必读」**，写「适合什么阶段」。

---

## 30 分钟 MVP

```text
30 本书
4 个主题
index + book detail + reading-path
无对比、无目录
```

---

## 验收清单

- [ ] 每本书有 ISBN 或唯一标识
- [ ] 版次、年份、页数完整
- [ ] 有官方/出版社链接
- [ ] 难度有锚点理由
- [ ] 阅读路径有顺序理由
- [ ] 不链接盗版

---

## Brief 片段

```yaml
variant: book-map
field: "机器学习 / LLM"
scope: "入门到研究的 40 本书"
scale: { core: 40, extended: 60 }
sources:
  metadata: "出版社 + Open Library"
  reviews: "豆瓣 / Goodreads（仅参考）"
output:
  pages: [index, book, reading-path, topic]
```

---

## 给 AI 的增量指令

```text
按书单模板实现。先做 30 本书的垂直切片：
书目元数据 → items JSON → detail 页 → reading path → check.py。
版次必须写；区分原版/翻译；免费版只链官方；
难度评分要写理由；不要使用「必读」这种绝对词。
```
