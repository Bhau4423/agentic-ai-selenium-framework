from agents.generator_agent.agent import GeneratorAgent


def main():

    print(
        "\n====================================="
    )

    print(
        "TESTING AGENT 3 - GENERATOR AGENT"
    )

    print(
        "=====================================\n"
    )

    agent = GeneratorAgent()

    result = (
        agent.generate_framework()
    )

    print(
        "\n========== SUMMARY =========="
    )

    print(
        f"Requirement Mappings : "
        f"{result['requirement_mappings']}"
    )

    print(
        f"Page Objects : "
        f"{result['page_objects']}"
    )

    print(
        f"Scenario Mappings : "
        f"{result['scenario_mappings']}"
    )

    print(
        f"Generated Pages : "
        f"{len(result['generated_pages'])}"
    )

    print(
        f"Generated Tests : "
        f"{len(result['generated_tests'])}"
    )

    print(
        f"Traceability File : "
        f"{result['traceability']}"
    )

    print(
        f"Base Test : "
        f"{result['base_test']}"
    )

    print(
        f"Config : "
        f"{result['config']}"
    )

    print(
        "\n========== AGENT 3 SUCCESS =========="
    )


if __name__ == "__main__":
    main()