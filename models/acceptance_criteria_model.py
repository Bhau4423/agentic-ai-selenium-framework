from pydantic import BaseModel


class AcceptanceCriteria(BaseModel):

    id: str

    requirement_id: str

    description: str