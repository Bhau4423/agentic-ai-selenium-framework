import json
from pathlib import Path

from models.review_report_model import (
    ReviewReport
)


class ReportGenerator:

    @staticmethod
    def save(
        report: ReviewReport
    ):

        output_dir = Path(
            "output/review"
        )

        output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        file_path = (
            output_dir
            / "review_report.json"
        )

        report_data = {

            "iteration":
                report.iteration,

            "status":
                report.status,

            "total_findings":
                report.total_findings,

            "findings": [

                {
                    "finding_id":
                        finding.finding_id,

                    "severity":
                        finding.severity,

                    "category":
                        finding.category,

                    "file_name":
                        finding.file_name,

                    "description":
                        finding.description,

                    "recommendation":
                        finding.recommendation
                }

                for finding
                in report.findings
            ]
        }

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                report_data,
                file,
                indent=4
            )

        return str(file_path)