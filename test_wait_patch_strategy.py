from models.review_finding_model import (
    ReviewFinding
)

from agents.reviewer_agent.wait_patch_strategy import (
    WaitPatchStrategy
)


finding = ReviewFinding(

    finding_id="WAIT-001",

    severity="MEDIUM",

    category="WAIT",

    file_name="LoginTest.java",

    description=
    "Missing wait before click.",

    recommendation=
    "Add explicit wait.",

    scenario_id=None,

    requirement_id=None,

    impacted_component=
    "Generated Test",

    auto_fixable=True,

    validation_status=
    "PENDING"
)

patch = (
    WaitPatchStrategy.create_patch(
        finding
    )
)

print(patch)