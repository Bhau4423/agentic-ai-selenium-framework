from pydantic import BaseModel


class PatchPlan(BaseModel):

    finding_id: str

    file_name: str

    category: str

    patch_action: str

    reason: str

    patch_status: str = "PENDING"