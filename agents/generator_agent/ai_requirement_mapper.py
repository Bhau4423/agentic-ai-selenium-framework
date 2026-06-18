import json

from services.llm_service import (
    LLMService
)


class AIRequirementMapper:

    def __init__(self):

        self.llm = LLMService()

    def map_requirement(
        self,
        requirement: dict,
        pages: list
    ):

        prompt = f"""
You are an expert QA Automation Architect.

Requirement:

{json.dumps(requirement, indent=2)}

Available Pages:

{json.dumps(pages, indent=2)}

Select the single best matching page.

Return JSON only:

{{
    "page_name": "",
    "confidence_score": 0.0
}}
"""

        response = self.llm.invoke(
            prompt
        )

        try:

            return json.loads(
                response
            )

        except:

            return {
                "page_name": "",
                "confidence_score": 0.0
            }