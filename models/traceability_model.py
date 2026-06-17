from pydantic import BaseModel


class Traceability(BaseModel):

    requirement_id: str

    page_name: str

    generated_page_object: str

    generated_test_class: str