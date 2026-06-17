from agents.discovery_agent.crawl_config import (
    CrawlConfig
)

from agents.discovery_agent.crawl_controller import (
    CrawlController
)

config = CrawlConfig(
    max_pages=3
)

controller = CrawlController(
    config
)

results = controller.run(
    "https://example.com"
)

print(results)

print()

print(
    controller.state
)