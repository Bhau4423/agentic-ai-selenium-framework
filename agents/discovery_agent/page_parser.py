from models.element_model import Element
from models.link_model import Link
from models.table_model import Table

from agents.discovery_agent.locator_builder import LocatorBuilder


class PageParser:

    @staticmethod
    def extract_inputs(page):

        elements = []

        inputs = page.locator(
            "input:not([type='checkbox']):not([type='radio']):not([type='hidden'])"
        )

        count = inputs.count()

        for index in range(count):

            input_element = inputs.nth(index)

            locator = LocatorBuilder.build(
                input_element
            )

            element = Element(
                element_name=(
                    input_element.get_attribute("name")
                    or f"input_{index}"
                ),
                element_type="input",
                visible_text="",
                locator=locator,
                placeholder=input_element.get_attribute(
                    "placeholder"
                ),
                required=(
                    input_element.get_attribute("required")
                    is not None
                ),
                enabled=input_element.is_enabled(),
                visible=input_element.is_visible()
            )

            elements.append(element)

        return elements

    @staticmethod
    def extract_buttons(page):

        elements = []

        buttons = page.locator("button")

        count = buttons.count()

        for index in range(count):

            button = buttons.nth(index)

            locator = LocatorBuilder.build(
                button
            )

            element = Element(
                element_name=(
                    button.inner_text().strip()
                    or f"button_{index}"
                ),
                element_type="button",
                visible_text=button.inner_text().strip(),
                locator=locator,
                enabled=button.is_enabled(),
                visible=button.is_visible()
            )

            elements.append(element)

        return elements

    @staticmethod
    def extract_dropdowns(page):

        elements = []

        dropdowns = page.locator("select")

        count = dropdowns.count()

        for index in range(count):

            dropdown = dropdowns.nth(index)

            locator = LocatorBuilder.build(
                dropdown
            )

            element = Element(
                element_name=(
                    dropdown.get_attribute("name")
                    or f"dropdown_{index}"
                ),
                element_type="dropdown",
                visible_text="",
                locator=locator,
                enabled=dropdown.is_enabled(),
                visible=dropdown.is_visible()
            )

            elements.append(element)

        return elements

    @staticmethod
    def extract_checkboxes(page):

        elements = []

        checkboxes = page.locator(
            "input[type='checkbox']"
        )

        count = checkboxes.count()

        for index in range(count):

            checkbox = checkboxes.nth(index)

            locator = LocatorBuilder.build(
                checkbox
            )

            element = Element(
                element_name=(
                    checkbox.get_attribute("name")
                    or f"checkbox_{index}"
                ),
                element_type="checkbox",
                visible_text="",
                locator=locator,
                required=(
                    checkbox.get_attribute("required")
                    is not None
                ),
                enabled=checkbox.is_enabled(),
                visible=checkbox.is_visible()
            )

            elements.append(element)

        return elements

    @staticmethod
    def extract_radio_buttons(page):

        elements = []

        radio_buttons = page.locator(
            "input[type='radio']"
        )

        count = radio_buttons.count()

        for index in range(count):

            radio = radio_buttons.nth(index)

            locator = LocatorBuilder.build(
                radio
            )

            element = Element(
                element_name=(
                    radio.get_attribute("id")
                    or f"radio_{index}"
                ),
                element_type="radio",
                visible_text="",
                locator=locator,
                required=(
                    radio.get_attribute("required")
                    is not None
                ),
                enabled=radio.is_enabled(),
                visible=radio.is_visible()
            )

            elements.append(element)

        return elements

    @staticmethod
    def extract_textareas(page):

        elements = []

        textareas = page.locator("textarea")

        count = textareas.count()

        for index in range(count):

            textarea = textareas.nth(index)

            locator = LocatorBuilder.build(
                textarea
            )

            element = Element(
                element_name=(
                    textarea.get_attribute("name")
                    or f"textarea_{index}"
                ),
                element_type="textarea",
                visible_text="",
                locator=locator,
                placeholder=textarea.get_attribute(
                    "placeholder"
                ),
                required=(
                    textarea.get_attribute("required")
                    is not None
                ),
                enabled=textarea.is_enabled(),
                visible=textarea.is_visible()
            )

            elements.append(element)

        return elements

    @staticmethod
    def extract_links(page):

        links = []

        anchors = page.locator("a")

        count = anchors.count()

        for index in range(count):

            anchor = anchors.nth(index)

            link = Link(
                text=anchor.inner_text().strip(),
                href=anchor.get_attribute("href")
            )

            links.append(link)

        return links

    @staticmethod
    def extract_tables(page):

        tables = []

        table_elements = page.locator("table")

        count = table_elements.count()

        for index in range(count):

            table = table_elements.nth(index)

            headers = []

            header_elements = table.locator("th")

            header_count = header_elements.count()

            for header_index in range(header_count):

                headers.append(
                    header_elements.nth(
                        header_index
                    ).inner_text().strip()
                )

            tables.append(
                Table(
                    table_name=(
                        table.get_attribute("id")
                        or f"table_{index}"
                    ),
                    table_id=table.get_attribute("id"),
                    row_count=table.locator(
                        "tr"
                    ).count(),
                    column_count=len(headers),
                    headers=headers
                )
            )

        return tables