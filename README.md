<h1 align="center">
  <strong>Awesome-World-Models-for-Healthcare</strong>
</h1>

<div align="center">

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![GitHub stars](https://img.shields.io/github/stars/chengwang96/Awesome-World-Models-for-Healthcare?style=social)](https://github.com/chengwang96/Awesome-World-Models-for-Healthcare)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](#-contributing)
[![Catalog validation](https://github.com/chengwang96/Awesome-World-Models-for-Healthcare/actions/workflows/validate-catalog.yml/badge.svg)](https://github.com/chengwang96/Awesome-World-Models-for-Healthcare/actions/workflows/validate-catalog.yml)
[![Link health](https://github.com/chengwang96/Awesome-World-Models-for-Healthcare/actions/workflows/check-links.yml/badge.svg)](https://github.com/chengwang96/Awesome-World-Models-for-Healthcare/actions/workflows/check-links.yml)
[![Content license: CC BY 4.0](https://img.shields.io/badge/content-CC%20BY%204.0-lightgrey.svg)](LICENSE-CONTENT)
[![Code license: MIT](https://img.shields.io/badge/code-MIT-blue.svg)](LICENSE)

A curated list of papers and open-source resources on **world models for healthcare**, including **medical imaging**, **longitudinal EHR modeling**, **clinical prediction**, **counterfactual reasoning**, **treatment planning**, and **surgical simulation**.

</div>

---

## 🎯 Scope

A **world model** learns the dynamics of an environment so that an agent can predict future states, simulate interventions, and plan actions without interacting with the real system. Classic examples include Ha & Schmidhuber (2018), Dreamer (Hafner et al., 2020), and JEPA (LeCun, 2022).

We collect papers that apply world models (or equivalent learned dynamics/simulation models) to:

- **Medical imaging**: radiology, ultrasound, ophthalmology, pathology, contrast kinetics
- **Surgical simulation & robotics**: video-based prediction, action-conditioned surgical models, robot policy learning
- **Clinical decision support & treatment planning**: disease trajectory simulation, tumor evolution, counterfactual patient timelines
- **Longitudinal EHR & patient trajectories**: next-visit prediction, clinical event modeling, synthetic patient generation
- **Computational biology & drug discovery**: cellular dynamics, transcriptome modeling, protein folding, drug response
- **Epidemiology & public health**: disease spread modeling, policy intervention simulation

### Strict Inclusion Criteria

Papers in the main list must satisfy **all** of the following criteria. Calling a method a "world model," "digital twin," or "world modeling" is not sufficient by itself.

| Criterion | Required evidence |
|---|---|
| **Medical grounding** | The modeled system and evaluated task are directly biomedical, clinical, or healthcare-related. |
| **State** | The method represents a patient, organ, cell, molecule, procedure, population, or medical environment state. |
| **Dynamics** | It learns or computes transitions between states across time, space, procedure steps, views, or interventions. |
| **Operational rollout** | It supports future prediction, multi-step simulation, counterfactual intervention, planning, or control. |
| **Implemented evidence** | The paper implements and evaluates the dynamics or simulator rather than only proposing a concept or benchmark. |

Action conditioning is not mandatory for autonomous physiological processes such as disease progression or cardiac motion. However, a paper claiming intervention, treatment, or control capability must model how actions change subsequent states.

We exclude static representation learning, ordinary conditional generation without state transitions, synthetic-cohort generation without dynamics, benchmark-only papers, and conceptual position papers from the main list.

The [2026-09-07 scope audit](docs/scope-audit-2026-09-07.md) distinguishes learned/hybrid dynamics from mechanistic simulators and records candidates awaiting full-text verification; pending candidates are not counted in the main list.

The [2026-09-08 search update and recheck](docs/search-update-2026-09-08.md) records why two proposed main-list additions were withdrawn under a stricter medical-world-model interpretation; one perspective remains in Survey Papers.

The [2026-09-20 search update](docs/search-update-2026-09-20.md) adds two learned medical/biomedical dynamics models, separates two new reviews from the core catalog, and records methods-level decisions on recent near-scope candidates.

<details>
<summary><strong>Audited boundary cases not counted as world-model papers</strong></summary>

| Paper | Decision |
|---|---|
| [MedDream: A Radiographic World Model for Clinical Reasoning and Evidence Generation](https://arxiv.org/abs/2609.07719) | Learns examination-level radiographic representations for diagnosis and report-conditioned image generation; the paper explicitly leaves longitudinal patient-state dynamics for future work. |
| [JEPA-Anything](https://arxiv.org/abs/2609.20800) | Medical/cellular experiments terminate at a one-step readout or intervention nomination. Recursive rollouts in control, physics and generic molecular benchmarks do not establish a medical rollout task; held outside the core list. |
| [An Immune World Model for Multiscale Forecasting and Therapeutic Hypothesis Generation](https://arxiv.org/abs/2609.14709) | Implements action-conditioned one-step immune-state prediction, but cross-scale readout propagation and perturbation-pair endpoints do not validate recursive biological rollout; cohort-level recursive evaluation remains future work. Held pending that evidence. |
| [Arti-JEPA](https://arxiv.org/abs/2609.09757) | Clinical results use frozen-encoder probes. Appendix E does implement MRI latent rollouts, but reports negligible audio-conditioning effects and no demonstrated clinical use of those rollouts; held outside the core list, not dismissed as having no dynamics. |
| [Causal Multi-Modal AI for Personalized Chemosensitivity Prediction](https://arxiv.org/abs/2609.13567) | CTX estimates treatment-specific survival risks with counterfactual regression; it does not advance a patient state through a treatment sequence. Treatment-effect estimation alone is not a world model. |
| [PPIM](https://arxiv.org/abs/2609.06869) | Approximates a controlled bioheat solution from coordinates and a prescribed heat source, evaluating the final temperature field. Internal Mamba recurrence does not demonstrate reusable medical-state rollout or ablation planning. |
| [Cortical GNN-pHNN](https://arxiv.org/abs/2607.10439) | Held outside the core list: genuine learned EEG dynamics and autonomous rollout, but evaluation is signal-dynamics fidelity rather than a demonstrated disease, treatment, or medical-BCI task. This is a medical-scope boundary decision, not a claim that dynamics are absent. |
| [Multiphase PDE Tumor Therapy Scheduling](https://arxiv.org/abs/2607.20782) | Related mechanistic oncology simulation: COMSOL advances tissue states; the Gaussian process learns a schedule-to-objective mapping, not state transitions. Not counted as a learned medical world model in this stricter recheck. |
| [A Proof-of-Concept Simulation-Driven Digital Twin Framework for Decision-Aware Diabetes Modeling](https://arxiv.org/abs/2605.11247) | Evaluates static regression/classification on the scikit-learn diabetes dataset; intervention curves use illustrative parametric functions rather than an evaluated patient-state transition model. |
| [Physics-Informed Digital Twin of Maternal-Fetal Hemodynamics for Predictive Risk Simulation in Preeclampsia](https://doi.org/10.3233/SHTI260193) | Reports fitted resistance/perfusion indices and illustrative flow maps; despite a time-dependent governing equation, it does not demonstrate time-resolved state rollout or intervention-conditioned evolution. |
| [Neurosymbolic Alignment for Physiologically-Safe Clinical Language Models](https://arxiv.org/abs/2608.24534) | Its "Physiological World Model" scores the feasibility of candidate responses using a medical knowledge graph; it does not advance physiological states or generate patient trajectories. |
| [ORION: A Hierarchical Surgical World Model for Real-Time, Multi-Agent Operating-Room Intelligence](https://irojournals.com/jucct/article/view/2380) | Proposes an integrated architecture and reports results from constituent methods; the combined world model is not implemented and evaluated. |
| [Generative Diffusion Model Surrogates for Mechanistic Agent-Based Biological Models](https://pubmed.ncbi.nlm.nih.gov/41170496/) | Conditions diffusion on classes of mechanistic parameters to generate terminal cell configurations; it does not propagate a supplied cellular state through learned transitions. |
| [Future Querying: Can LLMs Serve as Implicit Medical World Models?](https://arxiv.org/abs/2608.23248) | Fine-tunes LLMs to answer time-indexed clinical questions from patient histories; the evaluated task does not execute patient-state transitions or intervention-conditioned trajectories. |
| [HounsWorld](https://arxiv.org/abs/2608.12904) | Evaluates CT readout, reconstruction, condition-shifted generation, and future-oriented clinical QA, but does not demonstrate an executable patient-state transition model or longitudinal rollout. |
| [EndoClock](https://arxiv.org/abs/2608.09266) | Audits whether synchronization removes medically relevant acquisition events; it does not implement or evaluate a medical-state dynamics model. |
| [Surg-UniWorld](https://arxiv.org/abs/2608.06770) | Renders surgical video from supplied full-sequence instrument and tissue masks, with optional depth, edge, and flow controls; it does not predict the underlying tool-tissue transitions from initial observations and actions. |
| [In vitro and in silico characterization of competitive inhibition and repression of DUX4 target gene activation as a therapeutic approach for facioscapulohumeral muscular dystrophy (FSHD)](https://www.biorxiv.org/content/10.64898/2026.08.04.742607v2) | Includes binding, diffusion, and compartmental models, but the ODE rollout is baseline-only; treatment-conditioned DBD trajectories and validated transition rates are left for future work. |
| [Counterfactual Analysis of Executable Clinical Decision Logic](https://www.medrxiv.org/content/10.64898/2026.08.05.26359737v1) | Perturbs BMI inputs to a static diabetes classifier and measures policy sensitivity; it does not model patient-state transitions or causal treatment trajectories. |
| [Innovative Digital Twin Framework for Early Risk Detection and Personalized Perinatal Healthcare](https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2026.1724029/full) | Combines static risk classifiers with synthetic clinical and wearable-like records; sequence-aware patient dynamics and real longitudinal validation are left for future work. |
| [Joint State-Parameter Inference Enhances Estimation Performance in Model-Based Digital Therapeutics for Type 1 Diabetes](https://arxiv.org/abs/2607.26790) | Evaluates online reconstruction of glucose states and model parameters, but does not roll the inferred state forward or evaluate insulin-action planning or control. |
| [CrohnTwin-X: An Explainable Digital Twin Framework for Predicting Postoperative Recurrence in Crohn's Disease Using Multi-Omics and Clinical Features](https://doi.org/10.1016/j.cmpb.2026.109379) | Clusters static pathway profiles and applies a logistic recurrence classifier; it does not model postoperative patient-state transitions or intervention-conditioned trajectories. |
| [Time-Resolved Aortic 3D Shape Reconstruction from a Limited Number of Cine 2D MRI Slices](https://doi.org/10.1016/j.cmpb.2026.109425) | Reconstructs separately observed cardiac phases from cine slices; it neither predicts unobserved future anatomy nor rolls the aortic state forward under interventions. |
| [Development and Validation of an Artificial Intelligence-Powered 3D Digital Twin for Teaching and Assessing Retraction for Laparoscopic Cholecystectomy](https://doi.org/10.1007/s00464-026-13178-6) | Presents video-derived 3D cases in which users choose a retraction vector and force toward a displayed target; the evaluation records those selections but does not roll anatomy or procedure state forward after the action. |
| [Investigation of In Vivo Silk Scaffold Degradation by Decoupling Tissue Ingrowth Using a Gaussian Process Regression-Driven Digital Twin Framework](https://pubmed.ncbi.nlm.nih.gov/42554206/) | Regresses degradation time and measurements to long-term scaffold properties, without an executable scaffold-state transition model or perturbation rollout. |
| [Toward Digital Twin-Enabled Venous Flow Modelling: Interactive Valve Geometry and Lab-on-Chip Generation Framework](https://doi.org/10.1016/j.compbiomed.2026.111755) | Generates parameterized valve geometries and simulation-ready meshes; patient-specific flow dynamics and real-time twin integration remain downstream uses rather than an evaluated state rollout. |
| [When Measurement Conventions Masquerade as Calibration Gains in Cardiac Digital Twins](https://arxiv.org/abs/2608.01602) | Audits ejection-fraction observation operators and reference conventions; it does not implement cardiac-state transitions or future rollouts. |
| [AuricularWorld](https://arxiv.org/abs/2607.28487) | Its three-step latent loop iteratively refines a static CT segmentation; the rolled state is an internal label representation rather than evolving anatomy or another medical environment state. |
| [CalTwin](https://arxiv.org/abs/2607.26752) | Implements an ICU latent next-state predictor, but evaluates only teacher-forced one-step transitions; closed-loop rollout and intervention-conditioned use are explicitly left for future work. |
| [An AI-Driven Digital Twin Framework for Personalized COPD Treatment Optimization](https://doi.org/10.5220/0015171200004088) | Perturbs static patient covariates to create replicas and aggregates LightGBM treatment classifications; no learned patient-state transition or longitudinal rollout. |
| [DynImmune-BERT](https://arxiv.org/abs/2607.17244) | Uses Neural ODEs to encode irregular immune-repertoire trajectories for patient classification, but does not evaluate future-state rollout, intervention simulation, or planning. |
| [An Intelligent Digital Twin Framework with AI-Driven Optimization for Patient Flow and Clinical Scheduling](https://doi.org/10.3389/fdgth.2026.1835028) | Forecasts arrivals and analyzes operational datasets, but does not implement the proposed scheduling optimizer or an operational scenario simulator. |
| [A Vascularized ODE Model for Patient-Specific Prediction of Treatment Resistance in Gastrointestinal Stromal Tumors](https://doi.org/10.23939/mmc2026.02.696) | Mechanistic oncology curve fitting and parameter sensitivity analysis; early-data resistance prediction fails, with no validated patient rollout or intervention-selection policy. |
| [TyG Trajectory and Digital Twin Simulation](https://doi.org/10.51789/cmsj.2026.6.e7) | Static logistic-risk counterfactual over an altered covariate slope; no patient-state dynamics. |
| [Apollo](https://arxiv.org/abs/2604.18570) | Temporal patient representation and downstream prediction, but no executable state rollout. |
| [Validated Synthetic Patient Generation](https://arxiv.org/abs/2604.07557) | Generates complete cohort profiles rather than transitions between patient states. |
| [MedGenesis](https://www.medrxiv.org/content/10.64898/2026.06.14.26355612v1) | Updates hypotheses, evidence, and research actions in an agentic discovery workflow, but does not roll out medical or biological system-state dynamics. |
| [CellOS](https://doi.org/10.64898/2026.06.18.733163) | Aligns expression and perception views for cellular representation learning; perturbation response is a downstream prediction benchmark rather than an operational state-transition rollout. |
| [Toward World Models for Epidemiology](https://arxiv.org/abs/2604.09519) | Conceptual framework; retained under Survey Papers. |
| [Contextual Invertible World Models](https://arxiv.org/abs/2603.02274) | Static perturbation-response emulator without temporal or sequential state dynamics. |
| [How Far Are Surgeons from Surgical World Models?](https://arxiv.org/abs/2511.01775) | Evaluation benchmark for an existing video generator, not a proposed world model. |
| [ODesign](https://arxiv.org/abs/2510.22304) | Conditional biomolecular structure design without environment-state transitions or rollouts. |
| [GeneJEPA](https://www.biorxiv.org/content/10.1101/2025.10.14.682378v1) | Masked transcriptome representation prediction rather than cellular-state evolution. |
| [CheXWorld](https://arxiv.org/abs/2504.13820) | Static radiograph representation learning across anatomy/domain transformations, without temporal or action-conditioned dynamics. |

</details>

---

## 📌 Contents

- [Taxonomy](#-taxonomy)
- [Survey Papers](#-survey-papers)
- [World Model Papers](#-world-model-papers)
- [By Topic](#-by-topic)
- [Datasets, Benchmarks and Simulators](#-datasets-benchmarks-and-simulators)
- [Related Repositories](#-related-repositories)
- [Cross-References](#-cross-references)
- [Industry Models / Platforms](#industry-models-platforms)
- [Special Issues / Calls](#-special-issues--calls)
- [License](#-license)
- [Citation](#-citation)
- [Contributing](#-contributing)
- [Contact Us](#-contact-us)

---

## 🧬 Taxonomy

Each main-list paper carries compact, controlled metadata so that methods with comparable modeled states and capabilities are easy to find.

| Field | Values | Meaning |
|---|---|---|
| **State** | `Patient`, `Physiology`, `Anatomy`, `Medical image`, `Procedure/Robot`, `Clinical workflow`, `Cell`, `Molecule`, `Population` | The primary medical or biological state advanced by the model. |
| **Dynamics** | `Temporal`, `Action-conditioned`, `Mechanistic`, `Spatial/view`, `Event sequence` | The transition structure implemented by the method. Multiple values may apply. |
| **Capability** | `Forecast`, `Simulate`, `Counterfactual`, `Plan`, `Control` | What the model's rollouts are used to accomplish. |
| **Assets** | `Code`, `Weights`, `Project`, `Paper only` | Public implementation or project resources linked by the paper entry. |

The labels describe demonstrated method capabilities, not claims inferred from a paper title.

---

## 📚 Survey Papers

- (*Cell'26 Review*) **World Models for Biomedicine**
  [[📝 Paper](https://doi.org/10.1016/j.cell.2026.08.032)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42753693/)]

- (*Cell'26 Review*) **A World Model of the Virtual Cell**
  [[📝 Paper](https://doi.org/10.1016/j.cell.2026.08.042)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42753692/)]

- (*npj Health Syst'26 Perspective*) **Structural Requirements for Intelligent Clinical Digital Twins in Feedback-Driven Care**
  [[📝 Paper](https://doi.org/10.1038/s44401-026-00143-7)]

- (*arXiv'26*) **Surgical Video Generation From Diffusion to World Models: A Survey**
  [[📝 Paper](https://arxiv.org/abs/2608.26214)]

- (*arXiv'26 Perspective*) **Physiological World Models for Human State Transitions**
  [[📝 Paper](https://arxiv.org/abs/2608.15309)]

- (*J Robot Surg'26*) **Digital Twin-Enabled Robotic Surgery: A Bibliometric and Knowledge-Mapping Analysis from Patient-Specific Simulation to Autonomy and Clinical Translation**
  [[📝 Paper](https://doi.org/10.1007/s11701-026-03739-1)]

- (*J Biomed Opt'26*) **Optical Digital Twins for Disease Prevention, Diagnosis, Therapy, and Intervention**
  [[📝 Paper](https://doi.org/10.1117/1.JBO.31.8.080601)]

- (*JAMIA Open'26*) **Validating Medical Digital Twins for Clinical Decision Support: Beyond Predictive Accuracy**
  [[📝 Paper](https://pubmed.ncbi.nlm.nih.gov/42553720/)]

- (*arXiv'26*) **Cardiovascular Digital Twins from Physics Based to Data Driven Approaches**
  [[📝 Paper](https://arxiv.org/abs/2608.02135)]

- (*Biomed Eng Lett'26*) **Digital Twin for Neurological Conditions: A Systematic Scoping Review**
  [[📝 Paper](https://doi.org/10.1007/s13534-026-00605-9)]

- (*arXiv'26*) **Medical World Models in Healthcare: Foundations, Applications, and Challenges for Trustworthy Clinical Translation**
  [[📝 Paper](https://arxiv.org/abs/2607.25242)]

- (*arXiv'26*) **Medical World Models: Representing Medical States, Modelling Clinical Dynamics and Guiding Intervention Policies**
  [[📝 Paper](https://arxiv.org/abs/2606.16721)]

- (*arXiv'26*) **Towards World Models in Biomedical Research**
  [[📝 Paper](https://arxiv.org/abs/2606.05925)]

- (*arXiv'26*) **From Static Risk to Dynamic Trajectories: Toward World-Model-Inspired Clinical Prediction**
  [[📝 Paper](https://arxiv.org/abs/2605.16927)]

- (*arXiv'26*) **Grounding Clinical AI Competency in Human Cognition Through the Clinical World Model and Skill-Mix Framework**
  [[📝 Paper](https://arxiv.org/abs/2604.08226)]

- (*arXiv'26*) **Toward World Models for Epidemiology**
  [[📝 Paper](https://arxiv.org/abs/2604.09519)]

- (*NeurIPS'25 Workshop*) **Beyond Generative AI: World Models for Clinical Prediction, Counterfactuals, and Planning**
  [[📝 Paper](https://arxiv.org/abs/2511.16333)]

---

## 📝 World Model Papers

> Entries are sorted by year in descending order. See [Scope](#-scope) for inclusion criteria.

### 2026

- (*Front Med'26*) **Beyond Static Risk Scores: Dynamic World Models Simulating Patient-Specific Trajectories to Inform Preoperative Risk Mitigation Strategies**
  [[📝 Paper](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2026.1913206/full)] [[💻 Code](https://github.com/ustive/Beyond-Static-Risk-Scores-Dynamic-World-Models)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate + Plan` · `Assets: Code`
  > **Why it qualifies:** DPWM learns action-conditioned latent patient dynamics and samples prior-driven multi-step trajectories to rank short-window preoperative strategies; evaluation on MIMIC-IV, eICU-CRD and VitalDB is retrospective and does not establish causal intervention benefit.

- (*Nature'26*) **An Operational Perturbation Proteomics-Based Virtual Cell Model**
  [[📝 Paper](https://doi.org/10.1038/s41586-026-11001-9)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42717098/)] [[💻 Code](https://github.com/guomics-lab/PTV-1)]
  **Metadata:** `State: Cell` · `Dynamics: Temporal + Action-conditioned` · `Capability: Forecast + Simulate` · `Assets: Code`
  > **Why it qualifies:** ProteinTalks learns proteomic dynamics from baseline under a specified drug perturbation, integrates a neural ODE to predict 6/24/48-hour states, and uses those trajectories for cancer drug-efficacy and combination-synergy prediction; it does not demonstrate changing-treatment rollouts, sequential planning, or clinical benefit.

- (*ECCV'26*) **CLARITY: Medical World Model for Guiding Treatment Decisions by Modeling Context-Aware Disease Trajectories in Latent Space**
  [[📝 Paper](https://arxiv.org/abs/2512.08029)] [[💻 Code](https://github.com/DingTianxingjian/CLARITY)] [[🌐 Project](https://dingtianxingjian.github.io/clarity-project-page/)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Action-conditioned` · `Capability: Forecast + Counterfactual + Plan` · `Assets: Code + Project`
  > **Why it qualifies:** Rolls latent disease states forward under alternative treatments to support clinical decisions.

- (*arXiv'26*) **NVIDIA Cosmos-H-Dreams: Real-Time Generative Physics Simulation for Surgical Robotics**
  [[📝 Paper](https://arxiv.org/abs/2608.24199)] [[💻 Code](https://github.com/isaac-for-healthcare/Cosmos-H-Dreams)] [[🌐 Weights](https://huggingface.co/nvidia/Cosmos-H-Dreams)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate` · `Assets: Code + Weights`
  > **Why it qualifies:** Distills a surgical video world model into a streaming simulator that advances generated observations under robot-kinematic actions and feeds them back to policies; evaluates closed-loop suturing tasks against physical dVRK experiments, with task-dependent simulation fidelity.

- (*arXiv'26*) **Progressive Experience Fusion for Multi-Task World Model Control in Endovascular Navigation**
  [[📝 Paper](https://arxiv.org/abs/2608.18647)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Temporal + Action-conditioned` · `Capability: Plan + Control` · `Assets: Paper only`
  > **Why it qualifies:** PEF learns guidewire-state transitions, rewards, and values for TD-MPC2 rollouts, then selects rotation and translation commands through model-predictive planning; evaluates patient-derived vascular simulations and an unseen fluoroscopic stroke phantom, not in-patient navigation.

- (*arXiv'26*) **Surgical WAM: A World-Action Model for Data-Efficient Surgical Robot Learning**
  [[📝 Paper](https://arxiv.org/abs/2608.11204)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Temporal + Action-conditioned` · `Capability: Control` · `Assets: Paper only`
  > **Why it qualifies:** Jointly samples future-observation and robot-action tokens during inference, with actions attending to predicted futures before receding-horizon execution; evaluates control success on four SurRoL tasks, not standalone future-video prediction fidelity.

- (*medRxiv'26*) **The Coupled Stochastic Dynamical System: A Generative Model for Simulating and Forecasting Youth Mental Health Trajectories**
  [[📝 Paper](https://www.medrxiv.org/content/10.64898/2026.07.26.26358943v1)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Mechanistic` · `Capability: Simulate` · `Assets: Paper only`
  > **Why it qualifies:** CSDS advances coupled psychiatric burden, affect, digital behavior, and wearable-physiology states to generate individualized trajectories evaluated on GLOBEM; downstream forecasting is retrospective, and twin calibration uses full-series summaries rather than a strictly prospective initialization window.

- (*Life AI'26*) **Diffusion-Pref: Diffusion World Model Guided Zero-Shot Preference Learning for Safe Glucose Control in Type 1 Diabetes**
  [[📝 Paper](https://www.sciltp.com/journals/lifeai/articles/2604003779)] [[💻 Code](https://github.com/aussie-bzhang/Diffusion-Pref)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Action-conditioned` · `Capability: Forecast + Simulate + Control` · `Assets: Code`
  > **Why it qualifies:** Generates six-hour glucose trajectories conditioned on glucose history, meal context, and insulin actions, using sampled outcomes to construct preferences for an offline dosing policy; OhioT1DM forecasting and model-based policy evaluation do not establish clinical treatment safety or efficacy.

- (*npj Syst Biol Appl'26*) **Learning Patient-Specific Spatial Biomarker Dynamics via Operator Learning for Alzheimer's Disease Progression**
  [[📝 Paper](https://doi.org/10.1038/s41540-026-00719-x)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42082519/)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Forecast + Simulate + Plan` · `Assets: Paper only`
  > **Why it qualifies:** LENO advances patient-specific amyloid, tau, and neurodegeneration dynamics and evaluates longitudinal PET forecasts in ADNI; additional anti-amyloid and anti-tau control terms support hypothetical treatment optimization, not clinically validated treatment effects.

- (*AISTATS'26*) **Bayesian Inverse Transition Learning: Learning Dynamics from Near-Optimal Trajectories**
  [[📝 Paper](https://proceedings.mlr.press/v300/benac26a.html)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Action-conditioned` · `Capability: Plan` · `Assets: Paper only`
  > **Why it qualifies:** BITL infers a posterior over action-conditioned state-transition matrices and solves the resulting decision models for treatment policies; the medical experiment uses MIMIC-IV hypotension trajectories with fluid and vasopressor actions, assessing offline policy agreement and reward transfer rather than clinical outcomes.

- (*arXiv'26*) **FlatASCEND: Autoregressive Clinical Sequence Generation with Continuous Time Prediction and Association-Based Pharmacological Testing**
  [[📝 Paper](https://arxiv.org/abs/2605.04071)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Event sequence` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  > **Why it qualifies:** Autoregressively appends clinical events and elapsed times to patient-specific prefixes, evaluating free-running trajectories on MIMIC-IV and INSPECT; medication-token experiments test observational associations and explicitly do not establish causal pharmacological responses.

- (*arXiv'26*) **Stable Long-Horizon Neural ODE Reduced-Order Models via Learned Feedback for Biological Growth and Remodeling**
  [[📝 Paper](https://arxiv.org/abs/2604.13820)] [[💻 Code](https://github.com/joel-laudo/TE-skin-NODE-ROM)]
  **Metadata:** `State: Anatomy` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Forecast + Simulate` · `Assets: Code`
  > **Why it qualifies:** Advances reduced skin-displacement and growth states under tissue-expander inflation histories using neural ODE dynamics with learned growth feedback; evaluates long-horizon surgical tissue-expansion rollouts against held-out finite-element simulations, not clinical healing outcomes.

- (*bioRxiv'26*) **OPTIMIS: Optimizing Personalized Therapies through Integrated Multiscale Intelligent Simulation**
  [[📝 Paper](https://www.biorxiv.org/content/10.64898/2026.03.24.713941v1)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41929084/)] [[💻 Code](https://github.com/wujah/OPTIMIS)]
  **Metadata:** `State: Cell` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Simulate + Control` · `Assets: Code`
  > **Why it qualifies:** Couples stochastic receptor signaling to neural-ODE tumor, CAR-T, and cytokine dynamics, then trains a dosing policy through treatment-conditioned rollouts; held-out evaluation uses synthetic patient cohorts and does not demonstrate clinical CAR-T treatment efficacy.

- (*bioRxiv'26*) **Digital Twin Brain Simulation and Manipulation of a Functional Brain Network Underlying Mental Illness**
  [[📝 Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC13015335/)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41890017/)] [[💻 Code](https://github.com/Shmily94/Digital_twin_brain-psychiatry-)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Simulate + Counterfactual` · `Assets: Code`
  > **Why it qualifies:** Personalizes a spiking whole-brain simulator, freezes calibration, and propagates neural and hemodynamic states under circuit-parameter perturbations; compares simulated network responses with independent pharmacological fMRI data, without establishing a clinical drug-dose response model.

- (*AAAI'26*) **Bootstrapping Personalized Insulin Therapy via Model-Based Reinforcement Learning: An In Silico Study**
  [[📝 Paper](https://ojs.aaai.org/index.php/AAAI/article/view/41160)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate + Plan + Control` · `Assets: Paper only`
  > **Why it qualifies:** Transfers patient-matched LSTM glucose dynamics and recursively simulates insulin-conditioned trajectories for H-step Deep Dyna-Q policy learning; dosing policies are evaluated in Simglucose, while real-data validation tests glucose prediction for one OhioT1DM participant only.

- (*arXiv'26*) **Uni-Flow: A Unified Autoregressive-Diffusion Model for Complex Multiscale Flows**
  [[📝 Paper](https://arxiv.org/abs/2602.15592)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  > **Why it qualifies:** Combines autoregressive latent dynamics with diffusion-based spatial refinement; its medical experiment rolls patient-specific aortic-coarctation surface-pressure fields across multiple cardiac cycles and compares them with high-fidelity hemodynamic simulations.

- (*BMC Med'26*) **Digital Twin Brain Reveals State-Specific Stimulation Targets for Abnormal Brain Dynamics in Tinnitus**
  [[📝 Paper](https://doi.org/10.1186/s12916-026-04687-1)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41664110/)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Simulate` · `Assets: Paper only`
  > **Why it qualifies:** Fits connectome-coupled oscillator dynamics to tinnitus brain states and reruns them under regional stimulation perturbations; compares simulated state changes with a small independent rTMS dataset, without prospectively validating personalized target selection or symptom improvement.

- (*Smart Health'26*) **Patient-Specific Deep Offline Artificial Pancreas for Blood Glucose Regulation in Type 1 Diabetes**
  [[📝 Paper](https://doi.org/10.1016/j.smhl.2026.100633)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41766716/)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Simulate + Control` · `Assets: Paper only`
  > **Why it qualifies:** Uses systems-biology-informed neural networks to infer patient-specific glucose-insulin ODE parameters and runs those dynamics under offline-RL insulin policies; treatment comparisons are in silico, and the paper reports inconsistent policy-experiment sample counts.

- (*arXiv'26*) **High-Fidelity Longitudinal Patient Simulation Using Real-World Data**
  [[📝 Paper](https://arxiv.org/abs/2601.17310)] [[💻 Code](https://github.com/yuakagi/Watcher)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Event sequence` · `Capability: Forecast + Simulate` · `Assets: Code`
  > **Why it qualifies:** Watcher autoregressively advances a patient timeline through clinical events, timestamps, and numeric laboratory results from an observed prefix; evaluates multi-day Monte Carlo trajectories and derived risks on temporally held-out hospital records, without causal treatment simulation.

- (*Comput Biol Med'26*) **Liquid Fourier Latent Dynamics Networks for Fast GPU-Based Numerical Simulations in Computational Cardiology**
  [[📝 Paper](https://doi.org/10.1016/j.compbiomed.2025.111355)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41338030/)] [[📝 Preprint](https://arxiv.org/abs/2408.09818)] [[💻 Code](https://github.com/StanfordCBCL/LFLDNets)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal` · `Capability: Simulate` · `Assets: Code`
  > **Why it qualifies:** LFLDNets evolve compact recurrent physiological states and reconstruct three-dimensional electrophysiology or flow fields, evaluating complete cardiac-cycle trajectories under held-out parameters and boundary conditions against numerical solvers; the journal article appeared online in December 2025.

- (*J Physiol'26*) **An Eikonal Model with Re-Excitability for Fast Simulations in Cardiac Electrophysiology**
  [[📝 Paper](https://doi.org/10.1113/JP287281)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42678922/)] [[📝 Preprint](https://arxiv.org/abs/2410.22583)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Simulate` · `Assets: Paper only`
  > **Why it qualifies:** Advances cardiac activation, recovery, and re-excitation under repeated stimuli, reproducing atrial and ventricular macro-reentry against monodomain simulations rather than only calculating a single activation map.

- (*Med Image Anal'26 Online*) **Towards Patient-Specific Optimization for Mandibular Reconstruction Planning Based on Predicted Bone-Union Propensity**
  [[📝 Paper](https://doi.org/10.1016/j.media.2026.104281)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42700676/)] [[📝 Preprint](https://arxiv.org/abs/2605.01084)] [[💻 Code](https://github.com/hamidreza-aftabi/OsteoOpt)]
  **Metadata:** `State: Anatomy` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Simulate + Plan` · `Assets: Code`
  > **Why it qualifies:** OsteoOpt++ time-integrates jaw mechanics through chewing cycles for candidate reconstruction geometries and optimizes surgical cuts and donor positioning using simulated apposition and safety; its year-1 CT comparison is retrospective spatial validation, not a bone-healing trajectory forecast.

- (*arXiv'26*) **A Physiology-Informed Digital Twin Framework for Simulating Liver Health Progression**
  [[📝 Paper](https://arxiv.org/abs/2608.14969)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Mechanistic` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  > **Why it qualifies:** hePaTwin advances coupled hepatic metabolic and bilirubin states with disease-stage calibration, initializing from baseline records and comparing multi-visit biomarker rollouts with longitudinal patient measurements; treatment-effect validation is not demonstrated.

- (*Nat Cardiovasc Res'26*) **Accounting for Uncertainty in Computational Models of Ventricular Tachycardia Improves Ablation Guidance**
  [[📝 Paper](https://doi.org/10.1038/s44161-026-00856-w)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42601469/)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Mechanistic` · `Capability: Simulate` · `Assets: Paper only`
  > **Why it qualifies:** Uses reaction-eikonal propagation and ionic dynamics to simulate ventricular-tachycardia circuits and ECGs across scar reconstructions, comparing them with clinical recordings and aggregating viable circuits into a SATHe Map; this is a mechanistic simulator, not learned latent dynamics.

- (*arXiv'26*) **Intervention-Aware Clinical World Model for Post-Op Outcome Forecasting in Cardiology**
  [[📝 Paper](https://arxiv.org/abs/2608.13518)] [[💻 Code](https://github.com/cys1102/af-blanking-world-model)]
  **Metadata:** `State: Anatomy` · `Dynamics: Temporal + Event sequence + Action-conditioned` · `Capability: Forecast` · `Assets: Code`
  > **Why it qualifies:** Recurrently advances an MRI-derived atrial latent state through ablation, clinical events, and elapsed-time drift to forecast scar extent and recurrence in DECAAF-II; input-editing experiments are associational sensitivity tests, not causal treatment counterfactuals.

- (*arXiv'26*) **S2-HWM: Sparse Event-Structured Hierarchical World Model for Long-Horizon Surgical Robot Manipulation**
  [[📝 Paper](https://arxiv.org/abs/2608.13103)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Temporal + Event sequence + Action-conditioned` · `Capability: Simulate + Control` · `Assets: Paper only`
  > **Why it qualifies:** Combines action-conditioned DreamerV3 dynamics with chained event-level state, duration, and reward predictions to train hierarchical policies in imagination, evaluating sequential surgical peg transfers and recovery from induced drops in SurRoL.

- (*arXiv'26*) **An Open-Source Framework for Predicting Ultrasound Neuromodulation: Bridging Tissue Elastomechanics and Neuron Firing Dynamics**
  [[📝 Paper](https://arxiv.org/abs/2608.06321)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Simulate + Counterfactual` · `Assets: Paper only`
  > **Why it qualifies:** Propagates prescribed tFUS exposures through acoustic, elastic, thermal, membrane, and neuron dynamics to simulate anatomy-registered firing histories under alternative mechanisms and parameters.

- (*bioRxiv'26*) **A Physics-Inspired Classical Digital Twin of the Cell: A Composite Multi-Clock Port-Hamiltonian Neural Network Learned from Multi-Omic Circadian Data**
  [[📝 Paper](https://www.biorxiv.org/content/10.64898/2026.07.11.737972v3)] [[💻 Code](https://github.com/quantum-omics/Classical-Virtual-Omics)]
  **Metadata:** `State: Cell` · `Dynamics: Temporal + Mechanistic` · `Capability: Forecast + Simulate` · `Assets: Code`
  > **Why it qualifies:** Learns port-Hamiltonian graph transitions over time-resolved mouse-liver transcript, protein, and metabolite states, then free-runs across held-out circadian segments while preserving passivity.

- (*bioRxiv'26*) **Parameter-Dependent Effects of Spinal Cord Stimulation on Neural Activation and Evoked Compound Action Potentials**
  [[📝 Paper](https://www.biorxiv.org/content/10.64898/2026.08.03.742575v1)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Simulate + Counterfactual` · `Assets: Paper only`
  > **Why it qualifies:** Couples spinal finite-element fields to temporal multicompartment axon dynamics and reruns alternative stimulation and recording parameters to simulate neural recruitment and ECAP waveforms.

- (*bioRxiv'26*) **A Dynamical Digital Twin Unmasks Hidden Neuromotor Control Policies and Catastrophic Tipping Points in Parkinson's Disease**
  [[📝 Paper](https://www.biorxiv.org/content/10.64898/2026.03.09.710685v2)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Mechanistic` · `Capability: Simulate` · `Assets: Paper only`
  > **Why it qualifies:** Assimilates individual force-plate trajectories into a mechanistic intermittent-control state model, generates patient-level stochastic sway rollouts, and simulates Parkinson-related attractor bifurcations.

- (*arXiv'26*) **Optimal Stimulation Sites Are Not the Most Affected: Personalised Models of Resting-State fMRI in Alzheimer's Disease**
  [[📝 Paper](https://arxiv.org/abs/2607.24356)] [[💻 Code](https://github.com/cristianocapone/AD-reservoir-FC-stimulation)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate + Counterfactual + Plan + Control` · `Assets: Code`
  > **Why it qualifies:** Fits subject-specific free-running fMRI dynamics, applies candidate focal drives to virtual patients, selects individual stimulation targets, and validates a causally informed real-time closed-loop controller.

- (*Phys Med Biol'26*) **Towards a Clinically Practical Computational Platform for Systematically Adapting Radiation Therapy for Glioma Patients**
  [[📝 Paper](https://doi.org/10.1088/1361-6560/ae9687)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42562016/)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Simulate + Counterfactual + Plan` · `Assets: Paper only`
  > **Why it qualifies:** Calibrates a biology-based glioma-growth model to each patient's longitudinal MRI, virtually applies standard and proliferation-targeted dose maps, and projects post-therapy tumor burden for adaptive planning.

- (*Ann Biomed Eng'26*) **Developing a Digital Twin of the Cardiopulmonary System in a Mouse: Inferring Hemodynamics from Sparse Measurements**
  [[📝 Paper](https://doi.org/10.1007/s10439-026-04107-8)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42550388/)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Mechanistic` · `Capability: Simulate` · `Assets: Paper only`
  > **Why it qualifies:** Fits an individualized 0D cardiopulmonary state model to mouse pressure-volume data and integrates its coupled hemodynamics to reproduce full waveforms and infer otherwise unmeasured physiology.

- (*Bull Math Biol'26*) **Assessing the Role of Model Complexity in Virtual Clinical Trial Outcomes**
  [[📝 Paper](https://doi.org/10.1007/s11538-026-01715-2)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42530700/)] [[💻 Code](https://github.com/jgevertz/VCT)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Simulate + Counterfactual` · `Assets: Code`
  > **Why it qualifies:** Runs mechanistic tumor-virus treatment trajectories for virtual murine patients under multiple dosing protocols, testing how model complexity and cohort construction alter trial outcomes.

- (*eLife'26*) **Large-Scale Synthetic Data Enable Digital Twins of Human Excitable Cells**
  [[📝 Paper](https://doi.org/10.7554/eLife.110013)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42489674/)] [[💻 Code](https://github.com/ClancyLabUCD/Digital-Twin-for-the-Win-Personalized-Cardiac-Electrophysiology)]
  **Metadata:** `State: Cell` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Simulate + Counterfactual` · `Assets: Code`
  > **Why it qualifies:** Infers 52 biophysical parameters for individual cardiomyocytes, then runs mechanistic action-potential rollouts under alternative E-4031 concentrations to expose heterogeneous proarrhythmic responses.

- (*bioRxiv'26*) **Patient-Specific Heart Rate Modulates Developmental Electrophysiology in Transcriptomic-Guided In Silico Models of Pediatric Human Atrial Cardiomyocytes**
  [[📝 Paper](https://www.biorxiv.org/content/10.64898/2026.07.21.739866v1)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42538960/)]
  **Metadata:** `State: Cell` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Simulate + Counterfactual` · `Assets: Paper only`
  > **Why it qualifies:** Scales atrial-cell models with each pediatric patient's transcriptome and rolls action potentials and calcium transients to steady state under intrinsic and counterfactual fixed pacing rates.

- (*Cell'26*) **Whole-Cell Particle-Based Digital Twin Simulations from 4D Lattice Light-Sheet Microscopy Data**
  [[📝 Paper](https://doi.org/10.1016/j.cell.2026.06.010)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42379169/)] [[💻 Code](https://github.com/schoeneberglab/readdy-cell)]
  **Metadata:** `State: Cell` · `Dynamics: Temporal + Mechanistic + Spatial/view + Action-conditioned` · `Capability: Forecast + Simulate + Counterfactual` · `Assets: Code`
  > **Why it qualifies:** Builds microscopy-conditioned spatial cell states and advances mitochondria through reaction-diffusion, fusion/fission, and motor transport while predicting control, microtubule-perturbed, and stress responses.

- (*Comput Methods Programs Biomed'26*) **Integrating EMT Dynamics in Model-Based Metastasis Prediction**
  [[📝 Paper](https://doi.org/10.1016/j.cmpb.2026.109390)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42061167/)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  > **Why it qualifies:** Couples TGF-beta and EMT signaling to temporal primary and metastatic tumor growth under chemotherapy and radiotherapy, then rolls virtual patients forward to survival outcomes.

- (*Heart Rhythm'26*) **High-Fidelity Postmyocardial Infarction Ventricular Tachycardia Simulation for Intraprocedure Ablation Guidance**
  [[📝 Paper](https://doi.org/10.1016/j.hrthm.2026.03.1962)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41956268/)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  > **Why it qualifies:** Advances paced myocardial electrophysiology and ECG states through a GPU-accelerated monodomain solver, reproducing VT inducibility and morphology across ablation stages and exposing potential future VTs.

- (*arXiv'26*) **CrossScope: A Role-Asymmetric World Model for Joint Dual-Scope Surgical Video Prediction**
  [[📝 Paper](https://arxiv.org/abs/2608.03211)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Temporal + Spatial/view` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  > **Why it qualifies:** Jointly predicts eight future Mother- and Child-scope frames from synchronized ERCP observations and causal history, with evaluation on phantom and patient-held-out real procedures.

- (*MICCAI'26 Workshop*) **Automatic Patient-Specific Microwave Ablation Planning Accelerated by a Physics-Guided Deep Learning Model**
  [[📝 Paper](https://arxiv.org/abs/2608.03086)]
  **Metadata:** `State: Anatomy` · `Dynamics: Mechanistic + Action-conditioned` · `Capability: Simulate + Counterfactual + Plan` · `Assets: Paper only`
  > **Why it qualifies:** Uses patient anatomy and treatment actions to predict post-ablation regions, then repeatedly queries this forward simulator while optimizing antenna trajectory, power, and duration.

- (*MICCAI'26 Workshop*) **tFUSOperator: Operator Learning for Transcranial Focused Ultrasound Digital Twins**
  [[📝 Paper](https://arxiv.org/abs/2608.01839)] [[💻 Code](https://github.com/CMME-Lab/tFUSOperator)]
  **Metadata:** `State: Anatomy` · `Dynamics: Mechanistic + Action-conditioned` · `Capability: Simulate` · `Assets: Code`
  > **Why it qualifies:** Learns patient-skull-conditioned acoustic propagation and simulates intracranial pressure fields under alternative transducer positions, orientations, frequencies, and treatment conditions.

- (*arXiv'26*) **NeuroWorld: A Latent Brain World Model for Stimulus-Conditioned Human Brain Dynamics**
  [[📝 Paper](https://arxiv.org/abs/2608.01773)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Action-conditioned` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  > **Why it qualifies:** Learns causal stimulus-conditioned latent brain transitions and autoregressively rolls them out into subject-specific whole-brain fMRI trajectories over multiple future time points.

- (*arXiv'26*) **EndoWAM: A Grounded World-Action Model for Generalizable Endoscopic Navigation**
  [[📝 Paper](https://arxiv.org/abs/2608.01221)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Temporal` · `Capability: Forecast` · `Assets: Paper only`
  > **Why it qualifies:** Trains a video dynamics prior and future-target generator over endoscopic states, with the predictive representation evaluated in closed-loop physical-phantom navigation across three procedures.

- (*MICCAI'26 Workshop*) **Anticipatory Digital Twins for Online Head-and-Neck Adaptive Proton Therapy via Foundation-Model Registration**
  [[📝 Paper](https://arxiv.org/abs/2608.00831)]
  **Metadata:** `State: Anatomy` · `Dynamics: Temporal + Spatial/view` · `Capability: Forecast` · `Assets: Paper only`
  > **Why it qualifies:** Transfers longitudinal anatomical change through a learned registration model to forecast patient-specific treatment-day CT states and contours before image acquisition.

- (*arXiv'26*) **Failure Detection for Surgical Robot Imitation Policies via Flow-Matching World Modeling**
  [[📝 Paper](https://arxiv.org/abs/2607.27511)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Temporal + Action-conditioned` · `Capability: Forecast` · `Assets: Paper only`
  > **Why it qualifies:** Learns nominal multi-step visual transitions conditioned on surgical-robot actions and detects failures from inconsistencies between predicted and realized endpoint states in simulated and real dVRK tasks.

- (*arXiv'26*) **Action-Conditioned World Model for Goal Plane Probe Guidance in Robotic Ultrasound**
  [[📝 Paper](https://arxiv.org/abs/2607.21918)]
  **Metadata:** `State: Medical image` · `Dynamics: Spatial/view + Action-conditioned` · `Capability: Forecast + Simulate + Control` · `Assets: Paper only`
  > **Why it qualifies:** Predicts future ultrasound states under candidate 6-DoF probe motions, uses the frozen model as an internal simulator for policy learning, and validates closed-loop carotid and thyroid guidance.

- (*arXiv'26*) **A Diffusion-Model Subpopulation Digital Twin for Mobile Health Deployment: A Case Study on the HeartSteps Intervention**
  [[📝 Paper](https://arxiv.org/abs/2607.21403)]
  **Metadata:** `State: Population` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate` · `Assets: Paper only`
  > **Why it qualifies:** Generates temporally causal participant trajectories, accepts sequential mobile-health intervention actions, and rolls subpopulation behavior forward to rehearse target deployments.

- (*arXiv'26*) **PIONEER: Bayesian Joint Modelling of Mechanistic Tumour Growth and Time-to-Event Endpoints for Dynamic Prediction of Ongoing Oncology Trials**
  [[📝 Paper](https://arxiv.org/abs/2607.17908)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Mechanistic` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  > **Why it qualifies:** Jointly infers latent tumor-growth and clinical-event dynamics, then forward-simulates patient trajectories and mature trial endpoints from interim data.

- (*arXiv'26*) **Enhancing Personalized Bladder Cancer Treatment Through Reinforcement Learning: A Recurrent Patient State Transition Decision Support Framework**
  [[📝 Paper](https://arxiv.org/abs/2607.16916)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate + Plan + Control` · `Assets: Paper only`
  > **Why it qualifies:** Learns treatment-conditioned recurrent bladder-cancer state transitions from historical observations and uses recursive simulated trajectories for DQN planning; validation is confined to the learned simulator.

- (*arXiv'26*) **Differentiable Cardiac Electrophysiology Simulations for Dynamical State and Parameter Estimation**
  [[📝 Paper](https://arxiv.org/abs/2607.15492)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Mechanistic` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  > **Why it qualifies:** Fits a differentiable electrophysiology PDE simulator to partial cardiac measurements and rolls the recovered action-potential dynamics forward.

- (*arXiv'26*) **AI-Augmented Adaptive Digital Twin Modeling for Brain Tumor Evolution Prediction and Treatment Scheduling**
  [[📝 Paper](https://arxiv.org/abs/2607.13877)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Forecast + Simulate + Plan + Control` · `Assets: Paper only`
  > **Why it qualifies:** Combines treatment-conditioned tumor dynamics, patient-specific online updating, 120-step recursive rollouts, and MPC scheduling; evaluation is limited to patient-data-informed synthetic trajectories.

- (*MICCAI'26*) **HemoPIC: A Physics-Informed Cerebral Hemodynamics Digital Twin for Brain Perfusion**
  [[📝 Paper](https://arxiv.org/abs/2607.08799)] [[💻 Code](https://github.com/jhuldr/HemoPIC)]
  **Metadata:** `State: Physiology` · `Dynamics: Mechanistic + Action-conditioned` · `Capability: Simulate + Counterfactual` · `Assets: Code`
  > **Why it qualifies:** Learns physics-constrained hemodynamic state transitions and rolls them forward under vascular interventions.

- (*arXiv'26*) **EHR-MPC: Inference-Time Control for Sepsis Treatment with Generative Patient Digital Twins**
  [[📝 Paper](https://arxiv.org/abs/2607.08793)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate + Plan + Control` · `Assets: Paper only`
  > **Why it qualifies:** Models intervention-conditioned patient dynamics and uses simulated treatment rollouts for model-predictive control.

- (*arXiv'26*) **Sectorial Customized Corneal Crosslinking for Keratoconus: An Inverse Biomechanical Design Study with an Anisotropic Reduced Shell Finite-Element Surrogate**
  [[📝 Paper](https://arxiv.org/abs/2607.06385)]
  **Metadata:** `State: Anatomy` · `Dynamics: Mechanistic + Action-conditioned` · `Capability: Simulate + Counterfactual + Plan` · `Assets: Paper only`
  > **Why it qualifies:** Simulates post-treatment corneal deformation under alternative spatial crosslinking actions and optimizes the intervention mask against biomechanical and optical objectives.

- (*medRxiv'26*) **Personalized Planning of Cardiac Resynchronization Therapy Through Integration of Coronary Sinus Geometry, Clinical Data, Digital Twins, and Machine Learning: Visualization, Stratification, and Optimization**
  [[📝 Paper](https://www.medrxiv.org/content/10.64898/2026.07.01.26356827v1)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Simulate + Counterfactual + Plan` · `Assets: Paper only`
  > **Why it qualifies:** Builds patient-specific ventricular and coronary-sinus twins, simulates activation under alternative pacing sites, and maps predicted response for pre-procedural planning; prospective validation remains outstanding.

- (*Stem Cell Reports'26*) **In Silico Optimization of Regenerative Cell Therapy in the Infarcted Human Ventricles to Mitigate Arrhythmic Burden**
  [[📝 Paper](https://doi.org/10.1016/j.stemcr.2026.103007)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42425090/)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Simulate + Counterfactual` · `Assets: Paper only`
  > **Why it qualifies:** Simulates patient-specific ventricular electrophysiology before and after cell therapy to evaluate intervention outcomes over time.

- (*arXiv'26*) **Personalized 4D Whole-Heart Mesh Reconstruction from Cine MRI via Multi-Scale Temporal Modeling and Differentiable Contour Rendering**
  [[📝 Paper](https://arxiv.org/abs/2607.01952)]
  **Metadata:** `State: Anatomy` · `Dynamics: Temporal` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  > **Why it qualifies:** Reconstructs and predicts patient-specific 3D cardiac geometry as a continuous trajectory through the cardiac cycle.

- (*Med Image Anal'26*) **Electrophysiologically-Informed Digital Twins for Atrial Fibrillation**
  [[📝 Paper](https://doi.org/10.1016/j.media.2026.104131)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42172939/)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Mechanistic` · `Capability: Simulate + Plan` · `Assets: Paper only`
  > **Why it qualifies:** Builds patient-specific electrophysiology simulators that reproduce atrial activation dynamics for AF analysis and treatment planning.

- (*J Physiol'26*) **Prospective In Silico Trials Identify Combined SK and K2P Channel Block as an Effective Strategy for Atrial Fibrillation Cardioversion**
  [[📝 Paper](https://doi.org/10.1113/JP287124)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/39557619/)]
  **Metadata:** `State: Physiology` · `Dynamics: Mechanistic + Action-conditioned` · `Capability: Simulate + Counterfactual` · `Assets: Paper only`
  > **Why it qualifies:** Rolls out multiscale atrial electrophysiology under alternative ion-channel interventions to predict cardioversion outcomes.

- (*Phys Med Biol'26*) **A Digital Twin Framework for Adaptive Treatment Planning in Radiotherapy**
  [[📝 Paper](https://doi.org/10.1088/1361-6560/ae835a)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42361838/)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Simulate + Plan` · `Assets: Paper only`
  > **Why it qualifies:** Updates a patient-specific tumor twin over treatment fractions and simulates adaptive radiotherapy plans against evolving anatomy and response.

- (*arXiv'26*) **Neural Operator-Based Digital Twins for Modeling Amyloid-Beta and Tau Propagation and Treatment Optimization in Alzheimer's Disease**
  [[📝 Paper](https://arxiv.org/abs/2606.25185)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Simulate + Counterfactual + Plan` · `Assets: Paper only`
  > **Why it qualifies:** Learns reaction-diffusion biomarker dynamics and optimizes treatment through counterfactual progression rollouts.

- (*Oper Neurosurg'26*) **Iterative Virtual and Physical Simulation for Staged Separation of Total Vertical Craniopagus: The Avatar Patient Approach to Conjoined Twins**
  [[📝 Paper](https://doi.org/10.1227/ons.0000000000002116)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42318872/)]
  **Metadata:** `State: Anatomy` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate + Plan` · `Assets: Paper only`
  > **Why it qualifies:** Maintains a patient-specific anatomical avatar across staged virtual interventions to simulate and revise a complex surgical plan.

- (*arXiv'26*) **OphthaDT: Generative Digital Twins for Forecasting Visual Acuity Trajectories in Ophthalmology**
  [[📝 Paper](https://arxiv.org/abs/2606.22101)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  > **Why it qualifies:** Generates longitudinal patient-state rollouts of visual acuity under observed clinical histories.

- (*arXiv'26*) **SurgVista: Long-Horizon Surgical World Modeling with Plausible Instrument-Tissue Dynamics**
  [[📝 Paper](https://arxiv.org/abs/2606.19889)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Temporal + Action-conditioned` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  > **Why it qualifies:** Predicts long-horizon surgical video states conditioned on actions while modeling instrument-tissue interactions.

- (*arXiv'26*) **DreamReg: Belief-Driven World Model for 2D-3D Ultrasound Registration**
  [[📝 Paper](https://arxiv.org/abs/2606.18825)]
  **Metadata:** `State: Medical image` · `Dynamics: Spatial/view + Action-conditioned` · `Capability: Simulate + Plan` · `Assets: Paper only`
  > **Why it qualifies:** Learns probe-motion-conditioned latent dynamics and imagines future observations for registration planning.

- (*Biomed Phys Eng Express'26*) **Physics-Informed Koopman-Constrained ImplicitQ-Learning for Safe Offline Reinforcement Learning in Mechanical Ventilation**
  [[📝 Paper](https://doi.org/10.1088/2057-1976/ae7d30)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42296990/)]
  **Metadata:** `State: Physiology` · `Dynamics: Mechanistic + Action-conditioned` · `Capability: Simulate + Control` · `Assets: Paper only`
  > **Why it qualifies:** Learns Koopman respiratory-state dynamics and uses predicted ventilator-action consequences to shape offline policy learning.

- (*arXiv'26*) **Learning Cardiac Electrophysiology Digital Twins Through Agentic Discovery of Hybrid Structure**
  [[📝 Paper](https://arxiv.org/abs/2606.18154)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Mechanistic` · `Capability: Simulate` · `Assets: Paper only`
  > **Why it qualifies:** Discovers hybrid reaction models that stably roll out patient-specific cardiac electrophysiology.

- (*arXiv'26*) **Treatment Response Optimized Clinical Decision Support AI System via Digital Twin Simulation**
  [[📝 Paper](https://arxiv.org/abs/2606.17405)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate + Plan` · `Assets: Paper only`
  > **Why it qualifies:** Simulates treatment-conditioned patient trajectories and couples the learned dynamics to sequential decision optimization.

- (*Comput Biol Med'26*) **Causal Counterfactual Simulation for Treatment Decisions in Multimodal Lung Disease Data**
  [[📝 Paper](https://doi.org/10.1016/j.compbiomed.2026.111807)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42275812/)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate + Counterfactual` · `Assets: Paper only`
  > **Why it qualifies:** Models longitudinal lung state transitions and generates treatment counterfactuals across imaging and clinical data.

- (*arXiv'26*) **Transition-Based Digital Twin Modelling for Alzheimer's Disease under Sparse Longitudinal Data**
  [[📝 Paper](https://arxiv.org/abs/2606.09671)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal` · `Capability: Forecast + Counterfactual` · `Assets: Paper only`
  > **Why it qualifies:** Learns visit-to-visit disease transitions and composes them into patient-specific what-if progression trajectories.

- (*bioRxiv'26*) **U-Pert: Unbalanced Perturbation Dynamics For Cell Fate Design**
  [[📝 Paper](https://www.biorxiv.org/content/10.64898/2026.06.30.735555v1)]
  **Metadata:** `State: Cell` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate + Plan` · `Assets: Paper only`
  > **Why it qualifies:** Learns context-aware perturbation dynamics over cell states and abundances for forward simulation and inverse intervention design.

- (*arXiv'26*) **Chreode: A Cell World Model for One-Step Temporal Dynamics and Perturbation Prediction**
  [[📝 Paper](https://arxiv.org/abs/2605.28111)] [[💻 Code](https://github.com/mufanq/Chreode)] [[🌐 Weights](https://huggingface.co/MufanQiu/chreode-pretrained)]
  **Metadata:** `State: Cell` · `Dynamics: Temporal + Action-conditioned` · `Capability: Forecast + Simulate` · `Assets: Code + Weights`
  > **Why it qualifies:** Predicts cell-state transitions across time and perturbations rather than only embedding static transcriptomes.

- (*IEEE JBHI'26*) **TwinRL-Onco: A World Model-Empowered Digital Twin Framework with Hierarchical Reinforcement Learning for Venetoclax Resistance Trajectory Prediction and Adaptive Therapy Optimization in Chronic Lymphocytic Leukemia**
  [[📝 Paper](https://doi.org/10.1109/JBHI.2026.3696685)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42184194/)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Action-conditioned` · `Capability: Forecast + Simulate + Plan` · `Assets: Paper only`
  > **Why it qualifies:** Learns recurrent leukemia-state dynamics and performs Monte Carlo treatment rollouts for adaptive therapy policies.

- (*arXiv'26*) **ChronoMedicalWorld: A Medical World Model for Learning Patient Trajectories from Longitudinal Care Data**
  [[📝 Paper](https://arxiv.org/abs/2605.21963)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Event sequence + Action-conditioned` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  > **Why it qualifies:** Recurrently rolls patient states forward under clinical actions over longitudinal care trajectories.

- (*arXiv'26*) **ECG-WM: A Physiology-Informed ECG World Model for Clinical Intervention Simulation**
  [[📝 Paper](https://arxiv.org/abs/2605.17580)] [[🌐 Project](https://chenzk202212.github.io/ECG_World_Model/)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Action-conditioned` · `Capability: Forecast + Counterfactual` · `Assets: Project`
  > **Why it qualifies:** Predicts post-intervention ECG trajectories from pre-intervention physiological state and treatment context.

- (*arXiv'26*) **GazeWorld: A World Model of Radiologist Reading for Medical Image Representation Learning**
  [[📝 Paper](https://arxiv.org/abs/2605.23992)]
  **Metadata:** `State: Clinical workflow` · `Dynamics: Temporal + Event sequence` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  > **Why it qualifies:** Autoregressively models the evolving sequence of radiologist fixations as a diagnostic interaction trajectory.

- (*arXiv'26*) **SWoMo: Neuro-Symbolic World Model for Cataract Surgery Simulation**
  [[📝 Paper](https://arxiv.org/abs/2605.16530)] [[🌐 Project](https://ssharvienkumar.github.io/SWoMo/)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate` · `Assets: Project`
  > **Why it qualifies:** Simulates tool-tissue state changes from symbolic surgical actions and renders their visual consequences.

- (*arXiv'26*) **Toward World Modeling of Physiological Signals with Chaos-Theoretic Balancing and Latent Dynamics (NormWear-2)**
  [[📝 Paper](https://arxiv.org/abs/2605.15465)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Action-conditioned` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  > **Why it qualifies:** Learns latent dynamics of multivariate physiological signals and rolls them forward under intervention context.

- (*arXiv'26*) **Agentifying Patient Dynamics within LLMs through Interacting with Clinical World Model**
  [[📝 Paper](https://arxiv.org/abs/2605.14723)] [[💻 Code](https://github.com/FreedomIntelligence/SepsisAgent)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate + Plan` · `Assets: Code`
  > **Why it qualifies:** Provides an interactive sepsis world model that simulates candidate treatment effects for an LLM decision agent.

- (*arXiv'26*) **MolWorld: Molecule World Models for Actionable Molecular Optimization**
  [[📝 Paper](https://arxiv.org/abs/2605.08954)]
  **Metadata:** `State: Molecule` · `Dynamics: Event sequence + Action-conditioned` · `Capability: Simulate + Plan` · `Assets: Paper only`
  > **Why it qualifies:** Models molecule optimization as sequential local state transformations and plans actionable editing trajectories.

- (*arXiv'26*) **Simulating Clinical Interventions with a Generative Multimodal Model of Human Physiology (HealthFormer)**
  [[📝 Paper](https://arxiv.org/abs/2604.27899)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Action-conditioned` · `Capability: Forecast + Counterfactual` · `Assets: Paper only`
  > **Why it qualifies:** Generates multimodal physiological trajectories and simulates how clinical interventions alter future patient states.

- (*arXiv'26*) **Beyond Patient Invariance: Learning Cardiac Dynamics via Action-Conditioned JEPAs**
  [[📝 Paper](https://arxiv.org/abs/2604.22618)] [[💻 Code](https://github.com/cljosegfer/lesaude-dynamics)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Action-conditioned` · `Capability: Forecast + Simulate` · `Assets: Code`
  > **Why it qualifies:** Predicts future cardiac electrophysiology states in latent space conditioned on disease-onset actions.

- (*arXiv'26*) **Toward Safe Autonomous Robotic Endovascular Interventions using World Models**
  [[📝 Paper](https://arxiv.org/abs/2604.20151)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Temporal + Action-conditioned` · `Capability: Plan + Control` · `Assets: Paper only`
  > **Why it qualifies:** Learns endovascular environment dynamics and uses imagined rollouts for TD-MPC2 catheter control.

- (*arXiv'26*) **Sonata: A Hybrid World Model for Inertial Kinematics under Clinical Data Scarcity**
  [[📝 Paper](https://arxiv.org/abs/2604.18058)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Mechanistic` · `Capability: Forecast` · `Assets: Paper only`
  > **Why it qualifies:** Combines learned and biomechanical dynamics to predict future clinically measured inertial kinematic states.

- (*arXiv'26*) **Open-H-Embodiment: A Large-Scale Dataset for Enabling Foundation Models in Medical Robotics**
  [[📝 Paper](https://arxiv.org/abs/2604.21017)] [[💻 Code](https://huggingface.co/nvidia/Cosmos-H-Surgical-Simulator)] [[💻 Code](https://github.com/NVIDIA-Medtech/Cosmos-H-Surgical-Simulator)] [[🌐 Project](https://open-h.github.io/open-h-embodiment/)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate` · `Assets: Code + Project`
  > **Why it qualifies:** Beyond releasing data, it trains an action-conditioned surgical simulator that predicts multi-embodiment procedure rollouts.

- (*arXiv'26*) **Lingshu-Cell: A Generative Cellular World Model for Transcriptome Modeling Toward Virtual Cells**
  [[📝 Paper](https://arxiv.org/abs/2603.25240)]
  **Metadata:** `State: Cell` · `Dynamics: Action-conditioned` · `Capability: Simulate + Counterfactual` · `Assets: Paper only`
  > **Why it qualifies:** Generates perturbation-conditioned distributions of future cellular transcriptomic states.

- (*arXiv'26*) **EyeWorld: A Generative World Model of Ocular State and Dynamics**
  [[📝 Paper](https://arxiv.org/abs/2603.14039)]
  **Metadata:** `State: Anatomy` · `Dynamics: Temporal` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  > **Why it qualifies:** Learns time-conditioned transitions of ocular state for longitudinal disease progression simulation.

- (*arXiv'26*) **SAW: Toward a Surgical Action World Model via Controllable and Scalable Video Generation**
  [[📝 Paper](https://arxiv.org/abs/2603.13024)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate` · `Assets: Paper only`
  > **Why it qualifies:** Generates future surgical states conditioned on tool trajectories and procedure actions.

- (*ICLR'26 Rejected*) **Unified Surgical World Model for Structured Understanding, Long-Horizon Prediction, and Fine-Grained Generation**
  [[📝 Paper](https://openreview.net/forum?id=Kk9t5empEf)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Temporal + Action-conditioned` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  > **Why it qualifies:** Learns action-aware surgical transitions for long-horizon trajectory prediction and controllable scene evolution.

- (*MIDL'26 rejected*) **Learning Action-Conditioned World Models for Cataract Surgery from Unlabeled Videos (SurgWorld)**
  [[📝 Paper](https://openreview.net/forum?id=aYQYOVm2AB)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Temporal + Action-conditioned` · `Capability: Forecast` · `Assets: Paper only`
  > **Why it qualifies:** Predicts latent cataract-surgery state transitions conditioned on inferred atomic action tokens.

- (*CVPR'26*) **X-WIN: Building Chest Radiograph World Model via Predictive Sensing**
  [[📝 Paper](https://arxiv.org/abs/2511.14918)]
  **Metadata:** `State: Medical image` · `Dynamics: Spatial/view + Action-conditioned` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  > **Why it qualifies:** Predicts how radiographic observations change under explicit 3D viewpoint and sensing transformations.

- (*arXiv'26*) **Brain-WM: Brain Glioblastoma World Model**
  [[📝 Paper](https://arxiv.org/abs/2603.07562)] [[💻 Code](https://github.com/thibault-wch/Brain-GBM-world-model)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Action-conditioned` · `Capability: Forecast + Simulate + Counterfactual` · `Assets: Code`
  > **Why it qualifies:** Simulates coupled tumor-treatment evolution and generates future MRI states under therapy scenarios.

- (*bioRxiv'26*) **Towards building a World Model to simulate perturbation-induced cellular dynamics by AlphaCell**
  [[📝 Paper](https://www.biorxiv.org/content/10.64898/2026.03.02.709176v1)]
  **Metadata:** `State: Cell` · `Dynamics: Temporal + Action-conditioned` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  > **Why it qualifies:** Learns continuous cellular-state dynamics from large-scale perturbation data and simulates unseen responses.

- (*CVPR'26*) **MRI Contrast Enhancement Kinetics World Model**
  [[📝 Paper](https://arxiv.org/abs/2602.19285)] [[💻 Code](https://github.com/DD0922/MRI-Contrast-Enhancement-Kinetics-World-Model)]
  **Metadata:** `State: Medical image` · `Dynamics: Temporal + Mechanistic` · `Capability: Forecast + Simulate` · `Assets: Code`
  > **Why it qualifies:** Models continuous contrast-agent kinetics and synthesizes MRI states at arbitrary enhancement times.

- (*medRxiv'26*) **MedOS: AI-XR-Cobot World Model for Clinical Perception and Action**
  [[📝 Paper](https://www.medrxiv.org/content/10.64898/2026.02.18.26345936v1)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Mechanistic + Action-conditioned` · `Capability: Simulate + Plan` · `Assets: Paper only`
  > **Why it qualifies:** Uses a physics-aware procedural simulator to predict adverse events and action consequences in embodied clinical tasks.

- (*arXiv'26*) **EHRWorld: A Patient-Centric Medical World Model for Long-Horizon Clinical Trajectories**
  [[📝 Paper](https://arxiv.org/abs/2602.03569)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Event sequence + Action-conditioned` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  > **Why it qualifies:** Autoregressively simulates long-horizon patient trajectories under sequential clinical interventions.

- (*AI Medicine'26*) **World Model Enhanced Offline Reinforcement Learning for Sequential Intervention Optimization in Acute Kidney Injury**
  [[📝 Paper](https://www.sciltp.com/journals/aim/articles/2602002965)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate + Plan + Control` · `Assets: Paper only`
  > **Why it qualifies:** Learns AKI patient-state dynamics and uses model-generated transitions to optimize sequential interventions offline.

- (*arXiv'26*) **The Patient is not a Moving Document: A World Model Training Paradigm for Longitudinal EHR**
  [[📝 Paper](https://arxiv.org/abs/2601.22128)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Event sequence` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  > **Why it qualifies:** Predicts future patient states in latent and token space from longitudinal clinical histories.

- (*arXiv'26*) **Generating Counterfactual Patient Timelines from Real-World Data**
  [[📝 Paper](https://arxiv.org/abs/2604.02337)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Event sequence + Action-conditioned` · `Capability: Simulate + Counterfactual` · `Assets: Paper only`
  > **Why it qualifies:** Autoregressively generates alternative patient-event timelines under specified treatment choices.

- (*arXiv'26*) **Policy4OOD: A Knowledge-Guided World Model for Policy Intervention Simulation against the Opioid Overdose Crisis**
  [[📝 Paper](https://arxiv.org/abs/2602.12373)]
  **Metadata:** `State: Population` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate + Plan` · `Assets: Paper only`
  > **Why it qualifies:** Simulates spatiotemporal overdose dynamics under policy actions and searches intervention plans with model rollouts.

- (*arXiv'26*) **BLINK: Behavioral Latent Modeling of NK Cell Cytotoxicity**
  [[📝 Paper](https://arxiv.org/abs/2603.05110)]
  **Metadata:** `State: Cell` · `Dynamics: Temporal` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  > **Why it qualifies:** Recurrently models latent NK-cell and tumor interaction dynamics over time.

- (*arXiv'26*) **RAVEN: Scaling Recurrence-Aware Foundation Models for Clinical Records via Next-Visit Prediction**
  [[📝 Paper](https://arxiv.org/abs/2603.24562)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Event sequence` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  > **Why it qualifies:** Generates recurrent next-visit clinical events to roll longitudinal patient records forward.

### 2025

- (*J Neuroeng Rehabil'25*) **Towards AI-Based Precision Rehabilitation via Contextual Model-Based Reinforcement Learning**
  [[📝 Paper](https://doi.org/10.1186/s12984-025-01771-0)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41419889/)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate + Plan` · `Assets: Paper only`
  > **Why it qualifies:** PSCRL updates a Bayesian model of patient motor recovery and uses its dose-dependent state transitions in constrained sequential planning; the personalized rehabilitation experiments involve 150 synthetic patients, not a clinical treatment trial.

- (*Sci Adv'25*) **Multiscale Mathematical Model-Informed Reinforcement Learning Optimizes Combination Treatment Scheduling in Glioblastoma Evolution**
  [[📝 Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC13155510/)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/40779623/)] [[💻 Code](https://github.com/SunXQlab/M4RL)]
  **Metadata:** `State: Cell` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Simulate + Plan + Control` · `Assets: Code`
  > **Why it qualifies:** M4RL couples an experimentally informed tumor-microenvironment agent model to a physics-informed dynamics surrogate, using simulated CSF1R/IGF1R treatment responses to optimize combination schedules; predicted regimen benefits are computational, not clinical-trial results.

- (*Nat Mach Intell'25*) **Model-Based Reinforcement Learning for Ultrasound-Driven Autonomous Microrobots**
  [[📝 Paper](https://doi.org/10.1038/s42256-025-01054-2)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/40709099/)] [[💻 Code](https://github.com/M-Medany/Model-Based-Reinforcement-Learning-for-Ultrasound-Driven-Autonomous-Microrobots)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate + Control` · `Assets: Code`
  > **Why it qualifies:** Learns recurrent image-based dynamics for ultrasound-actuated microrobots and trains control policies on imagined trajectories; evaluates physical navigation in artificial vascular channels under static and flowing conditions, not in-vivo drug delivery.

- (*npj Digit Med'25*) **Digital Twin Brain Simulator for Real-Time Consciousness Monitoring and Virtual Intervention Using Primate Electrocorticogram Data**
  [[📝 Paper](https://doi.org/10.1038/s41746-025-01444-1)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/39929926/)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  > **Why it qualifies:** Learns hierarchical variational recurrent ECoG dynamics from awake and anesthetized primates, generating future signals and freely evolving trajectories after latent-state perturbations; latent manipulation is not a calibrated anesthetic-dose intervention model.

- (*arXiv'25*) **Cosmos-H-Surgical: Learning Surgical Robot Policies from Videos via World Modeling**
  [[📝 Paper](https://arxiv.org/abs/2512.23162)] [[💻 Code](https://huggingface.co/nvidia/Cosmos-H-Surgical-Simulator)] [[💻 Code](https://github.com/nvidia-cosmos/cosmos-cookbook)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate + Control` · `Assets: Code`
  > **Why it qualifies:** Generates action-conditioned surgical video rollouts and uses them to learn robot policies.

- (*arXiv'25*) **VCWorld: A Biological World Model for Virtual Cell Simulation**
  [[📝 Paper](https://arxiv.org/abs/2512.00306)]
  **Metadata:** `State: Cell` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate + Counterfactual` · `Assets: Paper only`
  > **Why it qualifies:** Reproduces perturbation-induced signaling cascades as stepwise cellular-state transitions.

- (*arXiv'25*) **Evolving Diagnostic Agents in a Virtual Clinical Environment**
  [[📝 Paper](https://arxiv.org/abs/2510.24654)]
  **Metadata:** `State: Clinical workflow` · `Dynamics: Event sequence + Action-conditioned` · `Capability: Simulate + Plan + Control` · `Assets: Paper only`
  > **Why it qualifies:** Implements an interactive virtual patient environment whose evolving observations support closed-loop diagnostic policy learning.

- (*arXiv'25*) **Cosmos-Surg-dVRK: World Foundation Model-based Automated Online Evaluation of Surgical Robot Policy Learning**
  [[📝 Paper](https://arxiv.org/abs/2510.16240)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate + Control` · `Assets: Paper only`
  > **Why it qualifies:** Simulates action-conditioned surgical robot trajectories for online policy evaluation.

- (*bioRxiv'25*) **Virtual Clinical Trials of BMP4 Differentiation Therapy: Digital Twins to Aid Successful Glioblastoma Trial Design**
  [[📝 Paper](https://doi.org/10.1101/2024.08.22.609156)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41279885/)] [[💻 Code](https://github.com/Harbour-N/Virtual-Clinical-Trials-of-BMP4-Differentiation-Therapy)]
  **Metadata:** `State: Cell` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Simulate + Counterfactual + Plan` · `Assets: Code`
  > **Why it qualifies:** Uses mechanistic tumor-growth twins to run treatment-schedule trials over evolving glioblastoma states.

- (*NPJ Digit Med'25*) **Large Language Models Forecast Patient Health Trajectories Enabling Digital Twins**
  [[📝 Paper](https://doi.org/10.1038/s41746-025-02004-3)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41034564/)] [[💻 Code](https://github.com/MendenLab/DT-GPT)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Event sequence` · `Capability: Forecast + Simulate` · `Assets: Code`
  > **Why it qualifies:** Autoregressively forecasts longitudinal clinical events to instantiate patient-specific future trajectories.

- (*MICCAI'25*) **World Model for AI Autonomous Navigation in Mechanical Thrombectomy**
  [[📝 Paper](https://arxiv.org/abs/2509.25518)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Temporal + Action-conditioned` · `Capability: Plan + Control` · `Assets: Paper only`
  > **Why it qualifies:** Learns endovascular transition dynamics and plans thrombectomy navigation through imagined trajectories.

- (*J Diabetes Sci Technol'25*) **Including Aerobic Exercise Into Data-Based Virtual Twins for Glycemic Simulation**
  [[📝 Paper](https://doi.org/10.1177/19322968251364291)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/40947716/)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate + Counterfactual` · `Assets: Paper only`
  > **Why it qualifies:** Simulates patient-specific glucose dynamics under time-varying exercise interventions.

- (*arXiv'25*) **medDreamer: Model-Based Reinforcement Learning with Latent Imagination on Complex EHRs for Clinical Decision Support**
  [[📝 Paper](https://arxiv.org/abs/2505.19785)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Event sequence + Action-conditioned` · `Capability: Simulate + Plan + Control` · `Assets: Paper only`
  > **Why it qualifies:** Learns latent patient dynamics and trains treatment policies on imagined EHR trajectories.

- (*arXiv'25*) **Generative Medical Event Models Improve with Scale (CoMET)**
  [[📝 Paper](https://arxiv.org/abs/2508.12104)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Event sequence` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  > **Why it qualifies:** Autoregressively generates successive medical events to simulate longitudinal patient trajectories.

- (*arXiv'25*) **Visuomotor Grasping with World Models for Surgical Robots**
  [[📝 Paper](https://arxiv.org/abs/2508.11200)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Temporal + Action-conditioned` · `Capability: Forecast + Control` · `Assets: Paper only`
  > **Why it qualifies:** Learns action-conditioned surgical grasping dynamics for model-based visuomotor control.

- (*arXiv'25*) **Xray2Xray: World Model from Chest X-rays with Volumetric Context**
  [[📝 Paper](https://arxiv.org/abs/2506.19055)]
  **Metadata:** `State: Medical image` · `Dynamics: Spatial/view + Action-conditioned` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  > **Why it qualifies:** Predicts radiographic state transitions across view changes using an inferred volumetric patient state.

- (*ICCV'25*) **Medical World Model: Generative Simulation of Tumor Evolution for Treatment Planning**
  [[📝 Paper](https://arxiv.org/abs/2506.02327)] [[💻 Code](https://github.com/scott-yjyang/MeWM)] [[🌐 Project](https://yijun-yang.github.io/MeWM/)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Action-conditioned` · `Capability: Forecast + Simulate + Plan` · `Assets: Code + Project`
  > **Why it qualifies:** Generates treatment-conditioned tumor evolution trajectories for counterfactual planning.

- (*CVPR'25*) **EchoWorld: Learning Motion-Aware World Models for Echocardiography Probe Guidance**
  [[📝 Paper](https://arxiv.org/abs/2504.13065)]
  **Metadata:** `State: Medical image` · `Dynamics: Spatial/view + Action-conditioned` · `Capability: Forecast + Control` · `Assets: Paper only`
  > **Why it qualifies:** Predicts echocardiographic observations under probe motions for closed-loop guidance.

- (*bioRxiv'25*) **Generative World Models to compute protein folding pathways**
  [[📝 Paper](https://www.biorxiv.org/content/10.1101/2025.03.26.645554v1)]
  **Metadata:** `State: Molecule` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Simulate + Plan` · `Assets: Paper only`
  > **Why it qualifies:** Models structural transitions and uses dihedral-rotation actions to generate protein-folding trajectories.

- (*arXiv'25*) **Towards Suturing World Models: Learning Predictive Models for Robotic Surgical Tasks**
  [[📝 Paper](https://arxiv.org/abs/2503.12531)] [[🌐 Project](https://mkturkcan.github.io/suturingmodels/)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Temporal + Action-conditioned` · `Capability: Forecast + Simulate` · `Assets: Project`
  > **Why it qualifies:** Learns sub-stitch spatiotemporal dynamics to predict future states of robotic suturing.

- (*MICCAI Workshop'25*) **Surgical Vision World Model**
  [[📝 Paper](https://arxiv.org/abs/2503.02904)] [[💻 Code](https://github.com/bhattarailab/Surgical-Vision-World-Model)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Temporal + Action-conditioned` · `Capability: Forecast + Simulate` · `Assets: Code`
  > **Why it qualifies:** Learns latent surgical actions and action-controlled future-video dynamics.

- (*arXiv'25*) **MM-DADM: Multimodal Drug-Aware Diffusion Model for Virtual Clinical Trials**
  [[📝 Paper](https://arxiv.org/abs/2502.07297)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate + Counterfactual` · `Assets: Paper only`
  > **Why it qualifies:** Generates drug-conditioned ECG state changes for virtual intervention trials.

- (*MIDL'25*) **4D-VQ-GAN: A World Model for Synthesizing Medical Scans at Any Time Point for Personalized Disease Progression Modeling of Idiopathic Pulmonary Fibrosis**
  [[📝 Paper](https://openreview.net/forum?id=tU3IpPQCEc)] [[💻 Code](https://github.com/anzhao920/4DVQGAN)] [[📝 arXiv](https://arxiv.org/abs/2502.05713)]
  **Metadata:** `State: Medical image` · `Dynamics: Temporal` · `Capability: Forecast + Simulate` · `Assets: Code`
  > **Why it qualifies:** Uses continuous-time latent dynamics to synthesize patient scans along disease-progression trajectories.

### 2024

- (*arXiv'24*) **Structure-aware World Model for Probe Guidance via Large-scale Self-supervised Pre-train**
  [[📝 Paper](https://arxiv.org/abs/2406.19756)]
  **Metadata:** `State: Medical image` · `Dynamics: Spatial/view + Action-conditioned` · `Capability: Forecast + Control` · `Assets: Paper only`
  > **Why it qualifies:** Predicts ultrasound-plane transitions conditioned on probe pose changes.

- (*MICCAI'24*) **Cardiac Copilot: Automatic Probe Guidance for Echocardiography with World Model** (introduces Cardiac Dreamer as the world model for cardiac spatial structures)
  [[📝 Paper](https://arxiv.org/abs/2406.13165)]
  **Metadata:** `State: Medical image` · `Dynamics: Spatial/view + Action-conditioned` · `Capability: Simulate + Control` · `Assets: Paper only`
  > **Why it qualifies:** Uses Cardiac Dreamer to simulate spatial observation changes under probe actions for navigation.

- (*arXiv'24*) **World Models for General Surgical Grasping**
  [[📝 Paper](https://arxiv.org/abs/2405.17940)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate + Plan + Control` · `Assets: Paper only`
  > **Why it qualifies:** Learns surgical grasping transition dynamics and plans robot actions with model-based reinforcement learning.

---

## 🧭 By Topic

> A complementary topic-wise view.

### Medical Imaging and Radiology

- (*npj Syst Biol Appl'26*) **Learning Patient-Specific Spatial Biomarker Dynamics via Operator Learning for Alzheimer's Disease Progression**
  [[📝 Paper](https://doi.org/10.1038/s41540-026-00719-x)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42082519/)]

- (*arXiv'26*) **Uni-Flow: A Unified Autoregressive-Diffusion Model for Complex Multiscale Flows**
  [[📝 Paper](https://arxiv.org/abs/2602.15592)]

- (*Comput Biol Med'26*) **Liquid Fourier Latent Dynamics Networks for Fast GPU-Based Numerical Simulations in Computational Cardiology**
  [[📝 Paper](https://doi.org/10.1016/j.compbiomed.2025.111355)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41338030/)] [[📝 Preprint](https://arxiv.org/abs/2408.09818)] [[💻 Code](https://github.com/StanfordCBCL/LFLDNets)]

- (*arXiv'26*) **Intervention-Aware Clinical World Model for Post-Op Outcome Forecasting in Cardiology**
  [[📝 Paper](https://arxiv.org/abs/2608.13518)] [[💻 Code](https://github.com/cys1102/af-blanking-world-model)]

- (*arXiv'26*) **NeuroWorld: A Latent Brain World Model for Stimulus-Conditioned Human Brain Dynamics**
  [[📝 Paper](https://arxiv.org/abs/2608.01773)]

- (*arXiv'26*) **Action-Conditioned World Model for Goal Plane Probe Guidance in Robotic Ultrasound**
  [[📝 Paper](https://arxiv.org/abs/2607.21918)]

- (*arXiv'26*) **Differentiable Cardiac Electrophysiology Simulations for Dynamical State and Parameter Estimation**
  [[📝 Paper](https://arxiv.org/abs/2607.15492)]

- (*MICCAI'26*) **HemoPIC: A Physics-Informed Cerebral Hemodynamics Digital Twin for Brain Perfusion**
  [[📝 Paper](https://arxiv.org/abs/2607.08799)] [[💻 Code](https://github.com/jhuldr/HemoPIC)]

- (*arXiv'26*) **Personalized 4D Whole-Heart Mesh Reconstruction from Cine MRI via Multi-Scale Temporal Modeling and Differentiable Contour Rendering**
  [[📝 Paper](https://arxiv.org/abs/2607.01952)]

- (*Med Image Anal'26*) **Electrophysiologically-Informed Digital Twins for Atrial Fibrillation**
  [[📝 Paper](https://doi.org/10.1016/j.media.2026.104131)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42172939/)]

- (*arXiv'26*) **OphthaDT: Generative Digital Twins for Forecasting Visual Acuity Trajectories in Ophthalmology**
  [[📝 Paper](https://arxiv.org/abs/2606.22101)]

- (*arXiv'26*) **DreamReg: Belief-Driven World Model for 2D-3D Ultrasound Registration**
  [[📝 Paper](https://arxiv.org/abs/2606.18825)]

- (*arXiv'26*) **Learning Cardiac Electrophysiology Digital Twins Through Agentic Discovery of Hybrid Structure**
  [[📝 Paper](https://arxiv.org/abs/2606.18154)]

- (*arXiv'26*) **GazeWorld: A World Model of Radiologist Reading for Medical Image Representation Learning**
  [[📝 Paper](https://arxiv.org/abs/2605.23992)]

- (*arXiv'26*) **Beyond Patient Invariance: Learning Cardiac Dynamics via Action-Conditioned JEPAs**
  [[📝 Paper](https://arxiv.org/abs/2604.22618)] [[💻 Code](https://github.com/cljosegfer/lesaude-dynamics)]

- (*arXiv'26*) **ECG-WM: A Physiology-Informed ECG World Model for Clinical Intervention Simulation**
  [[📝 Paper](https://arxiv.org/abs/2605.17580)] [[🌐 Project](https://chenzk202212.github.io/ECG_World_Model/)]

- (*arXiv'26*) **EyeWorld: A Generative World Model of Ocular State and Dynamics**
  [[📝 Paper](https://arxiv.org/abs/2603.14039)]

- (*CVPR'26*) **X-WIN: Building Chest Radiograph World Model via Predictive Sensing**
  [[📝 Paper](https://arxiv.org/abs/2511.14918)]

- (*CVPR'26*) **MRI Contrast Enhancement Kinetics World Model**
  [[📝 Paper](https://arxiv.org/abs/2602.19285)] [[💻 Code](https://github.com/DD0922/MRI-Contrast-Enhancement-Kinetics-World-Model)]

- (*arXiv'25*) **Xray2Xray: World Model from Chest X-rays with Volumetric Context**
  [[📝 Paper](https://arxiv.org/abs/2506.19055)]

- (*CVPR'25*) **EchoWorld: Learning Motion-Aware World Models for Echocardiography Probe Guidance**
  [[📝 Paper](https://arxiv.org/abs/2504.13065)]

- (*arXiv'25*) **MM-DADM: Multimodal Drug-Aware Diffusion Model for Virtual Clinical Trials**
  [[📝 Paper](https://arxiv.org/abs/2502.07297)]

- (*MIDL'25*) **4D-VQ-GAN: A World Model for Synthesizing Medical Scans at Any Time Point for Personalized Disease Progression Modeling of Idiopathic Pulmonary Fibrosis**
  [[📝 Paper](https://openreview.net/forum?id=tU3IpPQCEc)] [[💻 Code](https://github.com/anzhao920/4DVQGAN)] [[📝 arXiv](https://arxiv.org/abs/2502.05713)]

- (*arXiv'24*) **Structure-aware World Model for Probe Guidance via Large-scale Self-supervised Pre-train**
  [[📝 Paper](https://arxiv.org/abs/2406.19756)]

- (*MICCAI'24*) **Cardiac Copilot: Automatic Probe Guidance for Echocardiography with World Model** (introduces Cardiac Dreamer as the world model for cardiac spatial structures)
  [[📝 Paper](https://arxiv.org/abs/2406.13165)]

### Computational Biology and Cellular Dynamics

- (*Nature'26*) **An Operational Perturbation Proteomics-Based Virtual Cell Model**
  [[📝 Paper](https://doi.org/10.1038/s41586-026-11001-9)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42717098/)] [[💻 Code](https://github.com/guomics-lab/PTV-1)]

- (*bioRxiv'26*) **OPTIMIS: Optimizing Personalized Therapies through Integrated Multiscale Intelligent Simulation**
  [[📝 Paper](https://www.biorxiv.org/content/10.64898/2026.03.24.713941v1)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41929084/)] [[💻 Code](https://github.com/wujah/OPTIMIS)]

- (*Sci Adv'25*) **Multiscale Mathematical Model-Informed Reinforcement Learning Optimizes Combination Treatment Scheduling in Glioblastoma Evolution**
  [[📝 Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC13155510/)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/40779623/)] [[💻 Code](https://github.com/SunXQlab/M4RL)]

- (*eLife'26*) **Large-Scale Synthetic Data Enable Digital Twins of Human Excitable Cells**
  [[📝 Paper](https://doi.org/10.7554/eLife.110013)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42489674/)] [[💻 Code](https://github.com/ClancyLabUCD/Digital-Twin-for-the-Win-Personalized-Cardiac-Electrophysiology)]

- (*bioRxiv'26*) **Patient-Specific Heart Rate Modulates Developmental Electrophysiology in Transcriptomic-Guided In Silico Models of Pediatric Human Atrial Cardiomyocytes**
  [[📝 Paper](https://www.biorxiv.org/content/10.64898/2026.07.21.739866v1)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42538960/)]

- (*Cell'26*) **Whole-Cell Particle-Based Digital Twin Simulations from 4D Lattice Light-Sheet Microscopy Data**
  [[📝 Paper](https://doi.org/10.1016/j.cell.2026.06.010)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42379169/)] [[💻 Code](https://github.com/schoeneberglab/readdy-cell)]

- (*bioRxiv'26*) **A Physics-Inspired Classical Digital Twin of the Cell: A Composite Multi-Clock Port-Hamiltonian Neural Network Learned from Multi-Omic Circadian Data**
  [[📝 Paper](https://www.biorxiv.org/content/10.64898/2026.07.11.737972v3)] [[💻 Code](https://github.com/quantum-omics/Classical-Virtual-Omics)]

- (*bioRxiv'26*) **U-Pert: Unbalanced Perturbation Dynamics For Cell Fate Design**
  [[📝 Paper](https://www.biorxiv.org/content/10.64898/2026.06.30.735555v1)]

- (*arXiv'26*) **Chreode: A Cell World Model for One-Step Temporal Dynamics and Perturbation Prediction**
  [[📝 Paper](https://arxiv.org/abs/2605.28111)] [[💻 Code](https://github.com/mufanq/Chreode)] [[🌐 Weights](https://huggingface.co/MufanQiu/chreode-pretrained)]

- (*arXiv'26*) **MolWorld: Molecule World Models for Actionable Molecular Optimization**
  [[📝 Paper](https://arxiv.org/abs/2605.08954)]

- (*arXiv'26*) **BLINK: Behavioral Latent Modeling of NK Cell Cytotoxicity**
  [[📝 Paper](https://arxiv.org/abs/2603.05110)]

- (*arXiv'26*) **Lingshu-Cell: A Generative Cellular World Model for Transcriptome Modeling Toward Virtual Cells**
  [[📝 Paper](https://arxiv.org/abs/2603.25240)]

- (*bioRxiv'26*) **Towards building a World Model to simulate perturbation-induced cellular dynamics by AlphaCell**
  [[📝 Paper](https://www.biorxiv.org/content/10.64898/2026.03.02.709176v1)]

- (*arXiv'25*) **VCWorld: A Biological World Model for Virtual Cell Simulation**
  [[📝 Paper](https://arxiv.org/abs/2512.00306)]

- (*bioRxiv'25*) **Generative World Models to compute protein folding pathways**
  [[📝 Paper](https://www.biorxiv.org/content/10.1101/2025.03.26.645554v1)]

### Longitudinal EHR and Clinical Trajectories

- (*Front Med'26*) **Beyond Static Risk Scores: Dynamic World Models Simulating Patient-Specific Trajectories to Inform Preoperative Risk Mitigation Strategies**
  [[📝 Paper](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2026.1913206/full)] [[💻 Code](https://github.com/ustive/Beyond-Static-Risk-Scores-Dynamic-World-Models)]

- (*medRxiv'26*) **The Coupled Stochastic Dynamical System: A Generative Model for Simulating and Forecasting Youth Mental Health Trajectories**
  [[📝 Paper](https://www.medrxiv.org/content/10.64898/2026.07.26.26358943v1)]

- (*arXiv'26*) **FlatASCEND: Autoregressive Clinical Sequence Generation with Continuous Time Prediction and Association-Based Pharmacological Testing**
  [[📝 Paper](https://arxiv.org/abs/2605.04071)]

- (*arXiv'26*) **High-Fidelity Longitudinal Patient Simulation Using Real-World Data**
  [[📝 Paper](https://arxiv.org/abs/2601.17310)] [[💻 Code](https://github.com/yuakagi/Watcher)]

- (*arXiv'26*) **A Physiology-Informed Digital Twin Framework for Simulating Liver Health Progression**
  [[📝 Paper](https://arxiv.org/abs/2608.14969)]

- (*arXiv'26*) **Intervention-Aware Clinical World Model for Post-Op Outcome Forecasting in Cardiology**
  [[📝 Paper](https://arxiv.org/abs/2608.13518)] [[💻 Code](https://github.com/cys1102/af-blanking-world-model)]

- (*arXiv'26*) **PIONEER: Bayesian Joint Modelling of Mechanistic Tumour Growth and Time-to-Event Endpoints for Dynamic Prediction of Ongoing Oncology Trials**
  [[📝 Paper](https://arxiv.org/abs/2607.17908)]

- (*arXiv'26*) **EHR-MPC: Inference-Time Control for Sepsis Treatment with Generative Patient Digital Twins**
  [[📝 Paper](https://arxiv.org/abs/2607.08793)]

- (*arXiv'26*) **OphthaDT: Generative Digital Twins for Forecasting Visual Acuity Trajectories in Ophthalmology**
  [[📝 Paper](https://arxiv.org/abs/2606.22101)]

- (*arXiv'26*) **Neural Operator-Based Digital Twins for Modeling Amyloid-Beta and Tau Propagation and Treatment Optimization in Alzheimer's Disease**
  [[📝 Paper](https://arxiv.org/abs/2606.25185)]

- (*arXiv'26*) **Transition-Based Digital Twin Modelling for Alzheimer's Disease under Sparse Longitudinal Data**
  [[📝 Paper](https://arxiv.org/abs/2606.09671)]

- (*arXiv'26*) **ChronoMedicalWorld: A Medical World Model for Learning Patient Trajectories from Longitudinal Care Data**
  [[📝 Paper](https://arxiv.org/abs/2605.21963)]

- (*arXiv'26*) **Toward World Modeling of Physiological Signals with Chaos-Theoretic Balancing and Latent Dynamics (NormWear-2)**
  [[📝 Paper](https://arxiv.org/abs/2605.15465)]

- (*arXiv'26*) **Agentifying Patient Dynamics within LLMs through Interacting with Clinical World Model**
  [[📝 Paper](https://arxiv.org/abs/2605.14723)] [[💻 Code](https://github.com/FreedomIntelligence/SepsisAgent)]

- (*arXiv'26*) **Simulating Clinical Interventions with a Generative Multimodal Model of Human Physiology (HealthFormer)**
  [[📝 Paper](https://arxiv.org/abs/2604.27899)]

- (*arXiv'26*) **Sonata: A Hybrid World Model for Inertial Kinematics under Clinical Data Scarcity**
  [[📝 Paper](https://arxiv.org/abs/2604.18058)]

- (*arXiv'26*) **EHRWorld: A Patient-Centric Medical World Model for Long-Horizon Clinical Trajectories**
  [[📝 Paper](https://arxiv.org/abs/2602.03569)]

- (*arXiv'26*) **The Patient is not a Moving Document: A World Model Training Paradigm for Longitudinal EHR**
  [[📝 Paper](https://arxiv.org/abs/2601.22128)]

- (*arXiv'26*) **Generating Counterfactual Patient Timelines from Real-World Data**
  [[📝 Paper](https://arxiv.org/abs/2604.02337)]

- (*arXiv'26*) **RAVEN: Scaling Recurrence-Aware Foundation Models for Clinical Records via Next-Visit Prediction**
  [[📝 Paper](https://arxiv.org/abs/2603.24562)]

- (*NPJ Digit Med'25*) **Large Language Models Forecast Patient Health Trajectories Enabling Digital Twins**
  [[📝 Paper](https://doi.org/10.1038/s41746-025-02004-3)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41034564/)] [[💻 Code](https://github.com/MendenLab/DT-GPT)]

- (*arXiv'25*) **medDreamer: Model-Based Reinforcement Learning with Latent Imagination on Complex EHRs for Clinical Decision Support**
  [[📝 Paper](https://arxiv.org/abs/2505.19785)]

- (*arXiv'25*) **Generative Medical Event Models Improve with Scale (CoMET)**
  [[📝 Paper](https://arxiv.org/abs/2508.12104)]

### Treatment Planning and Clinical Decision Support

- (*Front Med'26*) **Beyond Static Risk Scores: Dynamic World Models Simulating Patient-Specific Trajectories to Inform Preoperative Risk Mitigation Strategies**
  [[📝 Paper](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2026.1913206/full)] [[💻 Code](https://github.com/ustive/Beyond-Static-Risk-Scores-Dynamic-World-Models)]

- (*ECCV'26*) **CLARITY: Medical World Model for Guiding Treatment Decisions by Modeling Context-Aware Disease Trajectories in Latent Space**
  [[📝 Paper](https://arxiv.org/abs/2512.08029)] [[💻 Code](https://github.com/DingTianxingjian/CLARITY)] [[🌐 Project](https://dingtianxingjian.github.io/clarity-project-page/)]

- (*Life AI'26*) **Diffusion-Pref: Diffusion World Model Guided Zero-Shot Preference Learning for Safe Glucose Control in Type 1 Diabetes**
  [[📝 Paper](https://www.sciltp.com/journals/lifeai/articles/2604003779)] [[💻 Code](https://github.com/aussie-bzhang/Diffusion-Pref)]

- (*npj Syst Biol Appl'26*) **Learning Patient-Specific Spatial Biomarker Dynamics via Operator Learning for Alzheimer's Disease Progression**
  [[📝 Paper](https://doi.org/10.1038/s41540-026-00719-x)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42082519/)]

- (*AISTATS'26*) **Bayesian Inverse Transition Learning: Learning Dynamics from Near-Optimal Trajectories**
  [[📝 Paper](https://proceedings.mlr.press/v300/benac26a.html)]

- (*bioRxiv'26*) **OPTIMIS: Optimizing Personalized Therapies through Integrated Multiscale Intelligent Simulation**
  [[📝 Paper](https://www.biorxiv.org/content/10.64898/2026.03.24.713941v1)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41929084/)] [[💻 Code](https://github.com/wujah/OPTIMIS)]

- (*bioRxiv'26*) **Digital Twin Brain Simulation and Manipulation of a Functional Brain Network Underlying Mental Illness**
  [[📝 Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC13015335/)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41890017/)] [[💻 Code](https://github.com/Shmily94/Digital_twin_brain-psychiatry-)]

- (*AAAI'26*) **Bootstrapping Personalized Insulin Therapy via Model-Based Reinforcement Learning: An In Silico Study**
  [[📝 Paper](https://ojs.aaai.org/index.php/AAAI/article/view/41160)]

- (*BMC Med'26*) **Digital Twin Brain Reveals State-Specific Stimulation Targets for Abnormal Brain Dynamics in Tinnitus**
  [[📝 Paper](https://doi.org/10.1186/s12916-026-04687-1)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41664110/)]

- (*Smart Health'26*) **Patient-Specific Deep Offline Artificial Pancreas for Blood Glucose Regulation in Type 1 Diabetes**
  [[📝 Paper](https://doi.org/10.1016/j.smhl.2026.100633)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41766716/)]

- (*J Neuroeng Rehabil'25*) **Towards AI-Based Precision Rehabilitation via Contextual Model-Based Reinforcement Learning**
  [[📝 Paper](https://doi.org/10.1186/s12984-025-01771-0)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41419889/)]

- (*Sci Adv'25*) **Multiscale Mathematical Model-Informed Reinforcement Learning Optimizes Combination Treatment Scheduling in Glioblastoma Evolution**
  [[📝 Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC13155510/)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/40779623/)] [[💻 Code](https://github.com/SunXQlab/M4RL)]

- (*npj Digit Med'25*) **Digital Twin Brain Simulator for Real-Time Consciousness Monitoring and Virtual Intervention Using Primate Electrocorticogram Data**
  [[📝 Paper](https://doi.org/10.1038/s41746-025-01444-1)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/39929926/)]

- (*J Physiol'26*) **An Eikonal Model with Re-Excitability for Fast Simulations in Cardiac Electrophysiology**
  [[📝 Paper](https://doi.org/10.1113/JP287281)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42678922/)] [[📝 Preprint](https://arxiv.org/abs/2410.22583)]

- (*Med Image Anal'26 Online*) **Towards Patient-Specific Optimization for Mandibular Reconstruction Planning Based on Predicted Bone-Union Propensity**
  [[📝 Paper](https://doi.org/10.1016/j.media.2026.104281)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42700676/)] [[📝 Preprint](https://arxiv.org/abs/2605.01084)] [[💻 Code](https://github.com/hamidreza-aftabi/OsteoOpt)]

- (*arXiv'26*) **A Physiology-Informed Digital Twin Framework for Simulating Liver Health Progression**
  [[📝 Paper](https://arxiv.org/abs/2608.14969)]

- (*Nat Cardiovasc Res'26*) **Accounting for Uncertainty in Computational Models of Ventricular Tachycardia Improves Ablation Guidance**
  [[📝 Paper](https://doi.org/10.1038/s44161-026-00856-w)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42601469/)]

- (*arXiv'26*) **Intervention-Aware Clinical World Model for Post-Op Outcome Forecasting in Cardiology**
  [[📝 Paper](https://arxiv.org/abs/2608.13518)] [[💻 Code](https://github.com/cys1102/af-blanking-world-model)]

- (*Phys Med Biol'26*) **Towards a Clinically Practical Computational Platform for Systematically Adapting Radiation Therapy for Glioma Patients**
  [[📝 Paper](https://doi.org/10.1088/1361-6560/ae9687)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42562016/)]

- (*Ann Biomed Eng'26*) **Developing a Digital Twin of the Cardiopulmonary System in a Mouse: Inferring Hemodynamics from Sparse Measurements**
  [[📝 Paper](https://doi.org/10.1007/s10439-026-04107-8)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42550388/)]

- (*Bull Math Biol'26*) **Assessing the Role of Model Complexity in Virtual Clinical Trial Outcomes**
  [[📝 Paper](https://doi.org/10.1007/s11538-026-01715-2)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42530700/)] [[💻 Code](https://github.com/jgevertz/VCT)]

- (*Comput Methods Programs Biomed'26*) **Integrating EMT Dynamics in Model-Based Metastasis Prediction**
  [[📝 Paper](https://doi.org/10.1016/j.cmpb.2026.109390)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42061167/)]

- (*Heart Rhythm'26*) **High-Fidelity Postmyocardial Infarction Ventricular Tachycardia Simulation for Intraprocedure Ablation Guidance**
  [[📝 Paper](https://doi.org/10.1016/j.hrthm.2026.03.1962)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41956268/)]

- (*arXiv'26*) **An Open-Source Framework for Predicting Ultrasound Neuromodulation: Bridging Tissue Elastomechanics and Neuron Firing Dynamics**
  [[📝 Paper](https://arxiv.org/abs/2608.06321)]

- (*bioRxiv'26*) **Parameter-Dependent Effects of Spinal Cord Stimulation on Neural Activation and Evoked Compound Action Potentials**
  [[📝 Paper](https://www.biorxiv.org/content/10.64898/2026.08.03.742575v1)]

- (*bioRxiv'26*) **A Dynamical Digital Twin Unmasks Hidden Neuromotor Control Policies and Catastrophic Tipping Points in Parkinson's Disease**
  [[📝 Paper](https://www.biorxiv.org/content/10.64898/2026.03.09.710685v2)]

- (*arXiv'26*) **Optimal Stimulation Sites Are Not the Most Affected: Personalised Models of Resting-State fMRI in Alzheimer's Disease**
  [[📝 Paper](https://arxiv.org/abs/2607.24356)] [[💻 Code](https://github.com/cristianocapone/AD-reservoir-FC-stimulation)]

- (*MICCAI'26 Workshop*) **Automatic Patient-Specific Microwave Ablation Planning Accelerated by a Physics-Guided Deep Learning Model**
  [[📝 Paper](https://arxiv.org/abs/2608.03086)]

- (*MICCAI'26 Workshop*) **tFUSOperator: Operator Learning for Transcranial Focused Ultrasound Digital Twins**
  [[📝 Paper](https://arxiv.org/abs/2608.01839)] [[💻 Code](https://github.com/CMME-Lab/tFUSOperator)]

- (*MICCAI'26 Workshop*) **Anticipatory Digital Twins for Online Head-and-Neck Adaptive Proton Therapy via Foundation-Model Registration**
  [[📝 Paper](https://arxiv.org/abs/2608.00831)]

- (*arXiv'26*) **A Diffusion-Model Subpopulation Digital Twin for Mobile Health Deployment: A Case Study on the HeartSteps Intervention**
  [[📝 Paper](https://arxiv.org/abs/2607.21403)]

- (*arXiv'26*) **Enhancing Personalized Bladder Cancer Treatment Through Reinforcement Learning: A Recurrent Patient State Transition Decision Support Framework**
  [[📝 Paper](https://arxiv.org/abs/2607.16916)]

- (*arXiv'26*) **AI-Augmented Adaptive Digital Twin Modeling for Brain Tumor Evolution Prediction and Treatment Scheduling**
  [[📝 Paper](https://arxiv.org/abs/2607.13877)]

- (*arXiv'26*) **EHR-MPC: Inference-Time Control for Sepsis Treatment with Generative Patient Digital Twins**
  [[📝 Paper](https://arxiv.org/abs/2607.08793)]

- (*arXiv'26*) **Sectorial Customized Corneal Crosslinking for Keratoconus: An Inverse Biomechanical Design Study with an Anisotropic Reduced Shell Finite-Element Surrogate**
  [[📝 Paper](https://arxiv.org/abs/2607.06385)]

- (*medRxiv'26*) **Personalized Planning of Cardiac Resynchronization Therapy Through Integration of Coronary Sinus Geometry, Clinical Data, Digital Twins, and Machine Learning: Visualization, Stratification, and Optimization**
  [[📝 Paper](https://www.medrxiv.org/content/10.64898/2026.07.01.26356827v1)]

- (*Stem Cell Reports'26*) **In Silico Optimization of Regenerative Cell Therapy in the Infarcted Human Ventricles to Mitigate Arrhythmic Burden**
  [[📝 Paper](https://doi.org/10.1016/j.stemcr.2026.103007)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42425090/)]

- (*Med Image Anal'26*) **Electrophysiologically-Informed Digital Twins for Atrial Fibrillation**
  [[📝 Paper](https://doi.org/10.1016/j.media.2026.104131)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42172939/)]

- (*J Physiol'26*) **Prospective In Silico Trials Identify Combined SK and K2P Channel Block as an Effective Strategy for Atrial Fibrillation Cardioversion**
  [[📝 Paper](https://doi.org/10.1113/JP287124)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/39557619/)]

- (*Phys Med Biol'26*) **A Digital Twin Framework for Adaptive Treatment Planning in Radiotherapy**
  [[📝 Paper](https://doi.org/10.1088/1361-6560/ae835a)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42361838/)]

- (*arXiv'26*) **Neural Operator-Based Digital Twins for Modeling Amyloid-Beta and Tau Propagation and Treatment Optimization in Alzheimer's Disease**
  [[📝 Paper](https://arxiv.org/abs/2606.25185)]

- (*Biomed Phys Eng Express'26*) **Physics-Informed Koopman-Constrained ImplicitQ-Learning for Safe Offline Reinforcement Learning in Mechanical Ventilation**
  [[📝 Paper](https://doi.org/10.1088/2057-1976/ae7d30)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42296990/)]

- (*arXiv'26*) **Treatment Response Optimized Clinical Decision Support AI System via Digital Twin Simulation**
  [[📝 Paper](https://arxiv.org/abs/2606.17405)]

- (*Comput Biol Med'26*) **Causal Counterfactual Simulation for Treatment Decisions in Multimodal Lung Disease Data**
  [[📝 Paper](https://doi.org/10.1016/j.compbiomed.2026.111807)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42275812/)]

- (*IEEE JBHI'26*) **TwinRL-Onco: A World Model-Empowered Digital Twin Framework with Hierarchical Reinforcement Learning for Venetoclax Resistance Trajectory Prediction and Adaptive Therapy Optimization in Chronic Lymphocytic Leukemia**
  [[📝 Paper](https://doi.org/10.1109/JBHI.2026.3696685)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42184194/)]

- (*arXiv'26*) **Agentifying Patient Dynamics within LLMs through Interacting with Clinical World Model**
  [[📝 Paper](https://arxiv.org/abs/2605.14723)] [[💻 Code](https://github.com/FreedomIntelligence/SepsisAgent)]

- (*arXiv'26*) **ECG-WM: A Physiology-Informed ECG World Model for Clinical Intervention Simulation**
  [[📝 Paper](https://arxiv.org/abs/2605.17580)] [[🌐 Project](https://chenzk202212.github.io/ECG_World_Model/)]

- (*arXiv'26*) **Policy4OOD: A Knowledge-Guided World Model for Policy Intervention Simulation against the Opioid Overdose Crisis**
  [[📝 Paper](https://arxiv.org/abs/2602.12373)]

- (*arXiv'26*) **Brain-WM: Brain Glioblastoma World Model**
  [[📝 Paper](https://arxiv.org/abs/2603.07562)] [[💻 Code](https://github.com/thibault-wch/Brain-GBM-world-model)]

- (*bioRxiv'25*) **Virtual Clinical Trials of BMP4 Differentiation Therapy: Digital Twins to Aid Successful Glioblastoma Trial Design**
  [[📝 Paper](https://doi.org/10.1101/2024.08.22.609156)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41279885/)] [[💻 Code](https://github.com/Harbour-N/Virtual-Clinical-Trials-of-BMP4-Differentiation-Therapy)]

- (*J Diabetes Sci Technol'25*) **Including Aerobic Exercise Into Data-Based Virtual Twins for Glycemic Simulation**
  [[📝 Paper](https://doi.org/10.1177/19322968251364291)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/40947716/)]

- (*arXiv'25*) **MM-DADM: Multimodal Drug-Aware Diffusion Model for Virtual Clinical Trials**
  [[📝 Paper](https://arxiv.org/abs/2502.07297)]

- (*ICCV'25*) **Medical World Model: Generative Simulation of Tumor Evolution for Treatment Planning**
  [[📝 Paper](https://arxiv.org/abs/2506.02327)] [[💻 Code](https://github.com/scott-yjyang/MeWM)] [[🌐 Project](https://yijun-yang.github.io/MeWM/)]

- (*AI Medicine'26*) **World Model Enhanced Offline Reinforcement Learning for Sequential Intervention Optimization in Acute Kidney Injury**
  [[📝 Paper](https://www.sciltp.com/journals/aim/articles/2602002965)]

- (*arXiv'25*) **Evolving Diagnostic Agents in a Virtual Clinical Environment**
  [[📝 Paper](https://arxiv.org/abs/2510.24654)]

### Surgical Simulation and Embodied Healthcare

- (*arXiv'26*) **NVIDIA Cosmos-H-Dreams: Real-Time Generative Physics Simulation for Surgical Robotics**
  [[📝 Paper](https://arxiv.org/abs/2608.24199)] [[💻 Code](https://github.com/isaac-for-healthcare/Cosmos-H-Dreams)] [[🌐 Weights](https://huggingface.co/nvidia/Cosmos-H-Dreams)]

- (*arXiv'26*) **Progressive Experience Fusion for Multi-Task World Model Control in Endovascular Navigation**
  [[📝 Paper](https://arxiv.org/abs/2608.18647)]

- (*arXiv'26*) **Surgical WAM: A World-Action Model for Data-Efficient Surgical Robot Learning**
  [[📝 Paper](https://arxiv.org/abs/2608.11204)]

- (*arXiv'26*) **Stable Long-Horizon Neural ODE Reduced-Order Models via Learned Feedback for Biological Growth and Remodeling**
  [[📝 Paper](https://arxiv.org/abs/2604.13820)] [[💻 Code](https://github.com/joel-laudo/TE-skin-NODE-ROM)]

- (*Nat Mach Intell'25*) **Model-Based Reinforcement Learning for Ultrasound-Driven Autonomous Microrobots**
  [[📝 Paper](https://doi.org/10.1038/s42256-025-01054-2)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/40709099/)] [[💻 Code](https://github.com/M-Medany/Model-Based-Reinforcement-Learning-for-Ultrasound-Driven-Autonomous-Microrobots)]

- (*Med Image Anal'26 Online*) **Towards Patient-Specific Optimization for Mandibular Reconstruction Planning Based on Predicted Bone-Union Propensity**
  [[📝 Paper](https://doi.org/10.1016/j.media.2026.104281)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42700676/)] [[📝 Preprint](https://arxiv.org/abs/2605.01084)] [[💻 Code](https://github.com/hamidreza-aftabi/OsteoOpt)]

- (*arXiv'26*) **S2-HWM: Sparse Event-Structured Hierarchical World Model for Long-Horizon Surgical Robot Manipulation**
  [[📝 Paper](https://arxiv.org/abs/2608.13103)]

- (*arXiv'26*) **CrossScope: A Role-Asymmetric World Model for Joint Dual-Scope Surgical Video Prediction**
  [[📝 Paper](https://arxiv.org/abs/2608.03211)]

- (*arXiv'26*) **EndoWAM: A Grounded World-Action Model for Generalizable Endoscopic Navigation**
  [[📝 Paper](https://arxiv.org/abs/2608.01221)]

- (*arXiv'26*) **Failure Detection for Surgical Robot Imitation Policies via Flow-Matching World Modeling**
  [[📝 Paper](https://arxiv.org/abs/2607.27511)]

- (*Oper Neurosurg'26*) **Iterative Virtual and Physical Simulation for Staged Separation of Total Vertical Craniopagus: The Avatar Patient Approach to Conjoined Twins**
  [[📝 Paper](https://doi.org/10.1227/ons.0000000000002116)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42318872/)]

- (*arXiv'26*) **SurgVista: Long-Horizon Surgical World Modeling with Plausible Instrument-Tissue Dynamics**
  [[📝 Paper](https://arxiv.org/abs/2606.19889)]

- (*arXiv'26*) **SWoMo: Neuro-Symbolic World Model for Cataract Surgery Simulation**
  [[📝 Paper](https://arxiv.org/abs/2605.16530)] [[🌐 Project](https://ssharvienkumar.github.io/SWoMo/)]

- (*arXiv'26*) **Toward Safe Autonomous Robotic Endovascular Interventions using World Models**
  [[📝 Paper](https://arxiv.org/abs/2604.20151)]

- (*arXiv'26*) **SAW: Toward a Surgical Action World Model via Controllable and Scalable Video Generation**
  [[📝 Paper](https://arxiv.org/abs/2603.13024)]

- (*ICLR'26 Rejected*) **Unified Surgical World Model for Structured Understanding, Long-Horizon Prediction, and Fine-Grained Generation**
  [[📝 Paper](https://openreview.net/forum?id=Kk9t5empEf)]

- (*MIDL'26 rejected*) **Learning Action-Conditioned World Models for Cataract Surgery from Unlabeled Videos (SurgWorld)**
  [[📝 Paper](https://openreview.net/forum?id=aYQYOVm2AB)]

- (*medRxiv'26*) **MedOS: AI-XR-Cobot World Model for Clinical Perception and Action**
  [[📝 Paper](https://www.medrxiv.org/content/10.64898/2026.02.18.26345936v1)]

- (*arXiv'26*) **Open-H-Embodiment: A Large-Scale Dataset for Enabling Foundation Models in Medical Robotics**
  [[📝 Paper](https://arxiv.org/abs/2604.21017)] [[💻 Code](https://huggingface.co/nvidia/Cosmos-H-Surgical-Simulator)] [[💻 Code](https://github.com/NVIDIA-Medtech/Cosmos-H-Surgical-Simulator)] [[🌐 Project](https://open-h.github.io/open-h-embodiment/)]

- (*arXiv'25*) **Cosmos-H-Surgical: Learning Surgical Robot Policies from Videos via World Modeling**
  [[📝 Paper](https://arxiv.org/abs/2512.23162)] [[💻 Code](https://huggingface.co/nvidia/Cosmos-H-Surgical-Simulator)] [[💻 Code](https://github.com/nvidia-cosmos/cosmos-cookbook)]

- (*arXiv'25*) **Cosmos-Surg-dVRK: World Foundation Model-based Automated Online Evaluation of Surgical Robot Policy Learning**
  [[📝 Paper](https://arxiv.org/abs/2510.16240)]

- (*MICCAI'25*) **World Model for AI Autonomous Navigation in Mechanical Thrombectomy**
  [[📝 Paper](https://arxiv.org/abs/2509.25518)]

- (*arXiv'25*) **Visuomotor Grasping with World Models for Surgical Robots**
  [[📝 Paper](https://arxiv.org/abs/2508.11200)]

- (*arXiv'25*) **Towards Suturing World Models: Learning Predictive Models for Robotic Surgical Tasks**
  [[📝 Paper](https://arxiv.org/abs/2503.12531)] [[🌐 Project](https://mkturkcan.github.io/suturingmodels/)]

- (*MICCAI Workshop'25*) **Surgical Vision World Model**
  [[📝 Paper](https://arxiv.org/abs/2503.02904)] [[💻 Code](https://github.com/bhattarailab/Surgical-Vision-World-Model)]

- (*arXiv'24*) **World Models for General Surgical Grasping**
  [[📝 Paper](https://arxiv.org/abs/2405.17940)]

---

## 🧰 Datasets, Benchmarks and Simulators

> This resource index is narrower than a general medical AI directory. Datasets must support at least one qualifying medical world model, benchmarks must evaluate dynamics or rollouts, and simulators must expose an implementation that advances a medical state. Inclusion here does not place a dataset-only or benchmark-only paper in the main paper list.

### Datasets

| Resource | Domain | World-model use | Access |
|---|---|---|---|
| **Open-H-Embodiment** | Surgical robotics | Synchronized video and robot kinematics across multiple clinical platforms for training action-conditioned surgical rollouts. | [[📦 Dataset](https://huggingface.co/datasets/nvidia/PhysicalAI-Robotics-Open-H-Embodiment)] [[🌐 Project](https://open-h.github.io/open-h-embodiment/)] [[📝 Paper](https://arxiv.org/abs/2604.21017)] |
| **MIMIC-IV** | Longitudinal EHR | Timestamped hospital and ICU trajectories used for treatment-conditioned patient simulation, including the SepsisAgent clinical world model. | [[📦 Dataset](https://physionet.org/content/mimiciv/3.0/)] [[📝 Example](https://arxiv.org/abs/2605.14723)] |
| **MIMIC-IV-ECG** | Cardiac electrophysiology | ECGs linked to clinical records for learning event-conditioned cardiac state transitions. | [[📦 Dataset](https://physionet.org/content/mimic-iv-ecg/1.0/)] [[📝 Example](https://arxiv.org/abs/2604.22618)] |
| **ISLES 2017** | Cerebral perfusion MRI | Perfusion-weighted time series and reference maps used by the HemoPIC cerebral hemodynamics digital twin. | [[📦 Dataset](https://zenodo.org/records/17736412)] [[💻 HemoPIC](https://github.com/jhuldr/HemoPIC)] |

### Benchmarks

| Benchmark | Domain | What it evaluates | Availability |
|---|---|---|---|
| **SurgWMBench** | Surgical instrument motion | Short-horizon trajectory prediction, recursive rollout stability, and perturbation robustness on SAR-RARP50 suturing clips; distinguishes image-conditioned from fully predictive rollout settings. | [[📝 Paper specification](https://arxiv.org/abs/2608.08070)] `Paper only` |
| **Open-H Multi-Embodiment Surgical Benchmark** | Surgical robotics | Action-conditioned future-video fidelity across nine robot embodiments using frame decay, tool consistency, and tool displacement metrics. | [[📦 Data](https://huggingface.co/datasets/nvidia/PhysicalAI-Robotics-Open-H-Embodiment)] [[💻 Evaluation](https://github.com/NVIDIA-Medtech/Cosmos-H-Surgical-Simulator)] |
| **UniSWM-Bench** | Surgical workflow and video | Five understanding tasks, two long-horizon prediction tasks, and three action- or movement-conditioned generation tasks. | [[📝 Paper specification](https://openreview.net/forum?id=Kk9t5empEf)] `Paper only` |
| **SurgVeo and Surgical Plausibility Pyramid** | Surgical video | Expert assessment of generated rollouts at 1, 3, and 8 seconds across visual, instrument-operation, environment-feedback, and surgical-intent plausibility. | [[📝 Paper and protocol](https://arxiv.org/abs/2511.01775)] `Paper only` |

### Simulators

| Simulator | Medical state | Rollout interface | Access |
|---|---|---|---|
| **Cosmos-H-Dreams** | Surgical video and robot state | Streams action-conditioned video chunks and returns generated observations to a robot policy for interactive closed-loop rollouts; released with serving code and model weights. | [[💻 Code](https://github.com/isaac-for-healthcare/Cosmos-H-Dreams)] [[🌐 Weights](https://huggingface.co/nvidia/Cosmos-H-Dreams)] [[📝 Paper](https://arxiv.org/abs/2608.24199)] |
| **Lung CT Monte Carlo Workflow** | Light transport in patient-specific thoracic tissues | Propagates photons through CT-derived lung anatomy to simulate 3D fluence under alternative illumination and tissue conditions; dosimetry only, not longitudinal disease or treatment-response prediction. | [[💻 Code](https://github.com/JohanDiazTovar/Monte-Carlo-Modeling-of-Light-Propagation-in-Healthy-and-Diseased-Human-Lungs)] [[📝 Paper](https://doi.org/10.1073/pnas.2612370123)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42574619/)] |
| **Cosmos-H-Surgical-Simulator** | Surgical scene and robot state | Generates future surgical video from an initial frame and robot-kinematic action sequence across multiple embodiments. | [[💻 Code](https://github.com/NVIDIA-Medtech/Cosmos-H-Surgical-Simulator)] [[🌐 Weights](https://huggingface.co/nvidia/Cosmos-H-Surgical-Simulator)] |
| **HemoPIC** | Cerebral hemodynamics | Fits patient-specific tracer transport and rolls perfusion dynamics through a physics-informed digital twin; includes a runnable demo. | [[💻 Code and demo](https://github.com/jhuldr/HemoPIC)] [[📝 Paper](https://arxiv.org/abs/2607.08799)] |
| **MeWM** | Liver tumor state | Synthesizes treatment-conditioned post-intervention tumor states for TACE planning and survival analysis. | [[💻 Code](https://github.com/scott-yjyang/MeWM)] [[🌐 Project](https://yijun-yang.github.io/MeWM/)] |
| **SepsisAgent Clinical World Model** | ICU patient state | Simulates counterfactual patient trajectories under candidate fluid and vasopressor interventions. | [[💻 Code](https://github.com/FreedomIntelligence/SepsisAgent)] [[📝 Paper](https://arxiv.org/abs/2605.14723)] |
| **Brain-WM** | Glioblastoma and longitudinal MRI | Couples treatment planning with treatment-conditioned future MRI generation for disease-progression simulation. | [[💻 Code](https://github.com/thibault-wch/Brain-GBM-world-model)] [[📝 Paper](https://arxiv.org/abs/2603.07562)] |

---

## 🔗 Related Repositories

- **Awesome-Self-Evolving-AI-for-Agentic-Healthcare**
  [[💻 Repository](https://github.com/ZhihaoPENG-CityU/Awesome-Self-Evolving-AI-for-Agentic-Healthcare)]

- **knightnemo/Awesome-World-Models**
  [[💻 Repository](https://github.com/knightnemo/Awesome-World-Models)]

- **LMD0311/Awesome-World-Model**
  [[💻 Repository](https://github.com/LMD0311/Awesome-World-Model)]

---

## 🔀 Cross-References

> Adjacent work on world-model–augmented agents and MCP tool simulation—not healthcare-specific, but relevant for clinical agentic systems (see [Related Repositories](#-related-repositories) above).

- (*arXiv'26*) **MCP-Cosmos: World Model-Augmented Agents for Complex Task Execution in MCP Environments**
  [[📝 Paper](https://arxiv.org/abs/2605.09131)]
  > BYOWM framework: agents simulate MCP tool state transitions in latent space before execution (IBM).

---

<a id="industry-models-platforms"></a>

## 🏭 Industry Models / Platforms

- (*NVIDIA'25*) **Cosmos World Foundation Model**
  [[🌐 Platform](https://developer.nvidia.com/cosmos)] [[📝 Research](https://research.nvidia.com/labs/dir/cosmos1/)]
  > General-purpose world foundation model platform; extended to surgical simulation via **Cosmos-H-Surgical** and **Cosmos-H-Surgical-Simulator** (see [papers above](#surgical-simulation-and-embodied-healthcare)).

- (*NVIDIA'25*) **Holoscan AI Platform**
  [[🌐 Platform](https://docs.nvidia.com/holoscan/sdk-user-guide/index.html)]
  > Real-time AI inference platform for surgical robotics and medical device integration, enabling world-model-based decision support in the operating room.

- (*Siemens Healthineers'25*) **Digital Twin for Healthcare**
  [[🌐 Platform](https://www.siemens-healthineers.com/digital-health)]
  > Patient-specific digital twin technology for cardiac modeling, radiation therapy planning, and clinical decision support.

- (*OpenAI'26*) **GPT-Rosalind**
  [[📝 Blog](https://openai.com/index/introducing-gpt-rosalind/)] [[🌐 Life Sciences](https://openai.com/solutions/industries/life-sciences/)] [[🔗 Request access](https://openai.com/form/life-sciences-access/)] [[💻 Codex plugin](https://github.com/openai/plugins/tree/main/plugins/life-science-research)]

---

## 📣 Special Issues / Calls

### 2026

- **IEEE Transactions on Medical Imaging Special Issue on Large Multimodal & World Models in Medical Imaging**
  [[🌐 Call](https://ieeetmi.org/special-issue-world-model/)]

---

## ⭐ Star History

[View this repository's star history on Star History](https://www.star-history.com/?repos=chengwang96%2FAwesome-World-Models-for-Healthcare&type=date&logscale=&legend=bottom-right).

---

## ⚖️ License

This repository uses separate licenses for content and code:

- **Catalog content ([CC BY 4.0](LICENSE-CONTENT)):** `README.md`, `CONTRIBUTING.md`, `CITATION.cff`, the pull request and issue templates, and original material in `assets/`, including the taxonomy, metadata, annotations, and qualification notes.
- **Code ([MIT](LICENSE)):** source code in `scripts/` and `tests/`, automation in `.github/workflows/`, and repository configuration such as `.lychee.toml`.

Linked or quoted papers, code repositories, datasets, trademarks, and other third-party materials retain their original rights and licenses; their inclusion here does not relicense them.

This content/code split applies to this revision and subsequent contributions. Earlier repository revisions remain available under the license notices included with those revisions.

---

## 📖 Citation

If this catalog supports your research, please cite the repository using the metadata in [CITATION.cff](CITATION.cff). GitHub also provides ready-to-use APA and BibTeX formats through **Cite this repository**.

---

## 🤝 Contributing

Contributions are welcome. Please read the [contribution guide](CONTRIBUTING.md) before proposing a paper or resource. Main-list paper submissions must provide source-grounded evidence for the modeled state, transition dynamics, rollout capability, and medical task. You can submit a pull request or [suggest a paper through the structured issue form](https://github.com/chengwang96/Awesome-World-Models-for-Healthcare/issues/new?template=01-paper-suggestion.yml).

Entry format:

```markdown
- (*Venue'YY*) **Paper Title**
  [[📝 Paper](link)] [[💻 Code](link)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate + Plan` · `Assets: Code`
  > **Why it qualifies:** Learns intervention-conditioned patient-state transitions and uses rollouts to compare treatment plans.
```

The pull request template includes the required scope evidence and review checklist. Conceptual work belongs under Survey Papers; static representation learning, ordinary conditional generation, benchmark-only work, and other audited boundary cases are not counted in the main list.

---

## ✉️ Contact Us

If you have any questions or suggestions, please feel free to contact us via:

**Email:** chengwang@link.cuhk.edu.hk, zhihaopeng@cuhk.edu.hk
