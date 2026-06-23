from pydantic import BaseModel


class ApplicationUrl(BaseModel):

    page_name: str

    url: str