from urllib.parse import urljoin
from urllib.parse import urlparse


class URLManager:

    @staticmethod
    def normalize_url(
        base_url: str,
        href: str
    ):

        if not href:
            return None

        href = href.strip()

        if href.startswith("#"):
            return None

        if href.startswith("javascript:"):
            return None

        if href.startswith("mailto:"):
            return None

        return urljoin(
            base_url,
            href
        )

    @staticmethod
    def should_visit(
        start_url: str,
        url: str,
        visited: set
    ):

        if not url:
            return False

        if url in visited:
            return False

        start_domain = (
            urlparse(start_url)
            .netloc
            .replace("www.", "")
        )

        target_domain = (
            urlparse(url)
            .netloc
            .replace("www.", "")
        )

        if start_domain != target_domain:
            return False

        return True