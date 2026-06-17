import json

from agents.generator_agent.requirement_mapper import (
    RequirementMapper
)

from agents.generator_agent.page_mapper import (
    PageMapper
)

from agents.generator_agent.scenario_mapper import (
    ScenarioMapper
)

from agents.generator_agent.java_page_generator import (
    JavaPageGenerator
)

from agents.generator_agent.java_test_generator import (
    JavaTestGenerator
)

from agents.generator_agent.traceability_generator import (
    TraceabilityGenerator
)


class GeneratorAgent:

    def generate_framework(self):

        print(
            "\n========== AGENT 3 STARTED =========="
        )

        # -------------------------
        # REQUIREMENT MAPPING
        # -------------------------

        print(
            "\nMapping Requirements..."
        )

        requirement_mappings = (
            RequirementMapper.create_mappings()
        )

        print(
            f"Requirement Mappings: "
            f"{len(requirement_mappings)}"
        )

        # -------------------------
        # PAGE OBJECT CREATION
        # -------------------------

        print(
            "\nBuilding Page Objects..."
        )

        page_objects = (
            PageMapper.build_page_objects(
                requirement_mappings
            )
        )

        generated_pages = []

        for page_object in page_objects:

            file_path = (
                JavaPageGenerator.save(
                    page_object
                )
            )

            generated_pages.append(
                file_path
            )

            print(
                f"Generated Page: "
                f"{file_path}"
            )

        # -------------------------
        # SCENARIO MAPPING
        # -------------------------

        print(
            "\nMapping Scenarios..."
        )

        scenario_mappings = (
            ScenarioMapper.map_scenarios()
        )

        print(
            f"Scenario Mappings: "
            f"{len(scenario_mappings)}"
        )

        # -------------------------
        # LOAD SCENARIOS
        # -------------------------

        with open(
            "data/intermediate/requirement_analysis.json",
            "r",
            encoding="utf-8"
        ) as file:

            requirement_data = (
                json.load(file)
            )

        all_scenarios = []

        all_scenarios.extend(
            requirement_data.get(
                "positive_scenarios",
                []
            )
        )

        all_scenarios.extend(
            requirement_data.get(
                "negative_scenarios",
                []
            )
        )

        all_scenarios.extend(
            requirement_data.get(
                "boundary_scenarios",
                []
            )
        )

        scenario_lookup = {}

        for scenario in all_scenarios:

            scenario_lookup[
                scenario["id"]
            ] = scenario

        # -------------------------
        # GENERATE TESTS
        # -------------------------

        generated_tests = []

        for mapping in scenario_mappings:

            scenario = (
                scenario_lookup.get(
                    mapping.scenario_id
                )
            )

            if not scenario:
                continue

            file_path = (
                JavaTestGenerator.save(
                    mapping,
                    scenario
                )
            )

            generated_tests.append(
                file_path
            )

            print(
                f"Generated Test: "
                f"{file_path}"
            )

        # -------------------------
        # TRACEABILITY
        # -------------------------

        print(
            "\nGenerating Traceability Matrix..."
        )

        traceability_file = (
            TraceabilityGenerator.save()
        )

        print(
            f"Generated: "
            f"{traceability_file}"
        )

        print(
            "\n========== AGENT 3 COMPLETED =========="
        )

        return {

            "requirement_mappings":
                len(
                    requirement_mappings
                ),

            "page_objects":
                len(
                    page_objects
                ),

            "scenario_mappings":
                len(
                    scenario_mappings
                ),

            "generated_pages":
                generated_pages,

            "generated_tests":
                generated_tests,

            "traceability":
                traceability_file
        }