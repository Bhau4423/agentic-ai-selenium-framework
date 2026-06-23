from models.requirement_analysis_result import (
    RequirementAnalysisResult
)


class IDNormalizer:

    @staticmethod
    def normalize(
        result: RequirementAnalysisResult
    ):

        # -------------------------
        # POSITIVE
        # -------------------------

        for index, scenario in enumerate(
            result.positive_scenarios,
            start=1
        ):

            scenario.id = (
                f"POS-{index:03}"
            )

        # -------------------------
        # NEGATIVE
        # -------------------------

        for index, scenario in enumerate(
            result.negative_scenarios,
            start=1
        ):

            scenario.id = (
                f"NEG-{index:03}"
            )

        # -------------------------
        # BOUNDARY
        # -------------------------

        for index, scenario in enumerate(
            result.boundary_scenarios,
            start=1
        ):

            scenario.id = (
                f"BND-{index:03}"
            )

        return result