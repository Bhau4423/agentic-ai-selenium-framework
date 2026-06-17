from pathlib import Path
import json

from models.scenario_mapping_model import (
    ScenarioMapping
)


class ScenarioMapper:

    @staticmethod
    def tokenize(text: str):

        if not text:
            return set()

        return {
            word.lower()
            for word in text.replace(
                "_",
                " "
            ).replace(
                "-",
                " "
            ).split()
            if len(word.strip()) > 2
        }

    @staticmethod
    def load_requirements():

        with open(
            "data/intermediate/requirement_analysis.json",
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    @staticmethod
    def load_inventory():

        with open(
            "output/page_inventory.json",
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    @staticmethod
    def get_all_scenarios():

        data = (
            ScenarioMapper.load_requirements()
        )

        scenarios = []

        scenarios.extend(
            data.get(
                "positive_scenarios",
                []
            )
        )

        scenarios.extend(
            data.get(
                "negative_scenarios",
                []
            )
        )

        scenarios.extend(
            data.get(
                "boundary_scenarios",
                []
            )
        )

        return scenarios

    @staticmethod
    def map_scenarios():

        inventory = (
            ScenarioMapper.load_inventory()
        )

        pages = inventory.get(
            "pages",
            []
        )

        mappings = []

        scenarios = (
            ScenarioMapper.get_all_scenarios()
        )

        for scenario in scenarios:

            scenario_text = (
                scenario.get(
                    "title",
                    ""
                )
                + " "
                + " ".join(
                    scenario.get(
                        "steps",
                        []
                    )
                )
            )

            scenario_keywords = (
                ScenarioMapper.tokenize(
                    scenario_text
                )
            )

            best_page = None

            best_score = 0

            matched_elements = []

            for page in pages:

                page_score = 0

                page_matches = []

                elements = page.get(
                    "elements",
                    []
                )

                for element in elements:

                    element_name = (
                        element.get(
                            "element_name",
                            ""
                        )
                    )

                    element_keywords = (
                        ScenarioMapper.tokenize(
                            element_name
                        )
                    )

                    common = (
                        scenario_keywords.intersection(
                            element_keywords
                        )
                    )

                    if common:

                        page_score += len(
                            common
                        )

                        page_matches.append(
                            element_name
                        )

                if page_score > best_score:

                    best_score = page_score

                    best_page = page

                    matched_elements = (
                        page_matches
                    )

            if best_page:

                mappings.append(
                    ScenarioMapping(
                        scenario_id=scenario.get(
                            "id",
                            ""
                        ),
                        scenario_title=scenario.get(
                            "title",
                            ""
                        ),
                        scenario_type=scenario.get(
                            "scenario_type",
                            ""
                        ),
                        page_name=best_page.get(
                            "page_name",
                            ""
                        ),
                        matched_elements=matched_elements
                    )
                )

        return mappings