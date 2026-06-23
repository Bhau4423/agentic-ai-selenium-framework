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

from agents.generator_agent.action_classifier import (
    ActionClassifier
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

    @staticmethod
    def build_inventory_summary(
        page: dict
    ):

        inventory = []

        for element in page.get(
            "elements",
            []
        ):

            inventory.append(

                {
                    "element_name":
                        element.get(
                            "element_name",
                            ""
                        ),

                    "element_type":
                        element.get(
                            "element_type",
                            ""
                        ),

                    "input_type":
                        element.get(
                            "input_type",
                            ""
                        ),

                    "label":
                        element.get(
                            "label",
                            ""
                        ),

                    "visible_text":
                        element.get(
                            "visible_text",
                            ""
                        )
                }
            )

        return inventory

    @staticmethod
    def rule_based_mapping(
        scenario: dict,
        page: dict
    ):

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

        ).lower()

        matched_elements = []

        for element in page.get(
            "elements",
            []
        ):

            combined_text = (

                str(
                    element.get(
                        "element_name",
                        ""
                    )
                )

                + " "

                + str(
                    element.get(
                        "label",
                        ""
                    )
                )

                + " "

                + str(
                    element.get(
                        "visible_text",
                        ""
                    )
                )

                + " "

                + str(
                    element.get(
                        "placeholder",
                        ""
                    )
                )

            ).lower()

            score = 0

            scenario_words = {

                word

                for word

                in scenario_text.split()

                if len(word) > 2
            }

            element_words = {

                word

                for word

                in combined_text.split()

                if len(word) > 2
            }

            common_words = (
                scenario_words.intersection(
                    element_words
                )
            )

            score += len(
                common_words
            )

            if score > 0:

                action_type = (
                    ActionClassifier.classify(
                        element
                    )
                )

                matched_elements.append(

                    SemanticElement(

                        element_name=
                        element.get(
                            "element_name",
                            ""
                        ),

                        role=
                        element.get(
                            "element_type",
                            ""
                        ),

                        action_type=
                        action_type
                    )
                )

        return matched_elements

    def llm_mapping(
        self,
        scenario: dict,
        page: dict
    ):

        inventory = (
            self.build_inventory_summary(
                page
            )
        )

        prompt = f"""
You are a Senior QA Automation Architect.

Scenario:

{json.dumps(scenario, indent=2)}

Available Elements:

{json.dumps(inventory, indent=2)}

Task:

Identify ONLY the UI elements required
to automate the scenario.

Rules:

- Use ONLY elements from inventory.
- Do not invent elements.
- Match business intent.
- Choose best matching elements.
- Use one of the following action types:

SEND_KEYS
CLICK
SELECT
ASSERT

CHECKBOX
RADIO

FILE_UPLOAD
FILE_DOWNLOAD

ALERT_ACCEPT
ALERT_DISMISS

FRAME_SWITCH
WINDOW_SWITCH

TABLE_VALIDATE

MODAL_CLOSE

Return JSON only.

Expected Format:

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

        response = (
            self.llm.invoke(
                prompt
            )
        )

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

            if not element_name:
                continue

            semantic_elements.append(

                SemanticElement(

                    element_name=
                    element_name,

                    role=
                    item.get(
                        "role",
                        ""
                    ),

                    action_type=
                    item.get(
                        "action_type",
                        "CLICK"
                    )
                )
            )

        confidence_score = float(

            result.get(
                "confidence_score",
                0.0
            )
        )

        return (
            semantic_elements,
            confidence_score
        )

    def map_scenario(
        self,
        scenario: dict,
        page: dict
    ):

        try:

            rule_based_elements = (
                SemanticElementMapper
                .rule_based_mapping(
                    scenario,
                    page
                )
            )

            semantic_elements = (
                rule_based_elements
            )

            confidence_score = 0.75

            if len(
                semantic_elements
            ) == 0:

                (
                    semantic_elements,
                    confidence_score
                ) = self.llm_mapping(
                    scenario,
                    page
                )

            semantic_elements = (

                SemanticMappingValidator
                .validate(
                    semantic_elements,
                    page
                )
            )

            return SemanticMapping(

                scenario_id=
                scenario.get(
                    "id",
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
                    "POSITIVE"
                ),

                page_name=
                page.get(
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

                scenario_id=
                scenario.get(
                    "id",
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
                    "POSITIVE"
                ),

                page_name=
                page.get(
                    "page_name",
                    ""
                ),

                matched_elements=[],

                confidence_score=0.0
            )