# 10 · 城市与场所指南（Local Guide）

> 把一座城市/一个区域的场所整理成「分类地图 + 场所卡 + 路线 + 季节日历」。
>
> 这是一个**非技术**模板，用来验证这套骨架不只适用于课程或 AI。

---

## 与通用骨架的差异

| 维度 | 课程地图 | 城市指南 |
|---|---|---|
| 主键 | 课号 | 场所 ID（自建） |
| 时间 | 学期 | 营业时间/季节/价格 |
| 关系 | 先修 | 邻近、同类型、路线 |
| 质量信号 | 难度 | 体验 + 性价比 + 拥挤度 |
| 最大坑 | 课件权限 | 停业、涨价、营业时间变 |

---

## 数据源

| 数据 | 来源 | 备注 |
|---|---|---|
| 基本信息 | 官方站点 / Google Maps / 大众点评 | 以官方为准 |
| 营业时间 | 官方 / Maps | 节假日经常变 |
| 价格 | 官方 / 菜单 | 标「起价」与日期 |
| 交通 | 地图 / 公交官网 | 步行时间给区间 |
| 预约 | 官方 | 是否必须预约 |
| 无障碍 | 官方 / 评论 | 不确定写 unknown |

---

## 实体字段

```json
{
  "id": "PLACE:museum-xxx",
  "slug": "museum-xxx",
  "name": "某某博物馆",
  "name_en": "Museum XXX",
  "category": "博物馆",
  "summary": "以现代艺术为主，常设展免费，特展另收费。",
  "facets": {
    "area": "市中心",
    "hours": "Tue–Sun 10:00–18:00",
    "closed": "Monday",
    "price": "free / special exhibition ¥80",
    "transit": "Metro Line 2, Exit B, 8 min walk",
    "reservation": "not-required",
    "accessibility": "wheelchair-accessible",
    "crowd": "high-weekend"
  },
  "tags": ["art", "indoor", "rainy-day"],
  "links": [
    { "label": "官网", "url": "https://...", "type": "official" }
  ],
  "relations": [
    { "type": "nearby", "target": "PLACE:park-xxx", "note": "步行 10 分钟" }
  ],
  "artifacts": [
    { "type": "map", "label": "地图", "url": "https://...", "access": "public" }
  ],
  "sources": [
    { "label": "官网", "url": "https://...", "retrieved_at": "2026-10-31" }
  ],
  "freshness": {
    "checked_at": "2026-10-31",
    "volatile": ["hours", "price", "closed", "reservation"]
  }
}
```

**领域必填 facet**：`area`, `hours`, `price`, `transit`, `reservation`。
**领域必填内容**：`why_go`, `best_time`, `tips`, `avoid`, `nearby`.

---

## 页面结构

| 页面 | 内容 |
|---|---|
| `index` | 分类入口 + 精选 + 全部场所 |
| `place detail` | 照片、时间、价格、交通、建议、附近 |
| `map` | 地图打点（Leaflet/静态图） |
| `itinerary` | 半日/一日路线 |
| `seasonal` | 季节/节假日日历 |

---

## 关键判断规则

1. **营业时间标最后核验**：Google Maps 也可能错。
2. **价格写「起价」**，并标日期。
3. **区分「适合」与「不适合」**：例如「适合雨天，但没有寄存」。
4. **交通给区间**：步行 8–12 分钟，不要写精确 9 分钟。
5. **停业要归档**，不要直接删，标 `closed`。

---

## 30 分钟 MVP

```text
30 个场所
5 个分类
index + place detail
无地图、无路线
```

---

## 验收清单

- [ ] 每个场所有官方链接或地图链接
- [ ] 营业时间 + 闭馆日完整
- [ ] 价格标日期
- [ ] 交通方式可执行
- [ ] 停业/装修有标注
- [ ] 页面显示最后核验日期

---

## Brief 片段

```yaml
variant: local-guide
city: "京都"
scope: "博物馆 / 寺庙 / 咖啡馆 / 公园"
scale: { core: 50, extended: 100 }
sources:
  official: "场所官网"
  map: "Google Maps / 当地公交"
output:
  pages: [index, place, map, itinerary, seasonal]
```

---

## 给 AI 的增量指令

```text
按城市指南模板实现。先做 30 个场所的垂直切片：
官方信息 → items JSON → detail 页 → index → check.py。
营业时间/价格必须标最后核验；停业不要删除，标 closed；
交通时间给区间；不要编造评分。
```
