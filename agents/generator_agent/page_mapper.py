from pathlib import Path
import json

from models.page_object_model import (
    PageObject,
    PageElement
)


class PageMapper:

    @staticmethod
    def load_inventory():

        inventory_file = Path(
            "output/page_inventory.json"
        )

        with open(
            inventory_file,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    @staticmethod
    def get_page_by_name(
        page_name: str
    ):

        inventory = (
            PageMapper.load_inventory()
        )

        pages = inventory.get(
            "pages",
            []
        )

        for page in pages:

            if (
                page.get(
                    "page_name",
                    ""
                )
                == page_name
            ):

                return page

        return None

    @staticmethod
    def get_best_locator(
        locator: dict
    ):

        if not locator:

            return (
                None,
                None
            )

        if locator.get("id"):

            return (
                "id",
                locator["id"]
            )

        if locator.get("name"):

            return (
                "name",
                locator["name"]
            )

        if locator.get("css_selector"):

            return (
                "css_selector",
                locator["css_selector"]
            )

        if locator.get("xpath"):

            return (
                "xpath",
                locator["xpath"]
            )

        return (
            None,
            None
        )

    @staticmethod
    def map_requirement_to_page(
        page_mapping
    ):

        page = (
            PageMapper.get_page_by_name(
                page_mapping.page_name
            )
        )

        if not page:

            return None

        page_elements = []

        elements = page.get(
            "elements",
            []
        )

        for element in elements:

            locator = element.get(
                "locator",
                {}
            )

            locator_type, locator_value = (
                PageMapper.get_best_locator(
                    locator
                )
            )

            page_elements.append(
                PageElement(

                    element_name=element.get(
                        "element_name",
                        ""
                    ),

                    element_type=element.get(
                        "element_type",
                        ""
                    ),

                    input_type=element.get(
                        "input_type"
                    ),

                    locator_type=locator_type,

                    locator_value=locator_value,

                    label=element.get(
                        "label"
                    ),

                    aria_label=element.get(
                        "aria_label"
                    ),

                    placeholder=element.get(
                        "placeholder"
                    ),

                    required=element.get(
                        "required",
                        False
                    )
                )
            )

        return PageObject(

            page_name=page.get(
                "page_name",
                ""
            ),

            page_url=page.get(
                "url",
                ""
            ),

            elements=page_elements
        )

    @staticmethod
    def build_page_objects(
        mappings
    ):

        page_objects = []

        processed_pages = set()

        for mapping in mappings:

            if (
                mapping.page_name
                in processed_pages
            ):
                continue

            page_object = (
                PageMapper.map_requirement_to_page(
                    mapping
                )
            )

            if page_object:

                page_objects.append(
                    page_object
                )

                processed_pages.add(
                    mapping.page_name
                )

        return page_objects