import re


class PatchMetadataExtractor:

    @staticmethod
    def extract_missing_wait_target(
        description: str
    ):

        patterns = [

            r"Missing wait before interaction:\s*(.*)",

            r"Missing wait before click:\s*(.*)",

            r"Missing visibility wait:\s*(.*)"
        ]

        for pattern in patterns:

            match = re.search(
                pattern,
                description
            )

            if match:

                return (
                    match.group(1)
                    .strip()
                )

        return None

    @staticmethod
    def extract_hallucinated_method(
        description: str
    ):

        match = re.search(
            r"get_\w+\(\)",
            description
        )

        if match:

            return match.group(0)

        return None

    @staticmethod
    def extract_locator(
        description: str
    ):

        if ":" not in description:

            return None

        return (
            description
            .split(":")[-1]
            .strip()
        )