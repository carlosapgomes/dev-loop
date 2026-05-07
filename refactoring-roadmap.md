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

## Target Workflow ✅

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

## Guiding Principles ✅

Canonical interpretation lives in:

`docs/foundations/llm-engineering-principles.md`

Traditional software engineering principles are interpreted for LLM workflows as entropy/context controls, not generic slogans.

---

## Phase 1 — Structural Stabilization ✅

### Phase 1 Goal

Remove path drift and structural inconsistencies.

### Phase 1 Implemented

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

## Phase 2 — Lifecycle Formalization ✅

### Phase 2 Implemented

Canonical templates created:

- `templates/openspec/proposal.md`
- `templates/openspec/design.md`
- `templates/openspec/tasks.md`
- `templates/slices/slice-handoff.md`
- `templates/reports/implementation-report.md`
- `templates/reports/planner-review.md`

Lifecycle documented in `SOP.md`, `README.md`, `docs/getting-started.md`, and `templates/README.md`.

---

## Phase 3 — Contract Freeze System 🟡

### Phase 3 Implemented

- Contract Freeze section added to `templates/openspec/design.md`
- Slice handoffs inherit `design.md#contract-freeze`
- AGENTS/templates reference frozen contracts

### Phase 3 Still Manual

- No validator yet checks Contract Freeze completeness
- No automation blocks tasks/slices if contracts are missing
- No forbidden-file enforcement yet

### Phase 3 Recommended Next Step

Implement Phase 9 validators for Contract Freeze presence and slice inheritance.

---

## Phase 4 — Repository Laws ✅

### Phase 4 Implemented

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

## Phase 5 — Slice Handoff Hardening ✅

### Phase 5 Implemented

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

## Phase 6 — Evidence & Reviewer Gate ✅

### Phase 6 Implemented

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

## Phase 7 — Engineering Philosophy Consolidation ✅

### Phase 7 Implemented

Created:

- `docs/foundations/llm-engineering-principles.md`

AGENTS/templates reference the canonical doc instead of duplicating principle explanations.

---

## Phase 8 — OpenSpec Synchronization Strategy ✅

### Phase 8 Implemented

Created:

- `docs/openspec-compatibility.md`

Defined:

- supported OpenSpec baseline: `@fission-ai/openspec` 1.2.x
- DevLoop extensions
- compatibility boundaries
- upstream sync strategy
- upgrade process

---

## Phase 9A — DevLoop Upgrade Assistant ✅

### Phase 9A Goal

Help existing projects migrate from older DevLoop structures to DevLoop v2 safely.

### Phase 9A Implemented

Created:

- `.devloop/skills/core/devloop-upgrader/`

The upgrader supports:

- `--check`
- `--plan`
- `--apply-safe`
- backups for replaced markdown automation scripts
- manual warnings for risky active-change changes

Safety rule: detect much, apply little, never rewrite active planning artifacts silently.

---

## Phase 9B — Automation & Validation ✅

### Phase 9B Goal

Reduce manual enforcement for lifecycle artifacts.

### Phase 9B Implemented

Extended `.devloop/skills/core/artifacts-consistency-checker/check_consistency.py` with lightweight lifecycle governance checks:

1. Contract Freeze presence checks
2. Contract Freeze completeness warnings
3. `tasks.md` Contract Freeze reference checks
4. slice handoff structure checks
5. implementation-report/planner-review pairing warnings
6. forbidden-file diff checks against slice handoffs

### Phase 9B Remaining Future Enhancements

- stricter archive gate validation
- report-to-slice matching by slice id
- optional CI integration
- more precise forbidden-file scoping for selected active slice

---

## Final Goal

DevLoop v2 should function as:

- a low-entropy orchestration system
- for multi-agent software engineering
- using OpenSpec as the lifecycle backbone
- with explicit architectural governance
- and context-zero executable slices.
