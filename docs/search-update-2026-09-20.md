# Literature Search Update and Scope Recheck: 2026-09-20

## Basis and Coverage

- Search date and cutoff: 2026-09-20, Asia/Hong_Kong.
- Baseline: `7eaf6cb`, 127 main-list papers and 15 survey entries. `git pull --ff-only origin main` reported that the checkout was already current; the existing local commit was preserved.
- Re-read the README scope, main catalog, taxonomy, topic indexes and resources, CONTRIBUTING.md, and the [previous search recheck](search-update-2026-09-08.md). Deduplicated candidates by title, arXiv identifier and DOI.
- Prioritized September publications and revisions, with August overlap and exact-title follow-up of previously pending workshop papers. Searches also covered learned clinical dynamics, model-based reinforcement learning, neural surrogates and perturbation models that do not call themselves world models.
- Discovery combined web search, arXiv, PubMed, Crossref, publisher records, author implementations, and official MICCAI workshop programs. Secondary coverage was used only to find primary sources.
- The academic PubMed connector lacked its email configuration. Direct public NCBI E-utilities queries succeeded and supplied bibliographic records and abstracts. The direct arXiv API also succeeded. Some publisher/OpenReview pages remained inaccessible; those limits are distinguished from negative scope findings below.

Two reproducible database queries supplemented the broader targeted searches:

```text
PubMed, 19 returned records:
("world model"[Title/Abstract] OR "world models"[Title/Abstract])
AND ("2026/08/01"[Date - Publication] : "2026/09/20"[Date - Publication])

arXiv, 5 returned records:
all:"world model"
AND (all:medical OR all:clinical OR all:healthcare OR all:patient
     OR all:surgical OR all:biomedical OR all:cell)
AND submittedDate:[202609010000 TO 202609192359]
```

These are query-specific counts, not a count of qualifying papers or a claim of exhaustive coverage. PubMed issue dates can differ from first-online dates; arXiv initial submission, revision and announcement dates were kept separate. This is a targeted catalog update, not a systematic review.

## Applied Scope

For new core additions, require a specific medical/biomedical task, a modeled system state, learned or hybrid state dynamics, an executed forecast/simulation from that state, and evaluated implementation. A name, governing equation, temporal encoder, treatment-effect score, or recurrent layer alone is insufficient.

Apply the stricter interpretation established in the previous recheck. Ordinary mechanistic simulation is not automatically a learned world model. A general model must demonstrate the relevant capability in a medical task; results from unrelated control or physics tasks cannot be transferred to its clinical branch by implication. Autonomous physiological dynamics do not require actions, and clinical trials are not an inclusion prerequisite.

The broader "learns or computes" wording and older mechanistic entries are unchanged. This update does not resolve the catalog-wide consistency issue documented in the previous audit or reclassify all 127 existing papers.

## New Core Papers

**Two new methods: 127 -> 129 main-list papers.**

