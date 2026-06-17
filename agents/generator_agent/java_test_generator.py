from pathlib import Path

from agents.generator_agent.action_mapper import (
    ActionMapper
)

from models.scenario_mapping_model import (
    ScenarioMapping
)


class JavaTestGenerator:

    @staticmethod
    def create_method_name(
        title: str
    ):

        words = (
            title
            .replace("-", " ")
            .replace("_", " ")
            .split()
        )

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

        words = (
            scenario_title
            .replace("-", " ")
            .replace("_", " ")
            .split()
        )

        class_name = ""

        for word in words:

            class_name += word.capitalize()

        return class_name + "Test"

    @staticmethod
    def generate_action(
        action_type: str,
        element_name: str
    ):

        safe_name = (
            element_name
            .replace(" ", "_")
            .replace("-", "_")
            .replace("[", "_")
            .replace("]", "_")
        )

        if action_type == "SEND_KEYS":

            return (
                f'page.get_{safe_name}()'
                '.sendKeys("TEST_DATA");'
            )

        if action_type == "CLICK":

            return (
                f"page.get_{safe_name}()"
                ".click();"
            )

        if action_type == "ASSERT":

            return (
                "Assert.assertTrue(true);"
            )

        return (
            f"// UNKNOWN ACTION : "
            f"{action_type}"
        )

    @staticmethod
    def generate(
        scenario_mapping: ScenarioMapping,
        scenario: dict
    ):

        class_name = (
            JavaTestGenerator.create_class_name(
                scenario_mapping.scenario_title
            )
        )

        method_name = (
            JavaTestGenerator.create_method_name(
                scenario_mapping.scenario_title
            )
        )

        page_class = (
            scenario_mapping.page_name
            .replace(" ", "")
            .replace("|", "")
            .replace("-", "")
            + "Page"
        )

        actions = (
            ActionMapper.map_steps(
                scenario
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
            f"import pages.{page_class};"
        )

        lines.append("")
        lines.append(
            f"public class {class_name} {{"
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

        element_index = 0

        for action in actions:

            action_type = (
                action["action"]
            )

            if action_type == "NAVIGATE":
                continue

            if (
                element_index
                >= len(
                    scenario_mapping.matched_elements
                )
            ):
                continue

            element_name = (
                scenario_mapping
                .matched_elements[
                    element_index
                ]
            )

            lines.append(
                "        "
                + JavaTestGenerator.generate_action(
                    action_type,
                    element_name
                )
            )

            if action_type != "ASSERT":

                element_index += 1

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
        scenario_mapping: ScenarioMapping,
        scenario: dict
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
                scenario_mapping.scenario_title
            )
            + ".java"
        )

        java_code = (
            JavaTestGenerator.generate(
                scenario_mapping,
                scenario
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