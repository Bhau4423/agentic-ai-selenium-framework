from agents.reviewer_agent.hallucination_reviewer import (
    HallucinationReviewer
)

findings = (
    HallucinationReviewer.review()
)

print(
    f"Findings: {len(findings)}"
)

for finding in findings:

    print(
        finding
    )