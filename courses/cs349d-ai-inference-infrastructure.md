# CS 349D · AI 推理基础设施

> AI 推理基础设施：compound AI systems 在云上如何部署、调度、扩展。

| 项目 | 内容 |
| --- | --- |
| **课程编号** | CS 349D |
| **英文名称** | AI Inference Infrastructure |
| **学期** | 2027 春 |
| **学分** | 3 |
| **评分** | Letter or Credit/No Credit |
| **授课** | Kozyrakis, C. |
| **先修** | 系统/体系结构/ML 基础；有分布式系统经验更好。 |
| **难度** | ★★★★☆（主观） |
| **标签** | `推理` · `基础设施` · `云` · `系统` |

## 课程定位

CS 349D 由 Christos Kozyrakis 讲授，是一门研究型 seminar，聚焦“推理”而不是训练。课程认为未来的 AI 系统是 compound systems（多模型 + 检索 + 工具 + 传统软件），并讨论支撑它们的云基础设施、调度和架构模式。

## 主要内容

- **推理 serving**：批处理、连续批处理、KV cache
- **Compound AI systems**：多组件编排、数据流
- **云基础设施**：弹性、多租户、成本
- **调度与路由**：模型路由、优先级、SLA
- **延迟/吞吐/成本**：权衡与优化
- **工业实践**：Databricks、OpenAI、NVIDIA 等 guest lecture
- **quarter-long project**

## 考核与工作量

论文讨论 + guest lectures + 2–3 人小组项目。具体以当季官网为准。

## 适合谁

想做推理平台、AI 基础设施、云系统的人；系统背景的研究生。

## 学习建议

配合 CS 349E 学单机/集群性能，配合 CS 349F 学网络。项目尽量基于真实 serving 栈。

## 相关课程

- [CS 349E · 大规模高效 ML 推理](cs349e-efficient-ml-inference-at-scale.md)
- [CS 349F · AI 系统的网络 Fabric 架构](cs349f-fabric-architectures-for-ai-systems.md)
- [CS 229S · 机器学习系统](cs229s-systems-for-machine-learning.md)

## 资源

- [ExploreCourses](https://explorecourses.stanford.edu/search?view=catalog&academicYear=20262027&q=CS+349D)
- [课程官网](https://web.stanford.edu/class/cs349d/)

<details>
<summary>官方课程描述（英文原文）</summary>

> The emergence of foundation models has revolutionized AI applications, but the most powerful AI systems today are increasingly compound systems - compositions of multiple models, retrievers, tools, and traditional software components. This research seminar explores the intersection of cloud computing infrastructure and compound AI systems, covering both the infrastructure required to build and deploy these systems at scale and the architectural patterns that make them effective. Students will participate in guest lectures from leading experts across academia and industry, including leaders of companies like Databricks, OpenAI, Foundry, NVIDIA, Microsoft, and more, read and discuss papers, and complete a quarter-long project in groups of 2-3.

</details>

---

<sub>信息整理自 Stanford ExploreCourses（2026–27）与课程官网，最后更新 2026-10-30。课程安排、考核比例以官方为准。</sub>
