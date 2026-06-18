from models.page_object_model import (
    PageObject
)


class PageElementLookup:

    @staticmethod
    def get_element(
        page_object: PageObject,
        element_name: str
    ):

        for element in page_object.elements:

            if (
                element.element_name.lower()
                ==
                element_name.lower()
            ):

                return element

        return None