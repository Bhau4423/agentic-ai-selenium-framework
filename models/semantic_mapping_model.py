from pydantic import BaseModel


class SemanticElement(BaseModel):

    element_name: str

    role: str

    action_type: str


class SemanticMapping(BaseModel):

    scenario_id: str

    scenario_title: str

    page_name: str

    matched_elements: list[SemanticElement]

    confidence_score: float