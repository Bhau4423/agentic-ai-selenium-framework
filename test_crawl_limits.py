from agents.discovery_agent.crawl_config import (
    CrawlConfig
)

from agents.discovery_agent.crawl_controller import (
    CrawlController
)

config = CrawlConfig(
    max_pages=2
)

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
    controller.can_continue()
)

url = controller.get_next_url()

controller.mark_visited(
    url
)

print(
    controller.can_continue()
)

url = controller.get_next_url()

controller.mark_visited(
    url
)

print(
    controller.can_continue()
)