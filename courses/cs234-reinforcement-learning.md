# CS 234 · 强化学习

> 强化学习核心课：MDP、值迭代、策略梯度、探索，作业包含 deep RL。

| 项目 | 内容 |
| --- | --- |
| **课程编号** | CS 234 |
| **英文名称** | Reinforcement Learning |
| **学期** | 2026–27 未排课 |
| **学分** | 3 |
| **评分** | Letter or Credit/No Credit |
| **授课** | TBA |
| **先修** | 熟练 Python；CS 229 或同等 ML 基础；线性代数与概率。 |
| **难度** | ★★★★☆（主观） |
| **标签** | `RL` · `决策` · `机器人` |

> **备注**：2026-27 学年未在 ExploreCourses 排课，以最近一次开设的资料整理。

## 课程定位

CS 234 覆盖 RL 从表格方法到深度 RL 的主干，强调“自主系统如何通过试错做决策”。它适合机器人、游戏、推荐、医疗等序列决策场景，是 CS 224R/CS 332 的前置课。

## 主要内容

- **MDP 基础**：回报、贝尔曼方程、策略评估
- **动态规划**：值迭代、策略迭代
- **无模型方法**：蒙特卡洛、TD、Q-learning、SARSA
- **函数逼近**：线性逼近、深度 Q 网络
- **策略梯度**：REINFORCE、actor-critic、PPO
- **探索**：ε-greedy、UCB、 Thompson sampling
- **深度 RL 与离线 RL**：实践中的稳定性问题
- **项目**：通常训练一个 agent 解决控制/游戏任务

## 考核与工作量

通常为 3–4 次作业 + 期中 + 项目；至少一次 deep RL 作业。具体以当季官网为准。

## 适合谁

机器人、RL 研究、游戏 AI、推荐系统方向；想做具身智能的人。

## 学习建议

先把 MDP 和动态规划吃透，再上深度 RL。作业里的 exploration 部分建议配合 Sutton & Barto 第 2–3 章。

## 相关课程

- CS 224R
- CS 332
- [CS 237B · 机器人自主性原理 II](cs237b-principles-of-robot-autonomy-ii.md)

## 资源

- [ExploreCourses](https://explorecourses.stanford.edu/search?view=catalog&academicYear=20262027&q=CS+234)
- [课程官网](https://web.stanford.edu/class/cs234/)

<details>
<summary>官方课程描述（英文原文）</summary>

> To realize the dreams and impact of AI requires autonomous systems that learn to make good decisions. Reinforcement learning is one powerful paradigm for doing so, and it is relevant to an enormous range of tasks, including robotics, game playing, consumer modeling and healthcare. This class will briefly cover background on Markov decision processes and reinforcement learning, before focusing on some of the central problems, including scaling up to large domains and the exploration challenge. One key tool for tackling complex RL domains is deep learning and this class will include at least one homework on deep reinforcement learning. Prerequisites: proficiency in python, CS 229 or equivalents or permission of the instructor; linear algebra, basic probability.

</details>

---

<sub>信息整理自 Stanford ExploreCourses（2026–27）与课程官网，最后更新 2026-10-30。课程安排、考核比例以官方为准。</sub>
