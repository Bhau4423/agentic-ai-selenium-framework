from models.locator_model import Locator


class LocatorBuilder:

    @staticmethod
    def build(element):

        element_id = (
            element.get_attribute("id")
        )

        element_name = (
            element.get_attribute("name")
        )

        data_testid = (
            element.get_attribute(
                "data-testid"
            )
        )

        aria_label = (
            element.get_attribute(
                "aria-label"
            )
        )

        placeholder = (
            element.get_attribute(
                "placeholder"
            )
        )

        tag_name = (
            element.evaluate(
                "el => el.tagName.toLowerCase()"
            )
        )

        element_type = (
            element.get_attribute(
                "type"
            )
        )

        css_selector = None
        xpath = None

        # -------------------------
        # ID
        # -------------------------

        if element_id:

            css_selector = (
                f"#{element_id}"
            )

            xpath = (
                f"//*[@id='{element_id}']"
            )

        # -------------------------
        # NAME
        # -------------------------

        elif element_name:

            css_selector = (
                f"[name='{element_name}']"
            )

            xpath = (
                f"//*[@name='{element_name}']"
            )

        # -------------------------
        # DATA TEST ID
        # -------------------------

        elif data_testid:

            css_selector = (
                f"[data-testid='{data_testid}']"
            )

            xpath = (
                f"//*[@data-testid='{data_testid}']"
            )

        # -------------------------
        # ARIA LABEL
        # -------------------------

        elif aria_label:

            css_selector = (
                f"[aria-label='{aria_label}']"
            )

            xpath = (
                f"//*[@aria-label='{aria_label}']"
            )

        # -------------------------
        # PLACEHOLDER
        # -------------------------

        elif placeholder:

            css_selector = (
                f"[placeholder='{placeholder}']"
            )

            xpath = (
                f"//*[@placeholder='{placeholder}']"
            )

        # -------------------------
        # BUTTON TEXT
        # -------------------------

        elif tag_name == "button":

            try:

                button_text = (
                    element.inner_text()
                    .strip()
                )

            except Exception:

                button_text = ""

            if button_text:

                css_selector = "button"

                xpath = (
                    f"//button"
                    f"[normalize-space()="
                    f"'{button_text}']"
                )

            else:

                css_selector = "button"

                xpath = "//button"

        # -------------------------
        # TAG + TYPE
        # -------------------------

        elif element_type:

            css_selector = (
                f"{tag_name}[type='{element_type}']"
            )

            xpath = (
                f"//{tag_name}"
                f"[@type='{element_type}']"
            )

        # -------------------------
        # TAG FALLBACK
        # -------------------------

        else:

            css_selector = tag_name

            xpath = (
                f"//{tag_name}"
            )

        return Locator(

            id=element_id,

            name=element_name,

            css_selector=css_selector,

            xpath=xpath
        )