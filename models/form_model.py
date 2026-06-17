from pydantic import BaseModel
from models.element_model import Element


class Form(BaseModel):

    form_name: str
    form_id: str | None = None

    # 🔥 NEW (optional but important for future AI training)
    form_action: str | None = None
    form_method: str | None = None

    elements: list[Element]