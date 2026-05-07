# DevLoop

Kit de workflow para desenvolvimento assistido por IA com foco em:

- execução por slices pequenos
- memória em artefatos versionados
- qualidade verificável antes de commit/release
- retomada rápida após pausas

## Documento principal

- [`SOP.md`](SOP.md)
- Repository laws: [`openspec/project.md`](openspec/project.md)
- OpenSpec compatibility: [`docs/openspec-compatibility.md`](docs/openspec-compatibility.md)
- LLM engineering principles: [`docs/foundations/llm-engineering-principles.md`](docs/foundations/llm-engineering-principles.md)
- How to use DevLoop: [`docs/using-devloop.md`](docs/using-devloop.md)
- Tutorial de uso: [`docs/getting-started.md`](docs/getting-started.md)

## Lifecycle canônico

```text
Proposal → Design → Contract Freeze → Task Planning → Slice Execution → Evidence Report → Reviewer Gate → Archive
```

Templates: [`templates/README.md`](templates/README.md)

## Apêndices

- [`docs/appendices/rigor-by-complexity.md`](docs/appendices/rigor-by-complexity.md)

## Skills

- [`.devloop/skills/README.md`](.devloop/skills/README.md)

## Scripts utilitários

- [`scripts/README.md`](scripts/README.md)
- smoke test: `./scripts/smoke-skills.sh`

## Estrutura canônica

- OpenSpec changes ativos: `openspec/changes/active/`
- OpenSpec changes arquivados: `openspec/changes/archive/`
- Skills canônicos: `.devloop/skills/`
- Compatibilidade temporária: `skills -> .devloop/skills`
- Caminhos deprecated: [`docs/deprecated-paths.md`](docs/deprecated-paths.md)

## Observação

Materiais históricos foram movidos para `archive/`.
