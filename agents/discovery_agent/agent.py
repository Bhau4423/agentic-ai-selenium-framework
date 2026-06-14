from pathlib import Path
import json

from playwright.sync_api import (
    sync_playwright
)

from agents.discovery_agent.page_parser import (
    PageParser
)

from agents.discovery_agent.inventory_builder import (
    InventoryBuilder
)


class DiscoveryAgent:

    def discover(
        self,
        url: str
    ):

        with sync_playwright() as p:

            browser = p.chromium.launch(
                headless=False
            )

            page = browser.new_page()

            page.goto(
                url,
                wait_until="networkidle"
            )

            inputs = (
                PageParser.extract_inputs(
                    page
                )
            )

            buttons = (
                PageParser.extract_buttons(
                    page
                )
            )

            dropdowns = (
                PageParser.extract_dropdowns(
                    page
                )
            )

            checkboxes = (
                PageParser.extract_checkboxes(
                    page
                )
            )

            radio_buttons = (
                PageParser.extract_radio_buttons(
                    page
                )
            )

            textareas = (
                PageParser.extract_textareas(
                    page
                )
            )

            links = (
                PageParser.extract_links(
                    page
                )
            )

            elements = (
                inputs
                + buttons
                + dropdowns
                + checkboxes
                + radio_buttons
                + textareas
            )

            page_object = (
                InventoryBuilder.build_page(
                    page_name=page.title(),
                    url=page.url,
                    elements=elements,
                    links=links
                )
            )

            inventory = (
                InventoryBuilder.build_inventory(
                    [page_object]
                )
            )

            output_dir = Path(
                "output"
            )

            output_dir.mkdir(
                exist_ok=True
            )

            inventory_file = (
                output_dir /
                "page_inventory.json"
            )

            with open(
                inventory_file,
                "w",
                encoding="utf-8"
            ) as file:

                json.dump(
                    inventory.model_dump(),
                    file,
                    indent=4
                )

            print(
                f"\nPage Inventory saved to: {inventory_file}"
            )

            browser.close()

            return inventory