from agents.reviewer_agent.agent import (
    ReviewerAgent
)


def main():

    print(
        "\n====================================="
    )

    print(
        "TESTING AGENT 4 - REVIEWER AGENT"
    )

    print(
        "====================================="
    )

    agent = ReviewerAgent()

    result = agent.review()

    print(
        "\n========== REVIEW RESULT =========="
    )

    print(result)


if __name__ == "__main__":

    main()