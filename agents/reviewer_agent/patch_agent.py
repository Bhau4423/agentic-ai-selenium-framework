from models.patch_report_model import (
    PatchReport
)

from agents.reviewer_agent.impact_analyzer import (
    ImpactAnalyzer
)

from agents.reviewer_agent.patch_executor import (
    PatchExecutor
)

from agents.reviewer_agent.patch_report_generator import (
    PatchReportGenerator
)


class PatchAgent:

    @staticmethod
    def patch(
        findings,
        iteration: int = 1
    ):

        print(
            "\nCreating Patch Plans..."
        )

        patch_plans = (
            ImpactAnalyzer.analyze(
                findings
            )
        )

        print(
            f"Patch Plans: "
            f"{len(patch_plans)}"
        )

        print(
            "\nExecuting Patches..."
        )

        patch_results = (
            PatchExecutor.execute(
                patch_plans
            )
        )

        successful_patches = len(
            [
                plan
                for plan in patch_results
                if plan.patch_status
                == "COMPLETED"
            ]
        )

        failed_patches = len(
            [
                plan
                for plan in patch_results
                if plan.patch_status
                == "FAILED"
            ]
        )

        report = PatchReport(

            iteration=iteration,

            total_patches=len(
                patch_results
            ),

            successful_patches=
            successful_patches,

            failed_patches=
            failed_patches,

            patches=
            patch_results
        )

        report_file = (
            PatchReportGenerator.save(
                report
            )
        )

        print(
            f"\nPatch Report: "
            f"{report_file}"
        )

        print(
            f"Successful Patches: "
            f"{successful_patches}"
        )

        print(
            f"Failed Patches: "
            f"{failed_patches}"
        )

        return {

            "successful":
                successful_patches,

            "failed":
                failed_patches,

            "patches":
                patch_results,

            "report":
                report_file
        }