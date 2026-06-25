


from agents.requirement_agent.agent import (
    RequirementAgent
)


def requirement_node(
    state
):

    print(
        "\n[LangGraph] Requirement Node"
    )
    agent = (
        RequirementAgent()
    )

    result = (
        agent.analyze(
            state[
                "requirement_document"
            ]
        )
    )

    state[
        "requirement_result"
    ] = result

    return state