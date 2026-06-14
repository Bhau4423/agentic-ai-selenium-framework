from models.link_model import Link

from agents.discovery_agent.link_extractor import (
    LinkExtractor
)

links = [

    Link(
        text="Login",
        href="/login"
    ),

    Link(
        text="Email",
        href="mailto:test@test.com"
    )
]

urls = (
    LinkExtractor.extract_urls(
        "https://example.com",
        links
    )
)

print(urls)