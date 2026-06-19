import re
from pathlib import Path

from models.review_finding_model import (
    ReviewFinding
)


class HallucinationReviewer:

    @staticmethod
    def load_page_getters():

        page_folder = Path(
            "generated_framework/pages"
        )

        getters = set()

        if not page_folder.exists():

            return getters

        pattern = (
            r"public WebElement get_(\w+)\("
        )

        for java_file in page_folder.glob(
            "*.java"
        ):

            with open(
                java_file,
                "r",
                encoding="utf-8"
            ) as file:

                content = file.read()

            matches = re.findall(
                pattern,
                content
            )

            getters.update(
                matches
            )

        return getters

    @staticmethod
    def review():

        findings = []

        getters = (
            HallucinationReviewer.load_page_getters()
        )

        tests_folder = Path(
            "generated_framework/tests"
        )

        if not tests_folder.exists():

            return findings

        finding_counter = 1

        getter_pattern = (
            r"page\.get_(\w+)\("
        )

        for java_file in tests_folder.glob(
            "*.java"
        ):

            with open(
                java_file,
                "r",
                encoding="utf-8"
            ) as file:

                content = file.read()

            referenced_getters = (
                re.findall(
                    getter_pattern,
                    content
                )
            )

            for getter in referenced_getters:

                if getter not in getters:

                    findings.append(

                        ReviewFinding(

                            finding_id=
                            f"HAL-{finding_counter:03}",

                            severity=
                            "HIGH",

                            category=
                            "HALLUCINATED_METHOD",

                            file_name=
                            java_file.name,

                            description=
                            f"Getter not found in generated page objects: get_{getter}()",

                            recommendation=
                            "Validate page object mapping.",

                            impacted_component=
                            "Generated Test",

                            auto_fixable=
                            True
                        )
                    )

                    finding_counter += 1

        return findings