# 03 · 工具地图（Tool Map）

> 把某个方向的开源工具/框架/产品整理成「能力对比 + 选型建议 + 替代关系 + 维护状态」。
>
> 适合：技术选型、团队 toolbox、课程工具推荐、生态调研。

---

## 与通用骨架的差异

| 维度 | 课程地图 | 工具地图 |
|---|---|---|
| 主键 | 课号 | repo / 产品名 |
| 时间 | 学期 | 版本 + 最后提交 |
| 关系 | 先修 | 替代、依赖、集成 |
| 质量信号 | 难度 | 维护状态 + 采用度 + 许可证 |
| 最大坑 | 课件权限 | star 数误导、许可证、停更 |

---

## 数据源

| 数据 | 来源 | 备注 |
|---|---|---|
| 元数据 | GitHub API / 官网 | stars、license、last commit |
| 版本 | releases / changelog | 只取稳定版 |
| 依赖 | package registry / lockfile | 可选 |
| 采用度 | GitHub stars、下载量、招聘提及 | 必须存快照 |
| 安全 | OSV / GitHub Advisory | 可选 |
| 文档 | 官方 docs | 区分教程与 API reference |

---

## 实体字段

```json
{
  "id": "GH:vllm-project/vllm",
  "slug": "vllm",
  "name": "vLLM",
  "name_en": "vLLM",
  "category": "LLM 推理",
  "summary": "高吞吐 LLM 推理引擎，核心是 PagedAttention。",
  "facets": {
    "language": "Python/C++",
    "license": "Apache-2.0",
    "stars": 50000,
    "last_release": "2026-09",
    "maintenance": "active",
    "maturity": "production"
  },
  "tags": ["inference", "serving", "GPU"],
  "links": [
    { "label": "GitHub", "url": "https://github.com/vllm-project/vllm", "type": "official" },
    { "label": "文档", "url": "https://docs.vllm.ai/", "type": "docs" }
  ],
  "relations": [
    { "type": "alternative", "target": "GH:huggingface/text-generation-inference" },
    { "type": "depends_on", "target": "GH:NVIDIA/cuda" }
  ],
  "artifacts": [
    { "type": "install", "label": "pip install vllm", "url": "https://docs.vllm.ai/", "access": "public" }
  ],
  "sources": [
    { "label": "GitHub API", "url": "https://api.github.com/repos/vllm-project/vllm", "retrieved_at": "2026-10-31" }
  ],
  "freshness": {
    "checked_at": "2026-10-31",
    "volatile": ["stars", "last_release", "maintenance"]
  }
}
```

**领域必填 facet**：`language`, `license`, `stars`, `last_release`, `maintenance`, `maturity`。
**领域必填内容**：`use_case`, `pros`, `cons`, `alternatives`, `getting_started`。

---

## 分级规则

### 维护状态

| 值 | 含义 |
|---|---|
| `active` | 近 3 个月有提交/发版 |
| `maintained` | 近 12 个月有维护 |
| `stale` | 12–24 个月无更新 |
| `archived` | 归档/停止维护 |

### 成熟度

| 值 | 含义 |
|---|---|
| `experimental` | API 不稳定，慎用于生产 |
| `beta` | 可用，但边界情况多 |
| `production` | 有生产案例与稳定发版 |
| `legacy` | 仍可用，但推荐迁移 |

---

## 页面结构

| 页面 | 内容 |
|---|---|
| `index` | 分类入口 + 精选工具 + 全部工具 |
| `tool detail` | 定位、能力、安装、优缺点、替代品、维护状态 |
| `compare` | 3–5 个工具横向对比（功能/许可证/性能） |
| `stack` | 按场景组合的工具栈（如 RAG stack） |
| `alternatives` | 替代关系图 |

---

## 关键判断规则

1. **star ≠ 质量**：star 只作为采用度信号，必须和维护状态、文档质量一起看。
2. **许可证优先**：Apache/MIT 与 AGPL/SSPL 对商用影响完全不同，必须单列。
3. **区分「能跑」与「能上生产」**：demo 成功不等于 production-ready。
4. **不要只列优点**：每个工具至少 1 条 `cons`。
5. **快照日期**：stars、版本、维护状态都带 `checked_at`。

---

## 30 分钟 MVP

```text
25 个工具
5 个分类
index + detail + compare（只对比 3 个）
无依赖图、无 stack
```

---

## 验收清单

- [ ] 每个工具有 license、last release、维护状态
- [ ] 每个工具有 1 个官方链接 + 1 个文档链接
- [ ] 每个工具有至少 1 条缺点
- [ ] compare 页的维度一致
- [ ] star 数有快照日期
- [ ] 替代关系有依据

---

## Brief 片段

```yaml
variant: tool-map
field: "LLM 应用开发"
scope: "推理、编排、RAG、eval、可观测性"
scale: { core: 30, extended: 70 }
sources:
  metadata: "GitHub API"
  docs: "官方文档"
output:
  pages: [index, tool, compare, stack]
```

---

## 给 AI 的增量指令

```text
按工具地图模板实现。先做 25 个工具的垂直切片：
GitHub API 元数据 → items JSON → 详情页 → compare 页 → check.py。
stars 必须存快照日期；license 必须单列；
每个工具至少写 1 条 cons；不要把 star 数当质量分。
```
