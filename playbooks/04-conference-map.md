# 04 · 会议地图（Conference Map）

> 把某个领域的会议/期刊整理成「截稿日历 + 录用数据 + 投稿路线 + 系列关系」。
>
> 适合：投稿规划、领域入门、实验室 deadline 面板、学术活动日历。

---

## 与通用骨架的差异

| 维度 | 课程地图 | 会议地图 |
|---|---|---|
| 主键 | 课号 | 会议缩写 + 年份 |
| 时间 | 学期 | 截稿/通知/开会日期 |
| 关系 | 先修 | 同系列、同地、姊妹会 |
| 质量信号 | 难度 | 录用率 + h5 + 领域声誉 |
| 最大坑 | 课件权限 | 时区、周期、日期变更 |

---

## 数据源

| 数据 | 来源 | 备注 |
|---|---|---|
| 官方日期 | 会议官网 | 唯一可信来源 |
| 录用率 | 官网 / 统计博客 | 标注年份 |
| h5 / 影响因子 | Google Scholar Metrics | 只作参考 |
| 地点 | 官网 | 城市 + 场馆 |
| 注册费 | 官网 | 早鸟/学生/线上 |
| 系列历史 | 官网 / DBLP | 年份列表 |

---

## 实体字段

```json
{
  "id": "NEURIPS-2026",
  "slug": "neurips-2026",
  "name": "NeurIPS 2026",
  "name_en": "Conference on Neural Information Processing Systems 2026",
  "category": "机器学习",
  "summary": "ML 领域规模最大的综合会议，覆盖学习理论到系统。",
  "facets": {
    "year": 2026,
    "location": "Vancouver, Canada",
    "abstract_deadline": "2026-05-15T23:59:00-12:00",
    "paper_deadline": "2026-05-22T23:59:00-12:00",
    "notification": "2026-09-19",
    "conference_dates": "2026-12-06..2026-12-12",
    "acceptance_rate": 0.26,
    "h5_index": 320,
    "registration": "TBD"
  },
  "tags": ["ML", "NeurIPS", "deadline"],
  "links": [
    { "label": "官网", "url": "https://neurips.cc/", "type": "official" }
  ],
  "relations": [
    { "type": "same_series", "target": "NEURIPS-2025" }
  ],
  "artifacts": [
    { "type": "calendar", "label": "添加到日历 (.ics)", "url": "https://...", "access": "public" }
  ],
  "sources": [
    { "label": "NeurIPS 官网", "url": "https://neurips.cc/", "retrieved_at": "2026-10-31" }
  ],
  "freshness": {
    "checked_at": "2026-10-31",
    "volatile": ["deadlines", "location", "registration"]
  }
}
```

**领域必填 facet**：`year`, `location`, `paper_deadline`, `notification`, `conference_dates`。
**领域必填内容**：`scope`, `submission_tips`, `review_process`, `cost`, `travel`。

---

## 页面结构

| 页面 | 内容 |
|---|---|
| `index` | 按领域分组 + 最近 deadline |
| `conference detail` | 日期、地点、录用率、投稿要求、费用、往届 |
| `timeline` | 全年 deadline 时间轴 |
| `calendar` | 月历视图（可选） |
| `compare` | 3–5 个会议对比（录用率/规模/费用） |
| `series` | 同系列历年数据 |

---

## 关键判断规则

1. **时区必须显式**：截稿常用 AoE（UTC-12），存 ISO 时间 + 偏移，不要只写日期。
2. **区分 abstract / paper / supplementary**：三个 deadline 经常不同。
3. **录用率标年份**：2024 的 26% 不能代表 2026。
4. **workshop 单独标**：workshop deadline 通常晚于主会。
5. **日期会变**：页面必须显示「最后核验」并链接官网。

---

## 30 分钟 MVP

```text
15 个会议
按月份分组的 deadline 列表
index + detail
无日历、无对比、无系列图
```

---

## 验收清单

- [ ] 每个 deadline 有完整时间戳 + 时区
- [ ] 每个会议有官网链接
- [ ] 录用率标注年份与来源
- [ ] workshop 与主会分开
- [ ] 过期会议标「已结束」并归档
- [ ] 页面显示最后核验日期

---

## Brief 片段

```yaml
variant: conference-map
field: "NLP / ML / CV"
scope: "顶会 + 重要 workshop"
scale: { core: 20, extended: 30 }
sources:
  deadlines: "各会议官网"
  metrics: "Google Scholar Metrics"
output:
  pages: [index, conference, timeline, compare]
```

---

## 给 AI 的增量指令

```text
按会议地图模板实现。先做 15 个会议的垂直切片：
官网日期 → items JSON → detail 页 → timeline → check.py。
所有 deadline 必须带时区和 ISO 时间；录用率必须标年份；
不要合并 abstract/paper deadline；日期变更时保留旧快照。
```
