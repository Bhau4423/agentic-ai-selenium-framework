from agents.discovery_agent.agent import (
    DiscoveryAgent
)


def discovery_node(
    state
):

    print(
        "\n[LangGraph] Discovery Node"
    )

    agent = (
        DiscoveryAgent()
    )

    result = (
        agent.discover(
            "https://practicetestautomation.com/practice-test-login/"
        )
    )

    state[
        "discovery_result"
    ] = result

    return state