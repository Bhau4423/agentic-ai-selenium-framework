import re
from pathlib import Path

from models.semantic_mapping_model import (
    SemanticMapping,
    SemanticElement
)

from agents.generator_agent.wait_generator import (
    WaitGenerator
)

from agents.generator_agent.assertion_generator import (
    AssertionGenerator
)


class JavaTestGenerator:

    @staticmethod
    def sanitize_text(
        text: str
    ):

        if not text:
            return ""

        text = re.sub(
            r"[^A-Za-z0-9 ]",
            " ",
            text
        )

        text = re.sub(
            r"\s+",
            " ",
            text
        )

        return text.strip()

    @staticmethod
    def create_method_name(
        title: str
    ):

        title = (
            JavaTestGenerator
            .sanitize_text(
                title
            )
        )

        words = title.split()

        if not words:
            return "generatedTest"

        method_name = words[0].lower()

        for word in words[1:]:

            method_name += (
                word.capitalize()
            )

        return method_name

    @staticmethod
    def create_class_name(
        scenario_title: str
    ):

        scenario_title = (
            JavaTestGenerator
            .sanitize_text(
                scenario_title
            )
        )

        words = scenario_title.split()

        class_name = ""

        for word in words:

            class_name += (
                word.capitalize()
            )

        if not class_name:

            class_name = (
                "Generated"
            )

        if not class_name.endswith(
            "Test"
        ):

            class_name += "Test"

        return class_name

    @staticmethod
    def get_page_class_name(
        page_name: str
    ):

        if not page_name:

            return "GeneratedPage"

        page_name = (
            page_name.split("|")[0]
            .strip()
        )

        page_name = (
            JavaTestGenerator
            .sanitize_text(
                page_name
            )
        )

        words = page_name.split()

        class_name = ""

        for word in words:

            class_name += (
                word.capitalize()
            )

        if not class_name:

            class_name = (
                "GeneratedPage"
            )

        if not class_name.endswith(
            "Page"
        ):

            class_name += "Page"

        return class_name

    @staticmethod
    def get_safe_element_name(
        element_name: str
    ):

        if not element_name:

            return "unknownElement"

        element_name = re.sub(
            r"[^A-Za-z0-9_]",
            "_",
            element_name
        )

        element_name = re.sub(
            r"_+",
            "_",
            element_name
        )

        return element_name

    @staticmethod
    def generate_action(
        semantic_element: SemanticElement
    ):

        element_name = (
            JavaTestGenerator.get_safe_element_name(
                semantic_element.element_name
            )
        )

        action_type = (
            semantic_element.action_type
            .upper()
        )

        if action_type == "SEND_KEYS":

            return (
                f'page.get_{element_name}()'
                '.sendKeys("TEST_DATA");'
            )

        if action_type == "CLICK":

            return (
                f'page.get_{element_name}()'
                '.click();'
            )

        if action_type == "SELECT":

            return (
                f'// TODO: Select value for '
                f'{element_name}'
            )

        if action_type == "ASSERT":

            return (
                "// Assertion handled by "
                "AssertionGenerator"
            )

        return (
            f"// UNKNOWN ACTION : "
            f"{action_type}"
        )

    @staticmethod
    def generate(
        semantic_mapping: SemanticMapping
    ):

        class_name = (
            JavaTestGenerator.create_class_name(
                semantic_mapping.scenario_title
            )
        )

        method_name = (
            JavaTestGenerator.create_method_name(
                semantic_mapping.scenario_title
            )
        )

        page_class = (
            JavaTestGenerator.get_page_class_name(
                semantic_mapping.page_name
            )
        )

        lines = []

        lines.append(
            "package tests;"
        )

        lines.append("")

        lines.append(
            "import org.testng.Assert;"
        )

        lines.append(
            "import org.testng.annotations.Test;"
        )

        lines.append(
            "import org.openqa.selenium.support.ui.ExpectedConditions;"
        )

        lines.append(
            "import base.BaseTest;"
        )

        lines.append(
            f"import pages.{page_class};"
        )

        lines.append("")

        lines.append(
            f"public class {class_name} extends BaseTest {{"
        )

        lines.append("")

        lines.append(
            "    @Test"
        )

        lines.append(
            f"    public void {method_name}() {{"
        )

        lines.append("")

        lines.append(
            f"        {page_class} page = "
            f"new {page_class}(driver);"
        )

        lines.append("")

        for element in (
            semantic_mapping.matched_elements
        ):

            wait_code = (
                WaitGenerator.generate(
                    element.action_type,
                    element.element_name
                )
            )

            lines.append(
                f"        {wait_code}"
            )

            action_code = (
                JavaTestGenerator.generate_action(
                    element
                )
            )

            if (
                not action_code.startswith(
                    "// Assertion handled"
                )
            ):

                lines.append(
                    "        "
                    + action_code
                )

                lines.append("")

        assertion_code = (
            AssertionGenerator.generate(
                semantic_mapping.scenario_title,
                semantic_mapping.scenario_type
            )
        )

        lines.append(
            f"        {assertion_code}"
        )

        lines.append("")

        lines.append(
            "    }"
        )

        lines.append("")

        lines.append(
            "}"
        )

        return "\n".join(lines)

    @staticmethod
    def save(
        semantic_mapping: SemanticMapping
    ):

        output_dir = Path(
            "generated_framework/tests"
        )

        output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        file_name = (
            JavaTestGenerator.create_class_name(
                semantic_mapping.scenario_title
            )
            + ".java"
        )

        java_code = (
            JavaTestGenerator.generate(
                semantic_mapping
            )
        )

        file_path = (
            output_dir / file_name
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