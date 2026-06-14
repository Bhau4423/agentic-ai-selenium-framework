from pydantic import BaseModel

from models.element_model import Element


class Form(BaseModel):

    form_name: str

    elements: list[Element]