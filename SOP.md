# SOP

Este é o procedimento operacional padrão (SOP) do **DevLoop** (`dev-loop`).

## Princípios

1. IA executa; artefatos em disco preservam contexto.
2. Evidência no Git > intenção no chat.
3. Um change por vez, dividido em slices pequenos e verticais.
4. Um slice vertical = um commit + push.
5. Retomada deve ser possível com baixo tempo de aquecimento.

## Fluxo padrão por change

1. Classificar risco do change (`QUICK`, `FEATURE`, `HIGH/ARCH`).
2. Criar change no OpenSpec.
3. Gerar artefatos mínimos conforme risco.
4. Implementar por slices verticais (TDD Red/Green/Refactor + Stop Rule: validar -> commit -> push -> STOP).
5. Rodar quality gate do change.
6. Arquivar change.
7. Se necessário, gerar evidence pack de release.

## Risco e artefatos

### QUICK (0-1)

- `proposal.md`
- `tasks.md`
- permitido somente para bugfix simples, localizado e reversivel
- sem alteracao estrutural, sem novo contrato externo e sem migracao de dados

### FEATURE (2-3)

- `proposal.md`
- delta specs
- `design.md`
- `tasks.md`
- default para mudancas que nao sejam bugfix simples

### HIGH/ARCH (4+)

- tudo de FEATURE
- ADR
- plano de rollback

Regra de decisao: em caso de duvida entre QUICK e FEATURE, use FEATURE com `design.md`.

## Stop Rule

Após cada slice:

1. confirmar que o slice e vertical (fluxo end-to-end com valor entregue)
2. validar comandos de qualidade
3. atualizar tasks/artefatos
4. commitar com mensagem rastreavel
5. dar push da branch
6. parar e decidir conscientemente o próximo slice
7. nao continuar sem confirmacao explicita

Regra anti-pattern: nao fazer slice horizontal por camada (ex.: "so backend", "so frontend", "so banco") sem entregar fluxo vertical completo.

## Contrato de planejamento de slice (obrigatorio)

Todo slice deve ser planejado para execucao por **LLM com contexto zero**.

Checklist obrigatorio do slice:

1. objetivo vertical claro (valor end-to-end)
2. escopo enxuto: tocar poucos arquivos, apenas o necessario (se ampliar escopo, justificar)
3. handoff funcional e de negocio no proprio arquivo do slice
4. prompt pronto para implementacao (copiar/colar)
5. criterios de sucesso objetivos
6. gates de autoavaliacao (teste/lint/type-check/consistencia de artefatos)
7. exigencia de clean code no REFACTOR (nomes claros, funcoes coesas, remocao de codigo morto, baixo acoplamento)
8. relatorio detalhado de implementacao com snippets antes/depois
9. salvar o relatorio em markdown temporario e informar o caminho para avaliacao do planner

Formato de saida obrigatorio ao concluir slice:
- `REPORT_PATH=<caminho-do-arquivo-temporario.md>`

## TDD Red/Green/Refactor

Para cada slice vertical:

1. RED: escrever teste que falha e representa comportamento esperado/bug.
2. GREEN: implementar o minimo para passar o teste.
3. REFACTOR: limpar codigo mantendo toda suite verde.
4. repetir o ciclo no proximo slice (sem pular direto para implementacao).

## Quality baseline

- testes do escopo alterado
- lint e type-check do escopo
- markdown lint quando houver alteração em `.md`

## Setup mínimo de repositório

- `AGENTS.md`
- `PROJECT_CONTEXT.md`
- `openspec/`
- `docs/adr/`
- `docs/releases/`
- scripts de automação de markdown (`scripts/markdown-*.sh`, `.githooks/pre-commit`)

## Retomada rápida

1. ler `AGENTS.md` e `PROJECT_CONTEXT.md`
2. verificar change ativo e próximo slice
3. rodar validação rápida
4. executar apenas o próximo slice

## Quando aumentar rigor

Não usamos perfil fixo (ex: público/saas) no núcleo do SOP.

Use o apêndice para calibrar rigor por contexto:

- [`docs/appendices/rigor-by-complexity.md`](docs/appendices/rigor-by-complexity.md)
