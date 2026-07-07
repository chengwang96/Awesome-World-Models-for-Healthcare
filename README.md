<h1 align="center">
  <strong>Awesome-World-Models-for-Healthcare</strong>
</h1>

<div align="center">

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![GitHub stars](https://img.shields.io/github/stars/chengwang96/Awesome-World-Models-for-Healthcare?style=social)](https://github.com/chengwang96/Awesome-World-Models-for-Healthcare)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](#-contributing)

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

---

## 📌 Contents

- [Survey Papers](#-survey-papers)
- [World Model Papers](#-world-model-papers)
- [By Topic](#-by-topic)
- [Related Repositories](#-related-repositories)
- [Cross-References](#-cross-references)
- [Industry Models / Platforms](#industry-models-platforms)
- [Special Issues / Calls](#-special-issues--calls)
- [Contributing](#-contributing)
- [Contact Us](#-contact-us)

---

## 📚 Survey Papers

- (*arXiv'26*) **Medical World Models: Representing Medical States, Modelling Clinical Dynamics and Guiding Intervention Policies**
  [[📝 Paper](https://arxiv.org/abs/2606.16721)]

- (*arXiv'26*) **Towards World Models in Biomedical Research**
  [[📝 Paper](https://arxiv.org/abs/2606.05925)]

- (*arXiv'26*) **From Static Risk to Dynamic Trajectories: Toward World-Model-Inspired Clinical Prediction**
  [[📝 Paper](https://arxiv.org/abs/2605.16927)]

- (*arXiv'26*) **Grounding Clinical AI Competency in Human Cognition Through the Clinical World Model and Skill-Mix Framework**
  [[📝 Paper](https://arxiv.org/abs/2604.08226)]

- (*NeurIPS'25 Workshop*) **Beyond Generative AI: World Models for Clinical Prediction, Counterfactuals, and Planning**
  [[📝 Paper](https://arxiv.org/abs/2511.16333)]

---

## 📝 World Model Papers

> Entries are sorted by year in descending order. See [Scope](#-scope) for inclusion criteria.

### 2026

- (*Phys Med Biol'26*) **A Digital Twin Framework for Adaptive Treatment Planning in Radiotherapy**
  [[📝 Paper](https://doi.org/10.1088/1361-6560/ae835a)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42361838/)]

- (*Cardiometab Syndr J'26*) **TyG Trajectory and Digital Twin Simulation to Predict Metabolic Syndrome Risk**
  [[📝 Paper](https://doi.org/10.51789/cmsj.2026.6.e7)]

- (*arXiv'26*) **Neural Operator-Based Digital Twins for Modeling Amyloid-Beta and Tau Propagation and Treatment Optimization in Alzheimer's Disease**
  [[📝 Paper](https://arxiv.org/abs/2606.25185)]

- (*Oper Neurosurg'26*) **Iterative Virtual and Physical Simulation for Staged Separation of Total Vertical Craniopagus: The Avatar Patient Approach to Conjoined Twins**
  [[📝 Paper](https://doi.org/10.1227/ons.0000000000002116)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42318872/)]

- (*arXiv'26*) **OphthaDT: Generative Digital Twins for Forecasting Visual Acuity Trajectories in Ophthalmology**
  [[📝 Paper](https://arxiv.org/abs/2606.22101)]

- (*arXiv'26*) **SurgVista: Long-Horizon Surgical World Modeling with Plausible Instrument-Tissue Dynamics**
  [[📝 Paper](https://arxiv.org/abs/2606.19889)]

- (*arXiv'26*) **DreamReg: Belief-Driven World Model for 2D-3D Ultrasound Registration**
  [[📝 Paper](https://arxiv.org/abs/2606.18825)]

- (*Biomed Phys Eng Express'26*) **Physics-Informed Koopman-Constrained ImplicitQ-Learning for Safe Offline Reinforcement Learning in Mechanical Ventilation**
  [[📝 Paper](https://doi.org/10.1088/2057-1976/ae7d30)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42296990/)]

- (*arXiv'26*) **Learning Cardiac Electrophysiology Digital Twins Through Agentic Discovery of Hybrid Structure**
  [[📝 Paper](https://arxiv.org/abs/2606.18154)]

- (*arXiv'26*) **Treatment Response Optimized Clinical Decision Support AI System via Digital Twin Simulation**
  [[📝 Paper](https://arxiv.org/abs/2606.17405)]

- (*Comput Biol Med'26*) **Causal Counterfactual Simulation for Treatment Decisions in Multimodal Lung Disease Data**
  [[📝 Paper](https://doi.org/10.1016/j.compbiomed.2026.111807)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42275812/)]

- (*arXiv'26*) **Transition-Based Digital Twin Modelling for Alzheimer's Disease under Sparse Longitudinal Data**
  [[📝 Paper](https://arxiv.org/abs/2606.09671)]

- (*arXiv'26*) **Chreode: A Cell World Model for One-Step Temporal Dynamics and Perturbation Prediction**
  [[📝 Paper](https://arxiv.org/abs/2605.28111)] [[💻 Code](https://github.com/mufanq/Chreode)] [[🌐 Weights](https://huggingface.co/MufanQiu/chreode-pretrained)]

- (*IEEE JBHI'26*) **TwinRL-Onco: A World Model-Empowered Digital Twin Framework with Hierarchical Reinforcement Learning for Venetoclax Resistance Trajectory Prediction and Adaptive Therapy Optimization in Chronic Lymphocytic Leukemia**
  [[📝 Paper](https://doi.org/10.1109/JBHI.2026.3696685)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42184194/)]

- (*arXiv'26*) **ChronoMedicalWorld: A Medical World Model for Learning Patient Trajectories from Longitudinal Care Data**
  [[📝 Paper](https://arxiv.org/abs/2605.21963)]

- (*arXiv'26*) **ECG-WM: A Physiology-Informed ECG World Model for Clinical Intervention Simulation**
  [[📝 Paper](https://arxiv.org/abs/2605.17580)] [[🌐 Project](https://chenzk202212.github.io/ECG_World_Model/)]

- (*arXiv'26*) **GazeWorld: A World Model of Radiologist Reading for Medical Image Representation Learning**
  [[📝 Paper](https://arxiv.org/abs/2605.23992)]

- (*arXiv'26*) **SWoMo: Neuro-Symbolic World Model for Cataract Surgery Simulation**
  [[📝 Paper](https://arxiv.org/abs/2605.16530)] [[🌐 Project](https://ssharvienkumar.github.io/SWoMo/)]

- (*arXiv'26*) **Toward World Modeling of Physiological Signals with Chaos-Theoretic Balancing and Latent Dynamics (NormWear-2)**
  [[📝 Paper](https://arxiv.org/abs/2605.15465)]

- (*arXiv'26*) **Agentifying Patient Dynamics within LLMs through Interacting with Clinical World Model**
  [[📝 Paper](https://arxiv.org/abs/2605.14723)] [[💻 Code](https://github.com/FreedomIntelligence/SepsisAgent)]

- (*arXiv'26*) **MolWorld: Molecule World Models for Actionable Molecular Optimization**
  [[📝 Paper](https://arxiv.org/abs/2605.08954)]

- (*arXiv'26*) **Simulating Clinical Interventions with a Generative Multimodal Model of Human Physiology (HealthFormer)**
  [[📝 Paper](https://arxiv.org/abs/2604.27899)]

- (*arXiv'26*) **Beyond Patient Invariance: Learning Cardiac Dynamics via Action-Conditioned JEPAs**
  [[📝 Paper](https://arxiv.org/abs/2604.22618)] [[💻 Code](https://github.com/cljosegfer/lesaude-dynamics)]

- (*arXiv'26*) **Toward Safe Autonomous Robotic Endovascular Interventions using World Models**
  [[📝 Paper](https://arxiv.org/abs/2604.20151)]

- (*arXiv'26*) **Sonata: A Hybrid World Model for Inertial Kinematics under Clinical Data Scarcity**
  [[📝 Paper](https://arxiv.org/abs/2604.18058)]

- (*arXiv'26*) **Apollo: A Multimodal and Temporal Foundation Model for Virtual Patient Representations at Healthcare System Scale**
  [[📝 Paper](https://arxiv.org/abs/2604.18570)]

- (*arXiv'26*) **Open-H-Embodiment: A Large-Scale Dataset for Enabling Foundation Models in Medical Robotics**
  [[📝 Paper](https://arxiv.org/abs/2604.21017)] [[💻 Code](https://huggingface.co/nvidia/Cosmos-H-Surgical-Simulator)] [[💻 Code](https://github.com/NVIDIA-Medtech/Cosmos-H-Surgical-Simulator)] [[🌐 Project](https://open-h.github.io/open-h-embodiment/)]

- (*arXiv'26*) **Validated Synthetic Patient Generation for Small Longitudinal Cohorts: Coagulation Dynamics Across Pregnancy**
  [[📝 Paper](https://arxiv.org/abs/2604.07557)] [[💻 Code](https://github.com/varnerlab/SA-generation-legacy-dataset-paper)]

- (*arXiv'26*) **Toward World Models for Epidemiology**
  [[📝 Paper](https://arxiv.org/abs/2604.09519)]

- (*arXiv'26*) **Lingshu-Cell: A Generative Cellular World Model for Transcriptome Modeling Toward Virtual Cells**
  [[📝 Paper](https://arxiv.org/abs/2603.25240)]

- (*arXiv'26*) **EyeWorld: A Generative World Model of Ocular State and Dynamics**
  [[📝 Paper](https://arxiv.org/abs/2603.14039)]

- (*arXiv'26*) **SAW: Toward a Surgical Action World Model via Controllable and Scalable Video Generation**
  [[📝 Paper](https://arxiv.org/abs/2603.13024)]

- (*ICLR'26 Rejected*) **Unified Surgical World Model for Structured Understanding, Long-Horizon Prediction, and Fine-Grained Generation**
  [[📝 Paper](https://openreview.net/forum?id=Kk9t5empEf)]

- (*MIDL'26 rejected*) **Learning Action-Conditioned World Models for Cataract Surgery from Unlabeled Videos (SurgWorld)**
  [[📝 Paper](https://openreview.net/forum?id=aYQYOVm2AB)]

- (*CVPR'26*) **X-WIN: Building Chest Radiograph World Model via Predictive Sensing**
  [[📝 Paper](https://arxiv.org/abs/2511.14918)]

- (*arXiv'26*) **Brain-WM: Brain Glioblastoma World Model**
  [[📝 Paper](https://arxiv.org/abs/2603.07562)] [[💻 Code](https://github.com/thibault-wch/Brain-GBM-world-model)]

- (*bioRxiv'26*) **Towards building a World Model to simulate perturbation-induced cellular dynamics by AlphaCell**
  [[📝 Paper](https://www.biorxiv.org/content/10.64898/2026.03.02.709176v1)]

- (*CVPR'26*) **MRI Contrast Enhancement Kinetics World Model**
  [[📝 Paper](https://arxiv.org/abs/2602.19285)] [[💻 Code](https://github.com/DD0922/MRI-Contrast-Enhancement-Kinetics-World-Model)]

- (*arXiv'26*) **Contextual Invertible World Models: A Neuro-Symbolic Agentic Framework for Colorectal Cancer Drug Response**
  [[📝 Paper](https://arxiv.org/abs/2603.02274)]

- (*medRxiv'26*) **MedOS: AI-XR-Cobot World Model for Clinical Perception and Action**
  [[📝 Paper](https://www.medrxiv.org/content/10.64898/2026.02.18.26345936v1)]

- (*arXiv'26*) **EHRWorld: A Patient-Centric Medical World Model for Long-Horizon Clinical Trajectories**
  [[📝 Paper](https://arxiv.org/abs/2602.03569)]

- (*AI Medicine'26*) **World Model Enhanced Offline Reinforcement Learning for Sequential Intervention Optimization in Acute Kidney Injury**
  [[📝 Paper](https://www.sciltp.com/journals/aim/articles/2602002965)]

- (*arXiv'26*) **The Patient is not a Moving Document: A World Model Training Paradigm for Longitudinal EHR**
  [[📝 Paper](https://arxiv.org/abs/2601.22128)]

- (*arXiv'26*) **Generating Counterfactual Patient Timelines from Real-World Data**
  [[📝 Paper](https://arxiv.org/abs/2604.02337)]

- (*arXiv'26*) **Policy4OOD: A Knowledge-Guided World Model for Policy Intervention Simulation against the Opioid Overdose Crisis**
  [[📝 Paper](https://arxiv.org/abs/2602.12373)]

- (*arXiv'26*) **BLINK: Behavioral Latent Modeling of NK Cell Cytotoxicity**
  [[📝 Paper](https://arxiv.org/abs/2603.05110)]

- (*arXiv'26*) **RAVEN: Scaling Recurrence-Aware Foundation Models for Clinical Records via Next-Visit Prediction**
  [[📝 Paper](https://arxiv.org/abs/2603.24562)]

### 2025

- (*arXiv'25*) **Cosmos-H-Surgical: Learning Surgical Robot Policies from Videos via World Modeling**
  [[📝 Paper](https://arxiv.org/abs/2512.23162)] [[💻 Code](https://huggingface.co/nvidia/Cosmos-H-Surgical-Simulator)] [[💻 Code](https://github.com/nvidia-cosmos/cosmos-cookbook)]

- (*arXiv'25*) **CLARITY: Medical World Model for Guiding Treatment Decisions by Modeling Context-Aware Disease Trajectories in Latent Space**
  [[📝 Paper](https://arxiv.org/abs/2512.08029)]

- (*arXiv'25*) **VCWorld: A Biological World Model for Virtual Cell Simulation**
  [[📝 Paper](https://arxiv.org/abs/2512.00306)]

- (*arXiv'25*) **How Far Are Surgeons from Surgical World Models? A Pilot Study on Zero-shot Surgical Video Generation with Expert Assessment**
  [[📝 Paper](https://arxiv.org/abs/2511.01775)]

- (*arXiv'25*) **Evolving Diagnostic Agents in a Virtual Clinical Environment**
  [[📝 Paper](https://arxiv.org/abs/2510.24654)]

- (*arXiv'25*) **ODesign: A World Model for Biomolecular Interaction Design**
  [[📝 Paper](https://arxiv.org/abs/2510.22304)] [[💻 Code](https://github.com/The-Institute-for-AI-Molecular-Design/ODesign)] [[🌐 Project](https://odesign1.github.io/)]

- (*arXiv'25*) **Cosmos-Surg-dVRK: World Foundation Model-based Automated Online Evaluation of Surgical Robot Policy Learning**
  [[📝 Paper](https://arxiv.org/abs/2510.16240)]

- (*bioRxiv'25*) **GeneJepa: A Predictive World Model of the Transcriptome**
  [[📝 Paper](https://www.biorxiv.org/content/10.1101/2025.10.14.682378v1)] [[💻 Code](https://github.com/BiostateAI/GeneJEPA)] [[🌐 Weights](https://huggingface.co/elonlit/GeneJEPA)]

- (*bioRxiv'25*) **Virtual Clinical Trials of BMP4 Differentiation Therapy: Digital Twins to Aid Successful Glioblastoma Trial Design**
  [[📝 Paper](https://doi.org/10.1101/2024.08.22.609156)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41279885/)] [[💻 Code](https://github.com/Harbour-N/Virtual-Clinical-Trials-of-BMP4-Differentiation-Therapy)]

- (*NPJ Digit Med'25*) **Large Language Models Forecast Patient Health Trajectories Enabling Digital Twins**
  [[📝 Paper](https://doi.org/10.1038/s41746-025-02004-3)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41034564/)] [[💻 Code](https://github.com/MendenLab/DT-GPT)]

- (*MICCAI'25*) **World Model for AI Autonomous Navigation in Mechanical Thrombectomy**
  [[📝 Paper](https://arxiv.org/abs/2509.25518)]

- (*J Diabetes Sci Technol'25*) **Including Aerobic Exercise Into Data-Based Virtual Twins for Glycemic Simulation**
  [[📝 Paper](https://doi.org/10.1177/19322968251364291)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/40947716/)]

- (*arXiv'25*) **medDreamer: Model-Based Reinforcement Learning with Latent Imagination on Complex EHRs for Clinical Decision Support**
  [[📝 Paper](https://arxiv.org/abs/2505.19785)]

- (*arXiv'25*) **Generative Medical Event Models Improve with Scale (CoMET)**
  [[📝 Paper](https://arxiv.org/abs/2508.12104)]

- (*arXiv'25*) **Visuomotor Grasping with World Models for Surgical Robots**
  [[📝 Paper](https://arxiv.org/abs/2508.11200)]

- (*arXiv'25*) **Xray2Xray: World Model from Chest X-rays with Volumetric Context**
  [[📝 Paper](https://arxiv.org/abs/2506.19055)]

- (*ICCV'25*) **Medical World Model: Generative Simulation of Tumor Evolution for Treatment Planning**
  [[📝 Paper](https://arxiv.org/abs/2506.02327)] [[💻 Code](https://github.com/scott-yjyang/MeWM)] [[🌐 Project](https://yijun-yang.github.io/MeWM/)]

- (*CVPR'25*) **CheXWorld: Exploring Image World Modeling for Radiograph Representation Learning**
  [[📝 Paper](https://arxiv.org/abs/2504.13820)] [[💻 Code](https://github.com/LeapLabTHU/CheXWorld)]

- (*CVPR'25*) **EchoWorld: Learning Motion-Aware World Models for Echocardiography Probe Guidance**
  [[📝 Paper](https://arxiv.org/abs/2504.13065)]

- (*bioRxiv'25*) **Generative World Models to compute protein folding pathways**
  [[📝 Paper](https://www.biorxiv.org/content/10.1101/2025.03.26.645554v1)]

- (*arXiv'25*) **Towards Suturing World Models: Learning Predictive Models for Robotic Surgical Tasks**
  [[📝 Paper](https://arxiv.org/abs/2503.12531)] [[🌐 Project](https://mkturkcan.github.io/suturingmodels/)]

- (*MICCAI Workshop'25*) **Surgical Vision World Model**
  [[📝 Paper](https://arxiv.org/abs/2503.02904)] [[💻 Code](https://github.com/bhattarailab/Surgical-Vision-World-Model)]

- (*arXiv'25*) **MM-DADM: Multimodal Drug-Aware Diffusion Model for Virtual Clinical Trials**
  [[📝 Paper](https://arxiv.org/abs/2502.07297)]

- (*MIDL'25*) **4D-VQ-GAN: A World Model for Synthesizing Medical Scans at Any Time Point for Personalized Disease Progression Modeling of Idiopathic Pulmonary Fibrosis**
  [[📝 Paper](https://openreview.net/forum?id=tU3IpPQCEc)] [[💻 Code](https://github.com/anzhao920/4DVQGAN)] [[📝 arXiv](https://arxiv.org/abs/2502.05713)]

### 2024

- (*arXiv'24*) **Structure-aware World Model for Probe Guidance via Large-scale Self-supervised Pre-train**
  [[📝 Paper](https://arxiv.org/abs/2406.19756)]

- (*MICCAI'24*) **Cardiac Copilot: Automatic Probe Guidance for Echocardiography with World Model** (introduces Cardiac Dreamer as the world model for cardiac spatial structures)
  [[📝 Paper](https://arxiv.org/abs/2406.13165)]

- (*arXiv'24*) **World Models for General Surgical Grasping**
  [[📝 Paper](https://arxiv.org/abs/2405.17940)]

---

## 🧭 By Topic

> A complementary topic-wise view.

### Medical Imaging and Radiology

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

- (*CVPR'25*) **CheXWorld: Exploring Image World Modeling for Radiograph Representation Learning**
  [[📝 Paper](https://arxiv.org/abs/2504.13820)] [[💻 Code](https://github.com/LeapLabTHU/CheXWorld)]

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

- (*arXiv'26*) **Contextual Invertible World Models: A Neuro-Symbolic Agentic Framework for Colorectal Cancer Drug Response**
  [[📝 Paper](https://arxiv.org/abs/2603.02274)]

- (*arXiv'25*) **VCWorld: A Biological World Model for Virtual Cell Simulation**
  [[📝 Paper](https://arxiv.org/abs/2512.00306)]

- (*arXiv'25*) **ODesign: A World Model for Biomolecular Interaction Design**
  [[📝 Paper](https://arxiv.org/abs/2510.22304)] [[💻 Code](https://github.com/The-Institute-for-AI-Molecular-Design/ODesign)] [[🌐 Project](https://odesign1.github.io/)]

- (*bioRxiv'25*) **GeneJepa: A Predictive World Model of the Transcriptome**
  [[📝 Paper](https://www.biorxiv.org/content/10.1101/2025.10.14.682378v1)] [[💻 Code](https://github.com/BiostateAI/GeneJEPA)] [[🌐 Weights](https://huggingface.co/elonlit/GeneJEPA)]

- (*bioRxiv'25*) **Generative World Models to compute protein folding pathways**
  [[📝 Paper](https://www.biorxiv.org/content/10.1101/2025.03.26.645554v1)]

### Longitudinal EHR and Clinical Trajectories

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

- (*arXiv'26*) **Apollo: A Multimodal and Temporal Foundation Model for Virtual Patient Representations at Healthcare System Scale**
  [[📝 Paper](https://arxiv.org/abs/2604.18570)]

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

- (*arXiv'26*) **Validated Synthetic Patient Generation for Small Longitudinal Cohorts: Coagulation Dynamics Across Pregnancy**
  [[📝 Paper](https://arxiv.org/abs/2604.07557)] [[💻 Code](https://github.com/varnerlab/SA-generation-legacy-dataset-paper)]

- (*Cardiometab Syndr J'26*) **TyG Trajectory and Digital Twin Simulation to Predict Metabolic Syndrome Risk**
  [[📝 Paper](https://doi.org/10.51789/cmsj.2026.6.e7)]

- (*NPJ Digit Med'25*) **Large Language Models Forecast Patient Health Trajectories Enabling Digital Twins**
  [[📝 Paper](https://doi.org/10.1038/s41746-025-02004-3)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41034564/)] [[💻 Code](https://github.com/MendenLab/DT-GPT)]

- (*arXiv'25*) **medDreamer: Model-Based Reinforcement Learning with Latent Imagination on Complex EHRs for Clinical Decision Support**
  [[📝 Paper](https://arxiv.org/abs/2505.19785)]

- (*arXiv'25*) **Generative Medical Event Models Improve with Scale (CoMET)**
  [[📝 Paper](https://arxiv.org/abs/2508.12104)]

### Treatment Planning and Clinical Decision Support

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

- (*Cardiometab Syndr J'26*) **TyG Trajectory and Digital Twin Simulation to Predict Metabolic Syndrome Risk**
  [[📝 Paper](https://doi.org/10.51789/cmsj.2026.6.e7)]

- (*arXiv'25*) **CLARITY: Medical World Model for Guiding Treatment Decisions by Modeling Context-Aware Disease Trajectories in Latent Space**
  [[📝 Paper](https://arxiv.org/abs/2512.08029)]

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

- (*arXiv'25*) **How Far Are Surgeons from Surgical World Models? A Pilot Study on Zero-shot Surgical Video Generation with Expert Assessment**
  [[📝 Paper](https://arxiv.org/abs/2511.01775)]

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
  [[🌐 Platform](https://developer.nvidia.com/cosmos)] [[📝 Blog](https://developer.nvidia.com/blog/nvidia-cosmos-world-foundation-model-for-physical-ai/)]
  > General-purpose world foundation model platform; extended to surgical simulation via **Cosmos-H-Surgical** and **Cosmos-H-Surgical-Simulator** (see [papers above](#surgical-simulation-and-embodied-healthcare)).

- (*NVIDIA'25*) **Holoscan AI Platform**
  [[🌐 Platform](https://developer.nvidia.com/holoscan)]
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

<a href="https://www.star-history.com/?repos=chengwang96%2FAwesome-World-Models-for-Healthcare&type=date&logscale=&legend=bottom-right">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/image?repos=chengwang96/Awesome-World-Models-for-Healthcare&type=date&theme=dark&legend=bottom-right" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/image?repos=chengwang96/Awesome-World-Models-for-Healthcare&type=date&legend=bottom-right" />
   <img alt="Star History Chart" src="https://api.star-history.com/image?repos=chengwang96/Awesome-World-Models-for-Healthcare&type=date&legend=bottom-right" />
 </picture>
</a>

---

## 🤝 Contributing

Contributions are welcome!

If you find any relevant papers, codebases, benchmarks, or project pages related to **world models for healthcare**, feel free to:

- open an **Issue**
- submit a **Pull Request**

Suggested format:

```markdown
- (*Venue'Year*) **Paper Title** [[📝 Paper](link)] [[💻 Code](link)]
```

Please try to keep the formatting consistent with the existing entries.

Submissions should match the [**inclusion scope**](#-world-model-papers) above (world models or explicit clinical process simulation—not generic medical GenAI unless the paper’s contribution is clearly world-modeling).

---

## ✉️ Contact Us

If you have any questions or suggestions, please feel free to contact us via:

**Email:** chengwang@link.cuhk.edu.hk, zhihaopeng@cuhk.edu.hk
