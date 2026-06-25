import re
from pathlib import Path

from models.review_finding_model import (
    ReviewFinding
)

from agents.reviewer_agent.review_file_provider import (
    ReviewFileProvider
)


class HallucinationReviewer:

    @staticmethod
    def load_page_getters():

        java_files = (
            ReviewFileProvider
            .get_generated_page_files()
        )

        getters = set()

        if not java_files:

            return getters

        pattern = (
            r"public WebElement get_(\w+)\("
        )

        for java_file in java_files:

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

        java_files = (
            ReviewFileProvider
            .get_generated_page_files()
        )

        if not java_files:

            return findings

        finding_counter = 1

        getter_pattern = (
            r"page\.get_(\w+)\("
        )

        for java_file in java_files:

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