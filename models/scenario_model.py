from pydantic import BaseModel


class TestScenario(BaseModel):

    id: str

    scenario_type: str

    title: str

    steps: list[str]

    expected_result: str