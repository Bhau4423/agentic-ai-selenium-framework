from agents.reviewer_agent.agent import (
    ReviewerAgent
)

from agents.reviewer_agent.patch_agent import (
    PatchAgent
)

from agents.reviewer_agent.final_validation_report_generator import (
    FinalValidationReportGenerator
)


class RevalidationEngine:

    MAX_ITERATIONS = 5

    REVIEWERS_EXECUTED = [

        "AssertionReviewer",

        "CoverageReviewer",

        "WaitReviewer",

        "LocatorReviewer",

        "MissingScriptReviewer",

        "EdgeCaseReviewer",

        "TraceabilityReviewer",

        "HallucinationReviewer"
    ]

    @staticmethod
    def validate(
        iteration: int
    ):

        reviewer = ReviewerAgent()

        review_result = (
            reviewer.review(
                iteration
            )
        )

        return review_result[
            "findings"
        ]

    @staticmethod
    def execute():

        reviewer = (
            ReviewerAgent()
        )

        total_findings = 0

        resolved_findings = 0

        patches_applied = 0

        iteration = 1

        while (

            iteration
            <=
            RevalidationEngine.MAX_ITERATIONS

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

            findings_count = (
                review_result[
                    "total_findings"
                ]
            )

            # --------------------------------
            # APPROVED
            # --------------------------------

            if findings_count == 0:

                report = (
                    FinalValidationReportGenerator.generate(

                        status=
                        "APPROVED",

                        iterations=
                        iteration,

                        total_findings=
                        total_findings,

                        resolved_findings=
                        resolved_findings,

                        remaining_findings=
                        0,

                        patches_applied=
                        patches_applied,

                        reviewers_executed=
                        RevalidationEngine.REVIEWERS_EXECUTED,

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
                    f"\nFINAL REPORT: "
                    f"{report_file}"
                )

                return {

                    "status":
                    "APPROVED",

                    "iteration":
                    iteration,

                    "report":
                    report_file
                }

            # --------------------------------
            # TRACK FINDINGS
            # --------------------------------

            total_findings += (
                findings_count
            )

            print(
                "\nPatching Findings..."
            )

            patch_result = (
                PatchAgent.patch(
                    findings,
                    iteration
                )
            )

            successful_patches = (
                patch_result[
                    "successful"
                ]
            )

            patches_applied += (
                successful_patches
            )

            resolved_findings += (
                successful_patches
            )

            iteration += 1

        # --------------------------------
        # REVIEW LIMIT REACHED
        # --------------------------------

        report = (
            FinalValidationReportGenerator.generate(

                status=
                "REVIEW_LIMIT_REACHED",

                iterations=
                RevalidationEngine.MAX_ITERATIONS,

                total_findings=
                total_findings,

                resolved_findings=
                resolved_findings,

                remaining_findings=
                max(
                    0,
                    total_findings
                    -
                    resolved_findings
                ),

                patches_applied=
                patches_applied,

                reviewers_executed=
                RevalidationEngine.REVIEWERS_EXECUTED,

                approval_reason=
                "Maximum review iterations reached."
            )
        )

        report_file = (
            FinalValidationReportGenerator.save(
                report
            )
        )

        print(
            f"\nFINAL REPORT: "
            f"{report_file}"
        )

        return {

            "status":
            "REVIEW_LIMIT_REACHED",

            "iteration":
            RevalidationEngine.MAX_ITERATIONS,

            "report":
            report_file
        }