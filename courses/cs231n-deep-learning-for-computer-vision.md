# CS 231N · 计算机视觉的深度学习

> CV 领域最有名的深度学习课：从 kNN 到 Transformer，作业是自己手写反向传播并训练 CNN。

| 项目 | 内容 |
| --- | --- |
| **课程编号** | CS 231N |
| **英文名称** | Deep Learning for Computer Vision |
| **学期** | 2027 春 |
| **学分** | 3–4 |
| **评分** | Letter or Credit/No Credit |
| **授课** | Li, F.、Adeli, E. |
| **先修** | 熟练 Python/NumPy；微积分与线性代数（MATH 19/51）；概率统计基础（CS 109 级）。 |
| **难度** | ★★★★☆（主观） |
| **标签** | `CV` · `DL` · `视觉` · `项目` |

## 课程定位

CS 231N 是视觉识别方向的标准入口，强调 implement、train、debug 的完整闭环。它的作业设计（A1–A3 + final project）被大量课程借鉴，也是很多人真正“第一次把神经网络跑起来”的地方。

## 主要内容

- **图像分类**：kNN、线性分类器、损失函数与优化
- **神经网络**：反向传播、多层网络、激活函数
- **CNN 架构**：AlexNet、VGG、ResNet、高效网络
- **训练工程**：初始化、归一化、正则化、学习率、数据增强
- **可视化与可解释性**：显著图、特征可视化、对抗样本
- **检测/分割**：R-CNN 系列、YOLO、语义/实例分割
- **前沿**：视频、生成模型、多模态、Transformer
- **final project**：通常做真实视觉任务

## 考核与工作量

3 个编程作业 + final project；作业量较大但非常值。具体以当季官网为准。

## 适合谁

想做 CV、多模态、机器人感知、自动驾驶的人；想补“深度学习底层实现”能力的工程师；准备读视觉方向博士的人。

## 学习建议

A2 的 BatchNorm 和 A3 的 Transformer 建议手写，不要抄。final project 不要只刷 SOTA，做一个能讲清楚 error analysis 的小问题更加分。

## 相关课程

- [CS 230 · 深度学习](cs230-deep-learning.md)
- [CS 231A · 计算机视觉：从 3D 感知到重建](cs231a-computer-vision-3d.md)
- [CS 224N · 自然语言处理与深度学习](cs224n-nlp-with-deep-learning.md)

## 资源

- [ExploreCourses](https://explorecourses.stanford.edu/search?view=catalog&academicYear=20262027&q=CS+231N)
- [课程官网](https://cs231n.stanford.edu/)

<details>
<summary>官方课程描述（英文原文）</summary>

> Computer Vision has become ubiquitous in our society, with applications in search, image understanding, apps, mapping, medicine, drones, and self-driving cars. Core to many of these applications are visual recognition tasks such as image classification and object detection. Recent developments in neural network approaches have greatly advanced the performance of these state-of-the-art visual recognition systems. This course is a deep dive into details of neural-network based deep learning methods for computer vision. During this course, students will learn to implement, train and debug their own neural networks and gain a detailed understanding of cutting-edge research in computer vision. We will cover learning algorithms, neural network architectures, and practical engineering tricks for training and fine-tuning networks for visual recognition tasks.Prerequisites: Proficiency in Python - All class assignments will be in Python (and use numpy) (we provide a tutorial here for those who aren't as familiar with Python). If you have a lot of programming experience but in a different language (e.g. C/C++/Matlab/Javascript) you will probably be fine.College Calculus, Linear Algebra (e.g. MATH 19, MATH 51) -You should be comfortable taking derivatives and understanding matrix vector operations and notation. Basic Probability and Statistics (e.g. CS 109 or other stats course) -You should know basics of probabilities, gaussian distributions, mean, standard deviation, etc.

</details>

---

<sub>信息整理自 Stanford ExploreCourses（2026–27）与课程官网，最后更新 2026-10-30。课程安排、考核比例以官方为准。</sub>
