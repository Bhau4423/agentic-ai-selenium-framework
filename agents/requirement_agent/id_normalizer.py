from models.requirement_analysis_result import (
    RequirementAnalysisResult
)


class IDNormalizer:

    @staticmethod
    def normalize(
        result: RequirementAnalysisResult
    ):

        # --------------------------------
        # REQUIREMENTS
        # --------------------------------

        title_to_requirement_id = {}

        for index, requirement in enumerate(
            result.requirements,
            start=1
        ):

            requirement.id = (
                f"FR-{index:03}"
            )

            title_to_requirement_id[
                requirement.title.strip().lower()
            ] = requirement.id

        # --------------------------------
        # ACCEPTANCE CRITERIA
        # --------------------------------

        for index, ac in enumerate(
            result.acceptance_criteria,
            start=1
        ):

            ac.id = (
                f"AC-{index:03}"
            )

            title = (
                ac.requirement_title
                .strip()
                .lower()
            )

            ac.requirement_id = (
                title_to_requirement_id.get(
                    title,
                    ""
                )
            )

        # --------------------------------
        # POSITIVE SCENARIOS
        # --------------------------------

        for index, scenario in enumerate(
            result.positive_scenarios,
            start=1
        ):

            scenario.id = (
                f"POS-{index:03}"
            )

            title = (
                scenario.requirement_title
                .strip()
                .lower()
            )

            scenario.requirement_id = (
                title_to_requirement_id.get(
                    title,
                    ""
                )
            )

        # --------------------------------
        # NEGATIVE SCENARIOS
        # --------------------------------

        for index, scenario in enumerate(
            result.negative_scenarios,
            start=1
        ):

            scenario.id = (
                f"NEG-{index:03}"
            )

            title = (
                scenario.requirement_title
                .strip()
                .lower()
            )

            scenario.requirement_id = (
                title_to_requirement_id.get(
                    title,
                    ""
                )
            )

        # --------------------------------
        # BOUNDARY SCENARIOS
        # --------------------------------

        for index, scenario in enumerate(
            result.boundary_scenarios,
            start=1
        ):

            scenario.id = (
                f"BND-{index:03}"
            )

            title = (
                scenario.requirement_title
                .strip()
                .lower()
            )

            scenario.requirement_id = (
                title_to_requirement_id.get(
                    title,
                    ""
                )
            )

        print(
            "\n========== ID NORMALIZATION =========="
        )

        print(
            f"Requirements: "
            f"{len(result.requirements)}"
        )

        print(
            f"Acceptance Criteria: "
            f"{len(result.acceptance_criteria)}"
        )

        print(
            f"Positive Scenarios: "
            f"{len(result.positive_scenarios)}"
        )

        print(
            f"Negative Scenarios: "
            f"{len(result.negative_scenarios)}"
        )

        print(
            f"Boundary Scenarios: "
            f"{len(result.boundary_scenarios)}"
        )

        return result