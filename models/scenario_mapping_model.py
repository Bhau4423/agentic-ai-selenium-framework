from pydantic import BaseModel


class ScenarioMapping(BaseModel):

    scenario_id: str

    scenario_title: str

    scenario_type: str

    page_name: str

    matched_elements: list[str]