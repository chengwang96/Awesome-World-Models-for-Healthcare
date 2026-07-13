# Contributing

Thank you for helping improve Awesome World Models for Healthcare. This list is intentionally strict: relevance to healthcare and use of the phrase "world model" are necessary context, but neither is sufficient for inclusion in the main paper list.

You can contribute with a pull request or use the [structured paper-suggestion form](https://github.com/chengwang96/Awesome-World-Models-for-Healthcare/issues/new?template=01-paper-suggestion.yml) if you prefer not to edit the catalog directly.

## What Belongs in the Main List

A paper must satisfy all five [strict inclusion criteria](README.md#strict-inclusion-criteria):

1. **Medical grounding:** the modeled system and evaluated task are biomedical, clinical, or healthcare-related.
2. **State:** the method represents a patient, organ, physiological process, medical image, procedure, cell, molecule, or population state.
3. **Dynamics:** it learns or computes transitions between states across time, space, procedure steps, views, or interventions.
4. **Operational rollout:** it supports forecasting, simulation, counterfactual intervention, planning, or control.
5. **Implemented evidence:** the paper implements and evaluates the dynamics or simulator.

Action conditioning is optional for autonomous physiological processes. It is required when a paper claims that the model can evaluate treatments, interventions, or control actions.

The following do not belong in the main list by themselves:

- static representation learning or masked-feature prediction
- ordinary conditional generation without state transitions
- synthetic-cohort generation without longitudinal dynamics
- static risk prediction with manually altered covariates
- benchmark-only or dataset-only contributions without an implemented simulator
- surveys, perspectives, and conceptual frameworks

Surveys and position papers may be proposed for **Survey Papers**. Useful near-scope work may be documented as a boundary case instead of being counted as a world-model paper.

## Before Opening a Pull Request

- Read the abstract and methods in the primary paper source; do not classify from the title alone.
- Search the README for the title, arXiv identifier, and DOI to avoid duplicates.
- Prefer canonical links from the publisher, arXiv, OpenReview, PubMed, bioRxiv, or medRxiv.
- Link only official author code, weights, and project pages.
- Confirm the publication year and venue status, including workshop, preprint, rejected, or withdrawn status when relevant.
- Keep unrelated formatting or repository changes out of a paper-submission pull request.

## Required Paper Format

Add a full entry to the appropriate year under **World Model Papers**:

```markdown
- (*Venue'YY*) **Paper Title**
  [[📝 Paper](https://example.org/paper)] [[💻 Code](https://github.com/org/repo)]
  **Metadata:** `State: Patient` · `Dynamics: Temporal + Action-conditioned` · `Capability: Simulate + Plan` · `Assets: Code`
  > **Why it qualifies:** Learns intervention-conditioned patient-state transitions and uses rollouts to compare treatment plans.
```

Add the same title and links, without metadata or the qualification note, to every applicable subsection under **By Topic**.

## Controlled Metadata

Use only the labels below. Choose the smallest set directly demonstrated by the method.

| Field | Allowed values |
|---|---|
| **State** | `Patient`, `Physiology`, `Anatomy`, `Medical image`, `Procedure/Robot`, `Clinical workflow`, `Cell`, `Molecule`, `Population` |
| **Dynamics** | `Temporal`, `Action-conditioned`, `Mechanistic`, `Spatial/view`, `Event sequence` |
| **Capability** | `Forecast`, `Simulate`, `Counterfactual`, `Plan`, `Control` |
| **Assets** | `Code`, `Weights`, `Project`, `Paper only` |

Metadata definitions:

- **State** is the primary medical or biological state advanced by the model.
- **Dynamics** describes the implemented transition structure, not the input modality.
- **Capability** records what evaluated rollouts accomplish, not suggested future applications.
- **Assets** must match the public links in the entry.

## Writing the Qualification Note

The `Why it qualifies` sentence should name three things concretely:

1. the state being modeled
2. the transition or dynamics mechanism
3. the rollout capability or downstream use

Avoid circular explanations such as "it qualifies because it is a medical world model." Keep the note factual and short enough to verify against the abstract or methods.

## Pull Request Review

The pull request template asks for source-grounded scope evidence. Maintainers may request clarification, revise metadata, move a conceptual paper to Survey Papers, or record a rejected submission as a boundary case. These decisions keep the list useful and do not assess the general quality of the paper.

Before opening a pull request, run the same catalog check used by CI:

```bash
python scripts/validate_catalog.py
```

The validator checks controlled metadata, qualification notes, annual placement, duplicate titles and identifiers, asset labels, links, synchronization between the main list and **By Topic**, and taxonomy consistency in the paper-suggestion form.
