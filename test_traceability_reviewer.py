from agents.reviewer_agent.traceability_reviewer import (
    TraceabilityReviewer
)

findings = (
    TraceabilityReviewer.review()
)

print(
    f"Findings: {len(findings)}"
)

for finding in findings:

    print(
        finding
    )