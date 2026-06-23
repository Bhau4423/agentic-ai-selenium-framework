from pydantic import BaseModel

from models.semantic_element_model import (
    SemanticElement
)


class ScenarioMapping(BaseModel):

    scenario_id: str

    scenario_title: str

    scenario_type: str

    page_name: str

    page_url: str

    confidence_score: float

    mapping_quality: str

    matched_elements: list[
        SemanticElement
    ]