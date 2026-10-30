# CS 329Z · AI Agent 工程

> 从 LLM pipeline 到 compound AI system 再到 autonomous agent 的工程方法论：选问题、拆解、选组件、做 eval。

| 项目 | 内容 |
| --- | --- |
| **课程编号** | CS 329Z |
| **英文名称** | Engineering AI Agents |
| **学期** | 2026 秋 |
| **学分** | 3 |
| **评分** | Letter or Credit/No Credit |
| **授课** | Yang, D.、Ryan, M.、Yang, J. |
| **先修** | 编程能力；LLM 基础（prompting、API 使用）；有 ML 基础更好。 |
| **难度** | ★★★★☆（主观） |
| **标签** | `Agent` · `工程` · `RAG` · `Eval` |

## 课程定位

CS 329Z 是目前最贴近“AI 工程师”岗位的课程之一，由 Diyi Yang 等人讲授。它强调 agent 不是一个大模型，而是由 LLM、检索器、工具、优化器组成的复合系统；课程从零实现 RAG、tool use、agent loop，再过渡到 DSPy 等框架。

## 主要内容

- **Compound AI systems**：多组件系统的设计范式
- **RAG**：检索、重排、上下文管理、评估
- **Tool use**：函数调用、工具选择、错误处理
- **Agent loop**：规划、执行、反思、终止条件
- **DSPy**：用声明式方式优化 prompt/流程
- **数据 curation 与 evaluation**：构建 eval set、离线/在线指标
- **设计 trade-off**：延迟、成本、质量、可控性
- **三次 applied homework + quarter-long project**

## 考核与工作量

3 个 fully applied homework + 一个 quarter-long project，重点是 build、optimize、evaluate。具体以当季官网为准。

## 适合谁

想成为 AI engineer/agent 工程师的人；想从传统后端/ML 转向 LLM 应用的人；创业者。

## 学习建议

和 CS 224V 互补：224V 偏研究/形式化，329Z 偏工程/eval。作业不要只跑通 demo，重点是把 eval 做扎实。

## 相关课程

- [CS 224V · 智能体 AI](cs224v-agentic-ai.md)
- [CS 329T · 可信机器学习：构建与评估 Agent 系统](cs329t-trustworthy-machine-learning.md)
- [CS 224G · LLM 应用开发](cs224g-apps-with-llms-inside.md)

## 资源

- [ExploreCourses](https://explorecourses.stanford.edu/search?view=catalog&academicYear=20262027&q=CS+329Z)
- [课程官网](https://web.stanford.edu/class/cs329z/)

<details>
<summary>官方课程描述（英文原文）</summary>

> The shift from monolithic language models to compound AI systems - systems with multiple interacting components including LLMs, retrievers, tools, and optimizers -n represents a fundamental change in how AI applications are built for people. This course teaches students how to engineer agentic systems: the full spectrum from simple LLM pipelines to compound AI systems to autonomous agents. Students will learn to pick what types of problems to focus on, decompose problems, select appropriate components, collect and curate data, build evaluations, and reason about the design tradeoffs that arise when building these systems in practice. Students first build core components (RAG, tool use, agent loops) from scratch, then learn how frameworks like DSPy abstract these patterns. Through three fully applied homework assignments and a quarter-long project, students will gain hands-on experience building, optimizing, and evaluating agentic systems.

</details>

---

<sub>信息整理自 Stanford ExploreCourses（2026–27）与课程官网，最后更新 2026-10-30。课程安排、考核比例以官方为准。</sub>
