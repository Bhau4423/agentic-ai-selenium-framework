from pathlib import Path

from models.patch_plan_model import (
    PatchPlan
)


class PatchExecutor:

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

                # ------------------
                # REPLACE WEAK ASSERTION
                # ------------------

                if (
                    plan.patch_action
                    ==
                    "REPLACE_WEAK_ASSERTION"
                ):

                    content = (
                        content.replace(
                            "Assert.assertTrue(true);",
                            'Assert.assertTrue('
                            'driver.getCurrentUrl()'
                            '.length() > 0'
                            ');'
                        )
                    )

                # ------------------
                # ADD ASSERTION
                # ------------------

                elif (
                    plan.patch_action
                    ==
                    "ADD_ASSERTION"
                ):

                    content = (
                        content.replace(
                            "\n    }\n",
                            "\n"
                            "        Assert.assertTrue("
                            "driver.getCurrentUrl()"
                            ".length() > 0"
                            ");\n"
                            "\n"
                            "    }\n"
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

            except Exception:

                plan.patch_status = (
                    "FAILED"
                )

            results.append(
                plan
            )

        return results