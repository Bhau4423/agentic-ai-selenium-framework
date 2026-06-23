from models.requirement_analysis_result import (
    RequirementAnalysisResult
)


class TitleNormalizer:

    @staticmethod
    def normalize(
        result: RequirementAnalysisResult
    ):

        TitleNormalizer._normalize_titles(
            result.positive_scenarios
        )

        TitleNormalizer._normalize_titles(
            result.negative_scenarios
        )

        TitleNormalizer._normalize_titles(
            result.boundary_scenarios
        )

        return result

    @staticmethod
    def _normalize_titles(
        scenarios
    ):

        seen_titles = {}

        for scenario in scenarios:

            title = (
                scenario.title
                .strip()
            )

            key = title.lower()

            if key not in seen_titles:

                seen_titles[key] = 1

                continue

            seen_titles[key] += 1

            scenario.title = (
                f"{title} "
                f"{seen_titles[key]}"
            )