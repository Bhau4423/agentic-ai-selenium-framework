from agents.discovery_agent.link_filter import (
    LinkFilter
)

print(
    LinkFilter.is_valid_link(
        "/login"
    )
)

print(
    LinkFilter.is_valid_link(
        "mailto:test@test.com"
    )
)

print(
    LinkFilter.normalize_url(
        "https://example.com",
        "/login"
    )
)