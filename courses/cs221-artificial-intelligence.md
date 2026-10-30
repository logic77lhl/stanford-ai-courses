# CS 221 · 人工智能：原理与技术

> AI 的“总览课”：把搜索、MDP、概率图模型、逻辑和机器学习放进同一个“有限信息 + 有限算力下做决策”的框架里。

| 项目 | 内容 |
| --- | --- |
| **课程编号** | CS 221 |
| **英文名称** | Artificial Intelligence: Principles and Techniques |
| **学期** | 2026 秋 / 2027 春 |
| **学分** | 3–4 |
| **评分** | Letter or Credit/No Credit |
| **授课** | Piech, C.、Liang, P. |
| **先修** | CS 103（或 103B/X）、CS 106B（或 106X）、CS 109、CS 161；官方明确要求“不要指望课上补这些基础”。 |
| **难度** | ★★★★☆（主观） |
| **标签** | `AI` · `基础` · `搜索` · `概率` |

## 课程定位

CS 221 是 Stanford AI 路线的入口课，也是理解“AI 不只是调模型”的最好方式。它用统一的数学语言（概率 + 算法）描述智能体如何在信息不完全、计算有限的情况下做决策，覆盖面从经典符号 AI 一直延伸到现代机器学习。

## 主要内容

- **搜索与约束满足**：DFS/BFS/A*、启发式、CSP、局部搜索
- **博弈与对抗搜索**：minimax、alpha-beta、期望效用
- **MDP 与强化学习**：值迭代、策略迭代、Q-learning 基础
- **概率图模型**：贝叶斯网络、HMM、变量消元、采样
- **机器学习**：朴素贝叶斯、感知机、逻辑回归、损失函数与正则化
- **逻辑与知识表示**：命题逻辑、一阶逻辑、推理
- **综合项目**：把上述模块组合成一个可运行的 AI 系统

## 考核与工作量

通常为 5 次左右书面/编程作业 + 期中 + 期末 + 一个综合项目；工作量在 Stanford 课程里偏大。具体比例以当季官网为准。

## 适合谁

想建立完整 AI 知识地图的本科生/转专业学生；之后准备读 CS 229/224N/234 的人；以及想补“经典 AI”这一块的工程师。

## 学习建议

先补概率（CS 109）和算法（CS 161），否则作业会很痛苦。作业里的搜索和 MDP 部分建议自己从零写一遍，不要只调库。

## 相关课程

- [CS 229 · 机器学习](cs229-machine-learning.md)
- [CS 228 · 概率图模型](cs228-probabilistic-graphical-models.md)
- [CS 234 · 强化学习](cs234-reinforcement-learning.md)

## 资源

- [ExploreCourses](https://explorecourses.stanford.edu/search?view=catalog&academicYear=20262027&q=CS+221)
- [课程官网](https://web.stanford.edu/class/cs221/)

<details>
<summary>官方课程描述（英文原文）</summary>

> Artificial intelligence (AI) has had a huge impact in many areas, including medical diagnosis, speech recognition, robotics, web search, advertising, and scheduling. This course focuses on the foundational concepts that drive these applications. In short, AI is the mathematics of making good decisions given incomplete information (hence the need for probability) and limited computation (hence the need for algorithms). Specific topics include search, constraint satisfaction, game playing,n Markov decision processes, graphical models, machine learning, and logic. Prerequisites: CS 103 or CS 103B/X, CS 106B or CS 106X, CS 109, and CS 161 (algorithms, probability, and object-oriented programming in Python). We highly recommend comfort with these concepts before taking the course, as we will be building on them with little review.

</details>

---

<sub>信息整理自 Stanford ExploreCourses（2026–27）与课程官网，最后更新 2026-10-30。课程安排、考核比例以官方为准。</sub>
