import json

from agents.generator_agent.scenario_mapper import (
    ScenarioMapper
)

from agents.generator_agent.test_generation_service import (
    TestGenerationService
)


class MissingScriptPatchStrategy:

    @staticmethod
    def load_requirements():

        with open(
            "data/intermediate/requirement_analysis.json",
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(
                file
            )

    @staticmethod
    def load_inventory():

        with open(
            "output/page_inventory.json",
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(
                file
            )

    @staticmethod
    def get_scenario(
        scenario_id: str
    ):

        data = (
            MissingScriptPatchStrategy
            .load_requirements()
        )

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

                if (
                    scenario.get(
                        "id"
                    )
                    ==
                    scenario_id
                ):

                    return scenario

        return None

    @staticmethod
    def generate(
        scenario_id: str
    ):

        scenario = (
            MissingScriptPatchStrategy
            .get_scenario(
                scenario_id
            )
        )

        if not scenario:

            raise ValueError(
                f"Scenario not found: "
                f"{scenario_id}"
            )

        mappings = (
            ScenarioMapper.map_scenarios()
        )

        target_mapping = None

        for mapping in mappings:

            if (
                mapping.scenario_id
                ==
                scenario_id
            ):

                target_mapping = mapping
                break

        if not target_mapping:

            raise ValueError(
                f"No page mapping found "
                f"for scenario: "
                f"{scenario_id}"
            )

        inventory = (
            MissingScriptPatchStrategy
            .load_inventory()
        )

        page = None

        for inventory_page in inventory.get(
            "pages",
            []
        ):

            if (
                inventory_page.get(
                    "page_name",
                    ""
                )
                ==
                target_mapping.page_name
            ):

                page = inventory_page
                break

        if not page:

            raise ValueError(
                f"Page not found: "
                f"{target_mapping.page_name}"
            )

        return (
            TestGenerationService.generate_test(
                scenario,
                page
            )
        )