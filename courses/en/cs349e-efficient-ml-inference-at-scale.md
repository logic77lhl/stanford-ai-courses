# CS 349E · Efficient ML Inference at Scale (EE 339)

> Efficient inference at scale: model optimization, distributed serving, AI hardware, kernels, and compilers.

| Item | Detail |
| --- | --- |
| **Course** | CS 349E<br>Cross-listed: EE 339 |
| **Units** | 3 |
| **Terms** | Autumn 2026 |
| **Grading** | Letter or Credit/No Credit |
| **Instructors** | Asgar, Z.; Raina, P.; Horowitz, M.; Kjoelstad, F. |
| **Prerequisites** | Computer architecture, operating systems, ML basics; strong programming. |
| **Difficulty** | ★★★★★ (subjective) |
| **Tags** | `Inference` · `Performance` · `Hardware` · `Compilers` |

## Course positioning

CS 349E (EE 339) is taught by Mark Horowitz, Fredrik Kjolstad, and others — a hard-core mix of systems, algorithms, and hardware. It discusses how to serve large models on heterogeneous machines with low latency, high throughput, and low cost, covering quantization, distributed serving, performance modeling, kernel programming, and AI compilers.

## What it covers

- **Model optimization**: quantization, pruning, distillation, speculative decoding
- **Distributed serving**: tensor parallelism, pipelines, prefill/decode disaggregation
- **AI hardware**: GPUs/TPUs/accelerators, the memory wall
- **Performance modeling**: roofline, bandwidth/compute/latency
- **Kernel programming**: CUDA/Triton, fusion, tiling
- **AI compilers**: graph optimization, operator selection, code generation
- **Project**: end-to-end inference optimization

## Assessment & workload

Assignments plus a project, focused on implementation and measurement. Check the current syllabus for details.

## Who it's for

Graduate students/engineers working on inference performance, AI chips, or compilers; systems people going deeper into ML.

## Study advice

Brush up on CS 217/CS 149 first. Be ready to run benchmarks, not just read paper numbers.

## Related courses

- [CS 349D · AI Inference Infrastructure](cs349d-ai-inference-infrastructure.md)
- [CS 217 · Hardware Accelerators for Machine Learning (EE 244)](cs217-hardware-accelerators-for-ml.md)
- [CS 229S · Systems for Machine Learning](cs229s-systems-for-machine-learning.md)

## Resources

- [ExploreCourses](https://explorecourses.stanford.edu/search?view=catalog&academicYear=20262027&q=CS+349E)
- [Course site](https://cs349e.github.io/)

<details>
<summary>Official course description</summary>

> A graduate-level course focused on principles and techniques for designing and building large-scale disaggregated AI inference systems. The course explores architectural, algorithmic, system-level, and kernel implementation techniques for serving models with low latency, high throughput, and low cost on heterogeneous machines. Topics include model optimization techniques, distributed serving, AI hardware and performance modelling, kernel programming, and AI compilers. Class website: cs349e.github.io

</details>

---

<sub>Compiled from Stanford ExploreCourses (2026–27) and course sites. Last updated 2026-11-12. Course offerings and grading are subject to the official syllabus.</sub>
