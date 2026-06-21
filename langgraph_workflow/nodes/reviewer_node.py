from agents.reviewer_agent.review_cycle_manager import (
    ReviewCycleManager
)


def reviewer_node(
    state
):

    print(
        "\n[LangGraph] Reviewer Node"
    )

    result = (
        ReviewCycleManager.execute()
    )

    state[
        "review_result"
    ] = result

    state[
        "status"
    ] = result.get(
        "status",
        "REJECTED"
    )

    return state