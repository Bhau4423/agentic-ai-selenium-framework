from pydantic import BaseModel


class Link(BaseModel):

    text: str

    href: str | None = None