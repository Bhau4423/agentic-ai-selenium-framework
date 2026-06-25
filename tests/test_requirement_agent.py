from agents.requirement_agent.agent import (
    RequirementAgent
)

from pathlib import Path


def main():

    file_path = Path(
        "input/srs_document.txt"
    )

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        document = file.read()

    agent = RequirementAgent()

    agent.analyze(document)


if __name__ == "__main__":
    main()