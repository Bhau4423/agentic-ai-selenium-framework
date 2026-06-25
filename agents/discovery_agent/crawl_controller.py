from models.crawl_state_model import CrawlState

from agents.discovery_agent.crawler import (
    Crawler
)

from models.crawl_graph_model import (
    CrawlGraph
)


class CrawlController:

    def __init__(
        self,
        config
    ):

        self.config = config

        self.state = CrawlState()

        self.crawler = Crawler()

        self.graph = CrawlGraph()

    def run(
        self,
        start_urls: list[str]
    ):

        # -------------------------
        # Seed URLs from Agent 1
        # -------------------------

        for url in start_urls:

            self.state.push_url(
                1.0,
                url
            )

        crawl_results = []

        # -------------------------
        # Crawl only supplied URLs
        # -------------------------

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

            # print(
            #     f"Discovering: "
            #     f"{current_url}"
            # )

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
                    "url":
                        current_url,

                    "data":
                        result
                }
            )

            self.state.visited_urls.add(
                current_url
            )

            self.state.pages_crawled += 1

            # -------------------------
            # Store page relationships
            # DO NOT enqueue links
            # -------------------------

            links = result.get(
                "links",
                []
            )

            for link in links:

                href = link.get(
                    "href"
                )

                if not href:
                    continue

                self.graph.add_edge(
                    current_url,
                    href
                )

        print(
            f"\nTotal Crawled Pages: "
            f"{len(crawl_results)}"
        )

        return crawl_results