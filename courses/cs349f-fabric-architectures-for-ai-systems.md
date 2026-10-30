# CS 349F · AI 系统的网络 Fabric 架构

> AI 集群的网络 fabric：fat tree、拥塞控制、调度，追求超低延迟和近 100% goodput。

| 项目 | 内容 |
| --- | --- |
| **课程编号** | CS 349F |
| **英文名称** | Fabric Architectures For AI Systems |
| **学期** | 2026 秋 |
| **学分** | 2 |
| **评分** | Satisfactory/No Credit |
| **授课** | Prabhakar, B.、Rosenblum, M. |
| **先修** | CS 144/CS 140 或分布式系统基础；EE 178 有帮助。 |
| **难度** | ★★★★☆（主观） |
| **标签** | `网络` · `集群` · `数据中心` · `系统` |

> **备注**：2026-27 秋季开设；官网访问受限，暂只提供 ExploreCourses 链接。

## 课程定位

CS 349F 关注大规模 GPU/CPU 集群的互连网络，以及金融交易、多人游戏等 time-sensitive 系统。课程覆盖数据中心 fabric 架构、传输协议、拥塞控制、负载均衡和调度，并邀请工业界专家讲真实集群的设计与运维。

## 主要内容

- **数据中心 fabric**：fat tree、leaf-spine、拓扑
- **传输协议**：RDMA、RoCE、拥塞控制
- **负载均衡**：ECMP、packet spraying
- **调度**：作业调度、fabric 调度、交互
- **边缘 vs 网络中心**：两种高性能路线
- **工业案例**：GPU 集群、交易系统

## 考核与工作量

2 unit S/NC；讨论 + 项目/案例，具体以当季官网为准。

## 适合谁

网络、集群、数据中心方向；想做 AI 基础设施的人。

## 学习建议

和 CS 349D/E 一起看，形成“单机-集群-网络”的完整视角。

## 相关课程

- [CS 349D · AI 推理基础设施](cs349d-ai-inference-infrastructure.md)
- [CS 349E · 大规模高效 ML 推理](cs349e-efficient-ml-inference-at-scale.md)
- CS 144

## 资源

- [ExploreCourses](https://explorecourses.stanford.edu/search?view=catalog&academicYear=20262027&q=CS+349F)

<details>
<summary>官方课程描述（英文原文）</summary>

> The course is concerned with the design and operation of the network fabrics which interconnect large-scale compute and storage nodes in modern AI GPU clusters, cloud computing systems, and &quot;time-sensitive systems&quot; like financial trading platforms and massive multi-player games. We will consider architectures, protocols and algorithms which enable these network fabrics to deliver deterministic and ultra-low latency at near-100% goodput. Topics include data center fabric architectures - the fat tree topology, transport protocols - congestion control and load balancing, and scheduling algorithms - job scheduling, fabric scheduling and their interaction. A particular focus will be the contrast and synergy between the edge- and network-centric approaches to building high-performance network fabrics. Students will hear from industry experts who design, operate and use large-scale GPU and CPU clusters. Recommended: Knowledge of basic Networking, OS, or Distributed Systems (CS 144, 140, or equivalent), as well as basic EE courses (EE 178) will be useful.

</details>

---

<sub>信息整理自 Stanford ExploreCourses（2026–27）与课程官网，最后更新 2026-10-30。课程安排、考核比例以官方为准。</sub>
