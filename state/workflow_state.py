from typing import TypedDict


class WorkflowState(TypedDict):

    requirement_document: str

    requirement_analysis_result: dict

    acceptance_criteria: list

    test_scenarios: list

    page_inventory: dict

    locator_inventory: dict

    validation_messages: list

    generated_framework_path: str

    traceability_matrix: dict

    review_result: dict

    patch_instructions: list

    review_cycle: int