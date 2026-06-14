from playwright.sync_api import (
    sync_playwright
)


class Crawler:

    def crawl(
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

            page_title = page.title()

            current_url = page.url

            links = []

            link_elements = page.locator("a")

            count = link_elements.count()

            for index in range(count):

                link = link_elements.nth(index)

                text = link.inner_text().strip()

                href = link.get_attribute("href")

                links.append(
                    {
                        "text": text,
                        "href": href
                    }
                )

            browser.close()

            return {
                "page_title": page_title,
                "url": current_url,
                "links": links
            }