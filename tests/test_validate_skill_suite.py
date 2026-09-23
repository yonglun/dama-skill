import importlib.util
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = REPO_ROOT / "scripts" / "validate_skill_suite.py"


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_skill_suite", VALIDATOR_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load validator at {VALIDATOR_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class SkillSuiteValidatorTest(unittest.TestCase):
    def setUp(self):
        self.validator = load_validator()

    def _write_skill(self, root: Path, name: str, child: bool = True) -> None:
        skill_dir = root / name
        skill_dir.mkdir(parents=True)
        (skill_dir / "SKILL.md").write_text(
            "---\n"
            f"name: {name}\n"
            "description: Use when a concrete data-management project needs this domain.\n"
            "---\n\n"
            f"# {name}\n\n"
            "Read [the playbook](references/playbook.md).\n"
            if child
            else
            "---\n"
            f"name: {name}\n"
            "description: Use when a data project spans multiple data-management domains.\n"
            "---\n\n"
            f"# {name}\n\n"
            "Read [the lifecycle](references/project-lifecycle.md).\n",
            encoding="utf-8",
        )
        references = skill_dir / "references"
        references.mkdir()
        if child:
            headings = "\n\n".join(self.validator.CANONICAL_PLAYBOOK_HEADINGS)
            (references / "playbook.md").write_text(
                f"# Playbook\n\n{headings}\n",
                encoding="utf-8",
            )
        else:
            (references / "project-lifecycle.md").write_text("# Lifecycle\n", encoding="utf-8")
            (references / "routing-table.md").write_text("# Routing\n", encoding="utf-8")
            (references / "deliverable-templates.md").write_text("# Templates\n", encoding="utf-8")
            chapters = "\n".join(f"- 第 {number} 章" for number in range(1, 18))
            (references / "source-map.md").write_text(
                f"# Source map\n\n{chapters}\n",
                encoding="utf-8",
            )

    def test_reports_all_missing_required_skills(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            errors = self.validator.validate_suite(Path(temp_dir))
        self.assertEqual(len(self.validator.EXPECTED_SKILLS), 17)
        for name in self.validator.EXPECTED_SKILLS:
            self.assertIn(f"missing skill directory: {name}", errors)

    def test_accepts_complete_minimal_fixture(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            for name in self.validator.EXPECTED_SKILLS:
                self._write_skill(root, name, child=name != "managing-data-projects")
            errors = self.validator.validate_suite(root)
        self.assertEqual(errors, [])

    def test_rejects_placeholder_and_broken_relative_link(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            for name in self.validator.EXPECTED_SKILLS:
                self._write_skill(root, name, child=name != "managing-data-projects")
            target = root / "modeling-data" / "SKILL.md"
            target.write_text(
                target.read_text(encoding="utf-8")
                + "\nTODO: finish this. Read [missing](references/missing.md).\n",
                encoding="utf-8",
            )
            errors = self.validator.validate_suite(root)
        self.assertTrue(any("placeholder" in error for error in errors))
        self.assertTrue(any("broken relative link" in error for error in errors))

    def test_rejects_wrong_frontmatter_and_incomplete_playbook(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            for name in self.validator.EXPECTED_SKILLS:
                self._write_skill(root, name, child=name != "managing-data-projects")
            skill = root / "securing-data" / "SKILL.md"
            skill.write_text(
                skill.read_text(encoding="utf-8").replace(
                    "name: securing-data", "name: wrong-name"
                ).replace("description: Use when", "description: Helps when"),
                encoding="utf-8",
            )
            playbook = root / "securing-data" / "references" / "playbook.md"
            playbook.write_text("# Incomplete\n", encoding="utf-8")
            errors = self.validator.validate_suite(root)
        self.assertTrue(any("frontmatter name" in error for error in errors))
        self.assertTrue(any("description must start" in error for error in errors))
        self.assertTrue(any("missing playbook heading" in error for error in errors))

    def test_rejects_source_map_without_all_seventeen_chapters(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            for name in self.validator.EXPECTED_SKILLS:
                self._write_skill(root, name, child=name != "managing-data-projects")
            source_map = root / "managing-data-projects" / "references" / "source-map.md"
            source_map.write_text("# Source map\n\n- 第 1 章\n", encoding="utf-8")
            errors = self.validator.validate_suite(root)
        self.assertTrue(any("source map missing chapter 17" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
