from pydantic import BaseModel


class PageElement(BaseModel):

    element_name: str

    element_type: str

    input_type: str | None = None

    locator_type: str | None = None

    locator_value: str | None = None

    label: str | None = None

    aria_label: str | None = None

    placeholder: str | None = None

    required: bool = False


class PageObject(BaseModel):

    page_name: str

    page_url: str

    elements: list[PageElement]