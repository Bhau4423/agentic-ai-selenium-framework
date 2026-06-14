from pydantic import BaseModel

from models.requirement_model import Requirement
from models.acceptance_criteria_model import AcceptanceCriteria
from models.scenario_model import TestScenario


class RequirementAnalysisResult(BaseModel):

    requirements: list[Requirement]

    acceptance_criteria: list[AcceptanceCriteria]

    positive_scenarios: list[TestScenario]

    negative_scenarios: list[TestScenario]

    boundary_scenarios: list[TestScenario]