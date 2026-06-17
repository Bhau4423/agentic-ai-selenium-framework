from pydantic import BaseModel


class CrawlConfig(BaseModel):

    max_depth: int = 1

    max_pages: int = 3

    same_domain_only: bool = True