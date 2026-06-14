from pydantic import BaseModel


class Requirement(BaseModel):

    id: str

    title: str

    description: str