from pydantic import BaseModel


class ScenarioContext(BaseModel):

    scenario_id: str

    requirement_id: str

    scenario_title: str

    scenario_type: str

    steps: list[str]

    expected_result: str