# models/requirement_analysis_result.py

from pydantic import BaseModel

from models.requirement_model import Requirement
from models.acceptance_criteria_model import AcceptanceCriteria
from models.scenario_model import TestScenario
from models.application_url_model import (
    ApplicationUrl
)


class RequirementAnalysisResult(BaseModel):

    base_url: str | None = None

    application_urls: list[
        ApplicationUrl
    ] = []

    requirements: list[
        Requirement
    ]

    acceptance_criteria: list[
        AcceptanceCriteria
    ]

    positive_scenarios: list[
        TestScenario
    ]

    negative_scenarios: list[
        TestScenario
    ]

    boundary_scenarios: list[
        TestScenario
    ]