from pathlib import Path

from models.page_object_model import (
    PageObject
)

from agents.generator_agent.generation_manifest import (
    GenerationManifest
)


class JavaPageGenerator:

    @staticmethod
    def get_clean_page_name(
        page_name: str
    ):

        page_name = (
            page_name.split("|")[0]
            .strip()
        )

        words = (
            page_name
            .replace("-", " ")
            .replace("_", " ")
            .split()
        )

        class_name = ""

        for word in words:

            class_name += (
                word.capitalize()
            )

        if not class_name.endswith(
            "Page"
        ):

            class_name += "Page"

        return class_name

    @staticmethod
    def get_locator_annotation(
        locator_type: str,
        locator_value: str
    ):

        if not locator_type or not locator_value:

            return None

        locator_type = (
            locator_type.lower()
        )

        if locator_type == "id":

            return (
                f'@FindBy(id = "{locator_value}")'
            )

        if locator_type == "name":

            return (
                f'@FindBy(name = "{locator_value}")'
            )

        if locator_type == "css_selector":

            return (
                f'@FindBy(css = "{locator_value}")'
            )

        if locator_type == "xpath":

            return (
                f'@FindBy(xpath = "{locator_value}")'
            )

        return None

    @staticmethod
    def get_field_name(
        element_name: str
    ):

        return (
            element_name
            .replace(" ", "_")
            .replace("-", "_")
            .replace("[", "_")
            .replace("]", "_")
        )

    @staticmethod
    def to_pascal_case(
        text: str
    ):

        words = (
            text
            .replace("_", " ")
            .replace("-", " ")
            .split()
        )

        result = ""

        for word in words:

            result += (
                word.capitalize()
            )

        return result

    @staticmethod
    def generate(
        page_object: PageObject
    ):

        class_name = (
            JavaPageGenerator
            .get_clean_page_name(
                page_object.page_name
            )
        )

        lines = []

        # -------------------------
        # PACKAGE
        # -------------------------

        lines.append(
            "package pages;"
        )

        lines.append("")

        # -------------------------
        # IMPORTS
        # -------------------------

        lines.append(
            "import org.openqa.selenium.WebDriver;"
        )

        lines.append(
            "import org.openqa.selenium.WebElement;"
        )

        lines.append(
            "import org.openqa.selenium.support.FindBy;"
        )

        lines.append(
            "import org.openqa.selenium.support.PageFactory;"
        )

        lines.append(
            "import org.openqa.selenium.support.ui.Select;"
        )

        lines.append("")

        # -------------------------
        # CLASS
        # -------------------------

        lines.append(
            f"public class {class_name} {{"
        )

        lines.append("")

        lines.append(
            "    private WebDriver driver;"
        )

        lines.append("")

        valid_elements = []

        # -------------------------
        # WEBELEMENTS
        # -------------------------

        for element in page_object.elements:

            annotation = (
                JavaPageGenerator
                .get_locator_annotation(
                    element.locator_type,
                    element.locator_value
                )
            )

            if not annotation:

                continue

            field_name = (
                JavaPageGenerator
                .get_field_name(
                    element.element_name
                )
            )

            valid_elements.append(
                (
                    field_name,
                    element
                )
            )

            lines.append(
                f"    {annotation}"
            )

            lines.append(
                f"    private WebElement {field_name};"
            )

            lines.append("")

        # -------------------------
        # CONSTRUCTOR
        # -------------------------

        lines.append(
            f"    public {class_name}(WebDriver driver) {{"
        )

        lines.append(
            "        this.driver = driver;"
        )

        lines.append(
            "        PageFactory.initElements(driver, this);"
        )

        lines.append(
            "    }"
        )

        lines.append("")

        # -------------------------
        # GETTERS
        # -------------------------

        for field_name, element in valid_elements:

            lines.append(
                f"    public WebElement get_{field_name}() {{"
            )

            lines.append(
                f"        return {field_name};"
            )

            lines.append(
                "    }"
            )

            lines.append("")

        # -------------------------
        # ACTION METHODS
        # -------------------------

        for field_name, element in valid_elements:

            method_suffix = (
                JavaPageGenerator
                .to_pascal_case(
                    field_name
                )
            )

            element_type = (
                element.element_type
                .lower()
            )

            # INPUTS
            if element_type in [
                "input",
                "textarea"
            ]:

                lines.append(
                    f"    public void enter{method_suffix}(String value) {{"
                )

                lines.append(
                    f"        {field_name}.clear();"
                )

                lines.append(
                    f"        {field_name}.sendKeys(value);"
                )

                lines.append(
                    "    }"
                )

                lines.append("")

            # BUTTONS
            elif element_type == "button":

                lines.append(
                    f"    public void click{method_suffix}() {{"
                )

                lines.append(
                    f"        {field_name}.click();"
                )

                lines.append(
                    "    }"
                )

                lines.append("")

            # DROPDOWNS
            elif element_type == "dropdown":

                lines.append(
                    f"    public void select{method_suffix}(String value) {{"
                )

                lines.append(
                    f"        new Select({field_name}).selectByVisibleText(value);"
                )

                lines.append(
                    "    }"
                )

                lines.append("")

            # CHECKBOX
            elif element_type == "checkbox":

                lines.append(
                    f"    public void check{method_suffix}() {{"
                )

                lines.append(
                    f"        if(!{field_name}.isSelected()) {{"
                )

                lines.append(
                    f"            {field_name}.click();"
                )

                lines.append(
                    "        }"
                )

                lines.append(
                    "    }"
                )

                lines.append("")

            # RADIO
            elif element_type == "radio":

                lines.append(
                    f"    public void select{method_suffix}() {{"
                )

                lines.append(
                    f"        {field_name}.click();"
                )

                lines.append(
                    "    }"
                )

                lines.append("")

            # COMMON DISPLAY CHECK

            lines.append(
                f"    public boolean is{method_suffix}Visible() {{"
            )

            lines.append(
                f"        return {field_name}.isDisplayed();"
            )

            lines.append(
                "    }"
            )

            lines.append("")

        lines.append(
            "}"
        )

        return "\n".join(
            lines
        )

    @staticmethod
    def save(
        page_object: PageObject
    ):

        output_dir = Path(
            "generated_framework/pages"
        )

        output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        class_name = (
            JavaPageGenerator
            .get_clean_page_name(
                page_object.page_name
            )
            + ".java"
        )

        java_code = (
            JavaPageGenerator
            .generate(
                page_object
            )
        )

        file_path = (
            output_dir
            / class_name
        )

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(
                java_code
            )

        GenerationManifest.add_page(
            class_name
        )

        return str(
            file_path
        )