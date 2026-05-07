#!/usr/bin/env python3
import json
import subprocess
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "upgrade_devloop.py"


class DevLoopUpgraderTests(unittest.TestCase):
    def test_check_reports_missing_items(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            run = subprocess.run(
                ["python3", str(SCRIPT), "--project-root", tmp, "--check", "--format", "json"],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(run.returncode, 2, msg=run.stderr)
            payload = json.loads(run.stdout)
            statuses = {a["status"] for a in payload["actions"]}
            self.assertIn("missing", statuses)

    def test_apply_safe_creates_canonical_files_without_rewriting_agents(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "AGENTS.md").write_text("custom agents\n", encoding="utf-8")
            run = subprocess.run(
                ["python3", str(SCRIPT), "--project-root", str(root), "--apply-safe", "--format", "json"],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(run.returncode, 0, msg=run.stderr)
            self.assertTrue((root / "openspec/project.md").exists())
            self.assertTrue((root / "docs/foundations/llm-engineering-principles.md").exists())
            self.assertTrue((root / "openspec/changes/active").exists())
            self.assertEqual((root / "AGENTS.md").read_text(encoding="utf-8"), "custom agents\n")

    def test_apply_safe_updates_markdown_automation_with_backup(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            script = root / "scripts/markdown-lint.sh"
            script.parent.mkdir(parents=True)
            script.write_text("npx --yes markdownlint-cli file.md\n", encoding="utf-8")
            backup = root / "backup"
            run = subprocess.run(
                [
                    "python3",
                    str(SCRIPT),
                    "--project-root",
                    str(root),
                    "--apply-safe",
                    "--backup-dir",
                    str(backup),
                    "--format",
                    "json",
                ],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(run.returncode, 0, msg=run.stderr)
            self.assertIn("markdownlint-cli2", script.read_text(encoding="utf-8"))
            self.assertTrue((backup / "scripts/markdown-lint.sh").exists())

    def test_unsafe_gitignore_rule_is_manual_error(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / ".gitignore").write_text("openspec/changes/*/\n", encoding="utf-8")
            run = subprocess.run(
                ["python3", str(SCRIPT), "--project-root", str(root), "--check", "--format", "json"],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(run.returncode, 2, msg=run.stderr)
            payload = json.loads(run.stdout)
            self.assertTrue(any(a["status"] == "unsafe_rule" and not a["safe"] for a in payload["actions"]))


if __name__ == "__main__":
    unittest.main()
