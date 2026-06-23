import re

from models.application_url_model import (
    ApplicationUrl
)

from models.requirement_analysis_result import (
    RequirementAnalysisResult
)


class URLExtractor:

    @staticmethod
    def extract(
        result: RequirementAnalysisResult,
        requirement_document: str = ""
    ):

        scenarios = []

        scenarios.extend(
            result.positive_scenarios
        )

        scenarios.extend(
            result.negative_scenarios
        )

        scenarios.extend(
            result.boundary_scenarios
        )

        base_url = None

        application_urls = []

        seen_urls = set()

        # --------------------------------
        # EXTRACT BASE URL FROM SRS
        # --------------------------------

        if requirement_document:

            match = re.search(
                r"https?://[^\s]+",
                requirement_document
            )

            if match:

                base_url = (
                    match.group(0)
                    .rstrip("/")
                )

        # --------------------------------
        # FALLBACK:
        # EXTRACT FROM SCENARIOS
        # --------------------------------

        full_url_pattern = (
            r"https?://[^\s\"']+"
        )

        path_pattern = (
            r"/[a-zA-Z0-9_\-/]+"
        )

        for scenario in scenarios:

            steps = scenario.steps or []

            for step in steps:

                full_urls = re.findall(
                    full_url_pattern,
                    step
                )

                for url in full_urls:

                    if not base_url:

                        match = re.match(
                            r"(https?://[^/]+)",
                            url
                        )

                        if match:

                            base_url = (
                                match.group(1)
                            )

                paths = re.findall(
                    path_pattern,
                    step
                )

                for path in paths:

                    if (
                        path.startswith("//")
                    ):
                        continue

                    if path in seen_urls:
                        continue

                    seen_urls.add(
                        path
                    )

                    page_name = (
                        path.strip("/")
                        .replace(
                            "-",
                            " "
                        )
                        .replace(
                            "_",
                            " "
                        )
                        .title()
                    )

                    if not page_name:

                        page_name = (
                            "Home"
                        )

                    application_urls.append(

                        ApplicationUrl(

                            page_name=
                            page_name,

                            url=path
                        )
                    )

        result.base_url = (
            base_url
        )

        result.application_urls = (
            application_urls
        )

        return result