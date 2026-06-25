import re
from pathlib import Path

from models.review_finding_model import (
    ReviewFinding
)

from agents.reviewer_agent.review_file_provider import (
    ReviewFileProvider
)


class AssertionReviewer:

    @staticmethod
    def has_assertion(
        content: str
    ):

        executable_lines = []

        for line in content.splitlines():

            stripped = line.strip()

            if stripped.startswith("//"):

                continue

            executable_lines.append(
                stripped
            )

        executable_content = "\n".join(
            executable_lines
        )

        return bool(

            re.search(

                r"\bAssert\.",

                executable_content
            )
        )

    @staticmethod
    def has_dummy_assertion(
        content: str
    ):

        dummy_patterns = [

            r"Assert\.assertTrue\s*\(\s*true\s*\)",

            r"Assert\.assertFalse\s*\(\s*false\s*\)",

            r"Assert\.assertEquals\s*\(\s*true\s*,\s*true\s*\)",

            r"Assert\.assertEquals\s*\(\s*false\s*,\s*false\s*\)",

            r"Assert\.assertEquals\s*\(\s*1\s*,\s*1\s*\)",

            r'Assert\.assertEquals\s*\(\s*"([^"]*)"\s*,\s*"\1"\s*\)',

            r'Assert\.assertTrue\s*\(\s*".*"\.equals\(\s*".*"\s*\)\s*\)',

            r"Assert\.assertTrue\s*\(\s*1\s*==\s*1\s*\)"
        ]

        for pattern in dummy_patterns:

            if re.search(
                pattern,
                content
            ):

                return True

        return False

    @staticmethod
    def has_weak_assertion(
        content: str
    ):

        weak_patterns = [

            r"Assert\.assertNotNull\s*\(\s*driver\s*\)",

            r"Assert\.assertNotNull\s*\(\s*page\s*\)",

            r"Assert\.assertNotNull\s*\(\s*\w+\s*\)"
        ]

        for pattern in weak_patterns:

            if re.search(
                pattern,
                content
            ):

                return True

        return False

    @staticmethod
    def review():

        findings = []

        java_files = (
            ReviewFileProvider
            .get_generated_test_files()
        )

        if not java_files:

            return findings

        finding_counter = 1

        for java_file in java_files:

            with open(
               java_file,
               "r",
               encoding="utf-8"
            ) as file:

                content = file.read()

            # -----------------------------
            # MISSING ASSERTION
            # -----------------------------

            if not AssertionReviewer.has_assertion(
                content
            ):

                findings.append(

                    ReviewFinding(

                        finding_id=
                        f"AST-{finding_counter:03}",

                        severity=
                        "HIGH",

                        category=
                        "ASSERTION",

                        file_name=
                        java_file.name,

                        description=
                        "Missing assertion",

                        recommendation=
                        "Add business assertion.",

                        impacted_component=
                        "Generated Test",

                        auto_fixable=
                        True
                    )
                )

                finding_counter += 1

            # -----------------------------
            # DUMMY ASSERTION
            # -----------------------------

            if AssertionReviewer.has_dummy_assertion(
                content
            ):

                findings.append(

                    ReviewFinding(

                        finding_id=
                        f"AST-{finding_counter:03}",

                        severity=
                        "HIGH",

                        category=
                        "ASSERTION",

                        file_name=
                        java_file.name,

                        description=
                        "Dummy assertion",

                        recommendation=
                        "Replace dummy assertion with business validation.",

                        impacted_component=
                        "Generated Test",

                        auto_fixable=
                        True
                    )
                )

                finding_counter += 1

            # -----------------------------
            # WEAK ASSERTION
            # -----------------------------

            if AssertionReviewer.has_weak_assertion(
                content
            ):

                findings.append(

                    ReviewFinding(

                        finding_id=
                        f"AST-{finding_counter:03}",

                        severity=
                        "MEDIUM",

                        category=
                        "ASSERTION",

                        file_name=
                        file_path.name,

                        description=
                        "Weak assertion",

                        recommendation=
                        "Replace weak assertion with business validation.",

                        impacted_component=
                        "Generated Test",

                        auto_fixable=
                        True
                    )
                )

                finding_counter += 1

        return findings