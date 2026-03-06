# Skills do DevLoop

Este diretório foi reorganizado por função (e não por origem de modelo).

## Estrutura

```text
skills/
├── core/         # skills executáveis (script + testes)
├── playbooks/    # protocolos/guias (alguns com script auxiliar)
├── domain/       # especializações por stack
├── legacy/       # aliases e compatibilidade temporária
└── install_all_skills.sh
```

## Core (canônicos)

- `setup-solopreneur-project`
- `agents-md-generator`
- `project-context-maintainer`
- `classify-change-risk`
- `quality-gate-executor`
- `adr-generator`
- `artifacts-consistency-checker`

Exemplos:

```bash
python3 skills/core/setup-solopreneur-project/setup_project.py --project-root . --include-openspec
python3 skills/core/classify-change-risk/classify_risk.py "Implementar integração SSO" --format markdown
python3 skills/core/quality-gate-executor/quality_gate.py --format markdown
```

## Playbooks

- `changelog-updater` (já inclui `update_changelog.py`)
- `release-evidence-pack-generator` (já inclui `generate_release_pack.py`)
- `refactor-sprint-suggester` (já inclui `suggest_refactor_sprint.py`)
- `project-resurrection`
- `suggest-adr` (já inclui `suggest_adr.py`)
- `validate-agents` (já inclui `validate_agents.py`)

Exemplos (playbooks com script):

```bash
python3 skills/playbooks/validate-agents/validate_agents.py --project-root . --staged
python3 skills/playbooks/changelog-updater/update_changelog.py --project-root . --dry-run
python3 skills/playbooks/release-evidence-pack-generator/generate_release_pack.py --project-root . --version v1.0.0 --dry-run
python3 skills/playbooks/suggest-adr/suggest_adr.py --project-root . --auto-create
python3 skills/playbooks/refactor-sprint-suggester/suggest_refactor_sprint.py --project-root . --output docs/refactor-sprint-report.md
```

## Domain

- `django-insights` (já inclui `django_insights.py`)

## Legacy

Aliases e nomes antigos (`esaa-*`) para migração gradual.

## Instalação

Instala core + playbooks + domain:

```bash
bash skills/install_all_skills.sh
```

Instala também aliases legacy:

```bash
bash skills/install_all_skills.sh ~/.pi/agent/skills --include-legacy
```

## Validação rápida

```bash
for t in skills/core/*/tests/test_*.py; do python3 "$t"; done
for t in skills/playbooks/*/tests/test_*.py; do [ -f "$t" ] && python3 "$t"; done
for t in skills/domain/*/tests/test_*.py; do [ -f "$t" ] && python3 "$t"; done
```

## Convenção de CLI

Scripts seguem padrão de flags/exit codes em `docs/cli-conventions.md`.

## Próximo passo recomendado

Executar inventário e decisões de sobreposição em `docs/inventory-skills.md`.
