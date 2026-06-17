from models.form_model import Form
from agents.discovery_agent.page_parser import PageParser


class FormParser:

    @staticmethod
    def extract_forms(page):

        forms = []

        form_elements = page.locator("form")
        count = form_elements.count()

        for index in range(count):

            form = form_elements.nth(index)

            form_id = form.get_attribute("id")
            form_name = form.get_attribute("name") or form_id or f"form_{index}"
            form_action = form.get_attribute("action")
            form_method = form.get_attribute("method")

            elements = []

            # 🔥 Extract scoped elements (IMPORTANT IMPROVEMENT)
            elements.extend(PageParser.extract_inputs(form))
            elements.extend(PageParser.extract_dropdowns(form))
            elements.extend(PageParser.extract_checkboxes(form))
            elements.extend(PageParser.extract_radio_buttons(form))
            elements.extend(PageParser.extract_textareas(form))
            elements.extend(PageParser.extract_buttons(form))

            forms.append(
                Form(
                    form_name=form_name,
                    form_id=form_id,
                    elements=elements
                )
            )

        return forms