# 01 · 课程地图（Course Map）

> 把一个学校/院系的课程整理成「方向地图 + 课程详情 + 学习路径 + 学期/先修视图」。
>
> 完整实现说明见根目录 [PLAYBOOK.md](../PLAYBOOK.md)；本页是可复用的领域配置。

---

## 适用需求

- 本校学生选课、转专业、规划先修顺序。
- 自学者按某校课程体系自学。
- 留学申请者了解某方向课程版图。

---

## 数据源

| 数据 | 来源 | 备注 |
|---|---|---|
| 课程目录 | ExploreCourses / 学校 catalog | 结构化最好 |
| 官方描述 | 课程官网 | 保留英文原文 |
| 学期/学分/教师 | 目录 | 每学年变化 |
| 逐讲大纲 | syllabus / schedule | slides 可能只在 Canvas |
| 先修 | 课程页 / 目录 | 经常写得模糊 |
| 视频 | 官方 YouTube / B站 | 第三方必须标注 |

---

## 实体字段

```json
{
  "id": "CS 229",
  "slug": "cs229-machine-learning",
  "name": "机器学习",
  "name_en": "Machine Learning",
  "category": "基础核心",
  "summary": "把监督学习、无监督学习和 RL 串起来的 ML 总课。",
  "facets": {
    "units": "3–4",
    "terms": ["2026 秋", "2027 冬"],
    "difficulty": 4,
    "grading": "Letter or Credit/No Credit"
  },
  "tags": ["ML", "监督学习", "RL"],
  "links": [
    { "label": "课程官网", "url": "https://cs229.stanford.edu/", "type": "official" }
  ],
  "relations": [
    { "type": "prereq", "target": "CS 230", "note": "建议先学" }
  ],
  "artifacts": [
    { "type": "slides", "label": "Lecture Notes", "url": "https://...", "access": "public" }
  ],
  "sources": [
    { "label": "ExploreCourses", "url": "https://...", "retrieved_at": "2026-10-31" }
  ],
  "freshness": { "checked_at": "2026-10-31", "volatile": ["terms", "instructors"] }
}
```

**领域必填 facet**：`units`, `terms`, `difficulty`, `grading`。
**领域必填内容**：`prereq`, `assessment`, `who`, `tips`。

---

## 页面结构

| 页面 | 内容 |
|---|---|
| `index` | Hero + 统计 + 8 方向 + 8 门旗舰 + 全部课程 + 路径 |
| `course detail` | 海报头、定位、主要内容、逐讲、先修/考核、适合谁/建议、相关课、资源 |
| `paths` | 6 条目标导向路径 |
| `semester` | 秋/冬/春/夏 + 未排课 |
| `prereqs` | SVG 先修图 + 先修原文 |
| `videos` | 第三方视频汇总 + 失效报告 |

---

## 关键判断规则

### 难度

| 星 | 锚点 |
|---|---|
| 1 | 1 学分讲座，无背景要求 |
| 2 | 本科入门，作业轻 |
| 3 | 需要 ML 基础，工作量中等 |
| 4 | 研究生核心，数学/编程要求高 |
| 5 | 博士级 / 从零造系统 / workload 极大 |

### 核心 vs 延伸

- **核心**：讲核心方法，或某个方向的入口课；有相对完整的公开信息。
- **延伸**：专题、交叉、seminar、1 学分；只保留官方档案与入口。

### 学期

- 用固定枚举：`2026 秋 / 2027 冬 / 2027 春`。
- `terms=[]` → 「2026–27 未排课」+ note。
- 同一门课可跨学期，允许重复出现。

---

## 内容规则

1. 一句话 ≤ 60 字，写「在体系里的位置 + 最有辨识度的内容」。
2. 先修要具体到课号；不确定写「见官方」。
3. 不伪造 PPT：slides 只在 Canvas 就写「slides 在 Canvas」。
4. 第三方视频 label 含年份 + 语言 + `（第三方）`。
5. 往期 syllabus 必须注明学期。

---

## 30 分钟 MVP

```text
20 门核心课
1 个 index + 20 个课程页
无逐讲、无先修图、无 B站
check.py 只校验页面数与链接
```

---

## 验收清单

- [ ] 课程页数 == 核心 + 延伸
- [ ] 每门课有学期、学分、难度、先修
- [ ] 逐讲课 ≥ 8 讲且编号连续
- [ ] 未排课课程有 note
- [ ] 第三方视频有风险提示 + 报告入口
- [ ] 搜索命中课号/名称/术语

---

## Brief 片段

```yaml
variant: course-map
institution: "Stanford University"
scope: "CS / EE / STATS / MS&E 的 AI 相关课程"
academic_year: "2026–27"
scale: { core: 55, extended: 70, outlines: 27 }
sources:
  catalog: "https://explorecourses.stanford.edu/"
  official: "各课程官网"
  video: "Stanford Online / B站"
```

---

## 给 AI 的增量指令

```text
按课程地图模板实现。先做 20 门核心课的垂直切片：
catalog 抓取 → items JSON → 课程详情页 → check.py。
验收后再补逐讲、先修图、学期页和视频页。
注意：学期用固定枚举；未排课课程必须有 note；不要伪造 slides 链接。
```
