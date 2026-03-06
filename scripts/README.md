# Scripts utilitários

## smoke-skills.sh

Roda validação rápida (sanidade) do bundle de skills:

- frontmatter de `SKILL.md`
- compilação Python (`py_compile`)
- smoke de CLI (`--help`)
- testes unitários dos skills
- instalador de skills
- checks de política (`--fail-on` => exit code `2`)

Uso:

```bash
./scripts/smoke-skills.sh
./scripts/smoke-skills.sh --quick
./scripts/smoke-skills.sh --include-legacy
```
