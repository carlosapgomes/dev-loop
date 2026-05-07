#!/usr/bin/env bash
set -euo pipefail

TARGET_DIR="${1:-$HOME/.pi/agent/skills}"
INCLUDE_LEGACY="${INCLUDE_LEGACY:-false}"
SRC_DIR="$(cd "$(dirname "$0")" && pwd)"

# optional flag as second positional argument
if [[ "${2:-}" == "--include-legacy" ]]; then
  INCLUDE_LEGACY="true"
fi

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

install_group() {
  local group="$1"
  local dir="$SRC_DIR/$group"
  [ -d "$dir" ] || return 0
  for d in "$dir"/*; do
    [ -d "$d" ] || continue
    copy_skill "$d"
  done
}

install_group core
install_group playbooks
install_group domain

if [[ "$INCLUDE_LEGACY" == "true" ]]; then
  install_group legacy
fi

find "$TARGET_DIR" -type d -name "__pycache__" -prune -exec rm -rf {} + || true
find "$TARGET_DIR" -type f -name "*.pyc" -delete || true

echo
echo "Done."
echo "Installed skills count:"
find "$TARGET_DIR" -mindepth 1 -maxdepth 1 -type d | wc -l | awk '{print "  " $1}'

echo
echo "Tip:"
echo "  Read $SRC_DIR/README.md for usage examples."
echo "  Add --include-legacy to also install compatibility aliases."
