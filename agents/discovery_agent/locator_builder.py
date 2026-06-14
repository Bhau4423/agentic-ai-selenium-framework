from models.locator_model import Locator


class LocatorBuilder:

    @staticmethod
    def build(element):

        element_id = element.get_attribute("id")

        element_name = element.get_attribute("name")

        css_selector = None
        xpath = None

        if element_id:

            css_selector = f"#{element_id}"

            xpath = (
                f"//*[@id='{element_id}']"
            )

        elif element_name:

            css_selector = (
                f"[name='{element_name}']"
            )

            xpath = (
                f"//*[@name='{element_name}']"
            )

        return Locator(
            id=element_id,
            name=element_name,
            css_selector=css_selector,
            xpath=xpath
        )