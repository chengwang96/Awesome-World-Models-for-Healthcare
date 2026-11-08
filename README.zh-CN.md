<h1 align="center">
  <strong>Awesome-World-Models-for-Healthcare</strong>
</h1>

<div align="center">

[English](README.md) | **简体中文**

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![GitHub 星标](https://img.shields.io/github/stars/chengwang96/Awesome-World-Models-for-Healthcare?style=social)](https://github.com/chengwang96/Awesome-World-Models-for-Healthcare)
[![欢迎贡献](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](#-contributing)
[![目录校验](https://github.com/chengwang96/Awesome-World-Models-for-Healthcare/actions/workflows/validate-catalog.yml/badge.svg)](https://github.com/chengwang96/Awesome-World-Models-for-Healthcare/actions/workflows/validate-catalog.yml)
[![链接检查](https://github.com/chengwang96/Awesome-World-Models-for-Healthcare/actions/workflows/check-links.yml/badge.svg)](https://github.com/chengwang96/Awesome-World-Models-for-Healthcare/actions/workflows/check-links.yml)
[![内容许可：CC BY 4.0](https://img.shields.io/badge/content-CC%20BY%204.0-lightgrey.svg)](LICENSE-CONTENT)
[![代码许可：MIT](https://img.shields.io/badge/code-MIT-blue.svg)](LICENSE)

精选**医疗健康世界模型**相关论文与开源资源，涵盖**医学影像**、**纵向电子健康记录建模**、**临床预测**、**反事实推理**、**治疗规划**与**手术模拟**。

</div>

> 中文预览：基于 2026-11-08 的英文 README，主目录共 164 篇论文。论文标题保留英文原名，便于检索；目录结构、收录依据与资源说明均提供中文。

---

<a id="-scope"></a>

## 🎯 收录范围与分类

**世界模型**学习环境的动力学，使智能体能够在不与真实系统交互的情况下预测未来状态、模拟干预并规划动作。经典代表包括 Ha 与 Schmidhuber（2018）、Dreamer（Hafner 等，2020）和 JEPA（LeCun，2022）。

本项目收录将世界模型或具有同等功能的学习式动力学／模拟模型应用于以下领域的论文：

- **医学影像**：放射学、超声、眼科、病理与造影剂动力学
- **手术模拟与机器人**：基于视频的预测、动作条件手术模型与机器人策略学习
- **临床决策支持与治疗规划**：疾病轨迹模拟、肿瘤演化与患者反事实时间线
- **纵向电子健康记录与患者轨迹**：下一次就诊预测、临床事件建模与合成患者生成
- **计算生物学与药物发现**：细胞动力学、转录组建模、蛋白质折叠与药物反应
- **流行病学与公共卫生**：疾病传播建模与政策干预模拟

### 严格收录标准

主目录中的论文必须**同时满足**以下全部标准。仅将方法命名为“世界模型”“数字孪生”或“世界建模”，不足以构成收录依据。

| 标准 | 所需证据 |
|---|---|
| **医学相关性** | 建模系统与评估任务直接面向生物医学、临床或医疗健康。 |
| **状态** | 方法表示患者、器官、细胞、分子、操作过程、群体或医疗环境的状态。 |
| **动力学** | 方法学习或计算随时间、空间、操作步骤、视角或干预而发生的状态转移。 |
| **可执行推演** | 支持未来预测、多步模拟、反事实干预、规划或控制。 |
| **实现与评估证据** | 论文实际实现并评估了动力学或模拟器，而非仅提出概念或评测基准。 |

疾病进展、心脏运动等自主生理过程可以不含动作条件。但若论文声称具备干预、治疗或控制能力，就必须建模动作如何改变后续状态。

<a id="-taxonomy"></a>

### 🧬 分类体系

主目录为每篇论文提供简明、统一的元数据，便于查找具有相似建模状态与能力的方法。

| 字段 | 取值 | 含义 |
|---|---|---|
| **状态（State）** | 患者、生理、解剖、医学影像、操作／机器人、诊疗流程、细胞、分子、群体 | 模型推进的主要医学或生物学状态。 |
| **动力学（Dynamics）** | 时间演化、动作条件、机制模型、空间／视角、事件序列 | 方法实现的转移结构，可同时包含多项。 |
| **能力（Capability）** | 预测、模拟、反事实、规划、控制 | 模型推演所支持的用途。 |
| **资源（Assets）** | 代码、权重、项目、仅论文 | 条目所链接的公开实现或项目资源。 |

标签依据已展示的方法能力填写，不根据论文标题推断。

---

## 📌 目录

- [收录范围与分类](#-scope)
- [综述与观点](#-survey-papers)
- [世界模型论文](#-world-model-papers)
- [按主题浏览](#-by-topic)
- [资源](#resources)
- [专刊与征稿](#-special-issues--calls)
- [项目信息](#project-information)

---

<a id="-survey-papers"></a>

## 📚 综述与观点

- (*J Imaging Inform Med'26 Perspective*) **Toward Verifiable Medical Imaging World Models: An Engineering Framework for Evaluating Simulation Fidelity, Roll-Out Stability, and Clinical Plausibility**
  [[📝 论文](https://doi.org/10.1007/s10278-026-02413-0)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42907729/)]

- (*arXiv'26 Perspective*) **From Prediction to Action: Population Health World Model for Digital Medicine**
  [[📝 论文](https://arxiv.org/abs/2610.24662)]

- (*arXiv'26 Perspective*) **Rethinking World Models for Biosignals**
  [[📝 论文](https://arxiv.org/abs/2610.17510)]

- (*Cell'26 Review*) **World Models for Biomedicine**
  [[📝 论文](https://doi.org/10.1016/j.cell.2026.08.032)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42753693/)]

- (*Cell'26 Review*) **A World Model of the Virtual Cell**
  [[📝 论文](https://doi.org/10.1016/j.cell.2026.08.042)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42753692/)]

- (*npj Health Syst'26 Perspective*) **Structural Requirements for Intelligent Clinical Digital Twins in Feedback-Driven Care**
  [[📝 论文](https://doi.org/10.1038/s44401-026-00143-7)]

- (*arXiv'26*) **Surgical Video Generation From Diffusion to World Models: A Survey**
  [[📝 论文](https://arxiv.org/abs/2608.26214)]

- (*arXiv'26 Perspective*) **Physiological World Models for Human State Transitions**
  [[📝 论文](https://arxiv.org/abs/2608.15309)]

- (*J Robot Surg'26*) **Digital Twin-Enabled Robotic Surgery: A Bibliometric and Knowledge-Mapping Analysis from Patient-Specific Simulation to Autonomy and Clinical Translation**
  [[📝 论文](https://doi.org/10.1007/s11701-026-03739-1)]

- (*J Biomed Opt'26*) **Optical Digital Twins for Disease Prevention, Diagnosis, Therapy, and Intervention**
  [[📝 论文](https://doi.org/10.1117/1.JBO.31.8.080601)]

- (*JAMIA Open'26*) **Validating Medical Digital Twins for Clinical Decision Support: Beyond Predictive Accuracy**
  [[📝 论文](https://pubmed.ncbi.nlm.nih.gov/42553720/)]

- (*arXiv'26*) **Cardiovascular Digital Twins from Physics Based to Data Driven Approaches**
  [[📝 论文](https://arxiv.org/abs/2608.02135)]

- (*Biomed Eng Lett'26*) **Digital Twin for Neurological Conditions: A Systematic Scoping Review**
  [[📝 论文](https://doi.org/10.1007/s13534-026-00605-9)]

- (*arXiv'26*) **Medical world models in healthcare: capabilities, evidence, and trustworthy clinical translation**
  [[📝 论文](https://arxiv.org/abs/2607.25242)]

- (*arXiv'26*) **Medical World Models: Representing Medical States, Modelling Clinical Dynamics and Guiding Intervention Policies**
  [[📝 论文](https://arxiv.org/abs/2606.16721)]

- (*arXiv'26*) **Towards World Models in Biomedical Research**
  [[📝 论文](https://arxiv.org/abs/2606.05925)]

- (*arXiv'26*) **From Static Risk to Dynamic Trajectories: Toward World-Model-Inspired Clinical Prediction**
  [[📝 论文](https://arxiv.org/abs/2605.16927)]

- (*arXiv'26*) **Grounding Clinical AI Competency in Human Cognition Through the Clinical World Model and Skill-Mix Framework**
  [[📝 论文](https://arxiv.org/abs/2604.08226)]

- (*arXiv'26*) **Toward World Models for Epidemiology**
  [[📝 论文](https://arxiv.org/abs/2604.09519)]

- (*NeurIPS'25 Workshop*) **Beyond Generative AI: World Models for Clinical Prediction, Counterfactuals, and Planning**
  [[📝 论文](https://arxiv.org/abs/2511.16333)]

---

<a id="-world-model-papers"></a>

## 📝 世界模型论文

> 条目按年份从新到旧排列。收录标准见[收录范围](#-scope)。

### 2026

- (*arXiv'26*) **SurgTransfer: Multi-Step Latent Action Modeling for Action Transfer in Surgical World Model**
  [[📝 论文](https://arxiv.org/abs/2611.05443)] [[💻 代码](https://github.com/bhattarailab/Surgical-Vision-World-Model)]
  **元数据：** `状态：操作／机器人` · `动力学：时间演化 + 动作条件` · `能力：模拟` · `资源：代码`
  <details>
  <summary>收录依据</summary>
  <p>将从视频中提取的潜在动作序列迁移至初始手术画面，模拟后续场景演化；在 SurgToolLoc 和 PitVis 上评估了 14 帧续接预测及外科医生判定的合理性。动作是预先记录的潜在轨迹，并非可交互的机器人指令。</p>
  </details>

- (*arXiv'26*) **PulmoWorld: An Asynchronous Multimodal Medical World Model for Longitudinal Pneumonia Dynamics**
  [[📝 论文](https://arxiv.org/abs/2610.38289)]
  **元数据：** `状态：患者` · `动力学：时间演化 + 动作条件` · `能力：预测 + 模拟 + 规划` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>对多模态患者信念状态进行推进，并用观测加以校正；在分别拟合的肺炎队列上评估四步临床指标与表征预测，并通过模型内推演选择动作。规划仅在机制已知的 MASS-Syn 环境中测试，尚未验证为有效的临床治疗策略。</p>
  </details>

- (*Cell Rep Med'26*) **Tumor digital twins uncover therapeutic strategies in triple-negative breast cancer**
  [[📝 论文](https://doi.org/10.1016/j.xcrm.2026.103119)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42933397/)] [[💻 代码](https://github.com/jfisher-lab/TNBC_Victori2026)]
  **元数据：** `状态：细胞` · `动力学：机制模型 + 动作条件` · `能力：模拟 + 规划` · `资源：代码`
  <details>
  <summary>收录依据</summary>
  <p>在患者基因组与药物扰动条件下计算信号网络的同步状态转移，利用吸引子表型复现治疗反应并筛选恢复药物敏感性的靶点；更新步数未对应经过校准的临床时间，所推荐方案也未经过前瞻性验证。</p>
  </details>

- (*medRxiv'26*) **Digital Twin Workflow for Continuous Glucose Forecasting: Real-Time Data Assimilation Using Reinforcement Learning**
  [[📝 论文](https://www.medrxiv.org/content/10.64898/2026.10.23.26366163v1)]
  **元数据：** `状态：生理` · `动力学：时间演化` · `能力：预测` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>在此前脓毒症患者血糖孪生模型上加入有界的首步残差校正，并递归生成 15 步预测，在十名 ICU 患者中进行回顾性评估；强化学习动作调整的是预测值，而非胰岛素给药或其他生理干预。</p>
  </details>

- (*arXiv'26*) **DuoPIC: Uncertainty-Aware Voxel-Level Digital Twins of Cerebral Perfusion with Transport PDEs in Acute Stroke**
  [[📝 论文](https://arxiv.org/abs/2610.33071)] [[💻 代码](https://github.com/detinatran/duopic)]
  **元数据：** `状态：生理` · `动力学：时间演化 + 机制模型` · `能力：模拟` · `资源：代码`
  <details>
  <summary>收录依据</summary>
  <p>通过学习到的闭合项，将区域血流与随时间演化的示踪剂输运相耦合；评估了被遮蔽的时间片段、留出患者的动力学以及卒中病灶图。在其余帧上重新拟合不等同于前瞻性临床预测，也不构成经过验证的再灌注治疗模拟。</p>
  </details>

- (*arXiv'26*) **Saga: an in silico ontology for a multimodal patient world model**
  [[📝 论文](https://arxiv.org/abs/2610.33054)]
  **元数据：** `状态：患者` · `动力学：时间演化 + 事件序列 + 动作条件` · `能力：预测 + 模拟` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>通过生成事件及发生时间、将其追加至病史并重新编码，推进共享的肿瘤患者状态，评估八步自由推演，并另行评估配对的随访影像；治疗条件下的输出变化尚不能证明因果治疗效应或规划获益。</p>
  </details>

- (*arXiv'26*) **CaMeWM: A Causal Medical World Model for Generative Tumor Evolution and Treatment Planning**
  [[📝 论文](https://arxiv.org/abs/2610.26923)]
  **元数据：** `状态：医学影像` · `动力学：动作条件` · `能力：预测 + 模拟 + 规划` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>在受支持的 TACE 方案下模拟病灶局部的随访 CT 状态，按生存效用对采样得到的候选结果排序，并在 79 个诊疗事件中评估事实状态转移与观察性策略价值；实现的是一次治疗后的状态转移，尚未评估序贯治疗策略或前瞻性获益。</p>
  </details>

- (*Protein Sci'26*) **DreamFold: A World Model to efficiently generate protein folding pathways in the latent space**
  [[📝 论文](https://doi.org/10.1002/pro.70794)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42813590/)] [[📝 预印本](https://www.biorxiv.org/content/10.1101/2025.03.26.645554v1)]
  **元数据：** `状态：分子` · `动力学：事件序列 + 动作条件` · `能力：模拟 + 规划` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>在二面角动作下推进蛋白质构象的潜在状态，通过模型内推演学习折叠策略，并将解码后的路径与分子模拟及实验结构比较；这些轨迹不能直接给出物理动力学或热力学性质。</p>
  </details>

- (*arXiv'26*) **SonoWorld: Towards Interactive Pose-Controllable Ultrasound World Models**
  [[📝 论文](https://arxiv.org/abs/2610.19327)] [[🌐 项目](https://iclr2027anonymous.github.io/SonoWorld/)]
  **元数据：** `状态：医学影像` · `动力学：空间／视角 + 动作条件` · `能力：模拟 + 规划` · `资源：项目`
  <details>
  <summary>收录依据</summary>
  <p>生成以探头运动为条件的未来超声视图，在留出的跟踪甲状腺扫描上测试轨迹推演与候选方向排序；有真实动作对应的数据规模较小，尚未展示实体机器人的闭环导航。</p>
  </details>

- (*medRxiv'26*) **Informing risk stratification and vaccine policy via a predictive mathematical model of SARS-COV-2 infection**
  [[📝 论文](https://www.medrxiv.org/content/10.64898/2026.10.12.26365315v1)]
  **元数据：** `状态：生理` · `动力学：时间演化 + 机制模型` · `能力：预测 + 模拟` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>通过宿主体内 ODE 推进感染过程中的病毒与免疫状态，在人体挑战试验队列上拟合动力学，并用另一独立挑战试验队列检验抗体效应预测；疫苗政策情景仍属于模型推算。</p>
  </details>

- (*bioRxiv'26*) **scMTG reconstructs single-cell temporal dynamics with Markov transition generators**
  [[📝 论文](https://www.biorxiv.org/content/10.64898/2026.06.04.730241v2)] [[💻 代码](https://github.com/liuq-lab/scMTG)]
  **元数据：** `状态：细胞` · `动力学：时间演化` · `能力：预测 + 模拟` · `资源：代码`
  <details>
  <summary>收录依据</summary>
  <p>学习采样单细胞时间点之间可组合的生成式状态转移，在六个数据集上评估被留出的中间细胞群体重建；所推断的轨迹尚不能证明因果基因调控或治疗效应。</p>
  </details>

- (*medRxiv'26*) **FERMAT: An Autoregressive Clinical Foundation Model for Disease Risk and Clinical Event Prediction**
  [[📝 论文](https://www.medrxiv.org/content/10.64898/2026.10.11.26365210v1)]
  **元数据：** `状态：患者` · `动力学：事件序列 + 时间演化` · `能力：预测 + 模拟` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>根据纵向电子健康记录递归生成临床事件与事件间隔，评估下一记录的事件及疾病风险预测；生成轨迹的五年风险预测表现弱于基于表征的方法，且未以治疗动作为条件。</p>
  </details>

- (*arXiv'26*) **PatientWM: Towards Generalizable Clinical World Models via Unified Patient States**
  [[📝 论文](https://arxiv.org/abs/2610.17059)]
  **元数据：** `状态：患者` · `动力学：时间演化 + 动作条件` · `能力：预测 + 模拟 + 规划` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>在已记录的临床动作下递归推进患者潜在状态，并在多个电子健康记录队列中评估事实情景下的多步预测；候选动作排序使用较窄的回顾性选择集合，尚未验证反事实效应或治疗获益。</p>
  </details>

- (*bioRxiv'26*) **Mechanistic prediction of fecal microbiota transplant engraftment and Clostridioides difficile colonization resistance with μODE**
  [[📝 论文](https://www.biorxiv.org/content/10.64898/2026.10.09.758137v1)] [[💻 代码](https://github.com/cumbof/muODE)]
  **元数据：** `状态：群体` · `动力学：时间演化 + 机制模型 + 动作条件` · `能力：模拟` · `资源：代码`
  <details>
  <summary>收录依据</summary>
  <p>在抗生素或供体移植条件下，将微生物代谢通量与胞外代谢物及群落状态更新相耦合，并将模拟变化与纵向 FMT 数据比较；能够捕捉条件致病菌受抑制的方向，但存在组成偏差，也未经临床疗效验证。</p>
  </details>

- (*bioRxiv'26*) **A tissue time machine to forward-predict single-timepoint data applied to tuberculosis granulomas**
  [[📝 论文](https://www.biorxiv.org/content/10.64898/2026.10.09.758083v1)]
  **元数据：** `状态：生理` · `动力学：时间演化 + 机制模型` · `能力：预测 + 模拟` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>将观测到的非人灵长类肉芽肿匹配至基于智能体的感染轨迹，向后续结局推进免疫与细菌状态；历史汇总数据支持该模拟器，但 22/28 表示模拟匹配对象之间的一致性，并非与同一组织后续观测比较所得的准确率。</p>
  </details>

- (*arXiv'26*) **Finsler Flow Matching: Dynamics-Aware Geodesic Interpolation for Single-Snapshot Trajectory Inference**
  [[📝 论文](https://arxiv.org/abs/2610.11318)] [[💻 代码](https://github.com/mlbelab/FinslerFlowMatching)]
  **元数据：** `状态：细胞` · `动力学：时间演化` · `能力：预测 + 模拟` · `资源：代码`
  <details>
  <summary>收录依据</summary>
  <p>从有向马尔可夫图学习连续的随机细胞状态转移过程，通过积分恢复被留出的中间胰腺细胞群体；评估的是分化轨迹推断，而非治疗模拟。</p>
  </details>

- (*arXiv'26*) **Sign-Constrained Intervention Effects for Domain-Generalizable ICU World Models**
  [[📝 论文](https://arxiv.org/abs/2610.11090)]
  **元数据：** `状态：生理` · `动力学：时间演化 + 动作条件` · `能力：预测 + 模拟` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>PhysioWorld 在显式药物与呼吸机事件条件下递归推进 ICU 生命体征状态，在 MIMIC 和 VitalDB 队列中评估八步自由推演及剂量扰动；观察性评估尚不能识别因果治疗效应。</p>
  </details>

- (*arXiv'26*) **Similar Predictive Fit but Different Latent Dynamics: Characterizing Learned Dynamical Structure in Personalized Models of Brain Disorders**
  [[📝 论文](https://arxiv.org/abs/2610.10850)]
  **元数据：** `状态：生理` · `动力学：时间演化` · `能力：预测` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>拟合 EEG 衍生脑状态之间的个体化转移分布，评估留出数据上的下一状态预测及与癫痫相关的转移结构；未测试自由推演的疾病预测、诊断或干预。</p>
  </details>

- (*arXiv'26*) **MD-LLM-2: A Transferable Language Model of Molecular Dynamics with Physical Conditioning and Explicit Path Probabilities**
  [[📝 论文](https://arxiv.org/abs/2610.10879)]
  **元数据：** `状态：分子` · `动力学：时间演化` · `能力：模拟` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>根据分子历史、序列与物理条件自回归生成蛋白质构象轨迹，以分子动力学参考结果评估未见结构域的结构与转移动力学；未声称具备药物疗效或临床任务能力。</p>
  </details>

- (*arXiv'26*) **UltraWorld: Learning Interactive Ultrasound World Models from Untracked Clinical Videos with Acoustic Sampling Map**
  [[📝 论文](https://arxiv.org/abs/2610.09785)] [[🌐 项目](https://ultraworld-project.github.io/)]
  **元数据：** `状态：医学影像` · `动力学：空间／视角 + 动作条件` · `能力：模拟 + 规划` · `资源：项目`
  <details>
  <summary>收录依据</summary>
  <p>利用临床视频先验和解剖引导的合成扫描，自蒸馏动作条件下的超声观测模型，再通过探头运动的模型内推演进行局部规划；闭环导航在模拟中测试，真实临床帧仅用于一致性检验。</p>
  </details>

- (*arXiv'26*) **One Frame, Full Heartbeat: ECG-Free Cardiac Cine MRI Synthesis via Phase-Conditioned Flow Matching**
  [[📝 论文](https://arxiv.org/abs/2610.09397)]
  **元数据：** `状态：解剖` · `动力学：时间演化` · `能力：预测 + 模拟` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>从一帧舒张末期 MRI 预测按相位索引的心脏位移场，并经形变生成未观测到的电影序列；在 ACDC 及外部 M&amp;Ms 数据上评估心室容积与射血分数轨迹。时间标定采用疾病类别层面的模板，而非实测的患者个体相位。</p>
  </details>

- (*arXiv'26*) **One Frame, Full Heartbeat: ECG-Free 4D Cardiac Cine MRI Synthesis via Radial-Decomposed Flow Matching**
  [[📝 论文](https://arxiv.org/abs/2610.09185)]
  **元数据：** `状态：解剖` · `动力学：时间演化` · `能力：预测 + 模拟` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>通过径向收缩先验与学习到的残余形变，将相位条件下的心脏运动合成扩展至三维体积；从单个舒张末期体积生成四维心动周期，评估生理运动及下游影像任务，所用标准相位来自群体数据。</p>
  </details>

- (*bioRxiv'26*) **Identifiable Inverse Optimal Transport for Single-Cell State Transitions**
  [[📝 论文](https://www.biorxiv.org/content/10.64898/2026.10.01.756056v1)] [[💻 代码](https://github.com/XTSgreen/IOT-single-cell-paper)]
  **元数据：** `状态：细胞` · `动力学：时间演化` · `能力：预测 + 模拟` · `资源：代码`
  <details>
  <summary>收录依据</summary>
  <p>学习细胞状态输运及连续时间生成元，用其转移矩阵将克隆与群体组成推进至未来观测，并包含独立的 CellTag 实验；治疗反应关联尚未作为干预轨迹推演得到验证。</p>
  </details>

- (*arXiv'26*) **ProCut: Probabilistic Cutting Topology for Autonomous Electrosurgical Tissue Dissection**
  [[📝 论文](https://arxiv.org/abs/2610.07515)]
  **元数据：** `状态：操作／机器人` · `动力学：时间演化 + 机制模型 + 动作条件` · `能力：模拟 + 控制` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>用可微力学模拟器在切割动作下推进可变形组织网格，从观测中更新对切割拓扑的信念，并用于机器人闭环组织分离；验证限于模拟及离体鸡皮，未在患者中测试，状态转移规律由计算得到而非学习得到。</p>
  </details>

- (*arXiv'26*) **HyperNSDE: Personalized Neural SDEs for Joint Static-Longitudinal Clinical Data Generation**
  [[📝 论文](https://arxiv.org/abs/2610.07383)] [[💻 代码](https://github.com/perrinechassat/HyperNSDE)]
  **元数据：** `状态：患者` · `动力学：时间演化` · `能力：模拟` · `资源：代码`
  <details>
  <summary>收录依据</summary>
  <p>通过具有学习到的漂移与扩散项的个体化神经随机微分方程模拟不规则患者轨迹，在结直肠癌和帕金森病队列上评估；属于以基线为条件的合成轨迹生成，未包含基于已观测病史的更新或治疗动作效应。</p>
  </details>

- (*arXiv'26*) **APOD: Reasoning-Guided Agentic Population Ordinary Differential Equation Discovery for Pharmacological Digital Twins**
  [[📝 论文](https://arxiv.org/abs/2610.06227)] [[💻 代码](https://gitlab.inria.fr/compo/apod)]
  **元数据：** `状态：生理` · `动力学：时间演化 + 机制模型 + 动作条件` · `能力：预测 + 模拟` · `资源：代码`
  <details>
  <summary>收录依据</summary>
  <p>发现并拟合可执行的剂量驱动肿瘤与血小板状态 ODE，在独立的 19 人队列中利用首个疗程数据预测血小板减少，并模拟其他放射性配体治疗安排；未观测方案下的结局仍属于模型推算。</p>
  </details>

- (*arXiv'26*) **Ultrasound Operator Guidance Using World Modeling and Retrieval Based Action Planning**
  [[📝 论文](https://arxiv.org/abs/2610.06008)]
  **元数据：** `状态：医学影像` · `动力学：空间／视角 + 动作条件` · `能力：模拟 + 规划` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>基于学习到的影像状态嵌入及已记录的动作—状态转移，规划多步颈动脉探头运动，开展回顾性导航评估及三名志愿者的实时可行性研究；实际使用的转移算子为非参数检索，而非学习到的生成式视频模型。</p>
  </details>

- (*npj Metab Health Dis'26*) **A Digital Twin for Tracking and Forecasting Glycemia with Septic Patients in ICUs**
  [[📝 论文](https://doi.org/10.1038/s44324-026-00132-2)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42823439/)]
  **元数据：** `状态：生理` · `动力学：时间演化` · `能力：预测` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>用单名患者连续血糖数据预训练的时间序列 Transformer，根据 30 分钟历史预测随后 15–30 分钟血糖；在另外十名脓毒症 ICU 患者中回顾性评估自适应与滚动预测，未包含以胰岛素为条件的模拟或治疗规划。</p>
  </details>

- (*arXiv'26*) **An Uncertainty-Guided Digital Twin Framework for Online Adaptive Proton Therapy in Head and Neck Cancer: A Feasibility Study**
  [[📝 论文](https://arxiv.org/abs/2609.39010)]
  **元数据：** `状态：解剖` · `动力学：时间演化 + 空间／视角` · `能力：预测` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>复用已收录的纵向形变迁移模型，预测治疗日 CT 与轮廓集合并估计患者特异性边界；十个回顾性病例评估了下游质子治疗计划调整，该过程仍需使用治疗日 CT 重新优化。</p>
  </details>

- (*arXiv'26*) **Graph World Models for Constrained Epidemic Policy Planning**
  [[📝 论文](https://arxiv.org/abs/2609.35545)] [[💻 代码](https://anonymous.4open.science/r/epimind-9706/README.md)]
  **元数据：** `状态：群体` · `动力学：时间演化 + 动作条件` · `能力：预测 + 模拟 + 规划` · `资源：代码`
  <details>
  <summary>收录依据</summary>
  <p>EpiMind 在联合干预序列下递归推进由图结构耦合的区域疫情状态，并规划满足资源约束的分配方案；评估结合模拟反事实与美国监测数据的回顾性预测，未实施政策的效应仍以模型为参照。</p>
  </details>

- (*arXiv'26*) **SurgGMF: Fully Causal Gaussian Motion Forecasting for Anticipatory Surgical Scene Rendering**
  [[📝 论文](https://arxiv.org/abs/2609.34733)]
  **元数据：** `状态：操作／机器人` · `动力学：时间演化` · `能力：预测` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>从既往手术场景运动预测由教师模型提取的五个未来高斯几何状态，在不使用目标帧高斯属性的情况下完成渲染；评估覆盖 EndoNeRF/StereoMIS 的 12 个数据片段，未包含动作条件或端到端前瞻性部署测试。</p>
  </details>

- (*arXiv'26*) **Towards Surgical World-Action Modeling: A Preliminary Joint Visual-Trajectory Forecasting for Surgical Motion Planning**
  [[📝 论文](https://arxiv.org/abs/2608.20284)]
  **元数据：** `状态：操作／机器人` · `动力学：时间演化` · `能力：预测` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>以每块三步的方式递归预测 15 个未来手术视觉状态与器械位置，并在 SurgWMBench 上评估；预测随时间跨度增加而退化，论文未实现动作条件控制。</p>
  </details>

- (*bioRxiv'26*) **AnnFlux: Object-Conditioned Neural Stochastic Differential Equations for Single-Cell Perturbation Dynamics**
  [[📝 论文](https://www.biorxiv.org/content/10.64898/2026.09.01.748703v1)]
  **元数据：** `状态：细胞` · `动力学：时间演化 + 动作条件` · `能力：预测 + 模拟` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>从对照细胞状态出发，积分以对象为条件的潜在随机漂移，得到后续扰动群体；恢复了留出的一天 EMT 时间点，并测试未见扰动组合，未评估序贯给药。</p>
  </details>

- (*bioRxiv'26*) **MEGA-ODE: Learning Biologically Structured and Navigable Continuous Perturbation Dynamics from Sparse Omics**
  [[📝 论文](https://www.biorxiv.org/content/10.64898/2026.08.05.742921v1)] [[💻 代码](https://github.com/Candlelight-XYJ/MEGA-ODE)]
  **元数据：** `状态：细胞` · `动力学：时间演化` · `能力：预测 + 模拟` · `资源：代码`
  <details>
  <summary>收录依据</summary>
  <p>通过图约束的神经 ODE 专家推进转录组与蛋白组状态，评估留出未来时间点的分子谱；虚拟转录因子筛选属于计算假设，尚非经过验证的治疗效应。</p>
  </details>

- (*Cell'26*) **RegVelo: Gene-Regulatory-Informed Dynamics of Single Cells**
  [[📝 论文](https://doi.org/10.1016/j.cell.2026.04.022)] [[💻 代码](https://github.com/theislab/regvelo)]
  **元数据：** `状态：细胞` · `动力学：时间演化 + 动作条件` · `能力：预测 + 模拟` · `资源：代码`
  <details>
  <summary>收录依据</summary>
  <p>学习包含基因调控信息的剪接动力学，在模拟转录因子敲除后，通过 CellRank 转移计算终末细胞命运概率；部分预测在发育生物学中经 CRISPR 与 Perturb-seq 检验，未设置疾病或治疗终点。</p>
  </details>

- (*medRxiv'26*) **A World Model Simulates the Latent Dynamics of Human Health**
  [[📝 论文](https://www.medrxiv.org/content/10.64898/2026.09.19.26363460v1)]
  **元数据：** `状态：患者` · `动力学：时间演化` · `能力：预测 + 模拟` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>HealthFlux 在观测间隔内用神经 ODE 推进患者健康潜在状态，并在新测量到来时修正；在一至五年无新增观测的情况下模拟状态并预测疾病与死亡，未评估治疗反事实。</p>
  </details>

- (*bioRxiv'26*) **PHAROS: Turning Single-Cell Perturbation Models into Target-Directed Drug-Combination Screens**
  [[📝 论文](https://www.biorxiv.org/content/10.64898/2026.09.08.749477v1)] [[💻 代码](https://github.com/jbezney61/PHAROS)]
  **元数据：** `状态：细胞` · `动力学：时间演化 + 动作条件` · `能力：模拟 + 规划` · `资源：代码`
  <details>
  <summary>收录依据</summary>
  <p>PHAROS 沿有序的双药路径串联预训练的药物条件细胞状态转移模型，搜索接近目标状态的路径；联合反应在细胞系数据集上评估，患者肿瘤排序仍属探索性结果。</p>
  </details>

- (*bioRxiv'26*) **Forecasting Cell State Futures from Static Snapshots**
  [[📝 论文](https://www.biorxiv.org/content/10.64898/2026.02.08.704720v2)] [[💻 代码](https://github.com/EperLuo/CellTempo)]
  **元数据：** `状态：细胞` · `动力学：时间演化` · `能力：预测 + 模拟` · `资源：代码`
  <details>
  <summary>收录依据</summary>
  <p>CellTempo 从初始快照自回归生成多步转录组细胞状态，评估谱系及扰动启动的命运轨迹；训练轨迹由快照数据推断，药物效应属于假设，尚未验证为有效疗法。</p>
  </details>

- (*Front Med'26*) **Beyond Static Risk Scores: Dynamic World Models Simulating Patient-Specific Trajectories to Inform Preoperative Risk Mitigation Strategies**
  [[📝 论文](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2026.1913206/full)] [[💻 代码](https://github.com/ustive/Beyond-Static-Risk-Scores-Dynamic-World-Models)]
  **元数据：** `状态：患者` · `动力学：时间演化 + 动作条件` · `能力：模拟 + 规划` · `资源：代码`
  <details>
  <summary>收录依据</summary>
  <p>DPWM 学习动作条件下的患者潜在动力学，并根据先验采样多步轨迹，对短时间窗的术前策略排序；在 MIMIC-IV、eICU-CRD 和 VitalDB 上的评估为回顾性研究，尚不能证明因果干预获益。</p>
  </details>

- (*Nature'26*) **An Operational Perturbation Proteomics-Based Virtual Cell Model**
  [[📝 论文](https://doi.org/10.1038/s41586-026-11001-9)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42717098/)] [[💻 代码](https://github.com/guomics-lab/PTV-1)]
  **元数据：** `状态：细胞` · `动力学：时间演化 + 动作条件` · `能力：预测 + 模拟` · `资源：代码`
  <details>
  <summary>收录依据</summary>
  <p>ProteinTalks 学习指定药物扰动下从基线开始的蛋白组动力学，通过神经 ODE 积分预测 6、24、48 小时状态，并利用轨迹预测抗癌药物效力与联合协同；未展示变更治疗条件的轨迹推演、序贯规划或临床获益。</p>
  </details>

- (*ECCV'26*) **CLARITY: Medical World Model for Guiding Treatment Decisions by Modeling Context-Aware Disease Trajectories in Latent Space**
  [[📝 论文](https://arxiv.org/abs/2512.08029)] [[💻 代码](https://github.com/DingTianxingjian/CLARITY)] [[🌐 项目](https://dingtianxingjian.github.io/clarity-project-page/)]
  **元数据：** `状态：患者` · `动力学：时间演化 + 动作条件` · `能力：预测 + 反事实 + 规划` · `资源：代码 + 项目`
  <details>
  <summary>收录依据</summary>
  <p>在不同治疗条件下向前推演疾病潜在状态，以支持临床决策。</p>
  </details>

- (*arXiv'26*) **NVIDIA Cosmos-H-Dreams: Real-Time Generative Physics Simulation for Surgical Robotics**
  [[📝 论文](https://arxiv.org/abs/2608.24199)] [[💻 代码](https://github.com/isaac-for-healthcare/Cosmos-H-Dreams)] [[🌐 权重](https://huggingface.co/nvidia/Cosmos-H-Dreams)]
  **元数据：** `状态：操作／机器人` · `动力学：时间演化 + 动作条件` · `能力：模拟` · `资源：代码 + 权重`
  <details>
  <summary>收录依据</summary>
  <p>将手术视频世界模型蒸馏为流式模拟器，在机器人运动学动作下推进生成的观测，并将观测反馈给策略；以实体 dVRK 实验对照评估闭环缝合任务，模拟保真度随任务而异。</p>
  </details>

- (*arXiv'26*) **Progressive Experience Fusion for Multi-Task World Model Control in Endovascular Navigation**
  [[📝 论文](https://arxiv.org/abs/2608.18647)]
  **元数据：** `状态：操作／机器人` · `动力学：时间演化 + 动作条件` · `能力：规划 + 控制` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>PEF 学习导丝状态转移、奖励与价值，用于 TD-MPC2 推演，并通过模型预测规划选择旋转及平移指令；在患者来源的血管模拟和未见过的透视卒中体模上评估，尚未在患者体内导航。</p>
  </details>

- (*arXiv'26*) **Surgical WAM: A World-Action Model for Data-Efficient Surgical Robot Learning**
  [[📝 论文](https://arxiv.org/abs/2608.11204)]
  **元数据：** `状态：操作／机器人` · `动力学：时间演化 + 动作条件` · `能力：控制` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>推理时联合采样未来观测与机器人动作标记，使动作在滚动时域执行前关注预测的未来；在四个 SurRoL 任务上评估控制成功率，而非单独评估未来视频的预测保真度。</p>
  </details>

- (*medRxiv'26*) **The Coupled Stochastic Dynamical System: A Generative Model for Simulating and Forecasting Youth Mental Health Trajectories**
  [[📝 论文](https://www.medrxiv.org/content/10.64898/2026.07.26.26358943v1)]
  **元数据：** `状态：患者` · `动力学：时间演化 + 机制模型` · `能力：模拟` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>CSDS 推进相互耦合的精神症状负担、情感、数字行为与可穿戴生理状态，在 GLOBEM 上评估个体化轨迹；下游预测为回顾性评估，孪生模型校准使用全序列汇总，而非严格限定的前瞻性初始化窗口。</p>
  </details>

- (*Life AI'26*) **Diffusion-Pref: Diffusion World Model Guided Zero-Shot Preference Learning for Safe Glucose Control in Type 1 Diabetes**
  [[📝 论文](https://www.sciltp.com/journals/lifeai/articles/2604003779)] [[💻 代码](https://github.com/aussie-bzhang/Diffusion-Pref)]
  **元数据：** `状态：生理` · `动力学：时间演化 + 动作条件` · `能力：预测 + 模拟 + 控制` · `资源：代码`
  <details>
  <summary>收录依据</summary>
  <p>在血糖历史、进餐背景与胰岛素动作条件下生成六小时血糖轨迹，利用采样结果为离线给药策略构造偏好；OhioT1DM 预测与基于模型的策略评估尚不能证明临床治疗的安全性或有效性。</p>
  </details>

- (*npj Syst Biol Appl'26*) **Learning Patient-Specific Spatial Biomarker Dynamics via Operator Learning for Alzheimer's Disease Progression**
  [[📝 论文](https://doi.org/10.1038/s41540-026-00719-x)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42082519/)]
  **元数据：** `状态：生理` · `动力学：时间演化 + 机制模型 + 动作条件` · `能力：预测 + 模拟 + 规划` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>LENO 推进患者特异性的淀粉样蛋白、tau 与神经退行性变化，在 ADNI 上评估纵向 PET 预测；额外的抗淀粉样蛋白与抗 tau 控制项用于假设性治疗优化，尚未验证为临床治疗效应。</p>
  </details>

- (*AISTATS'26*) **Bayesian Inverse Transition Learning: Learning Dynamics from Near-Optimal Trajectories**
  [[📝 论文](https://proceedings.mlr.press/v300/benac26a.html)]
  **元数据：** `状态：患者` · `动力学：时间演化 + 动作条件` · `能力：规划` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>BITL 推断动作条件状态转移矩阵的后验分布，并求解相应决策模型以得到治疗策略；医学实验使用含补液及升压药动作的 MIMIC-IV 低血压轨迹，评估离线策略一致性与奖励迁移，而非临床结局。</p>
  </details>

- (*arXiv'26*) **FlatASCEND: Autoregressive Clinical Sequence Generation with Continuous Time Prediction and Association-Based Pharmacological Testing**
  [[📝 论文](https://arxiv.org/abs/2605.04071)]
  **元数据：** `状态：患者` · `动力学：时间演化 + 事件序列` · `能力：预测 + 模拟` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>将临床事件及经过时间自回归追加至患者特异性前缀，在 MIMIC-IV 和 INSPECT 上评估自由推演轨迹；药物标记实验测试观察性关联，并明确不构成因果药理反应。</p>
  </details>

- (*arXiv'26*) **Stable Long-Horizon Neural ODE Reduced-Order Models via Learned Feedback for Biological Growth and Remodeling**
  [[📝 论文](https://arxiv.org/abs/2604.13820)] [[💻 代码](https://github.com/joel-laudo/TE-skin-NODE-ROM)]
  **元数据：** `状态：解剖` · `动力学：时间演化 + 机制模型 + 动作条件` · `能力：预测 + 模拟` · `资源：代码`
  <details>
  <summary>收录依据</summary>
  <p>在组织扩张器充胀历史条件下，利用带有学习到的生长反馈的神经 ODE 推进降阶皮肤位移与生长状态；以留出有限元模拟对照评估长时程手术组织扩张轨迹，而非临床愈合结局。</p>
  </details>

- (*bioRxiv'26*) **OPTIMIS: Optimizing Personalized Therapies through Integrated Multiscale Intelligent Simulation**
  [[📝 论文](https://www.biorxiv.org/content/10.64898/2026.03.24.713941v1)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41929084/)] [[💻 代码](https://github.com/wujah/OPTIMIS)]
  **元数据：** `状态：细胞` · `动力学：时间演化 + 机制模型 + 动作条件` · `能力：模拟 + 控制` · `资源：代码`
  <details>
  <summary>收录依据</summary>
  <p>将随机受体信号与肿瘤、CAR-T 及细胞因子的神经 ODE 动力学耦合，通过治疗条件下的推演训练给药策略；留出评估使用合成患者队列，尚未证明临床 CAR-T 治疗疗效。</p>
  </details>

- (*bioRxiv'26*) **Digital Twin Brain Simulation and Manipulation of a Functional Brain Network Underlying Mental Illness**
  [[📝 论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC13015335/)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41890017/)] [[💻 代码](https://github.com/Shmily94/Digital_twin_brain-psychiatry-)]
  **元数据：** `状态：生理` · `动力学：时间演化 + 机制模型 + 动作条件` · `能力：模拟 + 反事实` · `资源：代码`
  <details>
  <summary>收录依据</summary>
  <p>对全脑脉冲神经网络模拟器进行个体化校准，固定校准结果后，在回路参数扰动下推进神经与血流动力学状态；将模拟的网络反应与独立药理 fMRI 数据比较，尚未建立临床药物剂量—反应模型。</p>
  </details>

- (*AAAI'26*) **Bootstrapping Personalized Insulin Therapy via Model-Based Reinforcement Learning: An In Silico Study**
  [[📝 论文](https://ojs.aaai.org/index.php/AAAI/article/view/41160)]
  **元数据：** `状态：生理` · `动力学：时间演化 + 动作条件` · `能力：模拟 + 规划 + 控制` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>迁移与患者匹配的 LSTM 血糖动力学，递归模拟胰岛素条件下的轨迹，用于 H 步 Deep Dyna-Q 策略学习；给药策略在 Simglucose 中评估，真实数据验证仅测试了一名 OhioT1DM 参与者的血糖预测。</p>
  </details>

- (*arXiv'26*) **Uni-Flow: A Unified Autoregressive-Diffusion Model for Complex Multiscale Flows**
  [[📝 论文](https://arxiv.org/abs/2602.15592)]
  **元数据：** `状态：生理` · `动力学：时间演化` · `能力：预测 + 模拟` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>将自回归潜在动力学与基于扩散的空间细化相结合；医学实验跨多个心动周期推演患者特异性的主动脉缩窄表面压力场，并与高保真血流动力学模拟比较。</p>
  </details>

- (*BMC Med'26*) **Digital Twin Brain Reveals State-Specific Stimulation Targets for Abnormal Brain Dynamics in Tinnitus**
  [[📝 论文](https://doi.org/10.1186/s12916-026-04687-1)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41664110/)]
  **元数据：** `状态：生理` · `动力学：时间演化 + 机制模型 + 动作条件` · `能力：模拟` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>将连接组耦合的振荡器动力学拟合至耳鸣脑状态，在区域刺激扰动下重新模拟；将模拟状态变化与小规模独立 rTMS 数据比较，尚未前瞻性验证个体化靶点选择或症状改善。</p>
  </details>

- (*Smart Health'26*) **Patient-Specific Deep Offline Artificial Pancreas for Blood Glucose Regulation in Type 1 Diabetes**
  [[📝 论文](https://doi.org/10.1016/j.smhl.2026.100633)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41766716/)]
  **元数据：** `状态：生理` · `动力学：时间演化 + 机制模型 + 动作条件` · `能力：模拟 + 控制` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>通过系统生物学知情神经网络推断患者特异性的葡萄糖—胰岛素 ODE 参数，在离线强化学习胰岛素策略下运行该动力学；治疗比较限于计算模拟，且论文中策略实验的样本数表述不一致。</p>
  </details>

- (*arXiv'26*) **High-Fidelity Longitudinal Patient Simulation Using Real-World Data**
  [[📝 论文](https://arxiv.org/abs/2601.17310)] [[💻 代码](https://github.com/yuakagi/Watcher)]
  **元数据：** `状态：患者` · `动力学：时间演化 + 事件序列` · `能力：预测 + 模拟` · `资源：代码`
  <details>
  <summary>收录依据</summary>
  <p>Watcher 从已观测的病史前缀出发，通过临床事件、时间戳与数值检验结果自回归推进患者时间线；在时间留出的住院记录上评估多日蒙特卡洛轨迹及衍生风险，未开展因果治疗模拟。</p>
  </details>

- (*Comput Biol Med'26*) **Liquid Fourier Latent Dynamics Networks for Fast GPU-Based Numerical Simulations in Computational Cardiology**
  [[📝 论文](https://doi.org/10.1016/j.compbiomed.2025.111355)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41338030/)] [[📝 预印本](https://arxiv.org/abs/2408.09818)] [[💻 代码](https://github.com/StanfordCBCL/LFLDNets)]
  **元数据：** `状态：生理` · `动力学：时间演化` · `能力：模拟` · `资源：代码`
  <details>
  <summary>收录依据</summary>
  <p>LFLDNets 推进紧凑的递归生理状态并重建三维电生理或流场，在留出参数与边界条件下，以数值求解器为参照评估完整心动周期轨迹；期刊论文于 2025 年 12 月在线发表。</p>
  </details>

- (*J Physiol'26*) **An Eikonal Model with Re-Excitability for Fast Simulations in Cardiac Electrophysiology**
  [[📝 论文](https://doi.org/10.1113/JP287281)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42678922/)] [[📝 预印本](https://arxiv.org/abs/2410.22583)]
  **元数据：** `状态：生理` · `动力学：时间演化 + 机制模型 + 动作条件` · `能力：模拟` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>在重复刺激下推进心脏激活、恢复与再次兴奋状态，以单域模型模拟为参照复现心房及心室大折返，而非仅计算单次激活图。</p>
  </details>

- (*Med Image Anal'26 Online*) **Towards Patient-Specific Optimization for Mandibular Reconstruction Planning Based on Predicted Bone-Union Propensity**
  [[📝 论文](https://doi.org/10.1016/j.media.2026.104281)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42700676/)] [[📝 预印本](https://arxiv.org/abs/2605.01084)] [[💻 代码](https://github.com/hamidreza-aftabi/OsteoOpt)]
  **元数据：** `状态：解剖` · `动力学：时间演化 + 机制模型 + 动作条件` · `能力：模拟 + 规划` · `资源：代码`
  <details>
  <summary>收录依据</summary>
  <p>OsteoOpt++ 对候选重建几何进行咀嚼周期内的颌骨力学时间积分，依据模拟的骨端贴合与安全性优化手术截骨及供骨位置；术后一年 CT 比较属于回顾性空间验证，而非骨愈合轨迹预测。</p>
  </details>

- (*arXiv'26*) **A Physiology-Informed Digital Twin Framework for Simulating Liver Health Progression**
  [[📝 论文](https://arxiv.org/abs/2608.14969)]
  **元数据：** `状态：生理` · `动力学：时间演化 + 机制模型` · `能力：模拟` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>hePaTwin 在疾病阶段转移校准下推进耦合的肝脏代谢与胆红素状态，并将模拟生物标志物与纵向测量比较；按阶段校准后的一致性尚不等同于独立验证的仅基于基线的预测或治疗效应估计。</p>
  </details>

- (*Nat Cardiovasc Res'26*) **Accounting for Uncertainty in Computational Models of Ventricular Tachycardia Improves Ablation Guidance**
  [[📝 论文](https://doi.org/10.1038/s44161-026-00856-w)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42601469/)]
  **元数据：** `状态：生理` · `动力学：时间演化 + 机制模型` · `能力：模拟` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>在不同瘢痕重建下，利用反应—程函传播与离子动力学模拟室性心动过速回路和 ECG，与临床记录比较，并将可行回路汇总为 SATHe Map；属于机制模拟器，而非学习到的潜在动力学。</p>
  </details>

- (*arXiv'26*) **Intervention-Aware Clinical World Model for Post-Op Outcome Forecasting in Cardiology**
  [[📝 论文](https://arxiv.org/abs/2608.13518)] [[💻 代码](https://github.com/cys1102/af-blanking-world-model)]
  **元数据：** `状态：解剖` · `动力学：时间演化 + 事件序列 + 动作条件` · `能力：预测` · `资源：代码`
  <details>
  <summary>收录依据</summary>
  <p>在消融、临床事件及经过时间的漂移作用下，递归推进 MRI 衍生的心房潜在状态，在 DECAAF-II 中预测瘢痕范围与复发；输入编辑实验属于关联性敏感性测试，而非因果治疗反事实。</p>
  </details>

- (*arXiv'26*) **S2-HWM: Sparse Event-Structured Hierarchical World Model for Long-Horizon Surgical Robot Manipulation**
  [[📝 论文](https://arxiv.org/abs/2608.13103)]
  **元数据：** `状态：操作／机器人` · `动力学：时间演化 + 事件序列 + 动作条件` · `能力：模拟 + 控制` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>将动作条件下的 DreamerV3 动力学与串联的事件级状态、持续时间和奖励预测结合，通过模型内推演训练分层策略；在 SurRoL 中评估序贯手术移块及人为掉落后的恢复。</p>
  </details>

- (*arXiv'26*) **An Open-Source Framework for Predicting Ultrasound Neuromodulation: Bridging Tissue Elastomechanics and Neuron Firing Dynamics**
  [[📝 论文](https://arxiv.org/abs/2608.06321)]
  **元数据：** `状态：生理` · `动力学：时间演化 + 机制模型 + 动作条件` · `能力：模拟 + 反事实` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>将设定的经颅聚焦超声暴露依次通过声学、弹性、热学、细胞膜及神经元动力学传播，在不同机制与参数下模拟与解剖配准的放电历史。</p>
  </details>

- (*bioRxiv'26*) **A Physics-Inspired Classical Digital Twin of the Cell: A Composite Multi-Clock Port-Hamiltonian Neural Network Learned from Multi-Omic Circadian Data**
  [[📝 论文](https://www.biorxiv.org/content/10.64898/2026.07.11.737972v3)] [[💻 代码](https://github.com/quantum-omics/Classical-Virtual-Omics)]
  **元数据：** `状态：细胞` · `动力学：时间演化 + 机制模型` · `能力：预测 + 模拟` · `资源：代码`
  <details>
  <summary>收录依据</summary>
  <p>学习小鼠肝脏多组学状态之间的端口哈密顿图转移，评估留出昼夜节律片段的推演；逐基因的相位滞后关系尚未得到确定，留出边的恢复接近随机水平，也未验证疾病或干预模拟。</p>
  </details>

- (*bioRxiv'26*) **Parameter-Dependent Effects of Spinal Cord Stimulation on Neural Activation and Evoked Compound Action Potentials**
  [[📝 论文](https://www.biorxiv.org/content/10.64898/2026.08.03.742575v1)]
  **元数据：** `状态：生理` · `动力学：时间演化 + 机制模型 + 动作条件` · `能力：模拟 + 反事实` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>将脊髓有限元场与随时间演化的多分室轴突动力学耦合，在不同刺激与记录参数下重复运行，模拟神经募集及诱发复合动作电位（ECAP）波形。</p>
  </details>

- (*bioRxiv'26*) **A Dynamical Digital Twin Unmasks Hidden Neuromotor Control Policies and Catastrophic Tipping Points in Parkinson's Disease**
  [[📝 论文](https://www.biorxiv.org/content/10.64898/2026.03.09.710685v2)]
  **元数据：** `状态：生理` · `动力学：时间演化 + 机制模型` · `能力：模拟` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>将个体测力台轨迹同化到机制性的间歇控制状态模型中，生成患者层面的随机姿态摇摆轨迹，并模拟与帕金森病相关的吸引子分岔。</p>
  </details>

- (*arXiv'26*) **Optimal Stimulation Sites Are Not the Most Affected: Personalised Models of Resting-State fMRI in Alzheimer's Disease**
  [[📝 论文](https://arxiv.org/abs/2607.24356)] [[💻 代码](https://github.com/cristianocapone/AD-reservoir-FC-stimulation)]
  **元数据：** `状态：生理` · `动力学：时间演化 + 动作条件` · `能力：模拟 + 反事实 + 规划 + 控制` · `资源：代码`
  <details>
  <summary>收录依据</summary>
  <p>拟合受试者特异性的自由演化 fMRI 动力学，对虚拟患者施加候选局部驱动，选择个体化刺激靶点，并验证引入因果信息的实时闭环控制器。</p>
  </details>

- (*Phys Med Biol'26*) **Towards a Clinically Practical Computational Platform for Systematically Adapting Radiation Therapy for Glioma Patients**
  [[📝 论文](https://doi.org/10.1088/1361-6560/ae9687)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42562016/)]
  **元数据：** `状态：患者` · `动力学：时间演化 + 机制模型 + 动作条件` · `能力：模拟 + 反事实 + 规划` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>利用每位患者的纵向 MRI 校准基于生物学的胶质瘤生长模型，虚拟施加标准及增殖靶向剂量分布，推算治疗后肿瘤负荷以支持自适应规划。</p>
  </details>

- (*Ann Biomed Eng'26*) **Developing a Digital Twin of the Cardiopulmonary System in a Mouse: Inferring Hemodynamics from Sparse Measurements**
  [[📝 论文](https://doi.org/10.1007/s10439-026-04107-8)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42550388/)]
  **元数据：** `状态：生理` · `动力学：时间演化 + 机制模型` · `能力：模拟` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>将个体化零维心肺状态模型拟合至小鼠压力—容积数据，对耦合血流动力学积分，以复现完整波形并推断未直接测量的生理量。</p>
  </details>

- (*Bull Math Biol'26*) **Assessing the Role of Model Complexity in Virtual Clinical Trial Outcomes**
  [[📝 论文](https://doi.org/10.1007/s11538-026-01715-2)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42530700/)] [[💻 代码](https://github.com/jgevertz/VCT)]
  **元数据：** `状态：患者` · `动力学：时间演化 + 机制模型 + 动作条件` · `能力：模拟 + 反事实` · `资源：代码`
  <details>
  <summary>收录依据</summary>
  <p>在多种给药方案下，为虚拟小鼠患者运行机制性肿瘤—病毒治疗轨迹，测试模型复杂度与队列构建如何改变试验结局。</p>
  </details>

- (*eLife'26*) **Large-Scale Synthetic Data Enable Digital Twins of Human Excitable Cells**
  [[📝 论文](https://doi.org/10.7554/eLife.110013)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42489674/)] [[💻 代码](https://github.com/ClancyLabUCD/Digital-Twin-for-the-Win-Personalized-Cardiac-Electrophysiology)]
  **元数据：** `状态：细胞` · `动力学：时间演化 + 机制模型 + 动作条件` · `能力：模拟 + 反事实` · `资源：代码`
  <details>
  <summary>收录依据</summary>
  <p>利用合成数据训练的神经网络，根据电压钳轨迹推断固定心脏离子 ODE 模型的参数，再模拟细胞特异性的电生理及 IKr 阻断反应；神经网络学习的是参数推断，而非前向状态转移规律。</p>
  </details>

- (*bioRxiv'26*) **Patient-Specific Heart Rate Modulates Developmental Electrophysiology in Transcriptomic-Guided In Silico Models of Pediatric Human Atrial Cardiomyocytes**
  [[📝 论文](https://www.biorxiv.org/content/10.64898/2026.07.21.739866v1)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42538960/)]
  **元数据：** `状态：细胞` · `动力学：时间演化 + 机制模型 + 动作条件` · `能力：模拟 + 反事实` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>以每位儿童患者的转录组调整心房细胞模型，在其内在心率和反事实固定起搏频率下，将动作电位及钙瞬变推演至稳态。</p>
  </details>

- (*Cell'26*) **Whole-Cell Particle-Based Digital Twin Simulations from 4D Lattice Light-Sheet Microscopy Data**
  [[📝 论文](https://doi.org/10.1016/j.cell.2026.06.010)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42379169/)] [[💻 代码](https://github.com/schoeneberglab/readdy-cell)]
  **元数据：** `状态：细胞` · `动力学：时间演化 + 机制模型 + 空间／视角 + 动作条件` · `能力：模拟 + 反事实` · `资源：代码`
  <details>
  <summary>收录依据</summary>
  <p>根据显微影像初始化粒子状态，通过扩散、融合／分裂及马达运输推进线粒体动态，比较对照与微管扰动行为，并推算应激条件；这些机制模拟尚未建立独立的前瞻性预测任务。</p>
  </details>

- (*Comput Methods Programs Biomed'26*) **Integrating EMT Dynamics in Model-Based Metastasis Prediction**
  [[📝 论文](https://doi.org/10.1016/j.cmpb.2026.109390)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42061167/)]
  **元数据：** `状态：患者` · `动力学：时间演化 + 机制模型 + 动作条件` · `能力：预测 + 模拟` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>将 TGF-beta 与上皮—间质转化（EMT）信号耦合至化疗和放疗下随时间演化的原发及转移肿瘤生长，继而将虚拟患者向前推演至生存结局。</p>
  </details>

- (*Heart Rhythm'26*) **High-Fidelity Postmyocardial Infarction Ventricular Tachycardia Simulation for Intraprocedure Ablation Guidance**
  [[📝 论文](https://doi.org/10.1016/j.hrthm.2026.03.1962)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41956268/)]
  **元数据：** `状态：生理` · `动力学：时间演化 + 机制模型 + 动作条件` · `能力：预测 + 模拟` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>通过 GPU 加速的单域求解器推进起搏后的心肌电生理与 ECG 状态，复现不同消融阶段的室性心动过速可诱发性及形态，并揭示未来可能出现的室速。</p>
  </details>

- (*arXiv'26*) **CrossScope: A Role-Asymmetric World Model for Joint Dual-Scope Surgical Video Prediction**
  [[📝 论文](https://arxiv.org/abs/2608.03211)]
  **元数据：** `状态：操作／机器人` · `动力学：时间演化 + 空间／视角` · `能力：预测 + 模拟` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>从同步的 ERCP 观测与因果历史中，联合预测母镜及子镜各八帧未来画面，在体模和按患者留出的真实手术中评估。</p>
  </details>

- (*MICCAI'26 Workshop*) **Automatic Patient-Specific Microwave Ablation Planning Accelerated by a Physics-Guided Deep Learning Model**
  [[📝 论文](https://arxiv.org/abs/2608.03086)]
  **元数据：** `状态：解剖` · `动力学：机制模型 + 动作条件` · `能力：模拟 + 反事实 + 规划` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>根据患者解剖与治疗动作预测消融后的区域，在优化天线轨迹、功率及持续时间时反复查询该前向模拟器。</p>
  </details>

- (*arXiv'26*) **NeuroWorld: A Latent Brain World Model for Stimulus-Conditioned Human Brain Dynamics**
  [[📝 论文](https://arxiv.org/abs/2608.01773)]
  **元数据：** `状态：生理` · `动力学：时间演化 + 动作条件` · `能力：预测 + 模拟` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>学习具有因果时序约束、以刺激为条件的脑潜在状态转移，自回归推演多个未来时间点的受试者特异性全脑 fMRI 轨迹。</p>
  </details>

- (*arXiv'26*) **EndoWAM: A Grounded World-Action Model for Generalizable Endoscopic Navigation**
  [[📝 论文](https://arxiv.org/abs/2608.01221)]
  **元数据：** `状态：操作／机器人` · `动力学：时间演化` · `能力：预测` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>在内镜状态上训练视频动力学先验与未来目标生成器，通过三类操作中的实体体模闭环导航评估该预测表征。</p>
  </details>

- (*MICCAI'26 Workshop*) **Anticipatory Digital Twins for Online Head-and-Neck Adaptive Proton Therapy via Foundation-Model Registration**
  [[📝 论文](https://arxiv.org/abs/2608.00831)]
  **元数据：** `状态：解剖` · `动力学：时间演化 + 空间／视角` · `能力：预测` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>通过学习到的配准模型迁移纵向解剖变化，在影像采集前预测患者特异性的治疗日 CT 状态与轮廓。</p>
  </details>

- (*arXiv'26*) **A Digital-Twin Framework for Forecasting Treatment-Day Imaging with Contour Uncertainty in Adaptive Proton Radiotherapy**
  [[📝 论文](https://arxiv.org/abs/2609.24725)]
  **元数据：** `状态：解剖` · `动力学：时间演化 + 空间／视角` · `能力：预测` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>将此前的跨患者形变迁移方法扩展为未来 CT 与轮廓状态集合，提供具有方向性的预测不确定性，并与后续治疗 CT 比较；仅依靠形变库得到的轮廓中心未优于计划轮廓。</p>
  </details>

- (*arXiv'26*) **Failure Detection for Surgical Robot Imitation Policies via Flow-Matching World Modeling**
  [[📝 论文](https://arxiv.org/abs/2607.27511)]
  **元数据：** `状态：操作／机器人` · `动力学：时间演化 + 动作条件` · `能力：预测` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>学习以手术机器人动作为条件的正常多步视觉转移，根据预测与实际终点状态的不一致检测失败，在模拟及真实 dVRK 任务中评估。</p>
  </details>

- (*arXiv'26*) **Action-Conditioned World Model for Goal Plane Probe Guidance in Robotic Ultrasound**
  [[📝 论文](https://arxiv.org/abs/2607.21918)]
  **元数据：** `状态：医学影像` · `动力学：空间／视角 + 动作条件` · `能力：预测 + 模拟 + 控制` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>在候选六自由度探头运动下预测未来超声状态，将冻结的模型作为策略学习的内部模拟器，并验证颈动脉与甲状腺闭环引导。</p>
  </details>

- (*arXiv'26*) **A Diffusion-Model Subpopulation Digital Twin for Mobile Health Deployment: A Case Study on the HeartSteps Intervention**
  [[📝 论文](https://arxiv.org/abs/2607.21403)]
  **元数据：** `状态：群体` · `动力学：时间演化 + 动作条件` · `能力：模拟` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>利用因果时间核与保留既有前缀的扩散更新，在序贯移动健康动作下生成逐小时行为轨迹；评估了已观测动作下的轨迹保真度，尚未证明新策略的因果效应或临床获益。</p>
  </details>

- (*arXiv'26*) **PIONEER: Bayesian Joint Modelling of Mechanistic Tumour Growth and Time-to-Event Endpoints for Dynamic Prediction of Ongoing Oncology Trials**
  [[📝 论文](https://arxiv.org/abs/2607.17908)]
  **元数据：** `状态：患者` · `动力学：时间演化 + 机制模型` · `能力：预测 + 模拟` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>联合推断潜在肿瘤生长与临床事件动力学，根据中期数据向前模拟患者轨迹及成熟试验终点。</p>
  </details>

- (*arXiv'26*) **Enhancing Personalized Bladder Cancer Treatment Through Reinforcement Learning: A Recurrent Patient State Transition Decision Support Framework**
  [[📝 论文](https://arxiv.org/abs/2607.16916)]
  **元数据：** `状态：患者` · `动力学：时间演化 + 动作条件` · `能力：模拟 + 规划 + 控制` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>根据历史观测学习治疗条件下的递归膀胱癌状态转移，利用递归模拟轨迹进行 DQN 规划；验证仅限于所学习的模拟器内部。</p>
  </details>

- (*arXiv'26*) **Differentiable Cardiac Electrophysiology Simulations for Dynamical State and Parameter Estimation**
  [[📝 论文](https://arxiv.org/abs/2607.15492)]
  **元数据：** `状态：生理` · `动力学：时间演化 + 机制模型` · `能力：预测 + 模拟` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>将可微电生理偏微分方程模拟器拟合至部分心脏测量，并向前推演恢复出的动作电位动力学。</p>
  </details>

- (*arXiv'26*) **AI-Augmented Adaptive Digital Twin Modeling for Brain Tumor Evolution Prediction and Treatment Scheduling**
  [[📝 论文](https://arxiv.org/abs/2607.13877)]
  **元数据：** `状态：患者` · `动力学：时间演化 + 机制模型 + 动作条件` · `能力：预测 + 模拟 + 规划 + 控制` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>结合治疗条件下的肿瘤动力学、患者特异性在线更新、120 步递归推演与模型预测控制（MPC）排程；评估仅限于基于患者数据构建的合成轨迹。</p>
  </details>

- (*MICCAI'26*) **HemoPIC: A Physics-Informed Cerebral Hemodynamics Digital Twin for Brain Perfusion**
  [[📝 论文](https://arxiv.org/abs/2607.08799)] [[💻 代码](https://github.com/jhuldr/HemoPIC)]
  **元数据：** `状态：生理` · `动力学：时间演化 + 机制模型` · `能力：模拟` · `资源：代码`
  <details>
  <summary>收录依据</summary>
  <p>拟合固定 Windkessel 与示踪剂分室方程的参数，模拟随时间变化的造影剂通过过程并生成脑灌注图；已评估实验尚未建立学习到的状态转移规律或血管干预反事实。</p>
  </details>

- (*arXiv'26*) **EHR-MPC: Inference-Time Control for Sepsis Treatment with Generative Patient Digital Twins**
  [[📝 论文](https://arxiv.org/abs/2607.08793)]
  **元数据：** `状态：患者` · `动力学：时间演化 + 动作条件` · `能力：模拟 + 规划 + 控制` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>在候选治疗标记条件下递归生成未来临床状态，将这些轨迹用于脓毒症 MPC；回顾性离策略估计与学习到的模拟器内部结局，尚不能证明前瞻性治疗疗效。</p>
  </details>

- (*arXiv'26*) **Sectorial Customized Corneal Crosslinking for Keratoconus: An Inverse Biomechanical Design Study with an Anisotropic Reduced Shell Finite-Element Surrogate**
  [[📝 论文](https://arxiv.org/abs/2607.06385)]
  **元数据：** `状态：解剖` · `动力学：机制模型 + 动作条件` · `能力：模拟 + 反事实 + 规划` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>在不同空间交联动作下模拟治疗后的角膜形变，针对生物力学与光学目标优化干预区域掩膜。</p>
  </details>

- (*medRxiv'26*) **Personalized Planning of Cardiac Resynchronization Therapy Through Integration of Coronary Sinus Geometry, Clinical Data, Digital Twins, and Machine Learning: Visualization, Stratification, and Optimization**
  [[📝 论文](https://www.medrxiv.org/content/10.64898/2026.07.01.26356827v1)]
  **元数据：** `状态：生理` · `动力学：时间演化 + 机制模型 + 动作条件` · `能力：模拟 + 反事实 + 规划` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>模拟不同 CRT 起搏位点下的心室激活，利用独立的反应分类器辅助位点规划；虚拟位点上更好的预测反应，尚不等于植入该位置后的实际临床获益。</p>
  </details>

- (*Stem Cell Reports'26*) **In Silico Optimization of Regenerative Cell Therapy in the Infarcted Human Ventricles to Mitigate Arrhythmic Burden**
  [[📝 论文](https://doi.org/10.1016/j.stemcr.2026.103007)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42425090/)]
  **元数据：** `状态：生理` · `动力学：时间演化 + 机制模型 + 动作条件` · `能力：模拟 + 反事实` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>模拟再生细胞治疗前后患者特异性的心室电生理，评估随时间变化的干预结果。</p>
  </details>

- (*arXiv'26*) **Personalized 4D Whole-Heart Mesh Reconstruction from Cine MRI via Multi-Scale Temporal Modeling and Differentiable Contour Rendering**
  [[📝 论文](https://arxiv.org/abs/2607.01952)]
  **元数据：** `状态：解剖` · `动力学：时间演化` · `能力：预测 + 模拟` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>将患者特异性的三维心脏几何表示为贯穿心动周期的连续轨迹，进行重建与预测。</p>
  </details>

- (*Med Image Anal'26*) **Electrophysiologically-Informed Digital Twins for Atrial Fibrillation**
  [[📝 论文](https://doi.org/10.1016/j.media.2026.104131)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42172939/)]
  **元数据：** `状态：生理` · `动力学：时间演化 + 机制模型` · `能力：模拟` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>校准患者特异性的心房电生理并模拟房颤波动，将相位奇点图与回顾性消融位置比较；尚未展示经过评估的虚拟消融策略或治疗计划优化器。</p>
  </details>

- (*J Physiol'26*) **Prospective In Silico Trials Identify Combined SK and K2P Channel Block as an Effective Strategy for Atrial Fibrillation Cardioversion**
  [[📝 论文](https://doi.org/10.1113/JP287124)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/39557619/)]
  **元数据：** `状态：生理` · `动力学：机制模型 + 动作条件` · `能力：模拟 + 反事实` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>在不同离子通道干预下推演多尺度心房电生理，以预测心律复律结局。</p>
  </details>

- (*Phys Med Biol'26*) **A Digital Twin Framework for Adaptive Treatment Planning in Radiotherapy**
  [[📝 论文](https://doi.org/10.1088/1361-6560/ae835a)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42361838/)]
  **元数据：** `状态：解剖` · `动力学：时间演化 + 空间／视角` · `能力：预测 + 规划` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>通过迁移影像配准形变，预测合理的治疗日解剖并构建自适应放疗计划；回顾性选择与重新优化使用当日锥形束 CT（CBCT），未建立肿瘤生物学反应或放射治疗动作的状态转移模型。</p>
  </details>

- (*arXiv'26*) **Neural Operator-Based Digital Twins for Modeling Amyloid-Beta and Tau Propagation and Treatment Optimization in Alzheimer's Disease**
  [[📝 论文](https://arxiv.org/abs/2606.25185)]
  **元数据：** `状态：生理` · `动力学：时间演化 + 机制模型 + 动作条件` · `能力：模拟 + 反事实 + 规划` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>学习空间淀粉样蛋白／tau 的反应—扩散动力学，通过最优控制推算不同治疗安排；生物标志物轨迹评估尚未验证这些假设性控制对应的临床治疗反应。</p>
  </details>

- (*arXiv'26*) **OphthaDT: Generative Digital Twins for Forecasting Visual Acuity Trajectories in Ophthalmology**
  [[📝 论文](https://arxiv.org/abs/2606.22101)]
  **元数据：** `状态：患者` · `动力学：时间演化` · `能力：预测` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>根据序列化的患者病史生成多个时间跨度的视力预测，在四个临床试验数据集的留出患者上评估；尚未展示治疗条件下的因果模拟或规划。</p>
  </details>

- (*arXiv'26*) **SurgVista: Long-Horizon Surgical World Modeling with Plausible Instrument-Tissue Dynamics**
  [[📝 论文](https://arxiv.org/abs/2606.19889)]
  **元数据：** `状态：操作／机器人` · `动力学：时间演化 + 动作条件` · `能力：预测 + 模拟` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>在动作条件下预测长时程手术视频状态，同时建模器械与组织的相互作用。</p>
  </details>

- (*arXiv'26*) **DreamReg: Belief-Driven World Model for 2D-3D Ultrasound Registration**
  [[📝 论文](https://arxiv.org/abs/2606.18825)]
  **元数据：** `状态：医学影像` · `动力学：空间／视角 + 动作条件` · `能力：模拟 + 规划` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>学习以探头运动为条件的潜在动力学，通过想象未来观测进行配准规划。</p>
  </details>

- (*Biomed Phys Eng Express'26*) **Physics-Informed Koopman-Constrained ImplicitQ-Learning for Safe Offline Reinforcement Learning in Mechanical Ventilation**
  [[📝 论文](https://doi.org/10.1088/2057-1976/ae7d30)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42296990/)]
  **元数据：** `状态：生理` · `动力学：机制模型 + 动作条件` · `能力：模拟 + 控制` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>学习 Koopman 呼吸状态动力学，利用预测的呼吸机动作后果引导离线策略学习。</p>
  </details>

- (*arXiv'26*) **Learning Cardiac Electrophysiology Digital Twins Through Agentic Discovery of Hybrid Structure**
  [[📝 论文](https://arxiv.org/abs/2606.18154)]
  **元数据：** `状态：生理` · `动力学：时间演化 + 机制模型` · `能力：模拟` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>发现用于心脏电生理推演的反应方程与神经扩散结构，在合成模型和动物电图上评估；尚未建立面向人类患者的个体化临床部署证据。</p>
  </details>

- (*arXiv'26*) **Treatment Response Optimized Clinical Decision Support AI System via Digital Twin Simulation**
  [[📝 论文](https://arxiv.org/abs/2606.17405)]
  **元数据：** `状态：患者` · `动力学：时间演化 + 动作条件` · `能力：模拟 + 规划` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>学习显式的残差下一状态更新，进行治疗条件下的多步推演，并评估离线决策策略；使用模型内部奖励的合成及回顾性实验，尚不能证明因果性的临床治疗获益。</p>
  </details>

- (*Comput Biol Med'26*) **Causal Counterfactual Simulation for Treatment Decisions in Multimodal Lung Disease Data**
  [[📝 论文](https://doi.org/10.1016/j.compbiomed.2026.111807)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42275812/)]
  **元数据：** `状态：患者` · `动力学：时间演化 + 动作条件` · `能力：模拟 + 反事实` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>建模纵向肺部状态转移，结合影像与临床数据生成治疗反事实。</p>
  </details>

- (*arXiv'26*) **Transition-Based Digital Twin Modelling for Alzheimer's Disease under Sparse Longitudinal Data**
  [[📝 论文](https://arxiv.org/abs/2606.09671)]
  **元数据：** `状态：患者` · `动力学：时间演化` · `能力：预测` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>学习相邻随访间的 MMSE 与诊断预测，并评估更长时程预测；修改 FAQ 和海马体积的假设分析属于协变量敏感性分析，而非已识别的治疗反事实。</p>
  </details>

- (*bioRxiv'26*) **U-Pert: Unbalanced Perturbation Dynamics For Cell Fate Design**
  [[📝 论文](https://www.biorxiv.org/content/10.64898/2026.06.30.735555v1)]
  **元数据：** `状态：细胞` · `动力学：时间演化 + 动作条件` · `能力：模拟 + 规划` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>学习同时涉及细胞状态与数量、具有上下文感知能力的扰动动力学，用于前向模拟与逆向干预设计。</p>
  </details>

- (*arXiv'26*) **Chreode: A Cell World Model for One-Step Temporal Dynamics and Perturbation Prediction**
  [[📝 论文](https://arxiv.org/abs/2605.28111)] [[💻 代码](https://github.com/mufanq/Chreode)] [[🌐 权重](https://huggingface.co/MufanQiu/chreode-pretrained)]
  **元数据：** `状态：细胞` · `动力学：时间演化 + 动作条件` · `能力：预测 + 模拟` · `资源：代码 + 权重`
  <details>
  <summary>收录依据</summary>
  <p>预测不同时间及扰动下的细胞状态转移，而非仅嵌入静态转录组。</p>
  </details>

- (*IEEE JBHI'26*) **TwinRL-Onco: A World Model-Empowered Digital Twin Framework with Hierarchical Reinforcement Learning for Venetoclax Resistance Trajectory Prediction and Adaptive Therapy Optimization in Chronic Lymphocytic Leukemia**
  [[📝 论文](https://doi.org/10.1109/JBHI.2026.3696685)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42184194/)]
  **元数据：** `状态：患者` · `动力学：时间演化 + 动作条件` · `能力：预测 + 模拟 + 规划` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>原始摘要报告了递归状态空间动力学、耐药轨迹的蒙特卡洛模拟与分层治疗优化；0.917 的 AUROC 针对模拟的 12 个月疾病进展，本轮核查尚未验证完整方法与临床预测有效性。</p>
  </details>

- (*arXiv'26*) **ChronoMedicalWorld: A Medical World Model for Learning Patient Trajectories from Longitudinal Care Data**
  [[📝 论文](https://arxiv.org/abs/2605.21963)]
  **元数据：** `状态：患者` · `动力学：时间演化 + 事件序列 + 动作条件` · `能力：预测 + 模拟` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>在纵向诊疗轨迹中，根据临床动作递归向前推演患者状态。</p>
  </details>

- (*arXiv'26*) **ECG-WM: A Physiology-Informed ECG World Model for Clinical Intervention Simulation**
  [[📝 论文](https://arxiv.org/abs/2605.17580)] [[🌐 项目](https://chenzk202212.github.io/ECG_World_Model/)]
  **元数据：** `状态：生理` · `动力学：时间演化 + 动作条件` · `能力：预测 + 反事实` · `资源：项目`
  <details>
  <summary>收录依据</summary>
  <p>根据干预前的生理状态与治疗背景，预测干预后的 ECG 轨迹。</p>
  </details>

- (*arXiv'26*) **GazeWorld: A World Model of Radiologist Reading for Medical Image Representation Learning**
  [[📝 论文](https://arxiv.org/abs/2605.23992)]
  **元数据：** `状态：诊疗流程` · `动力学：时间演化 + 事件序列` · `能力：预测 + 模拟` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>自回归建模放射科医生注视点序列的演化，将其作为诊断交互轨迹。</p>
  </details>

- (*arXiv'26*) **SWoMo: Neuro-Symbolic World Model for Cataract Surgery Simulation**
  [[📝 论文](https://arxiv.org/abs/2605.16530)] [[🌐 项目](https://ssharvienkumar.github.io/SWoMo/)]
  **元数据：** `状态：操作／机器人` · `动力学：时间演化 + 动作条件` · `能力：模拟` · `资源：项目`
  <details>
  <summary>收录依据</summary>
  <p>根据符号化手术动作模拟器械—组织状态变化，并渲染对应的视觉结果。</p>
  </details>

- (*arXiv'26*) **Toward World Modeling of Physiological Signals with Chaos-Theoretic Balancing and Latent Dynamics (NormWear-2)**
  [[📝 论文](https://arxiv.org/abs/2605.15465)]
  **元数据：** `状态：生理` · `动力学：时间演化 + 动作条件` · `能力：预测 + 模拟` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>学习多变量生理信号的潜在动力学，在干预背景下向前推演。</p>
  </details>

- (*arXiv'26*) **Agentifying Patient Dynamics within LLMs through Interacting with Clinical World Model**
  [[📝 论文](https://arxiv.org/abs/2605.14723)] [[💻 代码](https://github.com/FreedomIntelligence/SepsisAgent)]
  **元数据：** `状态：患者` · `动力学：时间演化 + 动作条件` · `能力：模拟 + 规划` · `资源：代码`
  <details>
  <summary>收录依据</summary>
  <p>提供可交互的脓毒症世界模型，为大语言模型决策智能体模拟候选治疗的影响。</p>
  </details>

- (*arXiv'26*) **MolWorld: Molecule World Models for Actionable Molecular Optimization**
  [[📝 论文](https://arxiv.org/abs/2605.08954)]
  **元数据：** `状态：分子` · `动力学：事件序列 + 动作条件` · `能力：模拟 + 规划` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>将分子优化建模为连续的局部状态变换，规划可执行的分子编辑轨迹。</p>
  </details>

- (*arXiv'26*) **Simulating Clinical Interventions with a Generative Multimodal Model of Human Physiology (HealthFormer)**
  [[📝 论文](https://arxiv.org/abs/2604.27899)]
  **元数据：** `状态：生理` · `动力学：时间演化 + 动作条件` · `能力：预测 + 反事实` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>生成多模态生理轨迹，模拟临床干预如何改变未来患者状态。</p>
  </details>

- (*arXiv'26*) **Beyond Patient Invariance: Learning Cardiac Dynamics via Action-Conditioned JEPAs**
  [[📝 论文](https://arxiv.org/abs/2604.22618)] [[💻 代码](https://github.com/cljosegfer/lesaude-dynamics)]
  **元数据：** `状态：生理` · `动力学：时间演化 + 动作条件` · `能力：预测 + 模拟` · `资源：代码`
  <details>
  <summary>收录依据</summary>
  <p>在疾病发生动作条件下，于潜在空间预测未来心脏电生理状态。</p>
  </details>

- (*arXiv'26*) **Toward Safe Autonomous Robotic Endovascular Interventions using World Models**
  [[📝 论文](https://arxiv.org/abs/2604.20151)]
  **元数据：** `状态：操作／机器人` · `动力学：时间演化 + 动作条件` · `能力：规划 + 控制` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>学习血管内介入环境的动力学，利用模型内推演进行 TD-MPC2 导管控制。</p>
  </details>

- (*arXiv'26*) **Sonata: A Hybrid World Model for Inertial Kinematics under Clinical Data Scarcity**
  [[📝 论文](https://arxiv.org/abs/2604.18058)]
  **元数据：** `状态：生理` · `动力学：时间演化 + 机制模型` · `能力：预测` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>结合学习到的动力学与生物力学，预测临床测量的未来惯性运动学状态。</p>
  </details>

- (*arXiv'26*) **Open-H-Embodiment: A Large-Scale Dataset for Enabling Foundation Models in Medical Robotics**
  [[📝 论文](https://arxiv.org/abs/2604.21017)] [[💻 代码](https://huggingface.co/nvidia/Cosmos-H-Surgical-Simulator)] [[💻 代码](https://github.com/NVIDIA-Medtech/Cosmos-H-Surgical-Simulator)] [[🌐 项目](https://open-h.github.io/open-h-embodiment/)]
  **元数据：** `状态：操作／机器人` · `动力学：时间演化 + 动作条件` · `能力：模拟` · `资源：代码 + 项目`
  <details>
  <summary>收录依据</summary>
  <p>除发布数据外，还训练动作条件下的手术模拟器，以预测多种具身平台上的操作轨迹。</p>
  </details>

- (*arXiv'26*) **Lingshu-Cell: A Generative Cellular World Model for Transcriptome Modeling Toward Virtual Cells**
  [[📝 论文](https://arxiv.org/abs/2603.25240)]
  **元数据：** `状态：细胞` · `动力学：动作条件` · `能力：模拟 + 反事实` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>生成以扰动为条件的未来细胞转录组状态分布。</p>
  </details>

- (*arXiv'26*) **EyeWorld: A Generative World Model of Ocular State and Dynamics**
  [[📝 论文](https://arxiv.org/abs/2603.14039)]
  **元数据：** `状态：解剖` · `动力学：时间演化` · `能力：预测 + 模拟` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>学习以时间为条件的眼部状态转移，用于纵向疾病进展模拟。</p>
  </details>

- (*arXiv'26*) **SAW: Toward a Surgical Action World Model via Controllable and Scalable Video Generation**
  [[📝 论文](https://arxiv.org/abs/2603.13024)]
  **元数据：** `状态：操作／机器人` · `动力学：时间演化 + 动作条件` · `能力：模拟` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>根据器械轨迹与操作动作，生成未来手术状态。</p>
  </details>

- (*ICLR'26 Rejected*) **Unified Surgical World Model for Structured Understanding, Long-Horizon Prediction, and Fine-Grained Generation**
  [[📝 论文](https://openreview.net/forum?id=Kk9t5empEf)]
  **元数据：** `状态：操作／机器人` · `动力学：时间演化 + 动作条件` · `能力：预测 + 模拟` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>学习考虑动作的手术状态转移，用于长时程轨迹预测与可控场景演化。</p>
  </details>

- (*MIDL'26 rejected*) **Learning Action-Conditioned World Models for Cataract Surgery from Unlabeled Videos (SurgWorld)**
  [[📝 论文](https://openreview.net/forum?id=aYQYOVm2AB)]
  **元数据：** `状态：操作／机器人` · `动力学：时间演化 + 动作条件` · `能力：预测` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>在推断出的原子动作标记条件下，预测白内障手术潜在状态转移。</p>
  </details>

- (*CVPR'26*) **X-WIN: Building Chest Radiograph World Model via Predictive Sensing**
  [[📝 论文](https://arxiv.org/abs/2511.14918)]
  **元数据：** `状态：医学影像` · `动力学：空间／视角 + 动作条件` · `能力：预测 + 模拟` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>预测放射影像观测在显式三维视角与感知变换下如何变化。</p>
  </details>

- (*arXiv'26*) **Brain-WM: Brain Glioblastoma World Model**
  [[📝 论文](https://arxiv.org/abs/2603.07562)] [[💻 代码](https://github.com/thibault-wch/Brain-GBM-world-model)]
  **元数据：** `状态：患者` · `动力学：时间演化 + 动作条件` · `能力：预测 + 模拟 + 反事实` · `资源：代码`
  <details>
  <summary>收录依据</summary>
  <p>模拟肿瘤与治疗的耦合演化，在不同治疗情景下生成未来 MRI 状态。</p>
  </details>

- (*bioRxiv'26*) **Towards building a World Model to simulate perturbation-induced cellular dynamics by AlphaCell**
  [[📝 论文](https://www.biorxiv.org/content/10.64898/2026.03.02.709176v1)]
  **元数据：** `状态：细胞` · `动力学：时间演化 + 动作条件` · `能力：预测 + 模拟` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>从大规模扰动数据学习连续细胞状态动力学，模拟未见过的反应。</p>
  </details>

- (*CVPR'26*) **MRI Contrast Enhancement Kinetics World Model**
  [[📝 论文](https://arxiv.org/abs/2602.19285)] [[💻 代码](https://github.com/DD0922/MRI-Contrast-Enhancement-Kinetics-World-Model)]
  **元数据：** `状态：医学影像` · `动力学：时间演化 + 机制模型` · `能力：预测 + 模拟` · `资源：代码`
  <details>
  <summary>收录依据</summary>
  <p>建模连续的造影剂动力学，在任意增强时间点合成 MRI 状态。</p>
  </details>

- (*medRxiv'26*) **MedOS: AI-XR-Cobot World Model for Clinical Perception and Action**
  [[📝 论文](https://www.medrxiv.org/content/10.64898/2026.02.18.26345936v1)]
  **元数据：** `状态：操作／机器人` · `动力学：机制模型 + 动作条件` · `能力：模拟 + 规划` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>利用考虑物理规律的操作模拟器，预测医疗具身任务中的不良事件与动作后果。</p>
  </details>

- (*arXiv'26*) **EHRWorld: A Patient-Centric Medical World Model for Long-Horizon Clinical Trajectories**
  [[📝 论文](https://arxiv.org/abs/2602.03569)]
  **元数据：** `状态：患者` · `动力学：时间演化 + 事件序列 + 动作条件` · `能力：预测 + 模拟` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>在序贯临床干预下，自回归模拟长时程患者轨迹。</p>
  </details>

- (*AI Medicine'26*) **World Model Enhanced Offline Reinforcement Learning for Sequential Intervention Optimization in Acute Kidney Injury**
  [[📝 论文](https://www.sciltp.com/journals/aim/articles/2602002965)]
  **元数据：** `状态：患者` · `动力学：时间演化 + 动作条件` · `能力：模拟 + 规划 + 控制` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>学习急性肾损伤（AKI）患者的状态动力学，利用模型生成的转移离线优化序贯干预。</p>
  </details>

- (*arXiv'26*) **The Patient is not a Moving Document: A World Model Training Paradigm for Longitudinal EHR**
  [[📝 论文](https://arxiv.org/abs/2601.22128)]
  **元数据：** `状态：患者` · `动力学：时间演化 + 事件序列` · `能力：预测 + 模拟` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>根据纵向临床病史，在潜在空间与标记空间中预测未来患者状态。</p>
  </details>

- (*arXiv'26*) **Generating Counterfactual Patient Timelines from Real-World Data**
  [[📝 论文](https://arxiv.org/abs/2604.02337)]
  **元数据：** `状态：患者` · `动力学：时间演化 + 事件序列 + 动作条件` · `能力：模拟 + 反事实` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>在指定治疗选择下，自回归生成不同的患者事件时间线。</p>
  </details>

- (*arXiv'26*) **Policy4OOD: A Knowledge-Guided World Model for Policy Intervention Simulation against the Opioid Overdose Crisis**
  [[📝 论文](https://arxiv.org/abs/2602.12373)]
  **元数据：** `状态：群体` · `动力学：时间演化 + 动作条件` · `能力：模拟 + 规划` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>在政策动作下模拟药物过量的时空动态，利用模型推演搜索干预计划。</p>
  </details>

- (*arXiv'26*) **BLINK: Behavioral Latent Modeling of NK Cell Cytotoxicity**
  [[📝 论文](https://arxiv.org/abs/2603.05110)]
  **元数据：** `状态：细胞` · `动力学：时间演化` · `能力：预测 + 模拟` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>递归建模自然杀伤（NK）细胞与肿瘤之间随时间演化的潜在交互动力学。</p>
  </details>

- (*arXiv'26*) **RAVEN: Scaling Recurrence-Aware Foundation Models for Clinical Records via Next-Visit Prediction**
  [[📝 论文](https://arxiv.org/abs/2603.24562)]
  **元数据：** `状态：患者` · `动力学：时间演化 + 事件序列` · `能力：预测 + 模拟` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>递归生成下一次就诊的临床事件，将纵向患者记录向前推进。</p>
  </details>

### 2025

- (*J Neuroeng Rehabil'25*) **Towards AI-Based Precision Rehabilitation via Contextual Model-Based Reinforcement Learning**
  [[📝 论文](https://doi.org/10.1186/s12984-025-01771-0)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41419889/)]
  **元数据：** `状态：患者` · `动力学：时间演化 + 动作条件` · `能力：模拟 + 规划` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>PSCRL 更新患者运动恢复的贝叶斯模型，在有约束的序贯规划中使用剂量相关状态转移；个体化康复实验涉及 150 名合成患者，并非临床治疗试验。</p>
  </details>

- (*Sci Adv'25*) **Multiscale Mathematical Model-Informed Reinforcement Learning Optimizes Combination Treatment Scheduling in Glioblastoma Evolution**
  [[📝 论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC13155510/)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/40779623/)] [[💻 代码](https://github.com/SunXQlab/M4RL)]
  **元数据：** `状态：细胞` · `动力学：时间演化 + 机制模型 + 动作条件` · `能力：模拟 + 规划 + 控制` · `资源：代码`
  <details>
  <summary>收录依据</summary>
  <p>M4RL 将实验数据支持的肿瘤微环境智能体模型与物理知情动力学代理耦合，利用模拟的 CSF1R／IGF1R 治疗反应优化联合给药安排；所预测的方案获益为计算结果，而非临床试验结果。</p>
  </details>

- (*Nat Mach Intell'25*) **Model-Based Reinforcement Learning for Ultrasound-Driven Autonomous Microrobots**
  [[📝 论文](https://doi.org/10.1038/s42256-025-01054-2)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/40709099/)] [[💻 代码](https://github.com/M-Medany/Model-Based-Reinforcement-Learning-for-Ultrasound-Driven-Autonomous-Microrobots)]
  **元数据：** `状态：操作／机器人` · `动力学：时间演化 + 动作条件` · `能力：模拟 + 控制` · `资源：代码`
  <details>
  <summary>收录依据</summary>
  <p>为超声驱动的微型机器人学习基于影像的递归动力学，在想象轨迹中训练控制策略；实体导航评估使用静止及流动条件下的人工血管通道，尚非活体给药。</p>
  </details>

- (*npj Digit Med'25*) **Digital Twin Brain Simulator for Real-Time Consciousness Monitoring and Virtual Intervention Using Primate Electrocorticogram Data**
  [[📝 论文](https://doi.org/10.1038/s41746-025-01444-1)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/39929926/)]
  **元数据：** `状态：生理` · `动力学：时间演化` · `能力：预测 + 模拟` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>从清醒及麻醉灵长类动物中学习分层变分递归 ECoG 动力学，在潜在状态扰动后生成未来信号与自由演化轨迹；潜在状态操控并非经过校准的麻醉药剂量干预模型。</p>
  </details>

- (*arXiv'25*) **Cosmos-H-Surgical: Learning Surgical Robot Policies from Videos via World Modeling**
  [[📝 论文](https://arxiv.org/abs/2512.23162)] [[💻 代码](https://huggingface.co/nvidia/Cosmos-H-Surgical-Simulator)] [[💻 代码](https://github.com/nvidia-cosmos/cosmos-cookbook)]
  **元数据：** `状态：操作／机器人` · `动力学：时间演化 + 动作条件` · `能力：模拟 + 控制` · `资源：代码`
  <details>
  <summary>收录依据</summary>
  <p>生成动作条件下的手术视频轨迹，并用其学习机器人策略。</p>
  </details>

- (*arXiv'25*) **VCWorld: A Biological World Model for Virtual Cell Simulation**
  [[📝 论文](https://arxiv.org/abs/2512.00306)]
  **元数据：** `状态：细胞` · `动力学：时间演化 + 动作条件` · `能力：模拟 + 反事实` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>以逐步细胞状态转移复现扰动诱导的信号级联。</p>
  </details>

- (*arXiv'25*) **Evolving Diagnostic Agents in a Virtual Clinical Environment**
  [[📝 论文](https://arxiv.org/abs/2510.24654)]
  **元数据：** `状态：诊疗流程` · `动力学：事件序列 + 动作条件` · `能力：模拟 + 规划 + 控制` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>实现可交互的虚拟患者环境，利用演化的观测支持闭环诊断策略学习。</p>
  </details>

- (*arXiv'25*) **Cosmos-Surg-dVRK: World Foundation Model-based Automated Online Evaluation of Surgical Robot Policy Learning**
  [[📝 论文](https://arxiv.org/abs/2510.16240)]
  **元数据：** `状态：操作／机器人` · `动力学：时间演化 + 动作条件` · `能力：模拟 + 控制` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>模拟动作条件下的手术机器人轨迹，用于在线策略评估。</p>
  </details>

- (*bioRxiv'25*) **Virtual Clinical Trials of BMP4 Differentiation Therapy: Digital Twins to Aid Successful Glioblastoma Trial Design**
  [[📝 论文](https://doi.org/10.1101/2024.08.22.609156)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41279885/)] [[💻 代码](https://github.com/Harbour-N/Virtual-Clinical-Trials-of-BMP4-Differentiation-Therapy)]
  **元数据：** `状态：细胞` · `动力学：时间演化 + 机制模型 + 动作条件` · `能力：模拟 + 反事实 + 规划` · `资源：代码`
  <details>
  <summary>收录依据</summary>
  <p>将机制性的胶质母细胞瘤细胞分室与 BMP4 暴露方程拟合至细胞系数据，再模拟治疗安排及虚拟试验队列；预测疗效与试验效能属于模型输出，而非临床验证。</p>
  </details>

- (*NPJ Digit Med'25*) **Large Language Models Forecast Patient Health Trajectories Enabling Digital Twins**
  [[📝 论文](https://doi.org/10.1038/s41746-025-02004-3)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41034564/)] [[💻 代码](https://github.com/MendenLab/DT-GPT)]
  **元数据：** `状态：患者` · `动力学：时间演化` · `能力：预测` · `资源：代码`
  <details>
  <summary>收录依据</summary>
  <p>根据序列化的患者病史，在肺癌、ICU 及阿尔茨海默病数据集中生成指定的未来检验与临床测量轨迹；这些观察性预测尚未展示通用临床事件模拟器或治疗条件下的轨迹推演。</p>
  </details>

- (*MICCAI'25*) **World Model for AI Autonomous Navigation in Mechanical Thrombectomy**
  [[📝 论文](https://arxiv.org/abs/2509.25518)]
  **元数据：** `状态：操作／机器人` · `动力学：时间演化 + 动作条件` · `能力：规划 + 控制` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>学习血管内环境的状态转移动力学，通过想象轨迹规划取栓导航。</p>
  </details>

- (*arXiv'25*) **medDreamer: Model-Based Reinforcement Learning with Latent Imagination on Complex EHRs for Clinical Decision Support**
  [[📝 论文](https://arxiv.org/abs/2505.19785)]
  **元数据：** `状态：患者` · `动力学：时间演化 + 事件序列 + 动作条件` · `能力：模拟 + 规划 + 控制` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>学习患者潜在动力学，在想象的电子健康记录轨迹中训练治疗策略。</p>
  </details>

- (*arXiv'25*) **Generative Medical Event Models Improve with Scale (CoMET)**
  [[📝 论文](https://arxiv.org/abs/2508.12104)]
  **元数据：** `状态：患者` · `动力学：时间演化 + 事件序列` · `能力：预测 + 模拟` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>自回归生成连续医疗事件，以模拟纵向患者轨迹。</p>
  </details>

- (*arXiv'25*) **Visuomotor Grasping with World Models for Surgical Robots**
  [[📝 论文](https://arxiv.org/abs/2508.11200)]
  **元数据：** `状态：操作／机器人` · `动力学：时间演化 + 动作条件` · `能力：预测 + 控制` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>学习动作条件下的手术抓取动力学，用于基于模型的视觉运动控制。</p>
  </details>

- (*arXiv'25*) **Xray2Xray: World Model from Chest X-rays with Volumetric Context**
  [[📝 论文](https://arxiv.org/abs/2506.19055)]
  **元数据：** `状态：医学影像` · `动力学：空间／视角 + 动作条件` · `能力：预测 + 模拟` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>利用推断出的患者三维体积状态，预测视角变化下的放射影像状态转移。</p>
  </details>

- (*ICCV'25*) **Medical World Model: Generative Simulation of Tumor Evolution for Treatment Planning**
  [[📝 论文](https://arxiv.org/abs/2506.02327)] [[💻 代码](https://github.com/scott-yjyang/MeWM)] [[🌐 项目](https://yijun-yang.github.io/MeWM/)]
  **元数据：** `状态：患者` · `动力学：时间演化 + 动作条件` · `能力：预测 + 模拟 + 规划` · `资源：代码 + 项目`
  <details>
  <summary>收录依据</summary>
  <p>生成治疗条件下的肿瘤演化轨迹，用于反事实规划。</p>
  </details>

- (*CVPR'25*) **EchoWorld: Learning Motion-Aware World Models for Echocardiography Probe Guidance**
  [[📝 论文](https://arxiv.org/abs/2504.13065)]
  **元数据：** `状态：医学影像` · `动力学：空间／视角 + 动作条件` · `能力：预测 + 控制` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>预测探头运动下的超声心动图观测，用于闭环引导。</p>
  </details>

- (*arXiv'25*) **Towards Suturing World Models: Learning Predictive Models for Robotic Surgical Tasks**
  [[📝 论文](https://arxiv.org/abs/2503.12531)] [[🌐 项目](https://mkturkcan.github.io/suturingmodels/)]
  **元数据：** `状态：操作／机器人` · `动力学：时间演化 + 动作条件` · `能力：预测 + 模拟` · `资源：项目`
  <details>
  <summary>收录依据</summary>
  <p>学习缝合子步骤的时空动力学，以预测机器人缝合的未来状态。</p>
  </details>

- (*MICCAI Workshop'25*) **Surgical Vision World Model**
  [[📝 论文](https://arxiv.org/abs/2503.02904)] [[💻 代码](https://github.com/bhattarailab/Surgical-Vision-World-Model)]
  **元数据：** `状态：操作／机器人` · `动力学：时间演化 + 动作条件` · `能力：预测 + 模拟` · `资源：代码`
  <details>
  <summary>收录依据</summary>
  <p>学习手术潜在动作及动作控制的未来视频动力学。</p>
  </details>

- (*arXiv'25*) **MM-DADM: Multimodal Drug-Aware Diffusion Model for Virtual Clinical Trials**
  [[📝 论文](https://arxiv.org/abs/2502.07297)]
  **元数据：** `状态：生理` · `动力学：时间演化 + 动作条件` · `能力：模拟 + 反事实` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>生成药物条件下的 ECG 状态变化，用于虚拟干预试验。</p>
  </details>

- (*MIDL'25*) **4D-VQ-GAN: A World Model for Synthesizing Medical Scans at Any Time Point for Personalized Disease Progression Modeling of Idiopathic Pulmonary Fibrosis**
  [[📝 论文](https://openreview.net/forum?id=tU3IpPQCEc)] [[💻 代码](https://github.com/anzhao920/4DVQGAN)] [[📝 arXiv](https://arxiv.org/abs/2502.05713)]
  **元数据：** `状态：医学影像` · `动力学：时间演化` · `能力：预测 + 模拟` · `资源：代码`
  <details>
  <summary>收录依据</summary>
  <p>通过连续时间潜在动力学，沿疾病进展轨迹合成患者影像。</p>
  </details>

### 2024

- (*arXiv'24*) **Structure-aware World Model for Probe Guidance via Large-scale Self-supervised Pre-train**
  [[📝 论文](https://arxiv.org/abs/2406.19756)]
  **元数据：** `状态：医学影像` · `动力学：空间／视角 + 动作条件` · `能力：预测 + 控制` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>预测以探头位姿变化为条件的超声切面转移。</p>
  </details>

- (*MICCAI'24*) **Cardiac Copilot: Automatic Probe Guidance for Echocardiography with World Model**（引入 Cardiac Dreamer，作为心脏空间结构的世界模型）
  [[📝 论文](https://arxiv.org/abs/2406.13165)]
  **元数据：** `状态：医学影像` · `动力学：空间／视角 + 动作条件` · `能力：模拟 + 控制` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>利用 Cardiac Dreamer 模拟探头动作下的空间观测变化，用于导航。</p>
  </details>

- (*arXiv'24*) **World Models for General Surgical Grasping**
  [[📝 论文](https://arxiv.org/abs/2405.17940)]
  **元数据：** `状态：操作／机器人` · `动力学：时间演化 + 动作条件` · `能力：模拟 + 规划 + 控制` · `资源：仅论文`
  <details>
  <summary>收录依据</summary>
  <p>学习手术抓取的状态转移动力学，通过基于模型的强化学习规划机器人动作。</p>
  </details>

---

<a id="-by-topic"></a>

## 🧭 按主题浏览

> 以下按主题提供另一种浏览方式。

<a id="medical-imaging-and-radiology"></a>

### 医学影像与放射学

- (*arXiv'26*) **DuoPIC: Uncertainty-Aware Voxel-Level Digital Twins of Cerebral Perfusion with Transport PDEs in Acute Stroke**
  [[📝 论文](https://arxiv.org/abs/2610.33071)] [[💻 代码](https://github.com/detinatran/duopic)]

- (*arXiv'26*) **Saga: an in silico ontology for a multimodal patient world model**
  [[📝 论文](https://arxiv.org/abs/2610.33054)]

- (*arXiv'26*) **CaMeWM: A Causal Medical World Model for Generative Tumor Evolution and Treatment Planning**
  [[📝 论文](https://arxiv.org/abs/2610.26923)]

- (*arXiv'26*) **SonoWorld: Towards Interactive Pose-Controllable Ultrasound World Models**
  [[📝 论文](https://arxiv.org/abs/2610.19327)] [[🌐 项目](https://iclr2027anonymous.github.io/SonoWorld/)]

- (*arXiv'26*) **UltraWorld: Learning Interactive Ultrasound World Models from Untracked Clinical Videos with Acoustic Sampling Map**
  [[📝 论文](https://arxiv.org/abs/2610.09785)] [[🌐 项目](https://ultraworld-project.github.io/)]

- (*arXiv'26*) **One Frame, Full Heartbeat: ECG-Free Cardiac Cine MRI Synthesis via Phase-Conditioned Flow Matching**
  [[📝 论文](https://arxiv.org/abs/2610.09397)]

- (*arXiv'26*) **One Frame, Full Heartbeat: ECG-Free 4D Cardiac Cine MRI Synthesis via Radial-Decomposed Flow Matching**
  [[📝 论文](https://arxiv.org/abs/2610.09185)]

- (*arXiv'26*) **Ultrasound Operator Guidance Using World Modeling and Retrieval Based Action Planning**
  [[📝 论文](https://arxiv.org/abs/2610.06008)]

- (*arXiv'26*) **An Uncertainty-Guided Digital Twin Framework for Online Adaptive Proton Therapy in Head and Neck Cancer: A Feasibility Study**
  [[📝 论文](https://arxiv.org/abs/2609.39010)]

- (*arXiv'26*) **A Digital-Twin Framework for Forecasting Treatment-Day Imaging with Contour Uncertainty in Adaptive Proton Radiotherapy**
  [[📝 论文](https://arxiv.org/abs/2609.24725)]

- (*npj Syst Biol Appl'26*) **Learning Patient-Specific Spatial Biomarker Dynamics via Operator Learning for Alzheimer's Disease Progression**
  [[📝 论文](https://doi.org/10.1038/s41540-026-00719-x)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42082519/)]

- (*arXiv'26*) **Uni-Flow: A Unified Autoregressive-Diffusion Model for Complex Multiscale Flows**
  [[📝 论文](https://arxiv.org/abs/2602.15592)]

- (*Comput Biol Med'26*) **Liquid Fourier Latent Dynamics Networks for Fast GPU-Based Numerical Simulations in Computational Cardiology**
  [[📝 论文](https://doi.org/10.1016/j.compbiomed.2025.111355)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41338030/)] [[📝 预印本](https://arxiv.org/abs/2408.09818)] [[💻 代码](https://github.com/StanfordCBCL/LFLDNets)]

- (*arXiv'26*) **Intervention-Aware Clinical World Model for Post-Op Outcome Forecasting in Cardiology**
  [[📝 论文](https://arxiv.org/abs/2608.13518)] [[💻 代码](https://github.com/cys1102/af-blanking-world-model)]

- (*arXiv'26*) **NeuroWorld: A Latent Brain World Model for Stimulus-Conditioned Human Brain Dynamics**
  [[📝 论文](https://arxiv.org/abs/2608.01773)]

- (*arXiv'26*) **Action-Conditioned World Model for Goal Plane Probe Guidance in Robotic Ultrasound**
  [[📝 论文](https://arxiv.org/abs/2607.21918)]

- (*arXiv'26*) **Differentiable Cardiac Electrophysiology Simulations for Dynamical State and Parameter Estimation**
  [[📝 论文](https://arxiv.org/abs/2607.15492)]

- (*MICCAI'26*) **HemoPIC: A Physics-Informed Cerebral Hemodynamics Digital Twin for Brain Perfusion**
  [[📝 论文](https://arxiv.org/abs/2607.08799)] [[💻 代码](https://github.com/jhuldr/HemoPIC)]

- (*arXiv'26*) **Personalized 4D Whole-Heart Mesh Reconstruction from Cine MRI via Multi-Scale Temporal Modeling and Differentiable Contour Rendering**
  [[📝 论文](https://arxiv.org/abs/2607.01952)]

- (*Med Image Anal'26*) **Electrophysiologically-Informed Digital Twins for Atrial Fibrillation**
  [[📝 论文](https://doi.org/10.1016/j.media.2026.104131)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42172939/)]

- (*arXiv'26*) **OphthaDT: Generative Digital Twins for Forecasting Visual Acuity Trajectories in Ophthalmology**
  [[📝 论文](https://arxiv.org/abs/2606.22101)]

- (*arXiv'26*) **DreamReg: Belief-Driven World Model for 2D-3D Ultrasound Registration**
  [[📝 论文](https://arxiv.org/abs/2606.18825)]

- (*arXiv'26*) **Learning Cardiac Electrophysiology Digital Twins Through Agentic Discovery of Hybrid Structure**
  [[📝 论文](https://arxiv.org/abs/2606.18154)]

- (*arXiv'26*) **GazeWorld: A World Model of Radiologist Reading for Medical Image Representation Learning**
  [[📝 论文](https://arxiv.org/abs/2605.23992)]

- (*arXiv'26*) **Beyond Patient Invariance: Learning Cardiac Dynamics via Action-Conditioned JEPAs**
  [[📝 论文](https://arxiv.org/abs/2604.22618)] [[💻 代码](https://github.com/cljosegfer/lesaude-dynamics)]

- (*arXiv'26*) **ECG-WM: A Physiology-Informed ECG World Model for Clinical Intervention Simulation**
  [[📝 论文](https://arxiv.org/abs/2605.17580)] [[🌐 项目](https://chenzk202212.github.io/ECG_World_Model/)]

- (*arXiv'26*) **EyeWorld: A Generative World Model of Ocular State and Dynamics**
  [[📝 论文](https://arxiv.org/abs/2603.14039)]

- (*CVPR'26*) **X-WIN: Building Chest Radiograph World Model via Predictive Sensing**
  [[📝 论文](https://arxiv.org/abs/2511.14918)]

- (*CVPR'26*) **MRI Contrast Enhancement Kinetics World Model**
  [[📝 论文](https://arxiv.org/abs/2602.19285)] [[💻 代码](https://github.com/DD0922/MRI-Contrast-Enhancement-Kinetics-World-Model)]

- (*arXiv'25*) **Xray2Xray: World Model from Chest X-rays with Volumetric Context**
  [[📝 论文](https://arxiv.org/abs/2506.19055)]

- (*CVPR'25*) **EchoWorld: Learning Motion-Aware World Models for Echocardiography Probe Guidance**
  [[📝 论文](https://arxiv.org/abs/2504.13065)]

- (*arXiv'25*) **MM-DADM: Multimodal Drug-Aware Diffusion Model for Virtual Clinical Trials**
  [[📝 论文](https://arxiv.org/abs/2502.07297)]

- (*MIDL'25*) **4D-VQ-GAN: A World Model for Synthesizing Medical Scans at Any Time Point for Personalized Disease Progression Modeling of Idiopathic Pulmonary Fibrosis**
  [[📝 论文](https://openreview.net/forum?id=tU3IpPQCEc)] [[💻 代码](https://github.com/anzhao920/4DVQGAN)] [[📝 arXiv](https://arxiv.org/abs/2502.05713)]

- (*arXiv'24*) **Structure-aware World Model for Probe Guidance via Large-scale Self-supervised Pre-train**
  [[📝 论文](https://arxiv.org/abs/2406.19756)]

- (*MICCAI'24*) **Cardiac Copilot: Automatic Probe Guidance for Echocardiography with World Model**（引入 Cardiac Dreamer，作为心脏空间结构的世界模型）
  [[📝 论文](https://arxiv.org/abs/2406.13165)]

<a id="computational-biology-and-cellular-dynamics"></a>

### 计算生物学与细胞动力学

- (*Cell Rep Med'26*) **Tumor digital twins uncover therapeutic strategies in triple-negative breast cancer**
  [[📝 论文](https://doi.org/10.1016/j.xcrm.2026.103119)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42933397/)] [[💻 代码](https://github.com/jfisher-lab/TNBC_Victori2026)]

- (*Protein Sci'26*) **DreamFold: A World Model to efficiently generate protein folding pathways in the latent space**
  [[📝 论文](https://doi.org/10.1002/pro.70794)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42813590/)] [[📝 预印本](https://www.biorxiv.org/content/10.1101/2025.03.26.645554v1)]

- (*medRxiv'26*) **Informing risk stratification and vaccine policy via a predictive mathematical model of SARS-COV-2 infection**
  [[📝 论文](https://www.medrxiv.org/content/10.64898/2026.10.12.26365315v1)]

- (*bioRxiv'26*) **scMTG reconstructs single-cell temporal dynamics with Markov transition generators**
  [[📝 论文](https://www.biorxiv.org/content/10.64898/2026.06.04.730241v2)] [[💻 代码](https://github.com/liuq-lab/scMTG)]

- (*bioRxiv'26*) **Mechanistic prediction of fecal microbiota transplant engraftment and Clostridioides difficile colonization resistance with μODE**
  [[📝 论文](https://www.biorxiv.org/content/10.64898/2026.10.09.758137v1)] [[💻 代码](https://github.com/cumbof/muODE)]

- (*bioRxiv'26*) **A tissue time machine to forward-predict single-timepoint data applied to tuberculosis granulomas**
  [[📝 论文](https://www.biorxiv.org/content/10.64898/2026.10.09.758083v1)]

- (*arXiv'26*) **Finsler Flow Matching: Dynamics-Aware Geodesic Interpolation for Single-Snapshot Trajectory Inference**
  [[📝 论文](https://arxiv.org/abs/2610.11318)] [[💻 代码](https://github.com/mlbelab/FinslerFlowMatching)]

- (*arXiv'26*) **MD-LLM-2: A Transferable Language Model of Molecular Dynamics with Physical Conditioning and Explicit Path Probabilities**
  [[📝 论文](https://arxiv.org/abs/2610.10879)]

- (*bioRxiv'26*) **Identifiable Inverse Optimal Transport for Single-Cell State Transitions**
  [[📝 论文](https://www.biorxiv.org/content/10.64898/2026.10.01.756056v1)] [[💻 代码](https://github.com/XTSgreen/IOT-single-cell-paper)]

- (*bioRxiv'26*) **AnnFlux: Object-Conditioned Neural Stochastic Differential Equations for Single-Cell Perturbation Dynamics**
  [[📝 论文](https://www.biorxiv.org/content/10.64898/2026.09.01.748703v1)]

- (*bioRxiv'26*) **MEGA-ODE: Learning Biologically Structured and Navigable Continuous Perturbation Dynamics from Sparse Omics**
  [[📝 论文](https://www.biorxiv.org/content/10.64898/2026.08.05.742921v1)] [[💻 代码](https://github.com/Candlelight-XYJ/MEGA-ODE)]

- (*Cell'26*) **RegVelo: Gene-Regulatory-Informed Dynamics of Single Cells**
  [[📝 论文](https://doi.org/10.1016/j.cell.2026.04.022)] [[💻 代码](https://github.com/theislab/regvelo)]

- (*bioRxiv'26*) **PHAROS: Turning Single-Cell Perturbation Models into Target-Directed Drug-Combination Screens**
  [[📝 论文](https://www.biorxiv.org/content/10.64898/2026.09.08.749477v1)] [[💻 代码](https://github.com/jbezney61/PHAROS)]

- (*bioRxiv'26*) **Forecasting Cell State Futures from Static Snapshots**
  [[📝 论文](https://www.biorxiv.org/content/10.64898/2026.02.08.704720v2)] [[💻 代码](https://github.com/EperLuo/CellTempo)]

- (*Nature'26*) **An Operational Perturbation Proteomics-Based Virtual Cell Model**
  [[📝 论文](https://doi.org/10.1038/s41586-026-11001-9)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42717098/)] [[💻 代码](https://github.com/guomics-lab/PTV-1)]

- (*bioRxiv'26*) **OPTIMIS: Optimizing Personalized Therapies through Integrated Multiscale Intelligent Simulation**
  [[📝 论文](https://www.biorxiv.org/content/10.64898/2026.03.24.713941v1)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41929084/)] [[💻 代码](https://github.com/wujah/OPTIMIS)]

- (*Sci Adv'25*) **Multiscale Mathematical Model-Informed Reinforcement Learning Optimizes Combination Treatment Scheduling in Glioblastoma Evolution**
  [[📝 论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC13155510/)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/40779623/)] [[💻 代码](https://github.com/SunXQlab/M4RL)]

- (*eLife'26*) **Large-Scale Synthetic Data Enable Digital Twins of Human Excitable Cells**
  [[📝 论文](https://doi.org/10.7554/eLife.110013)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42489674/)] [[💻 代码](https://github.com/ClancyLabUCD/Digital-Twin-for-the-Win-Personalized-Cardiac-Electrophysiology)]

- (*bioRxiv'26*) **Patient-Specific Heart Rate Modulates Developmental Electrophysiology in Transcriptomic-Guided In Silico Models of Pediatric Human Atrial Cardiomyocytes**
  [[📝 论文](https://www.biorxiv.org/content/10.64898/2026.07.21.739866v1)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42538960/)]

- (*Cell'26*) **Whole-Cell Particle-Based Digital Twin Simulations from 4D Lattice Light-Sheet Microscopy Data**
  [[📝 论文](https://doi.org/10.1016/j.cell.2026.06.010)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42379169/)] [[💻 代码](https://github.com/schoeneberglab/readdy-cell)]

- (*bioRxiv'26*) **A Physics-Inspired Classical Digital Twin of the Cell: A Composite Multi-Clock Port-Hamiltonian Neural Network Learned from Multi-Omic Circadian Data**
  [[📝 论文](https://www.biorxiv.org/content/10.64898/2026.07.11.737972v3)] [[💻 代码](https://github.com/quantum-omics/Classical-Virtual-Omics)]

- (*bioRxiv'26*) **U-Pert: Unbalanced Perturbation Dynamics For Cell Fate Design**
  [[📝 论文](https://www.biorxiv.org/content/10.64898/2026.06.30.735555v1)]

- (*arXiv'26*) **Chreode: A Cell World Model for One-Step Temporal Dynamics and Perturbation Prediction**
  [[📝 论文](https://arxiv.org/abs/2605.28111)] [[💻 代码](https://github.com/mufanq/Chreode)] [[🌐 权重](https://huggingface.co/MufanQiu/chreode-pretrained)]

- (*arXiv'26*) **MolWorld: Molecule World Models for Actionable Molecular Optimization**
  [[📝 论文](https://arxiv.org/abs/2605.08954)]

- (*arXiv'26*) **BLINK: Behavioral Latent Modeling of NK Cell Cytotoxicity**
  [[📝 论文](https://arxiv.org/abs/2603.05110)]

- (*arXiv'26*) **Lingshu-Cell: A Generative Cellular World Model for Transcriptome Modeling Toward Virtual Cells**
  [[📝 论文](https://arxiv.org/abs/2603.25240)]

- (*bioRxiv'26*) **Towards building a World Model to simulate perturbation-induced cellular dynamics by AlphaCell**
  [[📝 论文](https://www.biorxiv.org/content/10.64898/2026.03.02.709176v1)]

- (*arXiv'25*) **VCWorld: A Biological World Model for Virtual Cell Simulation**
  [[📝 论文](https://arxiv.org/abs/2512.00306)]

<a id="longitudinal-ehr-and-clinical-trajectories"></a>

### 纵向电子健康记录与临床轨迹

- (*arXiv'26*) **PulmoWorld: An Asynchronous Multimodal Medical World Model for Longitudinal Pneumonia Dynamics**
  [[📝 论文](https://arxiv.org/abs/2610.38289)]

- (*medRxiv'26*) **Digital Twin Workflow for Continuous Glucose Forecasting: Real-Time Data Assimilation Using Reinforcement Learning**
  [[📝 论文](https://www.medrxiv.org/content/10.64898/2026.10.23.26366163v1)]

- (*arXiv'26*) **Saga: an in silico ontology for a multimodal patient world model**
  [[📝 论文](https://arxiv.org/abs/2610.33054)]

- (*medRxiv'26*) **FERMAT: An Autoregressive Clinical Foundation Model for Disease Risk and Clinical Event Prediction**
  [[📝 论文](https://www.medrxiv.org/content/10.64898/2026.10.11.26365210v1)]

- (*arXiv'26*) **PatientWM: Towards Generalizable Clinical World Models via Unified Patient States**
  [[📝 论文](https://arxiv.org/abs/2610.17059)]

- (*arXiv'26*) **Sign-Constrained Intervention Effects for Domain-Generalizable ICU World Models**
  [[📝 论文](https://arxiv.org/abs/2610.11090)]

- (*arXiv'26*) **Similar Predictive Fit but Different Latent Dynamics: Characterizing Learned Dynamical Structure in Personalized Models of Brain Disorders**
  [[📝 论文](https://arxiv.org/abs/2610.10850)]

- (*arXiv'26*) **HyperNSDE: Personalized Neural SDEs for Joint Static-Longitudinal Clinical Data Generation**
  [[📝 论文](https://arxiv.org/abs/2610.07383)] [[💻 代码](https://github.com/perrinechassat/HyperNSDE)]

- (*npj Metab Health Dis'26*) **A Digital Twin for Tracking and Forecasting Glycemia with Septic Patients in ICUs**
  [[📝 论文](https://doi.org/10.1038/s44324-026-00132-2)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42823439/)]

- (*medRxiv'26*) **A World Model Simulates the Latent Dynamics of Human Health**
  [[📝 论文](https://www.medrxiv.org/content/10.64898/2026.09.19.26363460v1)]

- (*Front Med'26*) **Beyond Static Risk Scores: Dynamic World Models Simulating Patient-Specific Trajectories to Inform Preoperative Risk Mitigation Strategies**
  [[📝 论文](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2026.1913206/full)] [[💻 代码](https://github.com/ustive/Beyond-Static-Risk-Scores-Dynamic-World-Models)]

- (*medRxiv'26*) **The Coupled Stochastic Dynamical System: A Generative Model for Simulating and Forecasting Youth Mental Health Trajectories**
  [[📝 论文](https://www.medrxiv.org/content/10.64898/2026.07.26.26358943v1)]

- (*arXiv'26*) **FlatASCEND: Autoregressive Clinical Sequence Generation with Continuous Time Prediction and Association-Based Pharmacological Testing**
  [[📝 论文](https://arxiv.org/abs/2605.04071)]

- (*arXiv'26*) **High-Fidelity Longitudinal Patient Simulation Using Real-World Data**
  [[📝 论文](https://arxiv.org/abs/2601.17310)] [[💻 代码](https://github.com/yuakagi/Watcher)]

- (*arXiv'26*) **A Physiology-Informed Digital Twin Framework for Simulating Liver Health Progression**
  [[📝 论文](https://arxiv.org/abs/2608.14969)]

- (*arXiv'26*) **Intervention-Aware Clinical World Model for Post-Op Outcome Forecasting in Cardiology**
  [[📝 论文](https://arxiv.org/abs/2608.13518)] [[💻 代码](https://github.com/cys1102/af-blanking-world-model)]

- (*arXiv'26*) **PIONEER: Bayesian Joint Modelling of Mechanistic Tumour Growth and Time-to-Event Endpoints for Dynamic Prediction of Ongoing Oncology Trials**
  [[📝 论文](https://arxiv.org/abs/2607.17908)]

- (*arXiv'26*) **EHR-MPC: Inference-Time Control for Sepsis Treatment with Generative Patient Digital Twins**
  [[📝 论文](https://arxiv.org/abs/2607.08793)]

- (*arXiv'26*) **OphthaDT: Generative Digital Twins for Forecasting Visual Acuity Trajectories in Ophthalmology**
  [[📝 论文](https://arxiv.org/abs/2606.22101)]

- (*arXiv'26*) **Neural Operator-Based Digital Twins for Modeling Amyloid-Beta and Tau Propagation and Treatment Optimization in Alzheimer's Disease**
  [[📝 论文](https://arxiv.org/abs/2606.25185)]

- (*arXiv'26*) **Transition-Based Digital Twin Modelling for Alzheimer's Disease under Sparse Longitudinal Data**
  [[📝 论文](https://arxiv.org/abs/2606.09671)]

- (*arXiv'26*) **ChronoMedicalWorld: A Medical World Model for Learning Patient Trajectories from Longitudinal Care Data**
  [[📝 论文](https://arxiv.org/abs/2605.21963)]

- (*arXiv'26*) **Toward World Modeling of Physiological Signals with Chaos-Theoretic Balancing and Latent Dynamics (NormWear-2)**
  [[📝 论文](https://arxiv.org/abs/2605.15465)]

- (*arXiv'26*) **Agentifying Patient Dynamics within LLMs through Interacting with Clinical World Model**
  [[📝 论文](https://arxiv.org/abs/2605.14723)] [[💻 代码](https://github.com/FreedomIntelligence/SepsisAgent)]

- (*arXiv'26*) **Simulating Clinical Interventions with a Generative Multimodal Model of Human Physiology (HealthFormer)**
  [[📝 论文](https://arxiv.org/abs/2604.27899)]

- (*arXiv'26*) **Sonata: A Hybrid World Model for Inertial Kinematics under Clinical Data Scarcity**
  [[📝 论文](https://arxiv.org/abs/2604.18058)]

- (*arXiv'26*) **EHRWorld: A Patient-Centric Medical World Model for Long-Horizon Clinical Trajectories**
  [[📝 论文](https://arxiv.org/abs/2602.03569)]

- (*arXiv'26*) **The Patient is not a Moving Document: A World Model Training Paradigm for Longitudinal EHR**
  [[📝 论文](https://arxiv.org/abs/2601.22128)]

- (*arXiv'26*) **Generating Counterfactual Patient Timelines from Real-World Data**
  [[📝 论文](https://arxiv.org/abs/2604.02337)]

- (*arXiv'26*) **RAVEN: Scaling Recurrence-Aware Foundation Models for Clinical Records via Next-Visit Prediction**
  [[📝 论文](https://arxiv.org/abs/2603.24562)]

- (*NPJ Digit Med'25*) **Large Language Models Forecast Patient Health Trajectories Enabling Digital Twins**
  [[📝 论文](https://doi.org/10.1038/s41746-025-02004-3)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41034564/)] [[💻 代码](https://github.com/MendenLab/DT-GPT)]

- (*arXiv'25*) **medDreamer: Model-Based Reinforcement Learning with Latent Imagination on Complex EHRs for Clinical Decision Support**
  [[📝 论文](https://arxiv.org/abs/2505.19785)]

- (*arXiv'25*) **Generative Medical Event Models Improve with Scale (CoMET)**
  [[📝 论文](https://arxiv.org/abs/2508.12104)]

<a id="treatment-planning-and-clinical-decision-support"></a>

### 治疗规划与临床决策支持

- (*arXiv'26*) **PulmoWorld: An Asynchronous Multimodal Medical World Model for Longitudinal Pneumonia Dynamics**
  [[📝 论文](https://arxiv.org/abs/2610.38289)]

- (*Cell Rep Med'26*) **Tumor digital twins uncover therapeutic strategies in triple-negative breast cancer**
  [[📝 论文](https://doi.org/10.1016/j.xcrm.2026.103119)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42933397/)] [[💻 代码](https://github.com/jfisher-lab/TNBC_Victori2026)]

- (*arXiv'26*) **CaMeWM: A Causal Medical World Model for Generative Tumor Evolution and Treatment Planning**
  [[📝 论文](https://arxiv.org/abs/2610.26923)]

- (*arXiv'26*) **APOD: Reasoning-Guided Agentic Population Ordinary Differential Equation Discovery for Pharmacological Digital Twins**
  [[📝 论文](https://arxiv.org/abs/2610.06227)] [[💻 代码](https://gitlab.inria.fr/compo/apod)]

- (*arXiv'26*) **Graph World Models for Constrained Epidemic Policy Planning**
  [[📝 论文](https://arxiv.org/abs/2609.35545)] [[💻 代码](https://anonymous.4open.science/r/epimind-9706/README.md)]

- (*arXiv'26*) **An Uncertainty-Guided Digital Twin Framework for Online Adaptive Proton Therapy in Head and Neck Cancer: A Feasibility Study**
  [[📝 论文](https://arxiv.org/abs/2609.39010)]

- (*Front Med'26*) **Beyond Static Risk Scores: Dynamic World Models Simulating Patient-Specific Trajectories to Inform Preoperative Risk Mitigation Strategies**
  [[📝 论文](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2026.1913206/full)] [[💻 代码](https://github.com/ustive/Beyond-Static-Risk-Scores-Dynamic-World-Models)]

- (*ECCV'26*) **CLARITY: Medical World Model for Guiding Treatment Decisions by Modeling Context-Aware Disease Trajectories in Latent Space**
  [[📝 论文](https://arxiv.org/abs/2512.08029)] [[💻 代码](https://github.com/DingTianxingjian/CLARITY)] [[🌐 项目](https://dingtianxingjian.github.io/clarity-project-page/)]

- (*Life AI'26*) **Diffusion-Pref: Diffusion World Model Guided Zero-Shot Preference Learning for Safe Glucose Control in Type 1 Diabetes**
  [[📝 论文](https://www.sciltp.com/journals/lifeai/articles/2604003779)] [[💻 代码](https://github.com/aussie-bzhang/Diffusion-Pref)]

- (*npj Syst Biol Appl'26*) **Learning Patient-Specific Spatial Biomarker Dynamics via Operator Learning for Alzheimer's Disease Progression**
  [[📝 论文](https://doi.org/10.1038/s41540-026-00719-x)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42082519/)]

- (*AISTATS'26*) **Bayesian Inverse Transition Learning: Learning Dynamics from Near-Optimal Trajectories**
  [[📝 论文](https://proceedings.mlr.press/v300/benac26a.html)]

- (*bioRxiv'26*) **OPTIMIS: Optimizing Personalized Therapies through Integrated Multiscale Intelligent Simulation**
  [[📝 论文](https://www.biorxiv.org/content/10.64898/2026.03.24.713941v1)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41929084/)] [[💻 代码](https://github.com/wujah/OPTIMIS)]

- (*bioRxiv'26*) **Digital Twin Brain Simulation and Manipulation of a Functional Brain Network Underlying Mental Illness**
  [[📝 论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC13015335/)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41890017/)] [[💻 代码](https://github.com/Shmily94/Digital_twin_brain-psychiatry-)]

- (*AAAI'26*) **Bootstrapping Personalized Insulin Therapy via Model-Based Reinforcement Learning: An In Silico Study**
  [[📝 论文](https://ojs.aaai.org/index.php/AAAI/article/view/41160)]

- (*BMC Med'26*) **Digital Twin Brain Reveals State-Specific Stimulation Targets for Abnormal Brain Dynamics in Tinnitus**
  [[📝 论文](https://doi.org/10.1186/s12916-026-04687-1)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41664110/)]

- (*Smart Health'26*) **Patient-Specific Deep Offline Artificial Pancreas for Blood Glucose Regulation in Type 1 Diabetes**
  [[📝 论文](https://doi.org/10.1016/j.smhl.2026.100633)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41766716/)]

- (*J Neuroeng Rehabil'25*) **Towards AI-Based Precision Rehabilitation via Contextual Model-Based Reinforcement Learning**
  [[📝 论文](https://doi.org/10.1186/s12984-025-01771-0)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41419889/)]

- (*Sci Adv'25*) **Multiscale Mathematical Model-Informed Reinforcement Learning Optimizes Combination Treatment Scheduling in Glioblastoma Evolution**
  [[📝 论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC13155510/)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/40779623/)] [[💻 代码](https://github.com/SunXQlab/M4RL)]

- (*npj Digit Med'25*) **Digital Twin Brain Simulator for Real-Time Consciousness Monitoring and Virtual Intervention Using Primate Electrocorticogram Data**
  [[📝 论文](https://doi.org/10.1038/s41746-025-01444-1)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/39929926/)]

- (*J Physiol'26*) **An Eikonal Model with Re-Excitability for Fast Simulations in Cardiac Electrophysiology**
  [[📝 论文](https://doi.org/10.1113/JP287281)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42678922/)] [[📝 预印本](https://arxiv.org/abs/2410.22583)]

- (*Med Image Anal'26 Online*) **Towards Patient-Specific Optimization for Mandibular Reconstruction Planning Based on Predicted Bone-Union Propensity**
  [[📝 论文](https://doi.org/10.1016/j.media.2026.104281)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42700676/)] [[📝 预印本](https://arxiv.org/abs/2605.01084)] [[💻 代码](https://github.com/hamidreza-aftabi/OsteoOpt)]

- (*arXiv'26*) **A Physiology-Informed Digital Twin Framework for Simulating Liver Health Progression**
  [[📝 论文](https://arxiv.org/abs/2608.14969)]

- (*Nat Cardiovasc Res'26*) **Accounting for Uncertainty in Computational Models of Ventricular Tachycardia Improves Ablation Guidance**
  [[📝 论文](https://doi.org/10.1038/s44161-026-00856-w)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42601469/)]

- (*arXiv'26*) **Intervention-Aware Clinical World Model for Post-Op Outcome Forecasting in Cardiology**
  [[📝 论文](https://arxiv.org/abs/2608.13518)] [[💻 代码](https://github.com/cys1102/af-blanking-world-model)]

- (*Phys Med Biol'26*) **Towards a Clinically Practical Computational Platform for Systematically Adapting Radiation Therapy for Glioma Patients**
  [[📝 论文](https://doi.org/10.1088/1361-6560/ae9687)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42562016/)]

- (*Ann Biomed Eng'26*) **Developing a Digital Twin of the Cardiopulmonary System in a Mouse: Inferring Hemodynamics from Sparse Measurements**
  [[📝 论文](https://doi.org/10.1007/s10439-026-04107-8)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42550388/)]

- (*Bull Math Biol'26*) **Assessing the Role of Model Complexity in Virtual Clinical Trial Outcomes**
  [[📝 论文](https://doi.org/10.1007/s11538-026-01715-2)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42530700/)] [[💻 代码](https://github.com/jgevertz/VCT)]

- (*Comput Methods Programs Biomed'26*) **Integrating EMT Dynamics in Model-Based Metastasis Prediction**
  [[📝 论文](https://doi.org/10.1016/j.cmpb.2026.109390)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42061167/)]

- (*Heart Rhythm'26*) **High-Fidelity Postmyocardial Infarction Ventricular Tachycardia Simulation for Intraprocedure Ablation Guidance**
  [[📝 论文](https://doi.org/10.1016/j.hrthm.2026.03.1962)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41956268/)]

- (*arXiv'26*) **An Open-Source Framework for Predicting Ultrasound Neuromodulation: Bridging Tissue Elastomechanics and Neuron Firing Dynamics**
  [[📝 论文](https://arxiv.org/abs/2608.06321)]

- (*bioRxiv'26*) **Parameter-Dependent Effects of Spinal Cord Stimulation on Neural Activation and Evoked Compound Action Potentials**
  [[📝 论文](https://www.biorxiv.org/content/10.64898/2026.08.03.742575v1)]

- (*bioRxiv'26*) **A Dynamical Digital Twin Unmasks Hidden Neuromotor Control Policies and Catastrophic Tipping Points in Parkinson's Disease**
  [[📝 论文](https://www.biorxiv.org/content/10.64898/2026.03.09.710685v2)]

- (*arXiv'26*) **Optimal Stimulation Sites Are Not the Most Affected: Personalised Models of Resting-State fMRI in Alzheimer's Disease**
  [[📝 论文](https://arxiv.org/abs/2607.24356)] [[💻 代码](https://github.com/cristianocapone/AD-reservoir-FC-stimulation)]

- (*MICCAI'26 Workshop*) **Automatic Patient-Specific Microwave Ablation Planning Accelerated by a Physics-Guided Deep Learning Model**
  [[📝 论文](https://arxiv.org/abs/2608.03086)]

- (*MICCAI'26 Workshop*) **Anticipatory Digital Twins for Online Head-and-Neck Adaptive Proton Therapy via Foundation-Model Registration**
  [[📝 论文](https://arxiv.org/abs/2608.00831)]

- (*arXiv'26*) **A Digital-Twin Framework for Forecasting Treatment-Day Imaging with Contour Uncertainty in Adaptive Proton Radiotherapy**
  [[📝 论文](https://arxiv.org/abs/2609.24725)]

- (*arXiv'26*) **A Diffusion-Model Subpopulation Digital Twin for Mobile Health Deployment: A Case Study on the HeartSteps Intervention**
  [[📝 论文](https://arxiv.org/abs/2607.21403)]

- (*arXiv'26*) **Enhancing Personalized Bladder Cancer Treatment Through Reinforcement Learning: A Recurrent Patient State Transition Decision Support Framework**
  [[📝 论文](https://arxiv.org/abs/2607.16916)]

- (*arXiv'26*) **AI-Augmented Adaptive Digital Twin Modeling for Brain Tumor Evolution Prediction and Treatment Scheduling**
  [[📝 论文](https://arxiv.org/abs/2607.13877)]

- (*arXiv'26*) **EHR-MPC: Inference-Time Control for Sepsis Treatment with Generative Patient Digital Twins**
  [[📝 论文](https://arxiv.org/abs/2607.08793)]

- (*arXiv'26*) **Sectorial Customized Corneal Crosslinking for Keratoconus: An Inverse Biomechanical Design Study with an Anisotropic Reduced Shell Finite-Element Surrogate**
  [[📝 论文](https://arxiv.org/abs/2607.06385)]

- (*medRxiv'26*) **Personalized Planning of Cardiac Resynchronization Therapy Through Integration of Coronary Sinus Geometry, Clinical Data, Digital Twins, and Machine Learning: Visualization, Stratification, and Optimization**
  [[📝 论文](https://www.medrxiv.org/content/10.64898/2026.07.01.26356827v1)]

- (*Stem Cell Reports'26*) **In Silico Optimization of Regenerative Cell Therapy in the Infarcted Human Ventricles to Mitigate Arrhythmic Burden**
  [[📝 论文](https://doi.org/10.1016/j.stemcr.2026.103007)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42425090/)]

- (*Med Image Anal'26*) **Electrophysiologically-Informed Digital Twins for Atrial Fibrillation**
  [[📝 论文](https://doi.org/10.1016/j.media.2026.104131)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42172939/)]

- (*J Physiol'26*) **Prospective In Silico Trials Identify Combined SK and K2P Channel Block as an Effective Strategy for Atrial Fibrillation Cardioversion**
  [[📝 论文](https://doi.org/10.1113/JP287124)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/39557619/)]

- (*Phys Med Biol'26*) **A Digital Twin Framework for Adaptive Treatment Planning in Radiotherapy**
  [[📝 论文](https://doi.org/10.1088/1361-6560/ae835a)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42361838/)]

- (*arXiv'26*) **Neural Operator-Based Digital Twins for Modeling Amyloid-Beta and Tau Propagation and Treatment Optimization in Alzheimer's Disease**
  [[📝 论文](https://arxiv.org/abs/2606.25185)]

- (*Biomed Phys Eng Express'26*) **Physics-Informed Koopman-Constrained ImplicitQ-Learning for Safe Offline Reinforcement Learning in Mechanical Ventilation**
  [[📝 论文](https://doi.org/10.1088/2057-1976/ae7d30)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42296990/)]

- (*arXiv'26*) **Treatment Response Optimized Clinical Decision Support AI System via Digital Twin Simulation**
  [[📝 论文](https://arxiv.org/abs/2606.17405)]

- (*Comput Biol Med'26*) **Causal Counterfactual Simulation for Treatment Decisions in Multimodal Lung Disease Data**
  [[📝 论文](https://doi.org/10.1016/j.compbiomed.2026.111807)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42275812/)]

- (*IEEE JBHI'26*) **TwinRL-Onco: A World Model-Empowered Digital Twin Framework with Hierarchical Reinforcement Learning for Venetoclax Resistance Trajectory Prediction and Adaptive Therapy Optimization in Chronic Lymphocytic Leukemia**
  [[📝 论文](https://doi.org/10.1109/JBHI.2026.3696685)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42184194/)]

- (*arXiv'26*) **Agentifying Patient Dynamics within LLMs through Interacting with Clinical World Model**
  [[📝 论文](https://arxiv.org/abs/2605.14723)] [[💻 代码](https://github.com/FreedomIntelligence/SepsisAgent)]

- (*arXiv'26*) **ECG-WM: A Physiology-Informed ECG World Model for Clinical Intervention Simulation**
  [[📝 论文](https://arxiv.org/abs/2605.17580)] [[🌐 项目](https://chenzk202212.github.io/ECG_World_Model/)]

- (*arXiv'26*) **Policy4OOD: A Knowledge-Guided World Model for Policy Intervention Simulation against the Opioid Overdose Crisis**
  [[📝 论文](https://arxiv.org/abs/2602.12373)]

- (*arXiv'26*) **Brain-WM: Brain Glioblastoma World Model**
  [[📝 论文](https://arxiv.org/abs/2603.07562)] [[💻 代码](https://github.com/thibault-wch/Brain-GBM-world-model)]

- (*bioRxiv'25*) **Virtual Clinical Trials of BMP4 Differentiation Therapy: Digital Twins to Aid Successful Glioblastoma Trial Design**
  [[📝 论文](https://doi.org/10.1101/2024.08.22.609156)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/41279885/)] [[💻 代码](https://github.com/Harbour-N/Virtual-Clinical-Trials-of-BMP4-Differentiation-Therapy)]

- (*arXiv'25*) **MM-DADM: Multimodal Drug-Aware Diffusion Model for Virtual Clinical Trials**
  [[📝 论文](https://arxiv.org/abs/2502.07297)]

- (*ICCV'25*) **Medical World Model: Generative Simulation of Tumor Evolution for Treatment Planning**
  [[📝 论文](https://arxiv.org/abs/2506.02327)] [[💻 代码](https://github.com/scott-yjyang/MeWM)] [[🌐 项目](https://yijun-yang.github.io/MeWM/)]

- (*AI Medicine'26*) **World Model Enhanced Offline Reinforcement Learning for Sequential Intervention Optimization in Acute Kidney Injury**
  [[📝 论文](https://www.sciltp.com/journals/aim/articles/2602002965)]

- (*arXiv'25*) **Evolving Diagnostic Agents in a Virtual Clinical Environment**
  [[📝 论文](https://arxiv.org/abs/2510.24654)]

<a id="surgical-simulation-and-embodied-healthcare"></a>

### 手术模拟与医疗具身智能

- (*arXiv'26*) **SurgTransfer: Multi-Step Latent Action Modeling for Action Transfer in Surgical World Model**
  [[📝 论文](https://arxiv.org/abs/2611.05443)] [[💻 代码](https://github.com/bhattarailab/Surgical-Vision-World-Model)]

- (*arXiv'26*) **ProCut: Probabilistic Cutting Topology for Autonomous Electrosurgical Tissue Dissection**
  [[📝 论文](https://arxiv.org/abs/2610.07515)]

- (*arXiv'26*) **SurgGMF: Fully Causal Gaussian Motion Forecasting for Anticipatory Surgical Scene Rendering**
  [[📝 论文](https://arxiv.org/abs/2609.34733)]

- (*arXiv'26*) **Towards Surgical World-Action Modeling: A Preliminary Joint Visual-Trajectory Forecasting for Surgical Motion Planning**
  [[📝 论文](https://arxiv.org/abs/2608.20284)]

- (*arXiv'26*) **NVIDIA Cosmos-H-Dreams: Real-Time Generative Physics Simulation for Surgical Robotics**
  [[📝 论文](https://arxiv.org/abs/2608.24199)] [[💻 代码](https://github.com/isaac-for-healthcare/Cosmos-H-Dreams)] [[🌐 权重](https://huggingface.co/nvidia/Cosmos-H-Dreams)]

- (*arXiv'26*) **Progressive Experience Fusion for Multi-Task World Model Control in Endovascular Navigation**
  [[📝 论文](https://arxiv.org/abs/2608.18647)]

- (*arXiv'26*) **Surgical WAM: A World-Action Model for Data-Efficient Surgical Robot Learning**
  [[📝 论文](https://arxiv.org/abs/2608.11204)]

- (*arXiv'26*) **Stable Long-Horizon Neural ODE Reduced-Order Models via Learned Feedback for Biological Growth and Remodeling**
  [[📝 论文](https://arxiv.org/abs/2604.13820)] [[💻 代码](https://github.com/joel-laudo/TE-skin-NODE-ROM)]

- (*Nat Mach Intell'25*) **Model-Based Reinforcement Learning for Ultrasound-Driven Autonomous Microrobots**
  [[📝 论文](https://doi.org/10.1038/s42256-025-01054-2)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/40709099/)] [[💻 代码](https://github.com/M-Medany/Model-Based-Reinforcement-Learning-for-Ultrasound-Driven-Autonomous-Microrobots)]

- (*Med Image Anal'26 Online*) **Towards Patient-Specific Optimization for Mandibular Reconstruction Planning Based on Predicted Bone-Union Propensity**
  [[📝 论文](https://doi.org/10.1016/j.media.2026.104281)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42700676/)] [[📝 预印本](https://arxiv.org/abs/2605.01084)] [[💻 代码](https://github.com/hamidreza-aftabi/OsteoOpt)]

- (*arXiv'26*) **S2-HWM: Sparse Event-Structured Hierarchical World Model for Long-Horizon Surgical Robot Manipulation**
  [[📝 论文](https://arxiv.org/abs/2608.13103)]

- (*arXiv'26*) **CrossScope: A Role-Asymmetric World Model for Joint Dual-Scope Surgical Video Prediction**
  [[📝 论文](https://arxiv.org/abs/2608.03211)]

- (*arXiv'26*) **EndoWAM: A Grounded World-Action Model for Generalizable Endoscopic Navigation**
  [[📝 论文](https://arxiv.org/abs/2608.01221)]

- (*arXiv'26*) **Failure Detection for Surgical Robot Imitation Policies via Flow-Matching World Modeling**
  [[📝 论文](https://arxiv.org/abs/2607.27511)]

- (*arXiv'26*) **SurgVista: Long-Horizon Surgical World Modeling with Plausible Instrument-Tissue Dynamics**
  [[📝 论文](https://arxiv.org/abs/2606.19889)]

- (*arXiv'26*) **SWoMo: Neuro-Symbolic World Model for Cataract Surgery Simulation**
  [[📝 论文](https://arxiv.org/abs/2605.16530)] [[🌐 项目](https://ssharvienkumar.github.io/SWoMo/)]

- (*arXiv'26*) **Toward Safe Autonomous Robotic Endovascular Interventions using World Models**
  [[📝 论文](https://arxiv.org/abs/2604.20151)]

- (*arXiv'26*) **SAW: Toward a Surgical Action World Model via Controllable and Scalable Video Generation**
  [[📝 论文](https://arxiv.org/abs/2603.13024)]

- (*ICLR'26 Rejected*) **Unified Surgical World Model for Structured Understanding, Long-Horizon Prediction, and Fine-Grained Generation**
  [[📝 论文](https://openreview.net/forum?id=Kk9t5empEf)]

- (*MIDL'26 rejected*) **Learning Action-Conditioned World Models for Cataract Surgery from Unlabeled Videos (SurgWorld)**
  [[📝 论文](https://openreview.net/forum?id=aYQYOVm2AB)]

- (*medRxiv'26*) **MedOS: AI-XR-Cobot World Model for Clinical Perception and Action**
  [[📝 论文](https://www.medrxiv.org/content/10.64898/2026.02.18.26345936v1)]

- (*arXiv'26*) **Open-H-Embodiment: A Large-Scale Dataset for Enabling Foundation Models in Medical Robotics**
  [[📝 论文](https://arxiv.org/abs/2604.21017)] [[💻 代码](https://huggingface.co/nvidia/Cosmos-H-Surgical-Simulator)] [[💻 代码](https://github.com/NVIDIA-Medtech/Cosmos-H-Surgical-Simulator)] [[🌐 项目](https://open-h.github.io/open-h-embodiment/)]

- (*arXiv'25*) **Cosmos-H-Surgical: Learning Surgical Robot Policies from Videos via World Modeling**
  [[📝 论文](https://arxiv.org/abs/2512.23162)] [[💻 代码](https://huggingface.co/nvidia/Cosmos-H-Surgical-Simulator)] [[💻 代码](https://github.com/nvidia-cosmos/cosmos-cookbook)]

- (*arXiv'25*) **Cosmos-Surg-dVRK: World Foundation Model-based Automated Online Evaluation of Surgical Robot Policy Learning**
  [[📝 论文](https://arxiv.org/abs/2510.16240)]

- (*MICCAI'25*) **World Model for AI Autonomous Navigation in Mechanical Thrombectomy**
  [[📝 论文](https://arxiv.org/abs/2509.25518)]

- (*arXiv'25*) **Visuomotor Grasping with World Models for Surgical Robots**
  [[📝 论文](https://arxiv.org/abs/2508.11200)]

- (*arXiv'25*) **Towards Suturing World Models: Learning Predictive Models for Robotic Surgical Tasks**
  [[📝 论文](https://arxiv.org/abs/2503.12531)] [[🌐 项目](https://mkturkcan.github.io/suturingmodels/)]

- (*MICCAI Workshop'25*) **Surgical Vision World Model**
  [[📝 论文](https://arxiv.org/abs/2503.02904)] [[💻 代码](https://github.com/bhattarailab/Surgical-Vision-World-Model)]

- (*arXiv'24*) **World Models for General Surgical Grasping**
  [[📝 论文](https://arxiv.org/abs/2405.17940)]

---

<a id="resources"></a>

<a id="-datasets-benchmarks-and-simulators"></a>

## 🧰 资源

> 对于数据集、评测基准与模拟器，本索引的收录范围比通用医学 AI 目录更窄：数据集须支持至少一个符合标准的医学世界模型；基准须评估动力学或轨迹推演；模拟器须提供能够推进医学状态的实现。被列入资源索引，不代表仅发布数据集或基准的论文也进入论文主目录。

### 数据集

| 资源 | 领域 | 世界模型用途 | 获取方式 |
|---|---|---|---|
| **Open-H-Embodiment** | 手术机器人 | 跨多个临床平台同步采集的视频与机器人运动学数据，用于训练动作条件下的手术轨迹推演。 | [[📦 数据集](https://huggingface.co/datasets/nvidia/PhysicalAI-Robotics-Open-H-Embodiment)] [[🌐 项目](https://open-h.github.io/open-h-embodiment/)] [[📝 论文](https://arxiv.org/abs/2604.21017)] |
| **MIMIC-IV** | 纵向电子健康记录 | 带时间戳的住院与 ICU 轨迹，用于治疗条件下的患者模拟，包括 SepsisAgent 临床世界模型。 | [[📦 数据集](https://physionet.org/content/mimiciv/3.0/)] [[📝 示例](https://arxiv.org/abs/2605.14723)] |
| **MIMIC-IV-ECG** | 心脏电生理 | 与临床记录关联的 ECG，用于学习事件条件下的心脏状态转移。 | [[📦 数据集](https://physionet.org/content/mimic-iv-ecg/1.0/)] [[📝 示例](https://arxiv.org/abs/2604.22618)] |
| **ISLES 2017** | 脑灌注 MRI | HemoPIC 脑血流动力学数字孪生使用的灌注加权时间序列与参考图。 | [[📦 数据集](https://zenodo.org/records/17736412)] [[💻 HemoPIC](https://github.com/jhuldr/HemoPIC)] |

### 评测基准

| 基准 | 领域 | 评估内容 | 可用资源 |
|---|---|---|---|
| **T1D Digital Twin Decision-Quality Benchmark** | 葡萄糖—胰岛素动力学 | 在一种基础—餐时胰岛素方案下拟合每个孪生模型，再在 30 名 UVA/Padova 虚拟患者中，评估其他 20 种方案下的血糖轨迹保真度、治疗排序相关性与决策遗憾；全部实验均为计算模拟。 | [[📝 论文](https://arxiv.org/abs/2610.30577)] [[💻 代码与方案](https://github.com/Veeeeeee7/T1D-Digital-Twin-Benchmark)] |
| **SurgWMBench** | 手术器械运动 | 在 SAR-RARP50 缝合片段上评估短时程轨迹预测、递归推演稳定性与扰动鲁棒性；区分以影像为条件和完全依赖预测的推演设置。 | [[📝 论文说明](https://arxiv.org/abs/2608.08070)] `仅论文` |
| **Open-H Multi-Embodiment Surgical Benchmark** | 手术机器人 | 通过帧退化、器械一致性及器械位移指标，评估九种机器人具身形态下动作条件未来视频的保真度。 | [[📦 数据](https://huggingface.co/datasets/nvidia/PhysicalAI-Robotics-Open-H-Embodiment)] [[💻 评估](https://github.com/NVIDIA-Medtech/Cosmos-H-Surgical-Simulator)] |
| **UniSWM-Bench** | 手术流程与视频 | 涵盖五项理解任务、两项长时程预测任务，以及三项以动作或运动为条件的生成任务。 | [[📝 论文说明](https://openreview.net/forum?id=Kk9t5empEf)] `仅论文` |
| **SurgVeo and Surgical Plausibility Pyramid** | 手术视频 | 由专家从视觉、器械操作、环境反馈和手术意图四个层面，评估 1 秒、3 秒和 8 秒生成轨迹的合理性。 | [[📝 论文与方案](https://arxiv.org/abs/2511.01775)] `仅论文` |

### 模拟器

| 模拟器 | 医学状态 | 推演接口 | 获取方式 |
|---|---|---|---|
| **OSS-DBS v2** | 脑电场与受刺激的神经通路 | 根据电极与组织模型计算刺激相关电场及神经反应；属于生物物理规划工具，尚非经过验证的临床结局模拟器。 | [[💻 代码](https://github.com/SFB-ELAINE/OSS-DBSv2)] [[📝 论文](https://www.medrxiv.org/content/10.64898/2026.10.10.26365197v1)] |
| **Cosmos-H-Dreams** | 手术视频与机器人状态 | 流式生成动作条件下的视频片段，将生成观测返回机器人策略以进行交互式闭环推演；已发布服务代码与模型权重。 | [[💻 代码](https://github.com/isaac-for-healthcare/Cosmos-H-Dreams)] [[🌐 权重](https://huggingface.co/nvidia/Cosmos-H-Dreams)] [[📝 论文](https://arxiv.org/abs/2608.24199)] |
| **Lung CT Monte Carlo Workflow** | 患者特异性胸部组织中的光输运 | 在 CT 重建的肺部解剖中传播光子，模拟不同照明与组织条件下的三维光通量；仅用于剂量学，未预测纵向疾病或治疗反应。 | [[💻 代码](https://github.com/JohanDiazTovar/Monte-Carlo-Modeling-of-Light-Propagation-in-Healthy-and-Diseased-Human-Lungs)] [[📝 论文](https://doi.org/10.1073/pnas.2612370123)] [[📝 PubMed](https://pubmed.ncbi.nlm.nih.gov/42574619/)] |
| **Cosmos-H-Surgical-Simulator** | 手术场景与机器人状态 | 根据初始帧及机器人运动学动作序列，跨多种具身形态生成未来手术视频。 | [[💻 代码](https://github.com/NVIDIA-Medtech/Cosmos-H-Surgical-Simulator)] [[🌐 权重](https://huggingface.co/nvidia/Cosmos-H-Surgical-Simulator)] |
| **HemoPIC** | 脑血流动力学 | 拟合患者特异性的示踪剂输运，通过物理知情数字孪生推演灌注动力学；提供可运行的演示。 | [[💻 代码与演示](https://github.com/jhuldr/HemoPIC)] [[📝 论文](https://arxiv.org/abs/2607.08799)] |
| **MeWM** | 肝脏肿瘤状态 | 合成治疗条件下的干预后肿瘤状态，用于 TACE 规划及生存分析。 | [[💻 代码](https://github.com/scott-yjyang/MeWM)] [[🌐 项目](https://yijun-yang.github.io/MeWM/)] |
| **SepsisAgent Clinical World Model** | ICU 患者状态 | 在候选补液与升压药干预下，模拟患者反事实轨迹。 | [[💻 代码](https://github.com/FreedomIntelligence/SepsisAgent)] [[📝 论文](https://arxiv.org/abs/2605.14723)] |
| **Brain-WM** | 胶质母细胞瘤与纵向 MRI | 将治疗规划与治疗条件下的未来 MRI 生成结合，用于疾病进展模拟。 | [[💻 代码](https://github.com/thibault-wch/Brain-GBM-world-model)] [[📝 论文](https://arxiv.org/abs/2603.07562)] |

<a id="-related-repositories"></a>

### 🔗 相关仓库

- **Awesome-Self-Evolving-AI-for-Agentic-Healthcare**
  [[💻 仓库](https://github.com/ZhihaoPENG-CityU/Awesome-Self-Evolving-AI-for-Agentic-Healthcare)]

- **knightnemo/Awesome-World-Models**
  [[💻 仓库](https://github.com/knightnemo/Awesome-World-Models)]

- **LMD0311/Awesome-World-Model**
  [[💻 仓库](https://github.com/LMD0311/Awesome-World-Model)]

<a id="industry-models-platforms"></a>

### 🏭 产业模型与平台

- (*NVIDIA'25*) **Cosmos World Foundation Model**
  [[🌐 平台](https://docs.nvidia.com/cosmos/index.html)] [[📝 研究](https://research.nvidia.com/labs/dir/cosmos1/)]
  > 通用世界基础模型平台，通过 **Cosmos-H-Surgical** 与 **Cosmos-H-Surgical-Simulator** 扩展至手术模拟，相关论文见[手术模拟与医疗具身智能](#surgical-simulation-and-embodied-healthcare)。

- (*NVIDIA'25*) **Holoscan AI Platform**
  [[🌐 平台](https://docs.nvidia.com/holoscan/sdk-user-guide/index.html)]
  > 面向手术机器人与医疗设备集成的实时 AI 推理平台，可支持基于世界模型的术中决策。

- (*Siemens Healthineers'25*) **Digital Twin for Healthcare**
  [[🌐 平台](https://www.siemens-healthineers.com/digital-health)]
  > 面向患者个体的数字孪生技术，用于心脏建模、放疗计划与临床决策支持。

- (*OpenAI'26*) **GPT-Rosalind**
  [[📝 博客](https://openai.com/index/introducing-gpt-rosalind/)] [[🌐 生命科学](https://openai.com/solutions/industries/life-sciences/)] [[🔗 申请访问](https://openai.com/form/life-sciences-access/)] [[💻 Codex 插件](https://github.com/openai/plugins/tree/main/plugins/life-science-research)]

---

<a id="-special-issues--calls"></a>

## 📣 专刊与征稿

### 2026

- **IEEE Transactions on Medical Imaging 专刊：医学影像中的大型多模态模型与世界模型**
  [[🌐 征稿](https://ieeetmi.org/special-issue-world-model/)]

---

<a id="project-information"></a>

## 📋 项目信息

<a id="-license"></a>

### ⚖️ 许可证

本仓库的内容与代码分别采用不同许可证：

- **目录内容（[CC BY 4.0](LICENSE-CONTENT)）**：`README.md` 及本中文版本、`CONTRIBUTING.md`、`CITATION.cff`、拉取请求与议题模板，以及 `assets/` 中的原创材料，包括分类体系、元数据、注释与收录依据。
- **代码（[MIT](LICENSE)）**：`scripts/` 与 `tests/` 中的源码、`.github/workflows/` 中的自动化流程，以及 `.lychee.toml` 等仓库配置。

所链接或引用的论文、代码仓库、数据集、商标及其他第三方材料，仍保留各自的权利与许可证；本仓库的收录不会改变其许可。

上述内容／代码许可划分适用于本修订及后续贡献。较早的仓库版本继续遵循各自版本中附带的许可声明。

<a id="-citation"></a>

### 📖 引用

如果本目录对您的研究有所帮助，请使用 [CITATION.cff](CITATION.cff) 中的信息引用本仓库。GitHub 的 **Cite this repository** 功能也提供可直接使用的 APA 与 BibTeX 格式。

<a id="-contributing"></a>

### 🤝 参与贡献

欢迎贡献。推荐论文或资源前，请先阅读[贡献指南](CONTRIBUTING.md)。主目录论文提案必须依据原始来源，说明建模状态、转移动力学、推演能力与医学任务。您可以提交拉取请求，或[通过结构化议题表单推荐论文](https://github.com/chengwang96/Awesome-World-Models-for-Healthcare/issues/new?template=01-paper-suggestion.yml)。

条目格式（英文主目录使用以下统一格式）：

```markdown
- (*Venue'YY*) **Paper Title**
  [[📝 Paper](link)] [[💻 Code](link)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate + Plan` · `Assets: Code`
  <details>
  <summary>Why it qualifies</summary>
  <p>Learns intervention-conditioned patient-state transitions and uses rollouts to compare treatment plans.</p>
  </details>
```

拉取请求模板包含所需的收录范围证据与核查清单。概念性工作应放在综述与观点部分；静态表征学习、普通条件生成、仅提出基准的工作及其他不符合收录条件的方法，不计入主目录。

<a id="-contact-us"></a>

### ✉️ 联系我们

如有问题或建议，欢迎通过以下方式联系我们：

**邮箱：** chengwang@link.cuhk.edu.hk, zhihaopeng@cuhk.edu.hk

---

<a id="-star-history"></a>

[在 Star History 查看本仓库的星标历史](https://www.star-history.com/?repos=chengwang96%2FAwesome-World-Models-for-Healthcare&type=date&logscale=&legend=bottom-right)。
