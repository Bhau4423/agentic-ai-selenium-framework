import json
import re

from pathlib import Path
from difflib import get_close_matches


class LocatorRepairEngine:

    GENERIC_PREFIXES = [

        "button_",
        "input_",
        "link_",
        "checkbox_",
        "radio_",
        "dropdown_",
        "textarea_"

    ]

    @staticmethod
    def normalize(
        text: str
    ):

        return (
            text.lower()
            .replace("_", " ")
            .replace("-", " ")
            .strip()
        )

    @staticmethod
    def is_generic_name(
        element_name: str
    ):

        element_name = (
            element_name.lower()
        )

        for prefix in (
            LocatorRepairEngine
            .GENERIC_PREFIXES
        ):

            if (
                element_name.startswith(
                    prefix
                )
            ):

                return True

        return False

    @staticmethod
    def load_inventory_elements():

        inventory_file = Path(
            "output/page_inventory.json"
        )

        if not inventory_file.exists():

            return []

        with open(
            inventory_file,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(
                file
            )

        elements = []

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

                if not element_name:

                    continue

                if (
                    LocatorRepairEngine
                    .is_generic_name(
                        element_name
                    )
                ):

                    continue

                elements.append(
                    element_name
                )

        return list(
            set(elements)
        )

    @staticmethod
    def extract_invalid_element(
        description: str
    ):

        match = re.search(
            r"Locator not found in inventory:\s*(.+)",
            description
        )

        if match:

            return (
                match.group(1)
                .strip()
            )

        return None

    @staticmethod
    def find_replacement(
        invalid_element: str
    ):

        inventory_elements = (
            LocatorRepairEngine
            .load_inventory_elements()
        )

        if not inventory_elements:

            return None

        normalized_inventory = {

            LocatorRepairEngine.normalize(
                element
            ): element

            for element in inventory_elements
        }

        normalized_invalid = (
            LocatorRepairEngine.normalize(
                invalid_element
            )
        )

        matches = get_close_matches(
            normalized_invalid,
            list(
                normalized_inventory.keys()
            ),
            n=1,
            cutoff=0.4
        )

        if matches:

            return (
                normalized_inventory[
                    matches[0]
                ]
            )

        return None

    @staticmethod
    def repair(
        content: str,
        description: str
    ):

        invalid_element = (
            LocatorRepairEngine
            .extract_invalid_element(
                description
            )
        )

        if not invalid_element:

            print(
                "Unable to identify invalid locator."
            )

            return content

        replacement = (
            LocatorRepairEngine
            .find_replacement(
                invalid_element
            )
        )

        print(
            f"Invalid Element: "
            f"{invalid_element}"
        )

        print(
            f"Suggested Replacement: "
            f"{replacement}"
        )

        if not replacement:

            print(
                "No replacement found."
            )

            return content

        print(
            f"Replacing locator: "
            f"{invalid_element}"
            f" -> "
            f"{replacement}"
        )

        content = re.sub(
            rf"\b{re.escape(invalid_element)}\b",
            replacement,
            content
        )

        return content