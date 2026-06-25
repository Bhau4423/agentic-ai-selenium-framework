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

    # --------------------------------
    # APPROVED
    # --------------------------------

    if findings == 0:

        state[
            "status"
        ] = "APPROVED"

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

    # --------------------------------
    # REJECTED
    # --------------------------------

    elif (
        current_iteration
        >=
        MAX_ITERATIONS
    ):

        state[
            "status"
        ] = "REJECTED"

        print(
            "\n====================================="
        )

        print(
            "MAX REVIEW ITERATIONS REACHED"
        )

        print(
            "FRAMEWORK REJECTED"
        )

        print(
            "====================================="
        )

    # --------------------------------
    # PATCH REQUIRED
    # --------------------------------

    else:

        state[
            "status"
        ] = "PATCH"

        print(
            "\n====================================="
        )

        print(
            "FINDINGS DETECTED"
        )

        print(
            "PATCH CYCLE REQUIRED"
        )

        print(
            "====================================="
        )

    print(
        f"\nApproval Status: "
        f"{state['status']}"
    )

    print(
        f"Review Iteration: "
        f"{current_iteration}"
    )

    print(
        f"Remaining Findings: "
        f"{findings}"
    )

    return state