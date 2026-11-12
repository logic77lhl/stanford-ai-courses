# CS 229S · Systems for Machine Learning

> ML systems: efficiency across the data, training, and inference stack, with hardware-software co-design.

| Item | Detail |
| --- | --- |
| **Course** | CS 229S |
| **Units** | 3 |
| **Terms** | Not scheduled in 2026–27 |
| **Grading** | Letter or Credit/No Credit |
| **Instructors** | TBA |
| **Prerequisites** | CS 224N or CS 229; systems/architecture background helps. |
| **Difficulty** | ★★★★☆ (subjective) |
| **Tags** | `MLSys` · `Systems` · `Distributed` · `Performance` |

> **Note**: Not offered in the 2026–27 ExploreCourses listing; no stable course-site link found.

## Course positioning

CS 229S looks at machine learning from a systems perspective: models are bigger, data is larger, hardware is more heterogeneous — where is the performance bottleneck? It covers data pipelines, distributed training, GPUs/accelerators, networking, inference serving, and compilation, for people who want to work on MLSys/infrastructure.

## What it covers

- **Data pipelines**: collection, cleaning, storage, throughput
- **Distributed training**: data, model, and pipeline parallelism
- **Accelerators**: GPUs/TPUs, memory hierarchy, interconnects
- **Communication and networking**: all-reduce, RDMA, topology
- **Inference serving**: batching, scheduling, KV cache, latency
- **Compilation and kernels**: XLA, TVM, Triton
- **Cases and project**: performance analysis of real systems

## Assessment & workload

Assignments plus a project, focused on systems implementation and performance analysis. Check the current syllabus for details.

## Who it's for

People who want to work on MLSys, inference infrastructure, or training platforms; systems people moving into ML.

## Study advice

Pair with CS 149 (parallel computing) and CS 217 (accelerators). Understand the roofline model and communication costs first.

## Related courses

- [CS 329S · Machine Learning Systems Design](cs329s-machine-learning-systems-design.md)
- [CS 349D · AI Inference Infrastructure](cs349d-ai-inference-infrastructure.md)
- [CS 217 · Hardware Accelerators for Machine Learning (EE 244)](cs217-hardware-accelerators-for-ml.md)

## Resources

- [ExploreCourses](https://explorecourses.stanford.edu/search?view=catalog&academicYear=20262027&q=CS+229S)
- [Course site](https://cs229s.stanford.edu/)

<details>
<summary>Official course description</summary>

> Deep learning and neural networks are being increasingly adopted across industries. They are now used to serve billions of users across applications such as search, knowledge discovery, and productivity assistants. As models become more capable and intelligent, this trend of large-scale adoption will continue to grow rapidly. Due to the widespread application, there is an increasing need to achieve high performance for both training and serving deep-learning models. However, performance is hindered by a multitude of infrastructure and lifecycle hurdles - the increasing complexity of the models, massive sizes of training and inference data, heterogeneity of the available accelerators and multi-node platforms, and diverse network properties. The slow adaptation of systems to new algorithms creates a bottleneck for the rapid evolution of deep-learning models and their applications. This course will cover systems approaches for improving the efficiency of machine learning pipelines - comprising data preparation, model training, and model deployment &amp; inference -at each level of the systems stack spanning software and hardware. Pre-req: CS224N or CS229.

</details>

---

<sub>Compiled from Stanford ExploreCourses (2026–27) and course sites. Last updated 2026-11-12. Course offerings and grading are subject to the official syllabus.</sub>
