from models.review_finding_model import (
    ReviewFinding
)

from agents.reviewer_agent.locator_patch_strategy import (
    LocatorPatchStrategy
)


finding = ReviewFinding(

    finding_id="LOC-001",

    severity="HIGH",

    category=
    "HALLUCINATED_LOCATOR",

    file_name=
    "ContactPage.java",

    description=
    "Locator not found in inventory.",

    recommendation=
    "Validate locator.",

    scenario_id=None,

    requirement_id=None,

    impacted_component=
    "Page Object",

    auto_fixable=True,

    validation_status=
    "PENDING"
)

patch = (
    LocatorPatchStrategy.create_patch(
        finding
    )
)

print(patch)