from pathlib import Path

from models.review_finding_model import (
    ReviewFinding
)


class AssertionReviewer:

    @staticmethod
    def review():

        findings = []

        tests_folder = Path(
            "generated_framework/tests"
        )

        if not tests_folder.exists():

            return findings

        finding_counter = 1

        for file_path in tests_folder.glob(
            "*.java"
        ):

            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as file:

                content = file.read()

            # ---------------------
            # Missing Assertion
            # ---------------------

            if (
                "Assert."
                not in content
            ):

                findings.append(
                    ReviewFinding(

                        finding_id=
                        f"FND-{finding_counter:03d}",

                        severity="HIGH",

                        category="ASSERTION",

                        file_name=file_path.name,

                        description=
                        "No assertion found in test.",

                        recommendation=
                        "Add assertion to validate expected outcome."
                    )
                )

                finding_counter += 1

                continue

            # ---------------------
            # Weak Assertion
            # ---------------------

            if (
                "Assert.assertTrue(true)"
                in content
            ):

                findings.append(
                    ReviewFinding(

                        finding_id=
                        f"FND-{finding_counter:03d}",

                        severity="MEDIUM",

                        category="ASSERTION",

                        file_name=file_path.name,

                        description=
                        "Weak assertion detected.",

                        recommendation=
                        "Replace with business validation."
                    )
                )

                finding_counter += 1

        return findings