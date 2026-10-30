# CS 217 · 机器学习硬件加速器

> ML 硬件加速器：数据流、张量处理、存储层次、编译，以及 CNN/Transformer 的映射。

| 项目 | 内容 |
| --- | --- |
| **课程编号** | CS 217<br>同时列于：EE 244 |
| **英文名称** | Hardware Accelerators for Machine Learning (EE 244) |
| **学期** | 2027 春 |
| **学分** | 3–4 |
| **评分** | Letter or Credit/No Credit |
| **授课** | Olukotun, O.、Tambe, T. |
| **先修** | 数字电路/计算机体系结构；VLSI 或 FPGA 经验有帮助。 |
| **难度** | ★★★★☆（主观） |
| **标签** | `硬件` · `加速器` · `体系结构` · `芯片` |

## 课程定位

CS 217（EE 244）由 Olukotun 和 Tambe 讲授，是 AI 芯片方向的经典课。课程从 CNN/Transformer 的计算模式出发，讲加速器架构、数据流、存储层次、低精度/稀疏和编译，最终做一个设计项目。

## 主要内容

- **AI 计算模式**：CNN、Transformer、训练 vs 推理
- **加速器架构**：脉动阵列、张量核心、数据流
- **存储层次**：片上缓存、HBM、数据复用
- **低精度与稀疏**：量化、剪枝、压缩
- **编译与映射**：算子调度、tiling
- **能效与面积**：系统级 trade-off
- **设计项目**

## 考核与工作量

论文阅读 + final design project。具体以当季官网为准。

## 适合谁

想做 AI 芯片、加速器、体系结构的人；硬件背景想理解 ML 负载的人。

## 学习建议

先理解 roofline 和矩阵乘的分块。配合 CS 149/CS 349E。

## 相关课程

- [CS 349E · 大规模高效 ML 推理](cs349e-efficient-ml-inference-at-scale.md)
- EE 244
- CS 149

## 资源

- [ExploreCourses](https://explorecourses.stanford.edu/search?view=catalog&academicYear=20262027&q=CS+217)
- [课程官网](https://cs217.stanford.edu/)

<details>
<summary>官方课程描述（英文原文）</summary>

> This course explores the design, programming, and performance of modern AI accelerators. It covers architectural techniques, dataflow, tensor processing, memory hierarchies, compilation for accelerators, and emerging trends in AI computing. This course will cover modern AI/ML algorithms such as convolutional neural nets, and Transformer-based models / LLMs. We will consider both training and inference for these models and discuss the impact of parameters such as batch size, precision, sparsity and compression on the accuracy of these models. Students will become familiar with hardware implementation techniques for using parallelism, locality, and low precision to implement the core computational kernels used in ML. Students will develop intuitions to make system-level trade-offs to design energy-efficient accelerators. Students will read recent research papers and complete a final design project.

</details>

---

<sub>信息整理自 Stanford ExploreCourses（2026–27）与课程官网，最后更新 2026-10-30。课程安排、考核比例以官方为准。</sub>
