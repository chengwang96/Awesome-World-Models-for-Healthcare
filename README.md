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

<a id="-scope"></a>

## 🎯 Scope and Taxonomy

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

### 🧬 Taxonomy

Each main-list paper carries compact, controlled metadata so that methods with comparable modeled states and capabilities are easy to find.

| Field | Values | Meaning |
|---|---|---|
| **State** | `Patient`, `Physiology`, `Anatomy`, `Medical image`, `Procedure/Robot`, `Clinical workflow`, `Cell`, `Molecule`, `Population` | The primary medical or biological state advanced by the model. |
| **Dynamics** | `Temporal`, `Action-conditioned`, `Mechanistic`, `Spatial/view`, `Event sequence` | The transition structure implemented by the method. Multiple values may apply. |
| **Capability** | `Forecast`, `Simulate`, `Counterfactual`, `Plan`, `Control` | What the model's rollouts are used to accomplish. |
| **Assets** | `Code`, `Weights`, `Project`, `Paper only` | Public implementation or project resources linked by the paper entry. |

The labels describe demonstrated method capabilities, not claims inferred from a paper title.

---

## 📌 Contents

- [Scope and Taxonomy](#-scope)
- [Survey Papers](#-survey-papers)
- [World Model Papers](#-world-model-papers)
- [By Topic](#-by-topic)
- [Resources](#resources)
- [Special Issues / Calls](#-special-issues--calls)
- [Project Information](#project-information)

---

## 📚 Survey Papers

- (*arXiv'26 Perspective*) **Digital Twins for Clinical Development: A Five-Level Framework from Prognostic Adjustment to In-Silico Trials**
  [[📝 Paper](https://arxiv.org/abs/2611.10888)]

- (*Ann Biomed Eng'26 Perspective*) **World Foundation Models and Agentic AI in Medicine: Physiological Simulation, Digital Twins, and Clinical Decision-Making**
  [[📝 Paper](https://doi.org/10.1007/s10439-026-04445-7)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42993397/)]

- (*J Imaging Inform Med'26 Perspective*) **Toward Verifiable Medical Imaging World Models: An Engineering Framework for Evaluating Simulation Fidelity, Roll-Out Stability, and Clinical Plausibility**
  [[📝 Paper](https://doi.org/10.1007/s10278-026-02413-0)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42907729/)]

- (*arXiv'26 Perspective*) **From Prediction to Action: Population Health World Model for Digital Medicine**
  [[📝 Paper](https://arxiv.org/abs/2610.24662)]

- (*arXiv'26 Perspective*) **Rethinking World Models for Biosignals**
  [[📝 Paper](https://arxiv.org/abs/2610.17510)]

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

- (*arXiv'26*) **Medical world models in healthcare: capabilities, evidence, and trustworthy clinical translation**
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

- (*medRxiv'26*) **An agent-based model of Epstein-Barr virus transmission and vaccination**
  [[📝 Paper](https://www.medrxiv.org/content/10.64898/2026.11.10.26367734v1)]
  **Metadata:** `State: Population` · `Dynamics: Temporal + Action-conditioned + Mechanistic` · `Capability: Simulate + Counterfactual` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>A 10,000-agent age-structured model advances EBV infection and infectious-mononucleosis states under vaccination scenarios, calibrated to U.S. seroprevalence and used to project 100-year vaccine profiles; the scenario comparisons are model projections, and no public code or prospective validation is reported.</p>
  </details>

- (*medRxiv'26*) **Prediction of Subsolid Pulmonary Nodule Evolution from Baseline CT Using Temporal Imaging Models**
  [[📝 Paper](https://www.medrxiv.org/content/10.64898/2026.08.12.26360292v2)]
  **Metadata:** `State: Medical image` · `Dynamics: Temporal` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>An interval-aware model predicts future subsolid-nodule growth and a temporally conditioned generative model synthesizes future lesion morphology from baseline CT, evaluated on 24,946 longitudinal scan pairings from 426 patients; the study is retrospective and single-center, and no treatment action is modeled.</p>
  </details>

- (*arXiv'26*) **ProTEUS: A mutation-resolved world model for closed-loop protein evolution**
  [[📝 Paper](https://arxiv.org/abs/2611.13348)] [[💻 Code](https://github.com/yikunpku/ProTEUS)]
  **Metadata:** `State: Molecule` · `Dynamics: Event sequence + Action-conditioned` · `Capability: Forecast + Plan` · `Assets: Code`
  <details>
  <summary>Why it qualifies</summary>
  <p>Represents protein variants as latent states and mutations as actions, predicts activity across higher-order variants, and uses the model in five-round active-learning simulations and two closed-loop wet-lab engineering campaigns; the transition is mutation-induced variant state, not a physical folding trajectory.</p>
  </details>

- (*arXiv'26*) **stMIND: Learning multiscale interaction dynamics from spatial-temporal transcriptomics**
  [[📝 Paper](https://arxiv.org/abs/2611.12228)] [[💻 Code](https://github.com/LongquanLi135/stMIND)]
  **Metadata:** `State: Cell` · `Dynamics: Temporal` · `Capability: Forecast + Simulate` · `Assets: Code`
  <details>
  <summary>Why it qualifies</summary>
  <p>An interacting neural SDE infers coupled expression, spatial-migration, and proliferation dynamics from unmatched spatial transcriptomic snapshots, and evaluates held-out forecasts in axolotl regeneration and zebrafish embryogenesis; the model is observational and does not test treatment or perturbation interventions.</p>
  </details>

- (*J Sleep Res'26*) **Development of a Digital Twin to Analyse Waiting Lists in a Sleep-Disordered Breathing Unit**
  [[📝 Paper](https://doi.org/10.1111/jsr.70489)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/43000229/)]
  **Metadata:** `State: Clinical workflow` · `Dynamics: Temporal + Event sequence` · `Capability: Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>A stochastic discrete-event model advances patients through six sleep-medicine care stages with service times and priority rules, calibrated on 2024 operational data and checked against 2025 waiting-time and queue-length records; capacity what-ifs are simulated, but prospective deployment and clinical outcomes are not evaluated.</p>
  </details>

- (*arXiv'26*) **ICare-DT: a digital twin for continuous forecasting of intensive care patients**
  [[📝 Paper](https://arxiv.org/abs/2611.09712)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal` · `Capability: Forecast` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>A Transformer keeps a 64-dimensional latent patient state, re-reads each new ICU hour without retraining, and issues 1–48 h competing-risk forecasts for vital-sign threshold crossings, discharge, or death; eICU-CRD evaluation includes a registered MIMIC-IV transfer read, while treatment-response prediction remains a semi-synthetic benchmark and no tested action-conditioned policy is claimed.</p>
  </details>

- (*bioRxiv'26*) **Virtual dynamics of spatiotemporal single-cell interactions**
  [[📝 Paper](https://www.biorxiv.org/content/10.64898/2026.11.04.764438v1)]
  **Metadata:** `State: Cell` · `Dynamics: Temporal` · `Capability: Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>An unbalanced mean-field Schrödinger bridge learns continuous cell-state, position, and population-size trajectories from sparse spatial transcriptomic snapshots, with ligand–receptor interaction and growth terms; five datasets test unmeasured-stage generation and in silico perturbation responses. The perturbations are hypothesis-generating, not experimentally validated interventions.</p>
  </details>

- (*arXiv'26*) **Learning a patient world model for health system simulation in intensive care**
  [[📝 Paper](https://arxiv.org/abs/2611.08392)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Event sequence` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>A frozen autoregressive model advances sparse ICU state–event histories to simulator-requested times, generating admission demand, organ-support events, and discharge proposals inside a discrete-event ICU; 14-day virtual cohorts reproduce occupancy and policy responses on MIMIC-IV, but service capacities and times are calibrated assumptions and policy effects remain observational.</p>
  </details>

- (*arXiv'26*) **Personalized health coaching via coachable health age and counterfactual wearable trajectories**
  [[📝 Paper](https://arxiv.org/abs/2611.08568)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Action-conditioned` · `Capability: Forecast + Simulate + Counterfactual + Plan` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>A latent second-order transition operator conditioned on steps, sleep, and exercise rolls weekly wearable physiology forward for 12 weeks, and alternative action sequences feed a constrained coaching planner; 2.2 million person-weeks support pretraining and expert review supports plan quality, but alternative trajectories are model projections, not identified behavioral effects.</p>
  </details>

- (*medRxiv'26*) **Risk-benefit assessment of oral anticoagulation in atrial fibrillation using virtual clinical trials**
  [[📝 Paper](https://www.medrxiv.org/content/10.64898/2026.11.04.26367324v1)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Action-conditioned + Mechanistic` · `Capability: Simulate + Counterfactual` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>A lifetime state-transition model moves virtual atrial-fibrillation populations through stroke, major bleeding, and death under screening-triggered, continuous, or pill-in-pocket anticoagulation, reproducing event rates across scenarios; strategy comparisons are model-based projections assembled from multiple clinical sources, not a randomized trial.</p>
  </details>

- (*arXiv'26*) **SurgTransfer: Multi-Step Latent Action Modeling for Action Transfer in Surgical World Model**
  [[📝 Paper](https://arxiv.org/abs/2611.05443)] [[💻 Code](https://github.com/bhattarailab/Surgical-Vision-World-Model)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate` · `Assets: Code`
  <details>
  <summary>Why it qualifies</summary>
  <p>Transfers video-derived latent action sequences to an initial surgical frame and simulates subsequent scene evolution, evaluating 14-frame continuations and surgeon-rated plausibility on SurgToolLoc and PitVis; actions are prerecorded latent trajectories, not interactive robot commands.</p>
  </details>

- (*arXiv'26*) **PulmoWorld: An Asynchronous Multimodal Medical World Model for Longitudinal Pneumonia Dynamics**
  [[📝 Paper](https://arxiv.org/abs/2610.38289)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Action-conditioned` · `Capability: Forecast + Simulate + Plan` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Propagates and observation-corrects a multimodal patient belief, evaluates four-step clinical and representation forecasts on separately fitted pneumonia cohorts, and selects actions through imagined continuations; planning is tested only in known-mechanism MASS-Syn, not as a validated clinical treatment policy.</p>
  </details>

- (*Cell Rep Med'26*) **Tumor digital twins uncover therapeutic strategies in triple-negative breast cancer**
  [[📝 Paper](https://doi.org/10.1016/j.xcrm.2026.103119)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42933397/)] [[💻 Code](https://github.com/jfisher-lab/TNBC_Victori2026)]
  **Metadata:** `State: Cell` · `Dynamics: Mechanistic + Action-conditioned` · `Capability: Simulate + Plan` · `Assets: Code`
  <details>
  <summary>Why it qualifies</summary>
  <p>Computes synchronous signaling-network transitions under patient-genomic and drug perturbations, using attractor phenotypes to reproduce treatment responses and screen resensitizing targets; update steps have no calibrated clinical time, and nominated regimens are not prospectively validated.</p>
  </details>

- (*medRxiv'26*) **Digital Twin Workflow for Continuous Glucose Forecasting: Real-Time Data Assimilation Using Reinforcement Learning**
  [[📝 Paper](https://www.medrxiv.org/content/10.64898/2026.10.23.26366163v1)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal` · `Capability: Forecast` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Extends the earlier septic-patient glucose twin with bounded first-step residual correction and recursively propagated 15-step forecasts, evaluating ten ICU patients retrospectively; the RL action adjusts a prediction, not insulin delivery or physiological treatment.</p>
  </details>

- (*arXiv'26*) **DuoPIC: Uncertainty-Aware Voxel-Level Digital Twins of Cerebral Perfusion with Transport PDEs in Acute Stroke**
  [[📝 Paper](https://arxiv.org/abs/2610.33071)] [[💻 Code](https://github.com/detinatran/duopic)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Mechanistic` · `Capability: Simulate` · `Assets: Code`
  <details>
  <summary>Why it qualifies</summary>
  <p>Couples regional blood flow to time-evolving tracer transport with a learned closure, evaluating masked temporal blocks and patient-held-out dynamics alongside stroke lesion maps; refitting on remaining frames is not a prospective clinical forecast or validated reperfusion-treatment simulation.</p>
  </details>

- (*arXiv'26*) **Forecasting Patient Trajectories from the Electronic Health Records with Action-Conditioned World Models**
  [[📝 Paper](https://arxiv.org/abs/2610.23862)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Action-conditioned` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>A state-dependent linearization propagates latent patient-state increments under recorded ICU actions, supports free-running multi-step rollouts decoded to vital signs and laboratory values, and responds to perturbed action sequences; MIMIC-IV forecasting and downstream risk tests are observational, so action sensitivity is not a causal treatment effect.</p>
  </details>

- (*arXiv'26*) **Saga: an in silico ontology for a multimodal patient world model**
  [[📝 Paper](https://arxiv.org/abs/2610.33054)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Event sequence + Action-conditioned` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Advances shared oncology patient states by generating events and times, appending them to history and re-encoding for eight-step free rollouts, with separate paired follow-up image evaluations; treatment-conditioned outputs do not establish causal treatment effects or planning benefit.</p>
  </details>

- (*arXiv'26*) **CaMeWM: A Causal Medical World Model for Generative Tumor Evolution and Treatment Planning**
  [[📝 Paper](https://arxiv.org/abs/2610.26923)]
  **Metadata:** `State: Medical image` · `Dynamics: Action-conditioned` · `Capability: Forecast + Simulate + Plan` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Simulates a lesion-local follow-up CT state under a supported TACE regimen and ranks sampled worlds by survival utility, evaluating factual transitions and observational policy value in 79 episodes; this is a single post-treatment transition, not an evaluated sequential treatment policy or prospective benefit.</p>
  </details>

- (*Protein Sci'26*) **DreamFold: A World Model to efficiently generate protein folding pathways in the latent space**
  [[📝 Paper](https://doi.org/10.1002/pro.70794)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42813590/)] [[📝 Preprint](https://www.biorxiv.org/content/10.1101/2025.03.26.645554v1)]
  **Metadata:** `State: Molecule` · `Dynamics: Event sequence + Action-conditioned` · `Capability: Simulate + Plan` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Evolves latent protein conformations under dihedral moves and learns folding policies through imagined rollouts, comparing decoded pathways with molecular simulations and experimental structures; trajectories do not directly yield physical kinetics or thermodynamics.</p>
  </details>

- (*arXiv'26*) **SonoWorld: Towards Interactive Pose-Controllable Ultrasound World Models**
  [[📝 Paper](https://arxiv.org/abs/2610.19327)] [[🌐 Project](https://iclr2027anonymous.github.io/SonoWorld/)]
  **Metadata:** `State: Medical image` · `Dynamics: Spatial/view + Action-conditioned` · `Capability: Simulate + Plan` · `Assets: Project`
  <details>
  <summary>Why it qualifies</summary>
  <p>Generates future ultrasound views conditioned on probe motion and tests held-out tracked thyroid-scan rollouts and candidate direction ranking; the action-grounded set is small and no physical robot closed-loop navigation is shown.</p>
  </details>

- (*medRxiv'26*) **Informing risk stratification and vaccine policy via a predictive mathematical model of SARS-COV-2 infection**
  [[📝 Paper](https://www.medrxiv.org/content/10.64898/2026.10.12.26365315v1)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Mechanistic` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>A within-host ODE advances viral and immune states through infection, with kinetics fitted to a human challenge cohort and an antibody-effect prediction checked against a separate challenge cohort; vaccine-policy scenarios remain model projections.</p>
  </details>

- (*bioRxiv'26*) **scMTG reconstructs single-cell temporal dynamics with Markov transition generators**
  [[📝 Paper](https://www.biorxiv.org/content/10.64898/2026.06.04.730241v2)] [[💻 Code](https://github.com/liuq-lab/scMTG)]
  **Metadata:** `State: Cell` · `Dynamics: Temporal` · `Capability: Forecast + Simulate` · `Assets: Code`
  <details>
  <summary>Why it qualifies</summary>
  <p>Learns composable generative transitions between sampled single-cell time points and evaluates reconstruction of withheld intermediate populations across six datasets; inferred trajectories do not establish causal gene regulation or treatment effects.</p>
  </details>

- (*medRxiv'26*) **FERMAT: An Autoregressive Clinical Foundation Model for Disease Risk and Clinical Event Prediction**
  [[📝 Paper](https://www.medrxiv.org/content/10.64898/2026.10.11.26365210v1)]
  **Metadata:** `State: Patient` · `Dynamics: Event sequence + Temporal` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Recursively generates clinical events and inter-event times from longitudinal EHR history, evaluating next-record events and disease risk; generated trajectories underperform representation-based five-year risk prediction and are not treatment-conditioned.</p>
  </details>

- (*arXiv'26*) **PatientWM: Towards Generalizable Clinical World Models via Unified Patient States**
  [[📝 Paper](https://arxiv.org/abs/2610.17059)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Action-conditioned` · `Capability: Forecast + Simulate + Plan` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Recursively advances latent patient states under recorded clinical actions and evaluates factual multistep forecasts across EHR cohorts; candidate-action ranking uses a narrow retrospective choice set and does not validate counterfactual effects or treatment benefit.</p>
  </details>

- (*bioRxiv'26*) **Mechanistic prediction of fecal microbiota transplant engraftment and Clostridioides difficile colonization resistance with μODE**
  [[📝 Paper](https://www.biorxiv.org/content/10.64898/2026.10.09.758137v1)] [[💻 Code](https://github.com/cumbof/muODE)]
  **Metadata:** `State: Population` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Simulate` · `Assets: Code`
  <details>
  <summary>Why it qualifies</summary>
  <p>Couples microbial metabolic fluxes to extracellular-metabolite and community-state updates under antibiotics or donor transfer, comparing simulated shifts with longitudinal FMT data; it captures the direction of pathobiont suppression but has composition bias and no clinical efficacy validation.</p>
  </details>

- (*bioRxiv'26*) **A tissue time machine to forward-predict single-timepoint data applied to tuberculosis granulomas**
  [[📝 Paper](https://www.biorxiv.org/content/10.64898/2026.10.09.758083v1)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Mechanistic` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Matches observed nonhuman-primate granulomas to agent-based infection trajectories and propagates immune and bacterial states toward later outcomes; historical aggregate data support the simulator, but 22/28 is agreement among simulated partners, not accuracy against later observations of the same tissue.</p>
  </details>

- (*arXiv'26*) **Finsler Flow Matching: Dynamics-Aware Geodesic Interpolation for Single-Snapshot Trajectory Inference**
  [[📝 Paper](https://arxiv.org/abs/2610.11318)] [[💻 Code](https://github.com/mlbelab/FinslerFlowMatching)]
  **Metadata:** `State: Cell` · `Dynamics: Temporal` · `Capability: Forecast + Simulate` · `Assets: Code`
  <details>
  <summary>Why it qualifies</summary>
  <p>Learns a continuous stochastic cell-state transition process from a directed Markov graph and integrates it to recover withheld intermediate pancreatic-cell populations; this is differentiation-trajectory inference, not a tested treatment simulator.</p>
  </details>

- (*arXiv'26*) **Sign-Constrained Intervention Effects for Domain-Generalizable ICU World Models**
  [[📝 Paper](https://arxiv.org/abs/2610.11090)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Action-conditioned` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>PhysioWorld recurrently advances ICU vital-sign states under explicit drug and ventilator events, with eight-step free-running forecasts and dose-perturbation tests across MIMIC and VitalDB cohorts; observational evaluations do not identify causal treatment effects.</p>
  </details>

- (*arXiv'26*) **Similar Predictive Fit but Different Latent Dynamics: Characterizing Learned Dynamical Structure in Personalized Models of Brain Disorders**
  [[📝 Paper](https://arxiv.org/abs/2610.10850)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal` · `Capability: Forecast` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Fits subject-specific transition distributions over EEG-derived brain states and evaluates held-out next-state prediction plus epilepsy-associated transition structure; it does not test free-running disease forecasts, diagnosis, or interventions.</p>
  </details>

- (*arXiv'26*) **MD-LLM-2: A Transferable Language Model of Molecular Dynamics with Physical Conditioning and Explicit Path Probabilities**
  [[📝 Paper](https://arxiv.org/abs/2610.10879)]
  **Metadata:** `State: Molecule` · `Dynamics: Temporal` · `Capability: Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Autoregressively generates protein-conformation trajectories from molecular history, sequence, and physical conditions, evaluating unseen-domain structure and transition kinetics against molecular-dynamics references; no drug-efficacy or clinical task is claimed.</p>
  </details>

- (*arXiv'26*) **UltraWorld: Learning Interactive Ultrasound World Models from Untracked Clinical Videos with Acoustic Sampling Map**
  [[📝 Paper](https://arxiv.org/abs/2610.09785)] [[🌐 Project](https://ultraworld-project.github.io/)]
  **Metadata:** `State: Medical image` · `Dynamics: Spatial/view + Action-conditioned` · `Capability: Simulate + Plan` · `Assets: Project`
  <details>
  <summary>Why it qualifies</summary>
  <p>Self-distills an action-conditioned ultrasound observation model from clinical-video priors and anatomy-guided synthetic scans, then uses imagined probe-motion rollouts for local planning; closed-loop navigation is simulated, while real clinical frames support consistency tests only.</p>
  </details>

- (*arXiv'26*) **One Frame, Full Heartbeat: ECG-Free Cardiac Cine MRI Synthesis via Phase-Conditioned Flow Matching**
  [[📝 Paper](https://arxiv.org/abs/2610.09397)]
  **Metadata:** `State: Anatomy` · `Dynamics: Temporal` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Predicts phase-indexed cardiac displacement fields from an end-diastolic MRI frame and warps it into an unobserved cine cycle, evaluating ventricular volume and ejection-fraction trajectories on ACDC and external M&amp;Ms data; timing uses pathology-level templates, not measured patient-specific phase.</p>
  </details>

- (*arXiv'26*) **One Frame, Full Heartbeat: ECG-Free 4D Cardiac Cine MRI Synthesis via Radial-Decomposed Flow Matching**
  [[📝 Paper](https://arxiv.org/abs/2610.09185)]
  **Metadata:** `State: Anatomy` · `Dynamics: Temporal` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Extends phase-conditioned cardiac motion synthesis to 3D volumes with a radial-contraction prior and learned residual deformation, generating a 4D cycle from one end-diastolic volume and evaluating physiological motion and downstream imaging tasks; the canonical phase is population-derived.</p>
  </details>

- (*bioRxiv'26*) **Identifiable Inverse Optimal Transport for Single-Cell State Transitions**
  [[📝 Paper](https://www.biorxiv.org/content/10.64898/2026.10.01.756056v1)] [[💻 Code](https://github.com/XTSgreen/IOT-single-cell-paper)]
  **Metadata:** `State: Cell` · `Dynamics: Temporal` · `Capability: Forecast + Simulate` · `Assets: Code`
  <details>
  <summary>Why it qualifies</summary>
  <p>Learns cell-state transport and a continuous-time generator whose transition matrices propagate clone and population composition into future observations, including an independent CellTag experiment; treatment-response associations are not validated intervention rollouts.</p>
  </details>

- (*arXiv'26*) **ProCut: Probabilistic Cutting Topology for Autonomous Electrosurgical Tissue Dissection**
  [[📝 Paper](https://arxiv.org/abs/2610.07515)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Simulate + Control` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Advances a deforming tissue mesh under cutting actions with a differentiable mechanics simulator, updates cut-topology beliefs from observations, and uses them for closed-loop robot dissection; validation is in simulation and ex-vivo chicken skin, not patients, and the transition law is computed rather than learned.</p>
  </details>

- (*arXiv'26*) **HyperNSDE: Personalized Neural SDEs for Joint Static-Longitudinal Clinical Data Generation**
  [[📝 Paper](https://arxiv.org/abs/2610.07383)] [[💻 Code](https://github.com/perrinechassat/HyperNSDE)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal` · `Capability: Simulate` · `Assets: Code`
  <details>
  <summary>Why it qualifies</summary>
  <p>Simulates irregular patient trajectories through a personalized neural SDE with learned drift and diffusion, evaluated on colorectal-cancer and Parkinson's cohorts; this is baseline-conditioned synthetic trajectory generation, without observed-history updating or treatment-action effects.</p>
  </details>

- (*arXiv'26*) **APOD: Reasoning-Guided Agentic Population Ordinary Differential Equation Discovery for Pharmacological Digital Twins**
  [[📝 Paper](https://arxiv.org/abs/2610.06227)] [[💻 Code](https://gitlab.inria.fr/compo/apod)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Forecast + Simulate` · `Assets: Code`
  <details>
  <summary>Why it qualifies</summary>
  <p>Discovers and fits executable dose-driven ODEs for tumor and platelet states, forecasts thrombocytopenia from first-cycle data in an independent 19-patient cohort, and simulates alternative radioligand schedules; those unobserved schedule outcomes are model projections.</p>
  </details>

- (*arXiv'26*) **Ultrasound Operator Guidance Using World Modeling and Retrieval Based Action Planning**
  [[📝 Paper](https://arxiv.org/abs/2610.06008)]
  **Metadata:** `State: Medical image` · `Dynamics: Spatial/view + Action-conditioned` · `Capability: Simulate + Plan` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Plans multi-step carotid-probe motions over a learned image-state embedding and recorded action-state transitions, with retrospective navigation and a three-volunteer real-time feasibility study; the deployed transition operator is nonparametric retrieval, not a learned generative video model.</p>
  </details>

- (*npj Metab Health Dis'26*) **A Digital Twin for Tracking and Forecasting Glycemia with Septic Patients in ICUs**
  [[📝 Paper](https://doi.org/10.1038/s44324-026-00132-2)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42823439/)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal` · `Capability: Forecast` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>A time-series transformer pretrained on one patient's continuous glucose data forecasts the next 15–30 minutes from a 30-minute history; adaptation and rolling forecasts were evaluated retrospectively in ten other septic ICU patients, without insulin-conditioned simulation or treatment planning.</p>
  </details>

- (*arXiv'26*) **An Uncertainty-Guided Digital Twin Framework for Online Adaptive Proton Therapy in Head and Neck Cancer: A Feasibility Study**
  [[📝 Paper](https://arxiv.org/abs/2609.39010)]
  **Metadata:** `State: Anatomy` · `Dynamics: Temporal + Spatial/view` · `Capability: Forecast` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Reuses an already listed longitudinal deformation-transfer model to forecast treatment-day CT/contour ensembles and derive patient-specific margins; ten retrospective cases tested downstream proton-plan adaptation, which required treatment-day CT reoptimization.</p>
  </details>

- (*arXiv'26*) **Graph World Models for Constrained Epidemic Policy Planning**
  [[📝 Paper](https://arxiv.org/abs/2609.35545)] [[💻 Code](https://anonymous.4open.science/r/epimind-9706/README.md)]
  **Metadata:** `State: Population` · `Dynamics: Temporal + Action-conditioned` · `Capability: Forecast + Simulate + Plan` · `Assets: Code`
  <details>
  <summary>Why it qualifies</summary>
  <p>EpiMind recursively advances graph-coupled regional epidemic states under joint intervention sequences and plans resource-feasible allocations; evaluation combines simulated counterfactuals with retrospective U.S. surveillance forecasts, where unexecuted policy effects remain model-relative.</p>
  </details>

- (*arXiv'26*) **SurgGMF: Fully Causal Gaussian Motion Forecasting for Anticipatory Surgical Scene Rendering**
  [[📝 Paper](https://arxiv.org/abs/2609.34733)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Temporal` · `Capability: Forecast` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Predicts five future teacher-derived Gaussian geometry states from past surgical-scene motion and renders them without target-frame Gaussian attributes; evaluation spans 12 EndoNeRF/StereoMIS slices, with no action conditioning or end-to-end prospective deployment test.</p>
  </details>

- (*arXiv'26*) **Towards Surgical World-Action Modeling: A Preliminary Joint Visual-Trajectory Forecasting for Surgical Motion Planning**
  [[📝 Paper](https://arxiv.org/abs/2608.20284)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Temporal` · `Capability: Forecast` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Recursively predicts 15 future surgical visual states and instrument positions in three-step chunks on SurgWMBench; evaluated forecasts degrade with horizon, and the paper does not implement action-conditioned control.</p>
  </details>

- (*bioRxiv'26*) **AnnFlux: Object-Conditioned Neural Stochastic Differential Equations for Single-Cell Perturbation Dynamics**
  [[📝 Paper](https://www.biorxiv.org/content/10.64898/2026.09.01.748703v1)]
  **Metadata:** `State: Cell` · `Dynamics: Temporal + Action-conditioned` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Integrates an object-conditioned latent stochastic drift from control-cell states to later perturbed populations, recovering a held-out one-day EMT time point and testing unseen perturbation combinations; it does not evaluate sequential drug treatment.</p>
  </details>

- (*bioRxiv'26*) **MEGA-ODE: Learning Biologically Structured and Navigable Continuous Perturbation Dynamics from Sparse Omics**
  [[📝 Paper](https://www.biorxiv.org/content/10.64898/2026.08.05.742921v1)] [[💻 Code](https://github.com/Candlelight-XYJ/MEGA-ODE)]
  **Metadata:** `State: Cell` · `Dynamics: Temporal` · `Capability: Forecast + Simulate` · `Assets: Code`
  <details>
  <summary>Why it qualifies</summary>
  <p>Evolves transcriptomic and proteomic states through graph-constrained neural-ODE experts and evaluates held-out future-time profiles; virtual transcription-factor screens are in silico hypotheses rather than validated treatment effects.</p>
  </details>

- (*Cell'26*) **RegVelo: Gene-Regulatory-Informed Dynamics of Single Cells**
  [[📝 Paper](https://doi.org/10.1016/j.cell.2026.04.022)] [[💻 Code](https://github.com/theislab/regvelo)]
  **Metadata:** `State: Cell` · `Dynamics: Temporal + Action-conditioned` · `Capability: Forecast + Simulate` · `Assets: Code`
  <details>
  <summary>Why it qualifies</summary>
  <p>Learns gene-regulatory splicing dynamics and propagates CellRank transitions to terminal cell-fate probabilities after simulated transcription-factor knockouts; selected predictions were tested with CRISPR and Perturb-seq in developmental biology, without a disease or treatment endpoint.</p>
  </details>

- (*medRxiv'26*) **A World Model Simulates the Latent Dynamics of Human Health**
  [[📝 Paper](https://www.medrxiv.org/content/10.64898/2026.09.19.26363460v1)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>HealthFlux evolves a patient-health latent state by neural ODE between observations and revises it when measurements arrive; event-free state simulations forecast disease and mortality after one-to-five-year observation blackouts, without evaluating treatment counterfactuals.</p>
  </details>

- (*bioRxiv'26*) **PHAROS: Turning Single-Cell Perturbation Models into Target-Directed Drug-Combination Screens**
  [[📝 Paper](https://www.biorxiv.org/content/10.64898/2026.09.08.749477v1)] [[💻 Code](https://github.com/jbezney61/PHAROS)]
  **Metadata:** `State: Cell` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate + Plan` · `Assets: Code`
  <details>
  <summary>Why it qualifies</summary>
  <p>PHAROS chains a pretrained drug-conditioned cell-state transition model across ordered two-drug paths and searches for paths approaching a target state; combination responses are evaluated in cell-line datasets, while patient-tumor rankings remain exploratory.</p>
  </details>

- (*bioRxiv'26*) **Forecasting Cell State Futures from Static Snapshots**
  [[📝 Paper](https://www.biorxiv.org/content/10.64898/2026.02.08.704720v2)] [[💻 Code](https://github.com/EperLuo/CellTempo)]
  **Metadata:** `State: Cell` · `Dynamics: Temporal` · `Capability: Forecast + Simulate` · `Assets: Code`
  <details>
  <summary>Why it qualifies</summary>
  <p>CellTempo autoregressively generates multi-step transcriptomic cell states from an initial snapshot and evaluates lineage and perturbation-initiated fate trajectories; training trajectories are inferred from snapshot data, and drug effects are hypotheses rather than validated therapies.</p>
  </details>

- (*Front Med'26*) **Beyond Static Risk Scores: Dynamic World Models Simulating Patient-Specific Trajectories to Inform Preoperative Risk Mitigation Strategies**
  [[📝 Paper](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2026.1913206/full)] [[💻 Code](https://github.com/ustive/Beyond-Static-Risk-Scores-Dynamic-World-Models)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate + Plan` · `Assets: Code`
  <details>
  <summary>Why it qualifies</summary>
  <p>DPWM learns action-conditioned latent patient dynamics and samples prior-driven multi-step trajectories to rank short-window preoperative strategies; evaluation on MIMIC-IV, eICU-CRD and VitalDB is retrospective and does not establish causal intervention benefit.</p>
  </details>

- (*Nature'26*) **An Operational Perturbation Proteomics-Based Virtual Cell Model**
  [[📝 Paper](https://doi.org/10.1038/s41586-026-11001-9)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42717098/)] [[💻 Code](https://github.com/guomics-lab/PTV-1)]
  **Metadata:** `State: Cell` · `Dynamics: Temporal + Action-conditioned` · `Capability: Forecast + Simulate` · `Assets: Code`
  <details>
  <summary>Why it qualifies</summary>
  <p>ProteinTalks learns proteomic dynamics from baseline under a specified drug perturbation, integrates a neural ODE to predict 6/24/48-hour states, and uses those trajectories for cancer drug-efficacy and combination-synergy prediction; it does not demonstrate changing-treatment rollouts, sequential planning, or clinical benefit.</p>
  </details>

- (*ECCV'26*) **CLARITY: Medical World Model for Guiding Treatment Decisions by Modeling Context-Aware Disease Trajectories in Latent Space**
  [[📝 Paper](https://arxiv.org/abs/2512.08029)] [[💻 Code](https://github.com/DingTianxingjian/CLARITY)] [[🌐 Project](https://dingtianxingjian.github.io/clarity-project-page/)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Action-conditioned` · `Capability: Forecast + Counterfactual + Plan` · `Assets: Code + Project`
  <details>
  <summary>Why it qualifies</summary>
  <p>Rolls latent disease states forward under alternative treatments to support clinical decisions.</p>
  </details>

- (*arXiv'26*) **NVIDIA Cosmos-H-Dreams: Real-Time Generative Physics Simulation for Surgical Robotics**
  [[📝 Paper](https://arxiv.org/abs/2608.24199)] [[💻 Code](https://github.com/isaac-for-healthcare/Cosmos-H-Dreams)] [[🌐 Weights](https://huggingface.co/nvidia/Cosmos-H-Dreams)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate` · `Assets: Code + Weights`
  <details>
  <summary>Why it qualifies</summary>
  <p>Distills a surgical video world model into a streaming simulator that advances generated observations under robot-kinematic actions and feeds them back to policies; evaluates closed-loop suturing tasks against physical dVRK experiments, with task-dependent simulation fidelity.</p>
  </details>

- (*arXiv'26*) **Progressive Experience Fusion for Multi-Task World Model Control in Endovascular Navigation**
  [[📝 Paper](https://arxiv.org/abs/2608.18647)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Temporal + Action-conditioned` · `Capability: Plan + Control` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>PEF learns guidewire-state transitions, rewards, and values for TD-MPC2 rollouts, then selects rotation and translation commands through model-predictive planning; evaluates patient-derived vascular simulations and an unseen fluoroscopic stroke phantom, not in-patient navigation.</p>
  </details>

- (*arXiv'26*) **Surgical WAM: A World-Action Model for Data-Efficient Surgical Robot Learning**
  [[📝 Paper](https://arxiv.org/abs/2608.11204)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Temporal + Action-conditioned` · `Capability: Control` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Jointly samples future-observation and robot-action tokens during inference, with actions attending to predicted futures before receding-horizon execution; evaluates control success on four SurRoL tasks, not standalone future-video prediction fidelity.</p>
  </details>

- (*medRxiv'26*) **The Coupled Stochastic Dynamical System: A Generative Model for Simulating and Forecasting Youth Mental Health Trajectories**
  [[📝 Paper](https://www.medrxiv.org/content/10.64898/2026.07.26.26358943v1)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Mechanistic` · `Capability: Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>CSDS advances coupled psychiatric burden, affect, digital behavior, and wearable-physiology states to generate individualized trajectories evaluated on GLOBEM; downstream forecasting is retrospective, and twin calibration uses full-series summaries rather than a strictly prospective initialization window.</p>
  </details>

- (*Life AI'26*) **Diffusion-Pref: Diffusion World Model Guided Zero-Shot Preference Learning for Safe Glucose Control in Type 1 Diabetes**
  [[📝 Paper](https://www.sciltp.com/journals/lifeai/articles/2604003779)] [[💻 Code](https://github.com/aussie-bzhang/Diffusion-Pref)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Action-conditioned` · `Capability: Forecast + Simulate + Control` · `Assets: Code`
  <details>
  <summary>Why it qualifies</summary>
  <p>Generates six-hour glucose trajectories conditioned on glucose history, meal context, and insulin actions, using sampled outcomes to construct preferences for an offline dosing policy; OhioT1DM forecasting and model-based policy evaluation do not establish clinical treatment safety or efficacy.</p>
  </details>

- (*npj Syst Biol Appl'26*) **Learning Patient-Specific Spatial Biomarker Dynamics via Operator Learning for Alzheimer's Disease Progression**
  [[📝 Paper](https://doi.org/10.1038/s41540-026-00719-x)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42082519/)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Forecast + Simulate + Plan` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>LENO advances patient-specific amyloid, tau, and neurodegeneration dynamics and evaluates longitudinal PET forecasts in ADNI; additional anti-amyloid and anti-tau control terms support hypothetical treatment optimization, not clinically validated treatment effects.</p>
  </details>

- (*AISTATS'26*) **Bayesian Inverse Transition Learning: Learning Dynamics from Near-Optimal Trajectories**
  [[📝 Paper](https://proceedings.mlr.press/v300/benac26a.html)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Action-conditioned` · `Capability: Plan` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>BITL infers a posterior over action-conditioned state-transition matrices and solves the resulting decision models for treatment policies; the medical experiment uses MIMIC-IV hypotension trajectories with fluid and vasopressor actions, assessing offline policy agreement and reward transfer rather than clinical outcomes.</p>
  </details>

- (*arXiv'26*) **FlatASCEND: Autoregressive Clinical Sequence Generation with Continuous Time Prediction and Association-Based Pharmacological Testing**
  [[📝 Paper](https://arxiv.org/abs/2605.04071)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Event sequence` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Autoregressively appends clinical events and elapsed times to patient-specific prefixes, evaluating free-running trajectories on MIMIC-IV and INSPECT; medication-token experiments test observational associations and explicitly do not establish causal pharmacological responses.</p>
  </details>

- (*arXiv'26*) **Stable Long-Horizon Neural ODE Reduced-Order Models via Learned Feedback for Biological Growth and Remodeling**
  [[📝 Paper](https://arxiv.org/abs/2604.13820)] [[💻 Code](https://github.com/joel-laudo/TE-skin-NODE-ROM)]
  **Metadata:** `State: Anatomy` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Forecast + Simulate` · `Assets: Code`
  <details>
  <summary>Why it qualifies</summary>
  <p>Advances reduced skin-displacement and growth states under tissue-expander inflation histories using neural ODE dynamics with learned growth feedback; evaluates long-horizon surgical tissue-expansion rollouts against held-out finite-element simulations, not clinical healing outcomes.</p>
  </details>

- (*bioRxiv'26*) **OPTIMIS: Optimizing Personalized Therapies through Integrated Multiscale Intelligent Simulation**
  [[📝 Paper](https://www.biorxiv.org/content/10.64898/2026.03.24.713941v1)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41929084/)] [[💻 Code](https://github.com/wujah/OPTIMIS)]
  **Metadata:** `State: Cell` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Simulate + Control` · `Assets: Code`
  <details>
  <summary>Why it qualifies</summary>
  <p>Couples stochastic receptor signaling to neural-ODE tumor, CAR-T, and cytokine dynamics, then trains a dosing policy through treatment-conditioned rollouts; held-out evaluation uses synthetic patient cohorts and does not demonstrate clinical CAR-T treatment efficacy.</p>
  </details>

- (*bioRxiv'26*) **Digital Twin Brain Simulation and Manipulation of a Functional Brain Network Underlying Mental Illness**
  [[📝 Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC13015335/)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41890017/)] [[💻 Code](https://github.com/Shmily94/Digital_twin_brain-psychiatry-)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Simulate + Counterfactual` · `Assets: Code`
  <details>
  <summary>Why it qualifies</summary>
  <p>Personalizes a spiking whole-brain simulator, freezes calibration, and propagates neural and hemodynamic states under circuit-parameter perturbations; compares simulated network responses with independent pharmacological fMRI data, without establishing a clinical drug-dose response model.</p>
  </details>

- (*AAAI'26*) **Bootstrapping Personalized Insulin Therapy via Model-Based Reinforcement Learning: An In Silico Study**
  [[📝 Paper](https://ojs.aaai.org/index.php/AAAI/article/view/41160)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate + Plan + Control` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Transfers patient-matched LSTM glucose dynamics and recursively simulates insulin-conditioned trajectories for H-step Deep Dyna-Q policy learning; dosing policies are evaluated in Simglucose, while real-data validation tests glucose prediction for one OhioT1DM participant only.</p>
  </details>

- (*arXiv'26*) **Uni-Flow: A Unified Autoregressive-Diffusion Model for Complex Multiscale Flows**
  [[📝 Paper](https://arxiv.org/abs/2602.15592)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Combines autoregressive latent dynamics with diffusion-based spatial refinement; its medical experiment rolls patient-specific aortic-coarctation surface-pressure fields across multiple cardiac cycles and compares them with high-fidelity hemodynamic simulations.</p>
  </details>

- (*BMC Med'26*) **Digital Twin Brain Reveals State-Specific Stimulation Targets for Abnormal Brain Dynamics in Tinnitus**
  [[📝 Paper](https://doi.org/10.1186/s12916-026-04687-1)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41664110/)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Fits connectome-coupled oscillator dynamics to tinnitus brain states and reruns them under regional stimulation perturbations; compares simulated state changes with a small independent rTMS dataset, without prospectively validating personalized target selection or symptom improvement.</p>
  </details>

- (*Smart Health'26*) **Patient-Specific Deep Offline Artificial Pancreas for Blood Glucose Regulation in Type 1 Diabetes**
  [[📝 Paper](https://doi.org/10.1016/j.smhl.2026.100633)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41766716/)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Simulate + Control` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Uses systems-biology-informed neural networks to infer patient-specific glucose-insulin ODE parameters and runs those dynamics under offline-RL insulin policies; treatment comparisons are in silico, and the paper reports inconsistent policy-experiment sample counts.</p>
  </details>

- (*arXiv'26*) **High-Fidelity Longitudinal Patient Simulation Using Real-World Data**
  [[📝 Paper](https://arxiv.org/abs/2601.17310)] [[💻 Code](https://github.com/yuakagi/Watcher)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Event sequence` · `Capability: Forecast + Simulate` · `Assets: Code`
  <details>
  <summary>Why it qualifies</summary>
  <p>Watcher autoregressively advances a patient timeline through clinical events, timestamps, and numeric laboratory results from an observed prefix; evaluates multi-day Monte Carlo trajectories and derived risks on temporally held-out hospital records, without causal treatment simulation.</p>
  </details>

- (*Comput Biol Med'26*) **Liquid Fourier Latent Dynamics Networks for Fast GPU-Based Numerical Simulations in Computational Cardiology**
  [[📝 Paper](https://doi.org/10.1016/j.compbiomed.2025.111355)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41338030/)] [[📝 Preprint](https://arxiv.org/abs/2408.09818)] [[💻 Code](https://github.com/StanfordCBCL/LFLDNets)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal` · `Capability: Simulate` · `Assets: Code`
  <details>
  <summary>Why it qualifies</summary>
  <p>LFLDNets evolve compact recurrent physiological states and reconstruct three-dimensional electrophysiology or flow fields, evaluating complete cardiac-cycle trajectories under held-out parameters and boundary conditions against numerical solvers; the journal article appeared online in December 2025.</p>
  </details>

- (*J Physiol'26*) **An Eikonal Model with Re-Excitability for Fast Simulations in Cardiac Electrophysiology**
  [[📝 Paper](https://doi.org/10.1113/JP287281)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42678922/)] [[📝 Preprint](https://arxiv.org/abs/2410.22583)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Advances cardiac activation, recovery, and re-excitation under repeated stimuli, reproducing atrial and ventricular macro-reentry against monodomain simulations rather than only calculating a single activation map.</p>
  </details>

- (*Med Image Anal'26 Online*) **Towards Patient-Specific Optimization for Mandibular Reconstruction Planning Based on Predicted Bone-Union Propensity**
  [[📝 Paper](https://doi.org/10.1016/j.media.2026.104281)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42700676/)] [[📝 Preprint](https://arxiv.org/abs/2605.01084)] [[💻 Code](https://github.com/hamidreza-aftabi/OsteoOpt)]
  **Metadata:** `State: Anatomy` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Simulate + Plan` · `Assets: Code`
  <details>
  <summary>Why it qualifies</summary>
  <p>OsteoOpt++ time-integrates jaw mechanics through chewing cycles for candidate reconstruction geometries and optimizes surgical cuts and donor positioning using simulated apposition and safety; its year-1 CT comparison is retrospective spatial validation, not a bone-healing trajectory forecast.</p>
  </details>

- (*arXiv'26*) **A Physiology-Informed Digital Twin Framework for Simulating Liver Health Progression**
  [[📝 Paper](https://arxiv.org/abs/2608.14969)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Mechanistic` · `Capability: Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>hePaTwin advances coupled hepatic metabolic and bilirubin states with disease-stage transition calibration and compares simulated biomarkers with longitudinal measurements; stage-conditioned agreement is not an independently validated baseline-only forecast or treatment-effect estimate.</p>
  </details>

- (*Nat Cardiovasc Res'26*) **Accounting for Uncertainty in Computational Models of Ventricular Tachycardia Improves Ablation Guidance**
  [[📝 Paper](https://doi.org/10.1038/s44161-026-00856-w)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42601469/)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Mechanistic` · `Capability: Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Uses reaction-eikonal propagation and ionic dynamics to simulate ventricular-tachycardia circuits and ECGs across scar reconstructions, comparing them with clinical recordings and aggregating viable circuits into a SATHe Map; this is a mechanistic simulator, not learned latent dynamics.</p>
  </details>

- (*arXiv'26*) **Intervention-Aware Clinical World Model for Post-Op Outcome Forecasting in Cardiology**
  [[📝 Paper](https://arxiv.org/abs/2608.13518)] [[💻 Code](https://github.com/cys1102/af-blanking-world-model)]
  **Metadata:** `State: Anatomy` · `Dynamics: Temporal + Event sequence + Action-conditioned` · `Capability: Forecast` · `Assets: Code`
  <details>
  <summary>Why it qualifies</summary>
  <p>Recurrently advances an MRI-derived atrial latent state through ablation, clinical events, and elapsed-time drift to forecast scar extent and recurrence in DECAAF-II; input-editing experiments are associational sensitivity tests, not causal treatment counterfactuals.</p>
  </details>

- (*arXiv'26*) **S2-HWM: Sparse Event-Structured Hierarchical World Model for Long-Horizon Surgical Robot Manipulation**
  [[📝 Paper](https://arxiv.org/abs/2608.13103)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Temporal + Event sequence + Action-conditioned` · `Capability: Simulate + Control` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Combines action-conditioned DreamerV3 dynamics with chained event-level state, duration, and reward predictions to train hierarchical policies in imagination, evaluating sequential surgical peg transfers and recovery from induced drops in SurRoL.</p>
  </details>

- (*arXiv'26*) **An Open-Source Framework for Predicting Ultrasound Neuromodulation: Bridging Tissue Elastomechanics and Neuron Firing Dynamics**
  [[📝 Paper](https://arxiv.org/abs/2608.06321)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Simulate + Counterfactual` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Propagates prescribed tFUS exposures through acoustic, elastic, thermal, membrane, and neuron dynamics to simulate anatomy-registered firing histories under alternative mechanisms and parameters.</p>
  </details>

- (*bioRxiv'26*) **A Physics-Inspired Classical Digital Twin of the Cell: A Composite Multi-Clock Port-Hamiltonian Neural Network Learned from Multi-Omic Circadian Data**
  [[📝 Paper](https://www.biorxiv.org/content/10.64898/2026.07.11.737972v3)] [[💻 Code](https://github.com/quantum-omics/Classical-Virtual-Omics)]
  **Metadata:** `State: Cell` · `Dynamics: Temporal + Mechanistic` · `Capability: Forecast + Simulate` · `Assets: Code`
  <details>
  <summary>Why it qualifies</summary>
  <p>Learns port-Hamiltonian graph transitions over mouse-liver multi-omic states and evaluates held-out circadian rollouts; the per-gene phase-lag relation is unresolved and withheld-edge recovery is at chance, without validated disease or intervention simulation.</p>
  </details>

- (*bioRxiv'26*) **Parameter-Dependent Effects of Spinal Cord Stimulation on Neural Activation and Evoked Compound Action Potentials**
  [[📝 Paper](https://www.biorxiv.org/content/10.64898/2026.08.03.742575v1)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Simulate + Counterfactual` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Couples spinal finite-element fields to temporal multicompartment axon dynamics and reruns alternative stimulation and recording parameters to simulate neural recruitment and ECAP waveforms.</p>
  </details>

- (*bioRxiv'26*) **A Dynamical Digital Twin Unmasks Hidden Neuromotor Control Policies and Catastrophic Tipping Points in Parkinson's Disease**
  [[📝 Paper](https://www.biorxiv.org/content/10.64898/2026.03.09.710685v2)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Mechanistic` · `Capability: Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Assimilates individual force-plate trajectories into a mechanistic intermittent-control state model, generates patient-level stochastic sway rollouts, and simulates Parkinson-related attractor bifurcations.</p>
  </details>

- (*arXiv'26*) **Optimal Stimulation Sites Are Not the Most Affected: Personalised Models of Resting-State fMRI in Alzheimer's Disease**
  [[📝 Paper](https://arxiv.org/abs/2607.24356)] [[💻 Code](https://github.com/cristianocapone/AD-reservoir-FC-stimulation)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate + Counterfactual + Plan + Control` · `Assets: Code`
  <details>
  <summary>Why it qualifies</summary>
  <p>Fits subject-specific free-running fMRI dynamics, applies candidate focal drives to virtual patients, selects individual stimulation targets, and validates a causally informed real-time closed-loop controller.</p>
  </details>

- (*Phys Med Biol'26*) **Towards a Clinically Practical Computational Platform for Systematically Adapting Radiation Therapy for Glioma Patients**
  [[📝 Paper](https://doi.org/10.1088/1361-6560/ae9687)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42562016/)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Simulate + Counterfactual + Plan` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Calibrates a biology-based glioma-growth model to each patient's longitudinal MRI, virtually applies standard and proliferation-targeted dose maps, and projects post-therapy tumor burden for adaptive planning.</p>
  </details>

- (*Ann Biomed Eng'26*) **Developing a Digital Twin of the Cardiopulmonary System in a Mouse: Inferring Hemodynamics from Sparse Measurements**
  [[📝 Paper](https://doi.org/10.1007/s10439-026-04107-8)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42550388/)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Mechanistic` · `Capability: Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Fits an individualized 0D cardiopulmonary state model to mouse pressure-volume data and integrates its coupled hemodynamics to reproduce full waveforms and infer otherwise unmeasured physiology.</p>
  </details>

- (*Bull Math Biol'26*) **Assessing the Role of Model Complexity in Virtual Clinical Trial Outcomes**
  [[📝 Paper](https://doi.org/10.1007/s11538-026-01715-2)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42530700/)] [[💻 Code](https://github.com/jgevertz/VCT)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Simulate + Counterfactual` · `Assets: Code`
  <details>
  <summary>Why it qualifies</summary>
  <p>Runs mechanistic tumor-virus treatment trajectories for virtual murine patients under multiple dosing protocols, testing how model complexity and cohort construction alter trial outcomes.</p>
  </details>

- (*eLife'26*) **Large-Scale Synthetic Data Enable Digital Twins of Human Excitable Cells**
  [[📝 Paper](https://doi.org/10.7554/eLife.110013)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42489674/)] [[💻 Code](https://github.com/ClancyLabUCD/Digital-Twin-for-the-Win-Personalized-Cardiac-Electrophysiology)]
  **Metadata:** `State: Cell` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Simulate + Counterfactual` · `Assets: Code`
  <details>
  <summary>Why it qualifies</summary>
  <p>Infers parameters of a fixed cardiac ionic ODE model from voltage-clamp traces using a neural network trained on synthetic data, then simulates cell-specific electrophysiology and IKr-blockade responses; the neural network learns parameter inference rather than the forward transition law.</p>
  </details>

- (*bioRxiv'26*) **Patient-Specific Heart Rate Modulates Developmental Electrophysiology in Transcriptomic-Guided In Silico Models of Pediatric Human Atrial Cardiomyocytes**
  [[📝 Paper](https://www.biorxiv.org/content/10.64898/2026.07.21.739866v1)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42538960/)]
  **Metadata:** `State: Cell` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Simulate + Counterfactual` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Scales atrial-cell models with each pediatric patient's transcriptome and rolls action potentials and calcium transients to steady state under intrinsic and counterfactual fixed pacing rates.</p>
  </details>

- (*Cell'26*) **Whole-Cell Particle-Based Digital Twin Simulations from 4D Lattice Light-Sheet Microscopy Data**
  [[📝 Paper](https://doi.org/10.1016/j.cell.2026.06.010)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42379169/)] [[💻 Code](https://github.com/schoeneberglab/readdy-cell)]
  **Metadata:** `State: Cell` · `Dynamics: Temporal + Mechanistic + Spatial/view + Action-conditioned` · `Capability: Simulate + Counterfactual` · `Assets: Code`
  <details>
  <summary>Why it qualifies</summary>
  <p>Initializes particle states from microscopy and advances mitochondria through diffusion, fusion/fission, and motor transport, comparing control and microtubule-perturbed behavior and projecting stress conditions; these mechanistic simulations do not establish a separate prospective forecasting task.</p>
  </details>

- (*Comput Methods Programs Biomed'26*) **Integrating EMT Dynamics in Model-Based Metastasis Prediction**
  [[📝 Paper](https://doi.org/10.1016/j.cmpb.2026.109390)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42061167/)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Couples TGF-beta and EMT signaling to temporal primary and metastatic tumor growth under chemotherapy and radiotherapy, then rolls virtual patients forward to survival outcomes.</p>
  </details>

- (*Heart Rhythm'26*) **High-Fidelity Postmyocardial Infarction Ventricular Tachycardia Simulation for Intraprocedure Ablation Guidance**
  [[📝 Paper](https://doi.org/10.1016/j.hrthm.2026.03.1962)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41956268/)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Advances paced myocardial electrophysiology and ECG states through a GPU-accelerated monodomain solver, reproducing VT inducibility and morphology across ablation stages and exposing potential future VTs.</p>
  </details>

- (*arXiv'26*) **CrossScope: A Role-Asymmetric World Model for Joint Dual-Scope Surgical Video Prediction**
  [[📝 Paper](https://arxiv.org/abs/2608.03211)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Temporal + Spatial/view` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Jointly predicts eight future Mother- and Child-scope frames from synchronized ERCP observations and causal history, with evaluation on phantom and patient-held-out real procedures.</p>
  </details>

- (*MICCAI'26 Workshop*) **Automatic Patient-Specific Microwave Ablation Planning Accelerated by a Physics-Guided Deep Learning Model**
  [[📝 Paper](https://arxiv.org/abs/2608.03086)]
  **Metadata:** `State: Anatomy` · `Dynamics: Mechanistic + Action-conditioned` · `Capability: Simulate + Counterfactual + Plan` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Uses patient anatomy and treatment actions to predict post-ablation regions, then repeatedly queries this forward simulator while optimizing antenna trajectory, power, and duration.</p>
  </details>

- (*arXiv'26*) **NeuroWorld: A Latent Brain World Model for Stimulus-Conditioned Human Brain Dynamics**
  [[📝 Paper](https://arxiv.org/abs/2608.01773)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Action-conditioned` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Learns causal stimulus-conditioned latent brain transitions and autoregressively rolls them out into subject-specific whole-brain fMRI trajectories over multiple future time points.</p>
  </details>

- (*arXiv'26*) **EndoWAM: A Grounded World-Action Model for Generalizable Endoscopic Navigation**
  [[📝 Paper](https://arxiv.org/abs/2608.01221)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Temporal` · `Capability: Forecast` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Trains a video dynamics prior and future-target generator over endoscopic states, with the predictive representation evaluated in closed-loop physical-phantom navigation across three procedures.</p>
  </details>

- (*MICCAI'26 Workshop*) **Anticipatory Digital Twins for Online Head-and-Neck Adaptive Proton Therapy via Foundation-Model Registration**
  [[📝 Paper](https://arxiv.org/abs/2608.00831)]
  **Metadata:** `State: Anatomy` · `Dynamics: Temporal + Spatial/view` · `Capability: Forecast` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Transfers longitudinal anatomical change through a learned registration model to forecast patient-specific treatment-day CT states and contours before image acquisition.</p>
  </details>

- (*arXiv'26*) **A Digital-Twin Framework for Forecasting Treatment-Day Imaging with Contour Uncertainty in Adaptive Proton Radiotherapy**
  [[📝 Paper](https://arxiv.org/abs/2609.24725)]
  **Metadata:** `State: Anatomy` · `Dynamics: Temporal + Spatial/view` · `Capability: Forecast` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Extends the preceding cross-patient deformation-transfer method to an ensemble of future CT and contour states with directional forecast uncertainty, evaluated against later treatment CTs; its library-only contour center did not improve on the planning contour.</p>
  </details>

- (*arXiv'26*) **Failure Detection for Surgical Robot Imitation Policies via Flow-Matching World Modeling**
  [[📝 Paper](https://arxiv.org/abs/2607.27511)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Temporal + Action-conditioned` · `Capability: Forecast` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Learns nominal multi-step visual transitions conditioned on surgical-robot actions and detects failures from inconsistencies between predicted and realized endpoint states in simulated and real dVRK tasks.</p>
  </details>

- (*arXiv'26*) **Action-Conditioned World Model for Goal Plane Probe Guidance in Robotic Ultrasound**
  [[📝 Paper](https://arxiv.org/abs/2607.21918)]
  **Metadata:** `State: Medical image` · `Dynamics: Spatial/view + Action-conditioned` · `Capability: Forecast + Simulate + Control` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Predicts future ultrasound states under candidate 6-DoF probe motions, uses the frozen model as an internal simulator for policy learning, and validates closed-loop carotid and thyroid guidance.</p>
  </details>

- (*arXiv'26*) **A Diffusion-Model Subpopulation Digital Twin for Mobile Health Deployment: A Case Study on the HeartSteps Intervention**
  [[📝 Paper](https://arxiv.org/abs/2607.21403)]
  **Metadata:** `State: Population` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Uses causal temporal kernels and prefix-preserving diffusion updates to generate hourly behavior trajectories under sequential mobile-health actions; observed-action trajectory fidelity is evaluated, without establishing causal effects or clinical benefit of new policies.</p>
  </details>

- (*arXiv'26*) **PIONEER: Bayesian Joint Modelling of Mechanistic Tumour Growth and Time-to-Event Endpoints for Dynamic Prediction of Ongoing Oncology Trials**
  [[📝 Paper](https://arxiv.org/abs/2607.17908)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Mechanistic` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Jointly infers latent tumor-growth and clinical-event dynamics, then forward-simulates patient trajectories and mature trial endpoints from interim data.</p>
  </details>

- (*arXiv'26*) **Enhancing Personalized Bladder Cancer Treatment Through Reinforcement Learning: A Recurrent Patient State Transition Decision Support Framework**
  [[📝 Paper](https://arxiv.org/abs/2607.16916)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate + Plan + Control` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Learns treatment-conditioned recurrent bladder-cancer state transitions from historical observations and uses recursive simulated trajectories for DQN planning; validation is confined to the learned simulator.</p>
  </details>

- (*arXiv'26*) **Differentiable Cardiac Electrophysiology Simulations for Dynamical State and Parameter Estimation**
  [[📝 Paper](https://arxiv.org/abs/2607.15492)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Mechanistic` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Fits a differentiable electrophysiology PDE simulator to partial cardiac measurements and rolls the recovered action-potential dynamics forward.</p>
  </details>

- (*arXiv'26*) **AI-Augmented Adaptive Digital Twin Modeling for Brain Tumor Evolution Prediction and Treatment Scheduling**
  [[📝 Paper](https://arxiv.org/abs/2607.13877)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Forecast + Simulate + Plan + Control` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Combines treatment-conditioned tumor dynamics, patient-specific online updating, 120-step recursive rollouts, and MPC scheduling; evaluation is limited to patient-data-informed synthetic trajectories.</p>
  </details>

- (*MICCAI'26*) **HemoPIC: A Physics-Informed Cerebral Hemodynamics Digital Twin for Brain Perfusion**
  [[📝 Paper](https://arxiv.org/abs/2607.08799)] [[💻 Code](https://github.com/jhuldr/HemoPIC)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Mechanistic` · `Capability: Simulate` · `Assets: Code`
  <details>
  <summary>Why it qualifies</summary>
  <p>Fits parameters of fixed Windkessel and tracer-compartment equations, then simulates time-resolved contrast passage and derives cerebral perfusion maps; the evaluated experiments do not establish learned transition laws or vascular-intervention counterfactuals.</p>
  </details>

- (*arXiv'26*) **EHR-MPC: Inference-Time Control for Sepsis Treatment with Generative Patient Digital Twins**
  [[📝 Paper](https://arxiv.org/abs/2607.08793)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate + Plan + Control` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Recursively generates future clinical states under candidate treatment tokens and uses those rollouts for sepsis MPC; retrospective off-policy estimates and outcomes inside the learned simulator do not establish prospective treatment efficacy.</p>
  </details>

- (*arXiv'26*) **Sectorial Customized Corneal Crosslinking for Keratoconus: An Inverse Biomechanical Design Study with an Anisotropic Reduced Shell Finite-Element Surrogate**
  [[📝 Paper](https://arxiv.org/abs/2607.06385)]
  **Metadata:** `State: Anatomy` · `Dynamics: Mechanistic + Action-conditioned` · `Capability: Simulate + Counterfactual + Plan` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Simulates post-treatment corneal deformation under alternative spatial crosslinking actions and optimizes the intervention mask against biomechanical and optical objectives.</p>
  </details>

- (*medRxiv'26*) **Personalized Planning of Cardiac Resynchronization Therapy Through Integration of Coronary Sinus Geometry, Clinical Data, Digital Twins, and Machine Learning: Visualization, Stratification, and Optimization**
  [[📝 Paper](https://www.medrxiv.org/content/10.64898/2026.07.01.26356827v1)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Simulate + Counterfactual + Plan` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Simulates ventricular activation under alternative CRT pacing sites and uses a separate response classifier to support site planning; improved predicted response at a virtual site is not observed clinical benefit from implanting it.</p>
  </details>

- (*Stem Cell Reports'26*) **In Silico Optimization of Regenerative Cell Therapy in the Infarcted Human Ventricles to Mitigate Arrhythmic Burden**
  [[📝 Paper](https://doi.org/10.1016/j.stemcr.2026.103007)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42425090/)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Simulate + Counterfactual` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Simulates patient-specific ventricular electrophysiology before and after cell therapy to evaluate intervention outcomes over time.</p>
  </details>

- (*arXiv'26*) **Personalized 4D Whole-Heart Mesh Reconstruction from Cine MRI via Multi-Scale Temporal Modeling and Differentiable Contour Rendering**
  [[📝 Paper](https://arxiv.org/abs/2607.01952)]
  **Metadata:** `State: Anatomy` · `Dynamics: Temporal` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Reconstructs and predicts patient-specific 3D cardiac geometry as a continuous trajectory through the cardiac cycle.</p>
  </details>

- (*Med Image Anal'26*) **Electrophysiologically-Informed Digital Twins for Atrial Fibrillation**
  [[📝 Paper](https://doi.org/10.1016/j.media.2026.104131)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42172939/)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Mechanistic` · `Capability: Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Calibrates patient-specific atrial electrophysiology and simulates AF wave dynamics, comparing phase-singularity maps with retrospective ablation locations; an evaluated virtual-ablation strategy or treatment-plan optimizer is not demonstrated.</p>
  </details>

- (*J Physiol'26*) **Prospective In Silico Trials Identify Combined SK and K2P Channel Block as an Effective Strategy for Atrial Fibrillation Cardioversion**
  [[📝 Paper](https://doi.org/10.1113/JP287124)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/39557619/)]
  **Metadata:** `State: Physiology` · `Dynamics: Mechanistic + Action-conditioned` · `Capability: Simulate + Counterfactual` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Rolls out multiscale atrial electrophysiology under alternative ion-channel interventions to predict cardioversion outcomes.</p>
  </details>

- (*Phys Med Biol'26*) **A Digital Twin Framework for Adaptive Treatment Planning in Radiotherapy**
  [[📝 Paper](https://doi.org/10.1088/1361-6560/ae835a)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42361838/)]
  **Metadata:** `State: Anatomy` · `Dynamics: Temporal + Spatial/view` · `Capability: Forecast + Plan` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Transfers image-registration deformations to forecast plausible treatment-day anatomies and construct adaptive radiotherapy plans; retrospective selection and reoptimization use daily CBCT, without a biological tumor-response or radiation-action transition model.</p>
  </details>

- (*arXiv'26*) **Neural Operator-Based Digital Twins for Modeling Amyloid-Beta and Tau Propagation and Treatment Optimization in Alzheimer's Disease**
  [[📝 Paper](https://arxiv.org/abs/2606.25185)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Simulate + Counterfactual + Plan` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Learns spatial amyloid/tau reaction-diffusion dynamics and projects alternative treatment schedules through optimal control; biomarker trajectory evaluation does not validate clinical responses to those hypothetical controls.</p>
  </details>

- (*arXiv'26*) **OphthaDT: Generative Digital Twins for Forecasting Visual Acuity Trajectories in Ophthalmology**
  [[📝 Paper](https://arxiv.org/abs/2606.22101)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal` · `Capability: Forecast` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Generates multi-horizon visual-acuity forecasts from serialized patient histories and evaluates held-out patients across four clinical-trial datasets; treatment-conditioned causal simulation or planning is not demonstrated.</p>
  </details>

- (*arXiv'26*) **SurgVista: Long-Horizon Surgical World Modeling with Plausible Instrument-Tissue Dynamics**
  [[📝 Paper](https://arxiv.org/abs/2606.19889)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Temporal + Action-conditioned` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Predicts long-horizon surgical video states conditioned on actions while modeling instrument-tissue interactions.</p>
  </details>

- (*arXiv'26*) **DreamReg: Belief-Driven World Model for 2D-3D Ultrasound Registration**
  [[📝 Paper](https://arxiv.org/abs/2606.18825)]
  **Metadata:** `State: Medical image` · `Dynamics: Spatial/view + Action-conditioned` · `Capability: Simulate + Plan` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Learns probe-motion-conditioned latent dynamics and imagines future observations for registration planning.</p>
  </details>

- (*Biomed Phys Eng Express'26*) **Physics-Informed Koopman-Constrained ImplicitQ-Learning for Safe Offline Reinforcement Learning in Mechanical Ventilation**
  [[📝 Paper](https://doi.org/10.1088/2057-1976/ae7d30)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42296990/)]
  **Metadata:** `State: Physiology` · `Dynamics: Mechanistic + Action-conditioned` · `Capability: Simulate + Control` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Learns Koopman respiratory-state dynamics and uses predicted ventilator-action consequences to shape offline policy learning.</p>
  </details>

- (*arXiv'26*) **Learning Cardiac Electrophysiology Digital Twins Through Agentic Discovery of Hybrid Structure**
  [[📝 Paper](https://arxiv.org/abs/2606.18154)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Mechanistic` · `Capability: Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Discovers reaction equations and neural diffusion structures that roll out cardiac electrophysiology, evaluated on synthetic models and animal electrograms; personalized human clinical deployment is not established.</p>
  </details>

- (*arXiv'26*) **Treatment Response Optimized Clinical Decision Support AI System via Digital Twin Simulation**
  [[📝 Paper](https://arxiv.org/abs/2606.17405)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate + Plan` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Learns explicit residual next-state updates, performs multi-step treatment-conditioned rollouts, and evaluates an offline decision policy; synthetic and retrospective experiments with in-model rewards do not establish causal clinical treatment benefit.</p>
  </details>

- (*Comput Biol Med'26*) **Causal Counterfactual Simulation for Treatment Decisions in Multimodal Lung Disease Data**
  [[📝 Paper](https://doi.org/10.1016/j.compbiomed.2026.111807)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42275812/)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate + Counterfactual` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Models longitudinal lung state transitions and generates treatment counterfactuals across imaging and clinical data.</p>
  </details>

- (*arXiv'26*) **Transition-Based Digital Twin Modelling for Alzheimer's Disease under Sparse Longitudinal Data**
  [[📝 Paper](https://arxiv.org/abs/2606.09671)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal` · `Capability: Forecast` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Learns adjacent-visit MMSE and diagnosis prediction and evaluates longer-horizon forecasts; FAQ and hippocampal-volume what-if changes are covariate sensitivity analyses rather than identified treatment counterfactuals.</p>
  </details>

- (*bioRxiv'26*) **U-Pert: Unbalanced Perturbation Dynamics For Cell Fate Design**
  [[📝 Paper](https://www.biorxiv.org/content/10.64898/2026.06.30.735555v1)]
  **Metadata:** `State: Cell` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate + Plan` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Learns context-aware perturbation dynamics over cell states and abundances for forward simulation and inverse intervention design.</p>
  </details>

- (*arXiv'26*) **Chreode: A Cell World Model for One-Step Temporal Dynamics and Perturbation Prediction**
  [[📝 Paper](https://arxiv.org/abs/2605.28111)] [[💻 Code](https://github.com/mufanq/Chreode)] [[🌐 Weights](https://huggingface.co/MufanQiu/chreode-pretrained)]
  **Metadata:** `State: Cell` · `Dynamics: Temporal + Action-conditioned` · `Capability: Forecast + Simulate` · `Assets: Code + Weights`
  <details>
  <summary>Why it qualifies</summary>
  <p>Predicts cell-state transitions across time and perturbations rather than only embedding static transcriptomes.</p>
  </details>

- (*IEEE JBHI'26*) **TwinRL-Onco: A World Model-Empowered Digital Twin Framework with Hierarchical Reinforcement Learning for Venetoclax Resistance Trajectory Prediction and Adaptive Therapy Optimization in Chronic Lymphocytic Leukemia**
  [[📝 Paper](https://doi.org/10.1109/JBHI.2026.3696685)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42184194/)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Action-conditioned` · `Capability: Forecast + Simulate + Plan` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>The primary abstract reports recurrent state-space dynamics, Monte Carlo resistance trajectories, and hierarchical therapy optimization; its 0.917 AUROC concerns simulated 12-month progression, while full methods and clinical predictive validity remain unverified in this audit.</p>
  </details>

- (*arXiv'26*) **ChronoMedicalWorld: A Medical World Model for Learning Patient Trajectories from Longitudinal Care Data**
  [[📝 Paper](https://arxiv.org/abs/2605.21963)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Event sequence + Action-conditioned` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Recurrently rolls patient states forward under clinical actions over longitudinal care trajectories.</p>
  </details>

- (*arXiv'26*) **ECG-WM: A Physiology-Informed ECG World Model for Clinical Intervention Simulation**
  [[📝 Paper](https://arxiv.org/abs/2605.17580)] [[🌐 Project](https://chenzk202212.github.io/ECG_World_Model/)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Action-conditioned` · `Capability: Forecast + Counterfactual` · `Assets: Project`
  <details>
  <summary>Why it qualifies</summary>
  <p>Predicts post-intervention ECG trajectories from pre-intervention physiological state and treatment context.</p>
  </details>

- (*arXiv'26*) **GazeWorld: A World Model of Radiologist Reading for Medical Image Representation Learning**
  [[📝 Paper](https://arxiv.org/abs/2605.23992)]
  **Metadata:** `State: Clinical workflow` · `Dynamics: Temporal + Event sequence` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Autoregressively models the evolving sequence of radiologist fixations as a diagnostic interaction trajectory.</p>
  </details>

- (*arXiv'26*) **SWoMo: Neuro-Symbolic World Model for Cataract Surgery Simulation**
  [[📝 Paper](https://arxiv.org/abs/2605.16530)] [[🌐 Project](https://ssharvienkumar.github.io/SWoMo/)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate` · `Assets: Project`
  <details>
  <summary>Why it qualifies</summary>
  <p>Simulates tool-tissue state changes from symbolic surgical actions and renders their visual consequences.</p>
  </details>

- (*arXiv'26*) **Toward World Modeling of Physiological Signals with Chaos-Theoretic Balancing and Latent Dynamics (NormWear-2)**
  [[📝 Paper](https://arxiv.org/abs/2605.15465)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Action-conditioned` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Learns latent dynamics of multivariate physiological signals and rolls them forward under intervention context.</p>
  </details>

- (*arXiv'26*) **Agentifying Patient Dynamics within LLMs through Interacting with Clinical World Model**
  [[📝 Paper](https://arxiv.org/abs/2605.14723)] [[💻 Code](https://github.com/FreedomIntelligence/SepsisAgent)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate + Plan` · `Assets: Code`
  <details>
  <summary>Why it qualifies</summary>
  <p>Provides an interactive sepsis world model that simulates candidate treatment effects for an LLM decision agent.</p>
  </details>

- (*arXiv'26*) **MolWorld: Molecule World Models for Actionable Molecular Optimization**
  [[📝 Paper](https://arxiv.org/abs/2605.08954)]
  **Metadata:** `State: Molecule` · `Dynamics: Event sequence + Action-conditioned` · `Capability: Simulate + Plan` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Models molecule optimization as sequential local state transformations and plans actionable editing trajectories.</p>
  </details>

- (*arXiv'26*) **Simulating Clinical Interventions with a Generative Multimodal Model of Human Physiology (HealthFormer)**
  [[📝 Paper](https://arxiv.org/abs/2604.27899)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Action-conditioned` · `Capability: Forecast + Counterfactual` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Generates multimodal physiological trajectories and simulates how clinical interventions alter future patient states.</p>
  </details>

- (*arXiv'26*) **Beyond Patient Invariance: Learning Cardiac Dynamics via Action-Conditioned JEPAs**
  [[📝 Paper](https://arxiv.org/abs/2604.22618)] [[💻 Code](https://github.com/cljosegfer/lesaude-dynamics)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Action-conditioned` · `Capability: Forecast + Simulate` · `Assets: Code`
  <details>
  <summary>Why it qualifies</summary>
  <p>Predicts future cardiac electrophysiology states in latent space conditioned on disease-onset actions.</p>
  </details>

- (*arXiv'26*) **Toward Safe Autonomous Robotic Endovascular Interventions using World Models**
  [[📝 Paper](https://arxiv.org/abs/2604.20151)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Temporal + Action-conditioned` · `Capability: Plan + Control` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Learns endovascular environment dynamics and uses imagined rollouts for TD-MPC2 catheter control.</p>
  </details>

- (*arXiv'26*) **Sonata: A Hybrid World Model for Inertial Kinematics under Clinical Data Scarcity**
  [[📝 Paper](https://arxiv.org/abs/2604.18058)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Mechanistic` · `Capability: Forecast` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Combines learned and biomechanical dynamics to predict future clinically measured inertial kinematic states.</p>
  </details>

- (*arXiv'26*) **Open-H-Embodiment: A Large-Scale Dataset for Enabling Foundation Models in Medical Robotics**
  [[📝 Paper](https://arxiv.org/abs/2604.21017)] [[💻 Code](https://huggingface.co/nvidia/Cosmos-H-Surgical-Simulator)] [[💻 Code](https://github.com/NVIDIA-Medtech/Cosmos-H-Surgical-Simulator)] [[🌐 Project](https://open-h.github.io/open-h-embodiment/)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate` · `Assets: Code + Project`
  <details>
  <summary>Why it qualifies</summary>
  <p>Beyond releasing data, it trains an action-conditioned surgical simulator that predicts multi-embodiment procedure rollouts.</p>
  </details>

- (*arXiv'26*) **Lingshu-Cell: A Generative Cellular World Model for Transcriptome Modeling Toward Virtual Cells**
  [[📝 Paper](https://arxiv.org/abs/2603.25240)]
  **Metadata:** `State: Cell` · `Dynamics: Action-conditioned` · `Capability: Simulate + Counterfactual` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Generates perturbation-conditioned distributions of future cellular transcriptomic states.</p>
  </details>

- (*arXiv'26*) **EyeWorld: A Generative World Model of Ocular State and Dynamics**
  [[📝 Paper](https://arxiv.org/abs/2603.14039)]
  **Metadata:** `State: Anatomy` · `Dynamics: Temporal` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Learns time-conditioned transitions of ocular state for longitudinal disease progression simulation.</p>
  </details>

- (*arXiv'26*) **SAW: Toward a Surgical Action World Model via Controllable and Scalable Video Generation**
  [[📝 Paper](https://arxiv.org/abs/2603.13024)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Generates future surgical states conditioned on tool trajectories and procedure actions.</p>
  </details>

- (*ICLR'26 Rejected*) **Unified Surgical World Model for Structured Understanding, Long-Horizon Prediction, and Fine-Grained Generation**
  [[📝 Paper](https://openreview.net/forum?id=Kk9t5empEf)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Temporal + Action-conditioned` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Learns action-aware surgical transitions for long-horizon trajectory prediction and controllable scene evolution.</p>
  </details>

- (*MIDL'26 rejected*) **Learning Action-Conditioned World Models for Cataract Surgery from Unlabeled Videos (SurgWorld)**
  [[📝 Paper](https://openreview.net/forum?id=aYQYOVm2AB)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Temporal + Action-conditioned` · `Capability: Forecast` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Predicts latent cataract-surgery state transitions conditioned on inferred atomic action tokens.</p>
  </details>

- (*CVPR'26*) **X-WIN: Building Chest Radiograph World Model via Predictive Sensing**
  [[📝 Paper](https://arxiv.org/abs/2511.14918)]
  **Metadata:** `State: Medical image` · `Dynamics: Spatial/view + Action-conditioned` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Predicts how radiographic observations change under explicit 3D viewpoint and sensing transformations.</p>
  </details>

- (*arXiv'26*) **Brain-WM: Brain Glioblastoma World Model**
  [[📝 Paper](https://arxiv.org/abs/2603.07562)] [[💻 Code](https://github.com/thibault-wch/Brain-GBM-world-model)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Action-conditioned` · `Capability: Forecast + Simulate + Counterfactual` · `Assets: Code`
  <details>
  <summary>Why it qualifies</summary>
  <p>Simulates coupled tumor-treatment evolution and generates future MRI states under therapy scenarios.</p>
  </details>

- (*bioRxiv'26*) **Towards building a World Model to simulate perturbation-induced cellular dynamics by AlphaCell**
  [[📝 Paper](https://www.biorxiv.org/content/10.64898/2026.03.02.709176v1)]
  **Metadata:** `State: Cell` · `Dynamics: Temporal + Action-conditioned` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Learns continuous cellular-state dynamics from large-scale perturbation data and simulates unseen responses.</p>
  </details>

- (*CVPR'26*) **MRI Contrast Enhancement Kinetics World Model**
  [[📝 Paper](https://arxiv.org/abs/2602.19285)] [[💻 Code](https://github.com/DD0922/MRI-Contrast-Enhancement-Kinetics-World-Model)]
  **Metadata:** `State: Medical image` · `Dynamics: Temporal + Mechanistic` · `Capability: Forecast + Simulate` · `Assets: Code`
  <details>
  <summary>Why it qualifies</summary>
  <p>Models continuous contrast-agent kinetics and synthesizes MRI states at arbitrary enhancement times.</p>
  </details>

- (*medRxiv'26*) **MedOS: AI-XR-Cobot World Model for Clinical Perception and Action**
  [[📝 Paper](https://www.medrxiv.org/content/10.64898/2026.02.18.26345936v1)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Mechanistic + Action-conditioned` · `Capability: Simulate + Plan` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Uses a physics-aware procedural simulator to predict adverse events and action consequences in embodied clinical tasks.</p>
  </details>

- (*arXiv'26*) **EHRWorld: A Patient-Centric Medical World Model for Long-Horizon Clinical Trajectories**
  [[📝 Paper](https://arxiv.org/abs/2602.03569)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Event sequence + Action-conditioned` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Autoregressively simulates long-horizon patient trajectories under sequential clinical interventions.</p>
  </details>

- (*AI Medicine'26*) **World Model Enhanced Offline Reinforcement Learning for Sequential Intervention Optimization in Acute Kidney Injury**
  [[📝 Paper](https://www.sciltp.com/journals/aim/articles/2602002965)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate + Plan + Control` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Learns AKI patient-state dynamics and uses model-generated transitions to optimize sequential interventions offline.</p>
  </details>

- (*arXiv'26*) **The Patient is not a Moving Document: A World Model Training Paradigm for Longitudinal EHR**
  [[📝 Paper](https://arxiv.org/abs/2601.22128)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Event sequence` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Predicts future patient states in latent and token space from longitudinal clinical histories.</p>
  </details>

- (*arXiv'26*) **Generating Counterfactual Patient Timelines from Real-World Data**
  [[📝 Paper](https://arxiv.org/abs/2604.02337)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Event sequence + Action-conditioned` · `Capability: Simulate + Counterfactual` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Autoregressively generates alternative patient-event timelines under specified treatment choices.</p>
  </details>

- (*arXiv'26*) **Policy4OOD: A Knowledge-Guided World Model for Policy Intervention Simulation against the Opioid Overdose Crisis**
  [[📝 Paper](https://arxiv.org/abs/2602.12373)]
  **Metadata:** `State: Population` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate + Plan` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Simulates spatiotemporal overdose dynamics under policy actions and searches intervention plans with model rollouts.</p>
  </details>

- (*arXiv'26*) **BLINK: Behavioral Latent Modeling of NK Cell Cytotoxicity**
  [[📝 Paper](https://arxiv.org/abs/2603.05110)]
  **Metadata:** `State: Cell` · `Dynamics: Temporal` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Recurrently models latent NK-cell and tumor interaction dynamics over time.</p>
  </details>

- (*arXiv'26*) **RAVEN: Scaling Recurrence-Aware Foundation Models for Clinical Records via Next-Visit Prediction**
  [[📝 Paper](https://arxiv.org/abs/2603.24562)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Event sequence` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Generates recurrent next-visit clinical events to roll longitudinal patient records forward.</p>
  </details>

### 2025

- (*J Neuroeng Rehabil'25*) **Towards AI-Based Precision Rehabilitation via Contextual Model-Based Reinforcement Learning**
  [[📝 Paper](https://doi.org/10.1186/s12984-025-01771-0)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41419889/)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate + Plan` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>PSCRL updates a Bayesian model of patient motor recovery and uses its dose-dependent state transitions in constrained sequential planning; the personalized rehabilitation experiments involve 150 synthetic patients, not a clinical treatment trial.</p>
  </details>

- (*Sci Adv'25*) **Multiscale Mathematical Model-Informed Reinforcement Learning Optimizes Combination Treatment Scheduling in Glioblastoma Evolution**
  [[📝 Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC13155510/)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/40779623/)] [[💻 Code](https://github.com/SunXQlab/M4RL)]
  **Metadata:** `State: Cell` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Simulate + Plan + Control` · `Assets: Code`
  <details>
  <summary>Why it qualifies</summary>
  <p>M4RL couples an experimentally informed tumor-microenvironment agent model to a physics-informed dynamics surrogate, using simulated CSF1R/IGF1R treatment responses to optimize combination schedules; predicted regimen benefits are computational, not clinical-trial results.</p>
  </details>

- (*Nat Mach Intell'25*) **Model-Based Reinforcement Learning for Ultrasound-Driven Autonomous Microrobots**
  [[📝 Paper](https://doi.org/10.1038/s42256-025-01054-2)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/40709099/)] [[💻 Code](https://github.com/M-Medany/Model-Based-Reinforcement-Learning-for-Ultrasound-Driven-Autonomous-Microrobots)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate + Control` · `Assets: Code`
  <details>
  <summary>Why it qualifies</summary>
  <p>Learns recurrent image-based dynamics for ultrasound-actuated microrobots and trains control policies on imagined trajectories; evaluates physical navigation in artificial vascular channels under static and flowing conditions, not in-vivo drug delivery.</p>
  </details>

- (*npj Digit Med'25*) **Digital Twin Brain Simulator for Real-Time Consciousness Monitoring and Virtual Intervention Using Primate Electrocorticogram Data**
  [[📝 Paper](https://doi.org/10.1038/s41746-025-01444-1)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/39929926/)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Learns hierarchical variational recurrent ECoG dynamics from awake and anesthetized primates, generating future signals and freely evolving trajectories after latent-state perturbations; latent manipulation is not a calibrated anesthetic-dose intervention model.</p>
  </details>

- (*arXiv'25*) **Cosmos-H-Surgical: Learning Surgical Robot Policies from Videos via World Modeling**
  [[📝 Paper](https://arxiv.org/abs/2512.23162)] [[💻 Code](https://huggingface.co/nvidia/Cosmos-H-Surgical-Simulator)] [[💻 Code](https://github.com/nvidia-cosmos/cosmos-cookbook)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate + Control` · `Assets: Code`
  <details>
  <summary>Why it qualifies</summary>
  <p>Generates action-conditioned surgical video rollouts and uses them to learn robot policies.</p>
  </details>

- (*arXiv'25*) **VCWorld: A Biological World Model for Virtual Cell Simulation**
  [[📝 Paper](https://arxiv.org/abs/2512.00306)]
  **Metadata:** `State: Cell` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate + Counterfactual` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Reproduces perturbation-induced signaling cascades as stepwise cellular-state transitions.</p>
  </details>

- (*arXiv'25*) **Evolving Diagnostic Agents in a Virtual Clinical Environment**
  [[📝 Paper](https://arxiv.org/abs/2510.24654)]
  **Metadata:** `State: Clinical workflow` · `Dynamics: Event sequence + Action-conditioned` · `Capability: Simulate + Plan + Control` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Implements an interactive virtual patient environment whose evolving observations support closed-loop diagnostic policy learning.</p>
  </details>

- (*arXiv'25*) **Cosmos-Surg-dVRK: World Foundation Model-based Automated Online Evaluation of Surgical Robot Policy Learning**
  [[📝 Paper](https://arxiv.org/abs/2510.16240)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate + Control` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Simulates action-conditioned surgical robot trajectories for online policy evaluation.</p>
  </details>

- (*bioRxiv'25*) **Virtual Clinical Trials of BMP4 Differentiation Therapy: Digital Twins to Aid Successful Glioblastoma Trial Design**
  [[📝 Paper](https://doi.org/10.1101/2024.08.22.609156)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41279885/)] [[💻 Code](https://github.com/Harbour-N/Virtual-Clinical-Trials-of-BMP4-Differentiation-Therapy)]
  **Metadata:** `State: Cell` · `Dynamics: Temporal + Mechanistic + Action-conditioned` · `Capability: Simulate + Counterfactual + Plan` · `Assets: Code`
  <details>
  <summary>Why it qualifies</summary>
  <p>Fits mechanistic glioblastoma cell-compartment and BMP4-exposure equations to cell-line data, then simulates treatment schedules and virtual-trial cohorts; projected efficacy and trial power are model outputs rather than clinical validation.</p>
  </details>

- (*NPJ Digit Med'25*) **Large Language Models Forecast Patient Health Trajectories Enabling Digital Twins**
  [[📝 Paper](https://doi.org/10.1038/s41746-025-02004-3)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41034564/)] [[💻 Code](https://github.com/MendenLab/DT-GPT)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal` · `Capability: Forecast` · `Assets: Code`
  <details>
  <summary>Why it qualifies</summary>
  <p>Generates specified future laboratory and clinical-measurement trajectories from serialized patient histories across lung-cancer, ICU, and Alzheimer datasets; these observational forecasts do not demonstrate a generic clinical-event simulator or treatment-conditioned rollout.</p>
  </details>

- (*MICCAI'25*) **World Model for AI Autonomous Navigation in Mechanical Thrombectomy**
  [[📝 Paper](https://arxiv.org/abs/2509.25518)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Temporal + Action-conditioned` · `Capability: Plan + Control` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Learns endovascular transition dynamics and plans thrombectomy navigation through imagined trajectories.</p>
  </details>

- (*arXiv'25*) **medDreamer: Model-Based Reinforcement Learning with Latent Imagination on Complex EHRs for Clinical Decision Support**
  [[📝 Paper](https://arxiv.org/abs/2505.19785)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Event sequence + Action-conditioned` · `Capability: Simulate + Plan + Control` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Learns latent patient dynamics and trains treatment policies on imagined EHR trajectories.</p>
  </details>

- (*arXiv'25*) **Generative Medical Event Models Improve with Scale (CoMET)**
  [[📝 Paper](https://arxiv.org/abs/2508.12104)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Event sequence` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Autoregressively generates successive medical events to simulate longitudinal patient trajectories.</p>
  </details>

- (*arXiv'25*) **Visuomotor Grasping with World Models for Surgical Robots**
  [[📝 Paper](https://arxiv.org/abs/2508.11200)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Temporal + Action-conditioned` · `Capability: Forecast + Control` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Learns action-conditioned surgical grasping dynamics for model-based visuomotor control.</p>
  </details>

- (*arXiv'25*) **Xray2Xray: World Model from Chest X-rays with Volumetric Context**
  [[📝 Paper](https://arxiv.org/abs/2506.19055)]
  **Metadata:** `State: Medical image` · `Dynamics: Spatial/view + Action-conditioned` · `Capability: Forecast + Simulate` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Predicts radiographic state transitions across view changes using an inferred volumetric patient state.</p>
  </details>

- (*ICCV'25*) **Medical World Model: Generative Simulation of Tumor Evolution for Treatment Planning**
  [[📝 Paper](https://arxiv.org/abs/2506.02327)] [[💻 Code](https://github.com/scott-yjyang/MeWM)] [[🌐 Project](https://yijun-yang.github.io/MeWM/)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Action-conditioned` · `Capability: Forecast + Simulate + Plan` · `Assets: Code + Project`
  <details>
  <summary>Why it qualifies</summary>
  <p>Generates treatment-conditioned tumor evolution trajectories for counterfactual planning.</p>
  </details>

- (*CVPR'25*) **EchoWorld: Learning Motion-Aware World Models for Echocardiography Probe Guidance**
  [[📝 Paper](https://arxiv.org/abs/2504.13065)]
  **Metadata:** `State: Medical image` · `Dynamics: Spatial/view + Action-conditioned` · `Capability: Forecast + Control` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Predicts echocardiographic observations under probe motions for closed-loop guidance.</p>
  </details>

- (*arXiv'25*) **Towards Suturing World Models: Learning Predictive Models for Robotic Surgical Tasks**
  [[📝 Paper](https://arxiv.org/abs/2503.12531)] [[🌐 Project](https://mkturkcan.github.io/suturingmodels/)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Temporal + Action-conditioned` · `Capability: Forecast + Simulate` · `Assets: Project`
  <details>
  <summary>Why it qualifies</summary>
  <p>Learns sub-stitch spatiotemporal dynamics to predict future states of robotic suturing.</p>
  </details>

- (*MICCAI Workshop'25*) **Surgical Vision World Model**
  [[📝 Paper](https://arxiv.org/abs/2503.02904)] [[💻 Code](https://github.com/bhattarailab/Surgical-Vision-World-Model)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Temporal + Action-conditioned` · `Capability: Forecast + Simulate` · `Assets: Code`
  <details>
  <summary>Why it qualifies</summary>
  <p>Learns latent surgical actions and action-controlled future-video dynamics.</p>
  </details>

- (*arXiv'25*) **MM-DADM: Multimodal Drug-Aware Diffusion Model for Virtual Clinical Trials**
  [[📝 Paper](https://arxiv.org/abs/2502.07297)]
  **Metadata:** `State: Physiology` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate + Counterfactual` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Generates drug-conditioned ECG state changes for virtual intervention trials.</p>
  </details>

- (*MIDL'25*) **4D-VQ-GAN: A World Model for Synthesizing Medical Scans at Any Time Point for Personalized Disease Progression Modeling of Idiopathic Pulmonary Fibrosis**
  [[📝 Paper](https://openreview.net/forum?id=tU3IpPQCEc)] [[💻 Code](https://github.com/anzhao920/4DVQGAN)] [[📝 arXiv](https://arxiv.org/abs/2502.05713)]
  **Metadata:** `State: Medical image` · `Dynamics: Temporal` · `Capability: Forecast + Simulate` · `Assets: Code`
  <details>
  <summary>Why it qualifies</summary>
  <p>Uses continuous-time latent dynamics to synthesize patient scans along disease-progression trajectories.</p>
  </details>

### 2024

- (*arXiv'24*) **Structure-aware World Model for Probe Guidance via Large-scale Self-supervised Pre-train**
  [[📝 Paper](https://arxiv.org/abs/2406.19756)]
  **Metadata:** `State: Medical image` · `Dynamics: Spatial/view + Action-conditioned` · `Capability: Forecast + Control` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Predicts ultrasound-plane transitions conditioned on probe pose changes.</p>
  </details>

- (*MICCAI'24*) **Cardiac Copilot: Automatic Probe Guidance for Echocardiography with World Model** (introduces Cardiac Dreamer as the world model for cardiac spatial structures)
  [[📝 Paper](https://arxiv.org/abs/2406.13165)]
  **Metadata:** `State: Medical image` · `Dynamics: Spatial/view + Action-conditioned` · `Capability: Simulate + Control` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Uses Cardiac Dreamer to simulate spatial observation changes under probe actions for navigation.</p>
  </details>

- (*arXiv'24*) **World Models for General Surgical Grasping**
  [[📝 Paper](https://arxiv.org/abs/2405.17940)]
  **Metadata:** `State: Procedure/Robot` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate + Plan + Control` · `Assets: Paper only`
  <details>
  <summary>Why it qualifies</summary>
  <p>Learns surgical grasping transition dynamics and plans robot actions with model-based reinforcement learning.</p>
  </details>

---

## 🧭 By Topic

> A complementary topic-wise view.

### Medical Imaging and Radiology

- (*medRxiv'26*) **Prediction of Subsolid Pulmonary Nodule Evolution from Baseline CT Using Temporal Imaging Models**
  [[📝 Paper](https://www.medrxiv.org/content/10.64898/2026.08.12.26360292v2)]

- (*arXiv'26*) **DuoPIC: Uncertainty-Aware Voxel-Level Digital Twins of Cerebral Perfusion with Transport PDEs in Acute Stroke**
  [[📝 Paper](https://arxiv.org/abs/2610.33071)] [[💻 Code](https://github.com/detinatran/duopic)]

- (*arXiv'26*) **Saga: an in silico ontology for a multimodal patient world model**
  [[📝 Paper](https://arxiv.org/abs/2610.33054)]

- (*arXiv'26*) **CaMeWM: A Causal Medical World Model for Generative Tumor Evolution and Treatment Planning**
  [[📝 Paper](https://arxiv.org/abs/2610.26923)]

- (*arXiv'26*) **SonoWorld: Towards Interactive Pose-Controllable Ultrasound World Models**
  [[📝 Paper](https://arxiv.org/abs/2610.19327)] [[🌐 Project](https://iclr2027anonymous.github.io/SonoWorld/)]

- (*arXiv'26*) **UltraWorld: Learning Interactive Ultrasound World Models from Untracked Clinical Videos with Acoustic Sampling Map**
  [[📝 Paper](https://arxiv.org/abs/2610.09785)] [[🌐 Project](https://ultraworld-project.github.io/)]

- (*arXiv'26*) **One Frame, Full Heartbeat: ECG-Free Cardiac Cine MRI Synthesis via Phase-Conditioned Flow Matching**
  [[📝 Paper](https://arxiv.org/abs/2610.09397)]

- (*arXiv'26*) **One Frame, Full Heartbeat: ECG-Free 4D Cardiac Cine MRI Synthesis via Radial-Decomposed Flow Matching**
  [[📝 Paper](https://arxiv.org/abs/2610.09185)]

- (*arXiv'26*) **Ultrasound Operator Guidance Using World Modeling and Retrieval Based Action Planning**
  [[📝 Paper](https://arxiv.org/abs/2610.06008)]

- (*arXiv'26*) **An Uncertainty-Guided Digital Twin Framework for Online Adaptive Proton Therapy in Head and Neck Cancer: A Feasibility Study**
  [[📝 Paper](https://arxiv.org/abs/2609.39010)]

- (*arXiv'26*) **A Digital-Twin Framework for Forecasting Treatment-Day Imaging with Contour Uncertainty in Adaptive Proton Radiotherapy**
  [[📝 Paper](https://arxiv.org/abs/2609.24725)]

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

- (*arXiv'26*) **ProTEUS: A mutation-resolved world model for closed-loop protein evolution**
  [[📝 Paper](https://arxiv.org/abs/2611.13348)] [[💻 Code](https://github.com/yikunpku/ProTEUS)]

- (*arXiv'26*) **stMIND: Learning multiscale interaction dynamics from spatial-temporal transcriptomics**
  [[📝 Paper](https://arxiv.org/abs/2611.12228)] [[💻 Code](https://github.com/LongquanLi135/stMIND)]

- (*bioRxiv'26*) **Virtual dynamics of spatiotemporal single-cell interactions**
  [[📝 Paper](https://www.biorxiv.org/content/10.64898/2026.11.04.764438v1)]

- (*Cell Rep Med'26*) **Tumor digital twins uncover therapeutic strategies in triple-negative breast cancer**
  [[📝 Paper](https://doi.org/10.1016/j.xcrm.2026.103119)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42933397/)] [[💻 Code](https://github.com/jfisher-lab/TNBC_Victori2026)]

- (*Protein Sci'26*) **DreamFold: A World Model to efficiently generate protein folding pathways in the latent space**
  [[📝 Paper](https://doi.org/10.1002/pro.70794)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42813590/)] [[📝 Preprint](https://www.biorxiv.org/content/10.1101/2025.03.26.645554v1)]

- (*medRxiv'26*) **Informing risk stratification and vaccine policy via a predictive mathematical model of SARS-COV-2 infection**
  [[📝 Paper](https://www.medrxiv.org/content/10.64898/2026.10.12.26365315v1)]

- (*bioRxiv'26*) **scMTG reconstructs single-cell temporal dynamics with Markov transition generators**
  [[📝 Paper](https://www.biorxiv.org/content/10.64898/2026.06.04.730241v2)] [[💻 Code](https://github.com/liuq-lab/scMTG)]

- (*bioRxiv'26*) **Mechanistic prediction of fecal microbiota transplant engraftment and Clostridioides difficile colonization resistance with μODE**
  [[📝 Paper](https://www.biorxiv.org/content/10.64898/2026.10.09.758137v1)] [[💻 Code](https://github.com/cumbof/muODE)]

- (*bioRxiv'26*) **A tissue time machine to forward-predict single-timepoint data applied to tuberculosis granulomas**
  [[📝 Paper](https://www.biorxiv.org/content/10.64898/2026.10.09.758083v1)]

- (*arXiv'26*) **Finsler Flow Matching: Dynamics-Aware Geodesic Interpolation for Single-Snapshot Trajectory Inference**
  [[📝 Paper](https://arxiv.org/abs/2610.11318)] [[💻 Code](https://github.com/mlbelab/FinslerFlowMatching)]

- (*arXiv'26*) **MD-LLM-2: A Transferable Language Model of Molecular Dynamics with Physical Conditioning and Explicit Path Probabilities**
  [[📝 Paper](https://arxiv.org/abs/2610.10879)]

- (*bioRxiv'26*) **Identifiable Inverse Optimal Transport for Single-Cell State Transitions**
  [[📝 Paper](https://www.biorxiv.org/content/10.64898/2026.10.01.756056v1)] [[💻 Code](https://github.com/XTSgreen/IOT-single-cell-paper)]

- (*bioRxiv'26*) **AnnFlux: Object-Conditioned Neural Stochastic Differential Equations for Single-Cell Perturbation Dynamics**
  [[📝 Paper](https://www.biorxiv.org/content/10.64898/2026.09.01.748703v1)]

- (*bioRxiv'26*) **MEGA-ODE: Learning Biologically Structured and Navigable Continuous Perturbation Dynamics from Sparse Omics**
  [[📝 Paper](https://www.biorxiv.org/content/10.64898/2026.08.05.742921v1)] [[💻 Code](https://github.com/Candlelight-XYJ/MEGA-ODE)]

- (*Cell'26*) **RegVelo: Gene-Regulatory-Informed Dynamics of Single Cells**
  [[📝 Paper](https://doi.org/10.1016/j.cell.2026.04.022)] [[💻 Code](https://github.com/theislab/regvelo)]

- (*bioRxiv'26*) **PHAROS: Turning Single-Cell Perturbation Models into Target-Directed Drug-Combination Screens**
  [[📝 Paper](https://www.biorxiv.org/content/10.64898/2026.09.08.749477v1)] [[💻 Code](https://github.com/jbezney61/PHAROS)]

- (*bioRxiv'26*) **Forecasting Cell State Futures from Static Snapshots**
  [[📝 Paper](https://www.biorxiv.org/content/10.64898/2026.02.08.704720v2)] [[💻 Code](https://github.com/EperLuo/CellTempo)]

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

### Longitudinal EHR and Clinical Trajectories

- (*arXiv'26*) **ICare-DT: a digital twin for continuous forecasting of intensive care patients**
  [[📝 Paper](https://arxiv.org/abs/2611.09712)]

- (*arXiv'26*) **Learning a patient world model for health system simulation in intensive care**
  [[📝 Paper](https://arxiv.org/abs/2611.08392)]

- (*arXiv'26*) **Forecasting Patient Trajectories from the Electronic Health Records with Action-Conditioned World Models**
  [[📝 Paper](https://arxiv.org/abs/2610.23862)]

- (*arXiv'26*) **PulmoWorld: An Asynchronous Multimodal Medical World Model for Longitudinal Pneumonia Dynamics**
  [[📝 Paper](https://arxiv.org/abs/2610.38289)]

- (*medRxiv'26*) **Digital Twin Workflow for Continuous Glucose Forecasting: Real-Time Data Assimilation Using Reinforcement Learning**
  [[📝 Paper](https://www.medrxiv.org/content/10.64898/2026.10.23.26366163v1)]

- (*arXiv'26*) **Saga: an in silico ontology for a multimodal patient world model**
  [[📝 Paper](https://arxiv.org/abs/2610.33054)]

- (*medRxiv'26*) **FERMAT: An Autoregressive Clinical Foundation Model for Disease Risk and Clinical Event Prediction**
  [[📝 Paper](https://www.medrxiv.org/content/10.64898/2026.10.11.26365210v1)]

- (*arXiv'26*) **PatientWM: Towards Generalizable Clinical World Models via Unified Patient States**
  [[📝 Paper](https://arxiv.org/abs/2610.17059)]

- (*arXiv'26*) **Sign-Constrained Intervention Effects for Domain-Generalizable ICU World Models**
  [[📝 Paper](https://arxiv.org/abs/2610.11090)]

- (*arXiv'26*) **Similar Predictive Fit but Different Latent Dynamics: Characterizing Learned Dynamical Structure in Personalized Models of Brain Disorders**
  [[📝 Paper](https://arxiv.org/abs/2610.10850)]

- (*arXiv'26*) **HyperNSDE: Personalized Neural SDEs for Joint Static-Longitudinal Clinical Data Generation**
  [[📝 Paper](https://arxiv.org/abs/2610.07383)] [[💻 Code](https://github.com/perrinechassat/HyperNSDE)]

- (*npj Metab Health Dis'26*) **A Digital Twin for Tracking and Forecasting Glycemia with Septic Patients in ICUs**
  [[📝 Paper](https://doi.org/10.1038/s44324-026-00132-2)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42823439/)]

- (*medRxiv'26*) **A World Model Simulates the Latent Dynamics of Human Health**
  [[📝 Paper](https://www.medrxiv.org/content/10.64898/2026.09.19.26363460v1)]

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

- (*medRxiv'26*) **An agent-based model of Epstein-Barr virus transmission and vaccination**
  [[📝 Paper](https://www.medrxiv.org/content/10.64898/2026.11.10.26367734v1)]

- (*arXiv'26*) **Personalized health coaching via coachable health age and counterfactual wearable trajectories**
  [[📝 Paper](https://arxiv.org/abs/2611.08568)]

- (*medRxiv'26*) **Risk-benefit assessment of oral anticoagulation in atrial fibrillation using virtual clinical trials**
  [[📝 Paper](https://www.medrxiv.org/content/10.64898/2026.11.04.26367324v1)]

- (*J Sleep Res'26*) **Development of a Digital Twin to Analyse Waiting Lists in a Sleep-Disordered Breathing Unit**
  [[📝 Paper](https://doi.org/10.1111/jsr.70489)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/43000229/)]

- (*arXiv'26*) **PulmoWorld: An Asynchronous Multimodal Medical World Model for Longitudinal Pneumonia Dynamics**
  [[📝 Paper](https://arxiv.org/abs/2610.38289)]

- (*Cell Rep Med'26*) **Tumor digital twins uncover therapeutic strategies in triple-negative breast cancer**
  [[📝 Paper](https://doi.org/10.1016/j.xcrm.2026.103119)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42933397/)] [[💻 Code](https://github.com/jfisher-lab/TNBC_Victori2026)]

- (*arXiv'26*) **CaMeWM: A Causal Medical World Model for Generative Tumor Evolution and Treatment Planning**
  [[📝 Paper](https://arxiv.org/abs/2610.26923)]

- (*arXiv'26*) **APOD: Reasoning-Guided Agentic Population Ordinary Differential Equation Discovery for Pharmacological Digital Twins**
  [[📝 Paper](https://arxiv.org/abs/2610.06227)] [[💻 Code](https://gitlab.inria.fr/compo/apod)]

- (*arXiv'26*) **Graph World Models for Constrained Epidemic Policy Planning**
  [[📝 Paper](https://arxiv.org/abs/2609.35545)] [[💻 Code](https://anonymous.4open.science/r/epimind-9706/README.md)]

- (*arXiv'26*) **An Uncertainty-Guided Digital Twin Framework for Online Adaptive Proton Therapy in Head and Neck Cancer: A Feasibility Study**
  [[📝 Paper](https://arxiv.org/abs/2609.39010)]

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

- (*MICCAI'26 Workshop*) **Anticipatory Digital Twins for Online Head-and-Neck Adaptive Proton Therapy via Foundation-Model Registration**
  [[📝 Paper](https://arxiv.org/abs/2608.00831)]

- (*arXiv'26*) **A Digital-Twin Framework for Forecasting Treatment-Day Imaging with Contour Uncertainty in Adaptive Proton Radiotherapy**
  [[📝 Paper](https://arxiv.org/abs/2609.24725)]

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

- (*arXiv'25*) **MM-DADM: Multimodal Drug-Aware Diffusion Model for Virtual Clinical Trials**
  [[📝 Paper](https://arxiv.org/abs/2502.07297)]

- (*ICCV'25*) **Medical World Model: Generative Simulation of Tumor Evolution for Treatment Planning**
  [[📝 Paper](https://arxiv.org/abs/2506.02327)] [[💻 Code](https://github.com/scott-yjyang/MeWM)] [[🌐 Project](https://yijun-yang.github.io/MeWM/)]

- (*AI Medicine'26*) **World Model Enhanced Offline Reinforcement Learning for Sequential Intervention Optimization in Acute Kidney Injury**
  [[📝 Paper](https://www.sciltp.com/journals/aim/articles/2602002965)]

- (*arXiv'25*) **Evolving Diagnostic Agents in a Virtual Clinical Environment**
  [[📝 Paper](https://arxiv.org/abs/2510.24654)]

### Surgical Simulation and Embodied Healthcare

- (*arXiv'26*) **SurgTransfer: Multi-Step Latent Action Modeling for Action Transfer in Surgical World Model**
  [[📝 Paper](https://arxiv.org/abs/2611.05443)] [[💻 Code](https://github.com/bhattarailab/Surgical-Vision-World-Model)]

- (*arXiv'26*) **ProCut: Probabilistic Cutting Topology for Autonomous Electrosurgical Tissue Dissection**
  [[📝 Paper](https://arxiv.org/abs/2610.07515)]

- (*arXiv'26*) **SurgGMF: Fully Causal Gaussian Motion Forecasting for Anticipatory Surgical Scene Rendering**
  [[📝 Paper](https://arxiv.org/abs/2609.34733)]

- (*arXiv'26*) **Towards Surgical World-Action Modeling: A Preliminary Joint Visual-Trajectory Forecasting for Surgical Motion Planning**
  [[📝 Paper](https://arxiv.org/abs/2608.20284)]

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

<a id="resources"></a>

<a id="-datasets-benchmarks-and-simulators"></a>

## 🧰 Resources

> For datasets, benchmarks and simulators, this index is narrower than a general medical AI directory. Datasets must support at least one qualifying medical world model, benchmarks must evaluate dynamics or rollouts, and simulators must expose an implementation that advances a medical state. Inclusion here does not place a dataset-only or benchmark-only paper in the main paper list.

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
| **ivbench** | Clinical trial simulation | Scores patient world models on 9,996 audited within-trial contrasts from 7,207 registered trials using an intervention-blind reference, measuring how much accuracy depends on knowing the tested intervention. | [[📝 Paper](https://arxiv.org/abs/2611.05907)] [[💻 Code and data](https://github.com/alicemkyn/ivbench)] |
| **T1D Digital Twin Decision-Quality Benchmark** | Glucose-insulin dynamics | Fits each twin under one basal-bolus regimen and evaluates glucose-trajectory fidelity, treatment-ranking correlation and decision regret under 20 alternative regimens in 30 UVA/Padova virtual patients; entirely in silico. | [[📝 Paper](https://arxiv.org/abs/2610.30577)] [[💻 Code and protocol](https://github.com/Veeeeeee7/T1D-Digital-Twin-Benchmark)] |
| **SurgWMBench** | Surgical instrument motion | Short-horizon trajectory prediction, recursive rollout stability, and perturbation robustness on SAR-RARP50 suturing clips; distinguishes image-conditioned from fully predictive rollout settings. | [[📝 Paper specification](https://arxiv.org/abs/2608.08070)] `Paper only` |
| **Open-H Multi-Embodiment Surgical Benchmark** | Surgical robotics | Action-conditioned future-video fidelity across nine robot embodiments using frame decay, tool consistency, and tool displacement metrics. | [[📦 Data](https://huggingface.co/datasets/nvidia/PhysicalAI-Robotics-Open-H-Embodiment)] [[💻 Evaluation](https://github.com/NVIDIA-Medtech/Cosmos-H-Surgical-Simulator)] |
| **UniSWM-Bench** | Surgical workflow and video | Five understanding tasks, two long-horizon prediction tasks, and three action- or movement-conditioned generation tasks. | [[📝 Paper specification](https://openreview.net/forum?id=Kk9t5empEf)] `Paper only` |
| **SurgVeo and Surgical Plausibility Pyramid** | Surgical video | Expert assessment of generated rollouts at 1, 3, and 8 seconds across visual, instrument-operation, environment-feedback, and surgical-intent plausibility. | [[📝 Paper and protocol](https://arxiv.org/abs/2511.01775)] `Paper only` |

### Simulators

| Simulator | Medical state | Rollout interface | Access |
|---|---|---|---|
| **OSS-DBS v2** | Brain electric field and stimulated neural pathways | Computes stimulation-dependent fields and neural responses from electrode and tissue models; a biophysical planning aid, not a validated clinical-outcome simulator. | [[💻 Code](https://github.com/SFB-ELAINE/OSS-DBSv2)] [[📝 Paper](https://www.medrxiv.org/content/10.64898/2026.10.10.26365197v1)] |
| **Cosmos-H-Dreams** | Surgical video and robot state | Streams action-conditioned video chunks and returns generated observations to a robot policy for interactive closed-loop rollouts; released with serving code and model weights. | [[💻 Code](https://github.com/isaac-for-healthcare/Cosmos-H-Dreams)] [[🌐 Weights](https://huggingface.co/nvidia/Cosmos-H-Dreams)] [[📝 Paper](https://arxiv.org/abs/2608.24199)] |
| **Lung CT Monte Carlo Workflow** | Light transport in patient-specific thoracic tissues | Propagates photons through CT-derived lung anatomy to simulate 3D fluence under alternative illumination and tissue conditions; dosimetry only, not longitudinal disease or treatment-response prediction. | [[💻 Code](https://github.com/JohanDiazTovar/Monte-Carlo-Modeling-of-Light-Propagation-in-Healthy-and-Diseased-Human-Lungs)] [[📝 Paper](https://doi.org/10.1073/pnas.2612370123)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42574619/)] |
| **Cosmos-H-Surgical-Simulator** | Surgical scene and robot state | Generates future surgical video from an initial frame and robot-kinematic action sequence across multiple embodiments. | [[💻 Code](https://github.com/NVIDIA-Medtech/Cosmos-H-Surgical-Simulator)] [[🌐 Weights](https://huggingface.co/nvidia/Cosmos-H-Surgical-Simulator)] |
| **HemoPIC** | Cerebral hemodynamics | Fits patient-specific tracer transport and rolls perfusion dynamics through a physics-informed digital twin; includes a runnable demo. | [[💻 Code and demo](https://github.com/jhuldr/HemoPIC)] [[📝 Paper](https://arxiv.org/abs/2607.08799)] |
| **MeWM** | Liver tumor state | Synthesizes treatment-conditioned post-intervention tumor states for TACE planning and survival analysis. | [[💻 Code](https://github.com/scott-yjyang/MeWM)] [[🌐 Project](https://yijun-yang.github.io/MeWM/)] |
| **SepsisAgent Clinical World Model** | ICU patient state | Simulates counterfactual patient trajectories under candidate fluid and vasopressor interventions. | [[💻 Code](https://github.com/FreedomIntelligence/SepsisAgent)] [[📝 Paper](https://arxiv.org/abs/2605.14723)] |
| **Brain-WM** | Glioblastoma and longitudinal MRI | Couples treatment planning with treatment-conditioned future MRI generation for disease-progression simulation. | [[💻 Code](https://github.com/thibault-wch/Brain-GBM-world-model)] [[📝 Paper](https://arxiv.org/abs/2603.07562)] |

### 🔗 Related Repositories

- **Awesome-Self-Evolving-AI-for-Agentic-Healthcare**
  [[💻 Repository](https://github.com/ZhihaoPENG-CityU/Awesome-Self-Evolving-AI-for-Agentic-Healthcare)]

- **knightnemo/Awesome-World-Models**
  [[💻 Repository](https://github.com/knightnemo/Awesome-World-Models)]

- **LMD0311/Awesome-World-Model**
  [[💻 Repository](https://github.com/LMD0311/Awesome-World-Model)]

<a id="industry-models-platforms"></a>

### 🏭 Industry Models / Platforms

- (*NVIDIA'25*) **Cosmos World Foundation Model**
  [[🌐 Platform](https://docs.nvidia.com/cosmos/index.html)] [[📝 Research](https://research.nvidia.com/labs/dir/cosmos1/)]
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

<a id="project-information"></a>

## 📋 Project Information

### ⚖️ License

This repository uses separate licenses for content and code:

- **Catalog content ([CC BY 4.0](LICENSE-CONTENT)):** `README.md`, `CONTRIBUTING.md`, `CITATION.cff`, the pull request and issue templates, and original material in `assets/`, including the taxonomy, metadata, annotations, and qualification notes.
- **Code ([MIT](LICENSE)):** source code in `scripts/` and `tests/`, automation in `.github/workflows/`, and repository configuration such as `.lychee.toml`.

Linked or quoted papers, code repositories, datasets, trademarks, and other third-party materials retain their original rights and licenses; their inclusion here does not relicense them.

This content/code split applies to this revision and subsequent contributions. Earlier repository revisions remain available under the license notices included with those revisions.

### 📖 Citation

If this catalog supports your research, please cite the repository using the metadata in [CITATION.cff](CITATION.cff). GitHub also provides ready-to-use APA and BibTeX formats through **Cite this repository**.

### 🤝 Contributing

Contributions are welcome. Please read the [contribution guide](CONTRIBUTING.md) before proposing a paper or resource. Main-list paper submissions must provide source-grounded evidence for the modeled state, transition dynamics, rollout capability, and medical task. You can submit a pull request or [suggest a paper through the structured issue form](https://github.com/chengwang96/Awesome-World-Models-for-Healthcare/issues/new?template=01-paper-suggestion.yml).

Entry format:

```markdown
- (*Venue'YY*) **Paper Title**
  [[📝 Paper](link)] [[💻 Code](link)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate + Plan` · `Assets: Code`
  <details>
  <summary>Why it qualifies</summary>
  <p>Learns intervention-conditioned patient-state transitions and uses rollouts to compare treatment plans.</p>
  </details>
```

The pull request template includes the required scope evidence and review checklist. Conceptual work belongs under Survey Papers; static representation learning, ordinary conditional generation, benchmark-only work, and other work that does not meet the inclusion criteria are not counted in the main list.

### ✉️ Contact Us

If you have any questions or suggestions, please feel free to contact us via:

**Email:** chengwang@link.cuhk.edu.hk, zhihaopeng@cuhk.edu.hk

---

<a id="-star-history"></a>

[View this repository's star history on Star History](https://www.star-history.com/?repos=chengwang96%2FAwesome-World-Models-for-Healthcare&type=date&logscale=&legend=bottom-right).
