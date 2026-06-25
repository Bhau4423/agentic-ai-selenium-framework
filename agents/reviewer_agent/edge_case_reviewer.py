import json
from pathlib import Path

from models.review_finding_model import (
    ReviewFinding
)

from agents.reviewer_agent.review_file_provider import (
    ReviewFileProvider
)


class EdgeCaseReviewer:

    @staticmethod
    def load_boundary_scenarios():

        java_files = Path(
            "data/intermediate/requirement_analysis.json"
        )

        if not java_files.exists():

            return []

        with open(
            java_files,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(
                file
            )

        return data.get(
            "boundary_scenarios",
            []
        )

    @staticmethod
    def create_expected_test_name(
        scenario_title: str
    ):

        words = (
            scenario_title
            .replace("-", " ")
            .replace("_", " ")
            .split()
        )

        class_name = ""

        for word in words:

            class_name += (
                word.capitalize()
            )

        return (
            class_name
            + "Test.java"
        )

    @staticmethod
    def review():

        findings = []

        boundary_scenarios = (
            EdgeCaseReviewer.load_boundary_scenarios()
        )

        java_files = (
            ReviewFileProvider
            .get_generated_test_files()
        )

        generated_tests = {

            java_file.name

            for java_file in java_files
        }

        finding_counter = 1

        for scenario in boundary_scenarios:

            expected_test = (
                EdgeCaseReviewer.create_expected_test_name(
                    scenario.get(
                        "title",
                        ""
                    )
                )
            )

            if (
                expected_test
                not in generated_tests
            ):

                findings.append(

                    ReviewFinding(

                        finding_id=
                        f"EDGE-{finding_counter:03}",

                        severity=
                        "HIGH",

                        category=
                        "EDGE_CASE_NOT_COVERED",

                        file_name=
                        expected_test,

                        scenario_id=
                        scenario.get(
                            "id"
                        ),

                        requirement_id=
                        scenario.get(
                            "requirement_id"
                        ),

                        description=
                        (
                            "Boundary scenario is missing "
                            "its generated test script."
                        ),

                        recommendation=
                        (
                            "Regenerate the missing "
                            "boundary test script."
                        ),
                        impacted_component=
                        "Boundary Test Generation",

                        auto_fixable=
                        True
                    )
                )

                finding_counter += 1

        return findings