from __future__ import annotations

from hashlib import sha256
from pathlib import Path
from tempfile import TemporaryDirectory
from zipfile import ZipFile
import unittest

from scripts.build_release import build_release, PACKAGE_NAME
from scripts.validate_skill_suite import EXPECTED_SKILLS


class ReleaseTests(unittest.TestCase):
    def test_release_is_complete_safe_and_reproducible(self) -> None:
        with TemporaryDirectory() as first, TemporaryDirectory() as second:
            package = build_release(Path(first))
            build_release(Path(second))
            archive = Path(first) / f"{PACKAGE_NAME}.zip"
            other = Path(second) / f"{PACKAGE_NAME}.zip"
            self.assertEqual(sha256(archive.read_bytes()).digest(), sha256(other.read_bytes()).digest())
            with ZipFile(archive) as zipped:
                self.assertIsNone(zipped.testzip())
                names = set(zipped.namelist())
            self.assertEqual(len([name for name in names if name.endswith("/SKILL.md")]), 17)
            self.assertEqual(len([name for name in names if "/templates/" in name]), 102)
            self.assertIn(f"{PACKAGE_NAME}/LICENSE", names)
            self.assertIn(f"{PACKAGE_NAME}/README.md", names)
            self.assertIn(f"{PACKAGE_NAME}/README.en.md", names)
            self.assertEqual(len(list((package / "skills").iterdir())), len(EXPECTED_SKILLS))
            self.assertFalse(any("dmbok/" in name or "tmp/" in name or ".DS_Store" in name for name in names))


if __name__ == "__main__":
    unittest.main()
