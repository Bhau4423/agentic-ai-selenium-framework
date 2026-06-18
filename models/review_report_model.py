from pydantic import BaseModel

from models.review_finding_model import (
    ReviewFinding
)


class ReviewReport(BaseModel):

    iteration: int

    status: str

    total_findings: int

    findings: list[ReviewFinding]