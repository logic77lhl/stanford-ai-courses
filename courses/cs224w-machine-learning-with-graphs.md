# CS 224W · 图机器学习

> 图机器学习：GNN、知识图谱、影响力最大化，把关系数据变成可学习的表示。

| 项目 | 内容 |
| --- | --- |
| **课程编号** | CS 224W |
| **英文名称** | Machine Learning with Graphs |
| **学期** | 2026 秋 |
| **学分** | 3–4 |
| **评分** | Letter or Credit/No Credit |
| **授课** | Leskovec, J. |
| **先修** | CS 109；一门入门机器学习课程。 |
| **难度** | ★★★☆☆（主观） |
| **标签** | `图` · `GNN` · `表示学习` |

## 课程定位

CS 224W 由 Jure Leskovec 讲授，是图神经网络方向最受欢迎的课程之一。它覆盖图结构分析、节点/图表示学习、GNN、知识图谱推理、传播与影响力，应用横跨社交网络、推荐、生物网络和欺诈检测。

## 主要内容

- **图基础**：中心性、社区发现、幂律、图生成
- **节点嵌入**：DeepWalk、node2vec、矩阵分解
- **GNN**：GCN、GraphSAGE、GAT、消息传递
- **知识图谱**：TransE、RotatE、查询与推理
- **传播与影响力**：独立级联、线性阈值、影响力最大化
- **图生成与自监督**：图对比学习、扩散
- **项目**：通常用真实图数据做预测/分析

## 考核与工作量

作业 + 项目；编程以 PyTorch/PyG 为主。具体以当季官网为准。

## 适合谁

社交网络、推荐、风控、生物网络、知识图谱方向；想补“非欧几里得数据”建模的人。

## 学习建议

先理解消息传递范式，再学各种 GNN 变体。项目可以结合 CS 246 的大规模数据方法。

## 相关课程

- CS 246
- [CS 229 · 机器学习](cs229-machine-learning.md)
- [CS 224N · 自然语言处理与深度学习](cs224n-nlp-with-deep-learning.md)

## 资源

- [ExploreCourses](https://explorecourses.stanford.edu/search?view=catalog&academicYear=20262027&q=CS+224W)
- [课程官网](https://web.stanford.edu/class/cs224w/)

<details>
<summary>官方课程描述（英文原文）</summary>

> Many complex data can be represented as a graph of relationships between objects. Such networks are a fundamental tool for modeling complex social, technological, and biological systems. This course focuses on the computational, algorithmic, and modeling challenges specific to the analysis of massive graphs. By means of studying the underlying graph structure and its features, students are introduced to machine learning techniques and data mining tools apt to reveal insights on a variety of networks. Topics include: representation learning and Graph Neural Networks; algorithms for the World Wide Web; reasoning over Knowledge Graphs; influence maximization; disease outbreak detection, social network analysis. Prerequisites: CS109, any introductory course in Machine Learning.

</details>

---

<sub>信息整理自 Stanford ExploreCourses（2026–27）与课程官网，最后更新 2026-10-30。课程安排、考核比例以官方为准。</sub>
