import re


class GetterPatchStrategy:

    @staticmethod
    def extract_missing_element(
        description: str
    ):

        match = re.search(
            r"Getter missing for locator:\s*(\w+)",
            description
        )

        if match:

            return match.group(1)

        return None

    @staticmethod
    def generate_getter(
        element_name: str
    ):

        return f"""

    public WebElement get_{element_name}() {{
        return {element_name};
    }}
"""