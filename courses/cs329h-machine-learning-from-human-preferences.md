# CS 329H · 从人类偏好中学习

> RLHF 的理论与实作：从 choice model、偏好学习到 assistance games 和公平性。

| 项目 | 内容 |
| --- | --- |
| **课程编号** | CS 329H |
| **英文名称** | Machine Learning from Human Preferences |
| **学期** | 2026 秋 |
| **学分** | 3 |
| **评分** | Letter or Credit/No Credit |
| **授课** | Koyejo, S. |
| **先修** | 研究生级 ML 基础（CS 229 级）；概率与优化基础。 |
| **难度** | ★★★★☆（主观） |
| **标签** | `RLHF` · `偏好` · `对齐` · `推荐` |

## 课程定位

CS 329H 由 Sanmi Koyejo 讲授，系统讲解“如何优化被人使用的系统”。它把心理测量、离散选择、强化学习、信息检索和规范理论串起来，是理解 RLHF/DPO/推荐系统偏好建模的硬核课程。

## 主要内容

- **Choice modeling**：随机效用、Plackett-Luce、公理化方法
- **模仿与主动学习**：behavior cloning、偏好查询
- **RLHF**：奖励建模、PPO、DPO、KTO
- **Assistance games**：人机协作、bandit、推荐
- **行为偏差与风格控制**：偏好异质性、prompt/style
- **聚合与公平**：社会选择、群体偏好聚合

## 考核与工作量

作业 + 项目/论文复现，偏理论与实验结合。具体以当季官网为准。

## 适合谁

做 alignment、RLHF、推荐系统、人机交互的研究者；想理解“偏好数据为什么难”的工程师。

## 学习建议

先理解 Bradley-Terry 模型和 PPO。配合 CS 224N 的 RLHF 章节一起学。

## 相关课程

- [CS 224N · 自然语言处理与深度学习](cs224n-nlp-with-deep-learning.md)
- [CS 234 · 强化学习](cs234-reinforcement-learning.md)
- [CS 329A · 自我改进的 AI Agent](cs329a-self-improving-ai-agents.md)

## 资源

- [ExploreCourses](https://explorecourses.stanford.edu/search?view=catalog&academicYear=20262027&q=CS+329H)
- [课程官网](https://web.stanford.edu/class/cs329h/)

<details>
<summary>官方课程描述（英文原文）</summary>

> Machine learning from human preferences (MLHP) provides mechanisms for optimizing systems that are used by humans - with applications in personalization, finetuning, and assistance. MLHP has been important to successes in modern language modeling, but the technical and conceptual underpinnings are spread across fields: psychometrics, discrete choice, reinforcement learning, information retrieval, and normative theory. This course will provide a careful and practical introduction to the main methods and models of MLHP. It will cover: choice modeling and its axiomatic approaches; imitation and static and active learning of choice; reinforcement learning from human feedback; assistance games, bandits, and recommendation; behavioral biases, style control; aggregation and fairness. This is a graduate-level course. By the end of the course, students should be able to build, analyze, and optimize systems that are used by humans.

</details>

---

<sub>信息整理自 Stanford ExploreCourses（2026–27）与课程官网，最后更新 2026-10-30。课程安排、考核比例以官方为准。</sub>
