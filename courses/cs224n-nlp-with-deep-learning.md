# CS 224N · 自然语言处理与深度学习

> NLP 从 word2vec 到 LLM 的核心课：作业实现 word2vec、RNN、注意力，最后做一个 LLM 项目。

| 项目 | 内容 |
| --- | --- |
| **课程编号** | CS 224N<br>同时列于：LINGUIST 284、SYMSYS 195N |
| **英文名称** | Natural Language Processing with Deep Learning (LINGUIST 284, SYMSYS 195N) |
| **学期** | 2027 冬 |
| **学分** | 3–4 |
| **评分** | Letter or Credit/No Credit |
| **授课** | Hashimoto, T.、Yang, D. |
| **先修** | 微积分与线性代数；CS 124、CS 221 或 CS 229 之一。 |
| **难度** | ★★★★☆（主观） |
| **标签** | `NLP` · `LLM` · `DL` · `基础` |

## 课程定位

CS 224N 是 Stanford NLP 的旗舰课，也是很多人进入 LLM 领域的第一站。课程从词表示和语言模型讲起，逐步过渡到 Transformer、预训练、微调和 RLHF，既有数学推导也有大量工程实现。

## 主要内容

- **词表示**：word2vec、GloVe、子词/tokenization
- **语言模型**：n-gram、RNN/LSTM、注意力
- **Transformer**：self-attention、位置编码、架构细节
- **预训练模型**：BERT、GPT、T5、缩放规律
- **适配与对齐**：微调、提示、RLHF、DPO
- **NLP 任务**：句法、语义、问答、机器翻译、信息抽取
- **final project**：通常是 LLM/agent 相关的研究或应用

## 考核与工作量

通常为 4–5 次作业 + 期中 + final project；作业包含大量 PyTorch 实现。具体以当季官网为准。

## 适合谁

NLP/LLM 方向必选；想做 agent、RAG、对齐、多模态语言模型的人；想从传统 NLP 转向 LLM 的工程师。

## 学习建议

先修 CS 229 或至少理解 softmax/交叉熵/反向传播。想深入“从零训练 LLM”，接着上 CS 336。

## 相关课程

- [CS 336 · 从零构建语言模型](cs336-language-modeling-from-scratch.md)
- CS 224U
- [CS 224V · 智能体 AI](cs224v-agentic-ai.md)

## 资源

- [ExploreCourses](https://explorecourses.stanford.edu/search?view=catalog&academicYear=20262027&q=CS+224N)
- [课程官网](https://web.stanford.edu/class/cs224n/)

<details>
<summary>官方课程描述（英文原文）</summary>

> Methods for processing human language information and the underlying computational properties of natural languages. Focus on deep learning approaches: understanding, implementing, training, debugging, visualizing, and extending neural network models for a variety of language understanding tasks. Exploration of natural language tasks ranging from simple word level and syntactic processing to coreference, question answering, and machine translation. Examination of representative papers and systems and completion of a final project applying a complex neural network model to a large-scale NLP problem. Prerequisites: calculus and linear algebra; CS124, CS221, or CS229.

</details>

---

<sub>信息整理自 Stanford ExploreCourses（2026–27）与课程官网，最后更新 2026-10-30。课程安排、考核比例以官方为准。</sub>
