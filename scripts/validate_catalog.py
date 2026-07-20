#!/usr/bin/env python3
"""Validate the structure and controlled metadata in the README catalog."""

from __future__ import annotations

import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
ISSUE_FORM = ROOT / ".github" / "ISSUE_TEMPLATE" / "01-paper-suggestion.yml"

ALLOWED = {
    "State": {
        "Patient",
        "Physiology",
        "Anatomy",
        "Medical image",
        "Procedure/Robot",
        "Clinical workflow",
        "Cell",
        "Molecule",
        "Population",
    },
    "Dynamics": {
        "Temporal",
        "Action-conditioned",
        "Mechanistic",
        "Spatial/view",
        "Event sequence",
    },
    "Capability": {"Forecast", "Simulate", "Counterfactual", "Plan", "Control"},
    "Assets": {"Code", "Weights", "Project", "Paper only"},
}

ENTRY_RE = re.compile(r"^- \(\*.*?\*\) \*\*(.*?)\*\*", re.MULTILINE)
METADATA_RE = re.compile(
    r"^  \*\*Metadata:\*\* "
    r"`State: ([^`]+)` · "
    r"`Dynamics: ([^`]+)` · "
    r"`Capability: ([^`]+)` · "
    r"`Assets: ([^`]+)`$",
    re.MULTILINE,
)
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
RESOURCES_HEADING = "## 🧰 Datasets, Benchmarks and Simulators"
RELATED_REPOSITORIES_HEADING = "## 🔗 Related Repositories"
RESOURCE_CATEGORIES = ("Datasets", "Benchmarks", "Simulators")


@dataclass(frozen=True)
class Entry:
    title: str
    block: str
    section: str


