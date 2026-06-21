from models.patch_plan_model import (
    PatchPlan
)

from models.review_finding_model import (
    ReviewFinding
)


class ImpactAnalyzer:

    @staticmethod
    def analyze(
        findings: list[ReviewFinding]
    ):

        patch_plans = []

        for finding in findings:

            patch_action = "UNKNOWN"

            category = (
                finding.category.upper()
            )

            description = (
                finding.description.lower()
            )

            # ---------------------------------
            # ASSERTION
            # ---------------------------------

            if category == "ASSERTION":

                if (
                    "weak assertion"
                    in description
                ):

                    patch_action = (
                        "REPLACE_WEAK_ASSERTION"
                    )

                elif (
                    "no assertion"
                    in description
                ):

                    patch_action = (
                        "ADD_ASSERTION"
                    )

            # ---------------------------------
            # WAIT
            # ---------------------------------

            elif category == "WAIT":

                patch_action = (
                    "ADD_MISSING_WAIT"
                )

            # ---------------------------------
            # HALLUCINATED METHOD
            # ---------------------------------

            elif (
                category
                == "HALLUCINATED_METHOD"
            ):

                patch_action = (
                    "REMOVE_HALLUCINATED_METHOD"
                )

            # ---------------------------------
            # LOCATOR ISSUES
            # ---------------------------------

            elif (
                category
                == "LOCATOR_MISSING_GETTER"
            ):

                patch_action = (
                    "GENERATE_MISSING_GETTER"
                )

            elif (
                category
                == "HALLUCINATED_LOCATOR"
            ):

                patch_action = (
                    "REPLACE_INVALID_LOCATOR"
                )

            # ---------------------------------
            # COVERAGE
            # ---------------------------------

            elif (
                category
                == "COVERAGE"
            ):

                patch_action = (
                    "GENERATE_MISSING_TEST"
                )

            # ---------------------------------
            # MISSING SCRIPT
            # ---------------------------------

            elif category in [

                "MISSING_SCRIPT",

                "MISSING_TEST_SCRIPT"

            ]:

                patch_action = (
                    "GENERATE_MISSING_SCRIPT"
                )

            # ---------------------------------
            # EDGE CASE
            # ---------------------------------

            elif category in [

                "EDGE_CASE",

                "EDGE_CASE_NOT_COVERED"

            ]:

                patch_action = (
                    "GENERATE_EDGE_CASE_TEST"
                )

            # ---------------------------------
            # TRACEABILITY
            # ---------------------------------

            elif (
                category
                == "TRACEABILITY"
            ):

                patch_action = (
                    "UPDATE_TRACEABILITY"
                )

            # ---------------------------------
            # BUILD PATCH PLAN
            # ---------------------------------

            patch_plans.append(

                PatchPlan(

                    finding_id=
                    finding.finding_id,

                    file_name=
                    finding.file_name,

                    category=
                    finding.category,

                    patch_action=
                    patch_action,

                    reason=
                    finding.description,

                    patch_status=
                    "PENDING",

                    scenario_id=
                    finding.scenario_id,

                    requirement_id=
                    finding.requirement_id,

                    notes=
                    finding.recommendation
                )
            )

        return patch_plans