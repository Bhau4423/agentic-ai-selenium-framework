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

from agents.generator_agent.traceability_generator import (
    TraceabilityGenerator
)

from agents.generator_agent.base_test_generator import (
    BaseTestGenerator
)

from agents.generator_agent.config_generator import (
    ConfigGenerator
)

from agents.generator_agent.framework_structure_generator import (
    FrameworkStructureGenerator
)

from agents.generator_agent.test_generation_service import (
    TestGenerationService
)

from agents.generator_agent.generation_manifest import (
    GenerationManifest
)


class GeneratorAgent:

    def generate_framework(self):

        GenerationManifest.create()

        print(
            "\n========== AGENT 3 STARTED =========="
        )

        # --------------------------------
        # FRAMEWORK STRUCTURE
        # --------------------------------

        print(
            "\nCreating Framework Structure..."
        )

        folders = (
            FrameworkStructureGenerator.create()
        )

        print(
            f"Folders Created: "
            f"{len(folders)}"
        )

        # --------------------------------
        # REQUIREMENT MAPPING
        # --------------------------------

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

        # --------------------------------
        # CONFIG
        # --------------------------------

        print(
            "\nGenerating Config..."
        )

        config_file = (
            ConfigGenerator.save()
        )

        print(
            f"Generated Config: "
            f"{config_file}"
        )

        # --------------------------------
        # BASE TEST
        # --------------------------------

        print(
            "\nGenerating Base Framework..."
        )

        base_file = (
            BaseTestGenerator.save()
        )

        print(
            f"Generated Base Test: "
            f"{base_file}"
        )

        # --------------------------------
        # PAGE OBJECTS
        # --------------------------------

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

        # --------------------------------
        # SCENARIO MAPPING
        # --------------------------------

        print(
            "\nMapping Scenarios..."
        )

        scenario_mappings = (
            ScenarioMapper.map_scenarios()
        )

        scenario_mapping_file = (
            ScenarioMapper.save_mappings(
                scenario_mappings
            )
        )

        print(
            f"Scenario Mappings: "
            f"{len(scenario_mappings)}"
        )

        print(
            f"Saved Mapping File: "
            f"{scenario_mapping_file}"
        )

        # --------------------------------
        # LOAD REQUIREMENTS
        # --------------------------------

        with open(
            "data/intermediate/requirement_analysis.json",
            "r",
            encoding="utf-8"
        ) as file:

            requirement_data = (
                json.load(file)
            )

        # --------------------------------
        # LOAD INVENTORY
        # --------------------------------

        with open(
            "output/page_inventory.json",
            "r",
            encoding="utf-8"
        ) as file:

            inventory_data = (
                json.load(file)
            )

        pages = (
            inventory_data.get(
                "pages",
                []
            )
        )

        # --------------------------------
        # ALL SCENARIOS
        # --------------------------------

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

        # --------------------------------
        # SEMANTIC TEST GENERATION
        # --------------------------------

        print(
            "\nGenerating Semantic Tests..."
        )

        generated_tests = []

        for mapping in scenario_mappings:

            scenario = (
                scenario_lookup.get(
                    mapping.scenario_id
                )
            )

            if not scenario:
                continue

            page = None

            for inventory_page in pages:

                if (
                    inventory_page.get(
                        "page_name",
                        ""
                    )
                    ==
                    mapping.page_name
                ):

                    page = (
                        inventory_page
                    )

                    break

            if not page:

                print(
                    f"Page Not Found: "
                    f"{mapping.page_name}"
                )

                continue

            result = (
                TestGenerationService.generate_test(
                    scenario,
                    page
                )
            )

            semantic_mapping = (
                result[
                    "semantic_mapping"
                ]
            )

            file_path = (
                result[
                    "file_path"
                ]
            )

            generated_tests.append(
                file_path
            )

            print(
                f"Generated Test: "
                f"{file_path}"
            )

        # --------------------------------
        # TRACEABILITY
        # --------------------------------

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

        GenerationManifest.save()

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
                traceability_file,

            "base_test":
                base_file,

            "config":
                config_file,

            "folders":
                folders
        }