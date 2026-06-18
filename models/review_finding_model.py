from pydantic import BaseModel


class ReviewFinding(BaseModel):

    finding_id: str

    severity: str

    category: str

    file_name: str

    description: str

    recommendation: str