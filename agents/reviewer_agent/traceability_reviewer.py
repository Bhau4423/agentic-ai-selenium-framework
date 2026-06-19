import json
from pathlib import Path

from models.review_finding_model import (
    ReviewFinding
)


class TraceabilityReviewer:

    @staticmethod
    def load_scenarios():

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

        scenarios = []

        scenarios.extend(
            data.get(
                "positive_scenarios",
                []
            )
        )

        scenarios.extend(
            data.get(
                "negative_scenarios",
                []
            )
        )

        scenarios.extend(
            data.get(
                "boundary_scenarios",
                []
            )
        )

        return scenarios

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

        scenarios = (
            TraceabilityReviewer.load_scenarios()
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

        for scenario in scenarios:

            expected_test = (
                TraceabilityReviewer.create_expected_test_name(
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
                        f"TRC-{finding_counter:03}",

                        severity=
                        "CRITICAL",

                        category=
                        "REQUIREMENT_NOT_COVERED",

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
                        "Requirement scenario is not covered by generated test.",

                        recommendation=
                        "Generate missing test and update traceability.",

                        impacted_component=
                        "Traceability",

                        auto_fixable=
                        True
                    )
                )

                finding_counter += 1

        return findings