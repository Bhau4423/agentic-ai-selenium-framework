from agents.discovery_agent.crawl_config import (
    CrawlConfig
)

from agents.discovery_agent.crawl_controller import (
    CrawlController
)

config = CrawlConfig()

controller = CrawlController(
    config
)

controller.add_url(
    "https://example.com"
)

controller.add_url(
    "https://example.com/login"
)

print(
    controller.state
)

url = controller.get_next_url()

print(
    "Next URL:",
    url
)

controller.mark_visited(
    url
)

print(
    controller.state
)