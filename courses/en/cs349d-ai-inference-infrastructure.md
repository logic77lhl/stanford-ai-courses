# CS 349D · AI Inference Infrastructure

> AI inference infrastructure: how compound AI systems are deployed, scheduled, and scaled in the cloud.

| Item | Detail |
| --- | --- |
| **Course** | CS 349D |
| **Units** | 3 |
| **Terms** | Spring 2027 |
| **Grading** | Letter or Credit/No Credit |
| **Instructors** | Kozyrakis, C. |
| **Prerequisites** | Systems/architecture/ML basics; distributed-systems experience helps. |
| **Difficulty** | ★★★★☆ (subjective) |
| **Tags** | `Inference` · `Infrastructure` · `Cloud` · `Systems` |

## Course positioning

Taught by Christos Kozyrakis, CS 349D is a research seminar focused on inference rather than training. It argues that future AI systems are compound systems (multiple models + retrieval + tools + traditional software) and discusses the cloud infrastructure, scheduling, and architecture patterns that support them.

## What it covers

- **Inference serving**: batching, continuous batching, KV cache
- **Compound AI systems**: multi-component orchestration, dataflow
- **Cloud infrastructure**: elasticity, multi-tenancy, cost
- **Scheduling and routing**: model routing, priorities, SLAs
- **Latency/throughput/cost**: trade-offs and optimization
- **Industry practice**: guest lectures from Databricks, OpenAI, NVIDIA, etc.
- **Quarter-long project**

## Assessment & workload

Paper discussion plus guest lectures and a 2–3 person team project. Check the current syllabus for details.

## Who it's for

People who want to work on inference platforms, AI infrastructure, or cloud systems; systems-oriented graduate students.

## Study advice

Pair with CS 349E for single-machine/cluster performance and CS 349F for networking. Base the project on a real serving stack.

## Related courses

- [CS 349E · Efficient ML Inference at Scale (EE 339)](cs349e-efficient-ml-inference-at-scale.md)
- [CS 349F · Fabric Architectures For AI Systems](cs349f-fabric-architectures-for-ai-systems.md)
- [CS 229S · Systems for Machine Learning](cs229s-systems-for-machine-learning.md)

## Resources

- [ExploreCourses](https://explorecourses.stanford.edu/search?view=catalog&academicYear=20262027&q=CS+349D)
- [Course site](https://web.stanford.edu/class/cs349d/)

<details>
<summary>Official course description</summary>

> The emergence of foundation models has revolutionized AI applications, but the most powerful AI systems today are increasingly compound systems - compositions of multiple models, retrievers, tools, and traditional software components. This research seminar explores the intersection of cloud computing infrastructure and compound AI systems, covering both the infrastructure required to build and deploy these systems at scale and the architectural patterns that make them effective. Students will participate in guest lectures from leading experts across academia and industry, including leaders of companies like Databricks, OpenAI, Foundry, NVIDIA, Microsoft, and more, read and discuss papers, and complete a quarter-long project in groups of 2-3.

</details>

---

<sub>Compiled from Stanford ExploreCourses (2026–27) and course sites. Last updated 2026-11-12. Course offerings and grading are subject to the official syllabus.</sub>
