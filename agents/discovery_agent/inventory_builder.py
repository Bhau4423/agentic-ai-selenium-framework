from models.page_model import Page
from models.page_inventory_model import PageInventory


class InventoryBuilder:

    @staticmethod
    def build_page(
        page_name: str,
        url: str,
        elements: list,
        links: list,
        forms: list,
        tables: list
    ) -> Page:

        return Page(
            page_name=page_name,
            url=url,
            elements=elements,
            links=links,
            forms=forms,
            tables=tables
        )

    @staticmethod
    def build_inventory(
        pages: list[Page]
    ) -> PageInventory:

        return PageInventory(
            pages=pages
        )