# Convenções de CLI (scripts do DevLoop)

Padrão adotado para scripts em `.devloop/skills/core`, `.devloop/skills/playbooks` e `.devloop/skills/domain`.

## Flags comuns

- `--project-root <path>`: raiz do projeto alvo (default `.`)
- `--format text|json`: formato de saída
- `--dry-run`: não persiste mudanças (quando aplicável)
- `--fail-on <policy>`: limiar de gate/política

## Códigos de saída padronizados

- `0` = execução OK (sem violar política)
- `1` = erro de execução/uso (runtime, argumentos inválidos, IO, etc.)
- `2` = política/gate violado (`--fail-on` atingido)

## Observações

- Scripts de análise (`validate-agents`, `django-insights`, `refactor-sprint-suggester`) usam `--fail-on` por severidade.
- Scripts de recomendação/geração (`suggest-adr`, `changelog-updater`, `release-evidence-pack-generator`) usam `--fail-on` por condição de política.
- `--format json` deve incluir ao menos: `ok`, `policy_failed`, `fail_on`.
