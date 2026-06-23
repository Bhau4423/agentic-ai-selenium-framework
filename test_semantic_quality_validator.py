from agents.generator_agent.semantic_quality_validator import (
    SemanticQualityValidator
)

print(
    "\n========== AGENT 3.5 STARTED =========="
)

findings = (
    SemanticQualityValidator.validate()
)

report_file = (
    SemanticQualityValidator.save_report(
        findings
    )
)

high_count = 0
medium_count = 0

for finding in findings:

    if (
        finding.severity
        == "HIGH"
    ):
        high_count += 1

    if (
        finding.severity
        == "MEDIUM"
    ):
        medium_count += 1

print(
    f"\nValidation Findings : "
    f"{len(findings)}"
)

print(
    f"HIGH   : "
    f"{high_count}"
)

print(
    f"MEDIUM : "
    f"{medium_count}"
)

print(
    f"\nReport File:"
)

print(
    report_file
)

print(
    "\n========== AGENT 3.5 COMPLETED =========="
)