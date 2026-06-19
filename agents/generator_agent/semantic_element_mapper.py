import json

from services.llm_service import (
    LLMService
)

from models.semantic_mapping_model import (
    SemanticMapping,
    SemanticElement
)

from agents.generator_agent.semantic_mapping_validator import (
    SemanticMappingValidator
)


class SemanticElementMapper:

    def __init__(self):

        self.llm = LLMService()

    @staticmethod
    def extract_json(
        response: str
    ):

        response = response.strip()

        if "```json" in response:

            response = (
                response
                .replace(
                    "```json",
                    ""
                )
                .replace(
                    "```",
                    ""
                )
                .strip()
            )

        elif "```" in response:

            response = (
                response
                .replace(
                    "```",
                    ""
                )
                .strip()
            )

        return response

    def map_scenario(
        self,
        scenario: dict,
        page: dict
    ):

        prompt = f"""
You are a Senior QA Automation Architect.

Scenario:

{json.dumps(scenario, indent=2)}

Page Inventory:

{json.dumps(page, indent=2)}

Task:

Identify the exact UI elements required to automate this scenario.

For each element determine:

1. element_name
2. role
3. action_type

Allowed action types:

SEND_KEYS
CLICK
SELECT
ASSERT

Rules:

- Use only elements from Page Inventory.
- Match business meaning.
- Do not invent elements.
- Return JSON only.

Expected Response:

{{
    "matched_elements": [
        {{
            "element_name": "",
            "role": "",
            "action_type": ""
        }}
    ],
    "confidence_score": 0.0
}}
"""

        response = self.llm.invoke(
            prompt
        )

        try:

            cleaned_response = (
                SemanticElementMapper.extract_json(
                    response
                )
            )

            result = json.loads(
                cleaned_response
            )

            raw_elements = (
                result.get(
                    "matched_elements",
                    []
                )
            )

            semantic_elements = []

            for item in raw_elements:

                if not isinstance(
                    item,
                    dict
                ):
                    continue

                element_name = (
                    item.get(
                        "element_name",
                        ""
                    )
                )

                role = (
                    item.get(
                        "role",
                        ""
                    )
                )

                action_type = (
                    item.get(
                        "action_type",
                        ""
                    )
                )

                if not element_name:
                    continue

                semantic_elements.append(
                    SemanticElement(
                        element_name=element_name,
                        role=role,
                        action_type=action_type
                    )
                )

            confidence_score = float(
                result.get(
                    "confidence_score",
                    0.0
                )
            )

            # --------------------------------
            # HALLUCINATION VALIDATION
            # --------------------------------

            semantic_elements = (
                SemanticMappingValidator.validate(
                    semantic_elements,
                    page
                )
            )

            # --------------------------------
            # RETURN CLEAN MAPPING
            # --------------------------------

            return SemanticMapping(

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
                    "POSITIVE"
                ),

                page_name=page.get(
                    "page_name",
                    ""
                ),

                matched_elements=
                semantic_elements,

                confidence_score=
                confidence_score
            )

        except Exception as e:

            print(
                f"Semantic Mapping Error: {e}"
            )

            return SemanticMapping(

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
                    "POSITIVE"
                ),

                page_name=page.get(
                    "page_name",
                    ""
                ),

                matched_elements=[],

                confidence_score=0.0
            )