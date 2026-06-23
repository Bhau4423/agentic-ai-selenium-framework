from pydantic import BaseModel


class CrawlConfig(BaseModel):

    # -------------------------
    # Maximum crawl depth
    # -------------------------
    max_depth: int = 3

    # -------------------------
    # Maximum pages allowed
    # -------------------------
    max_pages: int = 100

    # -------------------------
    # Stay inside application
    # -------------------------
    same_domain_only: bool = True

    # -------------------------
    # Run browser hidden
    # -------------------------
    headless: bool = True

    # -------------------------
    # Page timeout
    # -------------------------
    timeout: int = 30000