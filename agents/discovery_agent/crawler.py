from playwright.sync_api import sync_playwright
from agents.discovery_agent.url_manager import URLManager


class Crawler:

    def crawl(self, url: str):

        with sync_playwright() as p:

            browser = p.chromium.launch(headless=False)
            page = browser.new_page()

            page.goto(url, wait_until="domcontentloaded")
            page.wait_for_timeout(1000)

            page_title = page.title()
            current_url = page.url

            links = []

            link_elements = page.locator("a")
            count = link_elements.count()

            for index in range(count):

                link = link_elements.nth(index)

                text = link.inner_text().strip()
                href = link.get_attribute("href")

                # 🔥 SAFE URL NORMALIZATION (FIX FOR /register ISSUE)
                safe_url = URLManager.normalize_url(current_url, href)

                if safe_url:
                    links.append({
                        "text": text,
                        "href": safe_url
                    })

            browser.close()

            return {
                "page_title": page_title,
                "url": current_url,
                "links": links
            }