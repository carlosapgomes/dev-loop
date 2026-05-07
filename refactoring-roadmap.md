# DevLoop v2 Refactor Roadmap

## Status

Core prepared prompts have been executed through Phase 8.

Legend:

- ✅ implemented
- 🟡 partially implemented / manual enforcement remains
- ⏭️ future work

## Vision

Transform DevLoop from:

- a bootstrap/project-template toolkit

into:

- a governance system for low-drift LLM-native software engineering.

DevLoop should:

- minimize probabilistic drift
- minimize architectural entropy
- support context-zero slice execution
- preserve architectural coherence across multi-agent workflows
- integrate OpenSpec as the canonical lifecycle backbone

---

# Target Workflow ✅

Proposal
→ Design
→ Contract Freeze
→ Task Planning
→ Slice Execution
→ Evidence Report
→ Reviewer Gate
→ Archive

Canonical templates live in `templates/`.

---

# Guiding Principles ✅

Canonical interpretation lives in:

`docs/foundations/llm-engineering-principles.md`

Traditional software engineering principles are interpreted for LLM workflows as entropy/context controls, not generic slogans.

---

# Phase 1 — Structural Stabilization ✅

## Goal

Remove path drift and structural inconsistencies.

## Implemented

- Normalized OpenSpec directory layout
- Standardized skills source strategy
- Fixed `.gitignore` to avoid hidden active changes
- Marked deprecated structures explicitly
- Preserved compatibility adapter for `skills/`

## Current Canonical Structure

```text
openspec/
  project.md
  specs/
  changes/
    active/
    archive/

.devloop/
  skills/

templates/
  openspec/
  slices/
  reports/

docs/
  adr/
  foundations/
```

Decision: `templates/` remains at repository root for now. `.devloop/templates` and `.devloop/adapters` were not introduced to avoid unnecessary churn.

---

# Phase 2 — Lifecycle Formalization ✅

## Implemented

Canonical templates created:

- `templates/openspec/proposal.md`
- `templates/openspec/design.md`
- `templates/openspec/tasks.md`
- `templates/slices/slice-handoff.md`
- `templates/reports/implementation-report.md`
- `templates/reports/planner-review.md`

Lifecycle documented in `SOP.md`, `README.md`, `docs/getting-started.md`, and `templates/README.md`.

---

# Phase 3 — Contract Freeze System 🟡

## Implemented

- Contract Freeze section added to `templates/openspec/design.md`
- Slice handoffs inherit `design.md#contract-freeze`
- AGENTS/templates reference frozen contracts

## Still Manual

- No validator yet checks Contract Freeze completeness
- No automation blocks tasks/slices if contracts are missing
- No forbidden-file enforcement yet

## Recommended Next Step

Implement Phase 9 validators for Contract Freeze presence and slice inheritance.

---

# Phase 4 — Repository Laws ✅

## Implemented

Created:

- `openspec/project.md`
- `PROJECT_CONTEXT.md`

Defined:

- architectural boundaries
- dependency rules
- layering constraints
- testing expectations
- engineering principle references
- current architecture decisions

---

# Phase 5 — Slice Handoff Hardening ✅

## Implemented

Slice handoff now requires:

- inherited frozen contracts
- architectural boundaries
- allowed files
- forbidden files
- explicit non-goals
- TDD plan
- success criteria
- required gates
- required evidence report

Primary template:

- `templates/slices/slice-handoff.md`

---

# Phase 6 — Evidence & Reviewer Gate ✅

## Implemented

Formalized:

- implementation reports
- planner review reports
- follow-up recommendations
- approval/rejection flow
- conceptual separation between implementation agent and reviewer/planner agent

Templates:

- `templates/reports/implementation-report.md`
- `templates/reports/planner-review.md`

---

# Phase 7 — Engineering Philosophy Consolidation ✅

## Implemented

Created:

- `docs/foundations/llm-engineering-principles.md`

AGENTS/templates reference the canonical doc instead of duplicating principle explanations.

---

# Phase 8 — OpenSpec Synchronization Strategy ✅

## Implemented

Created:

- `docs/openspec-compatibility.md`

Defined:

- supported OpenSpec baseline: `@fission-ai/openspec` 1.2.x
- DevLoop extensions
- compatibility boundaries
- upstream sync strategy
- upgrade process

---

# Phase 9 — Automation & Validation ⏭️

## Goal

Reduce manual enforcement.

## Recommended Future Tasks

1. Validate lifecycle completeness
2. Detect missing Contract Freeze sections
3. Validate slice handoff structure
4. Ensure implementation reports and planner reviews exist
5. Check forbidden file modifications against slice handoff
6. Gate archive based on reports/tests/reviewer approval

## Suggested Implementation Order

1. Extend `artifacts-consistency-checker` with lifecycle checks
2. Add Contract Freeze presence/completeness checks
3. Add slice handoff required-section checks
4. Add evidence/reviewer gate checks
5. Add optional forbidden-file diff checker

---

# Final Goal

DevLoop v2 should function as:

- a low-entropy orchestration system
- for multi-agent software engineering
- using OpenSpec as the lifecycle backbone
- with explicit architectural governance
- and context-zero executable slices.
