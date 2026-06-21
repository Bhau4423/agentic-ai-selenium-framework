from pydantic import BaseModel

from typing import Optional


class PatchPlan(BaseModel):

    finding_id: str

    file_name: str

    category: str

    patch_action: str

    reason: str

    patch_status: str = "PENDING"

    # ---------------------------------
    # TRACEABILITY
    # ---------------------------------

    scenario_id: Optional[str] = None

    requirement_id: Optional[str] = None

    # ---------------------------------
    # LOCATOR PATCHING
    # ---------------------------------

    target_element: Optional[str] = None

    replacement_element: Optional[str] = None

    # ---------------------------------
    # METHOD PATCHING
    # ---------------------------------

    target_method: Optional[str] = None

    replacement_method: Optional[str] = None

    # ---------------------------------
    # ASSERTION PATCHING
    # ---------------------------------

    target_assertion: Optional[str] = None

    replacement_assertion: Optional[str] = None

    # ---------------------------------
    # NOTES
    # ---------------------------------

    notes: Optional[str] = None