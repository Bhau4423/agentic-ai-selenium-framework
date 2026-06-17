from models.crawl_state_model import CrawlState

from agents.discovery_agent.url_manager import (
    URLManager
)

from agents.discovery_agent.crawler import (
    Crawler
)

from models.crawl_graph_model import (
    CrawlGraph
)


class CrawlController:

    def __init__(self, config):

        self.config = config

        self.state = CrawlState()

        self.crawler = Crawler()

        self.graph = CrawlGraph()

    def is_application_page(
        self,
        url: str
    ):

        url = url.lower()

        allowed_keywords = [

            "login",
            "register",
            "signup",
            "dashboard",
            "form",
            "contact",
            "profile",
            "account",
            "checkout"
        ]

        # Always allow start page
        if "practice-test-login" in url:
            return True

        for keyword in allowed_keywords:

            if keyword in url:
                return True

        return False

    def run(
        self,
        start_url: str
    ):

        self.state.push_url(
            1.0,
            start_url
        )

        crawl_results = []

        while (
            not self.state.is_empty()
            and
            self.state.pages_crawled
            < self.config.max_pages
        ):

            current_url = (
                self.state.pop_url()
            )

            if not current_url:
                continue

            if (
                current_url
                in self.state.visited_urls
            ):
                continue

            print(
                f"Discovering: {current_url}"
            )

            try:

                result = (
                    self.crawler.crawl(
                        current_url
                    )
                )

            except Exception as e:

                print(
                    f"Failed: {e}"
                )

                continue

            crawl_results.append(
                {
                    "url": current_url,
                    "data": result
                }
            )

            self.state.visited_urls.add(
                current_url
            )

            self.state.pages_crawled += 1

            links = result.get(
                "links",
                []
            )

            for link in links:

                href = link.get(
                    "href"
                )

                normalized = (
                    URLManager.normalize_url(
                        current_url,
                        href
                    )
                )

                if not normalized:
                    continue

                if not URLManager.should_visit(
                    start_url,
                    normalized,
                    self.state.visited_urls
                ):
                    continue

                if not self.is_application_page(
                    normalized
                ):
                    continue

                self.graph.add_edge(
                    current_url,
                    normalized
                )

                self.state.push_url(
                    0.5,
                    normalized
                )

        return crawl_results