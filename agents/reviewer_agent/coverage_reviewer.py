import json
from pathlib import Path

from agents.generator_agent.generation_manifest import (
    GenerationManifest
)

from models.review_finding_model import (
    ReviewFinding
)


class CoverageReviewer:

    @staticmethod
    def create_test_name(
        title: str
    ):

        words = (
            title
            .replace("-", " ")
            .replace("_", " ")
            .split()
        )

        class_name = ""

        for word in words:

            class_name += (
                word.capitalize()
            )

        return class_name + "Test"

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

        manifest = (
            GenerationManifest.load()
        )

        generated_tests = {

            Path(file).stem

            for file in manifest.get(
            "generated_tests",
            []
        )
    }

        expected_tests = {

            CoverageReviewer.create_test_name(
               scenario.get("title", "")
            )

            for scenario in all_scenarios
        }

        for scenario in all_scenarios:

            scenario_title = (
                scenario.get(
                    "title",
                    ""
                )
            )

            expected_test_name = (
                CoverageReviewer.create_test_name(
                    scenario_title
                )
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
                            f"Generated test missing for scenario: "
                            f"{scenario_title}"
                        ),

                        recommendation=
                        (
                            "Generate missing Java test."
                        ),

                        impacted_component=
                        "Test Generation",

                        auto_fixable=
                        True
                    )
                )

                finding_counter += 1
                # -------------------------
        # ORPHAN TEST DETECTION
        # -------------------------

        for generated_test in generated_tests:

            if generated_test not in expected_tests:

                findings.append(

                    ReviewFinding(

                        finding_id=
                        f"COV-{finding_counter:03d}",

                        severity=
                        "MEDIUM",

                        category=
                        "ORPHAN_TEST",

                        file_name=
                        generated_test + ".java",

                        description=
                        (
                            f"Generated test "
                            f"'{generated_test}' "
                            f"does not match any scenario."
                        ),

                        recommendation=
                        (
                            "Remove the orphan test "
                            "or map it to a valid scenario."
                        ),

                        impacted_component=
                        "Generated Test",

                        auto_fixable=
                        False
                    )
                )

                finding_counter += 1

        return findings