class CatalogValidator:
    def __init__(self, text: str) -> None:
        self.text = text
        self.errors: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def section_between(self, start: str, end: str) -> str:
        start_index = self.text.find(start)
        end_index = self.text.find(end)
        if start_index < 0:
            self.error(f"Missing section heading: {start}")
            return ""
        if end_index < 0 or end_index <= start_index:
            self.error(f"Missing or misplaced section heading: {end}")
            return ""
        return self.text[start_index + len(start) : end_index]

    @staticmethod
    def entries(section: str) -> list[Entry]:
        entries: list[Entry] = []
        current_heading = ""
        for block in re.split(r"\n\s*\n", section.strip()):
            heading_match = re.search(r"^###\s+(.+)$", block, re.MULTILINE)
            if heading_match:
                current_heading = heading_match.group(1).strip()
            entry_match = ENTRY_RE.search(block)
            if entry_match:
                entries.append(Entry(entry_match.group(1).strip(), block, current_heading))
        return entries

    def validate(self) -> list[str]:
        main = self.section_between("## 📝 World Model Papers", "## 🧭 By Topic")
        topics = self.section_between("## 🧭 By Topic", RESOURCES_HEADING)
        resources = self.section_between(RESOURCES_HEADING, RELATED_REPOSITORIES_HEADING)
        taxonomy = self.section_between("## 🧬 Taxonomy", "## 📚 Survey Papers")

        main_entries = self.entries(main)
        topic_entries = self.entries(topics)

        self.validate_taxonomy(taxonomy)
        self.validate_years(main)
        self.validate_main_entries(main_entries)
        self.validate_topics(main_entries, topic_entries)
        self.validate_resources(resources)
        self.validate_duplicate_identifiers(main_entries)
        self.validate_links(main_entries + topic_entries)
        return self.errors

    def validate_taxonomy(self, taxonomy: str) -> None:
        rows = re.findall(
            r"^\| \*\*(State|Dynamics|Capability|Assets)\*\* \| ([^|]+)",
            taxonomy,
            re.MULTILINE,
        )
        parsed: dict[str, set[str]] = {}
        for field, values in rows:
            parsed[field] = set(re.findall(r"`([^`]+)`", values))

        for field, allowed in ALLOWED.items():
            if field not in parsed:
                self.error(f"Taxonomy table is missing the {field} row")
            elif parsed[field] != allowed:
                self.error(
                    f"Taxonomy {field} values differ from the validator: "
                    f"README={sorted(parsed[field])}, validator={sorted(allowed)}"
                )

    def validate_years(self, main: str) -> None:
        years = [int(year) for year in re.findall(r"^### (\d{4})$", main, re.MULTILINE)]
        if not years:
            self.error("No year headings found in World Model Papers")
            return
        if len(years) != len(set(years)):
            self.error(f"Duplicate year headings: {years}")
        if years != sorted(years, reverse=True):
            self.error(f"Year headings must be in descending order: {years}")

    def validate_main_entries(self, entries: list[Entry]) -> None:
        if not entries:
            self.error("No entries found in World Model Papers")
            return

        duplicates = [title for title, count in Counter(e.title for e in entries).items() if count > 1]
        for title in duplicates:
            self.error(f"Duplicate main-list title: {title}")

        for entry in entries:
            self.validate_entry_year(entry)
            self.validate_metadata(entry)
            qualification_count = entry.block.count("> **Why it qualifies:**")
            if qualification_count != 1:
                self.error(
                    f"{entry.title}: expected one Why it qualifies note, found {qualification_count}"
                )

    def validate_entry_year(self, entry: Entry) -> None:
        if not entry.section.isdigit():
            self.error(f"{entry.title}: entry is not under a four-digit year heading")
            return
        venue_year = re.search(r"^- \(\*.*?'(\d{2})", entry.block)
        if not venue_year:
            self.error(f"{entry.title}: venue label must include a two-digit year")
            return
        if venue_year.group(1) != entry.section[-2:]:
            self.error(
                f"{entry.title}: venue year '{venue_year.group(1)}' does not match section {entry.section}"
            )

    def validate_metadata(self, entry: Entry) -> None:
        matches = list(METADATA_RE.finditer(entry.block))
        if len(matches) != 1:
            self.error(f"{entry.title}: expected one exact Metadata line, found {len(matches)}")
            return

        values = dict(zip(("State", "Dynamics", "Capability", "Assets"), matches[0].groups()))
        for field, raw_value in values.items():
            parts = raw_value.split(" + ")
            if len(parts) != len(set(parts)):
                self.error(f"{entry.title}: duplicate {field} value in '{raw_value}'")
            invalid = set(parts) - ALLOWED[field]
            if invalid:
                self.error(f"{entry.title}: invalid {field} values: {sorted(invalid)}")

        if " + " in values["State"]:
            self.error(f"{entry.title}: State must contain exactly one primary value")

        expected_assets: list[str] = []
        if "[[💻 Code]" in entry.block:
            expected_assets.append("Code")
        if "[[🌐 Weights]" in entry.block:
            expected_assets.append("Weights")
        if "[[🌐 Project]" in entry.block:
            expected_assets.append("Project")
        if not expected_assets:
            expected_assets.append("Paper only")
        expected = " + ".join(expected_assets)
        if values["Assets"] != expected:
            self.error(
                f"{entry.title}: Assets is '{values['Assets']}', expected '{expected}' from links"
            )

    def validate_topics(self, main_entries: list[Entry], topic_entries: list[Entry]) -> None:
        main_titles = {entry.title for entry in main_entries}
        topic_titles = {entry.title for entry in topic_entries}

        for title in sorted(main_titles - topic_titles):
            self.error(f"Main-list paper missing from By Topic: {title}")
        for title in sorted(topic_titles - main_titles):
            self.error(f"By Topic paper missing from main list: {title}")

        by_section: dict[str, list[str]] = defaultdict(list)
        for entry in topic_entries:
            by_section[entry.section].append(entry.title)
            if "**Metadata:**" in entry.block or "Why it qualifies" in entry.block:
                self.error(f"{entry.title}: topic entries must stay concise")

        for section, titles in by_section.items():
            duplicates = [title for title, count in Counter(titles).items() if count > 1]
            for title in duplicates:
                self.error(f"Duplicate title in topic '{section}': {title}")

    def validate_duplicate_identifiers(self, entries: list[Entry]) -> None:
        owners: dict[str, set[str]] = defaultdict(set)
        patterns = {
            "arXiv": re.compile(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})", re.IGNORECASE),
            "DOI": re.compile(r"doi\.org/(10\.[^\s)\]]+)", re.IGNORECASE),
            "PubMed": re.compile(r"pubmed\.ncbi\.nlm\.nih\.gov/(\d+)", re.IGNORECASE),
            "OpenReview": re.compile(r"openreview\.net/forum\?id=([^&)\s]+)", re.IGNORECASE),
        }
        for entry in entries:
            for kind, pattern in patterns.items():
                for value in pattern.findall(entry.block):
                    owners[f"{kind}:{unquote(value).lower()}"].add(entry.title)

        for identifier, titles in sorted(owners.items()):
            if len(titles) > 1:
                self.error(f"Duplicate identifier {identifier} appears in: {sorted(titles)}")

    def validate_links(self, entries: list[Entry]) -> None:
        for entry in entries:
            links = LINK_RE.findall(entry.block)
            if not links:
                self.error(f"{entry.title}: entry has no links")
            for link in links:
                if not link.startswith("https://"):
                    self.error(f"{entry.title}: link must use HTTPS: {link}")
                if link in {"https://example.org/paper", "https://github.com/org/repo"}:
                    self.error(f"{entry.title}: placeholder link found: {link}")

    def validate_resources(self, resources: str) -> None:
        headings = set(re.findall(r"^### (.+)$", resources, re.MULTILINE))
        if headings != set(RESOURCE_CATEGORIES):
            self.error(
                "Resource categories differ from the required set: "
                f"README={sorted(headings)}, required={sorted(RESOURCE_CATEGORIES)}"
            )

        for category in RESOURCE_CATEGORIES:
            match = re.search(
                rf"^### {re.escape(category)}\n(.*?)(?=^### |\Z)",
                resources,
                re.MULTILINE | re.DOTALL,
            )
            if not match or not re.search(
                r"^\| \*\*.+\*\* \|", match.group(1), re.MULTILINE
            ):
                self.error(f"Resource category '{category}' has no entries")

        for link in LINK_RE.findall(resources):
            if not link.startswith("https://"):
                self.error(f"Resource link must use HTTPS: {link}")
            if link in {"https://example.org/paper", "https://github.com/org/repo"}:
                self.error(f"Resource placeholder link found: {link}")


