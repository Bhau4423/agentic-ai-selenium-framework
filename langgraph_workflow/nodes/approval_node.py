def approval_node(
    state
):

    print(
        "\n[LangGraph] Approval Node"
    )

    review_result = (
        state.get(
            "review_result",
            {}
        )
    )

    state[
        "status"
    ] = review_result.get(
        "status",
        "REJECTED"
    )

    return state