# CS 336 · 从零构建语言模型

> 从零造一个语言模型：数据清洗、tokenizer、Transformer、训练、scaling、eval、部署。

| 项目 | 内容 |
| --- | --- |
| **课程编号** | CS 336 |
| **英文名称** | Language Modeling from Scratch |
| **学期** | 2027 春 |
| **学分** | 3–5 |
| **评分** | Letter or Credit/No Credit |
| **授课** | Liang, P.、Hashimoto, T. |
| **先修** | 强编程能力；深度学习基础（CS 224N/CS 231N/CS 230 级）；需要申请，且最好有 GPU 资源。 |
| **难度** | ★★★★★（主观） |
| **标签** | `LLM` · `预训练` · `系统` · `硬核` |

## 课程定位

CS 336 是目前最硬核的 LLM 课程之一，由 Percy Liang 和 Tatsunori Hashimoto 讲授。课程借鉴“操作系统从零实现”的思路，带学生走完语言模型的全生命周期；作业需要大量 GPU 算力，选课需要申请。

## 主要内容

- **数据**：采集、清洗、去重、过滤、配比
- **Tokenization**：BPE、词表设计、多语言问题
- **模型**：Transformer 架构、注意力变体、位置编码
- **训练**：初始化、优化器、学习率、混合精度、分布式
- **Scaling**：scaling laws、计算最优配置
- **评估**：困惑度、基准测试、污染、对齐评估
- **部署**：推理、量化、服务化
- **安全与伦理**：数据版权、偏见、滥用

## 考核与工作量

通常为 5 个左右的编程作业（逐步构建 LM）+ 一个项目；算力消耗大。具体以当季官网为准。

## 适合谁

想真正理解 LLM 全栈、之后做预训练/推理/系统研究的人；想创业做模型的人。

## 学习建议

先修 CS 224N 或 CS 231N。没有 GPU 的话可以先跑小模型，但作业体验会受限。

## 相关课程

- [CS 224N · 自然语言处理与深度学习](cs224n-nlp-with-deep-learning.md)
- [CS 229S · 机器学习系统](cs229s-systems-for-machine-learning.md)
- [CS 349E · 大规模高效 ML 推理](cs349e-efficient-ml-inference-at-scale.md)

## 资源

- [ExploreCourses](https://explorecourses.stanford.edu/search?view=catalog&academicYear=20262027&q=CS+336)
- [课程官网](https://cs336.stanford.edu/)

<details>
<summary>官方课程描述（英文原文）</summary>

> Language models serve as the cornerstone of modern natural language processing (NLP) applications and open up a new paradigm of having a single general purpose system address a range of downstream tasks. As the field of artificial intelligence (AI), machine learning (ML), and NLP continues to grow, possessing a deep understanding of language models becomes essential for scientists and engineers alike. This course is designed to provide students with a comprehensive understanding of language models by walking them through the entire process of developing their own. Drawing inspiration from operating systems courses that create an entire operating system from scratch, we will lead students through every aspect of language model creation, including data collection and cleansing for pre-training, transformer model construction, model training, and evaluation before deployment. Application required, apply at http://cs336.stanford.edu/

</details>

---

<sub>信息整理自 Stanford ExploreCourses（2026–27）与课程官网，最后更新 2026-10-30。课程安排、考核比例以官方为准。</sub>
