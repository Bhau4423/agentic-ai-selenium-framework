MAX_ITERATIONS = 5


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

    findings = (
        review_result.get(
            "total_findings",
            0
        )
    )

    current_iteration = (
        state.get(
            "review_iteration",
            1
        )
    )

    if findings == 0:

        state[
            "status"
        ] = "APPROVED"

    elif (
        current_iteration
        >=
        MAX_ITERATIONS
    ):

        state[
            "status"
        ] = "REJECTED"

    else:

        state[
            "status"
        ] = "REVIEWED"

    print(
        f"Approval Status: "
        f"{state['status']}"
    )

    print(
        f"Review Iteration: "
        f"{current_iteration}"
    )

    return state