| Method | Publication | Scope evidence and limits |
|---|---|---|
| DPWM | Frontiers in Medicine, 2026-09-17; DOI `10.3389/fmed.2026.1913206`. | Learned patient-state dynamics, explicit intervention inputs and multi-step prior sampling support preoperative strategy ranking. MIMIC-IV, eICU-CRD and VitalDB evaluation is retrospective. Concordance with observed care does not identify treatment effects. [Full text](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2026.1913206/full), Sections 4.1-4.6 and 5. |
| ProteinTalks | Nature, 2026-09-09; DOI `10.1038/s41586-026-11001-9`; PMID `42717098`. | Learns proteomic state evolution under drug perturbations for cancer drug-response tasks. Future proteomes, not only phenotype labels, are training targets. Limited to the demonstrated perturbation-trajectory use; no sequential treatment policy or proven clinical benefit is claimed. [Publisher record](https://www.nature.com/articles/s41586-026-11001-9), [PubMed abstract](https://pubmed.ncbi.nlm.nih.gov/42717098/), and implementation below. |

### Implementation Cross-Check

- **DPWM:** the paper-linked [repository](https://github.com/ustive/Beyond-Static-Risk-Scores-Dynamic-World-Models) contains `integration/rssm.py`, `ensemble/world_model.py` and `objective/loss.py` under `src/stormglass/`. `imagine` advances the state without future observations; `_imagine_probs` feeds each predicted state into the next transition; `counterfactual` repeats this over candidate action sequences. Next-observation and reconstruction losses train the dynamics. These files were inspected, not executed on clinical data.
- **ProteinTalks:** the publisher-linked [repository](https://github.com/guomics-lab/PTV-1) contains [model documentation](https://github.com/guomics-lab/PTV-1/blob/main/ProteinTalks/README.md), [the model](https://github.com/guomics-lab/PTV-1/blob/main/ProteinTalks/model.py), `dataset.py` and `trainer.py`. `ppODE` initializes from baseline expression and a perturbation descriptor, numerically integrates a learned vector field, decodes future proteomes corresponding to 6/24/48 hours, and passes the predicted trajectory to a phenotype head. Training includes future-proteome MSE as well as phenotype BCE. This is not merely a neural-ODE encoder for static classification. Full publisher HTML was not retrievable; the primary abstract, public figure descriptions and author implementation support the scoped inclusion. Experiments were not independently reproduced.

DPWM receives `Simulate + Plan`, without claiming validated causal counterfactual effects. ProteinTalks receives `Forecast + Simulate`, not `Plan` or `Control`. Both entries link official code; unverified weight usability is not asserted. Their matching topic entries were added without increasing the unique-paper count a second time.

## Reviews and Existing-Paper Update

**Two new reviews: 15 -> 17 Survey Papers. Neither is counted as a core method.**

| Review | Identity and placement |
|---|---|
| World Models for Biomedicine | Ayush Noori, Nic Fishman, Ada Fang, Lukas Fesser and Marinka Zitnik; Cell 189(19), 5845-5869, 2026-09-17. [DOI](https://doi.org/10.1016/j.cell.2026.08.032), [PMID 42753693](https://pubmed.ncbi.nlm.nih.gov/42753693/). NCBI labels it a Review. It discusses intervention-aware biomedical simulation rather than reporting a new implemented model. It is distinct from the existing Wang et al. preprint, [Towards World Models in Biomedical Research](https://arxiv.org/abs/2606.05925). |
| A World Model of the Virtual Cell | Eric P. Xing and Le Song; Cell 189(19), 5831-5844, 2026-09-17. [DOI](https://doi.org/10.1016/j.cell.2026.08.042), [PMID 42753692](https://pubmed.ncbi.nlm.nih.gov/42753692/). NCBI labels it a Review. Its proposed stateful, intervention-aware virtual-cell architecture belongs in Survey Papers, not the implemented-model count. An [author preprint page](https://genbio.ai/world-model-of-the-virtual-cell/) predates the journal publication. |

Review identity, date and article type were verified through NCBI records; Crossref independently confirmed the Noori et al. title, authors and DOI. The inaccessible Cell full texts were not represented as read end to end.

**CLARITY is an update, not a new paper.** Its [arXiv record](https://arxiv.org/abs/2512.08029) now identifies ECCV 2026 acceptance, corroborated by the [official repository](https://github.com/DingTianxingjian/CLARITY) and [project page](https://dingtianxingjian.github.io/clarity-project-page/). Moved the existing entry from the 2025 preprint section to 2026, added code/project links, and synchronized its topic entry. Retained the same arXiv identifier and existing capability labels. Initial submission was 2025-12-08; the current v3 is dated 2026-07-06, so this is not a newly submitted September method.

## Recent Candidates Not Promoted

| Candidate | Decision and primary evidence |
|---|---|
| MedDream, `2609.07719` | **Exclude from core.** [Full text](https://arxiv.org/html/2609.07719v1) explicitly distinguishes examination-level radiographic state from longitudinal patient dynamics. Diagnosis and report-conditioned image generation do not implement the required state progression. This is different from the already cataloged medDreamer. |
| JEPA-Anything, `2609.20800` | **Hold outside core.** [Full text](https://arxiv.org/html/2609.20800v1), Sections 3.2-3.4, distinguishes terminal clinical/cellular readouts from recursive control/physics/molecular rollouts. The clinical branch predicts one future latent then event risks; the cancer experiment nominates an intervention from factors. Generic molecular trajectory fidelity, including paracetamol, does not demonstrate pharmacological-response simulation. This is not a claim that the framework lacks world-model dynamics in other domains. |
| Immune World Model, `2609.14709` | **Hold.** [Full text](https://arxiv.org/html/2609.14709v1), Results and Discussion, implements intervention-conditioned next-state prediction and describes bounded composition. Quantitative dynamic tests are one-step; the illustrative cell-to-tissue-to-patient path is cross-scale propagation. Unseen simultaneous perturbation-pair prediction is not evidence of recursively advancing a biological state. Cohort-level recursive validation remains future work. Do not label the model static or the nominated therapy experimentally validated. |
| Arti-JEPA, `2609.09757`, v2 | **Hold.** [Full text](https://arxiv.org/html/2609.09757v2), Sections 5-7 and Appendix E. Clinical speech tasks use representation probes. The appendix genuinely implements autoregressive MRI-latent prediction, but the audio-shuffle diagnostic reports negligible conditioning dependence; medical use of that rollout is not established. Neither the negative result alone nor a blanket assertion of absent dynamics is the exclusion rule. |
| CTX / Ataraxis Tau lead, `2609.13567` | **Exclude from core.** [Full text](https://arxiv.org/html/2609.13567v1), Sections 2.2 and 4, combines baseline pathology/clinical representations with counterfactual regression and treatment-specific survival heads. This is medical treatment-effect prediction, not a patient-state transition simulator. The company platform label does not change the evaluated method. |
| PPIM, `2609.06869` | **Do not promote the previously pending lead.** [Full text](https://arxiv.org/html/2609.06869v1), Sections 2-4, is now accessible. A coordinate/heat-source-conditioned neural PDE solver is evaluated against a final 600-second temperature field under one controlled bioheat setting. Mamba hidden-state recurrence is not evidence of restarting an evolving tissue state or executing ablation plans. This is a neural solver, not an ordinary numerical solver, but the required operational medical rollout is unestablished. |

These decisions concern the inspected versions and our narrow catalog scope, not the overall scientific quality of the work. Six concise boundary records were added to the README.

## Leads Still Awaiting Evidence

- The [Medical World Model Workshop program](https://mwm2026.github.io/) lists **MedWorld-Lite: A Missingness-Aware Personalized World Model for ICU Physiological Forecasting** and **ICUWorld-QR: A Residual Latent World Model for Hourly ICU Physiology**. Exact-title searches did not locate their primary manuscripts in this pass. Titles and acceptance alone are insufficient.
- The [DT4H 2026 program](https://digitaltwinforhealthcare.com/workshops/2026) still lists promising cardiac and thermal-ablation surrogates. PPIM was resolved above; the other previously pending titles are not promoted without their methods and rollout protocols.
- [SepDreamer](https://github.com/rubboligabriele/SepDreamer) exposes a medical model-based RL implementation, but its README still marks the thesis link as coming soon. Retain it as a paper-search lead rather than inventing publication metadata or counting an unpublished thesis as a newly verified article.

## Verification

### Second-Pass Scope Review

Rechecked on 2026-09-20 after the user's request. **Retain both new core entries: 129 main-list papers.** This judgment uses the repository's explicit inclusion of equivalent learned dynamics models and biomedical drug-discovery tasks, not the model names or journal prestige. It does not equate every virtual cell or neural ODE with a world model.

| Item | Recheck decision | Evidence that matters |
|---|---|---|
| DPWM | **Keep in core.** | Patient latent state is advanced by an action-conditioned learned transition. The [implementation](https://github.com/ustive/Beyond-Static-Risk-Scores-Dynamic-World-Models/blob/main/src/stormglass/integration/rssm.py#L102-L109) samples the prior without future observations; the [rollout loop](https://github.com/ustive/Beyond-Static-Risk-Scores-Dynamic-World-Models/blob/main/src/stormglass/ensemble/world_model.py#L97-L129) propagates predictions across an intervention sequence. Its use is retrospective preoperative strategy comparison, not proven treatment benefit. |
| ProteinTalks | **Keep in core as a task-specific biomedical dynamics model.** | The [data loader](https://github.com/guomics-lab/PTV-1/blob/main/ProteinTalks/dataset.py#L82-L123) separates baseline inputs from future proteomic targets. The [model](https://github.com/guomics-lab/PTV-1/blob/main/ProteinTalks/model.py#L94-L176) integrates a learned latent vector field before decoding future states, which feed the drug-response head. The [trainer](https://github.com/guomics-lab/PTV-1/blob/main/ProteinTalks/trainer.py#L118-L134) directly supervises those states, rather than only a terminal phenotype. |
| World Models for Biomedicine | **Survey only.** | Re-fetched NCBI record `42753693`: Review; its abstract develops a biomedical simulation research agenda, not a newly implemented model. |
| A World Model of the Virtual Cell | **Survey only.** | Re-fetched NCBI record `42753692`: Review; proposed architecture, training and evaluation principles, not evidence of a new executable cell simulator. |
| CLARITY | **Keep the existing core entry; no new-paper count.** | The [v3 methods](https://arxiv.org/html/2512.08029v3), Sections 3.5-3.7, train therapy-conditioned MRI-latent transitions against follow-up states and recursively compose them for treatment exploration. This is distinct from only predicting survival from baseline. |

ProteinTalks needs a precise boundary: the [authors' institutional explanation](https://en.westlake.edu.cn/news_events/westlakenews/research/202609/t20260918_69874.html) identifies baseline proteomes and drug targets as dynamics inputs. The inspected implementation conditions the initial latent on a specified perturbation and advances it on a fixed latent integration grid; the three output positions correspond to 6/24/48-hour targets. It does not implement changing a treatment midway through that rollout, arbitrary clinical-time integration, a general-purpose cell digital twin, or closed-loop treatment planning. The README qualification was narrowed accordingly; `Forecast + Simulate` remains appropriate.

ProteinTalks also has a [2025 bioRxiv precursor](https://doi.org/10.1101/2025.02.07.637070), *A perturbation proteomics-based foundation model for virtual cell construction*. Crossref confirms the model name, authors and identifier. Neither that identifier nor the earlier title is already in the baseline catalog. This is one new catalog entry using the September 2026 journal version, not a claim that the model first appeared in September or an additional preprint entry.

Source-version fingerprints from the public GitHub Contents API: DPWM `rssm.py` blob `b6615492e3c25dac7549c29fdd40c9b5bcef336c`, `world_model.py` blob `a9422e9c62802ae84fe00cadbe63ba4a9521cc45`; ProteinTalks `model.py` blob `ad38dc28bf0a60466332dbb19a6d0451a218ec7f`, `dataset.py` blob `6bc86637683bab227f9ba99b7e04016cea73b4b1`, `trainer.py` blob `6bcf1949236ba52b3e2b8b83d873db8b4a28cdc0`. These are inspected source blobs, not reproduced experiments. Nature full HTML remained unavailable; NCBI, Crossref, public publisher descriptions and official implementation were cross-checked. No new evidence was obtained to promote the six previously held/excluded candidates.

### Catalog Checks

- `python scripts/validate_catalog.py`: passed; 129 main-list papers, 129 unique topic entries, and a synchronized paper-suggestion form.
- `python -m unittest discover -s tests -v`: all 10 tests passed.
- Whitespace checks found no errors in the README diff or this new record. The final diff was reviewed for duplicate identifiers, year placement and topic synchronization; the survey section contains 17 entries.
- Changes are limited to `README.md` and this record. The existing local commit was preserved; this update has not been committed or pushed.
- A complete Lychee network-health run was not performed. Bibliographic and method verification does not imply that every publisher URL is accessible to an automated checker. No clinical experiments or external training code were run.
