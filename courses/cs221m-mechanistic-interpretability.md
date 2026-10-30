# CS 221M · 机制可解释性

> 机制可解释性：probing、steering、causal abstraction、sparse autoencoders，理解模型内部到底在算什么。

| 项目 | 内容 |
| --- | --- |
| **课程编号** | CS 221M |
| **英文名称** | Mechanistic Interpretability |
| **学期** | 2027 春 |
| **学分** | 3 |
| **评分** | Letter or Credit/No Credit |
| **授课** | Icard, T. |
| **先修** | 深度学习/LLM 基础；概率与线性代数；最好读过 Transformer。 |
| **难度** | ★★★★☆（主观） |
| **标签** | `可解释性` · `LLM` · `Safety` · `研究` |

## 课程定位

CS 221M 由 Thomas Icard 讲授，是少数系统讲 mechanistic interpretability 的课程。它强调因果方法而不是“看图说话”，覆盖 probing、steering、causal abstraction、SAE、circuits，并邀请学术界/工业界可解释性实验室做客座讲座。

## 主要内容

- **Probing**：线性探针、表征分析、局限性
- **Steering**：激活干预、方向向量、因果追踪
- **Causal abstraction**：因果图、干预、抽象映射
- **Sparse autoencoders**：字典学习、特征分解、单义性
- **Circuits**：注意力头、MLP 神经元、组合结构
- **LLM 内部机制**：事实回忆、推理、欺骗
- **可解释性与安全**：如何用于审计和 alignment

## 考核与工作量

作业 + 项目/论文复现；偏研究与讨论。具体以当季官网为准。

## 适合谁

想做 interpretability、AI safety、模型审计的人；想理解 LLM 内部机制的研究者。

## 学习建议

先读 Anthropic 的“Towards Monosemanticity”和“Scaling Monosemanticity”，以及 causal abstraction 相关论文。

## 相关课程

- [CS 329A · 自我改进的 AI Agent](cs329a-self-improving-ai-agents.md)
- [CS 224N · 自然语言处理与深度学习](cs224n-nlp-with-deep-learning.md)
- [CS 221 · 人工智能：原理与技术](cs221-artificial-intelligence.md)

## 资源

- [ExploreCourses](https://explorecourses.stanford.edu/search?view=catalog&academicYear=20262027&q=CS+221M)
- [课程官网](https://web.stanford.edu/class/cs221m/)

<details>
<summary>官方课程描述（英文原文）</summary>

> What is the internal structure of modern neural networks and how can we study it? This course provides a broad and deep introduction to interpretability, the subfield of machine learning concerned with understanding precisely how models process information and why they produce the outputs they do. We will cover topics such as probing, steering, causal abstraction, and sparse autoencoders, with a particular emphasis on causal methods and large language models. The course will include guest lectures from leading interpretability labs across academia and industry.

</details>

---

<sub>信息整理自 Stanford ExploreCourses（2026–27）与课程官网，最后更新 2026-10-30。课程安排、考核比例以官方为准。</sub>
