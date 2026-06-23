from models.requirement_analysis_result import (
    RequirementAnalysisResult
)


class RequirementDeduplicator:

    @staticmethod
    def deduplicate(
        result: RequirementAnalysisResult
    ):

        unique_requirements = []

        seen_requirements = set()

        valid_requirement_ids = set()

        # -----------------------------
        # URL DEDUPLICATION
        # -----------------------------

        unique_urls = []

        seen_urls = set()

        for app_url in result.application_urls:

            if app_url.url in seen_urls:

                continue

            seen_urls.add(
                app_url.url
            )

            unique_urls.append(
                app_url
            )

        result.application_urls = (
            unique_urls
        )

        # -----------------------------
        # REQUIREMENTS
        # -----------------------------

        for requirement in result.requirements:

            key = (
                requirement.title
                .strip()
                .lower()
            )

            if key in seen_requirements:

                continue

            seen_requirements.add(
                key
            )

            unique_requirements.append(
                requirement
            )

            valid_requirement_ids.add(
                requirement.id
            )

        # -----------------------------
        # ACCEPTANCE CRITERIA
        # -----------------------------

        unique_acceptance_criteria = []

        seen_ac = set()

        for ac in result.acceptance_criteria:

            if (
                ac.requirement_id
                not in valid_requirement_ids
            ):
                continue

            key = (
                ac.requirement_id,
                ac.description
                .strip()
                .lower()
            )

            if key in seen_ac:

                continue

            seen_ac.add(
                key
            )

            unique_acceptance_criteria.append(
                ac
            )

        # -----------------------------
        # POSITIVE
        # -----------------------------

        positive_scenarios = (
            RequirementDeduplicator
            ._deduplicate_scenarios(
                result.positive_scenarios,
                valid_requirement_ids
            )
        )

        # -----------------------------
        # NEGATIVE
        # -----------------------------

        negative_scenarios = (
            RequirementDeduplicator
            ._deduplicate_scenarios(
                result.negative_scenarios,
                valid_requirement_ids
            )
        )

        # -----------------------------
        # BOUNDARY
        # -----------------------------

        boundary_scenarios = (
            RequirementDeduplicator
            ._deduplicate_scenarios(
                result.boundary_scenarios,
                valid_requirement_ids
            )
        )

        result.requirements = (
            unique_requirements
        )

        result.acceptance_criteria = (
            unique_acceptance_criteria
        )

        result.positive_scenarios = (
            positive_scenarios
        )

        result.negative_scenarios = (
            negative_scenarios
        )

        result.boundary_scenarios = (
            boundary_scenarios
        )

        return result

    @staticmethod
    def _deduplicate_scenarios(
        scenarios,
        valid_requirement_ids
    ):

        unique_scenarios = []

        seen_scenarios = set()

        for scenario in scenarios:

            if (
                scenario.requirement_id
                not in valid_requirement_ids
            ):
                continue

            key = (
                scenario.requirement_id,
                scenario.title
                .strip()
                .lower()
            )

            if key in seen_scenarios:

                continue

            seen_scenarios.add(
                key
            )

            unique_scenarios.append(
                scenario
            )

        return unique_scenarios