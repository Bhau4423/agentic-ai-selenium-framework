import re


class ElementNameNormalizer:

    @staticmethod
    def normalize(
        value: str
    ):

        if not value:

            return ""

        value = value.lower()

        value = re.sub(
            r"[^a-z0-9]",
            "",
            value
        )

        return value