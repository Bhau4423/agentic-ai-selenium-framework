from playwright.sync_api import (
    sync_playwright
)

from agents.discovery_agent.page_parser import (
    PageParser
)


with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False
    )

    page = browser.new_page()

    page.goto(
        "file:///D:/agentic-ai-selenium-framework/test_site.html"
    )

    tables = (
        PageParser.extract_tables(
            page
        )
    )

    print(tables)

    browser.close()