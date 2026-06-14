from pathlib import Path

from agents.discovery_agent.agent import (
    DiscoveryAgent
)

html_path = (
    Path("test_site.html")
    .absolute()
    .as_uri()
)

agent = DiscoveryAgent()

inventory = agent.discover(
    html_path
)

print(inventory)