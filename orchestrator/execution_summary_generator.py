import json

from pathlib import Path


class ExecutionSummaryGenerator:

    @staticmethod
    def save(
        summary: dict
    ):

        output_dir = Path(
            "output"
        )

        output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        file_path = (
            output_dir
            / "execution_summary.json"
        )

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                summary,
                file,
                indent=4
            )

        return str(
            file_path
        )