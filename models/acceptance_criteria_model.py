from pydantic import BaseModel


class AcceptanceCriteria(BaseModel):

    id: str

    description: str