from models.requirement_analysis_result import (
    RequirementAnalysisResult
)


class RequirementMerger:

    @staticmethod
    def merge(
        results: list[RequirementAnalysisResult]
    ):

        base_url = None

        application_urls = []

        requirements = []

        acceptance_criteria = []

        positive_scenarios = []

        negative_scenarios = []

        boundary_scenarios = []

        seen_urls = set()

        for result in results:

            if (
                not base_url
                and result.base_url
            ):
                base_url = result.base_url

            for app_url in result.application_urls:

                if app_url.url in seen_urls:
                    continue

                seen_urls.add(
                    app_url.url
                )

                application_urls.append(
                    app_url
                )

            requirements.extend(
                result.requirements
            )

            acceptance_criteria.extend(
                result.acceptance_criteria
            )

            positive_scenarios.extend(
                result.positive_scenarios
            )

            negative_scenarios.extend(
                result.negative_scenarios
            )

            boundary_scenarios.extend(
                result.boundary_scenarios
            )

        return RequirementAnalysisResult(

            base_url=
            base_url,

            application_urls=
            application_urls,

            requirements=
            requirements,

            acceptance_criteria=
            acceptance_criteria,

            positive_scenarios=
            positive_scenarios,

            negative_scenarios=
            negative_scenarios,

            boundary_scenarios=
            boundary_scenarios
        )