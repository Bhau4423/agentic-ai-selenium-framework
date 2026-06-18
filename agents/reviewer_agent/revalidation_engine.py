from agents.reviewer_agent.agent import (
    ReviewerAgent
)

from agents.reviewer_agent.patch_agent import (
    PatchAgent
)


class RevalidationEngine:

    MAX_ITERATIONS = 5

    @staticmethod
    def execute():

        reviewer = (
            ReviewerAgent()
        )

        iteration = 1

        while (
            iteration
            <=
            RevalidationEngine.MAX_ITERATIONS
        ):

            print(
                f"\n========== ITERATION {iteration} =========="
            )

            result = (
                reviewer.review(
                    iteration
                )
            )

            if (
                result["total_findings"]
                == 0
            ):

                print(
                    "\nFRAMEWORK APPROVED"
                )

                return {

                    "status":
                    "APPROVED",

                    "iteration":
                    iteration
                }

            report = (
                reviewer.review(
                    iteration
                )
            )

            findings_count = (
                report[
                    "total_findings"
                ]
            )

            if findings_count == 0:

                return {

                    "status":
                    "APPROVED",

                    "iteration":
                    iteration
                }

            print(
                "\nPatching Findings..."
            )

            # Temporary placeholder

            iteration += 1

        return {

            "status":
            "REVIEW_LIMIT_REACHED",

            "iteration":
            RevalidationEngine.MAX_ITERATIONS
        }