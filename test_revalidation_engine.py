from agents.reviewer_agent.revalidation_engine import (
    RevalidationEngine
)

findings = (
    RevalidationEngine.validate()
)

print(
    f"Total Findings: "
    f"{len(findings)}"
)

for finding in findings:

    print(
        finding
    )