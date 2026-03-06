#!/usr/bin/env bash
set -euo pipefail

TARGET_ROOT="${1:-.}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

mkdir -p "$TARGET_ROOT/scripts" "$TARGET_ROOT/.githooks"

cp "$SCRIPT_DIR/markdown-format.sh" "$TARGET_ROOT/scripts/markdown-format.sh"
cp "$SCRIPT_DIR/markdown-lint.sh" "$TARGET_ROOT/scripts/markdown-lint.sh"
cp "$SCRIPT_DIR/pre-commit" "$TARGET_ROOT/.githooks/pre-commit"
cp "$SCRIPT_DIR/.markdownlintignore" "$TARGET_ROOT/.markdownlintignore"

chmod +x \
  "$TARGET_ROOT/scripts/markdown-format.sh" \
  "$TARGET_ROOT/scripts/markdown-lint.sh" \
  "$TARGET_ROOT/.githooks/pre-commit"

git -C "$TARGET_ROOT" config core.hooksPath .githooks

echo "Markdown automation instalada em: $TARGET_ROOT"
