from models.requirement_model import (
    Requirement
)

from models.acceptance_criteria_model import (
    AcceptanceCriteria
)

from models.scenario_model import (
    TestScenario
)

from models.requirement_analysis_result import (
    RequirementAnalysisResult
)

from agents.requirement_agent.merger import (
    RequirementMerger
)


result_1 = RequirementAnalysisResult(

    requirements=[
        Requirement(
            id="FR-001",
            title="Login",
            description="Login"
        )
    ],

    acceptance_criteria=[
        AcceptanceCriteria(
            id="AC-001",
            requirement_id="FR-001",
            description="Login success"
        )
    ],

    positive_scenarios=[],

    negative_scenarios=[],

    boundary_scenarios=[]
)

result_2 = RequirementAnalysisResult(

    requirements=[
        Requirement(
            id="FR-001",
            title="Upload",
            description="Upload"
        )
    ],

    acceptance_criteria=[
        AcceptanceCriteria(
            id="AC-001",
            requirement_id="FR-001",
            description="Upload success"
        )
    ],

    positive_scenarios=[],

    negative_scenarios=[],

    boundary_scenarios=[]
)

merged = RequirementMerger.merge(
    [
        result_1,
        result_2
    ]
)

print(
    f"Requirements: "
    f"{len(merged.requirements)}"
)

print(
    f"Acceptance Criteria: "
    f"{len(merged.acceptance_criteria)}"
)

for requirement in merged.requirements:

    print(
        requirement.id,
        requirement.title
    )