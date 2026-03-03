#!/usr/bin/env python3
import subprocess
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "generate_agents_md.py"


class GenerateAgentsMdTests(unittest.TestCase):
    def test_generates_agents_for_django_project(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "manage.py").write_text("print('django')\n", encoding="utf-8")
            (root / "requirements.txt").write_text("Django==5.0.6\n", encoding="utf-8")
            (root / "pytest.ini").write_text("[pytest]\n", encoding="utf-8")

            run = subprocess.run(
                ["python3", str(SCRIPT), "--project-root", str(root)],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(run.returncode, 0, msg=run.stderr)

            content = (root / "AGENTS.md").read_text(encoding="utf-8")
            self.assertIn("## 2. Comandos de Validacao", content)
            self.assertIn("python3 manage.py check", content)
            self.assertIn("python3 -m pytest -q", content)

    def test_check_mode_detects_drift(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "requirements.txt").write_text("Django==5.0.6\n", encoding="utf-8")
            (root / "AGENTS.md").write_text("old-content\n", encoding="utf-8")

            run = subprocess.run(
                ["python3", str(SCRIPT), "--project-root", str(root), "--check"],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(run.returncode, 2, msg=run.stderr)


if __name__ == "__main__":
    unittest.main()
