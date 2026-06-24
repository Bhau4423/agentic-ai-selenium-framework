from pydantic import BaseModel


class AcceptanceCriteria(BaseModel):

    id: str = ""

    requirement_id: str = ""

    requirement_title: str

    description: str