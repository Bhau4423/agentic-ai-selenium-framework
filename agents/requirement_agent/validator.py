from models.requirement_analysis_result import (
    RequirementAnalysisResult
)


class RequirementValidator:

    @staticmethod
    def validate(
        result: RequirementAnalysisResult
    ):

        errors = []

        if not result.requirements:
            errors.append(
                "No requirements generated"
            )

        if not result.acceptance_criteria:
            errors.append(
                "No acceptance criteria generated"
            )

        if not result.positive_scenarios:
            errors.append(
                "No positive scenarios generated"
            )

        if not result.negative_scenarios:
            errors.append(
                "No negative scenarios generated"
            )

        if not result.boundary_scenarios:
            errors.append(
                "No boundary scenarios generated"
            )

        return errors