from agents.requirement_agent.prompt_builder import (
    PromptBuilder
)

from agents.requirement_agent.parser import (
    RequirementParser
)

from agents.requirement_agent.validator import (
    RequirementValidator
)

from services.llm_service import (
    LLMService
)

from services.file_service import (
    FileService
)


class RequirementAgent:

    def __init__(self):

        self.llm = LLMService()

    def analyze(
        self,
        requirement_document: str
    ):

        prompt = (
            PromptBuilder.build_prompt(
                requirement_document
            )
        )

        response = self.llm.invoke(
            prompt
        )

        result = RequirementParser.parse(
            response
        )

        errors = (
            RequirementValidator.validate(
                result
            )
        )

        if errors:

            raise ValueError(
                f"Validation Failed: {errors}"
            )

        FileService.save_json(
            "data/intermediate/requirement_analysis.json",
            result.model_dump()
        )

        return result