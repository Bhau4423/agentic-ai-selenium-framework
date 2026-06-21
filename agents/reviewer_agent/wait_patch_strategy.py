from models.review_finding_model import (
    ReviewFinding
)

from models.patch_plan_model import (
    PatchPlan
)


class WaitPatchStrategy:

    @staticmethod
    def create_patch(
        finding: ReviewFinding
    ):

        return PatchPlan(

            finding_id=
            finding.finding_id,

            file_name=
            finding.file_name,

            category=
            finding.category,

            patch_action=
            "ADD_MISSING_WAIT",

            reason=
            finding.description,

            patch_status=
            "PENDING"
        )