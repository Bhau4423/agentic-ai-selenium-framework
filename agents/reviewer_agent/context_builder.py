import json
from pathlib import Path

from models.scenario_context_model import (
    ScenarioContext
)


class ContextBuilder:

    @staticmethod
    def load_requirement_analysis():

        file_path = Path(
            "data/intermediate/requirement_analysis.json"
        )

        if not file_path.exists():

            raise FileNotFoundError(
                "requirement_analysis.json not found"
            )

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    @staticmethod
    def build_contexts():

        data = (
            ContextBuilder.load_requirement_analysis()
        )

        contexts = []

        scenario_groups = [

            "positive_scenarios",
            "negative_scenarios",
            "boundary_scenarios"
        ]

        for group in scenario_groups:

            for scenario in data.get(
                group,
                []
            ):

                contexts.append(

                    ScenarioContext(

                        scenario_id=
                        scenario.get(
                            "id",
                            ""
                        ),

                        requirement_id=
                        scenario.get(
                            "requirement_id",
                            ""
                        ),

                        scenario_title=
                        scenario.get(
                            "title",
                            ""
                        ),

                        scenario_type=
                        scenario.get(
                            "scenario_type",
                            ""
                        ),

                        steps=
                        scenario.get(
                            "steps",
                            []
                        ),

                        expected_result=
                        scenario.get(
                            "expected_result",
                            ""
                        )
                    )
                )

        return contexts

    @staticmethod
    def get_context(
        scenario_title: str
    ):

        contexts = (
            ContextBuilder.build_contexts()
        )

        for context in contexts:

            if (
                context.scenario_title.lower()
                ==
                scenario_title.lower()
            ):

                return context

        return None