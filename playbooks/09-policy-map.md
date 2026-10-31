# 09 · 政策与法规地图（Policy / Regulation Map）

> 把某个领域的法律、法规、标准、监管指南整理成「管辖区对比 + 时间线 + 义务清单 + 修订追踪」。
>
> 适合：合规入门、产品出海、政策研究、企业风险盘点。

---

## 与通用骨架的差异

| 维度 | 课程地图 | 法规地图 |
|---|---|---|
| 主键 | 课号 | 法规编号/名称 + 管辖区 |
| 时间 | 学期 | 生效/过渡/修订 |
| 关系 | 先修 | 修订、实施、替代 |
| 质量信号 | 难度 | 约束力 + 罚则 + 适用范围 |
| 最大坑 | 课件权限 | 法律准确性、版本、翻译 |

---

## 数据源

| 数据 | 来源 | 备注 |
|---|---|---|
| 法规原文 | 官方公报 / EUR-Lex / Congress.gov | 唯一权威 |
| 监管指南 | 监管机构官网 | 解释性文件 |
| 生效日期 | 原文条款 | 注意过渡期 |
| 罚则 | 原文 | 上限/比例/刑事责任 |
| 修订 | 官方 tracker | 只追加版本 |
| 解读 | 律所/智库 | 仅作参考，标 `secondary` |

---

## 实体字段

```json
{
  "id": "EU:AI-ACT",
  "slug": "eu-ai-act",
  "name": "欧盟人工智能法案",
  "name_en": "EU Artificial Intelligence Act",
  "category": "AI 监管",
  "summary": "按风险分级监管 AI 系统的横向立法，含通用模型与高风险系统义务。",
  "facets": {
    "jurisdiction": "EU",
    "instrument": "regulation",
    "status": "in-force-phased",
    "introduced": "2021-04-21",
    "effective": "2024-08-01",
    "transition": "2026-08-02",
    "regulator": "European AI Office",
    "penalty": "up to 7% global turnover"
  },
  "tags": ["AI", "EU", "risk-based"],
  "links": [
    { "label": "EUR-Lex 原文", "url": "https://eur-lex.europa.eu/...", "type": "official" }
  ],
  "relations": [
    { "type": "amends", "target": "EU:..." }
  ],
  "artifacts": [
    { "type": "guide", "label": "官方实施指南", "url": "https://...", "access": "public" }
  ],
  "sources": [
    { "label": "EUR-Lex", "url": "https://eur-lex.europa.eu/...", "retrieved_at": "2026-10-31" }
  ],
  "freshness": {
    "checked_at": "2026-10-31",
    "volatile": ["status", "transition", "guidance"]
  }
}
```

**领域必填 facet**：`jurisdiction`, `instrument`, `status`, `introduced`, `effective`, `regulator`, `penalty`。
**领域必填内容**：`scope`, `obligations`, `who_is_covered`, `compliance_steps`, `open_questions`。

---

## 状态与约束力

| 字段 | 取值 |
|---|---|
| `instrument` | `law` / `regulation` / `directive` / `standard` / `guidance` / `bill` |
| `status` | `proposed` / `in-force` / `in-force-phased` / `repealed` / `stalled` |
| 约束力 | `binding` / `semi-binding` / `voluntary` |

**不要把「草案」写成「已生效」。**

---

## 页面结构

| 页面 | 内容 |
|---|---|
| `index` | 按管辖区/主题分组 + 近期生效 |
| `instrument detail` | 范围、义务、罚则、时间线、官方链接 |
| `timeline` | 提案 → 通过 → 生效 → 过渡期 |
| `compare` | 多管辖区对比（EU/US/UK/CN） |
| `obligations` | 按角色（提供者/部署者/进口商）列义务 |

---

## 关键判断规则

1. **只引用官方原文**；律所解读标 `secondary`。
2. **区分生效日与过渡期**：很多义务分阶段适用。
3. **区分角色**：提供者、部署者、进口商、分销商的义务不同。
4. **罚则写口径**：固定金额 / 全球营业额比例 / 刑事责任。
5. **必须放免责声明**：不是法律意见，具体咨询律师。
6. **保留历史版本**：修订后旧版归档，不覆盖。

---

## 30 分钟 MVP

```text
20 部法规
3 个管辖区
index + detail + timeline
无对比、无义务清单
```

---

## 验收清单

- [ ] 每部法规有官方原文链接
- [ ] 状态与生效日期准确
- [ ] 区分 binding / voluntary
- [ ] 罚则口径完整
- [ ] 页面有「非法律意见」声明
- [ ] 修订有版本记录

---

## Brief 片段

```yaml
variant: policy-map
field: "AI 监管"
scope: "EU / US / UK / China 的 AI 法律与标准"
scale: { core: 25, extended: 40 }
sources:
  primary: "官方公报 / EUR-Lex / Congress.gov"
  secondary: "监管机构指南"
output:
  pages: [index, instrument, timeline, compare, obligations]
```

---

## 给 AI 的增量指令

```text
按政策地图模板实现。先做 20 部法规的垂直切片：
官方原文 → items JSON → detail → timeline → check.py。
只引用官方原文；区分生效日与过渡期；区分提供者/部署者义务；
不要给法律结论；页面顶部放「非法律意见」声明。
```
