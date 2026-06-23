from agents.reviewer_agent.patch_agent import (
    PatchAgent
)


def patch_node(
    state
):

    print(
        "\n[LangGraph] Patch Node"
    )

    findings = (
        state[
            "review_result"
        ].get(
            "findings",
            []
        )
    )

    if not findings:

        return state

    patch_result = (
        PatchAgent.patch(
            findings
        )
    )

    state[
        "patch_result"
    ] = patch_result

    current_iteration = (
        state.get(
            "review_iteration",
            1
        )
    )

    state[
        "review_iteration"
    ] = (
        current_iteration + 1
    )

    print(
        f"Next Review Iteration: "
        f"{state['review_iteration']}"
    )

    return state