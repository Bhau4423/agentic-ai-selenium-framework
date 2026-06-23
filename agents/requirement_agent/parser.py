import json
import re

from models.requirement_analysis_result import (
    RequirementAnalysisResult
)

from agents.requirement_agent.response_repair import (
    ResponseRepair
)


class RequirementParser:

    @staticmethod
    def parse(
        response: str
    ):

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

        data = json.loads(
            response
        )

        # --------------------------------
        # NORMALIZE URL STRUCTURE
        # --------------------------------

        data = (
            RequirementParser
            ._normalize_urls(
                data
            )
        )

        # --------------------------------
        # REPAIR RESPONSE
        # --------------------------------

        data = (
            ResponseRepair.repair(
                data
            )
        )

        return RequirementAnalysisResult(
            **data
        )

    @staticmethod
    def _normalize_urls(
        data: dict
    ):

        # -----------------------------
        # FIX BASE URL
        # -----------------------------

        base_url = data.get(
            "base_url"
        )

        if isinstance(
            base_url,
            dict
        ):

            data["base_url"] = (
                base_url.get(
                    "base_url"
                )
            )

        # -----------------------------
        # FIX APPLICATION URLS
        # -----------------------------

        application_urls = data.get(
            "application_urls",
            []
        )

        # Gemini sometimes returns:
        #
        # {
        #   "application_urls": {
        #      "base_url": "...",
        #      "application_urls": [...]
        #   }
        # }

        if isinstance(
            application_urls,
            dict
        ):

            application_urls = (
                application_urls.get(
                    "application_urls",
                    []
                )
            )

        normalized_urls = []

        for item in application_urls:

            # -------------------------
            # STRING PATH
            # -------------------------

            if isinstance(
                item,
                str
            ):

                page_name = (
                    item.strip("/")
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

                normalized_urls.append(
                    {
                        "page_name":
                        page_name,

                        "url":
                        item
                    }
                )

            # -------------------------
            # ALREADY CORRECT
            # -------------------------

            elif isinstance(
                item,
                dict
            ):

                normalized_urls.append(
                    item
                )

        data[
            "application_urls"
        ] = normalized_urls

        return data