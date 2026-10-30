# CS 229S · 机器学习系统

> ML 系统：数据准备、训练、部署推理全栈的效率优化，软硬件协同。

| 项目 | 内容 |
| --- | --- |
| **课程编号** | CS 229S |
| **英文名称** | Systems for Machine Learning |
| **学期** | 2026–27 未排课 |
| **学分** | 3 |
| **评分** | Letter or Credit/No Credit |
| **授课** | TBA |
| **先修** | CS 224N 或 CS 229；系统/体系结构基础有帮助。 |
| **难度** | ★★★★☆（主观） |
| **标签** | `MLSys` · `系统` · `分布式` · `性能` |

> **备注**：2026-27 学年未在 ExploreCourses 排课；课程官网暂未找到稳定链接。

## 课程定位

CS 229S 从系统视角讲机器学习：模型越来越大、数据越来越多、硬件越来越异构，性能瓶颈到底在哪。课程覆盖数据 pipeline、分布式训练、GPU/加速器、网络、推理 serving 和编译，适合想去做 MLSys/基础设施的人。

## 主要内容

- **数据 pipeline**：采集、清洗、存储、吞吐
- **分布式训练**：数据并行、模型并行、流水线并行
- **加速器**：GPU/TPU、内存层次、互联
- **通信与网络**：all-reduce、RDMA、拓扑
- **推理 serving**：批处理、调度、KV cache、延迟
- **编译与算子**：XLA、TVM、Triton
- **案例与项目**：真实系统的性能分析

## 考核与工作量

作业 + 项目，偏系统实现与性能分析。具体以当季官网为准。

## 适合谁

想做 MLSys、推理基础设施、训练平台的人；系统背景想转 ML 的人。

## 学习建议

配合 CS 149（并行计算）和 CS 217（加速器）。先理解 roofline 模型和通信开销。

## 相关课程

- [CS 329S · 机器学习系统设计](cs329s-machine-learning-systems-design.md)
- [CS 349D · AI 推理基础设施](cs349d-ai-inference-infrastructure.md)
- [CS 217 · 机器学习硬件加速器](cs217-hardware-accelerators-for-ml.md)

## 资源

- [ExploreCourses](https://explorecourses.stanford.edu/search?view=catalog&academicYear=20262027&q=CS+229S)
- [课程官网](https://cs229s.stanford.edu/)

<details>
<summary>官方课程描述（英文原文）</summary>

> Deep learning and neural networks are being increasingly adopted across industries. They are now used to serve billions of users across applications such as search, knowledge discovery, and productivity assistants. As models become more capable and intelligent, this trend of large-scale adoption will continue to grow rapidly. Due to the widespread application, there is an increasing need to achieve high performance for both training and serving deep-learning models. However, performance is hindered by a multitude of infrastructure and lifecycle hurdles - the increasing complexity of the models, massive sizes of training and inference data, heterogeneity of the available accelerators and multi-node platforms, and diverse network properties. The slow adaptation of systems to new algorithms creates a bottleneck for the rapid evolution of deep-learning models and their applications. This course will cover systems approaches for improving the efficiency of machine learning pipelines - comprising data preparation, model training, and model deployment &amp; inference -at each level of the systems stack spanning software and hardware. Pre-req: CS224N or CS229.

</details>

---

<sub>信息整理自 Stanford ExploreCourses（2026–27）与课程官网，最后更新 2026-10-30。课程安排、考核比例以官方为准。</sub>
