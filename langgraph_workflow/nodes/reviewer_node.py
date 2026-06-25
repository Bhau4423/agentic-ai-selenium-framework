

from agents.reviewer_agent.agent import (
    ReviewerAgent
)


def reviewer_node(
    state
):

    print(
        "\n[LangGraph] Reviewer Node"
    )

    iteration = (
        state.get(
            "review_iteration",
            1
        )
    )

    reviewer = (
        ReviewerAgent()
    )

    result = (
        reviewer.review(
            iteration
        )
    )

    state[
        "review_result"
    ] = result

    state[
        "review_iteration"
    ] = iteration + 1

    return state