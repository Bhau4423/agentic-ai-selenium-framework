from agents.discovery_agent.link_filter import (
    LinkFilter
)


class LinkExtractor:

    @staticmethod
    def extract_urls(
        base_url: str,
        links: list
    ) -> list[str]:

        urls = []

        for link in links:

            href = link.href

            if not LinkFilter.is_valid_link(
                href
            ):
                continue

            normalized_url = (
                LinkFilter.normalize_url(
                    base_url,
                    href
                )
            )

            urls.append(
                normalized_url
            )

        return urls