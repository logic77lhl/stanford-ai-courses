# 05 · 数据集与基准地图（Dataset / Benchmark Map）

> 把某个领域的数据集、benchmark、leaderboard 整理成「任务视图 + 许可证 + 榜单 + 使用建议」。
>
> 适合：实验选数据集、复现论文、课程作业、模型评测调研。

---

## 与通用骨架的差异

| 维度 | 课程地图 | 数据集地图 |
|---|---|---|
| 主键 | 课号 | 数据集名 + 版本 |
| 时间 | 学期 | 版本 + 榜单更新 |
| 关系 | 先修 | 衍生、替代、同任务 |
| 质量信号 | 难度 | 规模 + 质量 + 饱和风险 |
| 最大坑 | 课件权限 | 许可证、数据泄漏、榜单饱和 |

---

## 数据源

| 数据 | 来源 | 备注 |
|---|---|---|
| 元数据 | Papers with Code / HuggingFace / Kaggle | 任务、规模、模态 |
| 许可证 | 数据集主页 | 必须原文核对 |
| 榜单 | Papers with Code / 官方 leaderboard | 存快照 |
| 基线 | 原论文 / 榜单 | 标注模型与设置 |
| 文档 | 数据集 card | 采集方式、偏差 |

---

## 实体字段

```json
{
  "id": "HF:imagenet-1k",
  "slug": "imagenet-1k",
  "name": "ImageNet-1K",
  "name_en": "ImageNet-1K",
  "category": "图像分类",
  "summary": "1000 类、约 128 万张训练图的视觉分类基准。",
  "facets": {
    "task": "image-classification",
    "modality": "image",
    "size": "1.28M train / 50K val",
    "license": "custom-research-only",
    "access": "registration",
    "year": 2009,
    "saturation": "high"
  },
  "tags": ["vision", "classification", "benchmark"],
  "links": [
    { "label": "官网", "url": "https://image-net.org/", "type": "official" },
    { "label": "Papers with Code", "url": "https://paperswithcode.com/dataset/imagenet", "type": "leaderboard" }
  ],
  "relations": [
    { "type": "derived_from", "target": "HF:imagenet-21k" }
  ],
  "artifacts": [
    { "type": "leaderboard", "label": "SOTA 榜单", "url": "https://...", "access": "public" }
  ],
  "sources": [
    { "label": "ImageNet 官网", "url": "https://image-net.org/", "retrieved_at": "2026-10-31" }
  ],
  "freshness": {
    "checked_at": "2026-10-31",
    "volatile": ["leaderboard", "license", "size"]
  }
}
```

**领域必填 facet**：`task`, `modality`, `size`, `license`, `access`, `saturation`。
**领域必填内容**：`construction`, `baselines`, `known_issues`, `usage_tips`。

---

## 许可证分级

| 值 | 含义 |
|---|---|
| `permissive` | MIT/Apache/CC-BY，商用友好 |
| `research-only` | 仅研究用途 |
| `non-commercial` | 禁止商用 |
| `custom` | 自定义条款，必须读原文 |
| `unknown` | 未标注，默认谨慎 |

**不要替用户判断「能不能商用」**，只给原文链接与风险提示。

---

## 饱和风险

| 值 | 含义 |
|---|---|
| `low` | 仍有明显提升空间 |
| `medium` | 头部模型接近上限 |
| `high` | 已饱和，建议换 benchmark |
| `contaminated` | 疑似训练集泄漏 |

---

## 页面结构

| 页面 | 内容 |
|---|---|
| `index` | 按任务/模态分组 + 推荐数据集 |
| `dataset detail` | 规模、许可证、构造方式、基线、榜单、坑 |
| `leaderboard` | 榜单快照 + 模型/设置 |
| `task view` | 单任务下的数据集对比 |
| `compare` | 3–5 个数据集横向对比 |

---

## 关键判断规则

1. **许可证必须原文核对**：HuggingFace 上的 license 标签不一定完整。
2. **榜单要带日期与设置**：zero-shot / fine-tuned / extra data 不能混排。
3. **区分 size 与可用性**：有些数据集标称很大，但需要申请。
4. **泄漏风险单列**：尤其是从网页抓的预训练语料。
5. **饱和 benchmark 要提示迁移**。

---

## 30 分钟 MVP

```text
30 个数据集
5 个任务
index + detail + task view
无榜单、无对比
许可证先标 unknown
```

---

## 验收清单

- [ ] 每个数据集有 task、modality、size
- [ ] 每个数据集有 license 原文链接
- [ ] 榜单有快照日期与评测设置
- [ ] 饱和/泄漏风险有标注
- [ ] 不给出法律结论，只给风险提示
- [ ] 访问方式（公开/申请/付费）明确

---

## Brief 片段

```yaml
variant: dataset-map
field: "多模态 / VLM"
scope: "图像-文本、视频-文本、评测基准"
scale: { core: 40, extended: 60 }
sources:
  metadata: "HuggingFace + Papers with Code"
  leaderboard: "官方榜单 + PwC"
output:
  pages: [index, dataset, leaderboard, task, compare]
```

---

## 给 AI 的增量指令

```text
按数据集地图模板实现。先做 30 个数据集的垂直切片：
元数据 → items JSON → detail 页 → task view → check.py。
许可证必须给原文链接；榜单必须带快照日期与评测设置；
不要判断「能否商用」，只给风险和原文。
```
