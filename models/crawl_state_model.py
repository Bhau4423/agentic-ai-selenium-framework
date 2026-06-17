from dataclasses import dataclass, field
import heapq


@dataclass
class CrawlState:

    # -------------------------
    # TRACK VISITED URLS
    # -------------------------
    visited_urls: set = field(default_factory=set)

    # -------------------------
    # COUNT PAGES CRAWLED
    # -------------------------
    pages_crawled: int = 0

    # -------------------------
    # PRIORITY QUEUE STORAGE
    # (min-heap used as max-heap via negative priority)
    # -------------------------
    url_queue: list = field(default_factory=list)

    # -------------------------
    # ADD URL WITH PRIORITY
    # -------------------------
    def push_url(self, priority: int, url: str):

        if not url:
            return

        heapq.heappush(self.url_queue, (-priority, url))

    # -------------------------
    # GET NEXT URL (HIGHEST PRIORITY)
    # -------------------------
    def pop_url(self):

        if not self.url_queue:
            return None

        return heapq.heappop(self.url_queue)[1]

    # -------------------------
    # HELPER: CHECK IF EMPTY
    # -------------------------
    def is_empty(self):

        return len(self.url_queue) == 0