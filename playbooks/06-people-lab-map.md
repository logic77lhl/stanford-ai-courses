# 06 · 学者与实验室地图（People & Lab Map）

> 把某个领域的学者、实验室、研究方向整理成「人物卡 + 方向聚类 + 合作/师承关系 + 招生状态」。
>
> 适合：找导师、找合作者、会议 person 追踪、研究方向全景。

---

## 与通用骨架的差异

| 维度 | 课程地图 | 人物地图 |
|---|---|---|
| 主键 | 课号 | 姓名 + 机构 |
| 时间 | 学期 | 任职/招生状态 |
| 关系 | 先修 | 合作、师承、同机构 |
| 质量信号 | 难度 | 代表工作 + 领域影响力 |
| 最大坑 | 课件权限 | 隐私、过期信息、招生误判 |

---

## 数据源

| 数据 | 来源 | 备注 |
|---|---|---|
| 基本信息 | 个人主页 / 实验室页 | 唯一可信来源 |
| 论文 | Google Scholar / DBLP | 只取代表工作 |
| 合作 | DBLP / Semantic Scholar | 只取稳定合作 |
| 招生 | 个人主页 | 必须标「最后核验」 |
| 机构 | 学校官网 | 区分院系/实验室 |

---

## 实体字段

```json
{
  "id": "PERSON:percy-liang",
  "slug": "percy-liang",
  "name": "Percy Liang",
  "name_en": "Percy Liang",
  "category": "LLM / NLP",
  "summary": "Stanford CRFM 主任，研究基础模型评测、对齐与语言模型。",
  "facets": {
    "affiliation": "Stanford University",
    "department": "Computer Science",
    "role": "Associate Professor",
    "recruiting": "unknown",
    "h_index": 90,
    "last_verified": "2026-10-31"
  },
  "tags": ["LLM", "evaluation", "alignment"],
  "links": [
    { "label": "个人主页", "url": "https://cs.stanford.edu/~pliang/", "type": "official" },
    { "label": "Google Scholar", "url": "https://scholar.google.com/...", "type": "profile" }
  ],
  "relations": [
    { "type": "affiliated_with", "target": "LAB:stanford-crfm" },
    { "type": "advised_by", "target": "PERSON:..." }
  ],
  "artifacts": [
    { "type": "talk", "label": "代表性 talk", "url": "https://...", "access": "public" }
  ],
  "sources": [
    { "label": "个人主页", "url": "https://cs.stanford.edu/~pliang/", "retrieved_at": "2026-10-31" }
  ],
  "freshness": {
    "checked_at": "2026-10-31",
    "volatile": ["role", "recruiting", "affiliation"]
  }
}
```

**领域必填 facet**：`affiliation`, `department`, `role`, `recruiting`, `last_verified`。
**领域必填内容**：`research_areas`, `representative_works`, `advising_style`, `how_to_contact`。

---

## 招生状态

| 值 | 含义 |
|---|---|
| `open` | 主页明确写正在招生 |
| `closed` | 明确写不招生 |
| `unknown` | 没写/过期 |
| `not_applicable` | 非教职/已退休 |

**默认 `unknown`，不要根据「看起来年轻」猜招生。**

---

## 页面结构

| 页面 | 内容 |
|---|---|
| `index` | 按方向聚类 + 精选人物 |
| `person detail` | 方向、代表工作、实验室、招生、联系方式 |
| `lab detail` | 成员、方向、代表论文、招生 |
| `area graph` | 人物-方向二部图 |
| `collaboration` | 合作网络（可选） |

---

## 关键判断规则

1. **隐私优先**：只收公开主页信息；不收录私人邮箱、住址、学生名单细节。
2. **招生状态必须标来源与日期**，否则写 `unknown`。
3. **代表工作 ≤ 5 篇**，不要把所有论文堆上去。
4. **区分「师承」与「合作」**：不要从 co-author 推断导师关系。
5. **机构变动常见**：页面必须显示最后核验日期。

---

## 30 分钟 MVP

```text
30 位学者
5 个方向
index + person detail
无实验室页、无合作图
招生状态全部 unknown
```

---

## 验收清单

- [ ] 每个人都有官方主页
- [ ] 招生状态有来源或标 unknown
- [ ] 代表工作 ≤ 5 篇
- [ ] 不包含私人联系方式
- [ ] 关系边有依据
- [ ] 页面显示最后核验日期

---

## Brief 片段

```yaml
variant: people-lab-map
field: "LLM agents / evaluation"
scope: "高校与工业界研究者 + 实验室"
scale: { people: 60, labs: 15 }
sources:
  profile: "个人主页 + DBLP"
  recruiting: "个人主页原文"
output:
  pages: [index, person, lab, area-graph]
```

---

## 给 AI 的增量指令

```text
按学者与实验室模板实现。先做 30 位学者的垂直切片：
主页信息 → items JSON → person detail → area graph → check.py。
招生状态默认 unknown，只有主页明确写了才改；
不要收录私人邮箱；代表工作最多 5 篇；合作边必须有共同论文依据。
```
