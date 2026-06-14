import json
import re

from models.requirement_analysis_result import (
    RequirementAnalysisResult
)


class RequirementParser:

    @staticmethod
    def parse(response: str):

        response = response.strip()

        response = re.sub(
            r"^```json",
            "",
            response
        )

        response = re.sub(
            r"^```",
            "",
            response
        )

        response = re.sub(
            r"```$",
            "",
            response
        )

        response = response.strip()

        data = json.loads(response)

        return RequirementAnalysisResult(
            **data
        )