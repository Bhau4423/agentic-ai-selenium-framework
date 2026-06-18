from pydantic import BaseModel


class TestData(BaseModel):

    email: str

    password: str

    first_name: str

    last_name: str

    phone: str