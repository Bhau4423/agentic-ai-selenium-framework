class SemanticMappingValidator:

    @staticmethod
    def validate(
        semantic_elements: list,
        page: dict
    ):

        valid_elements = []

        inventory_elements = set()

        for element in page.get(
            "elements",
            []
        ):

            inventory_elements.add(
                element.get(
                    "element_name",
                    ""
                )
            )

        for semantic_element in semantic_elements:

            if (
                semantic_element.element_name
                in inventory_elements
            ):

                valid_elements.append(
                    semantic_element
                )

            else:

                print(
                    f"[WARNING] Hallucinated Element Removed: "
                    f"{semantic_element.element_name}"
                )

        return valid_elements