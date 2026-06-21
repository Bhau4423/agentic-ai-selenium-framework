from models.review_finding_model import (
    ReviewFinding
)

from agents.reviewer_agent.impact_analyzer import (
    ImpactAnalyzer
)

findings = [

    ReviewFinding(
        finding_id="WAIT-001",
        severity="MEDIUM",
        category="WAIT",
        file_name="LoginTest.java",
        description="Missing wait detected.",
        recommendation="Add explicit wait."
    ),

    ReviewFinding(
        finding_id="LOC-001",
        severity="HIGH",
        category="HALLUCINATED_LOCATOR",
        file_name="ContactPage.java",
        description="Invalid locator detected.",
        recommendation="Replace locator."
    )
]

plans = (
    ImpactAnalyzer.analyze(
        findings
    )
)

for plan in plans:

    print(plan)