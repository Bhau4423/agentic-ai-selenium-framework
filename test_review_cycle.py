from agents.reviewer_agent.review_cycle_manager import (
    ReviewCycleManager
)


def main():

    print(
        "\n====================================="
    )

    print(
        "TESTING FULL REVIEW CYCLE"
    )

    print(
        "====================================="
    )

    result = (
        ReviewCycleManager.execute()
    )

    print(
        "\n========== FINAL RESULT =========="
    )

    print(result)


if __name__ == "__main__":

    main()