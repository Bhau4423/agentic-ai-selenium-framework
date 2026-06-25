from langgraph_workflow.workflow import (
    LangGraphWorkflow
)

from pathlib import Path


def main():

    document = Path(
        "input/srs_document.txt"
    ).read_text(
        encoding="utf-8"
    )

    graph = (
        LangGraphWorkflow.build()
    )

    result = graph.invoke(

        {
            "requirement_document": document,
            "review_iteration": 1
        }

    )

    print(
        "\n========== FINAL STATE =========="
    )

    print(result)


if __name__ == "__main__":

    main()