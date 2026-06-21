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

    return state