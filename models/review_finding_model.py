from pydantic import BaseModel


class ReviewFinding(BaseModel):

    finding_id: str

    severity: str

    category: str

    file_name: str

    description: str

    recommendation: str

    scenario_id: str | None = None

    requirement_id: str | None = None

    impacted_component: str | None = None

    auto_fixable: bool = True

    validation_status: str = "PENDING"