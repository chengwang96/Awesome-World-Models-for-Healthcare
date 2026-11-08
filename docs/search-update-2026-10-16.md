# Literature Search Update and Scope Recheck: 2026-10-16

## Starting Point and Search Coverage

- Search date: 2026-10-16, Asia/Hong_Kong. `git fetch origin` and `git pull --ff-only origin main` found no newer remote commit than `eec4d63`. The local, uncommitted 2026-10-13 update already contained twelve papers and its audit; these changes were preserved. This review therefore starts from **153 local main-list entries**, while the remote commit alone still has 141.
- Re-read the README scope, controlled metadata, contribution rules, the main and topic entries, and the prior September/October scope and search audits. Checked candidate titles and identifiers against the current catalog before adding them.
- Queried arXiv by submitted dates 2026-10-12 through 2026-10-16 using broad medical and targeted world-model, digital-twin, biosignal, cell, infection, patient, and simulation terms. The broad query returned 55 records. Queried the bioRxiv and medRxiv date APIs over the same interval (921 and 252 records, respectively), plus targeted Crossref, Europe PMC, and primary paper/code pages. The targeted Europe PMC recent-date queries returned no new matches at search time; PubMed access through the academic-search connector failed because its email was not configured. These are search-interface observations, not evidence that the literature is empty.
- Read primary full text or methods for the promoted papers, including in-memory PDFs where publisher HTML was unavailable. Search counts are query-dependent and not a systematic-review census. Preprint indexing and version dates can lag.

## Scope Applied

Main-list inclusion requires a directly evaluated biomedical/healthcare task, represented state, an implemented **learned or computed** state transition, an operational future prediction/simulation/planning/control use, and evaluation of that use. Autonomous cell, infection, and physiological dynamics may qualify without actions. Treatment and control claims need action-dependent successor states. We use `Plan` only where the paper actually evaluates action selection, and distinguish retrospective factual forecasts, simulations, and causal intervention evidence. A perspective belongs in Survey Papers; a runnable but chiefly software/numerics platform can belong in Simulators without being counted as a validated clinical world-model paper.

## Seven Papers Added to the Main List

**153 → 160 unique local main-list papers.** Each new main entry is mirrored once in the topic index.

