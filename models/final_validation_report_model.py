from pydantic import BaseModel


class FinalValidationReport(BaseModel):

    status: str

    iterations: int

    total_findings: int

    resolved_findings: int

    remaining_findings: int

    patches_applied: int

    reviewers_executed: list[str]

    approval_reason: str