import json
from pathlib import Path

from models.traceability_model import (
    Traceability
)


class TraceabilityGenerator:

    @staticmethod
    def load_requirements():

        with open(
            "data/intermediate/requirement_analysis.json",
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    @staticmethod
    def load_scenario_mappings():

        with open(
            "data/intermediate/scenario_mapping.json",
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    @staticmethod
    def generate():

        requirement_data = (
            TraceabilityGenerator
            .load_requirements()
        )

        scenario_mappings = (
            TraceabilityGenerator
            .load_scenario_mappings()
        )

        requirements = (
            requirement_data.get(
                "requirements",
                []
            )
        )

        acceptance_criteria = (
            requirement_data.get(
                "acceptance_criteria",
                []
            )
        )

        positive = (
            requirement_data.get(
                "positive_scenarios",
                []
            )
        )

        negative = (
            requirement_data.get(
                "negative_scenarios",
                []
            )
        )

        boundary = (
            requirement_data.get(
                "boundary_scenarios",
                []
            )
        )

        all_scenarios = (
            positive
            + negative
            + boundary
        )

        records = []

        for requirement in requirements:

            requirement_id = (
                requirement.get(
                    "id",
                    ""
                )
            )

            requirement_title = (
                requirement.get(
                    "title",
                    ""
                )
            )

            requirement_ac = [

                ac["id"]

                for ac

                in acceptance_criteria

                if ac.get(
                    "requirement_id"
                )
                ==
                requirement_id
            ]

            requirement_scenarios = [

                scenario

                for scenario

                in all_scenarios

                if scenario.get(
                    "requirement_id"
                )
                ==
                requirement_id
            ]

            scenario_ids = [

                scenario.get(
                    "id",
                    ""
                )

                for scenario

                in requirement_scenarios
            ]

            page_name = None
            page_url = None

            mapped_elements = []

            for mapping in scenario_mappings:

                if (
                    mapping.get(
                        "scenario_id"
                    )
                    not in
                    scenario_ids
                ):

                    continue

                if not page_name:

                    page_name = (
                        mapping.get(
                            "page_name"
                        )
                    )

                if not page_url:

                    page_url = (
                        mapping.get(
                            "page_url"
                        )
                    )

                for element in mapping.get(
                    "matched_elements",
                    []
                ):

                    element_name = (
                        element.get(
                            "element_name",
                            ""
                        )
                    )

                    if (
                        element_name
                        and
                        element_name
                        not in mapped_elements
                    ):

                        mapped_elements.append(
                            element_name
                        )

            records.append(

                Traceability(

                    requirement_id=
                    requirement_id,

                    requirement_title=
                    requirement_title,

                    acceptance_criteria_ids=
                    requirement_ac,

                    scenario_ids=
                    scenario_ids,

                    page_name=
                    page_name,

                    page_url=
                    page_url,

                    mapped_elements=
                    mapped_elements
                )

            )

        return records

    @staticmethod
    def save():

        records = (
            TraceabilityGenerator
            .generate()
        )

        output_file = Path(
            "data/intermediate/traceability_matrix.json"
        )

        output_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            output_file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                [
                    record.model_dump()
                    for record
                    in records
                ],
                file,
                indent=4
            )

        print(
            f"\nTraceability Matrix saved: "
            f"{output_file}"
        )

        print(
            f"Traceability Records: "
            f"{len(records)}"
        )

        return str(
            output_file
        )