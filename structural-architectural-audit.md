# DevLoop Structural / Architectural Audit

> Audit generated before major refactor. No repository files were modified during the audit phase.

## Executive Summary

DevLoop already contains valuable building blocks, but currently behaves more like a bootstrap/SOP toolkit than a governed LLM-native workflow system.

Highest risks before refactor:

1. OpenSpec layout is not canonicalized.
2. Skills directories compete for authority.
3. `AGENTS.md` / `PROJECT_CONTEXT.md` are assumed as authority but are not governed in this repo.
4. Contract Freeze does not exist as an operational phase.
5. Desired lifecycle is not formalized in templates/gates.
6. Architectural rules are distributed and generic.
7. SOP, templates, generators and skills duplicate instructions.
8. Legacy skills still carry older ESAA terminology and paths.

---

## Findings

### 1. OpenSpec path inconsistencies

There is inconsistency between tools expecting:

- `openspec/changes/active`
- `openspec/changes/archive`

The roadmap target is:

```text
openspec/
  project.md
  specs/
  changes/
    active/
    archive/
```

But the bootstrap currently creates only:

```text
openspec/specs
openspec/changes/archive
```

#### Affected files

- `skills/core/setup-solopreneur-project/setup_project.py`
- `skills/core/setup-solopreneur-project/SKILL.md`
- `skills/core/artifacts-consistency-checker/check_consistency.py`
- `skills/playbooks/project-resurrection/SKILL.md`
- `skills/playbooks/suggest-adr/SKILL.md`
- `skills/playbooks/release-evidence-pack-generator/generate_release_pack.py`
- `scripts/smoke-skills.sh`
- `docs/getting-started.md`
- `SOP.md`
- `refactoring-roadmap.md`

#### Risk level

High

#### Recommendation

Canonicalize immediately:

```text
openspec/changes/active/
openspec/changes/archive/
```

Then update bootstrap, docs, smoke tests, gitignore, and scripts together.

---

### 2. `.gitignore` conflicts with OpenSpec lifecycle

Current repo `.gitignore` is minimal, but bootstrap injects:

```text
openspec/changes/*/
!openspec/changes/archive/
```

This risks ignoring active changes, even though active change artifacts are central to multi-agent coordination.

#### Affected files

- `.gitignore`
- `skills/core/setup-solopreneur-project/setup_project.py`

#### Risk level

High

#### Recommendation

Do not ignore `openspec/changes/active/` if active proposals/tasks/design/contracts must be shared between agents.

Suggested future direction:

```gitignore
tmp/
.tmp/
.pi/
.codex/
__pycache__/
*.py[cod]
```

---

### 3. Skills directory inconsistencies

There are multiple skill paths in use:

```text
skills/                      # source in this repo
.pi/skills                   # project-local install in docs
~/.pi/skills                 # legacy skill docs
~/.pi/agent/skills           # installer default
.codex/skills                # bootstrap creates
```

#### Affected files

- `skills/install_all_skills.sh`
- `docs/getting-started.md`
- `skills/core/setup-solopreneur-project/setup_project.py`
- `skills/README.md`
- `skills/legacy/*/SKILL.md`
- `skills/playbooks/*/SKILL.md`
- `skills/domain/django-insights/SKILL.md`

#### Risk level

High

#### Recommendation

Define a canonical model explicitly:

```text
skills/                  # DevLoop source bundle
.devloop/skills/         # optional project-local vendored skills
~/.pi/agent/skills/      # Pi runtime install target
```

Deprecate unless explicitly supported as adapters:

```text
.pi/skills
.codex/skills
~/.pi/skills
```

---

### 4. `AGENTS.md` authority is assumed but not governed

Many tools depend on root `AGENTS.md`, but the DevLoop repo itself does not currently contain a canonical root `AGENTS.md`.

Generated templates include useful rules, but remain generic.

Missing from canonical AGENTS behavior:

- contract freeze rules
- repository laws
- allowed/forbidden files policy
- lifecycle phase gates
- OpenSpec authority rules
- technical non-goals
- reviewer gate
- contract change approval rule

#### Affected files

- `skills/core/agents-md-generator/generate_agents_md.py`
- `skills/core/setup-solopreneur-project/setup_project.py`
- `skills/core/agents-md-generator/SKILL.md`
- `SOP.md`
- `templates/slices/slice-handoff-template.md`
- `skills/playbooks/validate-agents/*`
- `skills/core/quality-gate-executor/*`

#### Risk level

High

#### Recommendation

