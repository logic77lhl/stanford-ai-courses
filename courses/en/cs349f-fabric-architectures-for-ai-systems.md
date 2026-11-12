# CS 349F · Fabric Architectures For AI Systems

> The network fabric of AI clusters: fat trees, congestion control, and scheduling, aiming for ultra-low latency and near-100% goodput.

| Item | Detail |
| --- | --- |
| **Course** | CS 349F |
| **Units** | 2 |
| **Terms** | Autumn 2026 |
| **Grading** | Satisfactory/No Credit |
| **Instructors** | Prabhakar, B.; Rosenblum, M. |
| **Prerequisites** | CS 144/CS 140 or distributed-systems basics; EE 178 helps. |
| **Difficulty** | ★★★★☆ (subjective) |
| **Tags** | `Networking` · `Clusters` · `Data centers` · `Systems` |

> **Note**: Offered in Autumn 2026–27; the official site is restricted, so only the ExploreCourses link is provided.

## Course positioning

CS 349F focuses on the interconnect networks of large GPU/CPU clusters and on time-sensitive systems such as financial trading and multiplayer games. It covers data-center fabric architectures, transport protocols, congestion control, load balancing, and scheduling, with industry experts discussing real cluster design and operations.

## What it covers

- **Data-center fabric**: fat trees, leaf-spine, topologies
- **Transport protocols**: RDMA, RoCE, congestion control
- **Load balancing**: ECMP, packet spraying
- **Scheduling**: job scheduling, fabric scheduling, interaction
- **Edge vs network-centric**: two high-performance paths
- **Industry cases**: GPU clusters, trading systems

## Assessment & workload

2 units, S/NC; discussion plus a project/case study. Check the current syllabus for details.

## Who it's for

Networking, clusters, and data centers; anyone working on AI infrastructure.

## Study advice

Read it with CS 349D/E to get the full single-machine, cluster, and network picture.

## Related courses

- [CS 349D · AI Inference Infrastructure](cs349d-ai-inference-infrastructure.md)
- [CS 349E · Efficient ML Inference at Scale (EE 339)](cs349e-efficient-ml-inference-at-scale.md)
- CS 144

## Resources

- [ExploreCourses](https://explorecourses.stanford.edu/search?view=catalog&academicYear=20262027&q=CS+349F)

<details>
<summary>Official course description</summary>

> The course is concerned with the design and operation of the network fabrics which interconnect large-scale compute and storage nodes in modern AI GPU clusters, cloud computing systems, and &quot;time-sensitive systems&quot; like financial trading platforms and massive multi-player games. We will consider architectures, protocols and algorithms which enable these network fabrics to deliver deterministic and ultra-low latency at near-100% goodput. Topics include data center fabric architectures - the fat tree topology, transport protocols - congestion control and load balancing, and scheduling algorithms - job scheduling, fabric scheduling and their interaction. A particular focus will be the contrast and synergy between the edge- and network-centric approaches to building high-performance network fabrics. Students will hear from industry experts who design, operate and use large-scale GPU and CPU clusters. Recommended: Knowledge of basic Networking, OS, or Distributed Systems (CS 144, 140, or equivalent), as well as basic EE courses (EE 178) will be useful.

</details>

---

<sub>Compiled from Stanford ExploreCourses (2026–27) and course sites. Last updated 2026-11-12. Course offerings and grading are subject to the official syllabus.</sub>
