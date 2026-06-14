from pydantic import BaseModel


class Locator(BaseModel):

    id: str | None = None

    name: str | None = None

    xpath: str | None = None

    css_selector: str | None = None