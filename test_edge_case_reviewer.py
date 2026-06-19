from agents.reviewer_agent.edge_case_reviewer import (
    EdgeCaseReviewer
)

findings = (
    EdgeCaseReviewer.review()
)

print(
    f"Findings: {len(findings)}"
)

for finding in findings:

    print(
        finding
    )