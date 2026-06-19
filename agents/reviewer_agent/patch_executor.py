from pathlib import Path

from models.patch_plan_model import (
    PatchPlan
)

from agents.reviewer_agent.context_builder import (
    ContextBuilder
)

from agents.reviewer_agent.assertion_patch_strategy import (
    AssertionPatchStrategy
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
    def execute(
        patch_plans: list[PatchPlan]
    ):

        results = []

        tests_folder = Path(
            "generated_framework/tests"
        )

        for plan in patch_plans:

            try:

                file_path = (
                    tests_folder
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
                # REQUIREMENT AWARE ASSERTION PATCH
                # ---------------------------------

                if (
                    plan.patch_action
                    ==
                    "REPLACE_WEAK_ASSERTION"
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
                            AssertionPatchStrategy.generate_assertion(
                                context
                            )
                        )

                    else:

                        assertion_code = (
                            "Assert.assertTrue("
                            "driver.getCurrentUrl()"
                            ".length() > 0);"
                        )

                    content = (
                        content.replace(
                            "Assert.assertTrue(true);",
                            assertion_code
                        )
                    )

                # ---------------------------------
                # ADD ASSERTION
                # ---------------------------------

                elif (
                    plan.patch_action
                    ==
                    "ADD_ASSERTION"
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
                            AssertionPatchStrategy.generate_assertion(
                                context
                            )
                        )

                    else:

                        assertion_code = (
                            "Assert.assertTrue("
                            "driver.getCurrentUrl()"
                            ".length() > 0);"
                        )

                    content = (
                        content.replace(
                            "\n    }\n",
                            f"\n        {assertion_code}\n\n    }}\n"
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