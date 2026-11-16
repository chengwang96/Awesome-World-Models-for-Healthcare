## Summary

<!-- Briefly describe what this pull request changes. -->

## Change Type

- [ ] Add or update a world-model paper
- [ ] Add or update a survey, repository, platform, or call
- [ ] Fix metadata, links, formatting, or documentation

## Scope Evidence for Paper Additions

<!-- Complete this section for every proposed main-list paper. Use evidence from the primary paper source. -->

- **Medical task:**
- **Modeled state:**
- **Learned state-evolution component:** <!-- Identify the transition, discovered structure, surrogate, residual, or closure; fixed-model parameter fitting alone is insufficient. -->
- **Prediction or rollout use:** <!-- Direct future-state prediction or recursive simulation; explain how the learned component generates the evaluated states. -->
- **Implementation and evaluation evidence:** <!-- Cite sections/tables/figures, training/evaluation separation, and limitations. Separate downstream probes alone are insufficient. -->

## Proposed Metadata

<!-- Use only labels defined in CONTRIBUTING.md. Delete this section when no main-list paper is changed. -->

- **State:**
- **Dynamics:**
- **Capability:**
- **Assets:**

## Primary Links

- **Paper:**
- **Code:**
- **Weights/project page:**

## Checklist

### All Changes

- [ ] I used canonical sources and official author resource links where available.
- [ ] I preserved the repository's existing Markdown style and kept unrelated changes out of this pull request.

### Paper Additions or Updates

<!-- Complete this subsection only when changing a paper entry. -->

- [ ] I read the paper abstract and relevant methods rather than classifying it from the title alone.
- [ ] I confirmed that a learned state-evolution component generates evaluated future or intervention-dependent states, not only static representations, ordinary conditional generation, fixed-simulator calibration/inversion, policy learning, classification, or scalar plan scores.
- [ ] I searched for duplicate titles, arXiv identifiers, and DOIs in the README.
- [ ] I added the full entry to the correct year and concise copies to all applicable **By Topic** sections.
- [ ] The metadata uses only the controlled vocabulary in `CONTRIBUTING.md` and matches the linked assets.
- [ ] The `Why it qualifies` note identifies the modeled state, dynamics, and rollout capability.
