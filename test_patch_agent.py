from agents.reviewer_agent.agent import (
    ReviewerAgent
)

from agents.reviewer_agent.patch_agent import (
    PatchAgent
)

reviewer = ReviewerAgent()

review_result = (
    reviewer.review()
)

if (
    review_result["total_findings"]
    > 0
):

    patch_result = (
        PatchAgent.patch(
            review_result["findings"],
            iteration=1
        )
    )

    print(
        "\nPATCH RESULT:"
    )

    print(
        patch_result
    )

else:

    print(
        "\nNo findings to patch."
    )