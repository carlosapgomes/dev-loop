#!/usr/bin/env bash
set -euo pipefail

TARGET_DIR="${1:-$HOME/.pi/agent/skills}"
SRC_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "Installing skills bundle into: $TARGET_DIR"
mkdir -p "$TARGET_DIR"

copy_skill() {
  local src="$1"
  local base
  base="$(basename "$src")"
  rm -rf "$TARGET_DIR/$base"
  cp -R "$src" "$TARGET_DIR/$base"
  echo "  - installed: $base"
}

for d in "$SRC_DIR"/deepseek/*; do
  [ -d "$d" ] || continue
  copy_skill "$d"
done

for d in "$SRC_DIR"/k2.5/*; do
  [ -d "$d" ] || continue
  copy_skill "$d"
done

find "$TARGET_DIR" -type d -name "__pycache__" -prune -exec rm -rf {} + || true
find "$TARGET_DIR" -type f -name "*.pyc" -delete || true

echo
echo "Done."
echo "Installed skills count:"
find "$TARGET_DIR" -mindepth 1 -maxdepth 1 -type d | wc -l | awk '{print "  " $1}'

echo
echo "Tip:"
echo "  Read $SRC_DIR/README.md for usage examples."
