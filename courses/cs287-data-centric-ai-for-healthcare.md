# CS 287 · 医疗 Data-Centric AI

> 医疗 Data-Centric AI：数据怎么产生、偏见/缺失/泄漏怎么毁掉模型，以及怎么修。

| 项目 | 内容 |
| --- | --- |
| **课程编号** | CS 287<br>同时列于：BMDS 218 |
| **英文名称** | Data Centric AI for Healthcare (BMDS 218) |
| **学期** | 2027 冬 |
| **学分** | 3 |
| **评分** | Medical Option (Med-Ltr-CR/NC) |
| **授课** | Alsentzer, E.、Fries, J. |
| **先修** | 机器学习基础；对医疗数据有兴趣。 |
| **难度** | ★★★☆☆（主观） |
| **标签** | `医疗` · `数据` · `Data-Centric` · `鲁棒性` |

> **备注**：2026-27 冬季开设；官网暂未找到稳定链接。

## 课程定位

CS 287 由 Emily Alsentzer、Jason Fries 等讲授，视角和大多数 ML 课相反：不研究模型，而研究数据。课程讨论临床工作流、记录习惯和制度实践如何引入偏差、噪声、缺失和虚假相关，并给出数据质量、标注、合成数据和 drift 监控的实用方法。

## 主要内容

- **数据生成**：临床工作流、文档、制度
- **数据质量**：偏差、噪声、缺失、虚假相关
- **Label leakage**：泄漏检测与避免
- **标注策略**：可扩展、准确的标注
- **合成数据**：隐私、增广、风险
- **Drift 与监控**：数据/模型漂移
- **泛化与鲁棒性**
- **案例与项目**

## 考核与工作量

案例讨论 + 项目/作业。具体以当季官网为准。

## 适合谁

医疗 AI、临床数据科学、数据工程方向；被“模型很好但一上线就崩”困扰的人。

## 学习建议

和 CS 277 互补：277 讲模型，287 讲数据。项目尽量接触真实临床数据流程。

## 相关课程

- [CS 277 · 医疗基础模型](cs277-foundation-models-for-healthcare.md)
- [CS 286 · 计算机视觉与生物医学进阶](cs286-advanced-cv-and-biomedicine.md)
- [CS 229 · 机器学习](cs229-machine-learning.md)

## 资源

- [ExploreCourses](https://explorecourses.stanford.edu/search?view=catalog&academicYear=20262027&q=CS+287)

<details>
<summary>官方课程描述（英文原文）</summary>

> This course explores how healthcare data is generated in practice - and how these processes influence the development of robust, trustworthy machine learning models. Students will examine how clinical workflows, documentation habits, and institutional practices introduce bias, noise, missingness, and spurious correlations into datasets. The course emphasizes the often-overlooked reality that many model failures stem not from algorithmic design, but from subtle flaws in how data is collected, labeled, and interpreted. Through lectures, real-world case studies, and observation of clinical data workflows, students will develop practical tools for understanding and improving data quality and model reliability. Topics include assessing data quality, addressing missingness and label leakage, developing scalable and accurate annotation strategies, leveraging synthetic data, and monitoring data and models for drift over time. Students will also learn to evaluate how these data challenges impact model generalization and robustness.

</details>

---

<sub>信息整理自 Stanford ExploreCourses（2026–27）与课程官网，最后更新 2026-10-30。课程安排、考核比例以官方为准。</sub>
