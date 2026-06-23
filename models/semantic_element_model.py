from pydantic import BaseModel


class SemanticElement(BaseModel):

    element_name: str

    element_type: str

    locator: dict

    confidence_score: float = 0.0