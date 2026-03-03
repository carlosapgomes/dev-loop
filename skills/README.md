# Skills Bundle Completo (asaa-gpt/skills)

Este diretorio consolida todos os skills disponiveis nos pacotes comparados:

- Fonte 1: `esaa-deepseek/skills` (com scripts Python executaveis)
- Fonte 2: `esaa-k2.5/skills` (foco em SKILL.md/protocolo operacional)

## Estrutura

```text
skills/
├── deepseek/
│   ├── adr-generator/
│   ├── agents-md-generator/
│   ├── artifacts-consistency-checker/
│   ├── changelog-updater/
│   ├── classify-change-risk/
│   ├── project-context-maintainer/
│   ├── quality-gate-executor/
│   ├── refactor-sprint-suggester/
│   ├── release-evidence-pack-generator/
│   └── setup-solopreneur-project/
├── k2.5/
│   ├── esaa-classify-risk/
│   ├── esaa-django-insights/
│   ├── esaa-generate-agents/
│   ├── esaa-generate-context/
│   ├── esaa-project-resurrection/
│   ├── esaa-suggest-adr/
│   └── esaa-validate-agents/
└── install_all_skills.sh
```

## Skills executaveis agora (scripts Python)

Use diretamente:

1. `deepseek/setup-solopreneur-project/setup_project.py`
2. `deepseek/agents-md-generator/generate_agents_md.py`
3. `deepseek/project-context-maintainer/maintain_project_context.py`
4. `deepseek/classify-change-risk/classify_risk.py`
5. `deepseek/quality-gate-executor/quality_gate.py`
6. `deepseek/adr-generator/adr_generator.py`
7. `deepseek/artifacts-consistency-checker/check_consistency.py`

Exemplos:

```bash
python3 asaa-gpt/skills/deepseek/setup-solopreneur-project/setup_project.py --project-root . --include-openspec
python3 asaa-gpt/skills/deepseek/classify-change-risk/classify_risk.py "Implementar autenticacao SSO" --format markdown
python3 asaa-gpt/skills/deepseek/quality-gate-executor/quality_gate.py --format markdown
python3 asaa-gpt/skills/deepseek/artifacts-consistency-checker/check_consistency.py --root . --format markdown
```

## Skills de protocolo (usaveis via SKILL.md)

Os skills em `k2.5/` sao detalhados e usaveis como protocolo de trabalho, mesmo sem script pronto no pacote:

- `esaa-classify-risk`
- `esaa-django-insights`
- `esaa-generate-agents`
- `esaa-generate-context`
- `esaa-project-resurrection`
- `esaa-suggest-adr`
- `esaa-validate-agents`

## Instalacao em lote (Pi.dev)

```bash
bash asaa-gpt/skills/install_all_skills.sh
```

Destino padrao:
- `~/.pi/agent/skills`

Destino customizado:

```bash
bash asaa-gpt/skills/install_all_skills.sh /caminho/customizado/skills
```

## Validacao rapida

```bash
for t in asaa-gpt/skills/deepseek/*/tests/test_*.py; do python3 "$t"; done
```

## Documentos de workflow e tutoriais

- `asaa-gpt/workflow-hibrido-completo-skills-tutoriais-v2.md`
- `asaa-gpt/workflow-hibrido-recomendado-v1.md`
- `asaa-gpt/workflow-hibrido-checklist-executavel-1-pagina.md`
