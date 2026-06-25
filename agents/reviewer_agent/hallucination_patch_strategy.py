import re
from pathlib import Path
from difflib import get_close_matches

from agents.reviewer_agent.review_file_provider import (
    ReviewFileProvider
)


class HallucinationPatchStrategy:

    @staticmethod
    def load_all_getters():

        getters = []

        java_files = (
            ReviewFileProvider
            .get_generated_page_files()
        )

        if not java_files:

            return getters

        pattern = (
            r"public WebElement get_(\w+)\("
        )

        for java_file in java_files:

            with open(
                java_file,
                "r",
                encoding="utf-8"
            ) as file:

                content = file.read()

            matches = re.findall(
                pattern,
                content
            )

            getters.extend(
                matches
            )

        return list(
            set(getters)
        )

    @staticmethod
    def extract_invalid_getter(
        description: str
    ):

        match = re.search(
            r"get_(\w+)\(",
            description
        )

        if match:

            return match.group(1)

        return None

    @staticmethod
    def find_replacement(
        invalid_getter: str
    ):

        getters = (
            HallucinationPatchStrategy
            .load_all_getters()
        )

        if not getters:

            return None

        matches = get_close_matches(
            invalid_getter,
            getters,
            n=1,
            cutoff=0.30
        )

        if matches:

            return matches[0]

        return None