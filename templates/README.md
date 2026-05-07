# Workflow Templates

Este diretório contém templates reutilizáveis para bootstrap de projetos no DevLoop.

## DevLoop / OpenSpec Lifecycle

Lifecycle canônico:

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

Templates canônicos:

- `openspec/proposal.md`
- `openspec/design.md` — inclui seção **Contract Freeze**
- `openspec/tasks.md`
- `slices/slice-handoff.md` — handoff conciso; slices herdam Contract Freeze, fronteiras, escopo, plano TDD e gates
- `reports/implementation-report.md` — diff-oriented evidence from implementation agent
- `reports/planner-review.md` — approval/rejection by separate reviewer/planner agent

## Evidence / Reviewer Gate

- Implementation agent produces the implementation report and stops.
- Reviewer/planner agent evaluates report + diff and records Approved / Approved with follow-ups / Rejected.
- Archive is allowed only after reviewer/planner approval.

Keep reports concise and operational.

## Markdown Automation

- `markdown-automation/README.md`
- `markdown-automation/install.sh`
- `markdown-automation/markdown-format.sh`
- `markdown-automation/markdown-lint.sh`
- `markdown-automation/pre-commit`
- `markdown-automation/.markdownlintignore`

## CI

- `ci/github-actions-markdown.yml`

## Compatibility

- `slices/slice-handoff-template.md` permanece como template antigo/compatível.
- Preferir `slices/slice-handoff.md` para novos changes.
