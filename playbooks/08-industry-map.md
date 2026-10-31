# 08 · 公司与产业地图（Industry / Company Map）

> 把某个赛道的公司、产品、融资、竞争关系整理成「产业地图 + 公司卡 + 融资时间线 + 对比矩阵」。
>
> 适合：行业研究、求职、投资初筛、竞品分析、技术商业化调研。

---

## 与通用骨架的差异

| 维度 | 课程地图 | 产业地图 |
|---|---|---|
| 主键 | 课号 | 公司名 + 产品 |
| 时间 | 学期 | 融资/估值/产品发布 |
| 关系 | 先修 | 竞品、供应商、客户 |
| 质量信号 | 难度 | 融资 + 客户 + 技术壁垒 |
| 最大坑 | 课件权限 | 私有数据、传闻、估值口径 |

---

## 数据源

| 数据 | 来源 | 备注 |
|---|---|---|
| 公司信息 | 官网 / LinkedIn | 员工数、总部 |
| 融资 | Crunchbase / SEC / 新闻稿 | 标注轮次与日期 |
| 估值 | 融资新闻 / 二级市场 | 必须标「报道值」 |
| 产品 | 官网 / docs / pricing | 定价可能不公开 |
| 客户 | 案例页 / 新闻 | 区分 logo 与真实付费 |
| 竞争 | 官网对比页 / 第三方报告 | 不照抄厂商话术 |

---

## 实体字段

```json
{
  "id": "CO:openai",
  "slug": "openai",
  "name": "OpenAI",
  "name_en": "OpenAI",
  "category": "基础模型",
  "summary": "以 GPT 系列为核心的基础模型公司，同时提供 API 与消费级产品。",
  "facets": {
    "founded": 2015,
    "hq": "San Francisco, USA",
    "stage": "late-stage-private",
    "last_round": "2026-03",
    "valuation_usd_b": 300,
    "employees": "3000+",
    "status": "active"
  },
  "tags": ["foundation model", "API", "consumer"],
  "links": [
    { "label": "官网", "url": "https://openai.com/", "type": "official" }
  ],
  "relations": [
    { "type": "competitor", "target": "CO:anthropic" },
    { "type": "supplier", "target": "CO:nvidia" }
  ],
  "artifacts": [
    { "type": "pricing", "label": "API 定价", "url": "https://openai.com/api/pricing/", "access": "public" }
  ],
  "sources": [
    { "label": "官网", "url": "https://openai.com/", "retrieved_at": "2026-10-31" },
    { "label": "融资报道", "url": "https://...", "retrieved_at": "2026-10-31" }
  ],
  "freshness": {
    "checked_at": "2026-10-31",
    "volatile": ["valuation_usd_b", "employees", "last_round", "pricing"]
  }
}
```

**领域必填 facet**：`founded`, `hq`, `stage`, `last_round`, `valuation_usd_b`, `status`。
**领域必填内容**：`product`, `business_model`, `moat`, `customers`, `risks`。

---

## 数据可信度分级

| 值 | 含义 |
|---|---|
| `official` | 公司官网/ SEC 文件 |
| `reported` | 可信媒体报道 |
| `estimated` | 第三方估算 |
| `rumor` | 未证实传闻，默认不收录 |

页面上必须显示可信度，不要把 `estimated` 写成事实。

---

## 页面结构

| 页面 | 内容 |
|---|---|
| `index` | 赛道分层（芯片/云/模型/应用）+ 精选公司 |
| `company detail` | 产品、商业模式、融资、客户、竞争、风险 |
| `landscape` | 2×2 或分层矩阵 |
| `funding timeline` | 融资/估值时间线 |
| `compare` | 3–5 家公司对比 |

---

## 关键判断规则

1. **估值标口径**：融资估值 / 二级市场 / 报道值，不能混。
2. **员工数标来源与日期**：LinkedIn 数字波动大。
3. **客户 logo ≠ 付费客户**：写「案例客户」而不是「客户」。
4. **竞争关系不要照抄厂商对比页**。
5. **传闻不收录**；必须收录时标 `rumor` 并说明。

---

## 30 分钟 MVP

```text
30 家公司
4 个赛道层级
index + company detail + landscape
无融资时间线、无对比
估值先留空
```

---

## 验收清单

- [ ] 每家公司有官网与成立年份
- [ ] 融资/估值有来源与日期
- [ ] 私有数据标 `estimated`
- [ ] 客户描述不夸大
- [ ] 竞争关系有依据
- [ ] 页面显示最后核验日期

---

## Brief 片段

```yaml
variant: industry-map
field: "生成式 AI 产业链"
scope: "芯片 / 云 / 模型 / 应用"
scale: { core: 40, extended: 80 }
sources:
  company: "官网 + SEC"
  funding: "Crunchbase + 新闻稿"
output:
  pages: [index, company, landscape, funding-timeline, compare]
```

---

## 给 AI 的增量指令

```text
按产业地图模板实现。先做 30 家公司的垂直切片：
官网/融资信息 → items JSON → company detail → landscape → check.py。
估值必须标口径与日期；员工数标来源；传闻不收录；
客户写「案例客户」，不要写「客户包括」。
```
