from pathlib import Path
import re

from models.patch_plan_model import (
    PatchPlan
)

from agents.reviewer_agent.locator_repair_engine import (
    LocatorRepairEngine
)

from agents.reviewer_agent.context_builder import (
    ContextBuilder
)

from agents.reviewer_agent.assertion_patch_strategy import (
    AssertionPatchStrategy
)

from agents.reviewer_agent.patch_metadata_extractor import (
    PatchMetadataExtractor
)

from agents.reviewer_agent.missing_script_patch_strategy import (
    MissingScriptPatchStrategy
)

from agents.reviewer_agent.coverage_patch_strategy import (
    CoveragePatchStrategy
)

from agents.reviewer_agent.edge_case_patch_strategy import (
    EdgeCasePatchStrategy
)

from agents.reviewer_agent.getter_patch_strategy import (
    GetterPatchStrategy
)


class PatchExecutor:

    @staticmethod
    def extract_scenario_title(
        file_name: str
    ):

        title = (
            file_name
            .replace(".java", "")
            .replace("Test", "")
        )

        words = []

        current_word = ""

        for char in title:

            if (
                char.isupper()
                and current_word
            ):

                words.append(
                    current_word
                )

                current_word = char

            else:

                current_word += char

        if current_word:

            words.append(
                current_word
            )

        return " ".join(words)

    @staticmethod
    def apply_assertion_patch(
        content: str,
        plan: PatchPlan
    ):

        scenario_title = (
            PatchExecutor.extract_scenario_title(
                plan.file_name
            )
        )

        context = (
            ContextBuilder.get_context(
                scenario_title
            )
        )

        if context:

            assertion_code = (
                AssertionPatchStrategy
                .generate_assertion(
                    context
                )
            )

        else:

            assertion_code = (
                'Assert.assertTrue('
                'driver.getCurrentUrl()'
                '.length() > 0);'
            )

        if (
            plan.patch_action
            ==
            "REPLACE_WEAK_ASSERTION"
        ):

            content = (
                content.replace(
                    "Assert.assertTrue(true);",
                    assertion_code
                )
            )

        elif (
            plan.patch_action
            ==
            "ADD_ASSERTION"
        ):

            content = (
                content.replace(
                    "\n    }\n",
                    f"\n        {assertion_code}\n\n    }}\n"
                )
            )

        return content

    @staticmethod
    def apply_wait_patch(
        content: str,
        plan: PatchPlan
    ):

        target_action = (
            PatchMetadataExtractor
            .extract_missing_wait_target(
                plan.reason
            )
        )

        if not target_action:

            return content

        element_match = re.search(
            r"page\.get_(\w+)\(\)",
            target_action
        )

        if not element_match:

            return content

        element_name = (
            element_match.group(1)
        )

        wait_code = (
            f'wait.until('
            f'ExpectedConditions.'
            f'elementToBeClickable('
            f'page.get_{element_name}()'
            f'));'
        )

        content = content.replace(
            target_action,
            wait_code
            + "\n\n        "
            + target_action
        )

        return content

    @staticmethod
    def apply_hallucinated_method_patch(
        content: str,
        plan: PatchPlan
    ):

        method_name = (
            PatchMetadataExtractor
            .extract_hallucinated_method(
                plan.reason
            )
        )

        if not method_name:

            return content

        patterns = [

            rf".*{re.escape(method_name)}.*\n",

            rf".*visibilityOf\(page\.{re.escape(method_name)}\).*?\n"
        ]

        for pattern in patterns:

            content = re.sub(
                pattern,
                "",
                content
            )

        return content

    @staticmethod
    def generate_missing_getter(
        content: str,
        plan: PatchPlan
    ):

        element_name = (
            GetterPatchStrategy
            .extract_missing_element(
                plan.reason
            )
        )

        if not element_name:

            return content

        getter_code = (
            GetterPatchStrategy
            .generate_getter(
                element_name
            )
        )

        content = content.replace(
            "\n}",
            getter_code + "\n}"
        )

        print(
            f"Generated Getter: "
            f"get_{element_name}()"
        )

        return content

    @staticmethod
    def generate_missing_script(
        plan: PatchPlan
    ):

        if not plan.scenario_id:

            raise ValueError(
                "Scenario ID missing for script generation."
            )

        result = (
            MissingScriptPatchStrategy.generate(
                plan.scenario_id
            )
        )

        generated_file = (
            result.get(
                "file_path"
            )
        )

        print(
            f"Generated Missing Test: "
            f"{generated_file}"
        )

        return generated_file

    @staticmethod
    def generate_missing_test(
        plan: PatchPlan
    ):

        if not plan.scenario_id:

            raise ValueError(
                "Scenario ID missing for coverage generation."
            )

        result = (
            CoveragePatchStrategy.generate(
                plan.scenario_id
            )
        )

        generated_file = (
            result.get(
                "file_path"
            )
        )

        print(
            f"Generated Coverage Test: "
            f"{generated_file}"
        )

        return generated_file

    @staticmethod
    def generate_edge_case_test(
        plan: PatchPlan
    ):

        if not plan.scenario_id:

            raise ValueError(
                "Scenario ID missing for edge case generation."
            )

        result = (
            EdgeCasePatchStrategy.generate(
                plan.scenario_id
            )
        )

        generated_file = (
            result.get(
                "file_path"
            )
        )

        print(
            f"Generated Edge Case Test: "
            f"{generated_file}"
        )

        return generated_file

    @staticmethod
    def execute(
        patch_plans: list[PatchPlan]
    ):

        results = []

        for plan in patch_plans:

            try:

                # ---------------------------------
                # GENERATION PATCHES
                # ---------------------------------

                if (
                    plan.patch_action
                    ==
                    "GENERATE_MISSING_SCRIPT"
                ):

                    PatchExecutor.generate_missing_script(
                        plan
                    )

                    plan.patch_status = (
                        "COMPLETED"
                    )

                    results.append(
                        plan
                    )

                    continue

                elif (
                    plan.patch_action
                    ==
                    "GENERATE_MISSING_TEST"
                ):

                    PatchExecutor.generate_missing_test(
                        plan
                    )

                    plan.patch_status = (
                        "COMPLETED"
                    )

                    results.append(
                        plan
                    )

                    continue

                elif (
                    plan.patch_action
                    ==
                    "GENERATE_EDGE_CASE_TEST"
                ):

                    PatchExecutor.generate_edge_case_test(
                        plan
                    )

                    plan.patch_status = (
                        "COMPLETED"
                    )

                    results.append(
                        plan
                    )

                    continue

                # ---------------------------------
                # FILE LOCATION
                # ---------------------------------

                if plan.category in [

                    "LOCATOR_MISSING_GETTER",

                    "HALLUCINATED_LOCATOR"

                ]:

                    target_folder = Path(
                        "generated_framework/pages"
                    )

                else:

                    target_folder = Path(
                        "generated_framework/tests"
                    )

                file_path = (
                    target_folder
                    / plan.file_name
                )

                if not file_path.exists():

                    plan.patch_status = (
                        "FAILED"
                    )

                    results.append(
                        plan
                    )

                    continue

                with open(
                    file_path,
                    "r",
                    encoding="utf-8"
                ) as file:

                    content = (
                        file.read()
                    )

                # ---------------------------------
                # ASSERTIONS
                # ---------------------------------

                if (
                    plan.patch_action
                    in
                    [
                        "REPLACE_WEAK_ASSERTION",
                        "ADD_ASSERTION"
                    ]
                ):

                    content = (
                        PatchExecutor
                        .apply_assertion_patch(
                            content,
                            plan
                        )
                    )

                # ---------------------------------
                # WAITS
                # ---------------------------------

                elif (
                    plan.patch_action
                    ==
                    "ADD_MISSING_WAIT"
                ):

                    content = (
                        PatchExecutor
                        .apply_wait_patch(
                            content,
                            plan
                        )
                    )

                # ---------------------------------
                # HALLUCINATED METHOD
                # ---------------------------------

                elif (
                    plan.patch_action
                    ==
                    "REMOVE_HALLUCINATED_METHOD"
                ):

                    content = (
                        PatchExecutor
                        .apply_hallucinated_method_patch(
                            content,
                            plan
                        )
                    )

                # ---------------------------------
                # MISSING GETTER
                # ---------------------------------

                elif (
                    plan.patch_action
                    ==
                    "GENERATE_MISSING_GETTER"
                ):

                    content = (
                        PatchExecutor
                        .generate_missing_getter(
                            content,
                            plan
                        )
                    )

                elif (
                    plan.patch_action
                    ==
                    "REPLACE_INVALID_LOCATOR"
                ):

                    content = (
                        LocatorRepairEngine.repair(
                            content,
                            plan.reason
                        )
            )

                with open(
                    file_path,
                    "w",
                    encoding="utf-8"
                ) as file:

                    file.write(
                        content
                    )

                plan.patch_status = (
                    "COMPLETED"
                )

            except Exception as e:

                print(
                    f"Patch Error: {e}"
                )

                plan.patch_status = (
                    "FAILED"
                )

            results.append(
                plan
            )

        return results