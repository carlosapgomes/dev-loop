# DevLoop Prompt Playbooks

Use these prompts to make LLM sessions follow DevLoop reliably.

They are for human-operated sessions with a reasoning model. Copy the relevant prompt from `templates/prompts/` into the LLM, then provide your project/feature context.

## Why These Prompts Exist

DevLoop relies on phases and artifacts. Generic prompts often cause agents to skip discovery, invent architecture, or mix planning with implementation.

Prompt playbooks give the agent:

- a clear role
- the current lifecycle phase
- what to read
- what to produce
- when to stop

## Recommended Flow

### New Project

1. Discovery conversation:
   - `templates/prompts/new-project-discovery.md`
2. After approving the summary, generate artifacts:
   - `templates/prompts/new-project-artifacts.md`
3. Review generated files before saving.
4. Execute the first slice with:
   - `templates/prompts/execute-slice.md`
5. Review the slice with:
   - `templates/prompts/review-slice.md`

### New Feature in Existing Project

1. Discovery conversation:
   - `templates/prompts/new-feature-discovery.md`
2. After approving the summary, generate change artifacts:
   - `templates/prompts/new-feature-artifacts.md`
3. Review generated files before saving.
4. Execute each slice with:
   - `templates/prompts/execute-slice.md`
5. Review each slice with:
   - `templates/prompts/review-slice.md`

### Unsure Which Prompt to Use

Start with:

- `templates/prompts/devloop-planner-router.md`

The router chooses the right prompt/playbook.

## Prompt Index

- `devloop-planner-router.md`: use when unsure where to start; outputs recommended mode and next prompt.
- `new-project-discovery.md`: use for a project idea; outputs planning summary, risks, and open questions.
- `new-project-artifacts.md`: use after discovery approval; outputs initial DevLoop/OpenSpec files.
- `new-feature-discovery.md`: use for a feature/change; outputs feature summary, risk, and change id.
- `new-feature-artifacts.md`: use after feature discovery approval; outputs OpenSpec change and first slice.
- `execute-slice.md`: use when a slice handoff exists; outputs implementation and `REPORT_PATH`.
- `review-slice.md`: use when implementation report exists; outputs approval/rejection and review report.

## Important Rules

- Discovery prompts do not create files.
- Artifact prompts do not implement code.
- Implementation prompts do not approve work.
- Reviewer prompts do not implement code.
- Slices must inherit `design.md#contract-freeze`.
- Keep prompts and outputs concise.
- Every Markdown artifact created or edited by planner, implementer, or reviewer must pass `markdownlint-cli2` before delivery or commit.

## Example: New Feature

Paste `templates/prompts/new-feature-discovery.md`, then add:

```text
Feature idea: allow users to export invoices as CSV from the billing screen.
```

After the LLM returns `READY_TO_GENERATE_ARTIFACTS=yes`, paste `templates/prompts/new-feature-artifacts.md` and ask it to generate the files.

## Example: New Project

Paste `templates/prompts/new-project-discovery.md`, then describe the project idea.

After discovery is approved, paste `templates/prompts/new-project-artifacts.md` to generate:

- `PROJECT_CONTEXT.md`
- `AGENTS.md`
- `openspec/project.md`
- first active change
- first slice handoff

## Where These Fit

Prompt playbooks are not a replacement for DevLoop templates. They help a reasoning LLM produce and use those templates correctly.

Templates remain canonical under:

```text
templates/
```
