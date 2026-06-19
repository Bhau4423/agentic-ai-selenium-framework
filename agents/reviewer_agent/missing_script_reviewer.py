import json
from pathlib import Path

from models.review_finding_model import (
    ReviewFinding
)


class MissingScriptReviewer:

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

        scenario_groups = [

            "positive_scenarios",
            "negative_scenarios",
            "boundary_scenarios"
        ]

        for group in scenario_groups:

            scenarios.extend(
                data.get(
                    group,
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
            MissingScriptReviewer.load_scenarios()
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

            expected_file = (
                MissingScriptReviewer.create_expected_test_name(
                    scenario.get(
                        "title",
                        ""
                    )
                )
            )

            if (
                expected_file
                not in generated_tests
            ):

                findings.append(

                    ReviewFinding(

                        finding_id=
                        f"SCR-{finding_counter:03}",

                        severity=
                        "HIGH",

                        category=
                        "MISSING_TEST_SCRIPT",

                        file_name=
                        expected_file,

                        scenario_id=
                        scenario.get(
                            "id"
                        ),

                        requirement_id=
                        scenario.get(
                            "requirement_id"
                        ),

                        description=
                        "Scenario exists but test script was not generated.",

                        recommendation=
                        "Generate missing test script.",

                        impacted_component=
                        "Test Generation",

                        auto_fixable=
                        True
                    )
                )

                finding_counter += 1

        return findings