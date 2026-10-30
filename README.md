# Stanford AI / ML / Agent 课程地图

[![build](https://github.com/logic77lhl/stanford-ai-courses/actions/workflows/build.yml/badge.svg)](https://github.com/logic77lhl/stanford-ai-courses/actions/workflows/build.yml)

> 2026–27 学年 · 55 门核心课程 · 60+ 门延伸课程 · 每门核心课一份中文速览

Stanford 的 AI 课程分散在 CS、EE、STATS、MS&E、CME、AA、PSYCH、SymSys 等院系，编号从 CS 25 到 CS 528，还有大量 1 学分 seminar。这个仓库把它们按方向整理成一张地图：**每门核心课一份 Markdown 速览**，另附完整课程总表、学习路径和延伸课程。

**适合谁**：准备选课的 Stanford 学生；想按 Stanford 课程体系自学的人；想快速了解某个方向（LLM/Agent、CV、机器人、MLSys、AI4Science）课程版图的人。

---

## 仓库结构

```text
.
├── README.md                 # 总表 + 学习路径 + 延伸课程
├── courses/                  # 55 门核心课程，每门一份速览
├── docs/
│   └── learning-paths.md     # 六条学习路径的详细说明
├── data/
│   ├── courses.json          # 机器可读的课程数据
│   ├── catalog.json          # ExploreCourses 原始整理
│   ├── courses/              # 手写源数据（按方向分文件）
│   └── more_courses.json     # 延伸课程清单
└── scripts/
    ├── fetch_catalog.py      # 从 ExploreCourses 抓取
    └── build.py              # 生成 courses/*.md 与 README 表格
```

## 怎么用

1. **先看学习路径**：如果你已经有方向，直接跳到 [学习路径](#学习路径)，按路径选课。
2. **再查总表**：在 [课程总表](#课程总表) 里按方向浏览，点“打开”进入课程页。
3. **最后看课程页**：每页包含定位、主要内容、先修、考核、适合谁、学习建议、相关课程和官方链接。

## 收录说明

- **时间基准**：2026–27 学年，课程信息以 [Stanford ExploreCourses](https://explorecourses.stanford.edu/) 为准。
- **核心 55 门**：以 AI / ML / Agent 为核心方法或核心应用，且有相对完整的公开信息。
- **延伸课程**：相关但更专题、更交叉或 1 学分的 seminar，只在总表列出，暂未单独成文。
- **不含**：纯编程入门、纯数学/统计基础、纯政策/伦理（除非与 AI 技术强相关）。
- **未排课**：部分课程 2026–27 未在 ExploreCourses 排课，课程页会标注，内容按最近一次开设的资料整理。
- **主观评价**：难度星级、学习建议、适合谁均为整理者判断，不是官方说法。

---

## 课程总表

<!-- BEGIN:COURSE_TABLE -->

### 基础核心

| 课程 | 名称 | 学分 | 学期 | 难度 | 速览 |
| --- | --- | --- | --- | --- | --- |
| **CS 221** | 人工智能：原理与技术 | 3–4 | 2026 秋 / 2027 春 | ★★★★☆ | [打开](courses/cs221-artificial-intelligence.md) |
| **CS 224N** | 自然语言处理与深度学习 | 3–4 | 2027 冬 | ★★★★☆ | [打开](courses/cs224n-nlp-with-deep-learning.md) |
| **CS 224W** | 图机器学习 | 3–4 | 2026 秋 | ★★★☆☆ | [打开](courses/cs224w-machine-learning-with-graphs.md) |
| **CS 228** | 概率图模型 | 3–4 | 2026–27 未排课 | ★★★★☆ | [打开](courses/cs228-probabilistic-graphical-models.md) |
| **CS 229** | 机器学习 | 3–4 | 2027 冬 / 2027 春 | ★★★★☆ | [打开](courses/cs229-machine-learning.md) |
| **CS 229M** | 机器学习理论 | 3 | 2026–27 未排课 | ★★★★★ | [打开](courses/cs229m-machine-learning-theory.md) |
| **CS 230** | 深度学习 | 3–4 | 2026 秋 | ★★★☆☆ | [打开](courses/cs230-deep-learning.md) |
| **CS 231N** | 计算机视觉的深度学习 | 3–4 | 2027 春 | ★★★★☆ | [打开](courses/cs231n-deep-learning-for-computer-vision.md) |
| **CS 234** | 强化学习 | 3 | 2026–27 未排课 | ★★★★☆ | [打开](courses/cs234-reinforcement-learning.md) |
| **CS 236** | 深度生成模型 | 3 | 2027 春 | ★★★★☆ | [打开](courses/cs236-deep-generative-models.md) |

### LLM 与 Agent

| 课程 | 名称 | 学分 | 学期 | 难度 | 速览 |
| --- | --- | --- | --- | --- | --- |
| **CS 221M** | 机制可解释性 | 3 | 2027 春 | ★★★★☆ | [打开](courses/cs221m-mechanistic-interpretability.md) |
| **CS 222** | AI Agent 与社会模拟 | 3–4 | 2027 冬 | ★★★☆☆ | [打开](courses/cs222-ai-agents-and-simulations.md) |
| **CS 224G** | LLM 应用开发 | 3–4 | 2027 冬 | ★★★☆☆ | [打开](courses/cs224g-apps-with-llms-inside.md) |
| **CS 224V** | 智能体 AI | 3–4 | 2026 秋 | ★★★★☆ | [打开](courses/cs224v-agentic-ai.md) |
| **CS 25** | Transformers United | 1 | 2026–27 未排课 | ★☆☆☆☆ | [打开](courses/cs25-transformers-united.md) |
| **CS 324** | 基础模型进展 | 3 | 2026–27 未排课 | ★★★☆☆ | [打开](courses/cs324-advances-in-foundation-models.md) |
| **CS 329A** | 自我改进的 AI Agent | 3 | 2027 春 | ★★★★☆ | [打开](courses/cs329a-self-improving-ai-agents.md) |
| **CS 329H** | 从人类偏好中学习 | 3 | 2026 秋 | ★★★★☆ | [打开](courses/cs329h-machine-learning-from-human-preferences.md) |
| **CS 329T** | 可信机器学习：构建与评估 Agent 系统 | 3 | 2026–27 未排课 | ★★★☆☆ | [打开](courses/cs329t-trustworthy-machine-learning.md) |
| **CS 329Z** | AI Agent 工程 | 3 | 2026 秋 | ★★★★☆ | [打开](courses/cs329z-engineering-ai-agents.md) |
| **CS 336** | 从零构建语言模型 | 3–5 | 2027 春 | ★★★★★ | [打开](courses/cs336-language-modeling-from-scratch.md) |
| **CS 372** | AGI 的推理、规划与决策 | 3 | 2027 冬 | ★★★★☆ | [打开](courses/cs372-agi-reasoning-planning.md) |

### ML 系统与硬件

| 课程 | 名称 | 学分 | 学期 | 难度 | 速览 |
| --- | --- | --- | --- | --- | --- |
| **CS 217** | 机器学习硬件加速器 | 3–4 | 2027 春 | ★★★★☆ | [打开](courses/cs217-hardware-accelerators-for-ml.md) |
| **CS 229S** | 机器学习系统 | 3 | 2026–27 未排课 | ★★★★☆ | [打开](courses/cs229s-systems-for-machine-learning.md) |
| **CS 329S** | 机器学习系统设计 | 3–4 | 2026–27 未排课 | ★★★☆☆ | [打开](courses/cs329s-machine-learning-systems-design.md) |
| **CS 349D** | AI 推理基础设施 | 3 | 2027 春 | ★★★★☆ | [打开](courses/cs349d-ai-inference-infrastructure.md) |
| **CS 349E** | 大规模高效 ML 推理 | 3 | 2026 秋 | ★★★★★ | [打开](courses/cs349e-efficient-ml-inference-at-scale.md) |
| **CS 349F** | AI 系统的网络 Fabric 架构 | 2 | 2026 秋 | ★★★★☆ | [打开](courses/cs349f-fabric-architectures-for-ai-systems.md) |

### 视觉、图形与生成

| 课程 | 名称 | 学分 | 学期 | 难度 | 速览 |
| --- | --- | --- | --- | --- | --- |
| **CS 231A** | 计算机视觉：从 3D 感知到重建 | 3–4 | 2026–27 未排课 | ★★★★☆ | [打开](courses/cs231a-computer-vision-3d.md) |
| **CS 236G** | 生成对抗网络 | 3 | 2026–27 未排课 | ★★★☆☆ | [打开](courses/cs236g-generative-adversarial-networks.md) |
| **CS 348I** | AI 时代的计算机图形学 | 3–4 | 2026–27 未排课 | ★★★★☆ | [打开](courses/cs348i-computer-graphics-in-the-era-of-ai.md) |
| **CS 348N** | 3D 几何的神经模型 | 3 | 2026–27 未排课 | ★★★★☆ | [打开](courses/cs348n-neural-models-for-3d-geometry.md) |
| **CS 448I** | 计算成像 | 3 | 2027 冬 | ★★★★☆ | [打开](courses/cs448i-computational-imaging.md) |
| **CS 468** | 几何计算专题：3D/4D 基础模型 | 3 | 2026–27 未排课 | ★★★★☆ | [打开](courses/cs468-topics-in-geometric-computing.md) |

### 机器人、具身智能

| 课程 | 名称 | 学分 | 学期 | 难度 | 速览 |
| --- | --- | --- | --- | --- | --- |
| **CS 223A** | 机器人学导论 | 3 | 2027 冬 | ★★★★☆ | [打开](courses/cs223a-introduction-to-robotics.md) |
| **CS 225A** | 实验机器人学 | 3 | 2027 春 | ★★★★☆ | [打开](courses/cs225a-experimental-robotics.md) |
| **CS 227A** | 机器人感知 | 3–4 | 2026 秋 | ★★★★☆ | [打开](courses/cs227a-robot-perception.md) |
| **CS 237A** | 机器人自主性原理 I | 3 | 2026 秋 | ★★★★☆ | [打开](courses/cs237a-principles-of-robot-autonomy-i.md) |
| **CS 237B** | 机器人自主性原理 II | 3–4 | 2026–27 未排课 | ★★★★☆ | [打开](courses/cs237b-principles-of-robot-autonomy-ii.md) |
| **CS 381** | 具身智能的感知运动学习 | 3 | 2027 冬 | ★★★★★ | [打开](courses/cs381-sensorimotor-learning-for-embodied-agents.md) |

### AI for Science 与医疗

| 课程 | 名称 | 学分 | 学期 | 难度 | 速览 |
| --- | --- | --- | --- | --- | --- |
| **CS 273B** | 基因组与生物医学中的深度学习 | 3 | 2027 春 | ★★★★☆ | [打开](courses/cs273b-deep-learning-in-genomics.md) |
| **CS 277** | 医疗基础模型 | 3 | 2027 冬 | ★★★☆☆ | [打开](courses/cs277-foundation-models-for-healthcare.md) |
| **CS 279** | 计算生物学：生物分子与细胞的结构和组织 | 3 | 2026 秋 | ★★★★☆ | [打开](courses/cs279-computational-biology.md) |
| **CS 286** | 计算机视觉与生物医学进阶 | 3 | 2026 秋 | ★★★★☆ | [打开](courses/cs286-advanced-cv-and-biomedicine.md) |
| **CS 287** | 医疗 Data-Centric AI | 3 | 2027 冬 | ★★★☆☆ | [打开](courses/cs287-data-centric-ai-for-healthcare.md) |
| **CS 375** | 面向神经科学的大规模神经网络建模 | 3 | 2027 冬 | ★★★★☆ | [打开](courses/cs375-large-scale-neural-network-modeling-for-neuroscience.md) |
| **EE 292R** | AI 与数据驱动的科学 | 1 | 2026 秋 / 2027 冬 / 2027 春 | ★☆☆☆☆ | [打开](courses/ee292r-ai-and-data-for-science.md) |

### 产品、伦理与设计

| 课程 | 名称 | 学分 | 学期 | 难度 | 速览 |
| --- | --- | --- | --- | --- | --- |
| **CS 139** | 人本 AI | 3 | 2027 冬 | ★★☆☆☆ | [打开](courses/cs139-human-centered-ai.md) |
| **CS 247A** | 为人工智能而设计 | 3–4 | 2026–27 未排课 | ★★★☆☆ | [打开](courses/cs247a-design-for-artificial-intelligence.md) |
| **CS 281** | 人工智能伦理 | 3–4 | 2026–27 未排课 | ★★★☆☆ | [打开](courses/cs281-ethics-of-artificial-intelligence.md) |
| **MS&E 203** | 构建与评估 AI 产品 | 3 | 2026 秋 | ★★★☆☆ | [打开](courses/mse203-building-and-evaluating-ai-products.md) |

### 统计与优化

| 课程 | 名称 | 学分 | 学期 | 难度 | 速览 |
| --- | --- | --- | --- | --- | --- |
| **MS&E 318** | 安全与受约束的 AI | 3 | 2026–27 未排课 | ★★★★★ | [打开](courses/mse318-safe-and-constrained-ai.md) |
| **MS&E 319** | 高效生成模型 | 3 | 2026 秋 | ★★★★☆ | [打开](courses/mse319-efficient-generative-models.md) |
| **STATS 202** | 统计学习与数据科学 | 3 | 2027 冬 / 2027 春 | ★★★☆☆ | [打开](courses/stats202-statistical-learning-and-data-science.md) |
| **STATS 315A** | 现代应用统计：学习 | 3 | 2027 冬 | ★★★★☆ | [打开](courses/stats315a-modern-applied-statistics-learning.md) |

<!-- END:COURSE_TABLE -->

---

## 学习路径

| 路径 | 推荐顺序 | 适合 |
| --- | --- | --- |
| **LLM / Agent 工程** | CS 224N → CS 329Z → CS 224V / CS 329A → CS 336 | 想做 AI engineer、agent 产品、LLM 应用 |
| **ML 研究** | CS 229 → CS 229M / STATS 315A → CS 236 / CS 234 → 研究项目 | 想读博、做 ML theory/生成模型/RL |
| **CV / 生成** | CS 231N → CS 236 → CS 348N / CS 348I → CS 468 | 想做视觉、3D 生成、图形 |
| **机器人 / 具身** | CS 223A → CS 237A → CS 237B / CS 227A → CS 381 | 想做机器人、具身智能、自动驾驶 |
| **MLSys / 推理** | CS 229S / CS 329S → CS 349D / CS 349E → CS 217 | 想做训练/推理基础设施、AI 芯片 |
| **AI4Science / 医疗** | CS 229 → CS 273B / CS 279 → CS 277 / CS 287 → EE 292R | 想做计算生物、医疗 AI、科学发现 |

更详细的先修关系、每学期建议和“避坑”说明见 [docs/learning-paths.md](docs/learning-paths.md)。

---

## 延伸课程

以下课程与 AI/ML/Agent 相关，但更专题、更交叉或为 1 学分 seminar，暂未单独成文。课程名与学期来自 ExploreCourses。

<!-- BEGIN:MORE_TABLE -->

| 课程 | 名称 | 学分 | 学期 | 方向/备注 |
| --- | --- | --- | --- | --- |
| **CS 120** | Introduction to AI Safety | 3 | 2026 秋 | AI 安全入门 |
| **CS 121** | Equity and Governance for Artificial Intelligence | 4 | 2027 冬 | AI 公平与治理 |
| **CS 123** | A Hands-On Introduction to Building AI-Enabled Robots | 3 | 2026 秋 | 动手做 AI 机器人 |
| **CS 129** | Applied Machine Learning | 3–4 | 2027 春 | 应用机器学习 |
| **CS 131** | Computer Vision: Foundations and Applications | 3–4 | 2027 冬 | 计算机视觉基础 |
| **CS 224C** | NLP for Computational Social Science | 3 | 2026–27 未排课 | NLP × 计算社会科学 |
| **CS 224R** | Deep Reinforcement Learning | 3 | 2026–27 未排课 | 深度强化学习 |
| **CS 224S** | Spoken Language Processing (LINGUIST 285) | 2–4 | 2026–27 未排课 | 语音处理 |
| **CS 224U** | Natural Language Understanding (LINGUIST 188, LINGUIST 288, SYMSYS 195U) | 3–4 | 2026–27 未排课 | 自然语言理解 |
| **CS 225** | Machine Learning for Discrete Optimization (MS&E 236) | 3 | 2026–27 未排课 | ML × 离散优化 |
| **CS 229B** | Machine Learning for Sequence Modeling (STATS 232) | 3–4 | 2026–27 未排课 | 序列建模 |
| **CS 238** | Decision Making under Uncertainty (AA 228) | 3–4 | 2026 秋 | 不确定性下的决策 |
| **CS 239** | Advanced Topics in Sequential Decision Making (AA 229) | 3–4 | 2027 冬 | 序列决策进阶 |
| **CS 246** | Mining Massive Data Sets | 3–4 | 2027 冬 | 大规模数据挖掘 |
| **CS 253** | Securing AI Systems | 3 | 2027 春 | AI 系统安全 |
| **CS 256** | Algorithmic Fairness | 3 | 2027 春 | 算法公平 |
| **CS 270** | Modeling Biomedical Systems (BMDS 210) | 3 | 2027 春 | 生物医学系统建模 |
| **CS 271** | Algorithmic Foundations for Artificial Intelligence in Healthcare (BMDS 270) | 3–4 | 2026–27 未排课 | 医疗 AI 算法基础 |
| **CS 293** | Empowering Educators via Language Technology (EDUC 473) | 2–4 | 2026–27 未排课 | 语言技术 × 教育 |
| **CS 312** | Deep Learning Alchemy | 3–5 | 2026 秋 | 深度学习炼金术 |
| **CS 321M** | AI Measurement Science | 3 | 2027 春 | AI 测量科学 |
| **CS 322** | Triangulating Intelligence: Melding Neuroscience, Psychology, and AI (PSYCH 225) | 3 | 2026–27 未排课 | 神经科学 × AI |
| **CS 323** | The AI Awakening: Implications for the Economy and Society | 3–4 | 2027 春 | AI 经济与社会 |
| **CS 328** | Foundations of Causal Machine Learning | 3 | 2027 冬 | 因果机器学习 |
| **CS 329D** | Machine Learning Under Distributional Shifts | 3 | 2026–27 未排课 | 分布偏移下的 ML |
| **CS 329E** | Machine Learning on Embedded Systems (EE 292D) | 3 | 2026–27 未排课 | 嵌入式 ML |
| **CS 329M** | Machine Programming | 3–4 | 2026 秋 | Machine Programming |
| **CS 329P** | Practical Machine Learning | 3–4 | 2026–27 未排课 | 实用机器学习 |
| **CS 329X** | Human Centered NLP (CS 129X) | 3 | 2026 秋 | 人本 NLP |
| **CS 330** | Deep Multi-task and Meta Learning | 3 | 2026–27 未排课 | 多任务与元学习 |
| **CS 331X** | AI for Algorithmic Reasoning and Optimization (MS&E 331) | 3 | 2026–27 未排课 | AI × 算法优化 |
| **CS 332** | Advanced Survey of Reinforcement Learning | 3 | 2026–27 未排课 | 高级强化学习 |
| **CS 333** | Algorithms for Interactive Robotics | 3–4 | 2026–27 未排课 | 交互机器人算法 |
| **CS 338** | Aligning Superintelligence (MS&E 338) | 3 | 2027 春 | 对齐超级智能 |
| **CS 339N** | Machine Learning Methods for Neural Data Analysis (NBIO 220, STATS 220, STATS 320) | 3 | 2026–27 未排课 | 神经数据 ML |
| **CS 339R** | Collaborative Robotics (ME 326) | 3 | 2027 冬 | 协作机器人 |
| **CS 345** | Building AI-Enabled Robots | 3 | 2026–27 未排课 | 构建 AI 机器人 |
| **CS 348K** | Visual Computing Systems | 3–4 | 2027 春 | 视觉计算系统 |
| **CS 349H** | Software Techniques for Emerging Hardware Platforms (EE 349) | 3 | 2026 秋 | 新硬件软件技术 |
| **CS 362** | Research in AI Alignment | 3 | 2026–27 未排课 | AI 对齐研究 |
| **CS 384** | Seminar on Ethical and Social Issues in Natural Language Processing (LINGUIST 287) | 3–4 | 2026–27 未排课 | NLP 伦理 seminar |
| **CS 470** | Music and AI (MUSIC 356) | 3–4 | 2026–27 未排课 | 音乐与 AI |
| **CS 521** | Seminar on AI Safety | 1 | 2026–27 未排课 | AI 安全 seminar |
| **CS 522** | Seminar in Artificial Intelligence in Healthcare | 1 | 2026 秋 | 医疗 AI seminar |
| **CS 523** | Research Seminar in Computer Vision + X | 1–2 | 2026–27 未排课 | CV + X seminar |
| **CS 524** | AI for Science | 3 | 2026–27 未排课 | AI for Science |
| **CS 525** | Data for AI | 3 | 2026–27 未排课 | Data for AI |
| **CS 528** | Machine Learning Systems Seminar | 1 | 2026–27 未排课 | ML 系统 seminar |
| **EE 205** | Product Management for Engineers in the AI Age | 3 | 2027 冬 | AI 时代产品管理 |
| **EE 292M** | AI-Augmented Research and Development: Foundations and Practice | 3 | 2026 秋 | AI 增强研发 |
| **STATS 220** | Machine Learning Methods for Neural Data Analysis (CS 339N, NBIO 220, STATS 320) | 3 | 2026–27 未排课 | 神经数据 ML |
| **STATS 292** | Statistical Models of Text and Language | 3 | 2027 春 | 文本统计模型 |
| **STATS 326** | Topics in Generative Modeling Methods in Protein Modeling and Design | 3 | 2026–27 未排课 | 蛋白生成模型 |
| **STATS 357** | Reliability and Validity in Artificial Intelligence (MS&E 330) | 3 | 2027 冬 | AI 可靠性 |
| **MS&E 226** | Fundamentals of Data Science: Prediction, Inference, Causality | 3 | 2026 秋 | 数据科学基础 |
| **MS&E 228** | Applied Causal Inference with Machine Learning and AI (CS 288) | 3 | 2027 冬 | 因果推断 × ML |
| **MS&E 235A** | Markov Decision Processes (EE 283) | 3 | 2026 秋 | 马尔可夫决策过程 |
| **MS&E 235B** | Reinforcement Learning: Behaviors and Applications (EE 383) | 3 | 2026–27 未排课 | 强化学习 |
| **MS&E 328** | Foundations of Causal Machine Learning | 3 | 2027 冬 | 因果 ML 基础 |
| **MS&E 330** | Reliability and Validity in Artificial Intelligence (STATS 357) | 3 | 2027 冬 | AI 可靠性 |
| **MS&E 338** | Aligning Superintelligence (CS 338) | 3 | 2027 春 | 对齐超级智能 |
| **MS&E 346** | Foundations of Reinforcement Learning with Applications in Finance (CME 241) | 3 | 2027 冬 | RL × 金融 |
| **MS&E 446** | Artificial Intelligence in Financial Technology | 3 | 2026–27 未排课 | AI × 金融科技 |
| **CME 216** | Machine Learning for Computational Engineering. (ME 343) | 3 | 2026–27 未排课 | ML × 计算工程 |
| **PSYCH 209** | Neural Network Models of Cognition | 4 | 2026–27 未排课 | 认知的神经网络模型 |
| **PSYCH 239** | Do Language Models Have Mental States | 3 | 2027 春 | LLM 有心理状态吗 |
| **PSYCH 242** | A modern explainable AI approach to Theoretical Neuroscience (APPPHYS 293) | 3 | 2026–27 未排课 | 可解释 AI × 理论神经 |
| **SYMSYS 122** | The Social & Economic Impact of Artificial Intelligence (CS 22A, INTLPOL 200) | 1 | 2027 冬 | AI 社会经济影响 |
| **SYMSYS 123** | Neuroscience and Artificial Intelligence | 3–4 | 2026–27 未排课 | 神经科学 × AI |
| **EDUC 246I** | AI and Education: Foundations, Opportunities, Challenges, and Considerations | 1 | 2026 秋 | AI 与教育 |

<!-- END:MORE_TABLE -->

---

## 数据与构建

```bash
# 1. 抓取 ExploreCourses（带本地缓存，可重复运行）
python scripts/fetch_catalog.py

# 2. 生成课程页和 README 表格
python scripts/build.py
```

要求 Python 3.10+，无第三方依赖。`courses/*.md` 是生成文件，请修改 `data/courses/*.json` 后重新构建。

## 贡献

欢迎提 PR 补充课程、修正信息或改进课程页：

1. 在 `data/courses/` 对应方向文件里新增/修改条目（字段参考现有条目）。
2. 运行 `python scripts/build.py` 重新生成。
3. 提交 `data/`、`courses/` 和 `README.md` 的改动。

新增课程时请尽量附上官方来源（ExploreCourses 或课程官网），并把不确定的信息写进 `note`。

## 免责声明

这是一个非官方整理项目，与 Stanford University 无关。课程名称、学期、学分、教师和考核方式都可能变化，选课前请以 [ExploreCourses](https://explorecourses.stanford.edu/) 和课程官网为准。课程页中的难度、学习建议和“适合谁”是整理者的主观判断，不构成选课建议。

## License

- 文字内容：[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- 代码：[MIT](LICENSE)

课程描述与课程名称的版权归 Stanford University 及各课程教师所有，本仓库仅作信息整理与引用。
