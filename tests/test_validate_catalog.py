from __future__ import annotations

import unittest
from pathlib import Path

from scripts.validate_catalog import CatalogValidator, IssueFormValidator


ROOT = Path(__file__).resolve().parents[1]
README_TEXT = (ROOT / "README.md").read_text(encoding="utf-8")
ISSUE_FORM_TEXT = (
    ROOT / ".github" / "ISSUE_TEMPLATE" / "01-paper-suggestion.yml"
).read_text(encoding="utf-8")


class CatalogValidatorTests(unittest.TestCase):
    def validate(self, text: str) -> list[str]:
        return CatalogValidator(text).validate()

    def test_current_catalog_is_valid(self) -> None:
        self.assertEqual(self.validate(README_TEXT), [])

    def test_missing_metadata_is_reported(self) -> None:
        mutated = README_TEXT.replace("  **Metadata:**", "  **Removed metadata:**", 1)
        errors = self.validate(mutated)
        self.assertTrue(any("expected one exact Metadata line" in error for error in errors))

    def test_invalid_controlled_value_is_reported(self) -> None:
        mutated = README_TEXT.replace("`State: Physiology`", "`State: Galaxy`", 1)
        errors = self.validate(mutated)
        self.assertTrue(any("invalid State values" in error for error in errors))

    def test_asset_mismatch_is_reported(self) -> None:
        mutated = README_TEXT.replace("`Assets: Code`", "`Assets: Paper only`", 1)
        errors = self.validate(mutated)
        self.assertTrue(any("expected 'Code' from links" in error for error in errors))

    def test_topic_set_drift_is_reported(self) -> None:
        marker = "## 🧭 By Topic"
        before, topics = README_TEXT.split(marker, 1)
        topics = topics.replace(
            "HemoPIC: A Physics-Informed Cerebral Hemodynamics Digital Twin for Brain Perfusion",
            "HemoPIC: Altered Topic Title",
            1,
        )
        errors = self.validate(before + marker + topics)
        self.assertTrue(any("missing from By Topic" in error for error in errors))
        self.assertTrue(any("missing from main list" in error for error in errors))

    def test_duplicate_identifier_is_reported(self) -> None:
        mutated = README_TEXT.replace("2607.08793", "2607.08799", 1)
        errors = self.validate(mutated)
        self.assertTrue(any("Duplicate identifier arXiv:2607.08799" in error for error in errors))

    def test_missing_resource_category_is_reported(self) -> None:
        mutated = README_TEXT.replace("### Simulators", "### Tools", 1)
        errors = self.validate(mutated)
        self.assertTrue(any("Resource categories differ" in error for error in errors))
        self.assertTrue(
            any("Resource category 'Simulators' has no entries" in error for error in errors)
        )


class IssueFormValidatorTests(unittest.TestCase):
    def validate(self, form: str) -> list[str]:
        return IssueFormValidator(README_TEXT, form).validate()

    def test_current_issue_form_is_valid(self) -> None:
        self.assertEqual(self.validate(ISSUE_FORM_TEXT), [])

    def test_taxonomy_drift_is_reported(self) -> None:
        mutated = ISSUE_FORM_TEXT.replace("        - Population", "        - Galaxy", 1)
        errors = self.validate(mutated)
        self.assertTrue(any("field 'state' options differ" in error for error in errors))

    def test_missing_required_field_is_reported(self) -> None:
        mutated = ISSUE_FORM_TEXT.replace("    id: medical_task", "    id: removed_task", 1)
        errors = self.validate(mutated)
        self.assertTrue(any("missing field 'medical_task'" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
