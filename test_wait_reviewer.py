from agents.reviewer_agent.wait_reviewer import (
    WaitReviewer
)

findings = (
    WaitReviewer.review()
)

print(
    f"Findings: {len(findings)}"
)

for finding in findings:

    print(
        finding
    )