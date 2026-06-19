from agents.reviewer_agent.missing_script_reviewer import (
    MissingScriptReviewer
)

findings = (
    MissingScriptReviewer.review()
)

print(
    f"Findings: {len(findings)}"
)

for finding in findings:

    print(
        finding
    )