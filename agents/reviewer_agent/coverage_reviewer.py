import json
from pathlib import Path

from models.review_finding_model import (
    ReviewFinding
)


class CoverageReviewer:

    @staticmethod
    def review():

        findings = []

        finding_counter = 1

        requirement_file = Path(
            "data/intermediate/requirement_analysis.json"
        )

        tests_folder = Path(
            "generated_framework/tests"
        )

        if (
            not requirement_file.exists()
            or
            not tests_folder.exists()
        ):

            return findings

        with open(
            requirement_file,
            "r",
            encoding="utf-8"
        ) as file:

            requirement_data = (
                json.load(file)
            )

        all_scenarios = []

        all_scenarios.extend(
            requirement_data.get(
                "positive_scenarios",
                []
            )
        )

        all_scenarios.extend(
            requirement_data.get(
                "negative_scenarios",
                []
            )
        )

        all_scenarios.extend(
            requirement_data.get(
                "boundary_scenarios",
                []
            )
        )

        generated_tests = {

            file.stem

            for file in tests_folder.glob(
                "*.java"
            )
        }

        for scenario in all_scenarios:

            scenario_title = (
                scenario.get(
                    "title",
                    ""
                )
            )

            expected_test_name = (
                "".join(
                    word.capitalize()
                    for word in scenario_title.split()
                )
                + "Test"
            )

            if (
                expected_test_name
                not in generated_tests
            ):

                findings.append(

                    ReviewFinding(

                        finding_id=
                        f"COV-{finding_counter:03d}",

                        severity=
                        "HIGH",

                        category=
                        "COVERAGE",

                        file_name=
                        expected_test_name
                        + ".java",

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
                            "Scenario does not "
                            "have generated test."
                        ),

                        recommendation=
                        (
                            "Generate test for "
                            "missing scenario."
                        ),

                        impacted_component=
                        "Test Generation",

                        auto_fixable=
                        True
                    )
                )

                finding_counter += 1

        return findings