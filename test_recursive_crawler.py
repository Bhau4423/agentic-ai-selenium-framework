from models.crawl_config_model import (
    CrawlConfig
)

from agents.discovery_agent.recursive_crawler import (
    RecursiveCrawler
)

config = CrawlConfig()

crawler = RecursiveCrawler(config)

print(
    crawler.should_visit(
        "https://example.com"
    )
)

crawler.mark_visited(
    "https://example.com"
)

print(
    crawler.should_visit(
        "https://example.com"
    )
)