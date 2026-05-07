# Migration Map — Nomenclatura e Diretórios

## Projeto

- Nome antigo (interno): `Workflow-Beta`
- Nome alvo: `dev-loop` (marca: **DevLoop**)

## SOP

- Nome antigo: `Workflow Híbrido ...`
- Nome canônico novo: `SOP` (`SOP.md`)

## Skills — Diretórios

Fonte canônica atual: `.devloop/skills/`.

`skills/` permanece como adapter de compatibilidade para usuários e scripts antigos.

| Antigo | Novo canônico |
|---|---|
| `skills/deepseek/adr-generator` | `.devloop/skills/core/adr-generator` |
| `skills/deepseek/agents-md-generator` | `.devloop/skills/core/agents-md-generator` |
| `skills/deepseek/artifacts-consistency-checker` | `.devloop/skills/core/artifacts-consistency-checker` |
| `skills/deepseek/classify-change-risk` | `.devloop/skills/core/classify-change-risk` |
| `skills/deepseek/project-context-maintainer` | `.devloop/skills/core/project-context-maintainer` |
| `skills/deepseek/quality-gate-executor` | `.devloop/skills/core/quality-gate-executor` |
| `skills/deepseek/setup-solopreneur-project` | `.devloop/skills/core/setup-solopreneur-project` |
| `skills/deepseek/changelog-updater` | `.devloop/skills/playbooks/changelog-updater` |
| `skills/deepseek/refactor-sprint-suggester` | `.devloop/skills/playbooks/refactor-sprint-suggester` |
| `skills/deepseek/release-evidence-pack-generator` | `.devloop/skills/playbooks/release-evidence-pack-generator` |
| `skills/k2.5/esaa-project-resurrection` | `.devloop/skills/playbooks/project-resurrection` |
| `skills/k2.5/esaa-suggest-adr` | `.devloop/skills/playbooks/suggest-adr` |
| `skills/k2.5/esaa-validate-agents` | `.devloop/skills/playbooks/validate-agents` |
| `skills/k2.5/esaa-django-insights` | `.devloop/skills/domain/django-insights` |
| `skills/k2.5/esaa-classify-risk` | `.devloop/skills/legacy/esaa-classify-risk` |
| `skills/k2.5/esaa-generate-agents` | `.devloop/skills/legacy/esaa-generate-agents` |
| `skills/k2.5/esaa-generate-context` | `.devloop/skills/legacy/esaa-generate-context` |

## Installer

- `.devloop/skills/install_all_skills.sh` instala por grupos (`core`, `playbooks`, `domain`).
- `skills/install_all_skills.sh` continua funcionando via adapter de compatibilidade.
- Para compatibilidade, usar `--include-legacy`.
