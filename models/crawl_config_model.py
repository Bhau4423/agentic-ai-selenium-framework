from pydantic import BaseModel


class CrawlConfig(BaseModel):

    max_depth: int = 2

    max_pages: int = 20

    same_domain_only: bool = True