# Using DevLoop

DevLoop is both a bootstrap toolkit and a workflow governance system for LLM-assisted projects.

Use it to start projects with versioned workflow artifacts, skills, templates, OpenSpec structure, repository laws, and context-zero slice execution.

## What DevLoop Provides

DevLoop includes:

- bootstrap script for new/existing projects
- installable skills for Pi agents
- OpenSpec-compatible project/change structure
- lifecycle templates
- repository laws
- engineering principles for LLM agents
- slice handoff templates
- implementation/reviewer report templates

It is not a replacement for OpenSpec. DevLoop extends OpenSpec with governance artifacts.

## Canonical Lifecycle

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

## Bootstrap a New Project

From the DevLoop repository:

```bash
export DEVLOOP_HOME="/path/to/dev-loop"
```

Create a new project:

```bash
mkdir my-project
cd my-project
git init
```

Run bootstrap:

```bash
python3 "$DEVLOOP_HOME/.devloop/skills/core/setup-solopreneur-project/setup_project.py" \
  --project-root . \
  --include-openspec
```

This creates the baseline structure:

```text
AGENTS.md
PROJECT_CONTEXT.md
openspec/project.md
openspec/specs/
openspec/changes/active/
openspec/changes/archive/
docs/
scripts/
tests/
.githooks/
```

## Install Skills

Install skills into the Pi runtime:

```bash
bash "$DEVLOOP_HOME/.devloop/skills/install_all_skills.sh"
```

Default target:

```text
~/.pi/agent/skills
```

Optional legacy aliases:

```bash
bash "$DEVLOOP_HOME/.devloop/skills/install_all_skills.sh" ~/.pi/agent/skills --include-legacy
```

## Validate Setup

Inside the target project:

```bash
python3 "$DEVLOOP_HOME/.devloop/skills/core/setup-solopreneur-project/setup_project.py" \
  --project-root . \
  --check --format text
```

If hooks were created:

```bash
git config core.hooksPath .githooks
```

## Start a Change

Create an active OpenSpec change under:

```text
openspec/changes/active/<change-id>/
```

Use these templates:

```text
templates/openspec/proposal.md
templates/openspec/design.md
templates/openspec/tasks.md
```

For FEATURE/HIGH changes, `design.md` must include the Contract Freeze section.

## Contract Freeze

The Contract Freeze is the execution contract for agents.

It defines:

- frozen interfaces
- DTOs/schemas/payloads
- invariants
- architectural boundaries
- allowed files
- forbidden files
- technical non-goals
- testing strategy

Slices inherit this instead of reinventing architecture.

## Execute a Slice

Use:

```text
templates/slices/slice-handoff.md
```

A slice should contain only the minimum context required to execute one vertical outcome:

- frozen contracts
- architectural boundaries
- allowed/forbidden files
- non-goals
- TDD plan
- gates
- success criteria
- evidence report requirement

The implementation agent must stop after the slice and return:

```text
REPORT_PATH=<path-to-report.md>
```

## Review a Slice

Implementation and review are separate roles.

Implementation agent uses:

```text
templates/reports/implementation-report.md
```

Reviewer/planner agent uses:

```text
templates/reports/planner-review.md
```

Review decision:

- Approved
- Approved with follow-ups
- Rejected

Archive should only happen after reviewer/planner approval.

## OpenSpec vs DevLoop

OpenSpec provides the upstream lifecycle backbone.

DevLoop adds:

- Contract Freeze
- repository laws
- slice handoffs
- evidence reports
- reviewer gates
- LLM engineering principles
- skills and bootstrap automation

Compatibility policy lives in:

```text
docs/openspec-compatibility.md
```

## Use with a Reasoning LLM

For guided sessions, use the prompt playbooks:

```text
docs/prompt-playbooks.md
templates/prompts/
```

Recommended entry points:

- new project: `templates/prompts/new-project-discovery.md`
- new feature: `templates/prompts/new-feature-discovery.md`
- unsure where to start: `templates/prompts/devloop-planner-router.md`

## Main Reference Files

Use these when resuming work:

```text
PROJECT_CONTEXT.md
AGENTS.md
SOP.md
openspec/project.md
docs/foundations/llm-engineering-principles.md
docs/openspec-compatibility.md
templates/README.md
docs/prompt-playbooks.md
.devloop/skills/README.md
```

## Current Recommended Next Step

Phase 9: add lightweight validation automation for:

- lifecycle completeness
- Contract Freeze presence
- slice handoff structure
- evidence/report presence
- reviewer gate presence
- forbidden file changes
