# CS 336 · Language Modeling from Scratch

> Build a language model from scratch: data cleaning, tokenizer, Transformer, training, scaling, evaluation, and deployment.

| Item | Detail |
| --- | --- |
| **Course** | CS 336 |
| **Units** | 3–5 |
| **Terms** | Spring 2027 |
| **Grading** | Letter or Credit/No Credit |
| **Instructors** | Liang, P.; Hashimoto, T. |
| **Prerequisites** | Strong programming; deep learning background (CS 224N/CS 231N/CS 230 level); application required, GPU resources recommended. |
| **Difficulty** | ★★★★★ (subjective) |
| **Tags** | `LLM` · `Pre-training` · `Systems` · `Hard-core` |

## Course positioning

CS 336 is one of the most hard-core LLM courses, taught by Percy Liang and Tatsunori Hashimoto. Inspired by 'build an OS from scratch', it walks through the full language-model lifecycle; the assignments need substantial GPU compute, and enrollment requires an application.

## What it covers

- **Data**: collection, cleaning, deduplication, filtering, mixing
- **Tokenization**: BPE, vocabulary design, multilingual issues
- **Model**: Transformer architecture, attention variants, positional encoding
- **Training**: initialization, optimizers, learning rates, mixed precision, distributed training
- **Scaling**: scaling laws, compute-optimal configurations
- **Evaluation**: perplexity, benchmarks, contamination, alignment evaluation
- **Deployment**: inference, quantization, serving
- **Safety and ethics**: data copyright, bias, misuse

## Assessment & workload

Typically about five programming assignments that build the LM step by step, plus a project; compute-heavy. Check the current syllabus for details.

## Who it's for

People who want to understand the full LLM stack and later work on pre-training/inference/systems; founders building models.

## Study advice

Take CS 224N or CS 231N first. Without GPUs you can run small models, but the assignment experience will be limited.

## Related courses

- [CS 224N · Natural Language Processing with Deep Learning (LINGUIST 284, SYMSYS 195N)](cs224n-nlp-with-deep-learning.md)
- [CS 229S · Systems for Machine Learning](cs229s-systems-for-machine-learning.md)
- [CS 349E · Efficient ML Inference at Scale (EE 339)](cs349e-efficient-ml-inference-at-scale.md)

## Resources

- [ExploreCourses](https://explorecourses.stanford.edu/search?view=catalog&academicYear=20262027&q=CS+336)
- [Course site](https://cs336.stanford.edu/)

<details>
<summary>Official course description</summary>

> Language models serve as the cornerstone of modern natural language processing (NLP) applications and open up a new paradigm of having a single general purpose system address a range of downstream tasks. As the field of artificial intelligence (AI), machine learning (ML), and NLP continues to grow, possessing a deep understanding of language models becomes essential for scientists and engineers alike. This course is designed to provide students with a comprehensive understanding of language models by walking them through the entire process of developing their own. Drawing inspiration from operating systems courses that create an entire operating system from scratch, we will lead students through every aspect of language model creation, including data collection and cleansing for pre-training, transformer model construction, model training, and evaluation before deployment. Application required, apply at http://cs336.stanford.edu/

</details>

---

<sub>Compiled from Stanford ExploreCourses (2026–27) and course sites. Last updated 2026-11-12. Course offerings and grading are subject to the official syllabus.</sub>
