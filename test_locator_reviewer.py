from agents.reviewer_agent.locator_reviewer import (
    LocatorReviewer
)

findings = (
    LocatorReviewer.review()
)

print(
    f"Findings: {len(findings)}"
)

for finding in findings:

    print(
        finding
    )