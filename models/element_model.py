from pydantic import BaseModel

from models.locator_model import Locator


class Element(BaseModel):

    element_name: str

    element_type: str

    visible_text: str

    locator: Locator

    input_type: str | None = None

    label: str | None = None

    aria_label: str | None = None

    placeholder: str | None = None

    required: bool = False

    enabled: bool = True

    visible: bool = True