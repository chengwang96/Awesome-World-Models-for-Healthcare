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

## 📌 Contents

- [Survey Papers](#-survey-papers)
- [World Model Papers](#-world-model-papers)
- [By Topic](#-by-topic)
- [Related Repositories](#-related-repositories)
- [产业模型 / 平台](#-产业模型--平台)
- [Special Issues / Calls](#-special-issues--calls)
- [Contributing](#-contributing)
- [Contact Us](#-contact-us)

---

## 📚 Survey Papers

- (*NeurIPS'25 Workshop*) **Beyond Generative AI: World Models for Clinical Prediction, Counterfactuals, and Planning**
  [[📝 Paper](https://arxiv.org/abs/2511.16333)]

---

## 📝 World Model Papers

> Entries are sorted by year in descending order.

> **Inclusion scope.** We prioritize work where a **world model** (or an explicitly equivalent formulation) is the main object of study: learned simulators or dynamics models of clinically relevant processes—e.g., latent-state prediction, imagination rollouts, patient or disease-trajectory simulation, or environment models for clinical agents. Pure segmentation/classification with a generative or foundation backbone, or continual learning that only uses generative replay without modeling a clinical process as dynamics, is usually **out of scope** even if the title says “foundation” or “generative.” When unsure, open an Issue before a PR.

### 2026

- (*arXiv'26*) **Validated Synthetic Patient Generation for Small Longitudinal Cohorts: Coagulation Dynamics Across Pregnancy**
  [[📝 Paper](https://arxiv.org/abs/2604.07557)] [[💻 Code](https://github.com/varnerlab/SA-generation-legacy-dataset-paper)]

- (*arXiv'26*) **Toward World Models for Epidemiology**
  [[📝 Paper](https://arxiv.org/abs/2604.09519)]

- (*arXiv'26*) **WOMBET: World Model-based Experience Transfer for Robust and Sample-efficient Reinforcement Learning**
  [[📝 Paper](https://arxiv.org/abs/2604.08958)]

- (*npj Health Systems'26*) **Design for a Digital Twin in Clinical Patient Care**
  [[📝 Paper](https://doi.org/10.1038/s44401-025-00060-1)] [[📝 arXiv](https://arxiv.org/abs/2505.01206)]

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

- (*arXiv'26*) **Evaluating the impact of longitudinal treatment strategies in the presence of informative monitoring and time-dependent confounding**
  [[📝 Paper](https://arxiv.org/abs/2604.09898)]

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

- (*MICCAI'25*) **World Model for AI Autonomous Navigation in Mechanical Thrombectomy**
  [[📝 Paper](https://arxiv.org/abs/2509.25518)]

- (*arXiv'25*) **medDreamer: Model-Based Reinforcement Learning with Latent Imagination on Complex EHRs for Clinical Decision Support**
  [[📝 Paper](https://arxiv.org/abs/2505.19785)]

- (*arXiv'25*) **Generative Medical Event Models Improve with Scale (CoMET)**
  [[📝 Paper](https://arxiv.org/abs/2508.12104)]

- (*arXiv'25*) **Visuomotor Grasping with World Models for Surgical Robots**
  [[📝 Paper](https://arxiv.org/abs/2508.11200)]

- (*bioRxiv'25*) **STELLA: Towards a Biomedical World Model with Self-Evolving Multimodal Agents**
  [[📝 Paper](https://www.biorxiv.org/content/10.1101/2025.07.01.662467v2)] [[💻 Code](https://github.com/zaixizhang/STELLA)] [[🌐 Project](https://stella-agent.com/)]

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

### Surveys and Perspectives

- (*NeurIPS'25 Workshop*) **Beyond Generative AI: World Models for Clinical Prediction, Counterfactuals, and Planning**
  [[📝 Paper](https://arxiv.org/abs/2511.16333)]

### Medical Imaging and Radiology

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

- (*MIDL'25*) **4D-VQ-GAN: A World Model for Synthesizing Medical Scans at Any Time Point for Personalized Disease Progression Modeling of Idiopathic Pulmonary Fibrosis**
  [[📝 Paper](https://openreview.net/forum?id=tU3IpPQCEc)] [[💻 Code](https://github.com/anzhao920/4DVQGAN)] [[📝 arXiv](https://arxiv.org/abs/2502.05713)]

- (*arXiv'24*) **Structure-aware World Model for Probe Guidance via Large-scale Self-supervised Pre-train**
  [[📝 Paper](https://arxiv.org/abs/2406.19756)]

- (*MICCAI'24*) **Cardiac Copilot: Automatic Probe Guidance for Echocardiography with World Model** (introduces Cardiac Dreamer as the world model for cardiac spatial structures)
  [[📝 Paper](https://arxiv.org/abs/2406.13165)]

### Computational Biology and Cellular Dynamics

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

- (*bioRxiv'25*) **STELLA: Towards a Biomedical World Model with Self-Evolving Multimodal Agents**
  [[📝 Paper](https://www.biorxiv.org/content/10.1101/2025.07.01.662467v2)] [[💻 Code](https://github.com/zaixizhang/STELLA)] [[🌐 Project](https://stella-agent.com/)]

- (*bioRxiv'25*) **Generative World Models to compute protein folding pathways**
  [[📝 Paper](https://www.biorxiv.org/content/10.1101/2025.03.26.645554v1)]

### Longitudinal EHR and Clinical Trajectories

- (*arXiv'26*) **Evaluating the impact of longitudinal treatment strategies in the presence of informative monitoring and time-dependent confounding**
  [[📝 Paper](https://arxiv.org/abs/2604.09898)]

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

- (*arXiv'25*) **medDreamer: Model-Based Reinforcement Learning with Latent Imagination on Complex EHRs for Clinical Decision Support**
  [[📝 Paper](https://arxiv.org/abs/2505.19785)]

- (*arXiv'25*) **Generative Medical Event Models Improve with Scale (CoMET)**
  [[📝 Paper](https://arxiv.org/abs/2508.12104)]

### Treatment Planning and Clinical Decision Support

- (*arXiv'26*) **Brain-WM: Brain Glioblastoma World Model**
  [[📝 Paper](https://arxiv.org/abs/2603.07562)] [[💻 Code](https://github.com/thibault-wch/Brain-GBM-world-model)]

- (*arXiv'25*) **CLARITY: Medical World Model for Guiding Treatment Decisions by Modeling Context-Aware Disease Trajectories in Latent Space**
  [[📝 Paper](https://arxiv.org/abs/2512.08029)]

- (*ICCV'25*) **Medical World Model: Generative Simulation of Tumor Evolution for Treatment Planning**
  [[📝 Paper](https://arxiv.org/abs/2506.02327)] [[💻 Code](https://github.com/scott-yjyang/MeWM)] [[🌐 Project](https://yijun-yang.github.io/MeWM/)]

- (*AI Medicine'26*) **World Model Enhanced Offline Reinforcement Learning for Sequential Intervention Optimization in Acute Kidney Injury**
  [[📝 Paper](https://www.sciltp.com/journals/aim/articles/2602002965)]

- (*arXiv'25*) **Evolving Diagnostic Agents in a Virtual Clinical Environment**
  [[📝 Paper](https://arxiv.org/abs/2510.24654)]

### Surgical Simulation and Embodied Healthcare

- (*arXiv'26*) **SAW: Toward a Surgical Action World Model via Controllable and Scalable Video Generation**
  [[📝 Paper](https://arxiv.org/abs/2603.13024)]

- (*ICLR'26 Rejected*) **Unified Surgical World Model for Structured Understanding, Long-Horizon Prediction, and Fine-Grained Generation**
  [[📝 Paper](https://openreview.net/forum?id=Kk9t5empEf)]

- (*MIDL'26 rejected*) **Learning Action-Conditioned World Models for Cataract Surgery from Unlabeled Videos (SurgWorld)**
  [[📝 Paper](https://openreview.net/forum?id=aYQYOVm2AB)]

- (*medRxiv'26*) **MedOS: AI-XR-Cobot World Model for Clinical Perception and Action**
  [[📝 Paper](https://www.medrxiv.org/content/10.64898/2026.02.18.26345936v1)]

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

## 🏭 产业模型 / 平台

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