Create a DevLoop-level canonical `AGENTS.md` template with permanent laws. Generated project `AGENTS.md` should reference canonical philosophy docs instead of duplicating everything.

---

### 5. `PROJECT_CONTEXT.md` status is inconsistent

`PROJECT_CONTEXT.md` is sometimes treated as required and sometimes recommended.

#### Affected files

- `SOP.md`
- `skills/core/setup-solopreneur-project/SKILL.md`
- `skills/core/setup-solopreneur-project/setup_project.py`
- `skills/core/artifacts-consistency-checker/check_consistency.py`
- `skills/core/project-context-maintainer/*`
- `skills/playbooks/project-resurrection/SKILL.md`

#### Risk level

Medium

#### Recommendation

Recommended canonical split:

```text
openspec/project.md       # permanent project authority / repository laws
PROJECT_CONTEXT.md        # resumable project briefing
AGENTS.md                 # execution rules for agents
```

---

### 6. Missing lifecycle phases

Desired lifecycle:

```text
Proposal
→ Design
→ Contract Freeze
→ Task Planning
→ Slice Execution
→ Evidence Report
→ Reviewer Gate
→ Archive
```

Current lifecycle is closer to:

```text
Risk classification
→ OpenSpec change
→ proposal/design/tasks depending on risk
→ slice execution
→ report path
→ archive
```

Missing or weakly represented:

- explicit Contract Freeze
- contracts template
- reviewer gate
- planner review report template
- implementation report template
- lifecycle completeness validation
- archive readiness criteria
- approval/rejection flow

#### Affected files

- `SOP.md`
- `refactoring-roadmap.md`
- `templates/slices/slice-handoff-template.md`
- `skills/core/artifacts-consistency-checker/check_consistency.py`
- `skills/core/classify-change-risk/*`
- `skills/playbooks/suggest-adr/*`
- `skills/playbooks/release-evidence-pack-generator/*`

#### Risk level

High

#### Recommendation

Add canonical templates:

```text
templates/openspec/proposal.md
templates/openspec/design.md
templates/openspec/contracts.md
templates/openspec/tasks.md
templates/slices/slice-handoff.md
templates/reports/implementation-report.md
templates/reports/planner-review.md
```

---

### 7. Contract Freeze is absent

Contract Freeze is central in the roadmap but absent as a first-class artifact or gate.

Missing:

- frozen DTOs
- public interfaces
- schemas
- invariants
- architectural boundaries
- allowed files
- forbidden files
- non-goals
- approval required for contract changes

#### Affected files

- `refactoring-roadmap.md`
- `SOP.md`
- `templates/slices/slice-handoff-template.md`
- `skills/core/artifacts-consistency-checker/check_consistency.py`
- `skills/core/agents-md-generator/generate_agents_md.py`
- `skills/core/setup-solopreneur-project/setup_project.py`

#### Risk level

Critical

#### Recommendation

Introduce `contracts.md` as a first-class artifact.

Minimum required sections:

```text
# Contract Freeze

## Frozen Interfaces
## DTOs / Schemas
## Invariants
## Architectural Boundaries
## Allowed Files
## Forbidden Files
## Technical Non-goals
## Testing Strategy
## Change Approval Rule
```

Enforce:

```text
No tasks.md before contracts.md for FEATURE/HIGH.
No slice execution before contracts freeze.
Frozen contracts cannot change without reviewer/planner approval.
```

---

### 8. Documentation hierarchy is weak

Current top-level authority is unclear.

Existing docs include:

- `README.md`
- `SOP.md`
- `docs/getting-started.md`
- `docs/inventory-skills.md`
- `docs/migration-map.md`
- `docs/script-backlog.md`
- `docs/cli-conventions.md`
- `refactoring-roadmap.md`

But there is no explicit authority hierarchy.

#### Risk level

Medium

#### Recommendation

Add an authority map, either in `openspec/project.md` or `docs/foundations/documentation-authority.md`.

Suggested hierarchy:

```text
1. openspec/project.md
2. AGENTS.md
3. SOP.md
4. docs/foundations/*
5. templates/*
6. skill docs
7. archive/*
```

---

### 9. Philosophy is distributed and duplicated

Concepts like clean code, TDD, vertical slices, DRY, YAGNI, low coupling, and cohesion appear in many places without centralized interpretation.

#### Affected files

- `SOP.md`
- `skills/core/agents-md-generator/generate_agents_md.py`
- `skills/core/setup-solopreneur-project/setup_project.py`
- `templates/slices/slice-handoff-template.md`
- `skills/core/agents-md-generator/SKILL.md`
- multiple playbook docs

