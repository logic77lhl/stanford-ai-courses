# CS 236 · Deep Generative Models

> A theory course on deep generative models: the probabilistic foundations and training algorithms behind VAEs, GANs, flows, and diffusion.

| Item | Detail |
| --- | --- |
| **Course** | CS 236 |
| **Units** | 3 |
| **Terms** | Spring 2027 |
| **Grading** | Letter or Credit/No Credit |
| **Instructors** | Ermon, S. |
| **Prerequisites** | At least one of CS 221/228/229/230; probability and calculus; Python programming. |
| **Difficulty** | ★★★★☆ (subjective) |
| **Tags** | `Generative models` · `Diffusion` · `Probability` |

## Course positioning

CS 236 is one of the most systematic courses on generative modeling, taught by Stefano Ermon. It starts from probabilistic modeling and variational inference and covers VAEs, GANs, normalizing flows, energy-based models, and diffusion/score matching; the math load is high.

## What it covers

- **Probability foundations**: maximum likelihood, variational inference, ELBO, MCMC
- **VAEs**: reparameterization, posterior collapse, hierarchical VAEs
- **GANs**: adversarial training, mode collapse, Wasserstein GAN
- **Flow models**: invertible transforms, Jacobians, continuous flows
- **Energy-based models**: contrastive divergence, score matching
- **Diffusion**: DDPM, score-based models, classifier-free guidance
- **Applications**: images, text, speech, RL
- **Project**: generative-model research or application

## Assessment & workload

Assignments plus a midterm/final and a project; both derivations and implementation matter. Check the current syllabus for details.

## Who it's for

People working on diffusion models, image/video generation, or generative AI research; anyone who wants the probabilistic ideas behind VAEs and GANs.

## Study advice

Brush up on variational inference and score matching first, or the diffusion part will be rough. Pair with CS 236G for the engineering details of GANs.

## Related courses

- [CS 236G · Generative Adversarial Networks](cs236g-generative-adversarial-networks.md)
- [CS 229 · Machine Learning (STATS 229)](cs229-machine-learning.md)
- [CS 224N · Natural Language Processing with Deep Learning (LINGUIST 284, SYMSYS 195N)](cs224n-nlp-with-deep-learning.md)

## Resources

- [ExploreCourses](https://explorecourses.stanford.edu/search?view=catalog&academicYear=20262027&q=CS+236)
- [Course site](https://deepgenerativemodels.github.io/)

<details>
<summary>Official course description</summary>

> Generative models are widely used in many subfields of AI and Machine Learning. Recent advances in parameterizing these models using neural networks, combined with progress in stochastic optimization methods, have enabled scalable modeling of complex, high-dimensional data including images, text, and speech. In this course, we will study the probabilistic foundations and learning algorithms for deep generative models, including Variational Autoencoders (VAE), Generative Adversarial Networks (GAN), and flow models. The course will also discuss application areas that have benefitted from deep generative models, including computer vision, speech and natural language processing, and reinforcement learning. Prerequisites: Basic knowledge about machine learning from at least one of CS 221, 228, 229 or 230. Students will work with computational and mathematical models and should have a basic knowledge of probabilities and calculus. Proficiency in some programming language, preferably Python, required.

</details>

---

<sub>Compiled from Stanford ExploreCourses (2026–27) and course sites. Last updated 2026-11-12. Course offerings and grading are subject to the official syllabus.</sub>
