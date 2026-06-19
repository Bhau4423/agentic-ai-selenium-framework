import json
from pathlib import Path

from models.review_finding_model import (
    ReviewFinding
)


class EdgeCaseReviewer:

    @staticmethod
    def load_boundary_scenarios():

        file_path = Path(
            "data/intermediate/requirement_analysis.json"
        )

        if not file_path.exists():

            return []

        with open(
            file_path,
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

        tests_folder = Path(
            "generated_framework/tests"
        )

        generated_tests = set()

        if tests_folder.exists():

            for java_file in tests_folder.glob(
                "*.java"
            ):

                generated_tests.add(
                    java_file.name
                )

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
                        "Boundary scenario exists but no test was generated.",

                        recommendation=
                        "Generate missing boundary test.",

                        impacted_component=
                        "Test Coverage",

                        auto_fixable=
                        True
                    )
                )

                finding_counter += 1

        return findings