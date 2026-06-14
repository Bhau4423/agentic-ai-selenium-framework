from models.element_model import Element
from models.link_model import Link
from pydantic import BaseModel


class Page(BaseModel):

    page_name: str

    url: str

    elements: list[Element]

    links: list[Link]