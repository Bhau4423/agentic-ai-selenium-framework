from agents.generator_agent.semantic_element_mapper import (
    SemanticElementMapper
)

from agents.generator_agent.java_test_generator import (
    JavaTestGenerator
)


class TestGenerationService:

    @staticmethod
    def generate_test(
        scenario: dict,
        page: dict
    ):

        semantic_mapper = (
            SemanticElementMapper()
        )

        semantic_mapping = (
            semantic_mapper.map_scenario(
                scenario,
                page
            )
        )

        # print(
        #     f"Semantic Confidence: "
        #     f"{semantic_mapping.confidence_score}"
        # )

        file_path = (
            JavaTestGenerator.save(
                semantic_mapping
            )
        )

        return {

            "semantic_mapping":
                semantic_mapping,

            "file_path":
                file_path
        }