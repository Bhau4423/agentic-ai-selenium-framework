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
                "UNKNOWN"
            )

            # -------------------------
            # ASSERTION ISSUES
            # -------------------------

            if (
                finding.category
                == "ASSERTION"
            ):

                if (
                    "Weak assertion"
                    in finding.description
                ):

                    patch_action = (
                        "REPLACE_WEAK_ASSERTION"
                    )

                elif (
                    "No assertion"
                    in finding.description
                ):

                    patch_action = (
                        "ADD_ASSERTION"
                    )

            # -------------------------
            # COVERAGE ISSUES
            # -------------------------

            elif (
                finding.category
                == "COVERAGE"
            ):

                patch_action = (
                    "GENERATE_MISSING_TEST"
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
                    finding.description
                )
            )

        return patch_plans