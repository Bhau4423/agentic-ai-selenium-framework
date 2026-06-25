from pathlib import Path
import re

from models.patch_plan_model import (
    PatchPlan
)

from agents.reviewer_agent.locator_repair_engine import (
    LocatorRepairEngine
)

from agents.reviewer_agent.hallucination_patch_strategy import (
    HallucinationPatchStrategy
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
                '!driver.getCurrentUrl().isEmpty());'
            )

    # ---------------------------------
    # REPLACE DUMMY ASSERTION
    # ---------------------------------

        if (
            plan.patch_action
            ==
            "REPLACE_DUMMY_ASSERTION"
        ):

            dummy_assertions = [

                "Assert.assertTrue(true);",

                "Assert.assertFalse(false);",

                "Assert.assertEquals(true,true);",

                "Assert.assertEquals(true, true);",

                "Assert.assertEquals(1,1);",

                "Assert.assertEquals(1, 1);",

                'Assert.assertEquals("abc","abc");',

                'Assert.assertEquals("abc", "abc");'
            ]

            for dummy in dummy_assertions:

                content = (
                    content.replace(
                        dummy,
                        assertion_code
                    )
                )

    # ---------------------------------
    # REPLACE WEAK ASSERTION
    # ---------------------------------

        elif (
            plan.patch_action
            ==
            "REPLACE_WEAK_ASSERTION"
        ):

            weak_assertions = [

                "Assert.assertNotNull(driver);",

                "Assert.assertNotNull(page);",

                "Assert.assertNotNull(response);"
            ]

            for weak in weak_assertions:

                content = (
                    content.replace(
                        weak,
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

            print("\n===== ASSERTION PATCH DEBUG =====")
            print("Scenario :", scenario_title)
            print("Assertion:", assertion_code)
            content = (
               
                content.replace(
                    "\n    }\n",
                    f"\n        {assertion_code}\n\n    }}\n"
                )
            )

            print("Assertion inserted.")
            print("===== END ASSERTION PATCH DEBUG =====\n")

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

        print("\n===== WAIT PATCH DEBUG =====")
        print(f"Reason        : {plan.reason}")
        print(f"Target Action : {target_action}")

        if not target_action:

            return content

        element_match = re.search(
            r"page\.get_(\w+)\(\)",
            target_action
        )

        print(f"Element Match : {element_match}")
        if not element_match:

            return content

        element_name = (
            element_match.group(1)
        )

        print(f"Element Name  : {element_name}")

        interaction_keywords = [

            ".click(",
            ".sendKeys(",
            ".clear(",
            ".submit(",
            ".selectByVisibleText(",
            ".selectByValue(",
            ".selectByIndex("
        ]

        wait_code = (
            "wait.until("
            "ExpectedConditions."
            f"elementToBeClickable(page.get_{element_name}()));"
        )

        lines = content.splitlines()

        updated_lines = []

        wait_inserted = False

        for index, line in enumerate(lines):

            stripped_line = (
                line.strip()
            )

            is_target_interaction = (

                f"page.get_{element_name}()"
                in stripped_line

                and

                any(

                    keyword in stripped_line

                    for keyword in interaction_keywords
                )
            )

            print(f"Checking Line : {stripped_line}")

            if is_target_interaction:

                print("Interaction Found")

                wait_already_exists = False

                search_start = max(
                    0,
                    len(updated_lines) - 10
                )

                for previous_line in updated_lines[
                    search_start:
                ]:

                    stripped_previous = (
                        previous_line.strip()
                    )

                    if (
                        stripped_previous.startswith("//")
                    ):

                        continue

                    if (
                        "wait.until("
                        in stripped_previous
                    ):

                        wait_already_exists = True
                        break

                if not wait_already_exists:

                    indentation = (
                        line[
                            :
                            len(line)
                            -
                            len(
                                line.lstrip()
                            )
                        ]
                    )

                    updated_lines.append(
                        indentation
                        + wait_code
                    )

                    wait_inserted = True

            updated_lines.append(
                line
            )

        if wait_inserted:

            print(
                f"Inserted wait for element: {element_name}"
            )

            print(f"Wait Inserted : {wait_inserted}")
            print("===== END WAIT PATCH DEBUG =====\n")

        return "\n".join(
            updated_lines
        )

    @staticmethod
    def apply_hallucinated_method_patch(
        content: str,
        plan: PatchPlan
    ):

        invalid_getter = (
            HallucinationPatchStrategy
            .extract_invalid_getter(
                plan.reason
            )
        )

        if not invalid_getter:

            print(
                "Unable to identify hallucinated getter."
            )

            return content

        replacement = (
            HallucinationPatchStrategy
            .find_replacement(
                invalid_getter
            )
        )

        print(
            "\n===== HALLUCINATION PATCH DEBUG ====="
        )

        print(
            f"Invalid Getter : {invalid_getter}"
        )

        print(
            f"Replacement    : {replacement}"
        )

        if not replacement:

            print(
                "No replacement found."
            )

            return content

        content = re.sub(
            rf"get_{re.escape(invalid_getter)}\(",
            f"get_{replacement}(",
            content
        )

        print(
            "Getter replaced successfully."
        )

        print(
            "===== END DEBUG =====\n"
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

        completed_patches = []

        for plan in patch_plans:

            if PatchExecutor.should_skip_patch(
                plan,
                completed_patches
            ):

                print(
                    "\n----------------------------------------"
                )

                print(
                    f"Skipping : {plan.file_name}"
                )

                print(
                    f"Reason   : {plan.category} already resolved."
                )

                print(
                    "----------------------------------------"
                )

                plan.patch_status = "SKIPPED"

                results.append(
                    plan
                )

                continue

            if PatchExecutor.should_skip_patch(
                plan,
                completed_patches
            ):

                print(
                    "\nSkipping Patch "
                    f"({plan.category}) - "
                    "Already resolved."
                )

                plan.patch_status = "SKIPPED"

                results.append(
                    plan
                )

                continue

            print(
                "\n----------------------------------------"
            )

            print(
                f"File   : {plan.file_name}"
            )

            print(
                f"Action : {plan.patch_action}"
            )

            print(
                "----------------------------------------"
            )

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

                    completed_patches.append(
                        plan
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

                    completed_patches.append(
                        plan
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

                    completed_patches.append(
                        plan
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

                original_content = content

                # ---------------------------------
                # ASSERTIONS
                # ---------------------------------

                if (
                    plan.patch_action
                    in
                    [
                        "REPLACE_DUMMY_ASSERTION",
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
                    in
                    [
                        "REMOVE_HALLUCINATED_METHOD",
                        "REPAIR_HALLUCINATED_METHOD"
                    ]
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

                if content == original_content:

                    print(
                        "\nPatch produced no changes."
                    )

                    plan.patch_status = (
                        "FAILED"
                    )

                else:

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

                    completed_patches.append(
                        plan
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
    
    @staticmethod
    def should_skip_patch(
        plan: PatchPlan,
        completed_patches: list
    ):

    # ---------------------------------
    # Hallucination depends on Locator
    # ---------------------------------

        if (
            plan.category
            ==
            "HALLUCINATED_METHOD"
        ):

            for completed in completed_patches:

                if (
                    completed.category
                    ==
                    "LOCATOR_MISSING_GETTER"
                ):

                    return True

        return False