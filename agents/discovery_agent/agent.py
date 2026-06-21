from pathlib import Path
import json

from playwright.sync_api import sync_playwright

from agents.discovery_agent.page_parser import (
    PageParser
)

from agents.discovery_agent.form_parser import (
    FormParser
)

from agents.discovery_agent.inventory_builder import (
    InventoryBuilder
)

from agents.discovery_agent.crawl_controller import (
    CrawlController
)

from agents.discovery_agent.crawl_config import (
    CrawlConfig
)


class DiscoveryAgent:

    def discover_page(
        self,
        page,
        verbose: bool = True
    ):

        if verbose:

            print(
                f"Discovered: {page.title()}"
            )

        try:

            tables = (
                PageParser.extract_tables(
                    page
                )
            )

        except:

            tables = []

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

        forms = (
            FormParser.extract_forms(
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

        page_obj = (
            InventoryBuilder.build_page(
                page_name=page.title(),
                url=page.url,
                elements=elements,
                links=links,
                forms=forms,
                tables=tables
            )
        )

        return page_obj

    def save_inventory(
        self,
        inventory,
        verbose: bool = True
    ):

        output_dir = Path(
            "output"
        )

        output_dir.mkdir(
            exist_ok=True
        )

        inventory_file = (
            output_dir
            / "page_inventory.json"
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

        if verbose:

            print(
                f"\nPage Inventory saved to: "
                f"{inventory_file}"
            )

        return str(
            inventory_file
        )

    def discover(
        self,
        url: str,
        verbose: bool = True
    ):

        config = CrawlConfig()

        controller = CrawlController(
            config
        )

        crawl_results = (
            controller.run(url)
        )

        pages = []

        total_elements = 0
        total_forms = 0
        total_links = 0
        total_tables = 0

        with sync_playwright() as p:

            browser = p.chromium.launch(
                headless=False
            )

            for result in crawl_results:

                try:

                    page = (
                        browser.new_page()
                    )

                    page.goto(
                        result["url"],
                        wait_until="domcontentloaded",
                        timeout=15000
                    )

                    page_data = (
                        self.discover_page(
                            page,
                            verbose
                        )
                    )

                    if page_data:

                        pages.append(
                            page_data
                        )

                        total_elements += len(
                            page_data.elements
                        )

                        total_forms += len(
                            page_data.forms
                        )

                        total_links += len(
                            page_data.links
                        )

                        total_tables += len(
                            page_data.tables
                        )

                    page.close()

                except Exception as e:

                    if verbose:

                        print(
                            f"Failed to parse page: "
                            f"{result['url']}"
                        )

                        print(e)

            browser.close()

        inventory = (
            InventoryBuilder.build_inventory(
                pages
            )
        )

        inventory_file = (
            self.save_inventory(
                inventory,
                verbose
            )
        )

        graph_data = (
            controller.graph.get_graph()
        )

        return {

            "inventory":
                inventory,

            "crawl_graph":
                graph_data,

            "pages":
                len(
                    pages
                ),

            "elements":
                total_elements,

            "forms":
                total_forms,

            "links":
                total_links,

            "tables":
                total_tables,

            "inventory_file":
                inventory_file
        }