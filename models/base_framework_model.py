from pydantic import BaseModel


class BaseFramework(BaseModel):

    framework_name: str

    package_name: str