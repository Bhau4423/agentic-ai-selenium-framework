from pydantic import BaseModel


class SemanticValidationFinding(
    BaseModel
):

    scenario_id: str

    scenario_title: str

    severity: str

    finding: str

    recommendation: str