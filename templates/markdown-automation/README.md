# Markdown Automation Templates

Modelos prontos para padronizar lint/fix de Markdown no workflow.

## Arquivos

- `markdown-format.sh`: roda prettier + markdownlint --fix + markdownlint
- `markdown-lint.sh`: valida markdown
- `pre-commit`: auto-fix/lint de arquivos `.md` staged
- `.markdownlintignore`: ignora `.pi/`, `.codex/`, `node_modules/`, `.git/`
- `install.sh`: instala tudo no projeto e configura `core.hooksPath`

## Instalação em um projeto

Forma rápida:

```bash
bash templates/markdown-automation/install.sh .
```

Forma manual:

```bash
mkdir -p scripts .githooks
cp templates/markdown-automation/markdown-format.sh scripts/
cp templates/markdown-automation/markdown-lint.sh scripts/
cp templates/markdown-automation/pre-commit .githooks/pre-commit
cp templates/markdown-automation/.markdownlintignore .
chmod +x scripts/markdown-format.sh scripts/markdown-lint.sh .githooks/pre-commit
git config core.hooksPath .githooks
```

## Uso

```bash
./scripts/markdown-format.sh
./scripts/markdown-lint.sh
```
