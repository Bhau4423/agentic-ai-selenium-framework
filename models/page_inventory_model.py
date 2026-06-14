from pydantic import BaseModel

from models.page_model import Page


class PageInventory(BaseModel):

    pages: list[Page]