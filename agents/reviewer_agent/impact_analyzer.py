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

            patch_action = (
                ImpactAnalyzer._get_patch_action(
                    finding
                )
            )

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

    @staticmethod
    def _get_patch_action(
        finding: ReviewFinding
    ):

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
                "missing assertion"
                in description
            ):

                return (
                    "ADD_ASSERTION"
                )

            if (
                "dummy assertion"
                in description
            ):

                return (
                    "REPLACE_DUMMY_ASSERTION"
                )

            if (
                "weak assertion"
                in description
            ):

                return (
                    "REPLACE_WEAK_ASSERTION"
                )

            return (
                "ADD_ASSERTION"
            )

        # ---------------------------------
        # WAIT
        # ---------------------------------

        if category == "WAIT":

            return (
                "ADD_MISSING_WAIT"
            )

        # ---------------------------------
        # HALLUCINATED METHOD
        # ---------------------------------

        if (
            category
            == "HALLUCINATED_METHOD"
        ):

            return (
                "REPAIR_HALLUCINATED_METHOD"
            )

        # ---------------------------------
        # PAGE OBJECT
        # ---------------------------------

        if (
            category
            == "HALLUCINATED_PAGE_OBJECT"
        ):

            return (
                "GENERATE_MISSING_PAGE"
            )

        # ---------------------------------
        # LOCATOR
        # ---------------------------------

        if (
            category
            == "LOCATOR_MISSING_GETTER"
        ):

            return (
                "GENERATE_MISSING_GETTER"
            )

        if (
            category
            == "HALLUCINATED_LOCATOR"
        ):

            return (
                "REPLACE_INVALID_LOCATOR"
            )

        # ---------------------------------
        # COVERAGE
        # ---------------------------------

        if (
            category
            == "COVERAGE"
        ):

            return (
                "GENERATE_MISSING_TEST"
            )

        # ---------------------------------
        # TRACEABILITY
        # ---------------------------------

        if (
            category
            == "TRACEABILITY"
        ):

            return (
                "UPDATE_TRACEABILITY"
            )

        # ---------------------------------
        # MISSING SCRIPT
        # ---------------------------------

        if category in [

            "MISSING_SCRIPT",

            "MISSING_TEST_SCRIPT"

        ]:

            return (
                "GENERATE_MISSING_SCRIPT"
            )

        # ---------------------------------
        # EDGE CASE
        # ---------------------------------

        if category in [

            "EDGE_CASE",

            "EDGE_CASE_NOT_COVERED"

        ]:

            return (
                "GENERATE_EDGE_CASE_TEST"
            )

        # ---------------------------------
        # FALLBACK
        # ---------------------------------

        return (
            "UNKNOWN"
        )