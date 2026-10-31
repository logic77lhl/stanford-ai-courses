# 02 · 论文地图（Paper Map）

> 把某个方向的核心论文整理成「必读顺序 + 引用关系 + 代码/复现状态 + 主题时间线」。
>
> 适合：研究方向入门、组会 reading list、课程参考书目、技术调研。

---

## 与通用骨架的差异

| 维度 | 课程地图 | 论文地图 |
|---|---|---|
| 主键 | 课号 | DOI / arXiv ID |
| 时间 | 学期 | 发表年份 + 版本 |
| 关系 | 先修 | 引用、扩展、反驳、复现 |
| 质量信号 | 难度 | 引用数 + venue + 复现状态 |
| 最大坑 | 课件权限 | 版本、引用数变化、复现声明 |

---

## 数据源

| 数据 | 来源 | 备注 |
|---|---|---|
| 元数据 | arXiv API / Semantic Scholar / DBLP | 标题、作者、年份、venue |
| 引用关系 | Semantic Scholar / OpenAlex | 只取高置信边 |
| 代码 | Papers with Code / GitHub | 检查是否官方 |
| 复现 | Papers with Code / 论文附录 | 区分「有代码」与「可复现」 |
| 引用数 | Semantic Scholar | 必须存快照日期 |
| 版本 | arXiv versions | v1/v2 可能结论不同 |

---

## 实体字段

```json
{
  "id": "ARXIV:1706.03762",
  "slug": "attention-is-all-you-need",
  "name": "Attention Is All You Need",
  "name_en": "Attention Is All You Need",
  "category": "Transformer",
  "summary": "用自注意力替代循环结构，奠定现代 LLM 的架构基础。",
  "facets": {
    "year": 2017,
    "venue": "NeurIPS",
    "citation_count": 120000,
    "difficulty": 3,
    "reproducibility": "code-available"
  },
  "tags": ["Transformer", "attention", "NLP"],
  "links": [
    { "label": "arXiv", "url": "https://arxiv.org/abs/1706.03762", "type": "official" },
    { "label": "官方代码", "url": "https://github.com/tensorflow/tensor2tensor", "type": "code" }
  ],
  "relations": [
    { "type": "extends", "target": "ARXIV:1409.0473", "note": "用 attention 替代 RNN" }
  ],
  "artifacts": [
    { "type": "pdf", "label": "论文 PDF", "url": "https://arxiv.org/pdf/1706.03762", "access": "public" }
  ],
  "sources": [
    { "label": "arXiv", "url": "https://arxiv.org/abs/1706.03762", "retrieved_at": "2026-10-31" }
  ],
  "freshness": {
    "checked_at": "2026-10-31",
    "volatile": ["citation_count", "code_link", "venue"]
  }
}
```

**领域必填 facet**：`year`, `venue`, `difficulty`, `reproducibility`。
**领域必填内容**：`problem`, `idea`, `why_read`, `caveats`。

---

## 复现状态分级

| 值 | 含义 |
|---|---|
| `official-code` | 作者官方代码 |
| `code-available` | 有第三方实现 |
| `reproduced` | 有独立复现报告 |
| `partial` | 部分复现 |
| `none` | 无公开代码 |

**不要把「有 GitHub 链接」等同于「可复现」。**

---

## 页面结构

| 页面 | 内容 |
|---|---|
| `index` | 主题入口 + 必读 20 篇 + 全部论文 |
| `paper detail` | 问题、核心想法、方法图、实验、局限、代码、相关论文 |
| `timeline` | 按年份的主题演进 |
| `graph` | 引用/扩展关系图（可切换主题） |
| `reading-path` | 从入门到前沿的 5–10 篇顺序 |
| `venue` | 按会议/年份聚合 |

---

## 关键判断规则

### 必读等级

| 等级 | 锚点 |
|---|---|
| S | 开创性工作，绕不开 |
| A | 重要改进/系统总结 |
| B | 特定场景有用 |
| C | 仅存档/历史价值 |

### 阅读难度

| 星 | 锚点 |
|---|---|
| 1 | 综述/博客级 |
| 2 | 有 ML 基础可读 |
| 3 | 需要领域背景 |
| 4 | 数学/系统细节重 |
| 5 | 需要复现才能理解 |

---

## 内容规则

1. 摘要必须写「问题 → 想法 → 结果」，不要复制论文 abstract。
2. 引用数必须带快照日期；不同来源数字可能差很多。
3. 每篇论文最多 3 条「为什么读」，不要写泛泛的「很重要」。
4. 代码链接优先官方；第三方实现要标 `community`。
5. 有争议的结论写进 `caveats`，不要只写优点。

---

## 30 分钟 MVP

```text
30 篇论文
5 个主题
index + paper detail + reading-path
无引用图、无时间线
引用数先留空
```

---

## 验收清单

- [ ] 每篇有 DOI/arXiv ID、年份、venue
- [ ] 每篇有 1 个官方链接
- [ ] 引用数有 `checked_at`
- [ ] 复现状态不是「猜」的
- [ ] reading path 的顺序有理由
- [ ] 引用图每条边有来源

---

## Brief 片段

```yaml
variant: paper-map
field: "LLM agents"
scope: "2017–2026 的核心论文 + 代表性系统"
scale: { core: 60, extended: 140 }
sources:
  metadata: "arXiv + Semantic Scholar"
  code: "Papers with Code + GitHub"
  venue: "NeurIPS / ICML / ICLR / ACL"
output:
  pages: [index, paper, timeline, graph, reading-path]
```

---

## 给 AI 的增量指令

```text
按论文地图模板实现。先做 30 篇核心论文的垂直切片：
arXiv 元数据 → items JSON → 详情页 → reading path → check.py。
引用数必须存快照日期；代码链接区分 official/community；
不要把「有代码」写成「可复现」。关系图只画有来源的边。
```
