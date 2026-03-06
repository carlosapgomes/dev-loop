# Apêndice — Rigor por Complexidade e Contexto

Este apêndice complementa o SOP com recomendações de rigor.

## Objetivo

Evitar dois extremos:

- burocracia desnecessária em mudanças simples
- falta de evidência em mudanças críticas

## Sinais para aumentar rigor

Aplique o modo mais formal (`FEATURE`/`HIGH`) quando houver:

- impacto em autenticação/autorização
- migração de dados ou contrato externo
- risco regulatório/compliance
- integração crítica com terceiros
- rollback caro
- mudança arquitetural de longo prazo

## Recomendação prática

- Mudanças simples e reversíveis: mantenha enxuto.
- Mudanças estruturais/arriscadas: inclua ADR + plano de rollback + validação completa.
- Entregas formais (cliente enterprise/governo/regulado): gere release evidence pack com rastreabilidade.

## Regra de ouro

Aumente o rigor quando ele reduzir risco real de retrabalho, regressão ou auditoria futura.
