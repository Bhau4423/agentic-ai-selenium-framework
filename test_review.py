from agents.reviewer_agent.final_validation_report_generator import (
    FinalValidationReportGenerator
)

report = (
    FinalValidationReportGenerator.generate(

        status="APPROVED",

        iterations=1,

        total_findings=0,

        resolved_findings=0,

        remaining_findings=0,

        patches_applied=0,

        reviewers_executed=[

            "AssertionReviewer",

            "CoverageReviewer",

            "WaitReviewer",

            "LocatorReviewer",

            "MissingScriptReviewer",

            "EdgeCaseReviewer",

            "TraceabilityReviewer",

            "HallucinationReviewer"
        ],

        approval_reason=
        "All validations passed."
    )
)

file_path = (
    FinalValidationReportGenerator.save(
        report
    )
)

print(
    f"Generated: {file_path}"
)