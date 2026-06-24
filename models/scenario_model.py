from pydantic import BaseModel


class TestScenario(BaseModel):

    id: str = ""

    requirement_id: str = ""

    requirement_title: str

    scenario_type: str

    title: str

    steps: list[str]

    expected_result: str