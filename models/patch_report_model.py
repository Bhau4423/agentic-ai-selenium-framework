from pydantic import BaseModel

from models.patch_plan_model import (
    PatchPlan
)


class PatchReport(BaseModel):

    iteration: int

    total_patches: int

    successful_patches: int

    failed_patches: int

    patches: list[PatchPlan]