# Literature Search Update and Scope Recheck: 2026-09-08

## Basis and Coverage

- Search date: 2026-09-08, Asia/Hong_Kong; publication cutoff: the same date.
- Baseline: `983289c`, 127 main-list papers. `git pull --ff-only origin main` reported that the checkout was already current.
- Re-read the README scope, main catalog, taxonomy and resources, CONTRIBUTING.md, and the [2026-09-07 scope audit](scope-audit-2026-09-07.md).
- Prioritized recent August-September releases, then backfilled relevant 2026 papers and checked related 2025 methods. Search results were deduplicated against the catalog by identifiers and titles.
- Discovery used indexed arXiv, PubMed/publisher pages, author repositories, and the [DT4H 2026 accepted-paper list](https://digitaltwinforhealthcare.com/workshops/2026). Decisions below use primary methods or implementation documentation, not secondary summaries.
- This was a targeted update, not an exhaustive systematic review. The academic PubMed connector lacked its required email configuration, the arXiv connector failed with an SSL error, and direct requests encountered connection/proxy failures. Public web search remained usable; no complete database export was obtained. OpenReview verification also prevented access to several full texts.

Representative query families included medical/surgical/patient world models, intervention-conditioned simulation, clinical digital twins, tumor-growth surrogates, physiological simulation, and exact candidate titles. Searches included September 2026 and August 2026 terms, recent-date filters, and unfiltered searches to catch earlier omissions. Publication and revision dates were checked separately from search-engine crawl dates.

## Inclusion Rule and Scope Ambiguity

Apply the existing five-part rule: **biomedical task, medical system state, executable transitions, operational rollout, and implemented evaluation**. A temporal input, physics equation, digital-twin label, or plausible counterfactual picture alone is insufficient.

The README and CONTRIBUTING.md permit **learned or computed** dynamics and broadly biomedical tasks. The initial pass applied that wording and added two papers. On recheck against the requested **strict medical world model** focus, that was too permissive: an operational mechanistic simulator is not automatically a learned world model, and physiological signal simulation does not automatically demonstrate a specific medical application.

This recheck conservatively withdraws both proposed core entries. It does not claim that both fail the literal five-part wording, redefine all mechanistic models as invalid, or impose clinical trials as an inclusion requirement. The broader written criteria and the narrower requested focus remain a catalog-wide consistency issue; resolving it requires a separate audit of existing entries, including the mechanistic papers identified in the [previous audit](scope-audit-2026-09-07.md#mechanistic-simulators).

## Recheck Decisions

**Final result: zero new main-list papers; 129 -> 127 after withdrawing the two initial additions. Relative to baseline, the main catalog remains 127. One new perspective remains under Survey Papers and is not counted as a world-model method.**

| Paper / family | Verified method and evaluation | Recheck decision and primary evidence |
|---|---|---|
| Cortical GNN-pHNN; learned physiological dynamics | Learns EEG phase/frequency dynamics and autonomously rolls out held-out initial states. Evaluation measures signal invariants, not a disease, treatment, or medical-BCI task. | **Hold outside core.** Genuine learned dynamics; specific medical-task grounding remains insufficient for this stricter pass. [Full text, v3](https://arxiv.org/html/2607.10439v3), Sections III.7, V.1 and VI.4. |
| Multiphase PDE tumor therapy scheduling; mechanistic simulator | COMSOL integrates treatment-dependent tissue dynamics; Bayesian optimization compares schedules. The GP approximates schedule-to-objective values, not the transition operator. | **Withdraw from core; related mechanistic simulation only.** The medical task and rollout are real, but the implemented learning is objective optimization, not a learned world model. [Full text, v1](https://arxiv.org/html/2607.20782v1), Sections 2, 3.1-3.3 and 4. |
| Structural Requirements for Intelligent Clinical Digital Twins in Feedback-Driven Care; perspective | Discusses decision-dependent data, temporal states and alternative care strategies; no implemented dynamics model. | **Retain only in Survey Papers.** [Publisher](https://www.nature.com/articles/s44401-026-00143-7) labels it a Perspective, published 2026-09-02. |

For Cortical GNN-pHNN, failed spectral/DFA tests are validation limits, **not the scope-exclusion rule**. General physiological dynamics can fit the broad biomedical wording. The reason for holding this candidate is the narrower medical-task boundary, not absence of rollout, lack of action conditioning, or lack of a clinical trial. The [author repository](https://github.com/mindverse-computing/Classical-Virtual-Mind) identifies its disease/control suites as synthetic and some as unreproducible; they do not resolve that boundary.

Neither withdrawn paper is moved automatically into the simulator-resource table: that section has its own access and implementation criteria. No additional candidate is promoted merely to preserve the initial addition count.

## Not Promoted to the Main Catalog

| Candidate | Evidence examined | Decision |
|---|---|---|
| Simulation-driven diabetes proof of concept | [Full text](https://arxiv.org/html/2605.11247v1), Sections 4.8, 5.2-5.5 and 6. | Exclude. Static scikit-learn regression and classification are evaluated; smooth synthetic meal/exercise response curves are illustrative. OhioT1DM traces are shown descriptively, not used to validate an intervention-conditioned transition model. |
| Maternal-fetal PI-DT for preeclampsia | [Full text](https://journals.sagepub.com/doi/10.3233/SHTI260193), Sections 2.2 and 3; online 2026-08-27. | Exclude. Evaluated outputs are fitted RI/PFR indices and spatial flow illustrations, not time-resolved trajectories or action-dependent evolution. A time derivative in the governing equation does not establish an operational rollout. |
| Operational digital twin clinics | [Original manuscript](https://arxiv.org/pdf/2608.21416), policy evaluation and Methods, pp. 12 and 17-23. | Keep outside the core list in this update. Isaac Sim supports genuine closed-loop contact behavior, but the evaluated screen-touch and handle-contact proxies do not establish medical-device operation, patient interaction or physiological dynamics. This is not dismissed as static reconstruction. |
| ECMO digital twin for VR training | [Publisher](https://doi.org/10.1093/icvts/ivag047); [accepted manuscript copy](https://iperfusion.org/wp-content/uploads/2026/02/ivag047.pdf), Sections 2.3-2.4, 3.2-3.3 and Tables 1-5. | Hold. Device-setting-to-output and output-to-vital mappings are deployed and evaluated in VR. Recurrent horizon prediction is mentioned, but the reported main results do not establish a recurrent patient-state rollout. Supplementary temporal evaluation is needed before promotion. |
| FreamerV1 / Filter Before Mixing | [Full text](https://www.preprints.org/manuscript/202605.0736), Section 5 and Appendices C and I. | Hold. RSSM imagination is implemented, so this is not rejected as a non-world-model. The health example uses PAMAP2 activities and heuristic rewards; the grounding of intervention actions in physiological response data and the medical task need clearer evidence. |
| Efficient Deep Learning-based Forward Solvers for Brain Tumor Growth Models | [Full text, v2](https://arxiv.org/html/2501.08226v2), Sections 2-3. | Exclude from the core list. Predicts a tumor-concentration field from anatomy and growth parameters; the evaluation does not advance an observed tumor state through a sequence. Do not infer temporal rollout from the source PDE alone. |
| TERRA | [Author repository](https://github.com/Lotfollahi-lab/terra), method summary and citation section; [author model card](https://huggingface.co/lotfollahi-lab/TERRA-96M). | Do not add. The documented method predicts masked gene-token embeddings and supports spatial representation/perturbation analyses, without demonstrated cellular-state rollout. The repository still describes the manuscript as in preparation; a DOI found in secondary coverage was not verified and is not cited here. |
| Brain Tumor Growth Inversion via Differentiable Neural Surrogates | [MIDL 2026 record](https://proceedings.mlr.press/v315/weidner26a.html) and [author repository](https://github.com/jonasw247/brain-tumor-growth-inversion-via-differentiable-neural-surrogates). | Hold. Publication identity and inverse-calibration implementation are confirmed, but the full manuscript was not successfully retrieved in this pass. Determine whether evaluation goes beyond reconstructing terminal concentration fields before inclusion. |

## Workshop Leads Awaiting Full Text

The [official DT4H list](https://digitaltwinforhealthcare.com/workshops/2026) contains 32 accepted papers. Acceptance is not a scope decision, and listed titles alone do not justify adding them. The following unlisted candidates merit methods-level follow-up; **none is counted as an addition**:

- Rapid Electrophysiology Simulation and Inverse Optimization based on Multi-Task Surrogate Modeling for Cardiac Digital Twins.
- PPIM: Pennes Physics-Informed Mamba for Heat-Source-Conditioned 3D Bioheat Simulation.
- Modeling Progression of Microwave Ablation Volumes by Neural Surrogates.
- Learning Temperature-Dependent Properties in Cryoablation with Differentiable Physics.
- From Treatment Choices to Tumour Trajectories: Proof-of-Concept in Preference-Aware Agentic Simulation for Digital Twins.
- Observation-Anchored Selective Assimilation for Longitudinal Tumor-State Proxy Forecasting in Post-Treatment Glioma.
- Cohort-Level Twinning in an Agent-Based Model of Metastatic Tumor Growth.

Check state initialization, temporal/action conditioning, rollout protocol and evaluation in the manuscripts before promoting any lead. The two inaccessible cardiac papers in the [previous audit](scope-audit-2026-09-07.md#pending-full-text-verification) also remain pending; this update does not resolve them.

## Changes and Verification

- Removed both initially added main entries and their matching topic entries after the stricter recheck.
- Retained one new perspective under Survey Papers and recorded four README boundary cases, including the two withdrawn candidates.
- Preserved existing papers, taxonomy, resource tables and historical audit records.
- This recheck covers this update's two proposed methods and one perspective, not all 127 baseline papers. Other search decisions and pending leads above remain unchanged.
- Scope decisions concern reported methods, not independent experimental reproduction or demonstrated clinical safety.
- `python scripts/validate_catalog.py`: passed after recheck, 127 main-list papers and 127 unique topic entries.
- `python -m unittest discover -s tests -v`: all 10 tests passed after recheck.
- `git diff --check`: passed after recheck.
- Linked primary pages were opened during review; a complete local Lychee/CI network run was not performed.
