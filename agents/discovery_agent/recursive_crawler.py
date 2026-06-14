from urllib.parse import urlparse


class RecursiveCrawler:

    def __init__(self, config):

        self.config = config

        self.visited_urls = set()

    def should_visit(
        self,
        url: str
    ) -> bool:

        if not url:
            return False

        if url in self.visited_urls:
            return False

        if len(self.visited_urls) >= self.config.max_pages:
            return False

        return True

    def mark_visited(
        self,
        url: str
    ):

        self.visited_urls.add(url)