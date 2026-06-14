from pathlib import Path

from playwright.sync_api import (
    sync_playwright
)

from agents.discovery_agent.page_parser import (
    PageParser
)

html_path = (
    Path("test_site.html")
    .absolute()
    .as_uri()
)

with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False
    )

    page = browser.new_page()

    page.goto(html_path)

    textareas = (
        PageParser.extract_textareas(
            page
        )
    )

    print(textareas)

    browser.close()