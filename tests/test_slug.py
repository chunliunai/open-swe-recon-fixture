import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from recon_fixture import normalize_slug


class NormalizeSlugTests(unittest.TestCase):
    def test_lowercases_and_replaces_spaces(self) -> None:
        self.assertEqual(normalize_slug("Hello World"), "hello-world")

    def test_trims_outer_whitespace(self) -> None:
        self.assertEqual(normalize_slug("  release notes  "), "release-notes")

    def test_collapses_mixed_whitespace(self) -> None:
        self.assertEqual(
            normalize_slug("Release \t  Candidate\nNotes"),
            "release-candidate-notes",
        )


if __name__ == "__main__":
    unittest.main()
