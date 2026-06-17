from pathlib import Path

from playwright.sync_api import (
    sync_playwright
)

from agents.discovery_agent.form_parser import (
    FormParser
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

    forms = (
        FormParser.extract_forms(
            page
        )
    )

    print(forms)

    browser.close()