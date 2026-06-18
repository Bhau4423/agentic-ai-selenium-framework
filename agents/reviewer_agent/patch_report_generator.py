import json
from pathlib import Path

from models.patch_report_model import (
    PatchReport
)


class PatchReportGenerator:

    @staticmethod
    def save(
        report: PatchReport
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
            / "patch_report.json"
        )

        report_data = {

            "iteration":
                report.iteration,

            "total_patches":
                report.total_patches,

            "successful_patches":
                report.successful_patches,

            "failed_patches":
                report.failed_patches,

            "patches": [

                {
                    "finding_id":
                        patch.finding_id,

                    "file_name":
                        patch.file_name,

                    "category":
                        patch.category,

                    "patch_action":
                        patch.patch_action,

                    "reason":
                        patch.reason,

                    "patch_status":
                        patch.patch_status
                }

                for patch
                in report.patches
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