| Paper | State transition, evaluation, and limit |
|---|---|
| [SonoWorld](https://arxiv.org/html/2610.19327) | **Include as action-conditioned ultrasound view simulation.** A causal generator advances ultrasound observations under estimated/grounded 6-DoF probe motion. It trains largely from unlabeled video, grounds probe actions with 33 tracked thyroid scans, and evaluates held-out multi-second rollouts and candidate direction ranking. Direction ranking is a limited planning test; no real robot executes a closed-loop target-view search. Its [project page](https://iclr2027anonymous.github.io/SonoWorld/) is live but does not provide released code. |
| [SARS-CoV-2 within-host model](https://www.medrxiv.org/content/10.64898/2026.10.12.26365315v1) | **Include as computed physiological dynamics.** ODE states couple virus, epithelial cells and innate/adaptive responses. A seronegative wildtype human-challenge cohort calibrates viral kinetics; a separate seropositive Delta challenge checks the predicted direction of pre-existing-antibody effects. Immunodeficiency and vaccination scenarios are simulated hypotheses, not trial-validated policy effects. |
| [scMTG](https://www.biorxiv.org/content/10.64898/2026.06.04.730241v2) | **Include as learned cell-state transitions.** An autoencoder and adjacent-time generative Markov kernels map sampled cells forward; kernels can be composed. Tests on six time-series datasets reconstruct held-out intermediate cell distributions and compare with other trajectory methods. This v2 was posted in the search window; the initial preprint is from June. Inferred gene networks and trajectories do not establish causal perturbation effects. [Code](https://github.com/liuq-lab/scMTG). |
| [FERMAT](https://www.medrxiv.org/content/10.64898/2026.10.11.26365210v1) | **Include as autoregressive clinical-event simulation.** The model recursively generates event tokens and inter-event time from patient history; evaluation uses 3.77 million single-hospital records, next-record event prediction, and sampled five-year disease-risk trajectories. Generation gives higher next-record Recall@10 than representation readouts, while representation-based risk predictors outperform generated estimates on the reported five-year tasks. No action-conditioned or externally validated treatment model is shown. |
| [PatientWM](https://arxiv.org/html/2610.17059) | **Include as action-conditioned patient-state dynamics.** A latent state advances under an ordered record of clinical actions, with factual recursive rollouts and EHR forecasting across MIMIC and external cohorts. Its action-ranking test chooses among a narrow retrospective candidate set, including no update and the patient's earlier actions. Neither unobserved counterfactual trajectories nor clinical benefit are verified. |
| [μODE](https://www.biorxiv.org/content/10.64898/2026.10.09.758137v1) | **Include as computed microbial-community dynamics.** Dynamic flux-balance models and extracellular-metabolite ODEs update organisms and metabolites under antibiotic exposure or donor transfer. Longitudinal FMT comparisons support the direction of pathobiont suppression, but detailed community composition remains biased and no patient-level efficacy or causal donor-choice benefit is demonstrated. [Code](https://github.com/cumbof/muODE). |
| [Tissue time machine for tuberculosis granulomas](https://www.biorxiv.org/content/10.64898/2026.10.09.758083v1) | **Include as mechanistic infection-state simulation.** GranSim advances immune cells and bacterial load, and an observed nonhuman-primate granuloma is matched to virtual trajectories from a large run library. Historical granuloma data support aggregate simulator behavior. The reported 22/28 figure is **agreement among selected virtual partners** about a projected week-22 outcome; the 28 harvested tissues cannot supply their own later ground truth, so 22/28 is not prospective prediction accuracy. |

### Scope Recheck

All seven represent a medical or biomedical state and actually advance it: SonoWorld changes an ultrasound view under probe motion; PatientWM and FERMAT roll clinical states/events forward; scMTG propagates cell distributions; μODE, GranSim, and the SARS-CoV-2 ODE compute infection/ecological/immune dynamics. Each reports an evaluation of the transition or its operational output. `PatientWM` and `SonoWorld` receive `Plan` only for bounded action-ranking uses, with their limits stated in the entries. Only the SARS-CoV-2 study checks a specific mechanistic prediction against a separate human challenge cohort; none of these entries establishes clinical treatment benefit.

## Adjacent Items Kept Outside the Main List

- [Rethinking World Models for Biosignals](https://arxiv.org/abs/2610.17510) is a perspective proposing an intervention-effect validation checklist. It was added to **Survey Papers**, not the implemented-model list.
- [OSS-DBS v2](https://www.medrxiv.org/content/10.64898/2026.10.10.26365197v1) exposes a [runnable, open-source DBS simulator](https://github.com/SFB-ELAINE/OSS-DBSv2) for electrode fields and stimulated axonal responses. The paper reports numerical convergence and a pathway-activation optimization use case; its symptom-response objective relies on assumed target-pathway effects, without validating improved patient outcomes. It was added to **Simulators** only. The code README calls this a development version awaiting its first official release.

## Recent Candidates Not Promoted

| Candidate | Decision and reason |
|---|---|
| [Simulating Alzheimer's amyloid-like pathology on a fly central nervous system connectome](https://arxiv.org/abs/2610.19153) | **Hold.** A large spiking connectome runs after imposed amyloid-like lesion rules and simulates behavior, but the lesion locations/magnitudes and disease-behavior responses have no diseased-fly measurements; healthy-model agreement does not validate the pathological transition. This may be revisited as a mechanistic-model entry if relevant disease-state evidence appears. |
| [World model for longitudinal health trajectories in older adults](https://doi.org/10.2139/ssrn.7497619) | **Hold for methods access.** The September abstract describes an action-conditioned JEPA and open-loop aging trajectories, but SSRN full text/PDF access returned 403, preventing a transition/evaluation audit. |
| [Ventriculoperitoneal shunt digital twin](https://arxiv.org/abs/2610.20074) | **Exclude.** CT-derived ventricular geometry supports a static insertion-path optimization; no medical state is propagated through time or procedure actions. |
| [CardioFAD](https://arxiv.org/abs/2610.19050) | **Exclude from main list.** ECG/image-conditioned keyframes and interpolation synthesize a cine sequence; the inspected method does not expose and evaluate a reusable successor-state transition from the generated cardiac state. |
| [Graph-Enhanced Disease Trajectory](https://arxiv.org/abs/2610.20502) and [companion motif study](https://arxiv.org/abs/2610.20512) | **Exclude.** Admission motifs and sequence encoders support endpoint prediction or motif novelty, without executing a patient-state rollout. |
| [CloneOT](https://arxiv.org/abs/2610.16093) | **Exclude.** A lineage-supervised perturbation map estimates before/after endpoints, without a tested temporal rollout. |
| [CAP-DIR](https://arxiv.org/abs/2610.18926) | **Exclude.** It registers already observed images; it does not forecast later anatomy. |
| [Panvascular-JEPA](https://www.biorxiv.org/content/10.64898/2026.10.12.758273v1) | **Exclude.** The evaluated transition benchmark is a synthetic six-node vascular graph, without a demonstrated patient or clinical dynamics task. |
| [Hippocampal digital twin in bats](https://www.biorxiv.org/content/10.64898/2026.10.09.758148v1) | **Exclude.** The reported healthy-bat neural/behavioral task lacks direct medical or biomedical-disease evaluation. |
| [Virtual Brain schizophrenia study](https://www.biorxiv.org/content/10.64898/2026.10.13.758782v1) | **Hold.** Fits a whole-brain model to observed functional imaging and relates parameters to symptoms; the inspected use is parameter/biomarker analysis rather than an evaluated future-state or intervention rollout. |

The audit is a methods-level catalog decision, not a reproduction of authors' experiments. Preprints and software may change after the search date.

## Verification

- `python scripts/validate_catalog.py`: passed with 160 main-list papers, 160 unique topic entries, and synchronized paper-suggestion form.
- `python -m unittest discover -s tests -v`: all 13 tests passed.
- `git diff --check`: passed.
- Targeted GET checks returned HTTP 200 for all seven new main-paper links, the survey and simulator paper links, three new code links, and the SonoWorld project page. This was a targeted check, not a repository-wide link sweep.
