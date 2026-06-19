import json
from pathlib import Path

from models.final_validation_report_model import (
    FinalValidationReport
)


class FinalValidationReportGenerator:

    @staticmethod
    def generate(
        status: str,
        iterations: int,
        total_findings: int,
        resolved_findings: int,
        remaining_findings: int,
        patches_applied: int,
        reviewers_executed: list[str],
        approval_reason: str
    ):

        report = FinalValidationReport(

            status=status,

            iterations=iterations,

            total_findings=total_findings,

            resolved_findings=resolved_findings,

            remaining_findings=remaining_findings,

            patches_applied=patches_applied,

            reviewers_executed=
            reviewers_executed,

            approval_reason=
            approval_reason
        )

        return report

    @staticmethod
    def save(
        report: FinalValidationReport
    ):

        output_dir = Path(
            "output/review"
        )

        output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        file_path = (
            output_dir /
            "final_validation_report.json"
        )

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                report.model_dump(),
                file,
                indent=4
            )

        return str(
            file_path
        )