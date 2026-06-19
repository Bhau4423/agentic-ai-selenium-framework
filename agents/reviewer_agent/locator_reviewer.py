import json
import re
from pathlib import Path

from models.review_finding_model import (
    ReviewFinding
)

from agents.reviewer_agent.element_name_normalizer import (
    ElementNameNormalizer
)


class LocatorReviewer:

    @staticmethod
    def load_inventory():

        inventory_file = Path(
            "output/page_inventory.json"
        )

        if not inventory_file.exists():

            return set()

        with open(
            inventory_file,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(
                file
            )

        inventory_elements = set()

        for page in data.get(
            "pages",
            []
        ):

            for element in page.get(
                "elements",
                []
            ):

                element_name = (
                    element.get(
                        "element_name",
                        ""
                    )
                )

                normalized = (
                    ElementNameNormalizer.normalize(
                        element_name
                    )
                )

                if normalized:

                    inventory_elements.add(
                        normalized
                    )

        return inventory_elements

    @staticmethod
    def extract_page_elements(
        java_content: str
    ):

        pattern = (
            r"private WebElement\s+(\w+);"
        )

        return set(
            re.findall(
                pattern,
                java_content
            )
        )

    @staticmethod
    def extract_getters(
        java_content: str
    ):

        pattern = (
            r"public WebElement get_(\w+)\("
        )

        return set(
            re.findall(
                pattern,
                java_content
            )
        )

    @staticmethod
    def review():

        findings = []

        inventory_elements = (
            LocatorReviewer.load_inventory()
        )

        pages_folder = Path(
            "generated_framework/pages"
        )

        if not pages_folder.exists():

            return findings

        finding_counter = 1

        for java_file in pages_folder.glob(
            "*.java"
        ):

            with open(
                java_file,
                "r",
                encoding="utf-8"
            ) as file:

                content = (
                    file.read()
                )

            page_elements = (
                LocatorReviewer.extract_page_elements(
                    content
                )
            )

            getters = (
                LocatorReviewer.extract_getters(
                    content
                )
            )

            # -------------------------
            # CHECK 1
            # MISSING GETTER
            # -------------------------

            for element in page_elements:

                if element not in getters:

                    findings.append(

                        ReviewFinding(

                            finding_id=
                            f"LOC-{finding_counter:03}",

                            severity=
                            "HIGH",

                            category=
                            "LOCATOR_MISSING_GETTER",

                            file_name=
                            java_file.name,

                            description=
                            f"Getter missing for locator: {element}",

                            recommendation=
                            "Generate getter method.",

                            impacted_component=
                            "Page Object",

                            auto_fixable=
                            True
                        )
                    )

                    finding_counter += 1

            # -------------------------
            # CHECK 2
            # TRUE HALLUCINATION
            # -------------------------

            for element in page_elements:

                normalized_element = (
                    ElementNameNormalizer.normalize(
                        element
                    )
                )

                if (
                    normalized_element
                    not in inventory_elements
                ):

                    findings.append(

                        ReviewFinding(

                            finding_id=
                            f"LOC-{finding_counter:03}",

                            severity=
                            "HIGH",

                            category=
                            "HALLUCINATED_LOCATOR",

                            file_name=
                            java_file.name,

                            description=
                            f"Locator not found in inventory: {element}",

                            recommendation=
                            "Validate locator mapping.",

                            impacted_component=
                            "Page Object",

                            auto_fixable=
                            True
                        )
                    )

                    finding_counter += 1

        return findings