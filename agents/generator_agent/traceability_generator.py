from pathlib import Path
import json


class TraceabilityGenerator:

    @staticmethod
    def generate():

        requirement_file = Path(
            "data/intermediate/requirement_analysis.json"
        )

        with open(
            requirement_file,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

        rows = []

        positive = data.get(
            "positive_scenarios",
            []
        )

        negative = data.get(
            "negative_scenarios",
            []
        )

        boundary = data.get(
            "boundary_scenarios",
            []
        )

        scenarios = (
            positive
            + negative
            + boundary
        )

        for scenario in scenarios:

            rows.append(
                {
                    "requirement_id":
                        scenario.get(
                            "requirement_id",
                            ""
                        ),

                    "scenario_id":
                        scenario.get(
                            "id",
                            ""
                        ),

                    "scenario_title":
                        scenario.get(
                            "title",
                            ""
                        ),

                    "scenario_type":
                        scenario.get(
                            "scenario_type",
                            ""
                        )
                }
            )

        return rows

    @staticmethod
    def save():

        output_dir = Path(
            "generated_framework/traceability"
        )

        output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        rows = (
            TraceabilityGenerator.generate()
        )

        file_path = (
            output_dir
            / "traceability_matrix.csv"
        )

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(
                "Requirement ID,"
                "Scenario ID,"
                "Scenario Title,"
                "Scenario Type\n"
            )

            for row in rows:

                file.write(
                    f"{row['requirement_id']},"
                    f"{row['scenario_id']},"
                    f"{row['scenario_title']},"
                    f"{row['scenario_type']}\n"
                )

        return str(file_path)