class IssueFormValidator:
    REQUIRED_FIELDS = {
        "paper_title": "input",
        "paper_url": "input",
        "venue_year": "input",
        "publication_status": "dropdown",
        "medical_task": "textarea",
        "state": "dropdown",
        "dynamics": "dropdown",
        "capability": "dropdown",
        "transition_evidence": "textarea",
        "implementation_evidence": "textarea",
        "qualification": "textarea",
        "topics": "dropdown",
        "resources": "textarea",
        "confirmation": "checkboxes",
    }
    OPTIONAL_FIELDS = {"resources"}
    MULTISELECT_FIELDS = {"dynamics", "capability", "topics"}
    FIELD_RE = re.compile(
        r"^  - type: ([^\n]+)\n    id: ([^\n]+)\n(.*?)(?=^  - type:|\Z)",
        re.MULTILINE | re.DOTALL,
    )

    def __init__(self, readme: str, form: str) -> None:
        self.readme = readme
        self.form = form
        self.errors: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(f"Issue form: {message}")

    def validate(self) -> list[str]:
        fields = {
            field_id.strip(): (field_type.strip(), block)
            for field_type, field_id, block in self.FIELD_RE.findall(self.form)
        }

        for field_id, expected_type in self.REQUIRED_FIELDS.items():
            if field_id not in fields:
                self.error(f"missing field '{field_id}'")
                continue
            actual_type, block = fields[field_id]
            if actual_type != expected_type:
                self.error(
                    f"field '{field_id}' has type '{actual_type}', expected '{expected_type}'"
                )
            if field_id not in self.OPTIONAL_FIELDS and field_id != "confirmation":
                if not re.search(r"^    validations:\n      required: true$", block, re.MULTILINE):
                    self.error(f"field '{field_id}' must be required")

        for field_id in self.MULTISELECT_FIELDS:
            if field_id in fields and not re.search(
                r"^      multiple: true$", fields[field_id][1], re.MULTILINE
            ):
                self.error(f"field '{field_id}' must allow multiple selections")

        expected_options = {
            "state": ALLOWED["State"],
            "dynamics": ALLOWED["Dynamics"],
            "capability": ALLOWED["Capability"],
            "topics": self.readme_topics(),
        }
        for field_id, expected in expected_options.items():
            if field_id not in fields:
                continue
            options = set(re.findall(r"^        - ([^\n]+)$", fields[field_id][1], re.MULTILINE))
            if options != expected:
                self.error(
                    f"field '{field_id}' options differ from the catalog: "
                    f"form={sorted(options)}, catalog={sorted(expected)}"
                )

        if "confirmation" in fields and not re.search(
            r"^          required: true$", fields["confirmation"][1], re.MULTILINE
        ):
            self.error("confirmation checkbox must be required")

        return self.errors

    def readme_topics(self) -> set[str]:
        try:
            topic_section = self.readme.split("## 🧭 By Topic", 1)[1].split(
                RESOURCES_HEADING, 1
            )[0]
        except IndexError:
            self.error("cannot read topic headings from README")
            return set()
        return set(re.findall(r"^### (.+)$", topic_section, re.MULTILINE))


def main() -> int:
    if not README.exists():
        print(f"ERROR: README not found at {README}", file=sys.stderr)
        return 1

    if not ISSUE_FORM.exists():
        print(f"ERROR: issue form not found at {ISSUE_FORM}", file=sys.stderr)
        return 1

    text = README.read_text(encoding="utf-8")
    form = ISSUE_FORM.read_text(encoding="utf-8")
    errors = CatalogValidator(text).validate()
    errors.extend(IssueFormValidator(text, form).validate())
    if errors:
        print(f"Catalog validation failed with {len(errors)} error(s):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    main = CatalogValidator.entries(
        text.split("## 📝 World Model Papers", 1)[1].split("## 🧭 By Topic", 1)[0]
    )
    topics = CatalogValidator.entries(
        text.split("## 🧭 By Topic", 1)[1].split(RESOURCES_HEADING, 1)[0]
    )
    print(
        f"Catalog validation passed: {len(main)} main-list papers, "
        f"{len({entry.title for entry in topics})} unique topic entries, "
        "and a synchronized paper-suggestion form."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
