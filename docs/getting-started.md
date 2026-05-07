# Getting Started do DevLoop

Guia prático para responder: **o que rodar e em qual momento**.

## Pré-requisitos

- Git
- Python 3.11+
- Repositório `dev-loop` clonado localmente

Defina um atalho para facilitar os comandos:

```bash
export DEVLOOP_HOME="/caminho/para/dev-loop"
```

---

## Fluxo A — Projeto novo

### 1) Criar repositório/projeto

```bash
mkdir meu-projeto && cd meu-projeto
git init
```

### 2) Bootstrap do SOP

```bash
python3 "$DEVLOOP_HOME/.devloop/skills/core/setup-solopreneur-project/setup_project.py" \
  --project-root . \
  --include-openspec
```

Isso cria estrutura base (`AGENTS.md`, `PROJECT_CONTEXT.md`, `docs/`, `scripts/markdown-*.sh`, `.githooks/pre-commit`, etc.).

### 3) Instalar skills no runtime canônico

```bash
export DEVLOOP_SKILLS="$HOME/.pi/agent/skills"
bash "$DEVLOOP_HOME/.devloop/skills/install_all_skills.sh" "$DEVLOOP_SKILLS"
```

Opcional (compatibilidade com nomes antigos):

```bash
bash "$DEVLOOP_HOME/.devloop/skills/install_all_skills.sh" "$DEVLOOP_SKILLS" --include-legacy
```

> Fonte canônica no DevLoop: `.devloop/skills/`. O caminho `skills/` existe apenas como adapter de compatibilidade. Deprecated: `.pi/skills`, `.codex/skills` e `~/.pi/skills`.

### 4) Ativar hook e validar setup

```bash
git config core.hooksPath .githooks
./scripts/markdown-format.sh
./scripts/markdown-lint.sh
python3 "$DEVLOOP_HOME/.devloop/skills/core/setup-solopreneur-project/setup_project.py" \
  --project-root . \
  --check --format text
```

### 5) Rodar primeiro change piloto

Antes de planejar, leia as leis permanentes em `openspec/project.md`. Para interpretar princípios de engenharia, use `docs/foundations/llm-engineering-principles.md`.

Lifecycle DevLoop/OpenSpec:

```text
Proposal → Design → Contract Freeze → Task Planning → Slice Execution → Evidence Report → Reviewer Gate → Archive
```

1. Classificar risco do change.
2. Criar `proposal.md` usando `templates/openspec/proposal.md`.
3. Criar `design.md` usando `templates/openspec/design.md` quando aplicável.
   QUICK sem `design.md` so para bugfix simples; nos demais casos, incluir `design.md`.
4. Preencher a seção **Contract Freeze** do `design.md` antes de planejar tasks.
5. Criar `tasks.md` usando `templates/openspec/tasks.md`.
6. Planejar 1 slice vertical por vez usando `templates/slices/slice-handoff.md`; cada slice deve herdar o Contract Freeze.
7. Em cada slice, seguir TDD: RED -> GREEN -> REFACTOR preservando `openspec/project.md` e o Contract Freeze.
8. Ao fechar cada slice: validar, atualizar artefatos, commitar, dar push e gerar `implementation-report.md`.
9. Informar `REPORT_PATH=<arquivo.md>`; um reviewer/planner distinto usa `planner-review.md` para aprovar, aprovar com follow-ups ou rejeitar.

---

## Fluxo B — Projeto existente (adoção gradual)

### 1) Diagnóstico sem alterar nada

```bash
python3 "$DEVLOOP_HOME/.devloop/skills/core/setup-solopreneur-project/setup_project.py" \
  --project-root . \
  --check --format json
```

Se faltar estrutura, simule antes:

```bash
python3 "$DEVLOOP_HOME/.devloop/skills/core/setup-solopreneur-project/setup_project.py" \
  --project-root . \
  --dry-run --include-openspec --format text
```

### 2) Aplicar bootstrap incremental

