from urllib.parse import urljoin
from urllib.parse import urlparse


class LinkFilter:

    @staticmethod
    def normalize_url(
        base_url: str,
        href: str
    ) -> str:

        return urljoin(
            base_url,
            href
        )

    @staticmethod
    def is_valid_link(
        href: str
    ) -> bool:

        if not href:
            return False

        if href.startswith("#"):
            return False

        if href.startswith("mailto:"):
            return False

        if href.startswith("javascript:"):
            return False

        return True