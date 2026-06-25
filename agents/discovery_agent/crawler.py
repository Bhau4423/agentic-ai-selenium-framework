from playwright.sync_api import (
    sync_playwright
)

from agents.discovery_agent.url_manager import (
    URLManager
)


class Crawler:

    def crawl(
        self,
        url: str
    ):

        try:

            with sync_playwright() as p:

                browser = p.chromium.launch(
                    headless=True
                )

                page = browser.new_page()

                # print( f"Opening URL: {url}")
                page.goto(
                     url,
                     wait_until="domcontentloaded",
                     timeout=30000
                )


                page.wait_for_timeout(
                    2000
                )

                page_title = (
                    page.title()
                )

                current_url = (
                    page.url
                )

                links = []

                try:

                    link_elements = (
                        page.locator("a")
                    )

                    count = (
                        link_elements.count()
                    )

                except:

                    count = 0

                for index in range(
                    count
                ):

                    try:

                        link = (
                            link_elements.nth(
                                index
                            )
                        )

                        text = (
                            link
                            .inner_text()
                            .strip()
                        )

                        href = (
                            link.get_attribute(
                                "href"
                            )
                        )

                        safe_url = (
                            URLManager
                            .normalize_url(
                                current_url,
                                href
                            )
                        )

                        if safe_url:

                            links.append(
                                {
                                    "text":
                                        text,

                                    "href":
                                        safe_url
                                }
                            )

                    except:

                        continue

                browser.close()

                return {

                    "page_title":
                        page_title,

                    "url":
                        current_url,

                    "links":
                        links
                }

        except Exception as e:

            print(
                f"Failed URL: {url}"
            )

            print(e)

            return {

                "page_title": "",

                "url": url,

                "links": []
            }