```bash
python3 "$DEVLOOP_HOME/.devloop/skills/core/setup-solopreneur-project/setup_project.py" \
  --project-root . \
  --include-openspec
```

### 3) Ajustar AGENTS.md para a stack real

Revise principalmente:

- comandos de teste/lint/type-check/build
- DoD
- anti-patterns específicos do projeto

### 4) Instalar skills e ativar hook

```bash
export DEVLOOP_SKILLS="$HOME/.pi/agent/skills"
bash "$DEVLOOP_HOME/.devloop/skills/install_all_skills.sh" "$DEVLOOP_SKILLS"
git config core.hooksPath .githooks
```

### 5) Pilotar em 1 change real pequeno

Adote o DevLoop em um change de baixo risco primeiro. Depois expanda para todo o time/projeto.

---

## Template recomendado para cada slice

Use o template em `templates/slices/slice-handoff.md` para planejar execucao por LLM com contexto zero.

Minimo esperado por slice:
- escopo enxuto (poucos arquivos, so o necessario)
- Contract Freeze herdado de `design.md`
- handoff + prompt pronto de execucao
- criterios de sucesso e gates de autoavaliacao
- relatorio final diff-oriented em arquivo markdown temporario
- reviewer/planner gate separado da implementação

---

## O que rodar em cada momento

| Momento | Comando sugerido | Objetivo |
|---|---|---|
| Antes de abrir change | `python3 "$DEVLOOP_SKILLS/classify-change-risk/classify_risk.py" "<descrição>" --format markdown` | Definir risco e nível de rigor |
| Antes de implementar | validar artefatos do change (`proposal.md`, `design.md` com Contract Freeze, `tasks.md`) + preencher `templates/slices/slice-handoff.md` | Evitar QUICK indevido e preparar handoff para LLM contexto zero |
| Ao preparar change FEATURE/HIGH | `python3 "$DEVLOOP_SKILLS/suggest-adr/suggest_adr.py" --project-root . --fail-on recommendation` | Sinalizar necessidade de ADR |
| Durante cada slice | comandos de teste/lint do `AGENTS.md` em um fluxo vertical + ciclo TDD RED->GREEN->REFACTOR | Garantir qualidade incremental e aderência a `openspec/project.md` |
| Antes de commit | `python3 "$DEVLOOP_SKILLS/validate-agents/validate_agents.py" --project-root . --staged --fail-on medium` | Evitar anti-patterns críticos |
| Fechamento de slice | `git commit -m "<tipo>: <slice>"` + `git push origin <branch>` + gerar relatorio em `.tmp`/`/tmp` | Registrar evidencia remota e preparar avaliacao do planner |
| Handoff para planner | implementador imprime `REPORT_PATH=<arquivo-temporario.md>`; reviewer distinto usa `templates/reports/planner-review.md` | Permitir aprovação/rejeição objetiva do slice |
| Antes de archivar change | `python3 "$DEVLOOP_SKILLS/changelog-updater/update_changelog.py" --project-root . --dry-run --fail-on empty` | Verificar evidência de mudança |
| Pré-release | `python3 "$DEVLOOP_SKILLS/release-evidence-pack-generator/generate_release_pack.py" --project-root . --version vX.Y.Z --dry-run --fail-on missing-any` | Garantir pacote mínimo de evidências |
| Rotina periódica (mensal) | `python3 "$DEVLOOP_SKILLS/refactor-sprint-suggester/suggest_refactor_sprint.py" --project-root . --fail-on high` | Mapear dívida técnica prioritária |

> Convenção de exit code dos scripts: `0=ok`, `1=erro de execução`, `2=policy/gate violado`.

---

## Atalhos úteis

- Convenções de CLI: `docs/cli-conventions.md`
- Fluxo macro do processo: `SOP.md`
- Leis permanentes: `openspec/project.md`
- Princípios para agentes LLM: `docs/foundations/llm-engineering-principles.md`
- Catálogo de skills: `.devloop/skills/README.md`
- Smoke test do kit (para mantenedores): `./scripts/smoke-skills.sh`
