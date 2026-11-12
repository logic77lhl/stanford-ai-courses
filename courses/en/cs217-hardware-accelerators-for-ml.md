# CS 217 · Hardware Accelerators for Machine Learning (EE 244)

> ML hardware accelerators: dataflow, tensor processing, memory hierarchy, compilation, and mapping CNNs/Transformers.

| Item | Detail |
| --- | --- |
| **Course** | CS 217<br>Cross-listed: EE 244 |
| **Units** | 3–4 |
| **Terms** | Spring 2027 |
| **Grading** | Letter or Credit/No Credit |
| **Instructors** | Olukotun, O.; Tambe, T. |
| **Prerequisites** | Digital circuits/computer architecture; VLSI or FPGA experience helps. |
| **Difficulty** | ★★★★☆ (subjective) |
| **Tags** | `Hardware` · `Accelerators` · `Architecture` · `Chips` |

## Course positioning

CS 217 (EE 244) is taught by Olukotun and Tambe and is a classic course on AI chips. It starts from the compute patterns of CNNs/Transformers and covers accelerator architecture, dataflow, memory hierarchy, low precision/sparsity, and compilation, ending with a design project.

## What it covers

- **AI compute patterns**: CNNs, Transformers, training vs inference
- **Accelerator architecture**: systolic arrays, tensor cores, dataflow
- **Memory hierarchy**: on-chip buffers, HBM, data reuse
- **Low precision and sparsity**: quantization, pruning, compression
- **Compilation and mapping**: operator scheduling, tiling
- **Energy and area**: system-level trade-offs
- **Design project**

## Assessment & workload

Paper reading plus a final design project. Check the current syllabus for details.

## Who it's for

People who want to work on AI chips, accelerators, or architecture; hardware people who want to understand ML workloads.

## Study advice

Understand roofline and matrix-multiply tiling first. Pair with CS 149/CS 349E.

## Related courses

- [CS 349E · Efficient ML Inference at Scale (EE 339)](cs349e-efficient-ml-inference-at-scale.md)
- EE 244
- CS 149

## Resources

- [ExploreCourses](https://explorecourses.stanford.edu/search?view=catalog&academicYear=20262027&q=CS+217)
- [Course site](https://cs217.stanford.edu/)

<details>
<summary>Official course description</summary>

> This course explores the design, programming, and performance of modern AI accelerators. It covers architectural techniques, dataflow, tensor processing, memory hierarchies, compilation for accelerators, and emerging trends in AI computing. This course will cover modern AI/ML algorithms such as convolutional neural nets, and Transformer-based models / LLMs. We will consider both training and inference for these models and discuss the impact of parameters such as batch size, precision, sparsity and compression on the accuracy of these models. Students will become familiar with hardware implementation techniques for using parallelism, locality, and low precision to implement the core computational kernels used in ML. Students will develop intuitions to make system-level trade-offs to design energy-efficient accelerators. Students will read recent research papers and complete a final design project.

</details>

---

<sub>Compiled from Stanford ExploreCourses (2026–27) and course sites. Last updated 2026-11-12. Course offerings and grading are subject to the official syllabus.</sub>
