from pydantic import BaseModel


class PageMapping(BaseModel):

    requirement_id: str

    requirement_title: str

    page_name: str

    page_url: str

    matched_elements: list[str] = []

    match_score: float = 0.0