#### Risk level

Medium

#### Recommendation

Create:

```text
docs/foundations/llm-engineering-principles.md
```

This should explain principles through:

- entropy reduction
- context control
- semantic predictability
- probabilistic alignment
- multi-agent coordination

Then replace repeated philosophy blocks with references plus operational constraints.

---

### 10. Legacy skills remain a drift source

`skills/legacy/*` preserves old ESAA names and instructions. This is useful for migration, but many legacy docs still include old install paths, old commands, and old mental models.

#### Affected files

- `skills/legacy/esaa-*`
- `docs/migration-map.md`
- `skills/README.md`

#### Risk level

Medium

#### Recommendation

Keep legacy, but mark as non-authoritative:

```text
Legacy skills are compatibility aliases only.
They must not define lifecycle policy.
Canonical policy lives in SOP / OpenSpec templates / docs/foundations.
```

---

### 11. Reviewer Gate exists conceptually but not structurally

The current system requires implementation report and planner evaluation through `REPORT_PATH`, but no reviewer artifact or formal gate exists.

Missing:

- reviewer checklist
- approval/rejection format
- evidence evaluation standard
- rule that implementation agent and reviewer agent are distinct
- archive blocked until reviewer approval

#### Affected files

- `SOP.md`
- `templates/slices/slice-handoff-template.md`
- `skills/core/agents-md-generator/generate_agents_md.py`
- `skills/core/setup-solopreneur-project/setup_project.py`
- `refactoring-roadmap.md`

#### Risk level

High

#### Recommendation

Add:

```text
templates/reports/planner-review.md
templates/reports/implementation-report.md
```

Make archive require approved review.

---

## Recommended Refactor Order

### 1. Normalize structure first

- OpenSpec layout
- skills canonical paths
- `.gitignore`
- deprecated path markers

### 2. Define documentation authority

Create or clarify:

```text
openspec/project.md
docs/foundations/
docs/adr/
```

Decide precedence among:

```text
AGENTS.md
PROJECT_CONTEXT.md
openspec/project.md
SOP.md
```

### 3. Formalize lifecycle templates

Add templates for:

- proposal
- design
- contracts
- tasks
- slice handoff
- implementation report
- planner review

### 4. Add Contract Freeze rules

Update:

- SOP
- AGENTS template
- setup generator
- consistency checker
- slice template

### 5. Harden slice handoff

Make every slice inherit:

- frozen contracts
- allowed files
- forbidden files
- non-goals
- test strategy
- evidence requirements

### 6. Add Reviewer Gate

Archive should require:

- implementation report
- reviewer/planner review
- tests/gates evidence
- approval status

### 7. Consolidate philosophy

Create:

```text
docs/foundations/llm-engineering-principles.md
```

Then reduce repeated philosophy from templates and generators.

### 8. Update automation

Only after docs/templates are stable:

- lifecycle validator
- contract freeze validator
- forbidden file checker
- archive readiness checker

---

## Architecture Concerns

Main concern: DevLoop currently has multiple partial authorities:

```text
SOP.md
AGENTS.md generator
setup fallback
skills docs
slice template
legacy skills
roadmap
OpenSpec conventions
```

This makes agent behavior probabilistic and drift-prone.

Desired target:

```text
openspec/project.md
openspec/specs/
openspec/changes/active/<change>/
openspec/changes/archive/<change>/
```

DevLoop should extend OpenSpec with:

```text
contracts.md
repository laws
reviewer gate
evidence reports
slice hardening
philosophy consolidation
```

DevLoop should not aggressively fork OpenSpec.

---

## Quick Wins

1. Add `openspec/changes/active` to bootstrap.
2. Stop creating `.codex/skills` by default, or mark it deprecated.
3. Pick one project-local skills path.
4. Update `.gitignore` so OpenSpec changes are not accidentally ignored.
5. Add `contracts.md` template.
6. Add `implementation-report.md` and `planner-review.md` templates.
7. Add explicit authority order to `README.md` or `docs/README.md`.
8. Mark `skills/legacy/*` as compatibility-only and non-authoritative.
9. Update generated AGENTS template with lifecycle gates.
10. Add `docs/foundations/llm-engineering-principles.md` and stop duplicating philosophy everywhere.

---

## Overall Risk

Current refactor readiness: **Medium-Low**

The repository is valuable and salvageable, but a major refactor should not begin until the following are stabilized:

1. OpenSpec directory layout
2. Skills install/runtime strategy
3. Contract Freeze artifact
4. Lifecycle templates
5. Documentation authority model
