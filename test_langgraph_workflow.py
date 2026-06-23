from pathlib import Path

from langgraph_workflow.workflow import (
    LangGraphWorkflow
)


requirement_file = Path(
    "input/srs_document.txt"
)

requirement_document = (
    requirement_file.read_text(
        encoding="utf-8"
    )
)

graph = (
    LangGraphWorkflow.build()
)

result = graph.invoke(

    {
        "requirement_document":
            requirement_document,

        "requirement_result":
            {},

        "discovery_result":
            {},

        "generation_result":
            {},

        "review_result":
            {},

        "review_iteration": 1,

        "status":
            "STARTED"
    }
)

print(
    "\n========== LANGGRAPH RESULT =========="
)

print(
    f"Status: {result['status']}"
)

print(
    f"Review Result: "
    f"{result['review_result']}"
)