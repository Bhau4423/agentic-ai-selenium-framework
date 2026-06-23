from pydantic import BaseModel


class Traceability(BaseModel):

    requirement_id: str

    requirement_title: str

    acceptance_criteria_ids: list[str]

    scenario_ids: list[str]

    page_name: str | None = None

    page_url: str | None = None

    mapped_elements: list[str] = []