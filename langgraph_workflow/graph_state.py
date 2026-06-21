from typing import TypedDict


class GraphState(TypedDict):

    requirement_document: str

    requirement_result: dict

    discovery_result: dict

    generation_result: dict

    review_result: dict

    patch_result: dict

    status: str