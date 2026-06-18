from pathlib import Path

from models.page_object_model import (
    PageObject
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
            class_name += word.capitalize()

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

        locator_type = locator_type.lower()

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
    def generate(
        page_object: PageObject
    ):

        class_name = (
            JavaPageGenerator.get_clean_page_name(
                page_object.page_name
            )
        )

        lines = []

        lines.append(
            "package pages;"
        )

        lines.append("")
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

        lines.append("")
        lines.append(
            f"public class {class_name} {{"
        )

        lines.append("")
        lines.append(
            "    private WebDriver driver;"
        )

        lines.append("")

        valid_elements = []

        for element in page_object.elements:

            annotation = (
                JavaPageGenerator.get_locator_annotation(
                    element.locator_type,
                    element.locator_value
                )
            )

            if not annotation:
                continue

            field_name = (
                JavaPageGenerator.get_field_name(
                    element.element_name
                )
            )

            valid_elements.append(
                field_name
            )

            lines.append(
                f"    {annotation}"
            )

            lines.append(
                f"    private WebElement {field_name};"
            )

            lines.append("")

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

        for field_name in valid_elements:

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

        lines.append("}")

        return "\n".join(lines)

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
            JavaPageGenerator.get_clean_page_name(
                page_object.page_name
            )
            + ".java"
        )

        java_code = (
            JavaPageGenerator.generate(
                page_object
            )
        )

        file_path = (
            output_dir / class_name
        )

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(
                java_code
            )

        return str(file_path)