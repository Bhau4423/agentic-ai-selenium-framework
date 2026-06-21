from agents.generator_agent.agent import (
    GeneratorAgent
)


def generator_node(
    state
):

    print(
        "\n[LangGraph] Generator Node"
    )

    agent = (
        GeneratorAgent()
    )

    result = (
        agent.generate_framework()
    )

    state[
        "generation_result"
    ] = result

    return state