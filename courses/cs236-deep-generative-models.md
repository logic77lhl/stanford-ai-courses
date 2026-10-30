# CS 236 · 深度生成模型

> 深度生成模型的理论课：VAE、GAN、flow、diffusion 的概率基础与训练算法。

| 项目 | 内容 |
| --- | --- |
| **课程编号** | CS 236 |
| **英文名称** | Deep Generative Models |
| **学期** | 2027 春 |
| **学分** | 3 |
| **评分** | Letter or Credit/No Credit |
| **授课** | Ermon, S. |
| **先修** | CS 221/228/229/230 至少一门；概率与微积分；Python 编程。 |
| **难度** | ★★★★☆（主观） |
| **标签** | `生成模型` · `Diffusion` · `概率` |

## 课程定位

CS 236 是生成模型方向最系统的课程之一，由 Stefano Ermon 讲授。它从概率建模和变分推断出发，覆盖 VAE、GAN、normalizing flow、energy-based model、diffusion/score matching，数学要求较高。

## 主要内容

- **概率基础**：极大似然、变分推断、ELBO、MCMC
- **VAE**：重参数化、后验坍塌、层次化 VAE
- **GAN**：对抗训练、模式崩溃、Wasserstein GAN
- **Flow 模型**：可逆变换、Jacobian、连续流
- **Energy-based 模型**：对比散度、score matching
- **Diffusion**：DDPM、score-based、classifier-free guidance
- **应用**：图像、文本、语音、RL
- **项目**：生成模型的研究或应用

## 考核与工作量

作业 + 期中/期末 + 项目；数学推导和实现并重。具体以当季官网为准。

## 适合谁

想做扩散模型、图像/视频生成、生成式 AI 研究的人；想理解 VAE/GAN 背后概率原理的人。

## 学习建议

先补变分推断和 score matching，否则 diffusion 部分会很吃力。配合 CS 236G 可以补 GAN 的工程细节。

## 相关课程

- [CS 236G · 生成对抗网络](cs236g-generative-adversarial-networks.md)
- [CS 229 · 机器学习](cs229-machine-learning.md)
- [CS 224N · 自然语言处理与深度学习](cs224n-nlp-with-deep-learning.md)

## 资源

- [ExploreCourses](https://explorecourses.stanford.edu/search?view=catalog&academicYear=20262027&q=CS+236)
- [课程官网](https://deepgenerativemodels.github.io/)

<details>
<summary>官方课程描述（英文原文）</summary>

> Generative models are widely used in many subfields of AI and Machine Learning. Recent advances in parameterizing these models using neural networks, combined with progress in stochastic optimization methods, have enabled scalable modeling of complex, high-dimensional data including images, text, and speech. In this course, we will study the probabilistic foundations and learning algorithms for deep generative models, including Variational Autoencoders (VAE), Generative Adversarial Networks (GAN), and flow models. The course will also discuss application areas that have benefitted from deep generative models, including computer vision, speech and natural language processing, and reinforcement learning. Prerequisites: Basic knowledge about machine learning from at least one of CS 221, 228, 229 or 230. Students will work with computational and mathematical models and should have a basic knowledge of probabilities and calculus. Proficiency in some programming language, preferably Python, required.

</details>

---

<sub>信息整理自 Stanford ExploreCourses（2026–27）与课程官网，最后更新 2026-10-30。课程安排、考核比例以官方为准。</sub>
