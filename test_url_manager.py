from agents.discovery_agent.url_manager import (
    URLManager
)


print(
    URLManager.normalize_url(
        "https://example.com",
        "/login"
    )
)

print(
    URLManager.is_same_domain(
        "https://example.com",
        "https://example.com/profile"
    )
)

print(
    URLManager.is_same_domain(
        "https://example.com",
        "https://google.com"
    )
)

visited = {
    "https://example.com/login"
}

print(
    URLManager.should_visit(
        "https://example.com/login",
        visited
    )
)

print(
    URLManager.should_visit(
        "https://example.com/profile",
        visited
    )
)