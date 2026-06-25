from agents.reviewer_agent.agent import (
    ReviewerAgent
)

from agents.reviewer_agent.patch_agent import (
    PatchAgent
)

from agents.reviewer_agent.revalidation_engine import (
    RevalidationEngine
)

from agents.reviewer_agent.final_validation_report_generator import (
    FinalValidationReportGenerator
)


class ReviewCycleManager:

    MAX_ITERATIONS = 5

    @staticmethod
    def execute():

        reviewer = ReviewerAgent()

        total_findings = 0

        total_patches = 0

        reviewers_executed = [

            "AssertionReviewer",

            "CoverageReviewer",

            "WaitReviewer",

            "LocatorReviewer",

            "MissingScriptReviewer",

            "EdgeCaseReviewer",

            "TraceabilityReviewer",

            "HallucinationReviewer"
        ]

        for iteration in range(
            1,
            ReviewCycleManager.MAX_ITERATIONS + 1
        ):

            print(
                f"\n========== REVIEW CYCLE {iteration} =========="
            )

            review_result = (
                reviewer.review(
                    iteration
                )
            )

            findings = (
                review_result[
                    "findings"
                ]
            )

            total_findings += len(
                findings
            )

            # -------------------------
            # APPROVED
            # -------------------------

            if len(findings) == 0:

                print(
                    "\n====================================="
                )

                print(
                    "NO FINDINGS DETECTED"
                )

                print(
                    "FRAMEWORK APPROVED"
                )

                print(
                    "====================================="
                )

                report = (
                    FinalValidationReportGenerator.generate(

                        status="APPROVED",

                        iterations=iteration,

                        total_findings=
                        total_findings,

                        resolved_findings=
                        total_findings,

                        remaining_findings=0,

                        patches_applied=
                        total_patches,

                        reviewers_executed=
                        reviewers_executed,

                        approval_reason=
                        "All findings resolved successfully."
                    )
                )

                report_file = (
                    FinalValidationReportGenerator.save(
                        report
                    )
                )

                print(
                    f"\nFINAL REPORT: {report_file}"
                )

                return {

                    "status":
                    "APPROVED",

                    "iteration":
                    iteration,

                    "report":
                    report_file
                }

            # -------------------------
            # PATCH
            # -------------------------

            patch_result = (
                PatchAgent.patch(
                    findings,
                    iteration
                )
            )

            total_patches += (
                patch_result[
                    "successful"
                ]
            )

            # -------------------------
# LAST ITERATION
# -------------------------

            if iteration == ReviewCycleManager.MAX_ITERATIONS:

                print(
                    "\n====================================="
                )

                print(
                    "MAXIMUM REVIEW ITERATIONS REACHED"
                )

                print(
                    "FRAMEWORK REJECTED"
                )

                print(
                    "====================================="
                )

                remaining_findings = findings

                break

# -------------------------
# REVALIDATE
# -------------------------

            remaining_findings = (
                RevalidationEngine.validate(
                    iteration + 1
                )
            ) 

            if len(
                remaining_findings
            ) == 0:

                print(
                    "\n====================================="   
                )

                print(
                    "NO FINDINGS DETECTED"
                )

                print(
                    "FRAMEWORK APPROVED"
                )

                print(
                    "====================================="
                )
                report = (
                    FinalValidationReportGenerator.generate(

                        status="APPROVED",

                        iterations=iteration,

                        total_findings=
                        total_findings,

                        resolved_findings=
                        total_findings,

                        remaining_findings=0,

                        patches_applied=
                        total_patches,

                        reviewers_executed=
                        reviewers_executed,

                        approval_reason=
                        "All findings resolved after patching."
                    )
                )

                report_file = (
                    FinalValidationReportGenerator.save(
                        report
                    )
                )

                return {

                    "status":
                    "APPROVED",

                    "iteration":
                    iteration,

                    "report":
                    report_file
                }

        # -------------------------
        # MAX ITERATION REACHED
        # -------------------------

        report = (
            FinalValidationReportGenerator.generate(

                status="REJECTED",

                iterations=
                ReviewCycleManager.MAX_ITERATIONS,

                total_findings=
                total_findings,

                resolved_findings=
                total_findings
                - len(
                    remaining_findings
                ),

                remaining_findings=
                len(
                    remaining_findings
                ),

                patches_applied=
                total_patches,

                reviewers_executed=
                reviewers_executed,

                approval_reason=
                "Maximum review iterations reached."
            )
        )

        report_file = (
            FinalValidationReportGenerator.save(
                report
            )
        )

        return {

            "status":
            "REJECTED",

            "iteration":
            ReviewCycleManager.MAX_ITERATIONS,

            "report":
            report_file
        }