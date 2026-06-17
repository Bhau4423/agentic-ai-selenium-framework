from pydantic import BaseModel


class Table(BaseModel):

    table_name: str

    table_id: str | None = None

    row_count: int = 0

    column_count: int = 0

    headers: list[str] = []