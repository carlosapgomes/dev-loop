#!/usr/bin/env python3
import json
import subprocess
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "check_consistency.py"


class CheckConsistencyTests(unittest.TestCase):
    def _seed_minimal_required_artifacts(self, root: Path) -> None:
        (root / "AGENTS.md").write_text(
            (
                "# AGENTS\n"
                "## 2. Comandos de Validacao\n"
                "- Testes: `python3 -m pytest -q`\n"
            ),
            encoding="utf-8",
        )
        (root / "PROJECT_CONTEXT.md").write_text(
            "# PROJECT_CONTEXT.md\n\ntexto suficiente para consistencia.\n",
            encoding="utf-8",
        )
        (root / "docs" / "adr").mkdir(parents=True)
        (root / "docs" / "releases").mkdir(parents=True)

    def test_runs_with_minimal_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._seed_minimal_required_artifacts(root)

            run = subprocess.run(
                ["python3", str(SCRIPT), "--format", "json"],
                cwd=str(root),
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(run.returncode, 0, msg=run.stderr)
            payload = json.loads(run.stdout)
            self.assertEqual(payload["summary"]["errors"], 0)

    def test_missing_agents_is_error(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            run = subprocess.run(
                ["python3", str(SCRIPT), "--format", "json"],
                cwd=str(root),
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(run.returncode, 1, msg=run.stderr)
            payload = json.loads(run.stdout)
            self.assertGreaterEqual(payload["summary"]["errors"], 1)

    def test_missing_design_for_non_bugfix_change_is_error(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._seed_minimal_required_artifacts(root)
            change = root / "openspec" / "changes" / "active" / "add-csv-export"
            change.mkdir(parents=True)
            (change / "proposal.md").write_text(
                "# Proposal\n\nAdicionar endpoint de exportacao CSV para relatorios.\n",
                encoding="utf-8",
            )
            (change / "tasks.md").write_text("- [ ] Implementar endpoint\n", encoding="utf-8")

            run = subprocess.run(
                ["python3", str(SCRIPT), "--format", "json"],
                cwd=str(root),
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(run.returncode, 1, msg=run.stderr)
            payload = json.loads(run.stdout)
            messages = [f["message"] for f in payload["findings"]]
            self.assertTrue(any("design.md obrigatorio ausente" in msg for msg in messages))

    def test_quick_simple_bugfix_without_design_is_allowed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._seed_minimal_required_artifacts(root)
            change = root / "openspec" / "changes" / "active" / "fix-typo-label"
            change.mkdir(parents=True)
            (change / "proposal.md").write_text(
                "# Proposal\n\nRisco: QUICK\n\nBug fix simples: corrigir typo no label do botao.\n",
                encoding="utf-8",
            )
            (change / "tasks.md").write_text("- [ ] Corrigir label\n", encoding="utf-8")

            run = subprocess.run(
                ["python3", str(SCRIPT), "--format", "json"],
                cwd=str(root),
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(run.returncode, 0, msg=run.stderr)
            payload = json.loads(run.stdout)
            messages = [f["message"] for f in payload["findings"]]
            self.assertFalse(any("design.md obrigatorio ausente" in msg for msg in messages))

    def test_missing_contract_freeze_is_error_for_feature_design(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._seed_minimal_required_artifacts(root)
            change = root / "openspec" / "changes" / "active" / "add-reporting"
            change.mkdir(parents=True)
            (change / "proposal.md").write_text("# Proposal\n\nRisco: FEATURE\n\nAdicionar reporting.\n", encoding="utf-8")
            (change / "design.md").write_text("# Design\n\n## Approach\n\nOk.\n", encoding="utf-8")
            (change / "tasks.md").write_text("- [ ] Slice 1\n", encoding="utf-8")

            run = subprocess.run(
                ["python3", str(SCRIPT), "--format", "json"],
                cwd=str(root),
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(run.returncode, 1, msg=run.stderr)
            payload = json.loads(run.stdout)
            messages = [f["message"] for f in payload["findings"]]
            self.assertTrue(any("Contract Freeze ausente" in msg for msg in messages))

    def test_complete_slice_handoff_with_contract_reference_passes_lifecycle(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._seed_minimal_required_artifacts(root)
            change = root / "openspec" / "changes" / "active" / "add-reporting"
            slices = change / "slices"
            slices.mkdir(parents=True)
            (change / "proposal.md").write_text("# Proposal\n\nRisco: FEATURE\n\nAdicionar reporting.\n", encoding="utf-8")
            (change / "design.md").write_text(
                "# Design\n\n"
                "## Contract Freeze\n\n"
                "### Frozen Interfaces\n\n- x\n"
                "### DTOs / Schemas / Payloads\n\n- x\n"
                "### Invariants\n\n- x\n"
                "### Allowed Files / Areas\n\n- `app/report.py`\n"
                "### Forbidden Files / Areas\n\n- `app/legacy.py`\n"
                "### Technical Non-goals\n\n- x\n"
                "### Testing Strategy\n\n- x\n",
                encoding="utf-8",
            )
            (change / "tasks.md").write_text("- [ ] Slice 1 — design.md#contract-freeze\n", encoding="utf-8")
            (slices / "1.md").write_text(
                "# Slice\n\n"
                "## Frozen Contracts\n\nSource: design.md#contract-freeze\n\n"
                "## Architectural Boundaries\n\n"
                "### Allowed Files / Areas\n\n- `app/report.py`\n\n"
                "### Forbidden Files / Areas\n\n- `app/legacy.py`\n\n"
                "### Explicit Non-goals\n\n- x\n\n"
                "## TDD Plan\n\n- RED\n\n"
                "## Required Gates\n\n- [ ] tests\n\n"
                "## Success Criteria\n\n- [ ] ok\n\n"
                "## Evidence Report\n\n- report\n",
                encoding="utf-8",
            )

            run = subprocess.run(
                ["python3", str(SCRIPT), "--format", "json"],
                cwd=str(root),
                capture_output=True,
                text=True,
                check=False,
            )
            payload = json.loads(run.stdout)
            messages = [f["message"] for f in payload["findings"]]
            self.assertFalse(any("Contract Freeze ausente" in msg for msg in messages))
            self.assertFalse(any("Slice handoff incompleto" in msg for msg in messages))

    def test_forbidden_file_modification_is_error(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            subprocess.run(["git", "init", "-q"], cwd=str(root), check=True)
            subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=str(root), check=True)
            subprocess.run(["git", "config", "user.name", "Test"], cwd=str(root), check=True)
            self._seed_minimal_required_artifacts(root)
            (root / "app").mkdir()
            (root / "app/legacy.py").write_text("old\n", encoding="utf-8")
            change = root / "openspec" / "changes" / "active" / "add-reporting"
            slices = change / "slices"
            slices.mkdir(parents=True)
            (change / "proposal.md").write_text("# Proposal\n\nRisco: FEATURE\n\nAdicionar reporting.\n", encoding="utf-8")
            (change / "design.md").write_text("# Design\n\n## Contract Freeze\n\n", encoding="utf-8")
            (change / "tasks.md").write_text("- [ ] Slice 1\n", encoding="utf-8")
            (slices / "1.md").write_text("# Slice\n\n### Forbidden Files / Areas\n\n- `app/legacy.py`\n", encoding="utf-8")
            subprocess.run(["git", "add", "."], cwd=str(root), check=True)
            subprocess.run(["git", "commit", "-q", "-m", "seed"], cwd=str(root), check=True)
            (root / "app/legacy.py").write_text("changed\n", encoding="utf-8")

            run = subprocess.run(
                ["python3", str(SCRIPT), "--format", "json"],
                cwd=str(root),
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(run.returncode, 1, msg=run.stderr)
            payload = json.loads(run.stdout)
            messages = [f["message"] for f in payload["findings"]]
            self.assertTrue(any("Arquivos proibidos" in msg for msg in messages))


if __name__ == "__main__":
    unittest.main()
