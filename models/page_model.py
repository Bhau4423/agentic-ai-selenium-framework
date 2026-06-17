from pydantic import BaseModel

from models.element_model import Element
from models.link_model import Link
from models.form_model import Form
from models.table_model import Table


class Page(BaseModel):

    page_name: str

    url: str

    elements: list[Element]

    links: list[Link]

    forms: list[Form] = []

    tables: list[Table] = []