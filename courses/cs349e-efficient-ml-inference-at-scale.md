# CS 349E · 大规模高效 ML 推理

> 大规模高效推理：模型优化、分布式 serving、AI 硬件、kernel、编译器。

| 项目 | 内容 |
| --- | --- |
| **课程编号** | CS 349E<br>同时列于：EE 339 |
| **英文名称** | Efficient ML Inference at Scale (EE 339) |
| **学期** | 2026 秋 |
| **学分** | 3 |
| **评分** | Letter or Credit/No Credit |
| **授课** | Asgar, Z.、Raina, P.、Horowitz, M.、Kjoelstad, F. |
| **先修** | 计算机体系结构、操作系统、ML 基础；强编程能力。 |
| **难度** | ★★★★★（主观） |
| **标签** | `推理` · `性能` · `硬件` · `编译` |

## 课程定位

CS 349E（EE 339）由 Mark Horowitz、Fredrik Kjolstad 等讲授，是系统 + 算法 + 硬件的硬核课。它讨论如何在异构机器上以低延迟、高吞吐、低成本服务大模型，覆盖量化、分布式 serving、性能建模、kernel 编程和 AI 编译器。

## 主要内容

- **模型优化**：量化、剪枝、蒸馏、投机解码
- **分布式 serving**：张量并行、流水线、PD 分离
- **AI 硬件**：GPU/TPU/专用加速器、内存墙
- **性能建模**：roofline、带宽/算力/延迟
- **Kernel 编程**：CUDA/Triton、融合、tiling
- **AI 编译器**：图优化、算子选择、代码生成
- **项目**：端到端推理优化

## 考核与工作量

作业 + 项目，偏实现与性能测量。具体以当季官网为准。

## 适合谁

想做推理性能、AI 芯片、编译器的研究生/工程师；系统方向想深入 ML 的人。

## 学习建议

先补 CS 217/CS 149。准备好跑 benchmark，不要只看论文数字。

## 相关课程

- [CS 349D · AI 推理基础设施](cs349d-ai-inference-infrastructure.md)
- [CS 217 · 机器学习硬件加速器](cs217-hardware-accelerators-for-ml.md)
- [CS 229S · 机器学习系统](cs229s-systems-for-machine-learning.md)

## 资源

- [ExploreCourses](https://explorecourses.stanford.edu/search?view=catalog&academicYear=20262027&q=CS+349E)
- [课程官网](https://cs349e.github.io/)

<details>
<summary>官方课程描述（英文原文）</summary>

> A graduate-level course focused on principles and techniques for designing and building large-scale disaggregated AI inference systems. The course explores architectural, algorithmic, system-level, and kernel implementation techniques for serving models with low latency, high throughput, and low cost on heterogeneous machines. Topics include model optimization techniques, distributed serving, AI hardware and performance modelling, kernel programming, and AI compilers. Class website: cs349e.github.io

</details>

---

<sub>信息整理自 Stanford ExploreCourses（2026–27）与课程官网，最后更新 2026-10-30。课程安排、考核比例以官方为准。</sub>
